APP=sprezzatura
JS_FILES=media/js/src media/js/tests

all: jenkins cypress-test

include *.mk

integrationserver: check
	$(MANAGE) integrationserver --addrport $(INTERFACE):$(RUNSERVER_PORT) --noinput

webpack: $(JS_SENTINAL)
	npm run dev

cypress-run: $(JS_SENTINAL)
	npm run cypress:run

cypress-open: $(JS_SENTINAL)
	npm run cypress:open

cypress-test: $(JS_SENTINAL)
	npm run cypress:test

cypress-watch: $(JS_SENTINAL)
	npm run cypress:watch 

dev:
	trap 'kill 0' EXIT; make runserver & make webpack

cypress:
	trap 'kill 0' EXIT; make integrationserver & make webpack & make cypress-open

.PHONY: integrationserver webpack cypress-run cypress-open cypress-test cypress-watch dev cypress
