import urllib
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html')
@app.route('/parse')
def parse():
	
	return render_template('parse.html')
	
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username    
@app.route('/temp/<isim>')
def temp(isim=None):
    return render_template('hello.html',isim=isim)
@app.route("/hujjat")
def hujjat():
	tez=[]
	for i in [1,2,4]:
		tez.append(i)

	kimmat="hey hujjat hay jujjat"
	return render_template('hello.html',kimmat=kimmat,s=tez)

if __name__ == "__main__":
    app.run(debug=True)
