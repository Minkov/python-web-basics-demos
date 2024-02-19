from django import forms

from exam_prep_my_music_app.profiles.models import Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("username", "email", "age")

        widgets = {
            "username": forms.TextInput(
                attrs={
                    "placeholder": "Username"
                },
            ),
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Email"
                },
            ),
            "age": forms.NumberInput(
                attrs={
                    "placeholder": "Age",
                },
            )
        }
