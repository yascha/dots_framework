all: install-deps

install-deps:
	@echo "Installing dependencies..."
	sudo easy_install pip
	sudo pip install colorama
	@echo "Finished installing dependencies."

clean:
	rm *.pyc

.PHONY: all clean
