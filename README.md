# ti-book-reader

Part of Text Insights (TI) project.

This service reads the classic book text file, extracts words and sentences, and sends each word to the analysis service via gRPC.

## Purpose

Reads the classic book text file and sends each word to the `ti-text-analyzer`.

## Functionality

- Reads the text file
- Extracts words and sentences
- Sends words to `ti-text-analyzer` via gRPC
