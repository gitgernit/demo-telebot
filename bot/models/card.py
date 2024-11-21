import sqlalchemy
import sqlmodel


class Card(sqlmodel.SQLModel, table=True):
    id: int | None = sqlmodel.Field(
        default=None,
        sa_column=sqlalchemy.Column(
            sqlalchemy.BigInteger(),
            primary_key=True,
            autoincrement=True,
        ),
    )

    user_id: int = sqlmodel.Field(foreign_key='user.id')
    user: 'User' = sqlmodel.Relationship(back_populates='cards')

    favorite: bool
