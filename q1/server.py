import rpyc
from rpyc.utils.server import ThreadedServer

class MyService(rpyc.Service):
    def on_connect(self, conn):
        # executado quando uma conexão é iniciada
        pass

    def on_disconnect(self, conn):
        # executado quando uma conexão é finalizada
        pass

    def exposed_get_answer(self): 
        # este é um método exposto
        return 42

    exposed_the_real_answer_though = 43 # este é um atributo exposto

    def get_question(self): 
        # este método NÃO é exposto (não tem o prefixo exposed_)
        return "Qual é a cor do cavalo branco de Napoleão?"

if __name__ == "__main__":
    print("Iniciando servidor na porta 18861...")
    t = ThreadedServer(MyService, port=18861)
    t.start()