"""
Types for plisio.
"""

from typing import (
    Union as _Union,
    Dict as _Dict,
    Literal as _Literal,
    Optional as _Optional,
    List as _List,
)

from aiohttp import (
    ClientSession as AsyncRequestSession,
    ClientResponse as AsyncRequestResponse,
)

from requests import (
    Session as SyncRequestSession,
    Response as SyncRequestResponse,
)

from pydantic import (  # pylint: disable=no-name-in-module
    HttpUrl as _HttpUrl,
    EmailStr as _EmailStr,
)

from . import (
    enums as _enums
)

Text = _Union[str]

Number = _Union[int, float]
NumberLike = _Union[int, float, Text]

DictStrAny = _Dict[Text, _Union[Text, int, float, bool, None]]

OptionalText = _Optional[Text]
OptionalBool = _Optional[bool]
OptionalNumber = _Optional[Number]
OptionalNumberLike = _Optional[NumberLike]

Session = _Union[AsyncRequestSession, SyncRequestSession]
Response = _Union[AsyncRequestResponse, SyncRequestResponse]
RequestParams = _Optional[_Dict[str, _Union[Text, Number, DictStrAny]]]

Headers = _Dict[Text, Text]

Result = DictStrAny

Methods = _Union[
    _Literal["GET"],
    _Literal["POST"],
    _Literal["PUT"],
    _Literal["DELETE"],
    _enums.Methods,
]

SupportedCurrency = _Literal[
    "ETH",
    "BTC",
    "LTC",
    "DASH",
    "TZEC",
    "DOGE",
    "BCH",
    "XMR",
    "USDT",
    "USDC",
    "SHIB",
    "BTT",
    "USDT_TRX",
    "TRX",
    "BNB",
    "BUSD",
    "USDT_BSC"
]

SupportedFiat = _Literal[
    "AED",
    "AFN",
    "ALL",
    "AMD",
    "ANG",
    "AOA",
    "ARS",
    "AUD",
    "AWG",
    "AZN",
    "BAM",
    "BBD",
    "BDT",
    "BGN",
    "BHD",
    "BIF",
    "BMD",
    "BND",
    "BOB",
    "BRL",
    "BSD",
    "BTN",
    "BWP",
    "BYN",
    "BYR",
    "BZD",
    "CAD",
    "CDF",
    "CHF",
    "CLF",
    "CLP",
    "CNY",
    "COP",
    "CRC",
    "CUC",
    "CUP",
    "CVE",
    "CZK",
    "DJF",
    "DKK",
    "DOP",
    "DZD",
    "EGP",
    "ERN",
    "ETB",
    "EUR",
    "FJD",
    "FKP",
    "GBP",
    "GEL",
    "GGP",
    "GHS",
    "GIP",
    "GMD",
    "GNF",
    "GTQ",
    "GYD",
    "HKD",
    "HNL",
    "HRK",
    "HTG",
    "HUF",
    "IDR",
    "ILS",
    "IMP",
    "INR",
    "IQD",
    "IRR",
    "ISK",
    "JEP",
    "JMD",
    "JOD",
    "JPY",
    "KES",
    "KGS",
    "KHR",
    "KMF",
    "KPW",
    "KRW",
    "KWD",
    "KYD",
    "KZT",
    "LAK",
    "LBP",
    "LKR",
    "LRD",
    "LSL",
    "LTL",
    "LVL",
    "LYD",
    "MAD",
    "MDL",
    "MGA",
    "MKD",
    "MMK",
    "MNT",
    "MOP",
    "MRO",
    "MUR",
    "MVR",
    "MWK",
    "MXN",
    "MYR",
    "MZN",
    "NAD",
    "NGN",
    "NIO",
    "NOK",
    "NPR",
    "NZD",
    "OMR",
    "PAB",
    "PEN",
    "PGK",
    "PHP",
    "PKR",
    "PLN",
    "PYG",
    "QAR",
    "RON",
    "RSD",
    "RUB",
    "RWF",
    "SAR",
    "SBD",
    "SCR",
    "SDG",
    "SEK",
    "SGD",
    "SHP",
    "SLL",
    "SOS",
    "SRD",
    "STD",
    "SVC",
    "SYP",
    "SZL",
    "THB",
    "TJS",
    "TMT",
    "TND",
    "TOP",
    "TRY",
    "TTD",
    "TWD",
    "TZS",
    "UAH",
    "UGX",
    "USD",
    "UYU",
    "UZS",
    "VEF",
    "VND",
    "VUV",
    "WST",
    "XAF",
    "XAG",
    "XAU",
    "XCD",
    "XDR",
    "XOF",
    "XPF",
    "YER",
    "ZAR",
    "ZMK",
    "ZMW",
    "ZWL"
]

Currencies = _Union[_enums.Currencies, SupportedCurrency]
Fiats = _Union[_enums.FiatCurrency, SupportedFiat]
OptionalCurrencies = _Optional[Currencies]
OptionalFiats = _Optional[Fiats]

PsysCids = _List[Currencies]
OptionalPsysCids = _Optional[PsysCids]

Link = _HttpUrl
OptionalLink = _Optional[Link]

Email = _EmailStr
OptionalEmail = _Optional[Email]

_TransactionType = _Literal[
    "cash_in",
    "cash_out",
    "mass_cash_out",
    "invoice",
]
TransactionType = _Union[_enums.TransactionType, _TransactionType]
OptionalTransactionType = _Optional[TransactionType]

_TransactionStatus = _Literal[
    "new",
    "pending",
    "pending_internal",
    "expired",
    "completed",
    "mismatch",
    "error",
    "cancelled"
]
TransactionStatus = _Union[_enums.TransactionStatus, _TransactionStatus]
OptionalTransactionStatus = _Optional[TransactionStatus]

_WithdrawType = _Literal[
    "cash_out",
    "mass_cash_out",
]
WithdrawType = _Union[_enums.WithdrawType, _WithdrawType]
OptionalWithdrawType = _Optional[WithdrawType]
