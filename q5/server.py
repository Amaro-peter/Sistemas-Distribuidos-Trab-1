import rpyc
import time
from rpyc.utils.server import ThreadedServer


class VectorService(rpyc.Service):
    def on_connect(self, conn):
        pass

    def on_disconnect(self, conn):
        pass

    def exposed_sum_vector(self, vector):
        start = time.perf_counter()
        result = sum(vector)
        end = time.perf_counter()
        print("Tempo de execução no servidor:", end - start)
        return result

    def exposed_sum_vector_bits(self, payload, n):
        # payload: bytes, n: int
        start = time.perf_counter()
        # Each int is 4 bytes, signed
        vector = [int.from_bytes(payload[i*4:(i+1)*4], byteorder="big", signed=True) for i in range(n)]
        result = sum(vector)
        end = time.perf_counter()
        print("Tempo de execução no servidor (bits):", end - start)
        return result

if __name__ == "__main__":
    print("Iniciando servidor na porta 18861...")
    server = ThreadedServer(VectorService, port=18861)
    server.start()