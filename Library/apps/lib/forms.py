from django import forms
from .models import *


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class DebtorForm(forms.ModelForm):
    class Meta:
        model = Debtor
        fields = '__all__'


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class PublishingHouseForm(forms.ModelForm):
    class Meta:
        model = PublishingHouse
        fields = '__all__'
