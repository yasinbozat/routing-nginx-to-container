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

<h2>
  <a name="create-the-first-application" href="#create-the-first-application">
  </a>
  Create the first application
</h2>

<p>I just created a very basic nodeJs application. The app.js looks like the following<br>
</p>

<div class="highlight js-code-highlight">
<pre class="highlight javascript"><code><span class="kd">var</span> <span class="nx">express</span> <span class="o">=</span> <span class="nx">require</span><span class="p">(</span><span class="dl">"</span><span class="s2">express</span><span class="dl">"</span><span class="p">);</span>
<span class="kd">var</span> <span class="nx">app</span> <span class="o">=</span> <span class="nx">express</span><span class="p">();</span>

<span class="nx">app</span><span class="p">.</span><span class="nx">use</span><span class="p">(</span><span class="nx">express</span><span class="p">.</span><span class="nx">json</span><span class="p">());</span>
<span class="nx">app</span><span class="p">.</span><span class="nx">use</span><span class="p">(</span><span class="nx">express</span><span class="p">.</span><span class="nx">urlencoded</span><span class="p">({</span> <span class="na">extended</span><span class="p">:</span> <span class="kc">false</span> <span class="p">}));</span>

<span class="nx">app</span><span class="p">.</span><span class="kd">get</span><span class="p">(</span><span class="dl">"</span><span class="s2">/app-first</span><span class="dl">"</span><span class="p">,</span> <span class="kd">function</span> <span class="p">(</span><span class="nx">req</span><span class="p">,</span> <span class="nx">res</span><span class="p">,</span> <span class="nx">next</span><span class="p">)</span> <span class="p">{</span>
  <span class="nx">res</span><span class="p">.</span><span class="nx">send</span><span class="p">({</span> <span class="na">title</span><span class="p">:</span> <span class="dl">"</span><span class="s2">Express</span><span class="dl">"</span><span class="p">,</span> <span class="na">application</span><span class="p">:</span> <span class="dl">"</span><span class="s2">Application 1</span><span class="dl">"</span> <span class="p">});</span>
<span class="p">});</span>

<span class="nx">app</span><span class="p">.</span><span class="nx">listen</span><span class="p">(</span><span class="mi">3000</span><span class="p">,</span> <span class="p">()</span> <span class="o">=&gt;</span> <span class="nx">console</span><span class="p">.</span><span class="nx">log</span><span class="p">(</span><span class="dl">"</span><span class="s2">Running on http://localhost:3000</span><span class="dl">"</span><span class="p">));</span>
</code></pre>
<div class="highlight__panel js-actions-panel">
<div class="highlight__panel-action js-fullscreen-code-action">
    <svg xmlns="http://www.w3.org/2000/svg" width="20px" height="20px" viewbox="0 0 24 24" class="highlight-action crayons-icon highlight-action--fullscreen-on"><title>Enter fullscreen mode</title>
    <path d="M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z"></path>
</svg>

    <svg xmlns="http://www.w3.org/2000/svg" width="20px" height="20px" viewbox="0 0 24 24" class="highlight-action crayons-icon highlight-action--fullscreen-off"><title>Exit fullscreen mode</title>
    <path d="M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z"></path>
</svg>

</div>
</div>
</div>



<p>The package.json looks like the following<br>
</p>

<div class="highlight js-code-highlight">
<pre class="highlight javascript"><code><span class="p">{</span>
  <span class="dl">"</span><span class="s2">name</span><span class="dl">"</span><span class="p">:</span> <span class="dl">"</span><span class="s2">express-with-env</span><span class="dl">"</span><span class="p">,</span>
  <span class="dl">"</span><span class="s2">version</span><span class="dl">"</span><span class="p">:</span> <span class="dl">"</span><span class="s2">0.0.0</span><span class="dl">"</span><span class="p">,</span>
  <span class="dl">"</span><span class="s2">private</span><span class="dl">"</span><span class="p">:</span> <span class="kc">true</span><span class="p">,</span>
  <span class="dl">"</span><span class="s2">scripts</span><span class="dl">"</span><span class="p">:</span> <span class="p">{</span>
    <span class="dl">"</span><span class="s2">start</span><span class="dl">"</span><span class="p">:</span> <span class="dl">"</span><span class="s2">node app.js</span><span class="dl">"</span>
  <span class="p">},</span>
  <span class="dl">"</span><span class="s2">dependencies</span><span class="dl">"</span><span class="p">:</span> <span class="p">{</span>
    <span class="dl">"</span><span class="s2">express</span><span class="dl">"</span><span class="p">:</span> <span class="dl">"</span><span class="s2">~4.16.1</span><span class="dl">"</span>
  <span class="p">}</span>
<span class="p">}</span>
</code></pre>
<div class="highlight__panel js-actions-panel">
<div class="highlight__panel-action js-fullscreen-code-action">
    <svg xmlns="http://www.w3.org/2000/svg" width="20px" height="20px" viewbox="0 0 24 24" class="highlight-action crayons-icon highlight-action--fullscreen-on"><title>Enter fullscreen mode</title>
    <path d="M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z"></path>
