from .models import Hotel, Room
from modeltranslation.translator import (TranslationOptions, register)


@register(Hotel)
class ProductTranslationOptions(TranslationOptions):
    fields = ('hotel_name', 'description')


@register(Room)
class ProductTranslationOptions(TranslationOptions):
    fields = ('room_number', 'room_description')
