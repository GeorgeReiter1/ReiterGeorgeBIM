# TODO Найдите количество книг, которое можно разместить на дискете
import math
weight_of_one_book_in_byte = 4*25*50*100
weight_in_MB = weight_of_one_book_in_byte/(1024*1024)
amount_of_books = math.floor(1.44 / weight_in_MB)
print("Количество книг, помещающихся на дискету:", amount_of_books)
