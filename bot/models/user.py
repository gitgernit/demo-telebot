import sqlalchemy
import sqlmodel


class User(sqlmodel.SQLModel, table=True):
    id: int | None = sqlmodel.Field(
        default=None,
        sa_column=sqlalchemy.Column(sqlalchemy.BigInteger(), primary_key=True),
    )

    cards: list['Card'] = sqlmodel.Relationship(
        back_populates='user', sa_relationship_kwargs={'lazy': 'joined'},
    )
