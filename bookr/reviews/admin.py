from django.contrib import admin

from bookr.reviews.models import (Book, Publisher,
                                  Contributor, BookContributor, Review)

# Register models:
admin.site.register(Publisher)
admin.site.register(Contributor)
admin.site.register(Book)
admin.site.register(BookContributor)
admin.site.register(Review)
