from tbay import User, Item, Bid, session
from sqlalchemy import func

# Nested query
# first, find max bid price
# second, find bidder_id/user_id with max bid price
# print username 

print session.query(User.username).filter(User.id == session.query(Bid.bidder_id).filter(Bid.price == (session.query(func.max(Bid.price)).all()[0]))[0][0]).all()[0][0]