import hashlib
import requests

import sys


# TODO: Implement functionality to search for a proof 
def proof_of_work(block):
    """
    Simple Proof of Work Algorithm
    Find a number p such that hash(last_block_string, p) contains 6 leading
    zeroes
    :return: A valid proof for the provided block
    """
    block_string = json.dumps(block, sort_keys=True).encode()
    # return proof
    proof = 0
    while self.valid_proof(block_string, proof) is False:
        proof += 1
    return proof

def valid_proof(block_string, proof):
    #create proof
    guess = f'{block_string}{proof}'.encode()
    #hash proof
    guess_hash = hashlib.sha256(guess).hexdigest()
    # TODO TODO TODO TODO change back to 6 zeros TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO
    if guess_hash[:3] == "000":
        return True
    else:
        return False


if __name__ == '__main__':
    # What node are we interacting with?
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "http://localhost:5000"

    coins_mined = 0
    # Run forever until interrupted
    while True:
        # TODO: Get the last proof from the server and look for a new one
        # TODO: When found, POST it to the server {"proof": new_proof}
        # TODO: We're going to have to research how to do a POST in Python
        # HINT: Research `requests` and remember we're sending our data as JSON
        # TODO: If the server responds with 'New Block Forged'
            # add 1 to the number of coins mined and print it.  Otherwise,
            coins_mined += 1
            print(f"{coins_mined} coins")
        # print the message from the server.
        print(rers.json()['message'])
