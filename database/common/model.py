from peewee import *
import pathlib
from pathlib import Path

db = SqliteDatabase(Path(pathlib.Path.cwd(), 'database/Table', 'links.db'))

class BaseModel(Model):
    id = PrimaryKeyField(unique=True)
    class Meta():
        database = db
        order_by = 'id'


class Links(BaseModel):
    https_link = CharField()
    name_link = CharField()

    class Meta():
        db_table = 'Links'