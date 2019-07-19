# beautifulsoup_sample
A BeautifulSoap sample project

## Prerequisite

* To install virtualenv
```bash
sudo pip install virtualenv
```
* To make an environment
```bash
virtualenv -p python3 [env_name]
```
* Enable the environment
```bash
source [env_name]/bin/activate
```
* Disable the environment
```bash
deactivate
```
* Install dependencies
```bash
pip install -r requirements.txt
```

## Deploy

In this project, I use Heroku.com

### Prerequisite

* Install Heroku CLI

```bash
brew install heroku/brew/heroku
```

### Deploy

* Before to deploy, test on local machine

```bash
heroku local web
```

* Deploy to Heroku server \
  To deploy, push to Heroku git server

```bash
git push heroku master
```

* Get the log tails

```bash
heroku logs --tail
```

* Access URL: https://fb-reverser.herokuapp.com/