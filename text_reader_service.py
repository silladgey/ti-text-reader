from concurrent import futures
import logging

import grpc
import text_reader_pb2
import text_reader_pb2_grpc

from utils import constants

logging.basicConfig(level=logging.INFO)


class TextReaderService(text_reader_pb2_grpc.TextReaderServicer):
    """Provides methods that implement functionality of TextReader service."""

    def __init__(self, file_path):
        """Initializes the TextReaderService with the path to the file to read."""
        self.file_path = file_path
        self.words = self._load_words()
        logging.info("Loaded %d words from %s", len(self.words), file_path)

    def _load_words(self):
        """Loads the words from the file and returns them as a list."""
        with open(self.file_path, "r", encoding="utf-8") as file:
            text = file.read()
        return text.split()

    def GetNextWord(self, request, context):
        """Returns the next word from the file."""
        if not self.words:
            logging.info("Reached end of file")
            return text_reader_pb2.WordResponse(word="", eof=True)
        word = self.words.pop(0)
        logging.info("Sending word: %s", word)
        return text_reader_pb2.WordResponse(word=word, eof=False)


def serve():
    """Starts the gRPC server to serve the TextReader service."""
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    text_reader_service = TextReaderService(constants.BOOK_PATH)
    text_reader_pb2_grpc.add_TextReaderServicer_to_server(text_reader_service, server)
    PORT = 50051
    server.add_insecure_port(f"[::]:{PORT}")
    logging.info("Starting server on port %d", PORT)
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
