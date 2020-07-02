from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def application_state_excel1():
   return jsonify(response_value_1=1,response_value_2="value1")
   

if __name__ == "__main__":
  port = int(os.getenv("PORT", 8080))
  app.run(host='0.0.0.0', port=port)
