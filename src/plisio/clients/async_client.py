"""
Async client for Plisio API.
"""

# pylint: disable=unused-argument


from aiohttp import ClientSession as _Session

from ._base import BaseClient as _BaseClient
from .. import _types as _t
from .. import exceptions as _e
from ..enums import Methods as _Methods


class AsyncClient(_BaseClient):
    """
    Async client for Plisio API.
    """

    def _init_session(self) -> _t.AsyncRequestSession:
        headers = self._get_headers()
        return _Session(
            headers=headers,
        )

    async def _handle_response(  # type: ignore[override] # pylint: disable=invalid-overridden-method
        self, response: _t.AsyncRequestResponse
    ) -> _t.Result:
        """
        Handle response.

        Args:
            response (Response): Response.

        Returns:
            Response: Response.

        Raises:
            PlisioRequestException: If request failed.
            PlisioAPIException: If API returned error.
        """

        if not 200 <= response.status < 300:
            raise _e.PlisioAPIException(response, response.status, await response.text())

        try:
            data: _t.Result = await response.json()
        except ValueError as exc:
            txt: str = await response.text()
            raise _e.PlisioRequestException(f"Invalid JSON response: {txt}") from exc

        return data

    async def _request(  # type: ignore[override, no-untyped-def] # pylint: disable=invalid-overridden-method
        self, method: _t.Methods, uri: _t.Text, force_params: bool = False, **kwargs
    ) -> _t.Result:
        """
        Make request.

        Args:
            method (Methods): Method.
            uri (str): Path.
            force_params (bool): Force params.
            **kwargs: Arguments.

        Returns:
            dict: Response data.

        Raises:
            PlisioRequestException: If request failed.
            PlisioAPIException: If API returned error.
        """
        requests_kwargs = self._get_request_kwargs(method, force_params, **kwargs)

        async with getattr(self._session, str(method).lower())(uri, **requests_kwargs) as response:
            return await self._handle_response(response)

    async def _get(  # type: ignore[override, no-untyped-def] # pylint: disable=invalid-overridden-method
        self, path: _t.Text, version: _t.Text = _BaseClient.API_VERSION_V1, **kwargs
    ) -> _t.Result:
        """
        Make GET request.

        Args:
            path (str): Path.
            version (str): API version.
            **kwargs: Arguments.

        Returns:
            dict: Response data.

        Raises:
            PlisioRequestException: If request failed.
            PlisioAPIException: If API returned error.
        """
        uri = self._get_uri(path, version)
        return await self._request(_Methods.GET, uri, **kwargs)

    async def _post(  # type: ignore[override, no-untyped-def] # pylint: disable=invalid-overridden-method
        self, path: _t.Text, version: _t.Text = _BaseClient.API_VERSION_V1, **kwargs
    ) -> _t.Result:
        """
        Make POST request.

        Args:
            path (str): Path.
            version (str): API version.
            **kwargs: Arguments.

        Returns:
            dict: Response data.

        Raises:
            PlisioRequestException: If request failed.
            PlisioAPIException: If API returned error.
        """

        uri = self._get_uri(path, version)
        return await self._request(_Methods.POST, uri, **kwargs)

    async def _put(  # type: ignore[override, no-untyped-def] # pylint: disable=invalid-overridden-method
        self, path: _t.Text, version: _t.Text = _BaseClient.API_VERSION_V1, **kwargs
    ) -> _t.Result:
        """
        Make PUT request.

        Args:
            path (str): Path.
            version (str): API version.
            **kwargs: Arguments.

        Returns:
            dict: Response data.

        Raises:
            PlisioRequestException: If request failed.
            PlisioAPIException: If API returned error.
        """

        uri = self._get_uri(path, version)
        return await self._request(_Methods.PUT, uri, **kwargs)

    async def _delete(  # type: ignore[override, no-untyped-def] # pylint: disable=invalid-overridden-method
        self, path: _t.Text, version: _t.Text = _BaseClient.API_VERSION_V1, **kwargs
    ) -> _t.Result:
        """
        Make DELETE request.

        Args:
            path (str): Path.
            version (str): API version.
            **kwargs: Arguments.

        Returns:
            dict: Response data.

        Raises:
            PlisioRequestException: If request failed.
            PlisioAPIException: If API returned error.
        """

        uri = self._get_uri(path, version)
        return await self._request(_Methods.DELETE, uri, **kwargs)

    async def invoice(  # pylint: disable=too-many-arguments, too-many-locals
        self,
        order_name: _t.Text,
        currency: _t.Currencies,
        amount: _t.NumberLike,
        order_number: _t.NumberLike,
        source_currency: _t.OptionalFiats = None,
        source_amount: _t.OptionalNumberLike = None,
        allowed_psys_cids: _t.OptionalPsysCids = None,
        description: _t.OptionalText = None,
        callback_url: _t.OptionalLink = None,
        success_callback_url: _t.OptionalLink = None,
        fail_callback_url: _t.OptionalLink = None,
        email: _t.OptionalEmail = None,
        language: _t.OptionalText = "en_US",
        plugin: _t.OptionalText = None,
        version: _t.OptionalText = None,
        redirect_to_invoice: _t.OptionalBool = None,
        expire_min: _t.OptionalNumberLike = None,
    ) -> _t.Result:
        """
        Create invoice.

        See Also:
            https://plisio.net/documentation/endpoints/create-an-invoice

        Args:
            order_name (str): Order name.
            order_number (int): Order number.
            currency (str): Currency.
            amount (float): Amount.
            source_currency (str): Source currency.
            source_amount (float): Source amount.
            allowed_psys_cids (list): Allowed payment systems.
            description (str): Description.
            callback_url (str): Callback URL.
            success_callback_url (str): Success callback URL.
            fail_callback_url (str): Fail callback URL.
            email (str): Email.
            language (str): Language.
            plugin (str): Plugin.
            version (str): Version.
            redirect_to_invoice (bool): Redirect to invoice.
            expire_min (int): Expire minutes.

        Returns:
            dict: Response data.

        Raises:
            PlisioRequestException: If request failed.
            PlisioAPIException: If API returned error.
        """

        params = self._get_params(locals())
        return await self._get("invoices/new", data=params, force_params=True)

    async def transactions(  # pylint: disable=too-many-arguments
        self,
        page: _t.OptionalNumberLike = None,
        limit: _t.OptionalNumberLike = None,
        shop_id: _t.OptionalNumberLike = None,
        type: _t.OptionalTransactionStatus = None,  # pylint: disable=redefined-builtin
        status: _t.OptionalTransactionStatus = None,
        currency: _t.OptionalCurrencies = None,
        search: _t.OptionalText = None,
    ) -> _t.Result:
        """
        Get transactions.

        See Also:
            https://plisio.net/documentation/endpoints/transactions

        Args:
            page (int): Page.
            limit (int): Limit.
            shop_id (int): Shop ID.
            type (str): Type.
            status (str): Status.
            currency (str): Currency.
            search (str): Search.

        Returns:
            dict: Response data.

        Raises:
            PlisioRequestException: If request failed.
            PlisioAPIException: If API returned error.
        """

        params = self._get_params(locals())
        return await self._get("operations", data=params, force_params=True)

    async def withdraw(  # pylint: disable=too-many-arguments
        self,
        currency: _t.Currencies,
        type: _t.WithdrawType,  # pylint: disable=redefined-builtin
        to: _t.Text,  # pylint: disable=invalid-name
        amount: _t.NumberLike,
        fee_plan: _t.OptionalFeePlans = None,
    ) -> _t.Result:
        """
        Withdraw.

        See Also:
            https://plisio.net/documentation/endpoints/withdrawal-mass-withdrawal

        Args:
            currency (str): Currency.
            type (str): Type.
            to (str): To.
            amount (int): Amount.
            fee_plan (str): Fee plan.

        Returns:
            dict: Response data.

        Raises:
            PlisioRequestException: If request failed.
            PlisioAPIException: If API returned error.
        """

        params = self._get_params(locals())
        return await self._get("operations/withdraw", data=params, force_params=True)

    async def transaction_details(self, id: _t.Text) -> _t.Result:  # pylint: disable=invalid-name
        """
        Get transaction details.

        See Also:
            https://plisio.net/documentation/endpoints/transaction-details

        Args:
            id (str): Transaction ID.

        Returns:
            dict: Response data.

        Raises:
            PlisioRequestException: If request failed.
            PlisioAPIException: If API returned error.
        """

        return await self._get(f"operations/{id}")

    async def balance(self, psys_cid: _t.OptionalCurrencies = None) -> _t.Result:
        """
        Get balance.

        See Also:
            https://plisio.net/documentation/endpoints/balance

        Args:
            psys_cid (str): Payment system CID.

        Returns:
            dict: Response data.

        Raises:
            PlisioRequestException: If request failed.
            PlisioAPIException: If API returned error.
        """

        return await self._get("balance/", data={"psys_cid": psys_cid}, force_params=True)

    async def fee_plans(self, psys_cid: _t.Currencies) -> _t.Result:
        """
        Get fee plans.

        See Also:
            https://plisio.net/documentation/endpoints/fee-plans

        Args:
            psys_cid (str): Payment system CID.

        Returns:
            dict: Response data.

        Raises:
            PlisioRequestException: If request failed.
            PlisioAPIException: If API returned error.
        """

        return await self._get(f"operations/fee-plan/{psys_cid}")

    async def fee_estimation(
        self,
        currency: _t.OptionalCurrencies = None,
        addresses: _t.OptionalListStr = None,
        amounts: _t.OptionalListNumberLike = None,
        fee_plan: _t.OptionalFeePlans = None,
    ) -> _t.Result:
        """
        Fee estimation.

        See Also:
            https://plisio.net/documentation/endpoints/fee-estimation

        Args:
            currency (str): Currency.
            addresses (list): Addresses
            amounts (list): Amounts.
            fee_plan (str): Fee plan.

        Returns:
            dict: Response data.

        Raises:
            PlisioRequestException: If request failed.
            PlisioAPIException: If API returned error.
        """

        params = self._get_params(locals())
        return await self._get("operations/fee", data=params, force_params=True)

    async def plisio_fee(  # pylint: disable=too-many-arguments
        self,
        currency: _t.OptionalCurrencies = None,
        addresses: _t.OptionalListStr = None,
        amounts: _t.OptionalListNumberLike = None,
        type: _t.OptionalTransactionType = None,  # pylint: disable=redefined-builtin
        fee_plan: _t.OptionalFeePlans = None,
    ) -> _t.Result:
        """
        Plisio fee.

        See Also:
            https://plisio.net/documentation/endpoints/plisio-fee

        Args:
            currency (str): Currency.
            addresses (list): Addresses
            amounts (list): Amounts.
            type (str): Type.
            fee_plan (str): Fee plan.

        Returns:
            dict: Response data.

        Raises:
            PlisioRequestException: If request failed.
            PlisioAPIException: If API returned error.
        """
        params = self._get_params(locals())
        return await self._get("operations/plisio-fee", data=params, force_params=True)

    async def crypto_coins(self) -> _t.Result:
        """
        Get crypto coins.

        See Also:
            https://plisio.net/documentation/endpoints/crypto-coins

        Returns:
            dict: Response data.

        Raises:
            PlisioRequestException: If request failed.
            PlisioAPIException: If API returned error.
        """

        return await self._get("crypto-coins")
