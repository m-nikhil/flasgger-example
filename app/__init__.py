from flask import Flask, jsonify, request
from flasgger import Swagger

app = Flask(__name__)

app.config['SWAGGER'] = {
    'title': 'API doc',
    'uiversion': 3,
    'openapi' : '3.0.2'
}



@app.route('/ping', methods=['GET'])
def ping():
    return "The service is up and running :)"

@app.route('/api', methods=['POST'])
def api(): 
    """This endpoint runs an API in the backgraound and return corresponding response in the form of json 
    ---
    definitions:
      output:
        type: object
        properties:
          output1: 
            type: string
          output2: 
            type: string
          output3: 
            type: string
      input:
        type: object
        properties:
           input1: 
            type: string
           input2: 
            type: string
           input3: 
            type: string
    requestBody:
        content:
            application/json:
                schema:
                    $ref: '#/definitions/input'
    responses:
      200:
        description: 
        schema:
          $ref: '#/definitions/output'
    """
    # read input
    input = request.json

    # Call the api <<<here>>> 

    output_sample = {
        'output1': input["input1"],
        'output2': input["input2"],
        'output3': input["input3"],
    }

    return jsonify(output_sample)

swagger = Swagger(app)