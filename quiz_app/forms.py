from django import forms

class QuizForm(forms.Form):
    user_answer = forms.CharField(max_length=255)