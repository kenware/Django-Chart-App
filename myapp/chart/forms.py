from django import forms
CHOICES = (("Job","Job",), ("Vacancy","Vacancy",), ("Hobies","Hobies",), ("Music","Music",),
        ("Movies","Movies",),( "Music_Video","Music_Video",), ("Politics","Politics",),
           ("Sports","Sports",),("Admission","Admission",),("others","others",))
class ChannelForm(forms.Form):
    channel=forms.CharField(label='Channel Name ', max_length=100)
    category=forms.CharField(label='Category', widget=forms.Select(choices=CHOICES))
    
class SearchForm(forms.Form):
    search=forms.CharField(label='Search Channnels',widget=forms.TextInput(attrs={'placeholder':'Type in keyword'}))
    
class ChatForm(forms.Form):
    message=forms.CharField(label='message',widget=forms.Textarea(attrs={'cols':'25','rows':'3'}))
    username=forms.CharField(label='username ',widget=forms.TextInput(attrs={'placeholder':'username','size':'24'}))
