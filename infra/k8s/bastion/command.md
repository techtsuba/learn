
# Setup
## OS
### User
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