#!/usr/bin/env python3

# Variables
GROUP = "ansible"
GROUPID = 10000
USER = "ope"
USERID = 10001
PASSWORD = "hoge"
SSHPATH = f"/home/{USER}/.ssh"
AUTHFILE = "authorized_keys"
SSHKEY = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDMYerZGYckhDVRLsut2yYiJmMyNbYZAkK8wjLrZI+3rxLEvLcK1PVqlThIfuKTQ6dsweWK2Trpbk7zcXXzlTxKyaxxkpTpigKZ0Tkn0rQ+qs1IT0vu+WjV6kTxuKPmxZ10rk9fS7AMawTUhHlS2JjgMKK+tQGxBsVvEJHQ+B45igI1h6E6wc0ccc89i8DHoSey+oX1+XrrA9v2YkOS2FZCHSf3dmUxd8L2yOZ9gvDH8RaJLriCSoMGfMpO5ki5aIwaB0fel5yshrDJoHyxFzZ/Cx7rRn4yfDXt0IWGMUBxv50ZmAnVWZIIuDV3y7lQALw4z4JFK7/POFxmQI64L7PRSMCrm2kVoxbZdxWNXCxkSm3vGxxC4N7gxQ5blfNPth7kYGuIqe15zKXOfHOJukqpsoK0Ln9gZAnE7UZ3+bSZf09i+SG4RDf4o7VQbxndIdfcEnEyskTLsAqTCTIfQusJ1T1Ub3r4YU9o4mfBwMLxe8OJg19j1RowHtuUt+ZQH/8= ope@bastion"

import os
import grp
import pwd
import subprocess

def create_group():
    try:
        grp.getgrnam(GROUP)
        print(f"{GROUP} is already exists.")
    except KeyError:
        subprocess.run(["groupadd", "-g", str(GROUPID), GROUP], check=True)
        print(f"{GROUP} is created.")

def create_user():
    try:
        pwd.getpwnam(USER)
        print(f"{USER} is already exists.")
    except KeyError:
        subprocess.run(["useradd", "-u", str(USERID), "-g", GROUP, USER], check=True)
        subprocess.run(["chpasswd"], input=f"{USER}:{PASSWORD}", text=True, check=True)
        print(f"{USER} is created.")

def create_ssh_key():
    os.makedirs(SSHPATH, mode=0o700, exist_ok=True)
    with open(f"{SSHPATH}/{AUTHFILE}", "w") as f:
        f.write(SSHKEY)
    os.chmod(f"{SSHPATH}/{AUTHFILE}", 0o400)
    os.chown(f"{SSHPATH}/{AUTHFILE}", pwd.getpwnam(USER).pw_uid, grp.getgrnam(GROUP).gr_gid)

def setup_sudoers():
    sudoers_file = f"/etc/sudoers.d/{GROUP}"
    if not os.path.exists(sudoers_file):
        with open(sudoers_file, "w") as f:
            f.write(f"%{GROUP} ALL = (ALL:ALL) NOPASSWD:ALL")
            os.chmod(sudoers_file, 0o400)
    else:
        with open(sudoers_file, "a+") as f:
            if GROUP in f.read():
                print(f"{GROUP} already exists in sudoers.")
            else:
                f.write(f"%{GROUP} ALL = (ALL:ALL) NOPASSWD:ALL")
                os.chmod(sudoers_file, 0o400)

if __name__ == "__main__":
    create_group()
    create_user()
    create_ssh_key()
    setup_sudoers()

