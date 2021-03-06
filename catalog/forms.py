import datetime

from catalog.models import BookInstance  # noqa: F401

from django import forms
from django.forms import ModelForm  # noqa: F401


class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        # Check if a date is not in the past.
        if data < datetime.date.today():
            raise forms.ValidationError('Invalid date - renewal in past')

        # Check if a date is in the allowed range (+4 weeks from today).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise forms.ValidationError('Invalid date - renewal more than 4 weeks ahead')

        # Remember to always return the cleaned data.
        return data


# class RenewBookModelForm(ModelForm):
#     def clean_due_back(self):
#         data = self.cleaned_data['due_back']
#
#         # Проверка того, что дата не в прошлом
#         if data < datetime.date.today():
#             raise forms.ValidationError('Invalid date - renewal in past')
#
#         # Check date is in range librarian allowed to change (+4 weeks)
#         if data > datetime.date.today() + datetime.timedelta(weeks=4):
#             raise forms.ValidationError('Invalid date - renewal more than 4 weeks ahead')
#
#         # Не забывайте всегда возвращать очищенные данные
#         return data
#
#     class Meta:
#         model = BookInstance
#         fields = ['due_back', ]
#         labels = {'due_back': 'Renewal date', }
#         help_texts = {'due_back': 'Enter a date between now and 4 weeks (default 3).', }
