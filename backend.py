# backend py, talks to rxc node it used bitcoind rpc

from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import logging, datetime
rpc_host = '127.0.0.1'
rpc_port = '23505'
rpc_user="nemore"
rpc_password="nemore"


# create a new address for receiving payments

# create_address 
def create_address(discord_id):
    discord_id  = str(discord_id)
    logging.basicConfig()
    logging.getLogger('BitcoinRPC').setLevel(logging.DEBUG)
    rpc_connection = AuthServiceProxy('http://%s:%s@%s:%s'%(rpc_user, rpc_password, rpc_host, rpc_port))
    try:
        newaddress = rpc_connection.getnewaddress(discord_id)
        print("new address: %s" % newaddress)
        return newaddress
    except JSONRPCException as e:
        print("JSONRPC error: %s" % e.error['message'])

# get balance
def get_balance(discord_id):
    discord_id  = str(discord_id)

    logging.basicConfig()
    logging.getLogger('BitcoinRPC').setLevel(logging.DEBUG)
    rpc_connection = AuthServiceProxy('http://%s:%s@%s:%s'%(rpc_user, rpc_password, rpc_host, rpc_port))
    try:
        balance = rpc_connection.getbalance(discord_id)
        print("balance: %s" % balance)
        return balance
    except JSONRPCException as e:
        print("JSONRPC error: %s" % e.error['message'])

# send rxc: user to user
def send_rxc(discord_id, amount, address):
    discord_id  = str(discord_id)

    logging.basicConfig()
    logging.getLogger('BitcoinRPC').setLevel(logging.DEBUG)
    rpc_connection = AuthServiceProxy('http://%s:%s@%s:%s'%(rpc_user, rpc_password, rpc_host, rpc_port))
    try:
        txid = rpc_connection.sendfrom(discord_id, address, amount)
        print("txid: %s" % txid)
        return txid
    except JSONRPCException as e:
        print("JSONRPC error: %s" % e.error['message'])
    
# from discord id get address
def get_address(discord_id):
    discord_id  = str(discord_id)

    logging.basicConfig()
    logging.getLogger('BitcoinRPC').setLevel(logging.DEBUG)
    rpc_connection = AuthServiceProxy('http://%s:%s@%s:%s'%(rpc_user, rpc_password, rpc_host, rpc_port))
    try:
        address = rpc_connection.getaddressesbyaccount(discord_id)
        print("address: %s" % address)
        return address
    except JSONRPCException as e:
        print("JSONRPC error: %s" % e.error['message'])

# withdraw rxc
def withdraw_rxc(discord_id, amount, address):

    discord_id  = str(discord_id)
    logging.basicConfig()
    logging.getLogger('BitcoinRPC').setLevel(logging.DEBUG)
    rpc_connection = AuthServiceProxy('http://%s:%s@%s:%s'%(rpc_user, rpc_password, rpc_host, rpc_port))
    try:
        txid = rpc_connection.sendfrom(discord_id, address, amount)
        print("txid: %s" % txid)
        return txid
    except JSONRPCException as e:
        print("JSONRPC error: %s" % e.error['message'])


# address_user gets deposit address if one exists, if not it creates one
def address_user(discord_id):

    discord_id  = str(discord_id)
    logging.basicConfig()
    logging.getLogger('BitcoinRPC').setLevel(logging.DEBUG)
    rpc_connection = AuthServiceProxy('http://%s:%s@%s:%s'%(rpc_user, rpc_password, rpc_host, rpc_port))
    try:
        address = rpc_connection.getaddressesbyaccount(discord_id)
        if address == []:
            address = rpc_connection.getnewaddress(discord_id)
        else:
            address = address[0]
        print("address: %s" % address)
        return address
    except JSONRPCException as e:
        print("JSONRPC error: %s" % e.error['message'])

# tip discord id to discord id
def tip_user(discord_id_from, discord_id_to, amount):


    discord_id_from  = str(discord_id_from)
    discord_id_to  = str(discord_id_to)

    
    logging.basicConfig()
    logging.getLogger('BitcoinRPC').setLevel(logging.DEBUG)
    rpc_connection = AuthServiceProxy('http://%s:%s@%s:%s'%(rpc_user, rpc_password, rpc_host, rpc_port))
    try:
        txid = rpc_connection.sendfrom(discord_id_from, address_user(discord_id_to), amount)
        print("txid: %s" % txid)
        return txid
    except JSONRPCException as e:
        print("JSONRPC error: %s" % e.error['message'])