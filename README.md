# nulspy-requests

A python >=3.7 library to make NULS 2.0 JSON-RPC calls. These calls are available via interfaces including curl, Postman, html-api, websockets, etc. However, by using these Python libraries, you can create scripts that allow you to make multiple changes at once. 

For instance, you can create a set of 100 account and transfer tokens into them in one simple pass.

This project was inspired by the need to create multiple accounts and fund them quickly for blockchains used by students at Portland State University in 2020.

Each NULS 2.0 node can optionally provide a set of API interfaces for obtaining blockchain data from nodes. The interface is provided through JSON-RPC, and the underlying layer communicates using HTTP protocol.

Some of the calls you can make with this library are:

- contractCall
- createAccount
- getAccountBalance
- getAccountList
- getAccountLedgerList
- getAddressByPriKey
- getBestBlockHeader
- getChainInfo
- getPriKey
- getTx
- importPriKey
- imputedContractCallGas
- transfer
- writeReview

See the official NULS document on using JSON-RPC calls with NULS blockchains:  https://docs.nuls.io/Docs/i_nuls-api_JSONRPC.html








