from keras.preprocessing.image import img_to_array
from keras.models import load_model
from flask_restplus import Api, Resource, fields
from flask import Flask, request, jsonify
import numpy as np
from werkzeug.datastructures import FileStorage
from PIL import Image
from keras.models import model_from_json
import tensorflow as tf
import os
# from flask_pymongo import PyMongo
import datetime
from pymongo import MongoClient
import json

app = Flask(__name__)

client = MongoClient('mongodb://mongodb:27017/mnist')
mnist_db = client.mnist
coll = mnist_db['interaction']

api = Api(app, version='1.0', title='MNIST Classification', description='CNN for Mnist')
ns = api.namespace('Make_School', description='Methods')

single_parser = api.parser()
single_parser.add_argument('file', location='files',
                           type=FileStorage, required=True)

db_parser = api.parser()

model = load_model('my_model.h5')
graph = tf.get_default_graph()


@ns.route('/prediction')
class CNNPrediction(Resource):
    """Uploads your data to the CNN"""
    @api.doc(parser=single_parser, description='Upload an mnist image')
    def post(self):
        print('halp!!')
        
        args = single_parser.parse_args()
        image_file = args.file
        image_file.save('image.png')
        img = Image.open('image.png')
        image_red = img.resize((28, 28))
        image = img_to_array(image_red)
        print(image.shape)
        x = image.reshape(1, 28, 28, 1)
        x = x/255
        # This is not good, because this code implies that the model will be
        # loaded each and every time a new request comes in.
        # model = load_model('my_model.h5')
        with graph.as_default():
            out = model.predict(x)
        print(out[0])
        print(np.argmax(out[0]))
        r = np.argmax(out[0])
        print("datetime", datetime.datetime.utcnow())
        print("prediction", str(r))
        record_obj = {'prediction':str(r), 'time':datetime.datetime.utcnow(), 'filename':'image.png'}
        print('Record Object')
        print(record_obj)
        # doc = mnist_db.interaction.insert(record_obj)
        my_id = coll.insert_one(record_obj).inserted_id
        print(my_id)
        # print("docy mocky", doc)
        return {'prediction': str(r), 'db_id': str(my_id)}

@ns.route('/db_dump')
class dump_it(Resource):
    '''Dump all database data for anyone to explore and hack'''
    @api.doc(parser=db_parser, description='Testing this shit')
    def get(self):
        print("getting it")
        ladada = ''
        
        for x in coll.find():
            print("x is", str(x))
            ladada += str(x)
        return ladada

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)