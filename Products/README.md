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

-  `name = models.CharField(max_length=100, null=False)`, nome da categoria, CharField especifica um tipo string, comprimento maximo de 100 caractéres e null=False especifica que o campo é obrigatorio.


- `def __str__(self): return self.name`, representação da classe em tipo string.

#### Product



Antes de começar vou importar mais um modulo para este ficheiro:
```python
from django.core.validators import MinValueValidator
```




Este argumento em certos atributos vai fazer validaçõ mas diretamente a nivel de base de dados.

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
- `category = models.ForeignKey(Category, on_delete=models.PROTECT)`, um produto vai ter uma categoria, especificado pela sua foreign key, tambem obrigatório definir o modo de eliminação, neste caso é usado o protect para não apagar a categoria toda ao apagar um produto .
- `price = models.DecimalField(max_digits=10, decimal_places=2,validators=[MinValueValidator(0)])`, para preço podia se utilizar um float, mas o django tem solução melhor, Decimal Field, onde podemos especificar o numero de casas decimais que queremos, tambem temos um validador para os preços >= 0.
- `stock = models.IntegerField(validators=[MinValueValidator(0)])`, define um atributo int e stock >= 0 .
- `photo = models.ImageField(upload_to='product_photos/', null=True, blank=True)`, imagem do produto, guardada numa pasta no diretorio principal.





Registar os modelos no ficheiro **`admin.py`**:

```python
admin.site.register(Category)
admin.site.register(Product)
```

# Views


Definir a nossa homepage no ficheiro **`views.py`**

```python
from django.shortcuts import render

# Create your views here.
def frontpage(request):
    return render(request, 'Products/frontpage.html')
```

Começamos por importar a função `render`, esta função renderiza o modelo .html com os dados especificos.

Definimos a função `frontpage`, com o argumento de entrada `request`. O objecto `request` contem informaçoes do pedido html.

Como `return` executamos a função `render`, com o primeiro parametro ser o `request`e o segundo parametro é uma string onde se encontra o ficheiro .html da pagina em questão.

Resumo do chatgpt:
```Em resumo, quando um usuário acessa a página associada a essa view, o Django renderiza o template 'frontpage.html' e retorna o HTML resultante como parte da resposta à solicitação HTTP. Este é um padrão comum em aplicativos da web Django, onde as views são responsáveis por processar solicitações e renderizar templates para criar as respostas que serão enviadas de volta ao navegador do cliente.```

Para alem disso é necessário definir no **`urls.py`** do projecto:

```python
from django.contrib import admin
from django.urls import path,include
from Products.views import frontpage

urlpatterns = [
    path('',frontpage, name='frontpage'),
    path('admin/', admin.site.urls),
    ]
```
O que isto faz é para quando a pagina principal, neste caso vai ser o root directory do projecto tambem definido por **`''`**, chama a função `frontpage` importada de `Products.views` .

