
# Client
## OS
### firewalld
IPは変えること
```
firewall-cmd --permanent --zone=public --add-rich-rule="rule family="ipv4" source address="192.168.50.88" port protocol="tcp" port="22" accept"
firewall-cmd --add-port=7946/udp --zone=public
firewall-cmd --add-port=7946/tcp --zone=public
firewall-cmd --runtime-to-permanent
```
### user
```
useradd tsubame
usermod -G wheel tsubame
install  -m 700  -d ~/.ssh
install -m 400 ~/.ssh/authorized_keys
cat << EOF | ~/.ssh/authorized_keys
ansibleサーバの公開鍵を設定
visudo
```

```
passwd tsubame
```

# ansible server 
## OS
### firewall
```
```

## Anyenv
### Install

```
git clone https://github.com/anyenv/anyenv ~/.anyenv
echo 'export PATH="$HOME/.anyenv/bin:$PATH"' >> ~/.bash_profile
source  ~/.bash_profile
```

#### init
```
anyenv init
echo 'eval "$(anyenv init -)"' >> ~/.bash_profile
anyenv install --init
```

## pyenv
### install
```
anyenv install pyenv
source  ~/.bash_profile
```

## pytion
### install
- バージョンはリストで表示されたものから選択
```
pyenv install --list
pyenv install 3.11.5
```

### choose python version
```
pyenv versions
pyenv local 3.11.5
python --version
```

## pip
### install
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
which pip
```

## ansible
### install
```
pip install ansible
which ansible```


