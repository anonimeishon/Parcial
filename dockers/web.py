from flask import Flask, request, render_template, jsonify
#the getparams function will return a datetime object with these parameters '%Y-%m-%d_%H:%M:%S' followed by temperature in the form of a float
from params import getparams
from flask_redis import FlaskRedis


#weather api http://api.openweathermap.org/data/2.5/weather?id=3687238&appid=9583c3b4fa60a5323f4d1d115a5f2592
#Flask configs
app = Flask(__name__)
redis_client = FlaskRedis(app)

#routes
@app.route('/index')
def index():
    return ('<form action="/chain" method="GET"><input type="submit" value="See hash chain"></form>')


#This route will show every object added to the db
@app.route('/', methods=['GET', 'POST'])
def writehash():

    if request.method == 'POST':
        pass
        #return(render_template('post.html'))
    elif request.method == 'GET':
        pass
        #return render_template('get.html',hashes = hashes, title= "Show hashes")
 


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port = 80)