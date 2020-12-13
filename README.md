# Fastapi Web Starter

You can find the Medium article at [https://shinichiokada.medium.com/](https://shinichiokada.medium.com/).

This includes all the file ready to deploy to Heroku. 

- .env
- .gitignore
- app
- Procfile
- README.md
- requirements.txt
- runtime.txt
- static
- templates

## Installation

```
# unzip
$ unzip fastapi-web-starter.zip
# change the directory
$ cd fastapi-web-starter.zip
# install packages
$ pip install -r requirements.txt
# start the server
$ uvicorn app.main:app --reload --port 8080
```

Visit http://127.0.0.1:8080/.

![Starting](./images/image-1.png)





