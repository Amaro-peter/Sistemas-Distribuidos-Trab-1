import rpyc
import sys
import time

def serialize_vector_bits(vector):
    # 32 bits por inteiro (signed)
    return b"".join(x.to_bytes(4, byteorder="big", signed=True) for x in vector)

def main():
    n = int(input("Enter vector size: "))
    vector = list(range(n))

    if len(sys.argv) >= 3:
        host = sys.argv[1]
        port = int(sys.argv[2])
    else:
        host = "localhost"
        port = 18861

    conn = rpyc.connect(host, port)
    server = conn.root

    payload = serialize_vector_bits(vector)

    start = time.perf_counter()
    # Envia bytes + tamanho do vetor
    result = server.sum_vector_bits(payload, n)
    end = time.perf_counter()

    print(f"Sum: {result}")
    print("Tempo de execução no cliente:", end - start)

    conn.close()

if __name__ == "__main__":
    main()