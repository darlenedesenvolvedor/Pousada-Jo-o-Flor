
## Criar e ativar o ambiente virtual
1 - Crie o ambiente virtual
```console
virtualenv .venv
```

2 - Ative o ambiente virtual
```console
# Bash
source .venv/bin/activate
# Power Shell
./.venv/bin/activate.ps1
```

3 - Faça download das dependencias
```console
pip install -r requirements.txt
```

## Iniciar o localhost
4 - Inicie o localhost
```console
# Debug
flask run
# Gunicorn
gunicorn backend:'create_app()'
```

Endpoint http://127.0.0.1:5000/
