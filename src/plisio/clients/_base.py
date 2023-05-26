"""
Base client class.
"""

from abc import (
    ABC,
    abstractmethod,
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

    def __str__(self) -> _t.Text:
        """
        Get string representation.

        Returns:
            str: String representation.
        """

        return f"<{self.__class__.__name__}: {self.BASE_URL}/{self.API_VERSION_V1}>"

    def _get_uri(self, path: _t.Text, version: _t.Text = API_VERSION_V1) -> _t.Text:
        """
        Get URI.

        Args:
            path (str): Path.
            version (str): API version.

        Returns:
            str: URI.
        """

        return f"{self.BASE_URL}/{version}/{path.lstrip('/').rstrip('/')}"

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

        return {key: value for key, value in locals_.items() if key != "self" and not (exclude_unset and value is None)}

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

    def _get_request_kwargs(  # type: ignore[no-untyped-def]
        self, method: _t.Methods, force_params: bool = False, **kwargs
    ) -> _t.DictStrAny:
        """
        Get request kwargs.

        Args:
            method (Methods): Method.
            force_params (bool): Force params.
            **kwargs: Keyword arguments.

        Returns:
            dict: Request kwargs.
        """

        kwargs["timeout"] = self.REQUEST_TIMEOUT

        if self._requests_params:
            kwargs.update(self._requests_params)

        data = kwargs.pop("data", None)
        data.update({"api_key": self.api_key})

        if data and isinstance(data, dict):
            kwargs["data"] = data

            if "requests_params" in kwargs["data"]:
                kwargs.update(kwargs["data"]["requests_params"])
                del kwargs["data"]["requests_params"]

        if data and (str(method).upper() == _Methods.GET or force_params):
            _ = ""
            for data in kwargs["data"].items():
                key = data[0]
                if isinstance(data[1], list):
                    value = ",".join(data[1])
                else:
                    value = str(data[1])

                _ += f"{key}={value}&"

            kwargs["params"] = _.rstrip("&")
            del kwargs["data"]

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
    def _request(  # type: ignore[no-untyped-def]
        self, method: _t.Methods, uri: _t.Text, force_params: bool = False, **kwargs  # type: ignore[no-untyped-def]
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
    def _get(  # type: ignore[no-untyped-def]
        self,
        path: _t.Text,
        version: _t.Text = API_VERSION_V1,
        **kwargs,  # type: ignore[no-untyped-def]
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
    def _post(  # type: ignore[no-untyped-def]
        self,
        path: _t.Text,
        version: _t.Text = API_VERSION_V1,
        **kwargs,  # type: ignore[no-untyped-def]
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
    def _put(  # type: ignore[no-untyped-def]
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
    def _delete(  # type: ignore[no-untyped-def]
        self,
        path: _t.Text,
        version: _t.Text = API_VERSION_V1,
        **kwargs,  # type: ignore[no-untyped-def]
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
