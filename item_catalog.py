from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Category, Base, Item

app = Flask(__name__)

engine = create_engine('sqlite:///itemcatalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/catalog')
def catalog():
	categories = session.query(Category).all()
	items = session.query(Item).all()
	return render_template('main.html', categories=categories, items=items)

@app.route('/catalog/<string:category>')
def getCategory(category):
	categories = session.query(Category).all()
	current = session.query(Category).filter_by(title=category).one()
	items = session.query(Item).filter_by(category_id=current.id).all()
	return render_template('main.html', categories=categories, selectedCategory=category, items=items)

@app.route('/catalog/<string:category>/<string:item>')
def getItem(category, item):
	currentCategory = session.query(Category).filter_by(title=category).one()
	item = session.query(Item).filter_by(category_id=currentCategory.id, name=item).one()
	return render_template('item.html',item=item)

@app.route('/catalog/new', methods=['GET','POST'])
def newItem():
	if request.method == 'POST':
		newItem = Item(name=request.form['name'], description=request.form['description'], category_id=request.form['category_id'])
		session.add(newItem)
		session.commit()
		return redirect(url_for('catalog'))
	else:
		categories = session.query(Category).all()
		return render_template('editItem.html', new=True, item=None, categories=categories)

@app.route('/catalog/<string:category>/<string:item>/edit', methods=['GET','POST'])
def editItem(category, item):
	categories = session.query(Category).all()
	currentCategory = session.query(Category).filter_by(title=category).one()
	item = session.query(Item).filter_by(category_id=currentCategory.id, name=item).one()
	if request.method == 'POST':
		item.name=request.form['name']
		item.description=request.form['description']
		item.category_id=request.form['category_id']
		session.add(item)
		session.commit()
		return redirect(url_for('catalog'))
	else:
		return render_template('editItem.html', item=item, categories=categories)

@app.route('/catalog/<string:category>/<string:item>/delete', methods=['GET','POST'])
def deleteItem(category, item):
	if request.method == 'POST':
		currentCategory = session.query(Category).filter_by(title=category).one()
		item = session.query(Item).filter_by(category_id=currentCategory.id, name=item).one()
		session.delete(item)
		session.commit()
		return redirect(url_for('catalog'))
	else:
		return render_template('deleteItem.html')

@app.route('/login')
def login():
	return render_template('main.html')

if __name__ == '__main__':
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)
