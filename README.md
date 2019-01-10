# shannonpeng.com
new personal website :o

to run locally:

install less and less-watch-compiler (I have it installed globally):
```
npm install -g less
npm install -g less-watch-compiler
```
set up virtualenv:
```
python3 -m venv venv
```
activate venv, install python packages, and deactivate:
```
source venv/bin/activate
pip install -r requirements.txt
deactivate
```
then run the start script:
```
sh start.sh
```