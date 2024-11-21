from flask import *
from flask_cors import *

app = Flask(__name__)
CORS(app)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=15555)
