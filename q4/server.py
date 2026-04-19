import rpyc
import sys
from rpyc.utils.server import ThreadedServer

class VectorService(rpyc.Service):
    def on_connect(self, conn):
        # executado quando uma conexão é iniciada
        pass

    def on_disconnect(self, conn):
        # executado quando uma conexão é finalizada
        pass

    def exposed_sum_vector(self, vector):
        return sum(vector)

if __name__ == "__main__":
    print("Iniciando servidor na porta 18861...")
    server = ThreadedServer(VectorService, port=18861)
    server.start()