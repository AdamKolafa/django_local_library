from ninja import NinjaAPI
from ninja import Schema
from datetime import date
from django.shortcuts import get_object_or_404


from typing import List
from ninja import UploadedFile, File


api = NinjaAPI()

@api.get("/hello")
def hello(request, name="world"):
    return f"Hello {name}"

class BookOut(Schema):
    title: str
    author: str
    summary: str
    isbn: str
    genre: str

@api.get("/employees", response=List[BookOut])
def list_employees(request):
    qs = BookOut.objects.all()
    return qs

@api.get("/books/{book_id}", response=BookOut)
def get_book(request, book_id: int):
    book = get_object_or_404(BookOut, id=book_id)
    return book