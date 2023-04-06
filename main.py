from flask import Flask, render_template

main = Flask(__name__)

@main.route('/')
def hello_world():
  return "<p>Hello World</p>"

if __name__ == "__main__":
  main.run(host = '0.0.0.0', debug=True)