from django.db import models

# Create your models here.
class RatingChoice(models.TextChoices):
    G = "G"
    PG = "PG"
    PG13 = "PG-13"
    R = "R"
    NC17 = "NC-17"

class Movie(models.Model):
    title = models.CharField(max_length=127, null=False)
    duration = models.CharField(max_length=10, null=True, default=None)
    rating = models.CharField(max_length=20, choices=RatingChoice.choices, default=RatingChoice.G)
    synopsis = models.TextField(null=True, default=None)
    user = models.ForeignKey(
        "users.Account",
        on_delete=models.CASCADE,
        related_name="movies",
    )

def __repr__(self) -> str:
    return f"<Movie [{self.id}] - {self.title}>"



class MovieOrder(models.Model):
    buyed_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    buyer = models.ForeignKey("users.Account", on_delete=models.CASCADE,related_name="movies_orders")
    movie = models.ForeignKey("movies.Movie", on_delete=models.CASCADE, related_name="movies_orders")

def __repr__(self) -> str:
    return f"<Movie Order [{self.id}] - {self.price}>"