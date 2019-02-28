from django import forms
from django.core.mail import send_mail
from blog.models import Comment

# class EmailPostForm(forms.Form):
# 	your_name = forms.CharField(max_length = 230)
# 	#email = forms.EmailField()
# 	your_email = forms.EmailField()
# 	to = forms.EmailField()
# 	message = forms.CharField(required = False,widget = forms.Textarea)


# 	def send_email(self, url_name):
#          # send email using the self.cleaned_data dictionary
# 		your_name = self.cleaned_data.get('your_name')
# 		to = self.cleaned_data.get('to')
# 		your_email = self.cleaned_data.get('your_email')
# 		message = str(self.cleaned_data.get('message'))+url_name
# 		send_mail( your_name,message,your_email,[to],fail_silently=False,)


class CommentForm(forms.ModelForm):
    
    
    class Meta:
        model = Comment
        fields = ('name', 'comment')
