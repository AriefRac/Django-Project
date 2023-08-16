
from django.views.generic import TemplateView

from artikel.views import ArtikelPerKategori

class BlogHomeView(TemplateView, ArtikelPerKategori):
    template_name = "index.html"

    def get_context_data(self,*args, **kwargs):
        querysets = self.get_latest_artikel_each_category()
        context = {
            'latest_artikel_list':querysets
        }        

        return context