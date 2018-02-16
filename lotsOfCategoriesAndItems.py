#!/usr/bin/env python3.6

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from project.server.models import Base, Category, Item


engine = create_engine('postgresql://vagrant:vagrant@localhost/catalog')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()


# List of APG IV plant classification system

# Category 1 -- Basal Angiosperms

category1 = Category(name="Basal angiosperms")

session.add(category1)
session.commit()

item1 = Item(name="Amborellales", description="Amborella is a sprawling shrub or small tree up to 8 m high. It bears alternate or decussate, simple evergreen leaves without stipules. The leaves are two-ranked, with distinctly serrated or rippled margins, and about 8 to 10 cm long.")  # NOQA

session.add(item1)
session.commit()


# Category 2 -- Magnoliids

category2 = Category(name="Magnoliids")

session.add(category2)
session.commit()

item1 = Item(name="Canellales", description="The Canellaceae are found in tropical America and Africa, and the Winteraceae are part of the Antarctic flora (found in diverse parts of the southern hemisphere).")  # NOQA

session.add(item1)
session.commit()


# Category 3 -- Monocots

category3 = Category(name="Monocots")

session.add(category3)
session.commit()

item1 = Item(name="Acorales", description="The genus is native to North America and northern and eastern Asia, and naturalised in southern Asia and Europe from ancient cultivation.")  # NOQA

session.add(item1)
session.commit()


# Category 4 -- Eudicots

category4 = Category(name="Eudicots")

session.add(category4)
session.commit()

item1 = Item(name="Ranunculales", description="Ranunculales is an order of flowering plants. Of necessity it contains the family Ranunculaceae, the buttercup family, because the name of the order is based on the name of a genus in that family.")  # NOQA

session.add(item1)
session.commit()
