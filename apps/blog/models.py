from django.db import models
from ckeditor.fields import RichTextField

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name="Nombre de la categoria", max_length=100, null=False, blank=False)
    status = models.BooleanField('Categoria Activada/No Activada', default=True)
    created_at = models.DateField("Fecha de creción",auto_now=False, auto_now_add=True)
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name
    
class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name="Nombre del autor", max_length=255, null=False, blank=False)
    last_name = models.CharField("Apellidos del author", max_length=255, blank=False, null=False)
    facebook = models.URLField("Facebook", null=True, blank=True)
    twitter = models.URLField("Twitter", null=True, blank=True)
    instagram = models.URLField("Instagram", null=True, blank=True)
    website = models.URLField("Website", null=True, blank=True)
    email = models.EmailField("Email", null=False, blank=False)
    status = models.BooleanField('Author Activo/No Activo', default=True)
    created_at = models.DateField("Fecha de creción",auto_now=False, auto_now_add=True)
    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

    def __str__(self):
        return "{0}, {1}".format(self.name, self.last_name)
    
    
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Titulo', max_length=90, blank=False, null=False)
    slug = models.CharField('Slug', max_length=100, blank=False, null=False)
    description = models.CharField("Descripcion", max_length=110, blank=False, null=False)
    content = RichTextField()
    image = models.URLField(max_length=255, blank=False, null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    state = models.BooleanField("Publicado/No Publicado", default=True)
    created_at = models.DateField("Fecha de creacion", auto_now=False, auto_now_add=True)
    
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
    
    
    def __str__(self):
        return self.title