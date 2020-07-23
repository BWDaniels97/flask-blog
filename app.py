from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')

def home():
    return """Hello Internet!
hello"""




@app.route('/about')
    
def about():
    return "This is a about page!"

