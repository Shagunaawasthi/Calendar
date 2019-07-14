from django.forms import ModelForm, DateInput
from django import forms
from cal.models import Event,Detail

class EventForm(ModelForm):
  class Meta:
    model = Detail
    # format to make date time show on fields
    widgets = {
      'AP': DateInput(attrs={'type': 'date-local'}, format='%Y-%m-%d'),
      'Ramadaan': DateInput(attrs={'type': 'date-local'}, format='%Y-%m-%d'),
    }
    fields = '__all__'

  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    # input to datetime field
    self.fields['AP'].input_formats = ('%Y-%m-%d',)
    self.fields['Ramadaan'].input_formats = ('%Y-%m-%d',)
