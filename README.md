<h1 align="left">Routing Requests to Container With Nginx (Gunicorn, Flask)</h1>

###

Routing the web pages with nginx and gunicorn in Docker. Will be applications running in diffrent  ports and i will show how to running in same port. 

###

<div align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" height="40" width="52" alt="docker logo"  />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="40" width="52" alt="python logo"  />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nginx/nginx-original.svg" height="40" width="52" alt="nginx logo"  />
  <img src="https://upload.wikimedia.org/wikipedia/commons/0/00/Gunicorn_logo_2010.svg" height="40" width="100" alt="nginx logo"  />	
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg" height="40" width="52" alt="flask logo"  />
	
</div>

###

<br>

### Create the directories
```
mkdir service1
mkdir service2
mkdir web-service
```

### Create the first application
#### I just created a very basic python application. The app.py looks like the following

```
from flask import Flask

app = Flask(__name__)

@app.route("/service1")
def main():
    return "service1"

if __name__ == '__main__':
    app.run(debug=True,port=3000)
```

#### requirements.txt looks like the following

```
Flask
gunicorn
```

#### and Dockerfile looks like the following
```
FROM python:3.10-buster
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
#EXPOSE 3000
CMD ["gunicorn", "--bind", "0.0.0.0:3000", "app:app"]
```

### Create the second application
#### The second application is exactly like the first application, except, it runs on PORT 4000, and exposes path /service2. the app.js looks like the following
```
from flask import Flask

app = Flask(__name__)

@app.route("/service2")
def main():
    return "service2"

if __name__ == '__main__':
    app.run(debug=True,port=4000)
```

```
FROM python:3.10-buster
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 4000
CMD ["gunicorn", "--bind", "0.0.0.0:4000", "app:app"]
```

```
Flask
gunicorn
```

### Create the nginx config
#### Go to the nginx-docker directory and create nginx.conf file
```
upstream service1 {
    server 172.17.0.1:3000 weight=1;
}

upstream service2 {
    server 172.17.0.1:4000 weight=1;
}

server {

	listen       80;
    listen  [::]:80;
    server_name  localhost;

    #access_log  /var/log/nginx/host.access.log  main;

    location / {
        root   /usr/share/nginx/html;
        index  index.html index.htm;
    }

  location /service1 {
    proxy_set_header X-Forwarded-Host $host:$server_port;
    proxy_set_header X-Forwarded-Server $host;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_pass http://service1;
  }

  location /service2 {
    proxy_set_header X-Forwarded-Host $host:$server_port;
    proxy_set_header X-Forwarded-Server $host;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_pass http://service2;
  }

}
```

#### Create a Dockerfile for the nginx and here's what it looks like
```
FROM nginx
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/default.conf
```

### Create the images and run the containers
#### Go to service1 directory and build the image
```
docker build -t first-app .
```

#### Go to the service2 directory and build the image
```
docker build -t service2 .
```

#### Run the images now
```
docker run -p 3000:3000 -d service1
docker run -p 4000:4000 -d service2
```

#### Now, if you open http://localhost:3000/service1 in browser, you should see the following
```
This is service 1
```

#### and by opening http://localhost:4000/service2, you should get
```
This is service 2
```

#### You see, the applications are running in different ports. Your target is to expose them both in the same port.
#### Go to the nginx-docker directory and build the nginx image and run it.
```
docker build -t nginx-proxy .
docker run -p 80:80 -d nginx-proxy
```

#### Now you'll be able to see both the applications running in port 8000, as
#### http://localhost/service1
#### http://localhost/service2


