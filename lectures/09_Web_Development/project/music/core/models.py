from django.db import models
import cent


class Genre(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Artist(models.Model):
    name = models.CharField(max_length=255)
    avatar = models.CharField(max_length=255, blank=True, null=True)
    genres = models.ManyToManyField(Genre, blank=True, null=True)

    def calculate_capital(self):
        capital = self.ruble_set.aggregate(nominal=models.Sum("nominal"))
        return capital.get('nominal') or 0

    def __str__(self):
        return self.name


class Ruble(models.Model):
    nominal = models.IntegerField(default=1)
    artist = models.ForeignKey(Artist, blank=True, null=True)

    def __str__(self):
        return "{} ({})".format(self.nominal, self.artist.name)

    def push_capital(self):
        client = cent.Client("http://localhost:9000", "secret", timeout=1)
        try:
            client.publish("updates", {
                "artist": self.artist.id,
                "capital": self.artist.calculate_capital()
            })
        except cent.CentException:
            pass

    def delete(self, **kwargs):
        super(Ruble, self).delete(**kwargs)
        self.push_capital()

    def save(self, **kwargs):
        super(Ruble, self).save(**kwargs)
        self.push_capital()
