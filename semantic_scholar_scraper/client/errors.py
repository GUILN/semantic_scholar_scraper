"""
This module provides client errors
"""


class ClientBaseError(Exception):
    """
    ClientBaseError

    provides a base error class for client errors
    """

    def __init__(self, message: str, *args, **kwargs):
        self._message = message
        super().__init__(self, self._message, *args, **kwargs)


class HttpClientError(ClientBaseError):
    """
    HttpClientError

    provides error information for HTTP client errors
    """

    def __init__(
        self,
        status_code: int = 0,
        reason: str = None,
        client_error: Exception = None,
        *args,
        **kwargs,
    ):
        message = f"Error occurred while reaching the server. status code: {status_code} reason: {reason}"

        self._client_error = client_error
        self._status_code = status_code
        self._reason = reason
        super().__init__(self, message, *args, **kwargs)

    @property
    def status_code(self) -> int:
        """
        status code property
        """
        return self._status_code

    @property
    def reason(self) -> str:
        """
        reason property
        describes the error reason
        """
        return self._reason
