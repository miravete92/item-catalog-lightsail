from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
@app.route('/catalog')
def catalog():
	return render_template('main.html')

@app.route('/catalog/<string:category>')
def getCategory(category):
	return render_template('main.html')

@app.route('/catalog/<string:category>/<string:item>')
def getItem(category, item):
	return render_template('item.html')

@app.route('/catalog/new', methods=['GET','POST'])
def newItem():
	return render_template('editItem.html', new=True)

@app.route('/catalog/<string:category>/<string:item>/edit', methods=['GET','PUT'])
def editItem(category, item):
	return render_template('editItem.html')

@app.route('/catalog/<string:category>/<string:item>/delete', methods=['GET','DELETE'])
def deleteItem(category, item):
	return render_template('deleteItem.html')

if __name__ == '__main__':
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)
