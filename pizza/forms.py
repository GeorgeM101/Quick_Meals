from django import forms
from .models import Pizza,Size

# class PizzaForm(forms.Form):
#     topppings = forms.MultipleChoiceField(choices=[('pep','Pepperoni'),('cheese','Cheese'),('olives','Olives')], widget=forms.CheckboxSelectMultiple)
#     size = forms.ChoiceField(label='Size',choices=[('Small'),('Medium'),('Large')])

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['topping1','topping2','size']
        labels = {'topping1': 'Topping 1', 'topping2': 'Topping 2'}

class MultiplePizzaForm(forms.Form):
    number = forms.IntegerField(min_value=2, max_value=5)
