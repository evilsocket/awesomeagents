www/index.json:
	@python3 scripts/make_index.py > www/index.json

all: www/index.json