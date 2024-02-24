from django import forms
from .models import Video


class VideoCreateForm(forms.ModelForm):

    class Meta:
        model = Video
        fields = ('title', 'description', 'thumbnail', 'upload')
        # 少しツウな書き方
        widgets = {
            'title': forms.TextInput(attrs={  # <input type="text" class="form-control"
                'class': 'form-control mb-3',
            }),
            'description': forms.Textarea(attrs={  # <textarea class="form-cotrol"
                'class': 'form-control mb-3',
            }),
            'thumbnail': forms.ClearableFileInput(attrs={  # <input type="file" class="form-control-file"
                'class': "form-control mb-3",
                'type': "file"
            }),
            'upload': forms.ClearableFileInput(attrs={
                'class': "form-control mb-3",
                'type': "file"
            }),
        }
