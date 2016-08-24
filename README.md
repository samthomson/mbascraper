Scottish bothy scraper
======================

Using the MBA (Mountain Bothy Association) location page (http://www.mountainbothies.org.uk/locationmap.asp) to find bothies is awkward. Since
*   you have to click into regional sub pages
*   the map isn't a google map or similar, showing the bothies just as a number on a patch of green, hard to contextualise their real location
*   only grid refs are shown, fine for consulting paper maps or certain GPSs but not as universal as a GPS lat/lon

This scraper extracts all information on each bothy, and then a seperate script can be run to query a grid reference to lat-lon api to make the bothy data more useful


TODO
====

*    store bothy data into mysql
*    script to convert grid refs to lat lon
