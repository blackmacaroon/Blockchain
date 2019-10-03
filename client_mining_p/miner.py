import hashlib
import requests

import sys


# Implement functionality to search for a proof 
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
    while valid_proof(block_string, proof) is False:
        proof += 1
    print("mine?")
    return proof

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
        the_last_proof = requests.get('/last_block').json()
        print("doin somdething")   
        # TODO: When found, POST it to the server {"proof": new_proof}
        # TODO: We're going to have to research how to do a POST in Python
        # HINT: Research `requests` and remember we're sending our data as JSON
        response_obj = requests.post('/mine')
        # TODO: If the server responds with 'New Block Forged'
        if response_obj.json()['message'] == "New Block Forged":
            # add 1 to the number of coins mined and print it.  Otherwise,
            coins_mined += 1
            print(f"{coins_mined} coins")
        else:
            # print the message from the server.
            print(res.json()['message'])
