# Fastapi Web Starter

Updated: 2022-01-18

[https://shinichiokada.medium.com/](https://shinichiokada.medium.com/) ([Building a Website Starter with FastAPI](https://levelup.gitconnected.com/building-a-website-starter-with-fastapi-92d077092864)).

## Overview

A static simple website ready to deploy.
This repo includes all the file and it is ready to deploy to Heroku.
[How to Deploy a FastAPI App on Heroku for Free](https://towardsdatascience.com/how-to-deploy-your-fastapi-app-on-heroku-for-free-8d4271a4ab9)

- .env
- .gitignore
- app
- Procfile
- README.md
- requirements.txt
- runtime.txt
- static
- templates

## Requirement

See requirements.txt for updates.

```sh
requests==2.27.1
fastapi==0.72.0
uvicorn==0.17.0
python-dotenv==0.19.2
aiofiles==0.8.0
python-multipart==0.0.5
jinja2==3.0.3
Markdown==3.3.6
pytest==6.2.5
```

## Installation & Usage

```bash
$ git clone git@github.com:shinokada/fastapi-web-starter.git
$ cd fastapi-web-starter
# install packages
$ pip install -r requirements.txt
# start the server
$ uvicorn app.main:app --reload --port 8080
```

Visit [http://127.0.0.1:8080/](http://127.0.0.1:8080/).

![Starting](./images/image-1.png)

## Features

- Menu
- Unsplash
- Accordion
- Markdown pages

## Test

All tests are under `tests` directory.

```bash
# Change the directory
$ cd fastapi-web-starter
# Run tests
$ pytest -v
```

## Author

[twitter](https://twitter.com/shinokada)

## Licence

【MIT License】

Copyright 2021 Shinichi Okada

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
