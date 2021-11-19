source venv/bin/activate
less-watch-compiler app/static/styles/less app/static/styles main.less &
flask run