# Eureka - Digital Guidebook for Improvisation in the Ear Training Classroom 
## Quick Start 
Use `make dev`. This is equivalent to running Django's `./manage.py runserver` in one shell and Webpack in another. The output from both will be printed to the shell. Use CTR-C to exit.

To test, use `make all`. This is what Travis and Jenkins runs to build the project.

### Static Assets
This project diverges from the standard CTL project layout. The `media/js` and `media/css` directories have been removed in favor of `media/src`. Compiled assets are written to `media/build`.

To compile these assets during development, run `make webpack`.

## Make Targets for Development
### Overview
Eureka relies on a number of different technologies during development:
- Webpack to compile ES6 into a single js asset.
- Webpack also compiles SCSS files to CSS, along with generated source maps
- Cypress for client-side testing

During development, you'll need to run Django's server and Webpack for most development tasks. In addition, you may want to run Cypress in its headed mode, so that you can validate your client-side tests as you write.

To that end, you can run each of these in separate shells: `make runserver`, `make webpack`, and optionally `make cypress-open`.

### Kitchen Sink
For a kitchen sink approach, use `make cypress`. This will bring up `make integrationserver`, `make webpack`, and `make cypress-open` in a single shell. CTR-C will exit all three processes.

### Port Already Bound Errors
It's possible that `make dev` and `make cypress` don't clean up their constituent processes on exit. In particular, if you try to start Django's server and you get an error that the port is already bound, use `ps aux | grep runserver` to get the process and kill it manually.

### Make Target Explanations
Selected explanations of various make targets

#### django.mk Make Targets
- `make test`: runs all Python tests
- `make runserver`: runs Django's dev server, using local database settings
- `make integrationserver`: runs Django's dev server, except that it uses a test database populated with data created from factory methods

#### js.mk Make Targets
- `make eslint`: Runs ESLint on project.
- `make webpack`: Runs Webpack in watch mode, watches files and rebuilds on change.
- `make cypress-run`: Runs Cypress tests in headless mode, does not bring up test server. Use this when you want to run headless Cypress tests against a running test server. 
- `make cypress-open`: Runs Cypress tests in headed mode, does not bring up test server. Use this when you want to run Cypress during dev.
- `make cypress-test`: Runs Cypress tests in headless mode, uses `make integrationserver`. Use this for CI testing, or if you'd like to run Cypress tests before creating a PR.
- `make cypress-watch`: Runs `make integrationserver`, `make webpack`, and `make cypress-open` all at once. It will only output text from Cypress; so it's not as useful as `make dev`.

