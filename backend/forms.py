from django.forms import ModelForm
from backend.models import producttable
class productform(ModelForm):
    class Meta:
        model=producttable
        fields=['image']