from fastapi import APIRouter, status
import src.books.schemas as schemas
from typing import List


book_router = APIRouter()

@book_router.get('', response_model=List[schemas.Book])
async def get_all_books():
    pass

@book_router.post('', status_code=status.HTTP_201_CREATED)
async def create_a_book(book_data:schemas.Book):
    new_book = book_data
    return new_book


@book_router.get('/{book_id}')
async def get_book(book_id:int):
    pass

@book_router.put('/{book_id}')
async def update_book(book_id:int, book_update_data:schemas.UpdateBook):
    pass

@book_router.delete('/{book_id}')
async def delete_book(book_id:int):
    pass
