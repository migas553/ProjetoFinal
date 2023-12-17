# ProjetoFinal
Projeto final para Fundamentos de Programacão

***
# Virtual environment: 


Porquê ambiente virtual? 

- **Isolamento de Dependências**: Cada projeto pode ter suas próprias bibliotecas, sem interferir em outros projetos.
  
- **Versatilidade**: Permite testar diferentes versões de bibliotecas sem afetar o ambiente global.

- **Segurança**: Cria uma camada adicional de isolamento, evitando potenciais riscos associados à instalação de bibliotecas desconhecidas no sistema global.

- **Portabilidade**: Facilita a exportação e reprodução do ambiente de desenvolvimento em outros sistemas ou máquinas.


### Para criar o virtual environment:



```bash
python -m venv venv
```

Para activar o virtual environment usar:


```bash
venv\Scripts\activate
```

**Caso de erro** ao executar o comando anterior, existe a possibilidade de o windows não deixar executar scripts, para corrigir isso temos que abrir um terminal com previlegios de administrador e executar:
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned 
```

***
# Dependências:

Agora existe 2 opções, instalar o django, ou caso exista um ficheiro de requirements instalar apartir dai.

### Instalar só django
Com o ambiente virtual instalado e **activado**:

```bash
pip install django
```

### Dependencias apartir de um ficheiro 

Para instalar as dependencias apartir do ficheiro:
```bash
pip install -r requirements.txt
```

Ao longo de um projecto é possivel que comecem a aumentar o numero de modulos adicionais, para os registar no ficheiro usa-se:

```bash
pip freeze > requirements.txt
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

Para verificar se temos o django a funcionar precisamos de:

### Iniciar a base de dados

A informação da base de dados encontra-se no ficheiro **`settings.py`**
Neste primeiro caso vamos manter a base de dados padrão, SQLlite
Para a sua inicialização e futuros updates usamos :

```bash
python manage.py migrate
```
### Aceder ao painel admin

Para aceder ao admin pannel e necessario criar uma conta:
```bash
python manage.py createsuperuser
```


### Iniciar servidor

Na linha de comandos usamos:
```bash
python manage.py runserver
```
Se tudo estiver em condições o servidor vai iniciar e podemos testar no seguinte endereço:
```bash
http://127.0.0.1:8000/
#ou para pasta admin
http://127.0.0.1:8000/admin
```
Se tudo correr bem vai ser apresentado uma mensage, de boas vindas.
Para parar o servidor na linha de comandos usamos a combinação de **CTRL + C**

## Iniciar suoeruser
Para aceder ao admin pannel e necessario criar uma conta:
```bash
python manage.py createsuperuser
```

