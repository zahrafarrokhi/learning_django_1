from django.db import models

# point
# class Book(models.Model):
# 	name = models.CharField(max_length=100)
# 	author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='writers',related_query_name='writer')


class Author(models.Model):
	name = models.CharField(max_length=100)
	# writer = related be book
	def __str__(self):
		return self.name

class Book(models.Model):
	tagline = models.TextField()
	name = models.CharField(max_length=100)
	author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='writers',related_query_name='writer')

	def __str__(self):
		return self.name

class Publisher(models.Model):
	name = models.CharField(max_length=100)
	book = models.ManyToManyField(Book)

	def __str__(self):
		return self.name

'''
Author
	Id, name, book_set
Book
	Id, name, author

quries:
 #(Author to Book) Author ==> Book(has fk for Author ,has related_query_name='writer')
 Author.objects.filter(writer__name='Religion and Science')
 Author.objects.filter(writer__tagline='Science') 

 #(Author to Publisher )
 Author.objects.filter(writer__publisher__name='Oxford University Press')
 Author.objects.filter(writer__publisher__name__contains='Press')

 #(Publisher to Author)
 Publisher.objects.filter(book__author__name='Bertrand_Russell')

 #(Publisher to Book)
 Publisher.objects.filter(book__name='Religion and Science')

 #book so easy
 (Book to Author)
 Book.objects.filter(author__name='Bertrand_Russell')

 (Book to Puplisher)
 Book.objects.filter(publisher__name='Oxford University Press')
'''