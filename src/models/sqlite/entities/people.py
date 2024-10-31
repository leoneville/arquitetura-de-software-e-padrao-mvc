from dataclasses import dataclass
from sqlalchemy import Column, String, BIGINT, ForeignKey
from src.models.sqlite.settings.base import Base


@dataclass
class PeopleTable(Base):
    __tablename__ = "people"

    id: int = Column(BIGINT, primary_key=True)
    first_name: str = Column(String, nullable=False)
    last_name: str = Column(String, nullable=False)
    age: int = Column(BIGINT, nullable=False)
    pet_id: int = Column(BIGINT, ForeignKey("pets.id"))

    def __repr__(self) -> str:
        return f"People [name={self.first_name}, last_name={self.last_name}, pet_id={self.pet_id}]"
