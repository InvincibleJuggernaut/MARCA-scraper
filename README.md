# MARCA-scraper

[![](https://img.shields.io/badge/MADE%20WITH%20-Python-blueviolet)](https://www.python.org)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-brightgreen.svg)](https://www.gnu.org/licenses/gpl-3.0)

<h2>Introduction</h2>
MARCA is a Spanish daily sports newspaper whose primary focus is on the Madrid clubs, although it covers important news from other football teams as well. 
Majority of the content on their main website falls into the following categories :
<ul style="disc">
  <li>Real Madrid</li>
  <li>Barcelona</li>
  <li>Spanish Football</li>
  <li>International Football</li>
  <li>More Sports</li>
  <li>Lifestyle</li>
  </ul>
  
<h2>Objective</h2>  
This project scrapes their site dedicated to Real Madrid news and fetches as many articles as needed by the user. This could be used along with an application or RSS feeder to fetch the latest news rather than manually browsing the website through a browser.
<b>One thing to note here is that every website follows their own template style. By that I mean to say the nesting of various tags. Every website uses the HTML tags according to their own use and style. Therefore, this code might not necessarily work for other sites. One would need to observe the tags style of that particular website before implementing such a tool.</b> One only needs a basic understanding of how HTML works and the use of the tags.

<h2>Major Technologies</h2>
<ul type="disc">
  <li>Python - 3.6.9</li>
  <li>beautifulsoup4 - 4.9.1</li>
  <li>requests - 2.24.0</li>
  <li>urllib3 - 1.25.10</li>
</ul>
<p>All the dependencies can be found <a href="requirements.txt">here</a>.</p>

<h2>Installation</h2>
<p>Clone or download the repository in your preffered directory using:</p>
  
```
git clone https://github.com/InvincibleJuggernaut/MARCA-scraper.git
```
<h2>Dependencies</h2>

<p>All the dependencies for the program can be installed using :</p>

```
cd MARCA-scraper
pip3 install -r requirements.txt
```
<h2>Usage</h2>
<p> The program can be run using :</p>
  
```
python3 web_scraper.py
```
<br>
<br>

