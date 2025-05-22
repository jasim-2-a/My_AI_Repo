import hashlib
import time

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)
        return hashlib.sha256(value.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_data):
        last_block = self.get_latest_block()
        new_block = Block(len(self.chain), new_data, last_block.hash)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            curr = self.chain[i]
            prev = self.chain[i - 1]

            if curr.hash != curr.calculate_hash():
                return False

            if curr.previous_hash != prev.hash:
                return False

        return True

if __name__ == "__main__":
    my_chain = Blockchain()

 
    my_chain.add_block("First transaction")
    my_chain.add_block("Second transaction")

    
    for block in my_chain.chain:
        print(f"Index: {block.index}")
        print(f"Timestamp: {time.ctime(block.timestamp)}")
        print(f"Data: {block.data}")
        print(f"Hash: {block.hash}")
        print(f"Previous Hash: {block.previous_hash}\n")

   
    print("Is blockchain valid?", my_chain.is_chain_valid())
