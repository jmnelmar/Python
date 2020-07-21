from flask import Flask, escape, request,render_template, url_for, redirect,request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return render_template("/index.html")
    #return 'Hello {}!'.format( name )


#env FLASK_APP=app.py FLASK_DEBUG=1 flask run