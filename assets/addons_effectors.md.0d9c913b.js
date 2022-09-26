import{_ as s,c as n,o as a,b as o}from"./app.24b9f6f2.js";const h=JSON.parse('{"title":"Effectors","description":"","frontmatter":{},"headers":[{"level":2,"title":"Suction cup","slug":"suction-cup","link":"#suction-cup","children":[]},{"level":2,"title":"Gripper","slug":"gripper","link":"#gripper","children":[]}],"relativePath":"addons/effectors.md","lastUpdated":1664223018000}'),p={name:"addons/effectors.md"},l=o(`<h1 id="effectors" tabindex="-1">Effectors <a class="header-anchor" href="#effectors" aria-hidden="true">#</a></h1><p>Some of the most notable ones are: <span style="font-weight:600;color:orange;">Suction cup</span> and <span style="font-weight:600;color:orange;">Gripper</span></p><p>Both of these are controlled exaclty the same way. Let&#39;s see how to use them.</p><h2 id="suction-cup" tabindex="-1">Suction cup <a class="header-anchor" href="#suction-cup" aria-hidden="true">#</a></h2><div class="info custom-block"><p class="custom-block-title">INFO</p><p>Please check with manual that you have plugged the effector into the correct port.</p></div><p>Suction cup is a simple effector that can be used to pick up small objects by creating a vacuum.</p><div class="language-python"><button class="copy"></button><span class="lang">python</span><pre><code><span class="line"><span style="color:#89DDFF;">import</span><span style="color:#A6ACCD;"> os</span></span>
<span class="line"><span style="color:#89DDFF;">from</span><span style="color:#A6ACCD;"> dobotapi </span><span style="color:#89DDFF;">import</span><span style="color:#A6ACCD;"> Dobot</span></span>
<span class="line"></span>
<span class="line"><span style="color:#A6ACCD;">bot </span><span style="color:#89DDFF;">=</span><span style="color:#A6ACCD;"> </span><span style="color:#82AAFF;">Dobot</span><span style="color:#89DDFF;">()</span></span>
<span class="line"></span>
<span class="line highlighted"><span style="color:#A6ACCD;">bot</span><span style="color:#89DDFF;">.</span><span style="color:#F07178;">suction_cup</span><span style="color:#89DDFF;">.</span><span style="color:#82AAFF;">enable</span><span style="color:#89DDFF;">()</span><span style="color:#A6ACCD;"> </span><span style="color:#676E95;"># Enable the suction cup</span></span>
<span class="line"></span>
<span class="line"><span style="color:#A6ACCD;">os</span><span style="color:#89DDFF;">.</span><span style="color:#82AAFF;">system</span><span style="color:#89DDFF;">(</span><span style="color:#89DDFF;">&quot;</span><span style="color:#C3E88D;">pause</span><span style="color:#89DDFF;">&quot;</span><span style="color:#89DDFF;">)</span><span style="color:#A6ACCD;"> </span><span style="color:#676E95;"># Wait for the user to press any key</span></span>
<span class="line"></span>
<span class="line highlighted"><span style="color:#A6ACCD;">bot</span><span style="color:#89DDFF;">.</span><span style="color:#F07178;">suction_cup</span><span style="color:#89DDFF;">.</span><span style="color:#82AAFF;">disable</span><span style="color:#89DDFF;">()</span><span style="color:#A6ACCD;"> </span><span style="color:#676E95;"># Disable the suction cup</span></span>
<span class="line"></span>
<span class="line"><span style="color:#A6ACCD;">bot</span><span style="color:#89DDFF;">.</span><span style="color:#82AAFF;">close</span><span style="color:#89DDFF;">()</span><span style="color:#A6ACCD;"> </span><span style="color:#676E95;"># Properly close the connection</span></span>
<span class="line"></span></code></pre></div><h2 id="gripper" tabindex="-1">Gripper <a class="header-anchor" href="#gripper" aria-hidden="true">#</a></h2><div class="info custom-block"><p class="custom-block-title">INFO</p><p>Please check with manual that you have plugged the effector into the correct port.</p></div><p>Gripper is a simple effector that grabs items by squeezing them.</p><div class="language-python"><button class="copy"></button><span class="lang">python</span><pre><code><span class="line"><span style="color:#89DDFF;">import</span><span style="color:#A6ACCD;"> os</span></span>
<span class="line"><span style="color:#89DDFF;">from</span><span style="color:#A6ACCD;"> dobotapi </span><span style="color:#89DDFF;">import</span><span style="color:#A6ACCD;"> Dobot</span></span>
<span class="line"></span>
<span class="line"><span style="color:#A6ACCD;">bot </span><span style="color:#89DDFF;">=</span><span style="color:#A6ACCD;"> </span><span style="color:#82AAFF;">Dobot</span><span style="color:#89DDFF;">()</span></span>
<span class="line"></span>
<span class="line highlighted"><span style="color:#A6ACCD;">bot</span><span style="color:#89DDFF;">.</span><span style="color:#F07178;">gripper</span><span style="color:#89DDFF;">.</span><span style="color:#82AAFF;">enable</span><span style="color:#89DDFF;">()</span><span style="color:#A6ACCD;"> </span><span style="color:#676E95;"># Enable the suction cup</span></span>
<span class="line"></span>
<span class="line"><span style="color:#A6ACCD;">os</span><span style="color:#89DDFF;">.</span><span style="color:#82AAFF;">system</span><span style="color:#89DDFF;">(</span><span style="color:#89DDFF;">&quot;</span><span style="color:#C3E88D;">pause</span><span style="color:#89DDFF;">&quot;</span><span style="color:#89DDFF;">)</span><span style="color:#A6ACCD;"> </span><span style="color:#676E95;"># Wait for the user to press any key</span></span>
<span class="line"></span>
<span class="line highlighted"><span style="color:#A6ACCD;">bot</span><span style="color:#89DDFF;">.</span><span style="color:#F07178;">gripper</span><span style="color:#89DDFF;">.</span><span style="color:#82AAFF;">disable</span><span style="color:#89DDFF;">()</span><span style="color:#A6ACCD;"> </span><span style="color:#676E95;"># Disable the suction cup</span></span>
<span class="line"></span>
<span class="line"><span style="color:#A6ACCD;">bot</span><span style="color:#89DDFF;">.</span><span style="color:#82AAFF;">close</span><span style="color:#89DDFF;">()</span><span style="color:#A6ACCD;"> </span><span style="color:#676E95;"># Properly close the connection</span></span>
<span class="line"></span></code></pre></div>`,11),e=[l];function t(c,r,i,y,D,F){return a(),n("div",null,e)}const u=s(p,[["render",t]]);export{h as __pageData,u as default};
