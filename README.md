# vinloader
A Python program to scrape the internet for information related to input VIN...<br>
It returns the car's year, make, model, curb weight, and price.<br>
This is a freely available and limited version of the program written under contract with Horizon Motors.<br>
The car dealer version of the code is used to maintain and monitor the car dealers inventory
through a database.  VINS are input into a vins.txt file with one VIN number on each line.  The program will sequentially<br>
search for each VIN, establish its Year, Make, and Model, and from that information obtain Curb Weight and average<br>
prices for the car at local used car dealers.  Because the complete attribute list for the vehicle is not utilized, these<br>
prices are only a rough estimate...<br>
Database hooks are not included in this version, so it can be run easliy in a python environment.  This version<br>
is used to test and improve the web-scraping capabilities and robustness of the code for obtaining car data.<br>
It is an excellent example for persons interested in using a headless browser coupled with Beautiful Soup and Selenium.

Packages required to operate:<br>
bs4<br>
selenium<br>
pyvirtualdisplay<br>
numpy<br>
geckodriver
