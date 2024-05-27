# A helper method that will be used to calculate the average rating of a book
def average_rating(rating_list):
    if not rating_list:
        return 0

    return round(sum(rating_list) / len(rating_list))
