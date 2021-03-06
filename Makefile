format:
	black . --exclude checkpoint --exclude wandb --exclude save
	isort . --skip checkpoint --skip wandb --skip save

test:
	black . --check --exclude checkpoint --exclude wandb --exclude save
	isort . --check-only --skip checkpoint --skip wandb --skip save
	env PYTHONPATH=. pytest --pylint --flake8 --mypy --ignore=checkpoint --ignore=wandb --ignore=save --ignore=config

dev:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt
	pre-commit install

dep:
	pip install -r requirements.txt

docker-push:
	docker build -t jmarpledev/model_compression .
	docker push jmarpledev/model_compression
