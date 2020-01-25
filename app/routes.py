
from app import app

@app.route('/myroute')
def myroute():
	return 'myroute'
