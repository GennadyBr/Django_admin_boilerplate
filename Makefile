up:
	docker compose down --remove-orphans -v
	docker compose up -d --build
	docker system prune -a --force

down:
	docker compose down --remove-orphans -v
	docker system prune -a --force

lint:
	poetry run flake8 .
	poetry run mypy .
