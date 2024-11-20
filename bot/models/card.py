import sqlmodel


class Card(sqlmodel.SQLModel, table=True):
    id: int = sqlmodel.Field(primary_key=True)

    user_id: int = sqlmodel.Field(foreign_key='user.id')
    user: 'User' = sqlmodel.Relationship(back_populates='cards')
