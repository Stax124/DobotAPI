import{_ as e,c as o,o as t,b as i}from"./app.f1a8a6d1.js";const f=JSON.parse('{"title":"Shell Usage","description":"","frontmatter":{},"headers":[{"level":2,"title":"Invoking the Shell","slug":"invoking-the-shell","link":"#invoking-the-shell","children":[]},{"level":2,"title":"Get Position","slug":"get-position","link":"#get-position","children":[]},{"level":2,"title":"Move","slug":"move","link":"#move","children":[]},{"level":2,"title":"Gripper","slug":"gripper","link":"#gripper","children":[]},{"level":2,"title":"Suction Cup","slug":"suction-cup","link":"#suction-cup","children":[]},{"level":2,"title":"Conveyor Belt","slug":"conveyor-belt","link":"#conveyor-belt","children":[]}],"relativePath":"shell-usage.md","lastUpdated":1664479496000}'),l={name:"shell-usage.md"},s=i(`<h1 id="shell-usage" tabindex="-1">Shell Usage <a class="header-anchor" href="#shell-usage" aria-hidden="true">#</a></h1><h2 id="invoking-the-shell" tabindex="-1">Invoking the Shell <a class="header-anchor" href="#invoking-the-shell" aria-hidden="true">#</a></h2><div class="info custom-block"><p class="custom-block-title">INFO</p><p>This guide is assuming that you already have dobotapi package installed. If not, please refer to <a href="/DobotAPI/installation.html">Installation</a> guide.</p></div><p>You can open the TUI with this command:</p><div class="language-bash"><button class="copy"></button><span class="lang">bash</span><pre><code><span class="line"><span style="color:#A6ACCD;">python -m dobotapi.shell</span></span>
<span class="line"></span></code></pre></div><div class="warning custom-block"><p class="custom-block-title">WARNING</p><p>If some error occurs, please refer to <a href="/DobotAPI/troubleshooting.html">Troubleshooting</a> guide.</p></div><p>At this point, you should see a menu with a few options. Navigate through the menu with the arrow keys and press <code>Enter</code> or <code>Space</code> to select an option.</p><p>To continue, you need to press <code>Tab</code> to focus the other elements of the menu. Then, you can press <code>Enter</code> or <code>Space</code> to select an option.</p><p>At this point, a few options are available:</p><ul><li><code>Get position</code></li><li><code>Move</code></li><li><code>Gripper</code></li><li><code>Suction cup</code></li><li><code>Conveyor Belt</code></li><li><code>Exit</code></li></ul><p>We will now go through each of them (except <code>Exit</code> which is self-explanatory).</p><h2 id="get-position" tabindex="-1">Get Position <a class="header-anchor" href="#get-position" aria-hidden="true">#</a></h2><p>First of all, you will be asked if you want to log the positions to a file. If you want to log the positions, select <code>Yes</code> and press <code>Enter</code>. If you don&#39;t want to log the positions, select <code>No</code> and press <code>Enter</code>.</p><p>Once that is done, shell should start displaying the position of the robot. Once you are done, select <code>No</code> and press <code>Enter</code>.</p><div class="tip custom-block"><p class="custom-block-title">TIP</p><p>If you selected <code>Yes</code> when asked if you wanted to log the positions, you should be able to find a file called <code>coords.txt</code> with all the positions logged and ready to be further processed.</p></div><h2 id="move" tabindex="-1">Move <a class="header-anchor" href="#move" aria-hidden="true">#</a></h2><p>This option allows you to move the robot to a specific position. You will be asked to enter the coordinates of the position you want to move to. You can enter the coordinates in the following format:</p><p><code>x, y, z, r</code></p><p>where <code>x</code>, <code>y</code>, <code>z</code> are the coordinates of the position you want to move to and <code>r</code> is the rotation of the robot.</p><h2 id="gripper" tabindex="-1">Gripper <a class="header-anchor" href="#gripper" aria-hidden="true">#</a></h2><div class="warning custom-block"><p class="custom-block-title">WARNING</p><p>You need to have a gripper attached to the robot and the correct port for this option to work.</p></div><p>This option allows you to control the gripper of the robot. You can select one of the following options:</p><ul><li><code>Open</code></li><li><code>Close</code></li></ul><p>Operation should be instant.</p><h2 id="suction-cup" tabindex="-1">Suction Cup <a class="header-anchor" href="#suction-cup" aria-hidden="true">#</a></h2><div class="warning custom-block"><p class="custom-block-title">WARNING</p><p>You need to have a suction cup attached to the robot and the correct port for this option to work.</p></div><p>This option allows you to control the suction cup of the robot. You can select one of the following options:</p><ul><li><code>Suck</code></li><li><code>Idle</code></li></ul><p>Operation should be instant.</p><h2 id="conveyor-belt" tabindex="-1">Conveyor Belt <a class="header-anchor" href="#conveyor-belt" aria-hidden="true">#</a></h2><div class="warning custom-block"><p class="custom-block-title">WARNING</p><p>You need to have a conveyor belt attached to the robot and the correct port for this option to work.</p></div><p>This option allows you to control the conveyor belt of the robot. You will be asked a few questions:</p><ul><li><code>Speed</code>: You can enter a number between 0 and 1. This number represents the speed of the conveyor belt.</li><li><code>Forward</code>: You can select <code>Yes</code> or <code>No</code>. If you select <code>Yes</code>, the conveyor belt will move forward. If you select <code>No</code>, the conveyor belt will move backward.</li></ul>`,33),c=[s];function a(n,d,r,h,p,u){return t(),o("div",null,c)}const g=e(l,[["render",a]]);export{f as __pageData,g as default};
