from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base

engine = create_engine('sqlite:///itemcatalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Menu for UrbanBurger
category1 = Category(title="Soccer")
session.add(category1)
session.commit()

category2 = Category(title="Basketball")
session.add(category2)
session.commit()

category3 = Category(title="Baseball")
session.add(category3)
session.commit()

category4 = Category(title="Frisbee")
session.add(category4)
session.commit()

category5 = Category(title="Snowboarding")
session.add(category5)
session.commit()

category6 = Category(title="Rock Climbing")
session.add(category6)
session.commit()

category7 = Category(title="Foosball")
session.add(category7)
session.commit()

category8 = Category(title="Skating")
session.add(category8)
session.commit()

category9 = Category(title="Hockey")
session.add(category9)
session.commit()

print "added menu items!"
