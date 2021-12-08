from sqlalchemy.sql.expression import select
from tables import engine, cookies

conn = engine.connect()

#### SELECTION TYPES

## global select function
query = select([cookies])
rp = conn.execute(query)


## using select method
query = cookies.select()
all_cookies = conn.execute(query).fetchall()


## selecting fields to select
query = select([cookies.c.cookie_name, cookies.c.quantity, cookies.c.unit_cost])
rp = conn.execute(query)

#### ORDERING

## asc/desc as method
query = select([cookies]).order_by(cookies.c.cookie_name.asc())
rp = conn.execute(query)


## global asc/desc function
from sqlalchemy import desc
query = select([cookies]).order_by(desc(cookies.c.cookie_name))
rp = conn.execute(query)


#### LIMITING
query = select([cookies.c.cookie_name, cookies.c.quantity, cookies.c.unit_cost])
query = query.order_by(desc(cookies.c.unit_cost))
query = query.limit(2)
rp = conn.execute(query)


#### AGREGATE FUNCTIONS
from sqlalchemy.sql import func

## total number of cookies
query = select([func.sum(cookies.c.quantity)])
result = conn.execute(query).scalar()

## counting records
query = select([func.count(cookies.c.cookie_name)])
rp = conn.execute(query)
record = rp.first()
# print(record.keys())  # showing columns list
# print(record.count_1) # column value in that cell


## Renaming column name 
query = select([func.count(cookies.c.cookie_name).label("inventory_count")])
record = conn.execute(query).first()
# print(record.keys())
# print(record.inventory_count)


#### FILTERING
query = select([cookies]).where(cookies.c.quantity > 2)
rp = conn.execute(query)

## using ClauseElements
query = select([cookies]).where(cookies.c.cookie_name.like("%chocolate%"))
rp = conn.execute(query)

## Conjunctions
from sqlalchemy import or_, and_
query = select([cookies]).where(and_(cookies.c.cookie_name.like("%chocolate%"), cookies.c.quantity>=5))
rp = conn.execute(query)


















