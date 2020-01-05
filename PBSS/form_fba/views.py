from django.shortcuts import render, redirect
from form_fba.forms import FbaForm
from form_fba.models import Fba
from django.views.generic import TemplateView

# Create your views here.


def std(request):
    if request.method == "POST":
        form = FbaForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/view')
            except:
                pass
    else:
        form = FbaForm()
    return render(request, 'fbaindex.html', {'form': form})


def view(request):
    form_fba = Fba.objects.all()
    return render(request, "view.html", {'form_fba': form_fba})

class fbaChart(TemplateView):
    template_name = 'charts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Fba.objects.all()
        return context