"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask, request



app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app



@app.route('/pyapi')
def index():
  return 'Server Works!'
  
@app.route('/greet')
def say_hello():
  return 'Hello from Server'

@app.route('/pyapi/user/<username>')
def show_user(username):
  #returns the username
  return 'Username: %s' % username

@app.route('/pyapi/post/<int:post_id>')
def show_post(post_id):
  #returns the post, the post_id should be an int
  return str(post_id)

@app.route('/pyapi/query-example')
def query_example():
    language = request.args.get('language') #if key doesn't exist, returns None

    return '''<h1>The language value is: {}</h1>'''.format(language)




if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', '0.0.0.0')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '9020'))
    except ValueError:
        PORT = 9020
    app.run(HOST, PORT)
