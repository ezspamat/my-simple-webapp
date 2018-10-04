import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome! This is a containerized application"


if __name__ == "__main__":
    app.run()
