from django.views.generic import TemplateView
from .models import Team, Features, Post, Service, Showcase, Pricing, Testimonial
class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        contexto = super(IndexView,self).get_context_data(**kwargs)
        contexto['team'] = Team.objects.all()
        contexto['feature'] = Features.objects.all()
        contexto['blog'] = Post.objects.all()
        contexto['service'] = Service.objects.all()
        contexto['showcases'] = Showcase.objects.all()
        contexto['pricings'] = Pricing.objects.all()
        contexto['testimony'] = Testimonial.objects.all()


        return contexto
class TesteView(TemplateView):
    template_name = 'paginas/404.html'