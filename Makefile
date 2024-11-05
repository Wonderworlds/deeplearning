DATASET_URL := https://cdn.intra.42.fr/document/document/22562/data.csv
python := python3

define venvWrapper
	{\
	. bin/activate; \
	$1; \
	}
endef

DATASET_DIR := datasets
DATASET := $(DATASET_DIR)/data.csv
SRC_DIR := src
APP_FILE := $(SRC_DIR)/streamlit_app.py

help:
	@echo "Usage: make [target]"
	@echo "Targets:"
	@echo "  start:    	 Run the project"
	@echo "  install:    Install the project"
	@echo "  freeze:     Freeze the dependencies"
	@echo "  fclean:     Remove the virtual environment and the datasets"
	@echo "  clean:      Remove the cache files"
	@echo "  re:         Reinstall the project"
	@echo "  phony:      Run the phony targets"

start:
	$(call venvWrapper, streamlit run $(APP_FILE))


install:
	@{ \
		echo "Setting up..."; \
		python3 -m venv .; \
		. bin/activate; \
		if [ -f requirements.txt ]; then \
			pip install -r requirements.txt; \
			echo "Installing dependencies...DONE"; \
		fi; \
	}

freeze:
	$(call venvWrapper, pip freeze > requirements.txt)

fclean: clean
	rm -rf bin/ include/ lib/ lib64 pyvenv.cfg share/ datasets/ etc/

clean:
	rm -rf src/__pycache__ src/*/__pycache__

re: fclean install

phony: install freeze fclean clean re help