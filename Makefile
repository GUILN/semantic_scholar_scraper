BIN_NAME=sem_scraper

dev:
	poetry run $(BIN_NAME)

format:
	poetry run black ./

install_pre_commit:
	poetry run pre-commit install

live_test:
	poetry run $(BIN_NAME) --term "session-based recommendation" --key "your key here"
