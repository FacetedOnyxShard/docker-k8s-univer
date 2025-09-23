.PHONY: dev
dev:
	@uvicorn todo:app --reload

.PHONY: start
start:
	@uvicorn todo:app

.PHONY:
	@yapf -i todo.py