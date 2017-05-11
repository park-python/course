from django.db import models
import cent


class Country(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "country"

    def __str__(self):
        return self.name


class Label(models.Model):
    title = models.CharField(max_length=255)
    country = models.ForeignKey(
        Country, blank=True, null=True)

    def __str__(self):
        return self.title


class Auto(models.Model):
    BODY_HATCH = 0
    BODY_SEDAN = 1
    BODY_SUV = 2

    BODY_CHOICES = (
        (BODY_HATCH, "хетчбек"),
        (BODY_SEDAN, "седан"),
        (BODY_SUV, "внедорожник"),
    )

    label = models.ForeignKey(Label)
    name = models.CharField(max_length=255)
    year = models.IntegerField()
    body = models.IntegerField(choices=BODY_CHOICES)
    color = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images", blank=True, null=True)

    def calculate_income(self):
        income = self.sale_set.aggregate(total=models.Sum("price"))
        return income.get('total') or 0

    def get_full_name(self):
        return self.__str__()

    def __str__(self):
        return "{} {} {} ({})".format(self.label.title, self.name, self.get_body_display(), self.color)


class Dealer(models.Model):
    name = models.CharField(max_length=255)
    autos = models.ManyToManyField(Auto)

    def __str__(self):
        return self.name


class Sale(models.Model):
    price = models.IntegerField(default=0)
    auto = models.ForeignKey(Auto)

    def __str__(self):
        return self.auto.__str__()

    def push_income(self):
        client = cent.Client("http://localhost:9000", "secret", timeout=1)
        try:
            client.publish("updates", {
                "item": self.auto.id,
                "value": self.auto.calculate_income()
            })
        except cent.CentException:
            pass

    def delete(self, **kwargs):
        super(Sale, self).delete(**kwargs)
        self.push_income()

    def save(self, **kwargs):
        super(Sale, self).save(**kwargs)
        self.push_income()
