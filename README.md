<h1 align="left">Routing Nginx to Microservices (Containers)</h1>

###

<p align="left">Routing the web pages with nginx and gunicorn in Docker.</p>

###

<div align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" height="40" width="52" alt="docker logo"  />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg" height="40" width="52" alt="flask logo"  />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="40" width="52" alt="python logo"  />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nginx/nginx-original.svg" height="40" width="52" alt="nginx logo"  />
</div>

###

<h2>
  <a name="create-the-directories" href="#create-the-directories">
  </a>
  Create the directories
</h2>

<div class="highlight js-code-highlight">
<pre class="highlight shell"><code><span class="nb">mkdir </span>first-app
<span class="nb">mkdir </span>second-app
<span class="nb">mkdir </span>nginx-docker
</code></pre>


</div>
</div>
</div>


folder: ./service1/ 
```
docker build -t service1 .
```
