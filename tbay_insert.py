from tbay import User, Item, Bid
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://action:action@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()


ned = User(username="Ned", password="password123")
kara = User(username="Kara", password="password456")
layla = User(username="Layla", password="greenie")
thor = User(username="Thor", password="chuckit")

baseball = Item(name="Autographed baseball", description="Baseball autographed by Willie Mays", seller=ned)

bid1 = Bid(price=5.00, bidder=kara, bid_item=baseball)
bid2 = Bid(price=6.00, bidder=thor, bid_item=baseball)
bid3 = Bid(price=7.00, bidder=layla, bid_item=baseball)

session.add_all([ned, kara, layla, thor, baseball, bid1, bid2, bid3])
session.commit()