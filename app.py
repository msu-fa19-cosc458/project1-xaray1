import flask
import os

app = flask.Flask(__name__)

@app.route('/Father')
def render(): 
    
    return flask.render_template("structure.html")
    
app.run(
    port = int(os.getenv('PORT',8080)),
    host = os.getenv('IP', '0.0.0.0')
    )