from sqlalchemy.orm import Mapped, mapped_column
from db.db_env import Base

class Users(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    nickname: Mapped[str] = mapped_column(nullable=False, primary_key=True)
    password: Mapped[str] = mapped_column(nullable=False)
    phone_number: Mapped[int] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, primary_key=True)
    country: Mapped[str] = mapped_column(nullable=False)


