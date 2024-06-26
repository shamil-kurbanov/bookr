from django.contrib import auth
from django.db import models


class Publisher(models.Model):
    """ A company that publishes books. """
    name = models.CharField(max_length=50, help_text="The name of the Publisher")
    website = models.URLField(help_text="The website of the Publisher")
    email = models.EmailField(help_text="The publisher's email address")

    def __str__(self):
        return self.name


class Book(models.Model):
    """A published book."""
    title = models.CharField(max_length=70, help_text="The title of the book")
    publication_date = models.DateField(verbose_name='Date the book was published')
    isbn = models.CharField(max_length=20, verbose_name="ISBN number of the book")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    contributors = models.ManyToManyField('Contributor', through='BookContributor')

    def isbn13(self):
        """
        Returns the ISBN 13 string.

        '9780316769174' => '978-0-31-67917-4'
        """
        return f"{self.isbn[:3]}-{self.isbn[3:4]}-{self.isbn[4:6]}-{self.isbn[6:12]}-{self.isbn[12:13]}"

    def __str__(self):
        return self.title


class Contributor(models.Model):
    """ A person who contributes to a book, e.g. author, editor, co-author."""
    first_name = models.CharField(max_length=50, help_text="The contributor's first name or names")
    last_name = models.CharField(max_length=50, help_text="The contributor's last name")
    email = models.EmailField(help_text="The contact email for the contributor")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class BookContributor(models.Model):
    class ContributionRole(models.TextChoices):
        AUTHOR = 'AUTHOR', 'Author'
        CO_AUTHOR = 'CO_AUTHOR', 'Co-author'
        EDITOR = 'EDITOR', 'Editor'

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    role = models.CharField(verbose_name="The role this contributor had in the book",
                            choices=ContributionRole.choices, max_length=20)

    def __str__(self):
        return f"{self.contributor} - {self.role}"


class Review(models.Model):
    content = models.TextField(help_text="The Review content")
    rating = models.IntegerField(help_text="The rating the reviewer has given")
    date_created = models.DateTimeField(auto_now_add=True, help_text="The date and time the review was created")
    date_edited = models.DateTimeField(null=True, help_text="The date and time the review was last edited")
    creator = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, help_text="The book that this review is for")
