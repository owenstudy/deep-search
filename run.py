from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flasgger import Swagger

from resources.deep_search_service import ChatGPT

app = Flask(__name__)
CORS(app, resources=r"/*", supports_credentials=True)
# cors = CORS(app, resources={"*": {"origins": "*"}})
api = Api(app)
swagger = Swagger(app)

# chat gpt
api.add_resource(ChatGPT, '/admin/chatgpt/ask')


app.run(host='0.0.0.0', port=80, debug=True, threaded=True)

# if __name__ == '__main__':08
#     app.run(debug=True)
