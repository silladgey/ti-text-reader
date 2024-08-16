import logging

import grpc
import text_reader_pb2
import text_reader_pb2_grpc

from utils import constants

logging.basicConfig(level=logging.INFO)


def fetch_word(stub):
    """Returns the response from the server."""
    return stub.GetNextWord(text_reader_pb2.WordRequest())


def run():
    """Runs the client to communicate with the TextReader service."""
    with grpc.insecure_channel(constants.BASE_URL) as channel:
        stub = text_reader_pb2_grpc.TextReaderStub(channel)
        word_count = 0
        try:
            response = fetch_word(stub)
            while not response.eof:
                logging.info("Received word: %s", response.word)
                word_count += 1
                response = fetch_word(stub)

        except KeyboardInterrupt:
            logging.info("Stopped after receiving %d words.", word_count)


if __name__ == "__main__":
    run()
