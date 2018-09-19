# URLinfo

## Install
### install python
### install pip
### install redis

## clone the repository
git clone https://github.com/virtualanuj/urlinfo.git

## seed data
cat data.txt | redis-cli --pipe

# run
redis-server
python urlinfo.py

# test
http://localhost:5000/
http://localhost:5000/urlinfo/1/www.frosinonewesternshow.it/fws2011/7tappa.htm
http://localhost:5000/urlinfo/1/grendizer.biz/Informazioni/statistiche.zip