</svg>

    <svg xmlns="http://www.w3.org/2000/svg" width="20px" height="20px" viewbox="0 0 24 24" class="highlight-action crayons-icon highlight-action--fullscreen-off"><title>Exit fullscreen mode</title>
    <path d="M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z"></path>
</svg>

</div>
</div>
</div>



<p>and in parallel to these, the Dockerfile looks like the following<br>
</p>

<div class="highlight js-code-highlight">
<pre class="highlight docker"><code><span class="k">FROM</span><span class="s"> node:12-slim</span>
<span class="k">WORKDIR</span><span class="s"> /app</span>
<span class="k">COPY</span><span class="s"> ./package*.json ./</span>
<span class="k">RUN </span>npm <span class="nb">install</span>
<span class="k">COPY</span><span class="s"> ./ ./</span>
<span class="k">EXPOSE</span><span class="s"> 3000</span>

<span class="c"># Run the code</span>
<span class="k">CMD</span><span class="s"> [ "npm", "start" ]</span>
</code></pre>
<div class="highlight__panel js-actions-panel">
<div class="highlight__panel-action js-fullscreen-code-action">
    <svg xmlns="http://www.w3.org/2000/svg" width="20px" height="20px" viewbox="0 0 24 24" class="highlight-action crayons-icon highlight-action--fullscreen-on"><title>Enter fullscreen mode</title>
    <path d="M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z"></path>
</svg>

    <svg xmlns="http://www.w3.org/2000/svg" width="20px" height="20px" viewbox="0 0 24 24" class="highlight-action crayons-icon highlight-action--fullscreen-off"><title>Exit fullscreen mode</title>
    <path d="M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z"></path>
</svg>

</div>
</div>
</div>



<h2>
  <a name="create-the-second-application" href="#create-the-second-application">
  </a>
  Create the second application
</h2>

<p>The second application is exactly like the first application, except, it runs on PORT 4000, and exposes path <code>/app-second</code>. the app.js looks like the following<br>
</p>

<div class="highlight js-code-highlight">
<pre class="highlight javascript"><code><span class="kd">var</span> <span class="nx">express</span> <span class="o">=</span> <span class="nx">require</span><span class="p">(</span><span class="dl">"</span><span class="s2">express</span><span class="dl">"</span><span class="p">);</span>
<span class="kd">var</span> <span class="nx">app</span> <span class="o">=</span> <span class="nx">express</span><span class="p">();</span>

<span class="nx">app</span><span class="p">.</span><span class="nx">use</span><span class="p">(</span><span class="nx">express</span><span class="p">.</span><span class="nx">json</span><span class="p">());</span>
<span class="nx">app</span><span class="p">.</span><span class="nx">use</span><span class="p">(</span><span class="nx">express</span><span class="p">.</span><span class="nx">urlencoded</span><span class="p">({</span> <span class="na">extended</span><span class="p">:</span> <span class="kc">false</span> <span class="p">}));</span>

<span class="nx">app</span><span class="p">.</span><span class="kd">get</span><span class="p">(</span><span class="dl">"</span><span class="s2">/app-second</span><span class="dl">"</span><span class="p">,</span> <span class="kd">function</span> <span class="p">(</span><span class="nx">req</span><span class="p">,</span> <span class="nx">res</span><span class="p">,</span> <span class="nx">next</span><span class="p">)</span> <span class="p">{</span>
  <span class="nx">res</span><span class="p">.</span><span class="nx">send</span><span class="p">({</span> <span class="na">title</span><span class="p">:</span> <span class="dl">"</span><span class="s2">Express</span><span class="dl">"</span><span class="p">,</span> <span class="na">application</span><span class="p">:</span> <span class="dl">"</span><span class="s2">Application 2</span><span class="dl">"</span> <span class="p">});</span>
<span class="p">});</span>
<span class="nx">app</span><span class="p">.</span><span class="nx">listen</span><span class="p">(</span><span class="mi">4000</span><span class="p">,</span> <span class="p">()</span> <span class="o">=&gt;</span> <span class="nx">console</span><span class="p">.</span><span class="nx">log</span><span class="p">(</span><span class="dl">"</span><span class="s2">Running on http://localhost:4000</span><span class="dl">"</span><span class="p">));</span>
</code></pre>
<div class="highlight__panel js-actions-panel">
<div class="highlight__panel-action js-fullscreen-code-action">
    <svg xmlns="http://www.w3.org/2000/svg" width="20px" height="20px" viewbox="0 0 24 24" class="highlight-action crayons-icon highlight-action--fullscreen-on"><title>Enter fullscreen mode</title>
    <path d="M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z"></path>
