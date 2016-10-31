from googleAPI_Flask import googleAPI_Flask

@app.route('/')
@app.route('/index')
def index():
	return "Hello, World!"
