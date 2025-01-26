import os
from flask import render_template
from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        INFO_NODE_IP = os.getenv('INFO_NODE_IP', '')
        INFO_POD_IP = os.getenv('INFO_POD_IP', '')
        INFO_POD_UID = os.getenv('INFO_POD_UID', '')
        INFO_NODE_NAME = os.getenv('INFO_NODE_NAME', '')
        INFO_POD_NAME = os.getenv('INFO_POD_NAME', '')
        INFO_POD_NAMESPACE = os.getenv('INFO_POD_NAMESPACE', '')
        INFO_POD_SERVICE_ACCOUNT = os.getenv('INFO_POD_SERVICE_ACCOUNT', '')
        HOSTNAME = os.getenv('HOSTNAME', '')
        return render_template('index.html', 
                               INFO_NODE_IP=INFO_NODE_IP, 
                               INFO_POD_IP=INFO_POD_IP,
                               INFO_POD_UID=INFO_POD_UID,
                               INFO_NODE_NAME=INFO_NODE_NAME,
                               INFO_POD_NAME=INFO_POD_NAME,
                               INFO_POD_NAMESPACE=INFO_POD_NAMESPACE,
                               INFO_POD_SERVICE_ACCOUNT=INFO_POD_SERVICE_ACCOUNT,
                               HOSTNAME=HOSTNAME)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=8080, debug=True)