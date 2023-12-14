# ProjetoFinal
Projeto final para Fundamentos de Programacão

***
# Users APP
Para criar uma app em django utiliza-se o seguinte comando:

```bash
python manage.py startapp Users
```

Isto vai produzir a seguinte estrutura:

```bash
Farmacia
├── Users
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
    'Users',
]
```
Nesta app, vai ser necessario criar os modelos, ou as nossas classes:

