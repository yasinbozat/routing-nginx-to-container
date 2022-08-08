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
<div class="highlight__panel js-actions-panel">
<div class="highlight__panel-action js-fullscreen-code-action">
    <svg xmlns="http://www.w3.org/2000/svg" width="20px" height="20px" viewBox="0 0 24 24" class="highlight-action crayons-icon highlight-action--fullscreen-on"><title>Enter fullscreen mode</title>
    <path d="M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z"></path>
</svg>

    <svg xmlns="http://www.w3.org/2000/svg" width="20px" height="20px" viewBox="0 0 24 24" class="highlight-action crayons-icon highlight-action--fullscreen-off"><title>Exit fullscreen mode</title>
    <path d="M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z"></path>
</svg>

</div>
</div>
</div>


folder: ./service1/ 
```
docker build -t service1 .
```
