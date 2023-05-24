"""
Base client class.
"""

from abc import (
    ABC as ABC,
    abstractmethod as abstractmethod,
)

from .. import _types as _t
from ..enums import Methods as _Methods


class BaseClient(ABC):
    """
    Base client class.
    """

    BASE_URL: str = "https://plisio.net/api"
    API_VERSION_V1: str = "v1"
    REQUEST_TIMEOUT: int = 10

    def __init__(self, api_key: _t.Text, requests_params: _t.RequestParams = None):
        """
        Initialize client.

        Args:
            api_key (str): API key.
            requests_params (RequestParams): Request params.
        """

        self.api_key = api_key
        self._session = self._init_session()
        self._requests_params = requests_params

    def _get_uri(self, path: _t.Text, version: _t.Text = API_VERSION_V1) -> _t.Text:
        """
        Get URI.

        Args:
            path (str): Path.
            version (str): API version.

        Returns:
            str: URI.
        """

        return f"{self.BASE_URL}/{version}/{path}"

    @staticmethod
    def _get_params(locals_: _t.DictStrAny, exclude_unset: bool = True) -> _t.DictStrAny:
        """
        Get params.

        Args:
            locals_ (dict): Locals.
            exclude_unset (bool): Exclude unset.

        Returns:
            dict: Params.
        """

        return {
            key: value
            for key, value in locals_.items()
            if key != "self" and not (exclude_unset and value is None)
        }

    @staticmethod
    def _get_headers() -> _t.Headers:
        """
        Get headers.

        Returns:
            Headers: Headers.
        """

        return {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    def _get_request_kwargs(self, method: _t.Methods, force_params: bool = False, **kwargs) -> _t.DictStrAny:
        """
        Get request kwargs.

        Args:
            method (Methods): Method.
            force_params (bool): Force params.
            **kwargs: Keyword arguments.

        Returns:
            dict: Request kwargs.
        """

        kwargs['timeout'] = self.REQUEST_TIMEOUT

        if self._requests_params:
            kwargs.update(self._requests_params)

        data = kwargs.pop("data", None)

        if data and isinstance(data, dict):
            kwargs['data'] = data

            if 'requests_params' in kwargs['data']:
                kwargs.update(kwargs['data']['requests_params'])
                del (kwargs['data']['requests_params'])

            kwargs['data']['api_key'] = self.api_key

        if data and (str(method).upper() == _Methods.GET or force_params):
            _ = ""
            for data in kwargs['data'].items():
                key = data[0]
                if isinstance(data[1], list):
                    value = ','.join(data[1])
                else:
                    value = data[1]

                _ += f"{key}={value}&"

            kwargs['params'] = _.rstrip('&')
            del (kwargs['data'])

        return kwargs

    @abstractmethod
    def _init_session(self) -> _t.Session:
        """
        Initialize session.

        Returns:
            Session: Session.
        """

        raise NotImplementedError

    @abstractmethod
    def _handle_response(self, response: _t.Response) -> _t.Result:
        """
        Handle response.

        Args:
            response (Response): Response.

        Returns:
            Response: Response.
        """

        raise NotImplementedError

    @abstractmethod
    async def _request(
            self,
            method: _t.Methods,
            uri: _t.Text,
            force_params: bool = False,
            **kwargs
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

        raise NotImplementedError

    @abstractmethod
    def _get(
            self,
            path: _t.Text,
            version: _t.Text = API_VERSION_V1,
            **kwargs,  # type: ignore[untyped-definition]
    ) -> _t.Result:
        """
        Make GET request.

        Args:
            path (str): Path.
            version (str): API version.

        Returns:
            dict: Response data.
        """

        raise NotImplementedError

    @abstractmethod
    def _post(
            self,
            path: _t.Text,
            version: _t.Text = API_VERSION_V1,
            **kwargs,  # type: ignore[untyped-definition]
    ) -> _t.Result:
        """
        Make POST request.

        Args:
            path (str): Path.
            version (str): API version.

        Returns:
            dict: Response data.
        """

        raise NotImplementedError

    @abstractmethod
    def _put(
            self,
            path: _t.Text,
            version: _t.Text = API_VERSION_V1,
            **kwargs,  # type: ignore[untyped-definition]
    ) -> _t.Result:
        """
        Make PUT request.

        Args:
            path (str): Path.
            version (str): API version.

        Returns:
            dict: Response data.
        """

        raise NotImplementedError

    @abstractmethod
    def _delete(
            self,
            path: _t.Text,
            version: _t.Text = API_VERSION_V1,
            **kwargs,  # type: ignore[untyped-definition]
    ) -> _t.Result:
        """
        Make DELETE request.

        Args:
            path (str): Path.
            version (str): API version.

        Returns:
            dict: Response data.
        """

        raise NotImplementedError

    @abstractmethod
    def invoice(  # pylint: disable=too-many-arguments
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
            language: _t.OptionalText = 'en_US',
            plugin: _t.OptionalText = None,
            version: _t.OptionalText = None,
            redirect_to_invoice: _t.OptionalBool = None,
            expire_min: _t.OptionalNumberLike = None
    ) -> _t.Result:
        """
        Create invoice.

        Args:
            order_name (str): Order name.
            order_number (int): Order number.
            currency (str): Currency.
            amount (int): Amount.
            source_currency (str): Source currency.
            source_amount (int): Source amount.
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
            expire_min (int): Expire min.

        Returns:
            dict: Response data.

        Raises:
            ValueError: If both amount and source_amount are not set.
            PlisioRequestException: If request failed.
            PlisioAPIException: If API returned error.
        """

        raise NotImplementedError

    @abstractmethod
    def transactions(
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

        raise NotImplementedError

    @abstractmethod
    def withdraw(
            self,
            currency: _t.Currencies,
            type: _t.WithdrawType,  # pylint: disable=redefined-builtin
            to: _t.Text,
            amount: _t.NumberLike,
            fee_plan: _t.Text = None,
    ) -> _t.Result:
        """
        Withdraw.

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

        raise NotImplementedError
