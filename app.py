#web3.py

from flask import Flask,request,render_template

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
	#return '<h1>Home</h1>'
	return render_template('home.html')
	
@app.route('/signin',methods=['GET'])
def signin_form():
	#return '''<form action="/signin" method="post">
	#		  <p><input name="username"></p>
	#		  <p><input name="password" type="password"></p>
	#		  <p><button type="submit">Sign In</button></p>
	#		  </form>'''
	return render_template('form.html')
	
@app.route('/signin',methods=['POST'])
def signin():
	if request.form['username']=='admin' and request.form['password']=='password':
		#return '<h3>Hello,admin!</h3>'
		return render_template('signin-ok.html',username=username)
	#return '<h3>Bad username or password</h3>'
	return render_template('form.html',message='Bad username or password',username=username)
	
if __name__=='__main__':
	app.run()