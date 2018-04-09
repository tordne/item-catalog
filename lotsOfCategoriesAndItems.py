#!/usr/bin/env python3.6

from time import sleep

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from project.server.models import Base, User, Category, Item


engine = create_engine('postgresql://vagrant:vagrant@localhost/catalog')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()


# List of APG IV plant classification system

# User 1 -- Christopher Berdahl

user1 = User(name="John Smith", email="John.Smith@gmail.com", google_id="12345")

session.add(user1)
session.commit()

# Category 1 -- Basal Angiosperms

category1 = Category(name="Basal angiosperms")

session.add(category1)
session.commit()

item1 = Item(name="Amborellales", description="Amborella is a sprawling shrub or small tree up to 8 m high. It bears alternate or decussate, simple evergreen leaves without stipules. The leaves are two-ranked, with distinctly serrated or rippled margins, and about 8 to 10 cm long.", category_id=1, user_id=1)  # NOQA

session.add(item1)
session.commit()

sleep(1)

# Category 2 -- Magnoliids

category2 = Category(name="Magnoliids")

session.add(category2)
session.commit()

item1 = Item(name="Canellales", description="The Canellaceae are found in tropical America and Africa, and the Winteraceae are part of the Antarctic flora (found in diverse parts of the southern hemisphere).", category_id=2, user_id=1)  # NOQA

session.add(item1)
session.commit()

sleep(1)

# Category 3 -- Monocots

category3 = Category(name="Monocots")

session.add(category3)
session.commit()

item1 = Item(name="Acorales", description="The genus is native to North America and northern and eastern Asia, and naturalised in southern Asia and Europe from ancient cultivation.", category_id=3, user_id=1)  # NOQA

session.add(item1)
session.commit()

sleep(1)

# Category 4 -- Eudicots

category4 = Category(name="Eudicots")

session.add(category4)
session.commit()

item1 = Item(name="Ranunculales", description="Ranunculales is an order of flowering plants. Of necessity it contains the family Ranunculaceae, the buttercup family, because the name of the order is based on the name of a genus in that family.", category_id=4, user_id=1)  # NOQA

session.add(item1)
session.commit()

sleep(1)
