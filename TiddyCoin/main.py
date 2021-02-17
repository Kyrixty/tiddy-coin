import os

from app import app

if __name__=="__main__":
    app.socketio.run(host="localhost", port=5000)