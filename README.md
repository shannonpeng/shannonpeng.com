# Personal Website
## [https://shannonpeng.com](https://shannonpeng.com)

My personal website, built in January 2019.

To run the server locally:

Install less and less-watch-compiler (I have it installed globally):
```
npm install -g less
npm install -g less-watch-compiler
```
Set up virtualenv:
```
python3 -m venv venv
```
Activate venv, install Python packages, and then deactivate:
```
source venv/bin/activate
pip install -r requirements.txt
deactivate
```
Then, run:
```
source venv/bin/activate
less-watch-compiler app/static/styles/less app/static/styles main.less &
flask run
```
© 2020 Shannon Peng, All rights reserved.