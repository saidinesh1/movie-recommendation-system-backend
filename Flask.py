
from flask import Flask, jsonify, request
from scrapper2 import GetYtVideo
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/', methods = ['GET', 'POST'])
def home():
    if(request.method == 'GET'):

        data = "hello world"
        return jsonify({'data': data})



@app.route('/movie/<string:movie_name>', methods = ['GET'])
@cross_origin()
def disp(movie_name):
    result=GetYtVideo(movie_name)
    return result



if __name__ == '__main__':

    app.run(debug = True)