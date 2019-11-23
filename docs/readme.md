<h1 id="tweetstats">tweetStats</h1>
<p>Send a daily tweet with your Pi-Hole statistics and other system information!</p>
<h2 id="how-to-use">How to use</h2>
<h3 id="prerequisites">Prerequisites</h3>
<ul>
<li><p>Pi-hole</p>
<ul>
<li>install Pi-hole (<a href="https://install.pi-hole.net">https://install.pi-hole.net</a>) </li>
<li><code>api_path</code> = Path to <code>http://pi.hole/admin/api.php</code> of Pi-Hole (if you&#39;re running this script from the machine running Pi-hole that URL should work)</li>
</ul>
</li>
<li><p>Twitter</p>
<ul>
<li>Tokens: Create an application <a href="https://apps.twitter.com/">here</a></li>
</ul>
</li>
<li><p>speedtest-cli</p>
<ul>
<li>install speedtest-cli from your package manager</li>
<li><code>access_key</code> = get this from <a href="https://ipstack.com/signup/free">https://ipstack.com/signup/free</a></li>
</ul>
</li>
</ul>
<h3 id="guided-setup-install-script-">Guided Setup (install script)</h3>
<pre><code>wget http<span class="hljs-variable">s:</span>//raw.githubusercontent.<span class="hljs-keyword">com</span>/mwoolweaver/tweetStats/master/install.<span class="hljs-keyword">sh</span>
./install.<span class="hljs-keyword">sh</span>
</code></pre><h3 id="manual-setup-no-install-script-">Manual Setup (no install script)</h3>
<ol>
<li><code>git clone https://github.com/mwoolweaver/tweetStats.git</code></li>
<li>Install Python 3</li>
<li><code>pip3 install -U -r requirements.txt</code></li>
<li><code>cp config.json.example config.json</code> and adjust it</li>
<li>Run it! <code>python3 tweetStats.py</code> or <code>python3 tweetStats.py -h</code> for help</li>
<li>???</li>
<li>Profit</li>
</ol>
<h2 id="cmd-line-args-for-testing">cmd line args for testing</h2>
<ul>
<li><p>-db will print the tweet to be sent and all other variables that are used in the proccess.</p>
</li>
<li><p>-dbl will test your twitter credentials to test a successful login.</p>
</li>
<li><p>-dbp will make sure the pi-hole api can be reached. </p>
</li>
</ul>
<h2 id="cronjob">Cronjob</h2>
<p>test cron job w/ <code>sudo run-parts /etc/cron.daily</code></p>
<h3 id="use-install-script">Use Install Script</h3>
<p>or </p>
<h3 id="manual-setup">Manual Setup</h3>
<p>creaate file <code>/etc/cron.daily/tweetStats</code> with the following contents</p>
<pre><code><span class="hljs-meta">#!/bin/bash</span>
<span class="hljs-built_in">cd</span> /path/to/folder/containing/tweetStats.py/
python3 ./tweetStats.py &gt;&gt; tweetStats.txt
</code></pre><h1 id="how-it-looks">How it looks</h1>
<pre><code><span class="hljs-attribute">Tweet 1
#PiHoleStats
Blocklist Size</span>: 761,313
<span class="hljs-attribute">Total Queries</span>: 25,137
<span class="hljs-attribute">Queries Blocked</span>: 0|0%
<span class="hljs-attribute">Queries Forwarded</span>: 509
<span class="hljs-attribute">Queries Cached</span>: 24,628
<span class="hljs-attribute">Unique Clients</span>: 1
<span class="hljs-attribute">Privacy Level</span>: 2
<span class="hljs-attribute">Gravity Last Updated</span>: 2019-07-16 18:03
<span class="hljs-comment">#Python</span>

 Tweet 2
<span class="hljs-comment">#SystemStats</span>
<span class="hljs-attribute">CPU Load AVG</span>: 0.08, 0.02, 0.01
<span class="hljs-attribute">Ram Usage</span>: 483M/1G|39.3%
<span class="hljs-attribute">Disk Usage</span>: 9G/28G|32.14%
<span class="hljs-attribute">Network Interfaces</span>: ens4, tun0, tun1
<span class="hljs-attribute">Kernel &amp;&amp; OS</span>: Linux-5.0.0-1010-gcp-x86_64-with-Ubuntu-19.10-eoan
<span class="hljs-attribute">Boot Time</span>: 2019-07-16 18:12
<span class="hljs-comment">#Ubuntu</span>

 Tweet 3
<span class="hljs-comment">#NetStats</span>
<span class="hljs-attribute">Ping</span>: 38.68 ms
<span class="hljs-attribute">Down/Up Speed</span>: 994.81 Mbps/409.19 Mbps
<span class="hljs-attribute">Data Used (dl/ul)</span>: 390.41 MB/144.5 MB
<span class="hljs-attribute">IP</span>: 35.222.xx.xx
<span class="hljs-attribute">ISP</span>: Google Cloud
<span class="hljs-attribute">Region</span>: Virginia
<span class="hljs-attribute">Continent</span>: North America
<span class="hljs-attribute">Share</span>: http://www.speedtest.net/result/8438272507.png
<span class="hljs-comment">#Speedtest</span>
</code></pre><p><img src="../.github/tweetStats.gif" alt="example"></p>