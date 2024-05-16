# Nome do arquivo: Makefile

# Variáveis
ENV_FILE = .env
EXAMPLE_ENV_FILE = .env.example

# Comandos
.PHONY: help setup create-venv generate-secret-key install-deps migrate runserver

help:
	@echo "Comandos disponíveis:"
	@echo "  make setup                - Configura o ambiente de desenvolvimento"
	@echo "  make create-venv          - Cria o ambiente virtual"
	@echo "  make generate-secret-key  - Gera uma nova SECRET_KEY e adiciona ao arquivo .env"
	@echo "  make install-deps         - Instala as dependências"
	@echo "  make migrate              - Aplica as migrações"
	@echo "  make runserver            - Executa o servidor de desenvolvimento do Django"

setup: install-deps generate-secret-key migrate

create-venv:
	@echo "Criando ambiente virtual..."
	@python3 -m venv venv
	@echo "Ative o ambiente virtual com 'source venv/bin/activate' no Unix ou '.\venv\Scripts\activate' no Windows."

generate-secret-key:
	@if [ ! -f $(ENV_FILE) ]; then \
		cp $(EXAMPLE_ENV_FILE) $(ENV_FILE); \
	fi
	@SECRET_KEY=$$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'); \
	echo "SECRET_KEY=$$SECRET_KEY" >> $(ENV_FILE); \
	echo "SECRET_KEY gerada e adicionada ao arquivo .env"

install-deps:
	@echo "Instalando dependências..."
	venv/bin/pip install -r requirements.txt

migrate:
	@echo "Aplicando migrações..."
	venv/bin/python manage.py migrate

runserver:
	@echo "Iniciando o servidor de desenvolvimento..."
	venv/bin/python manage.py runserver

