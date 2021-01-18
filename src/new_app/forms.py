from django import forms
from .models import Link

class LinkForm(forms.ModelForm):

    def save(self, commit=True):
        instance = super(LinkForm, self).save(commit=False)
        if not Link.objects.filter(old_link=self.cleaned_data['old_link']):
            instance.save()
        return instance
    
    class Meta:
        model = Link
        exclude = ("new_link",)

    