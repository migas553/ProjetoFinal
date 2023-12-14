# ProjetoFinal
Projeto final para Fundamentos de Programacão

***
# Virtual environment: 


Porquê ambiente virtual? 

- **Isolamento de Dependências**: Cada projeto pode ter suas próprias bibliotecas, sem interferir em outros projetos.
  
- **Versatilidade**: Permite testar diferentes versões de bibliotecas sem afetar o ambiente global.

- **Segurança**: Cria uma camada adicional de isolamento, evitando potenciais riscos associados à instalação de bibliotecas desconhecidas no sistema global.

- **Portabilidade**: Facilita a exportação e reprodução do ambiente de desenvolvimento em outros sistemas ou máquinas.


Para activar o virtual environment usar:

```bash
venv\Scripts\activate
```

Com o ambiente virtual instalado e **activado**, começar por instalar dependencias:

```bash
pip install django
```

Para gravar os requesitos do projecto:

```bash
pip freeze > requirements.txt
```

Para instalar as dependencias apartir do ficheiro:
```bash
pip install -r requirements.txt
```

# Iniciar o projeto em django:

Para iniciar o projeto usamos o comando:

```bash
django-admin startproject Farmacia .
```
Isto vai a aplicaçao django para iniciar o projeto com o nome farmacia, o ponto na linha de codigo faz com que o projecto seja criado no directorio atual e não numa subpasta

## Com isto criamos o nosso projecto e temos a seguinte estrutura:

```bash
ProjetoFinal
├── manage.py 
├── Farmacia
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py 
│   ├── urls.py
│   └── wsgi.py
├── venv
│   └── ...
└── requirements.txt
```


Vamos dar uma olhada nos principais arquivos e diretórios criados:

- **`ProjetoFinal/`**: Diretório principal do projeto.
  - **`manage.py`**: Utilizado para gerir o projeto. Ex: Executar migrações, iniciar o servidor de desenvolvimento, etc.
- **`Farmacia/`**: Diretório interno com as configurações do projeto.
    - **`settings.py`**: Configurações principais do projeto (base de dados, aplicações, etc.).
    - **`urls.py`**: Mapeamento das URLs do projeto para as views.
    - **`asgi.py` e `wsgi.py`**: Configurações para servidores web.
