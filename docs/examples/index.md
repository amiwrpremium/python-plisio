# Examples

Here are some examples which help you to get started with the library.

## Initiate

You can initiate the client with or without request params.

??? note "See Also"

    Code Reference: [Client](../reference/clients)

=== "Sync"

    ```python title="client.py" linenums="1"
    from plisio import Client

    client = Client("<API_KEY>")
    ```

=== "Async"

    ```python title="client.py" linenums="1"
    import asyncio
    from plisio import AsyncClient

    client = AsyncClient("<API_KEY>")
    ```

=== "With Request Params"

    ``` python title="with_request_params.py" linenums="1"
    from plisio import Client

    client = Client("<API_KEY>", requests_params={
        "timeout": 10
    })
    ```

=== "Async With Request Params"

    ``` python title="async_with_request_params.py" linenums="1"
    import asyncio
    from plisio import AsyncClient

    client = AsyncClient("<API_KEY>", requests_params={
        "timeout": 10
    })
    ```

## Transactions

Query transactions.

??? note "See Also"

    Sync Code Reference: [Client.transactions](../reference/clients#src.plisio.clients.client.Client.transactions)
    Async Code Reference: [AsyncClient.transactions](../reference/clients#src.plisio.clients.async_client.AsyncClient.transactions)

    API Reference: [Transactions](https://plisio.net/documentation/endpoints/transactions)

=== "Sync"

    ```python title="get_transactions.py" linenums="1"
    def main():
        transactions = client.transactions()

        print(transactions)


    main()
    ```

=== "Async"

    ``` python title="get_transactions.py" linenums="1"
    async def main():
        transactions = await client.transactions()

        print(transactions)


    asyncio.run(main())
    ```

```shell title="output" linenums="1"
{'status': 'success', 'data': {'operations': [], '_links': {'self': {'href': 'https://plisio.net/api/v1/operations?api_key=By3QOfFqVu3w8mH7BZm5QO3T-Gq4fVnAaaCz790zFoLVamWWsR24ON_HlGUbjScd&page=1&per-page=10'}}, '_meta': {'totalCount': 0, 'pageCount': 0, 'currentPage': 1, 'perPage': 10}}}
```

## Create Invoice

Create an invoice.

??? note "See Also"

    Sync Code Reference: [Client.invoice](../reference/clients#src.plisio.clients.client.Client.invoice)
    Async Code Reference: [AsyncClient.invoice](../reference/clients#src.plisio.clients.async_client.AsyncClient.invoice)

    API Reference: [Create Invoice](https://plisio.net/documentation/endpoints/create-an-invoice)

=== "Sync"

    ```python title="create_invoice.py" linenums="1"
    def main():
        invoice = client.invoice(
            order_name="test",
            order_number="test",
            amount=1,
            currency="BTC",
        )

        print(invoice)


    main()
    ```

=== "Async"

    ```python title="create_invoice.py" linenums="1"
    async def main():
        invoice = await client.invoice(
            order_name="test",
            order_number="test",
            amount=1,
            currency="BTC",
        )

        print(invoice)


    asyncio.run(main())
    ```

```shell title="output" linenums="1"
{'status': 'success', 'data': {'txn_id': '6470c20600b6719c3f063d59', 'invoice_url': 'https://plisio.net/invoice/6470c20600b6719c3f063d59', 'invoice_total_sum': '1.00000000'}}
```