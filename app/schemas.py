from pydantic import BaseModel, Field, field_validator

class BookBase(BaseModel):
    title: str = Field(..., min_length=1) 
    authors: str = Field(..., min_length=1) 
    pages: int
    year: int | None = None

class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    title: str | None = None
    authors: str | None = None
    pages: int | None = None
    year: int | None = None

    @field_validator("title")
    def title_not_empty(cls, v):
        if v is not None and v.strip() == "":
            raise ValueError("title não pode ser vazio")
        return v

    @field_validator("authors")
    def authors_not_empty(cls, v):
        if v is not None and v.strip() == "":
            raise ValueError("authors não pode ser vazio")
        return v

class BookRead(BookBase):
    id: int
    class Config:
        orm_mode = True