</svg>

    <svg xmlns="http://www.w3.org/2000/svg" width="20px" height="20px" viewbox="0 0 24 24" class="highlight-action crayons-icon highlight-action--fullscreen-off"><title>Exit fullscreen mode</title>
    <path d="M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z"></path>
</svg>

</div>
</div>
</div>



<p>and the Dockerfile looks like the following<br>
</p>

<div class="highlight js-code-highlight">
<pre class="highlight plaintext"><code>FROM node:12-slim
WORKDIR /app
COPY ./package*.json ./
RUN npm install
COPY ./ ./
EXPOSE 4000

# Run the code
CMD [ "npm", "start" ]
</code></pre>
<div class="highlight__panel js-actions-panel">
<div class="highlight__panel-action js-fullscreen-code-action">
    <svg xmlns="http://www.w3.org/2000/svg" width="20px" height="20px" viewbox="0 0 24 24" class="highlight-action crayons-icon highlight-action--fullscreen-on"><title>Enter fullscreen mode</title>
    <path d="M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z"></path>
</svg>

    <svg xmlns="http://www.w3.org/2000/svg" width="20px" height="20px" viewbox="0 0 24 24" class="highlight-action crayons-icon highlight-action--fullscreen-off"><title>Exit fullscreen mode</title>
    <path d="M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z"></path>
</svg>

</div>
</div>
</div>



<p>The packageJSON looks exactly like the first application</p>

<h2>
  <a name="create-the-nginx-config" href="#create-the-nginx-config">
  </a>
  Create the nginx config
</h2>

<p>Go to the nginx-docker directory and create nginx.conf file<br>
</p>

<div class="highlight js-code-highlight">
<pre class="highlight nginx"><code><span class="k">upstream</span> <span class="s">first-app</span> <span class="p">{</span>
    <span class="kn">server</span> <span class="nf">172.17.0.1</span><span class="p">:</span><span class="mi">3000</span> <span class="s">weight=1</span><span class="p">;</span>
<span class="p">}</span>

<span class="k">upstream</span> <span class="s">second-app</span> <span class="p">{</span>
    <span class="kn">server</span> <span class="nf">172.17.0.1</span><span class="p">:</span><span class="mi">4000</span> <span class="s">weight=1</span><span class="p">;</span>
<span class="p">}</span>

<span class="k">server</span> <span class="p">{</span>

  <span class="kn">location</span> <span class="n">/app-first</span> <span class="p">{</span>
    <span class="kn">proxy_set_header</span> <span class="s">X-Forwarded-Host</span> <span class="nv">$host</span><span class="p">:</span><span class="nv">$server_port</span><span class="p">;</span>
    <span class="kn">proxy_set_header</span> <span class="s">X-Forwarded-Server</span> <span class="nv">$host</span><span class="p">;</span>
    <span class="kn">proxy_set_header</span> <span class="s">X-Forwarded-For</span> <span class="nv">$proxy_add_x_forwarded_for</span><span class="p">;</span>
    <span class="kn">proxy_pass</span> <span class="s">http://first-app</span><span class="p">;</span>
  <span class="p">}</span>

  <span class="kn">location</span> <span class="n">/app-second</span> <span class="p">{</span>
    <span class="kn">proxy_set_header</span> <span class="s">X-Forwarded-Host</span> <span class="nv">$host</span><span class="p">:</span><span class="nv">$server_port</span><span class="p">;</span>
    <span class="kn">proxy_set_header</span> <span class="s">X-Forwarded-Server</span> <span class="nv">$host</span><span class="p">;</span>
    <span class="kn">proxy_set_header</span> <span class="s">X-Forwarded-For</span> <span class="nv">$proxy_add_x_forwarded_for</span><span class="p">;</span>
    <span class="kn">proxy_pass</span> <span class="s">http://second-app</span><span class="p">;</span>
  <span class="p">}</span>

<span class="p">}</span>
</code></pre>
<div class="highlight__panel js-actions-panel">
<div class="highlight__panel-action js-fullscreen-code-action">
    <svg xmlns="http://www.w3.org/2000/svg" width="20px" height="20px" viewbox="0 0 24 24" class="highlight-action crayons-icon highlight-action--fullscreen-on"><title>Enter fullscreen mode</title>
    <path d="M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z"></path>
