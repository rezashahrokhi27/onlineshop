from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [_('first_name'), _('last_name'), _('phone_number'), _('address'), _('order_notes'), ]
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
            'order_notes': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': _('If you have any notes please enter here otherwise leave it empty')
            }),
        }
