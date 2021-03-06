from django_extensions.db.fields.json import JSONField as _JSONField
from django import forms

from jsoneditor.forms import JSONEditor

class JSONFormField(forms.CharField):
    widget = JSONEditor
    def __init__(self,*av,**kw):
        kw['widget'] = self.widget # force avoiding widget override
        super(JSONFormField,self).__init__(*av,**kw)


class JSONField(_JSONField):
    def formfield(self, **kwargs):
        defaults = {
            'form_class': kwargs.get('form_class', JSONFormField),
        }
        defaults.update(kwargs)
        return super(JSONField, self).formfield(**defaults)
