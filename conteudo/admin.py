from django.contrib import admin
from .models import Cargo, Team, Features, Post, Service, Showcase, Pricing, Testimonial, Espaco


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ['profissao']


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cargo', 'facebook', 'twitter', 'gmail', 'imagem']


@admin.register(Features)
class FeaturesAdmin(admin.ModelAdmin):
    list_display = ['features']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'texto', 'tempo_leitura', 'data', 'imagem']

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'texto', 'icone']

@admin.register(Showcase)
class ShowcaseAdmin(admin.ModelAdmin):
    list_display = ['imagem']

@admin.register(Pricing)
class PricingAdmin(admin.ModelAdmin):
    list_display =['instalation','storage', 'tamanho', 'user','tamanho', 'bandwith','features', ]

@admin.register(Testimonial)
class TestimonyAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'depoimento', 'imagem']


@admin.register(Espaco)
class EspacoAdmin(admin.ModelAdmin):
    list_display = ['tamanho','band']