# ProjetoFinal
Projeto final para Fundamentos de Programacão

***
# Products APP
Para criar uma app em django utiliza-se o seguinte comando:

```bash
python manage.py startapp Products
```

Isto vai produzir a seguinte estrutura:

```bash
Farmacia
├── Products
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
```

Esta app tambem precisa de ser inserida no ficheiro **`settings.py`** da pasta de projecto, na seguinte parte:

```bash
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Products',
]
```
# Models

No ficheiro **`models.py`** é onde definimos as classes do nosso projecto para depois serem instanciadas no nosso painel admin.

Se todos os passos anteriores terem sidos executados com sucesso no ficheiro **`models.py`** temos algo semelhante a isto:


```python
from django.db import models

# Create your models here.
```
Apartir de agora podemos pegar no nosso diagrama de classes e desenhar os atributos das nossas classes.
Estas vão seguir a estrutura de django, e os varios métodos incluidos de models.
Nesta app vamos ter 2 models:

### Category

```python
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    def __str__(self):
        return self.name
```
- `id = models.AutoField(primary_key=True)` , Isto vai gerar o id ,e subsequentemente, a Primary Key da classe.

-  `name = models.CharField(max_length=100, null=False)`, nome da categoria, CharField especifica um tipo string, comprimento maximo de 100 caractéres e null=False especifica que o campo é obrigatorio

- `def __str__(self): return self.name`, representação da classe em tipo string

#### Product

Antes de começar vou importar mais um modulo para este ficheiro:
```python
from django.core.validators import MinValueValidator
```
Este argumento em certos atributos vai fazer validaçõ mas diretamente a nivel de base de dados

```python
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    description = models.CharField(max_length=100, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2,validators=[MinValueValidator(0)])
    stock = models.IntegerField(validators=[MinValueValidator(0)])
    photo = models.ImageField(upload_to='product_photos/', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
```
Para alem dos atributos iguais a Category, temos mais alguns diferentes:
- `category = models.ForeignKey(Category, on_delete=models.PROTECT)`, um produto vai ter uma categoria, especificado pela sua foreign key, tambem obrigatório definir o modo de eliminação, neste caso é usado o protect para não apagar a categoria toda ao apagar um produto 
- `price = models.DecimalField(max_digits=10, decimal_places=2,validators=[MinValueValidator(0)])`, para preço podia se utilizar um float, mas o django tem solução melhor, Decimal Field, onde podemos especificar o numero de casas decimais que queremos, tambem temos um validador para os preços >= 0
- `stock = models.IntegerField(validators=[MinValueValidator(0)])`, define um atributo int e stock >= 0 
- `photo = models.ImageField(upload_to='product_photos/', null=True, blank=True)`, imagem do produto, guardada numa pasta no diretorio principal






Registar os modelos no ficheiro **`admin.py`**:

```python
admin.site.register(Category)
admin.site.register(Product)
```


