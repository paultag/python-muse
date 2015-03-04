all: help

help:
	@echo "Current targets:"
	@echo ""
	@echo "  test"

test:
	py.test --cov muse tests/
