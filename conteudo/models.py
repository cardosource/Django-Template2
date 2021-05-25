from django.db import models
from stdimage.models import  StdImageField
import uuid
def utilizando_imagem(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename
class Cargo(models.Model):
    cargo = (
        ('designer', 'Designer'),
        ('engineer', 'Support Engineer'),
        ('developer', 'Front-end Developer'),
        ('witer', 'Content Writer')
    )
    icone = models.CharField(max_length=50, choices=cargo)
    profissao = models.CharField(max_length=50)

    def __str__(self):
        return self.profissao

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'


class Team(models.Model):
    nome = models.CharField(max_length=50)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    facebook = models.CharField(max_length=50, default='#')
    twitter = models.CharField(max_length=50, default='#')
    gmail = models.CharField(max_length=50, default='#')
    imagem = models.ImageField(upload_to='imagens')

    def __str__(self):
        return f'{self.nome}{self.cargo}{self.facebook}{self.facebook}{self.twitter}{self.gmail}'

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'


class Features(models.Model):
    servicosDisponivel = (
        ('lni-coffee-cup', 'coffee-cup'),
        ('lni-invention', 'invention'),
        ('lni-reload', 'reload'),
        ('lni-briefcase', 'briefcase'),
        ('lni-layers', 'layers'),
        ('lni-support', 'support')
    )
    icone = models.CharField(max_length=50, choices=servicosDisponivel)
    titulo = models.CharField(max_length=100)
    featuresintroducao = models.TextField(max_length=1000)
    features = models.TextField(max_length=1000)

    def __str__(self):
        return self.features

    class Meta:
        verbose_name = 'Feature'
        verbose_name_plural = 'Features'


class Post(models.Model):
    titulo = models.CharField(max_length=50)
    texto = models.TextField(max_length=150)
    tempo_leitura = models.IntegerField()
    data = models.DateTimeField(auto_now=True)
    imagem = models.ImageField(upload_to='imagens/blog/')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return f'{self.texto}{self.texto}{self.texto}{self.data}'


class Service(models.Model):
    iconeservice = (
        ('lni-cog', 'cog'),
        ('lni-brush', 'brush'),
        ('lni-heart', 'heart')
    )
    titulo = models.CharField(max_length=50)
    texto = models.TextField(max_length=500)
    icone = models.CharField(max_length=20, choices=iconeservice)

    def __str__(self):
        return f'{self.texto}{self.texto}{self.iconeservice}'

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

class Showcase(models.Model):
    imagem = models.ImageField(upload_to='imagens/showcase/')
    class Meta:
        verbose_name = 'Show Case'
        verbose_name_plural = 'Show Cases'
    def __str__(self):
        return f'{self.imagem}'


class Espaco(models.Model):
    tamanho = models.CharField(max_length=10)
    band = models.CharField(max_length=10)
    def __str__(self):
        return f'{self.tamanho}{self.band}'

class Pricing(models.Model):
    titulo = models.CharField(max_length=25)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    instalation = models.CharField(max_length=10)
    storage = models.IntegerField()
    user = models.CharField(max_length=10)
    bandwith = models.CharField(max_length=10)
    features = models.CharField(max_length=10)
    dashboar = models.CharField(max_length=10)
    tamanho = models.ForeignKey(Espaco, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Pricing'
        verbose_name_plural = 'Pricings'

    def __str__(self):
        return f'{self.titulo}{self.preco}{self.instalation}' \
               f'{self.storage}{self.user}{self.bandwith}{self.features}' \
               f'{self.tamanho}{self.band}{self.dashboar}'

class Testimonial(models.Model):
    cliente = models.CharField(max_length=50)
    imagem =StdImageField(upload_to=f'imagens/testimonial/{utilizando_imagem}', variations={'thumb': {'width':480,'height':480,'crop':True}})

    depoimento = models.TextField(max_length=300)
    class Meta:
        verbose_name ='Testimony'
        verbose_name_plural = 'Testimonials'
    def __str__(self):
        return f'{self.cliente}{self.depoimento}{self.imagem}'