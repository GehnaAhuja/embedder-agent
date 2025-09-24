# Minimal Makefile for sim build
BUILD_DIR := build
GEN_DIR := generated
SRC := $(GEN_DIR)/main.c
BIN := $(BUILD_DIR)/blinky

.PHONY: all build run clean

all: build

$(BIN): $(SRC)
	@mkdir -p $(BUILD_DIR)
	gcc -O2 -o $(BIN) $(SRC)

build: $(BIN)

run: build
	./$(BIN)

clean:
	rm -rf $(BUILD_DIR)
