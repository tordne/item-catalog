#!/usr/bin/env python3.6

from time import sleep

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from project.server.models import Base, User, Category, Item

import os

engine = create_engine(os.environ['DATABASE_URL'])

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()


# List of APG IV plant classification system

# User 1 -- Christopher Berdahl

user1 = User(name="John Smith",
             email="John.Smith@gmail.com",
             google_id="12345")

session.add(user1)
session.commit()

# Categories

category1 = Category(name="Basal angiosperms", user_id=1)
category2 = Category(name="Magnoliids", user_id=1)
category3 = Category(name="Monocots", user_id=1)
category4 = Category(name="Eudicots", user_id=1)

session.add(category1)
session.add(category2)
session.add(category3)
session.add(category4)
session.commit()

# Items first round

item1 = Item(name="Amborellales",
             description="Amborella is a sprawling shrub or small tree up to \
             8 m high. It bears alternate or decussate, simple evergreen \
             leaves without stipules. The leaves are two-ranked, with \
             distinctly serrated or rippled margins, \
             and about 8 to 10 cm long.",
             category_id=1,
             user_id=1)


item2 = Item(name="Piperales",
             description="The Canellaceae are found in tropical America \
             and Africa, and the Winteraceae are part of the Antarctic flora \
             (found in diverse parts of the southern hemisphere).",
             category_id=2,
             user_id=1)


item3 = Item(name="Alismatales",
             description="Plants assigned to this order are mostly tropical \
             or aquatic. Some grow in fresh water, some in marine habitats.",
             category_id=3,
             user_id=1)


item4 = Item(name="Proteales",
             description="Well-known members of the Proteales include the \
             proteas of South Africa, the banksias and macadamias of \
             Australia, the London plane, and the sacred lotus.",
             category_id=4,
             user_id=1)


session.add(item1)
session.add(item2)
session.add(item3)
session.add(item4)
session.commit()

sleep(1)


# Items second Round

item1 = Item(name="Nymphaeales",
             description="Well-known plants which may be included in this \
             order include black pepper, kava, lizard's tail, birthwort, \
             and wild ginger.",
             category_id=1,
             user_id=1)


item2 = Item(name="Canellales",
             description="The Canellaceae are found in tropical America and \
             Africa, and the Winteraceae are part of the Antarctic flora \
             (found in diverse parts of the southern hemisphere).",
             category_id=2,
             user_id=1)


item3 = Item(name="Acorales",
             description="The genus is native to North America and northern \
             and eastern Asia, and naturalised in southern Asia and Europe \
             from ancient cultivation.",
             category_id=3,
             user_id=1)


item4 = Item(name="Ranunculales",
             description="Ranunculales is an order of flowering plants. Of \
             necessity it contains the family Ranunculaceae, the buttercup \
             family, because the name of the order is based on the name of \
             a genus in that family.",
             category_id=4,
             user_id=1)


session.add(item1)
session.add(item2)
session.add(item3)
session.add(item4)
session.commit()

sleep(1)


# Items third round

item1 = Item(name="Illiciales",
             description="Illiciales is an order of flowering plants that is \
             not recognized by the current most widely used system of plant \
             classification, the Angiosperm Phylogeny Group's \
             APG III system.",
             category_id=1,
             user_id=1)


item2 = Item(name="Laurales",
             description="The best known species in this order are those of \
             the Lauraceae (for example bay laurel, cinnamon, avocado, and \
             Sassafras)",
             category_id=2,
             user_id=1)


item3 = Item(name="Asparagales",
             description="The leaves of almost all species form a tight \
             rosette, either at the base of the plant or at the end of the \
             stem, but occasionally along the stem. The flowers are not \
             particularly distinctive, being 'lily type', \
             with six tepals and up to six stamina.",
             category_id=3,
             user_id=1)


item4 = Item(name="Trochodendraceae",
             description="It comprises two extant genera, each with a single \
             species[1] found in south east Asia. The two living species \
             (Tetracentron sinense and Trochodendron aralioides) both have \
             secondary xylem without vessel elements, which is quite rare in \
             angiosperms. As the vessel-free wood suggests primitiveness, \
             these two species have attracted much taxonomic attention.",
             category_id=4,
             user_id=1)


session.add(item1)
session.add(item2)
session.add(item3)
session.add(item4)
session.commit()
