from django import forms 
from .models import Author, Book, BookFiles

class AuthorForm(forms.ModelForm):    
    class Meta:
        model = Author
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(AuthorForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class BookForm(forms.ModelForm):
    pub_data = forms.DateField(widget=forms.DateInput(attrs={'type': 'date',})) 

    class Meta:
        model = Book
        exclude = ()
        
    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs) 
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        self.fields['created_date'].label = ''
        self.fields['created_date'].widget = forms.HiddenInput()

class BookFilesForm(forms.ModelForm): 
    class Meta:
        model = BookFiles
        exclude = () 
        
    def __init__(self, *args, **kwargs):
        super(BookFilesForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        
BookFilesFormSet = forms.inlineformset_factory(
    Book, 
    BookFiles,
    form=BookFilesForm, 
    fields=['created_file'],
    extra=1, 
    can_delete=True
)