</svg>

    <svg xmlns="http://www.w3.org/2000/svg" width="20px" height="20px" viewbox="0 0 24 24" class="highlight-action crayons-icon highlight-action--fullscreen-off"><title>Exit fullscreen mode</title>
    <path d="M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z"></path>
</svg>

</div>
</div>
</div>



<p>Create a dockerfile for the nginx and here's what it looks like<br>
</p>

<div class="highlight js-code-highlight">
<pre class="highlight docker"><code><span class="k">FROM</span><span class="s"> nginx</span>
<span class="k">RUN </span><span class="nb">rm</span> /etc/nginx/conf.d/default.conf
<span class="k">COPY</span><span class="s"> nginx.conf /etc/nginx/conf.d/default.conf</span>
</code></pre>
<div class="highlight__panel js-actions-panel">
<div class="highlight__panel-action js-fullscreen-code-action">
    <svg xmlns="http://www.w3.org/2000/svg" width="20px" height="20px" viewbox="0 0 24 24" class="highlight-action crayons-icon highlight-action--fullscreen-on"><title>Enter fullscreen mode</title>
    <path d="M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z"></path>
</svg>

    <svg xmlns="http://www.w3.org/2000/svg" width="20px" height="20px" viewbox="0 0 24 24" class="highlight-action crayons-icon highlight-action--fullscreen-off"><title>Exit fullscreen mode</title>
    <path d="M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z"></path>
</svg>

</div>
</div>
</div>



<h2>
  <a name="create-the-images-and-run-the-containers" href="#create-the-images-and-run-the-containers">
  </a>
  Create the images and run the containers
</h2>

<p>Go to <code>first-app</code> directory and build the image<br>
</p>

<div class="highlight js-code-highlight">
<pre class="highlight shell"><code><span class="nb">sudo </span>docker build <span class="nt">-t</span> first-app <span class="nb">.</span>
</code></pre>
<div class="highlight__panel js-actions-panel">
<div class="highlight__panel-action js-fullscreen-code-action">
    <svg xmlns="http://www.w3.org/2000/svg" width="20px" height="20px" viewbox="0 0 24 24" class="highlight-action crayons-icon highlight-action--fullscreen-on"><title>Enter fullscreen mode</title>
    <path d="M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z"></path>
</svg>

    <svg xmlns="http://www.w3.org/2000/svg" width="20px" height="20px" viewbox="0 0 24 24" class="highlight-action crayons-icon highlight-action--fullscreen-off"><title>Exit fullscreen mode</title>
    <path d="M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z"></path>
</svg>

</div>
</div>
</div>



<p>Go to the second-app directory and build the image<br>
</p>

<div class="highlight js-code-highlight">
<pre class="highlight shell"><code><span class="nb">sudo </span>docker build <span class="nt">-t</span> second-app <span class="nb">.</span>
</code></pre>
<div class="highlight__panel js-actions-panel">
<div class="highlight__panel-action js-fullscreen-code-action">
    <svg xmlns="http://www.w3.org/2000/svg" width="20px" height="20px" viewbox="0 0 24 24" class="highlight-action crayons-icon highlight-action--fullscreen-on"><title>Enter fullscreen mode</title>
    <path d="M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z"></path>
</svg>

    <svg xmlns="http://www.w3.org/2000/svg" width="20px" height="20px" viewbox="0 0 24 24" class="highlight-action crayons-icon highlight-action--fullscreen-off"><title>Exit fullscreen mode</title>
    <path d="M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z"></path>
</svg>

</div>
</div>
</div>



<p>Run the images now<br>
</p>

