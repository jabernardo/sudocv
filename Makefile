BIN = sudocv.py

build:
	pyinstaller $(BIN) --onefile --noconfirm

all: build