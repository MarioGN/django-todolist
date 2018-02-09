from django import forms

from .models import Task


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('text',)

        widgets = {
            'text': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'New task'}
            ),
        }


class TaskEditForm(forms.Form):

    id_field = forms.CharField(widget=forms.HiddenInput())
    text = forms.CharField(
        label='Description',
        widget=forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        required=True,
    )
