BASE_CMD = uvicorn todo:app --port 8000

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
