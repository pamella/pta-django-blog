# [PTA | CITi | 2018.2] Getting started with Django! :rocket:

Este repositório contém o projeto completo do treinamento de Django dado por mim e [Gabriela](https://github.com/gabrielaleal) para os trainees de 2018.2 do [CITi](http://citi.org.br/).

Links de referência:

https://github.com/pamella/pta-django/blob/master/README.md

https://djangogirls.org/

## Como utilizar
* Clone o projeto para seu computador
  ```bash
  $ git clone https://github.com/pamella/pta-django-blog
  ```
* Inicie um ambiente virtual e instale as dependências
  ```bash
  $ python -m virtualenv venv
  $ source venv/bin/activate
  $ pip install -r requirements.txt
  ```
* Rode as migrações
  ```bash
  $ python manage.py migrate
  ```
* Inicie o servidor
  ```bash
  $ python manage.py runserver
  ```
* Para deletar as pastas pycache
  ```bash
  $ make clean
  ```
