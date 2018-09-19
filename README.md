# URLinfo

## Install
* install python
* install pip
* install redis

## clone the repository
git clone https://github.com/virtualanuj/urlinfo.git


> **This is real malware data. Please don't naviage to the urls on your system. You may infect your machine.**


## seed data
* redis-server
* cat data.txt | redis-cli --pipe

## run
* redis-server
* python urlinfo.py

> **This is real malware data. Please don't naviage to the urls on your system. You may infect your machine.**

## test
* http://localhost:5000/
* http://localhost:5000/urlinfo/1/www.frosinonewesternshow.it/fws2011/7tappa.htm
* http://localhost:5000/urlinfo/1/grendizer.biz/Informazioni/statistiche.zip

## cli performance test
> ab -k -n 5000 http://127.0.0.1:5000/urlinfo/1/www.frosinonewesternshow.it/fws2011/7tappa.htm
