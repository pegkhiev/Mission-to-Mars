from flask import Flask, render_template
from flask_pymongo import PyMongo
import scraping


#set up flask
app = Flask(__name__)

#Use flask_pymongo to set up mongo connection
#URI is a uniform resource identifies like URL
#mongodb://localhost:27017 is the URI
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route('/')
def index():
    mars = mongo.db.mars.find_one()
    marshemi = mongo.db.marshemi.find_one()
    return render_template('index.html', mars=mars,
            marshemi = marshemi)
    
@app.route('/scrape')
def scrape(): 
    mars = mongo.db.mars
    mars_data = scraping.scrape_all()
    r = mars.update({},mars_data,upsert = True)
    print(mars_data)
    print(r)
    return render_template('scrape.html')

if __name__ =="__main__":
    app.run()