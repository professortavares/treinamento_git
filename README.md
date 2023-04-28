# Treinamento git
Repositório para o treinamento do git

## Dev.:

### Instruções de instalação

1. Criar o ambiente virtual (venv)

```bash
python3 -m venv venv
```

2. Ativar o ambiente virtual

```bash
. venv/bin/activate
```

Se você tiver usando windows:

```bash
venv\Scripts\activate.bat
```

Para desativar o ambiente:

```bash
deactivate
```

3. Instalar as dependências

```bash
pip install -r requirements.txt
```

Se precisar atualizar o ambiente (requirements.txt):

```bash
pip install --upgrade --force-reinstall -r requirements.txt
```

5. Instalar o projeto

```bash
pip install -e .
```

6. Rodar testes de unidade:

```bash
pytest
```

7. Rodar cobertura de teste:

```bash
pytest --cov=treinamento_git --cov-report=html
```

