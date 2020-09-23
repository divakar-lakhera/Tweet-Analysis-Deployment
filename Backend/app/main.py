from flask import Flask
from app.model.predict import modelPredict
from flask import request, jsonify
from flask_cors import CORS
app= Flask(__name__)
CORS(app)
systemModel=modelPredict()
systemModel.setup()
@app.route('/')
def index():
    return "<h1> Sentiment Analysis API v1 By Divakar Lakhera</h1>"

@app.route('/wake')
def wakeServer():
    print("Waking Server UP")
    systemModel.predictSentiment("TEST")
    return jsonify({'return':'ok'})

@app.route('/api/v1/predict/',methods=['GET'])
def doJob():
    job_id=str(request.args['id'])
    job_string=str(request.args['string'])
    print("Got Job id: "+job_id)
    ret=systemModel.predictSentiment(str(job_string))
    print("Done Job id: "+job_id)
    return jsonify({'request_id':job_id,'getRequest':str(job_string),'modelReturn':int(ret[0])})
## /api/v1/predict?id=13&string=Hello   