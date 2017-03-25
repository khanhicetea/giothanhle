from django import forms
from django.contrib import admin
from .models import Area, Church, MassTime
from .helpers import renderMassTimesToString, parseMassTimes

class AreaAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')


class ChurchForm(forms.ModelForm):
    mass_times = forms.CharField(max_length=255, widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ChurchForm, self).__init__(*args, **kwargs)
        self.initial['mass_times'] = renderMassTimesToString(self.instance.masses)

    def save(self, commit=True):
        mass_times = self.cleaned_data.get('mass_times', None)
        mass_time_data = parseMassTimes(mass_times)
        masses = [MassTime(**m) for m in mass_time_data]
        self.instance.masses.all().delete()
        self.instance.masses.set(masses, bulk=False, clear=True)
        return super(ChurchForm, self).save(commit=commit)

    class Meta:
        fields = '__all__'
        model = Church


class ChurchAdmin(admin.ModelAdmin):
    form = ChurchForm
    fields = ('name', 'address', 'area', 'location', 'website', 'mass_times')
    list_display = ('name', 'address', 'area')


class MassTimeAdmin(admin.ModelAdmin):
    list_display = ('church', 'day_of_week', 'time')


admin.site.register(Area, AreaAdmin)
admin.site.register(Church, ChurchAdmin)
admin.site.register(MassTime, MassTimeAdmin)