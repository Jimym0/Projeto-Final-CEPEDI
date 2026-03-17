# Projeto-Final---CEPEDI

### Projeto de Tarefas

Este projeto tem como finalidade a conclusão da primeira fase do curso de backend-python da CEPEDI.
Sendo este um sistema simples de listas de tarefas.

### Funcionalidades

O sistema vai ser executado apartir do terminal mas funcionara interiamente em um navegador.

Sua principal funcionalidade é o cadastro de tarefas contendo o dia que a mesma foi criada e possuindo um prazo para a finalização, tendo a possibilidade de editar, comcluir a tarefa e excluir.

Possuindo tambem a função de login e cadastro que permite que as tarefas sejam exclusivas de seus respectivos usuarios.

### Tecnologias

- Django
- HTML
- Bootstrap
- SQLite

### Como usar


- Inicialização do ambiente virtual
 
```
python -m venv venv

.\venv\Scripts\Activate.ps1
```
*Caso o terminal aponte um erro de segurança utilize o seguinte comando e repita novamente a inicialização do venv

```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```

- Agora a instalação do requerimentos

```
pip install -r requirements.txt
```

- Logo apos inicie o projeto

```
python manage.py runserver
```
Agora o projeto esta pronto para ser usando as contas criadas e tarefas seram armazenadas localmente no banco de dados presente nos arquivos do projeto.
