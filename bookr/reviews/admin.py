from django.contrib import admin
from reviews.models import (Book, Publisher, Contributor,
                            BookContributor, Review)


# ------------------BookAdmin class -------------------------
class BookAdmin(admin.ModelAdmin):
    date_hierarchy = 'publication_date'
    list_display = ('title', 'isbn13', 'publication_date', 'has_isbn')
    list_filter = ('publisher', 'publication_date')
    search_fields = ('title', 'isbn', 'publisher__name')

    @admin.display(
        ordering='isbn',
        description='ISBN-13',
        empty_value='-/-'
    )
    def isbn13(self, obj):
        """
        Returns the ISBN 13 string.

        '9780316769174' => '978-0-31-67917-4'
        """
        return f"{obj.isbn[:3]}-{obj.isbn[3:4]}-{obj.isbn[4:6]}-{obj.isbn[6:12]}-{obj.isbn[12:13]}"

    @admin.display(
        boolean=True,
        description='Has ISBN',
    )
    def has_isbn(self, obj):
        """ '978031679174' => True """
        return bool(obj.isbn)


# ------------------ReviewAdmin class -------------------------
class ReviewAdmin(admin.ModelAdmin):
    fieldsets = ((None, {'fields': ('creator', 'book')}),
                 ('Review content',
                  {'fields': ('content', 'rating')}))


@admin.display(
    description='Publisher',
)
def initialled_name(obj):
    """
        obj.first_name='Jerome David', obj.last_name='Salinder' => 'Salinder, JD'
        """
    initials = ''.join([name[0] for name in obj.first_name.split(' ')])
    return f"{obj.last_name}, {initials}"


class ContributorAdmin(admin.ModelAdmin):
    list_display = (initialled_name, "first_name", "last_name")
    list_filter = ('last_name',)
    search_fields = ('first_name', 'last_name')


# Register models:
admin.site.register(Publisher)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor)
admin.site.register(Review, ReviewAdmin)