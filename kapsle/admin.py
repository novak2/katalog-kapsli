from django.contrib import admin
from .models import Coin, UserCoin, Brewery, UserCoinType, UserCoinKind, UserCoinCondition, IgnoreCoin

admin.site.register(Coin)
admin.site.register(UserCoin)
admin.site.register(Brewery)
admin.site.register(UserCoinType)
admin.site.register(UserCoinKind)
admin.site.register(UserCoinCondition)
admin.site.register(IgnoreCoin)