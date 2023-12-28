#!/bin/sh

# Variables
GROUP="ansible"
GROUPID=10000
USER="ope"
USERID=10001
PASSWORD="hoge"
BASTIONIP="192.168.50.222"
SSHPATH="/home/${USER}/.ssh"
AUTHFILE="authorized_keys"
SSHKEY=""

 create_group() {
   if getent group ${GROUP} > /dev/null 2>&1; then
     echo "${GROUP} is already exists."
   else
     groupadd -g ${GROUPID} ${GROUP} > /dev/null 2>&1
     if [ $? -eq 0 ]; then
       echo "${GROUP} is create."
     else
       echo "${GROUP} is not create: error code ${$?}"
       exit 8
     fi
   fi
 }

 create_user() {
   if getent passwd ${USER} > /dev/null 2>&1; then
     echo "${USER} is already exists."
   else
     useradd -u ${USERID} -g ${GROUP} ${USER} > /dev/null 2>&1
     echo "${USER}:${PASSWORD}" | chpasswd > /dev/null 2>&1
     if getent passwd ${USER} > /dev/null 2>&1; then
       echo "${USER} is create."
     else
       echo "${USER} is not create: error code ${$?}"
       exit 8
     fi
   fi
 }

 create_ssh_key() {
   if install -o ${USER} -g ${GROUP} -m 700 -d /home/${USER}/.ssh; then
     echo "Directory created successfully"
   else
     echo "Failed to create directory"
     exit 8
   fi
   if echo ${SSHKEY} > "${SSHPATH}/${AUTHFILE}" && chmod 400 "${SSHPATH}/${AUTHFILE}" && chown ${USER}:${GROUP} "${SSHPATH}/${AUTHFILE}"; then
     echo "SSH key file created and permissions set successfully"
   else
     echo "Failed to create SSH key file or set permissions"
     exit 8
   fi
 }

 setup_sudoers() {
   if grep ${GROUP} /etc/sudoers.d/${GROUP} > /dev/null 2>&1; then
     echo "${GROUP} already exists in sudoers."
   else
     echo "%${GROUP} ALL = (ALL:ALL) NOPASSWD:ALL" >> /etc/sudoers.d/${GROUP}
     if grep ${GROUP} /etc/sudoers.d/${GROUP} > /dev/null 2>&1; then
       chmod 0400 /etc/sudoers.d/${GROUP}
       echo "Sudoers file setup for ${GROUP} completed."
     else
       echo "Failed to setup sudoers file for ${GROUP}."
       exit 8
     fi
   fi
 }

create_group
create_user
create_ssh_key
setup_sudoers

exit 0
