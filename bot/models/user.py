import sqlmodel


class User(sqlmodel.SQLModel, table=True):
    id: int = sqlmodel.Field(primary_key=True)

    cards: list['Card'] = sqlmodel.Relationship(back_populates='user')
