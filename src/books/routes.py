from fastapi import APIRouter, status, Depends, HTTPException
from typing import List
from src.db.main import get_session
from sqlmodel.ext.asyncio.session import AsyncSession
from src.books.service import BookService
from src.books.schemas import Book, UpdateBookModel, BookCreateModel


book_router = APIRouter()
book_service = BookService()


#show all books
@book_router.get('', response_model=List[Book])
async def get_all_books(session:AsyncSession = Depends(get_session)):
    books = await book_service.get_all_books(session)
    return books


## create a new book
@book_router.post('', status_code=status.HTTP_201_CREATED, response_model= Book)
async def create_a_book(book_data:BookCreateModel, session:AsyncSession = Depends(get_session))-> dict:
    new_book = await book_service.create_book(book_data, session)
    return new_book

 

 ## fetch a book with book_uid
@book_router.get('/{book_id}', response_model=Book)
async def get_book(book_uid:str, session:AsyncSession = Depends(get_session))->dict:
    book = await book_service.get_book(book_uid, session)
    if book:
        return book
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"book with id {book_uid} not available")



## Update a book with book_uid
@book_router.patch('/{book_uid}', response_model=Book)
async def update_book(book_uid:str, book_update_data:UpdateBookModel,session:AsyncSession = Depends(get_session))->dict:
    updated_book = await book_service.update_book(book_uid, book_update_data, session)
    if updated_book is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"book with id {book_uid} not available")
    else:
        return updated_book
    
        


## delete book with book_uid
@book_router.delete('/{book_uid}', status_code=status.HTTP_200_OK)
async def delete_book(book_uid:str, session: AsyncSession = Depends(get_session)):
    book_to_delete = await book_service.delete_book(book_uid, session)
    if book_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"book with id {book_uid} not available")
    
    return "delete successfully"