from django.db import models

# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User

class hotel(models.Model):
	#Id = models.IntegerField()
	Name = models.CharField(max_length=25)
	City =models.CharField(max_length=15)
	Star = models.CharField(max_length=10)
	Location = models.CharField(max_length=100)
	PhoneNum = models.CharField(max_length=18)


class hotel_rooms(models.Model):
	#Id = models.IntegerField()
	NumberOfRooms = models.IntegerField()
	#hotelId = models.IntegerField()
	singleId = models.IntegerField()
	vipId = models.IntegerField()
	suitId = models.IntegerField()
	hotel=models.ForeignKey(hotel,on_delete=models.CASCADE)

class hotel_photos(models.Model):
	#Id = models.IntegerField()
	hotelId = models.IntegerField()
	URL = models.ImageField()
	URL1 = models.ImageField()
	URL2 = models.ImageField()
	URL3= models.ImageField()
	URL4 = models.ImageField()

class single_room(models.Model):
	#Id = models.IntegerField()
	URL = models.ImageField()
	numberofrooms = models.IntegerField()
	#hotel_room = models.ForeignKey(hotel_rooms, on_delete=models.CASCADE)

class suit_room(models.Model):
	#ID = models.IntegerField()
	URL = models.ImageField()
	numberofrooms = models.IntegerField()


#hotel_room = models.ForeignKey(hotel_rooms, on_delete=models.CASCADE)
class vip_room(models.Model):
	#Id = models.IntegerField()
	URL = models.ImageField()
	numberofrooms = models.IntegerField()

# all this tables down belong to hotel

class review(models.Model):
	#Id = models.IntegerField()
	comment = models.CharField(max_length=500)
	hotel_id = models.IntegerField()

class near_places(models.Model):
	#Id = models.IntegerField()
	hotelId =  models.IntegerField()
	near_place = models.CharField(max_length=200)

#these tables for person and his/her informations

class user(models.Model):
	#Id = models.IntegerField()
	username = models.CharField(max_length=15)
	name = models.CharField(max_length=15)
	surname = models.CharField(max_length=15)
	email =  models.EmailField()
	phoneNum = models.CharField(max_length=25)

class person(models.Model):
	#Id = models.IntegerField()
	username = models.CharField(max_length=15)
	password = models.CharField(max_length=25)
	personId = models.IntegerField()
	#userper = models.ForeignKey(person, on_delete=models.CASCADE)

'''class Post(models.Model):
	STATUS_CHOICES=(
		('draft','Draft'),
		('published','published'),

	)
	title = models.CharField(max_length=250)
	slug = models.SlugField(max_length=250)
	content = models.TextField()
	seo_title = models.CharField(max_length=160)
	seo_description = models.CharField(max_length=250)
	author = models.ForeignKey(User,related_name='blog_posts',on_delete=models.CASCADE)
	published = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=9,choices=STATUS_CHOICES)

	def __str__(self):
		return  self.title'''


class Book(models.Model):
    HARDCOVER = 1
    PAPERBACK = 2
    EBOOK = 3
    BOOK_TYPES = (
        (HARDCOVER, 'Hardcover'),
        (PAPERBACK, 'Paperback'),
        (EBOOK, 'E-book'),
    )
    title = models.CharField(max_length=50)
    publication_date = models.DateField(null=True)
    author = models.CharField(max_length=30, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    pages = models.IntegerField(blank=True, null=True)
    book_type = models.PositiveSmallIntegerField(choices=BOOK_TYPES)

    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'