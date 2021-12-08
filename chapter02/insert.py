from sqlalchemy.sql.expression import insert
from tables import engine, cookies

# ISERTS
## Single insert as a method
# ins = cookies.insert().values(
#     cookie_name="chocolate chip",
#     cookie_recipe_url="https://www.youtube.com/",
#     cookie_sku="CC01",
#     quantity="12",
#     unit_cost="0.5",
# )

# with engine.connect() as connection:
#     result = connection.execute(ins)

# print(result.inserted_primary_key)

## Global insert method
# ins = insert(cookies).values(
#     cookie_name="chocolate chip",
#     cookie_recipe_url="https://www.youtube.com/",
#     cookie_sku="CC01",
#     quantity="12",
#     unit_cost="0.5",
# )
# connection = engine.connect()
# result = connection.execute(ins)
# connection.close()
# print(str(ins))

## Multiple inserts
inventories = [
    {
        "cookie_name":"chocolate chip",
        "cookie_recipe_url":"https://www.youtube.com/",
        "cookie_sku":"CC01",
        "quantity":"12",
        "unit_cost":"0.5",
    },
    {
        "cookie_name":"peanut butter",
        "cookie_recipe_url":"https://www.youtube.com/",
        "cookie_sku":"PB01",
        "quantity":"24",
        "unit_cost":"0.25",
    },
    {
        "cookie_name":"oatmeal raisen",
        "cookie_recipe_url":"https://www.youtube.com/",
        "cookie_sku":"EWW01",
        "quantity":"100",
        "unit_cost":"1.00",
    },
    {
        "cookie_name":"dark chocolate chip",
        "cookie_recipe_url":"https://www.youtube.com/",
        "cookie_sku":"CC02",
        "quantity":"1",
        "unit_cost":"0.75",
    },
    {
        "cookie_name":"chocolate chip",
        "cookie_recipe_url":"https://www.youtube.com/",
        "cookie_sku":"CC01",
        "quantity":"12",
        "unit_cost":"0.5",
    },
]
ins = cookies.insert()
connection = engine.connect()
rp = connection.execute(ins, inventories)
connection.close()