<div class="highlight js-code-highlight">
<pre class="highlight shell"><code><span class="nb">sudo </span>docker run <span class="nt">-p</span> 3000:3000 <span class="nt">-d</span> first-app
<span class="nb">sudo </span>docker run <span class="nt">-p</span> 4000:4000 <span class="nt">-d</span> second-app
</code></pre>
<div class="highlight__panel js-actions-panel">
<div class="highlight__panel-action js-fullscreen-code-action">
    <svg xmlns="http://www.w3.org/2000/svg" width="20px" height="20px" viewbox="0 0 24 24" class="highlight-action crayons-icon highlight-action--fullscreen-on"><title>Enter fullscreen mode</title>
    <path d="M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z"></path>
</svg>

    <svg xmlns="http://www.w3.org/2000/svg" width="20px" height="20px" viewbox="0 0 24 24" class="highlight-action crayons-icon highlight-action--fullscreen-off"><title>Exit fullscreen mode</title>
    <path d="M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z"></path>
</svg>

</div>
</div>
</div>



<p>Now, if you open <a href="http://localhost:3000/app-first">http://localhost:3000/app-first</a> in browser, you should get the following JSON<br>
</p>

<div class="highlight js-code-highlight">
<pre class="highlight plaintext"><code>{
"title": "Express",
"application": "Application 1"
}
</code></pre>
<div class="highlight__panel js-actions-panel">
<div class="highlight__panel-action js-fullscreen-code-action">
    <svg xmlns="http://www.w3.org/2000/svg" width="20px" height="20px" viewbox="0 0 24 24" class="highlight-action crayons-icon highlight-action--fullscreen-on"><title>Enter fullscreen mode</title>
    <path d="M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z"></path>
</svg>

    <svg xmlns="http://www.w3.org/2000/svg" width="20px" height="20px" viewbox="0 0 24 24" class="highlight-action crayons-icon highlight-action--fullscreen-off"><title>Exit fullscreen mode</title>
    <path d="M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z"></path>
</svg>

</div>
</div>
</div>



<p>and by opening <a href="http://localhost:4000/app-second">http://localhost:4000/app-second</a>, you should get<br>
</p>

<div class="highlight js-code-highlight">
<pre class="highlight plaintext"><code>{
"title": "Express",
"application": "Application 2"
}
</code></pre>
<div class="highlight__panel js-actions-panel">
<div class="highlight__panel-action js-fullscreen-code-action">
    <svg xmlns="http://www.w3.org/2000/svg" width="20px" height="20px" viewbox="0 0 24 24" class="highlight-action crayons-icon highlight-action--fullscreen-on"><title>Enter fullscreen mode</title>
    <path d="M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z"></path>
</svg>

    <svg xmlns="http://www.w3.org/2000/svg" width="20px" height="20px" viewbox="0 0 24 24" class="highlight-action crayons-icon highlight-action--fullscreen-off"><title>Exit fullscreen mode</title>
    <path d="M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z"></path>
</svg>

</div>
</div>
</div>



<p>You see, the applications are running in different ports. Your target is to expose them both in the same port. </p>

<p>Go to the nginx-docker directory and build the nginx image and run it.<br>
</p>

<div class="highlight js-code-highlight">
<pre class="highlight plaintext"><code>sudo docker build -t nginx-proxy .
sudo docker run -p 8000:80 -d nginx-proxy
</code></pre>
<div class="highlight__panel js-actions-panel">
<div class="highlight__panel-action js-fullscreen-code-action">
    <svg xmlns="http://www.w3.org/2000/svg" width="20px" height="20px" viewbox="0 0 24 24" class="highlight-action crayons-icon highlight-action--fullscreen-on"><title>Enter fullscreen mode</title>
    <path d="M16 3h6v6h-2V5h-4V3zM2 3h6v2H4v4H2V3zm18 16v-4h2v6h-6v-2h4zM4 19h4v2H2v-6h2v4z"></path>
</svg>

    <svg xmlns="http://www.w3.org/2000/svg" width="20px" height="20px" viewbox="0 0 24 24" class="highlight-action crayons-icon highlight-action--fullscreen-off"><title>Exit fullscreen mode</title>
    <path d="M18 7h4v2h-6V3h2v4zM8 9H2V7h4V3h2v6zm10 8v4h-2v-6h6v2h-4zM8 15v6H6v-4H2v-2h6z"></path>
</svg>

</div>
</div>
</div>



<p>Now you'll be able to see both the applications running in port 8000, as </p>

<ul>
<li><a href="http://localhost:8000/app-second">http://localhost:8000/app-second</a></li>
<li><a href="http://localhost:8000/app-first">http://localhost:8000/app-first</a></li>
</ul>



