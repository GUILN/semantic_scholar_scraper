BIN_NAME=sem_scraper

dev:
	poetry run $(BIN_NAME)

format:
	poetry run black ./

install_pre_commit:
	poetry run pre-commit install