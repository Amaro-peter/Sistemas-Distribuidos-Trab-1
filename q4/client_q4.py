import rpyc
import sys

def main():
    # Get vector size from user
    n = int(input("Enter vector size: "))
    
    # Create vector with elements from 0 to n-1
    vector = list(range(n))
    
    # Connect to server
    conn = rpyc.connect("localhost", 18861)
    server = conn.root
    
    # Call server procedure to sum vector elements
    result = server.sum_vector(vector)
    
    # Print the sum
    print(f"Sum: {result}")
    
    conn.close()

if __name__ == "__main__":
    main()