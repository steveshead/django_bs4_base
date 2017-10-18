from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions)

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(required=True, widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('contact_name', placeholder="Full Name"),
            Field('contact_email', placeholder="Email Address"),
            Field('content', placeholder=""),
            Submit('sign_in', 'Submit', css_class="btn btn-info"),
            )
        self.fields['contact_name'].label = "Your name:"
        self.fields['contact_email'].label = "Your email:"
        self.fields['content'].label = "Your message:"
