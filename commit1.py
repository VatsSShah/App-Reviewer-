class ReviewApp:
    def __init__(self):
        self.reviews = {}

    def add_review(self, product_id, user_id, rating, comment):
        if product_id not in self.reviews:
            self.reviews[product_id] = []

        self.reviews[product_id].append({
            'user_id': user_id,
            'rating': rating,
            'comment': comment
        })

    def get_reviews(self, product_id):
        if product_id not in self.reviews:
            return []

        return self.reviews[product_id]

# Example usage:
app = ReviewApp()

# Adding reviews for a product
app.add_review('product_1', 'user_1', 4, "Great product!")
app.add_review('product_1', 'user_2', 5, "Amazing!")

# Retrieving reviews for a product
product_reviews = app.get_reviews('product_1')
for review in product_reviews:
    print(f"User {review['user_id']} rated {review['rating']}. Comment: {review['comment']}")
