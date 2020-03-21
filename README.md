# Mission-to-Mars

##Challenge

### Background 
The challenge is to scrape new images for the Mars Hemispheres, add them to MongoDB, and add new elements to the Flask app using Bootstrap elements. 

### 1) Scraping Mars Hemispheres Images and Saving Data to MongoDB 
The new code is added to the Jupyter Notebook file which is included in this repo (file: Mission-to-Mars-Challenge.ipynb), and a screenshot is attached here. The new code does: 
- Scrape four images 
- Add the title and url link to a list with four dictionaries
- Insert the new list to the MongoDB mars_app database 

<img width=500px alt="Jupyter code" src = "https://github.com/pegkhiev/Mission-to-Mars/blob/master/images/juputer_code.png">

### 2) Add New Elements to the Flask App
The complete code is included in the file in this repo.  Below are the two screenshots of the new elements added to the flask app. 

<img width=400px alt="homepage" src = "https://github.com/pegkhiev/Mission-to-Mars/blob/master/images/Homepage.png"><<img width=400px alt="scraping page" src = "https://github.com/pegkhiev/Mission-to-Mars/blob/master/images/scraping_page.png">

The following Bootstrap elements are used: 

2.1) Adding four hemispheres images as thumbnails

2.2) Adding four buttons within the thumbnail for users to view full-size images 

2.3) Adding color background for the new heading "Mars Hemispheres Images"

2.4) On the Scraping app page, rendered a new HTML file ("scrape.html") which includes a button for users to return to homepage with new scraped data. 





