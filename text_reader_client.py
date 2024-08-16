import grpc
import text_reader_pb2
import text_reader_pb2_grpc


def run():
    """Runs the client to communicate with the TextReader service."""
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = text_reader_pb2_grpc.TextReaderStub(channel)
        while True:
            response = stub.GetNextWord(text_reader_pb2.WordRequest())
            if response.eof:
                print("Reached end of file")
                break
            print(f"Received word: {response.word}")


if __name__ == "__main__":
    run()
