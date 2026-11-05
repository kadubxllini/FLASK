# Estudos com Flask

Exercício para aprender a ligar um formulário HTML a uma aplicação Python. A página recebe nome e idade, salva os registros em SQLite e mostra a lista cadastrada.

O código usa Flask, Flask-SQLAlchemy e um template em `templates/`.

## Rodar localmente

Em um ambiente virtual Python:

```sh
python -m pip install flask flask-sqlalchemy
python app.py
```

Abra `http://127.0.0.1:5000`. A tabela é criada na inicialização pelo SQLAlchemy.

É um projeto de estudo. O servidor está configurado com debug e não há autenticação ou controle de acesso para uso público.
