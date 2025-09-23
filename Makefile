BASE_CMD = uvicorn todo:app

.PHONY: dev
dev:
	@$(BASE_CMD) --reload

.PHONY: start
start:
	@$(BASE_CMD)

.PHONY: format
format:
	@yapf -i todo.py

.PHONY: test
test:
	./test.sh
