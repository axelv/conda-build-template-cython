

# Build the container
build: ## Build the container
	docker build -t conda-build .

build-nc: ## Build the container without caching
	docker build --no-cache -t conda-build .

run: ## Run container on port configured in `config.env`
	docker run -i -t --rm --name="conda-build" conda-build
