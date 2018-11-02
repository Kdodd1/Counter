from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key ="Thisissecret"
@app.route('/')
def index():
	try:
		session['counter'] +=1 
	except KeyError as e:
		print(e)
		session['counter'] = 1
	return render_template("index.html", counter=session['counter'])

@app.route('/plustwo', methods=["POST"] )
def plustwo():
	session['counter'] +=1

	return redirect ('/')

@app.route('/reset', methods=['POST'])
def reset():
	session.clear()


	return redirect('/')
if __name__=='__main__':
	app.run(debug=True)