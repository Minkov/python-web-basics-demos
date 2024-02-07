from django import forms

from class_based_views_basics.web.models import Todo


class TodoBaseForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = "__all__"

    def clean_title(self):
        pass

    # def save(self, commit=True):
