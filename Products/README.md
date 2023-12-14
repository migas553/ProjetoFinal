# ProjetoFinal
Projeto final para Fundamentos de Programacão

***
# Users APP
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
Nesta app, vai ser necessario criar os modelos, ou as nossas classes:

```python
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    description = models.CharField(max_length=100, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2,validators=[MinValueValidator(0)])
    stock = models.IntegerField(validators=[MinValueValidator(0)])
    timestamp = models.DateTimeField(auto_now_add=True)
```