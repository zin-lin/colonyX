from flask import *
from flask_cors import *

app = Flask(__name__)
CORS(app)


# home route
@app.route('/')
def home():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=15555)
