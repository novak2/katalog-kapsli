from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Brewery(models.Model):
    name = models.CharField(max_length=130)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return '%s'  % (self.name)

    class Meta:
        ordering = ['name']


class Coin(models.Model):
    index = models.CharField(max_length=4, default='_')
    wiki_index = models.CharField(max_length=4, default='_')
    year = models.IntegerField()
    signature = models.CharField(max_length=15)
    image = models.ImageField(max_length=130)
    brewery = models.ForeignKey(Brewery, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s %s %s'  % (self.year, self.wiki_index, self.brewery, self.index, self.signature)

    class Meta:
        ordering = ['brewery', 'index', 'year', 'wiki_index']


class UserCoinKind(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return '%s'  % (self.name)


class UserCoinCondition(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return '%s'  % (self.name)


class UserCoinType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return '%s'  % (self.name)


class UserCoin(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)
    user_image = models.ImageField(max_length=130, blank=True, null=True)
    condition = models.ForeignKey(UserCoinCondition, on_delete=models.CASCADE)
    types = models.ForeignKey(UserCoinType, on_delete=models.CASCADE)
    kind = models.ForeignKey(UserCoinKind, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s %s %s'  % (self.coin.year, self.coin.wiki_index, self.coin.brewery, self.coin.index, self.coin.signature)

    class Meta:
        ordering = ['-coin__year', '-coin__wiki_index', '-coin__index']


class IgnoreCoin(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)

    def __str__(self):
        return '%s ' 'ignore' ' %s'  % (self.owner, self.coin)

    class Meta:
        unique_together = ("owner", "coin")