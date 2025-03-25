from fastapi import FastAPI
from postgres import Postgres

app = FastAPI()
db = Postgres("postgresql://postgres:abc123@db/postgres")

db.run("CREATE TABLE foo(bar TEXT, baz INT)")
db.run("INSERT INTO foo VALUES ('buz', 42)")
db.run("INSERT INTO foo VALUES ('bit', 537)")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/all")
def select_star():
    rows = db.all("SELECT * FROM foo")
    print(rows)
    return rows