from sqlalchemy.sql.expression import select
from tables import engine, cookies

# global select function
conn = engine.connect()
query = select([cookies]).order_by(cookies.c.quantity.desc())
rp = conn.execute(query)

for cookie in rp:
    print(cookie)

conn.close()
