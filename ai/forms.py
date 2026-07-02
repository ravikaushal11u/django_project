from django import forms


class ChatForm(forms.Form):

    prompt=forms.CharField(
        widget=forms.Textarea(
            attrs={
                "rows":2,
                "placeholder":"Ask anything..."
            }
        )
    )