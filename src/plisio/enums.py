"""
Enum for Plisio API
"""

from typing import (
    Iterator as _Iterator
)

from enum import (
    Enum as _Enum,
    EnumMeta as _EnumMeta,
)


class EnumMeta(_EnumMeta):
    """
    Enum Meta.
    """

    def __iter__(cls) -> _Iterator:
        """
        Iterate over Enum.
        """

        return (  # type: ignore[var-annotated]
            (member.value, member.name)
            for member in super().__iter__()
        )

    def __getitem__(cls, name: str):  # type: ignore[no-untyped-def]
        """
        Get Enum item by name.
        """

        return cls[name.upper()]  # pylint: disable=unsubscriptable-object

    def __contains__(cls, name: str) -> bool:  # type: ignore[override]
        """
        Check if Enum contains item.
        """

        return name.upper() in cls.__members__  # pylint: disable=unsupported-membership-test

    def __str__(cls) -> str:
        """
        String representation.
        """

        return f'<enum {cls.__name__}>'

    def __repr__(cls) -> str:
        """
        Representation.
        """

        return f'<enum {cls.__name__}>'


class Enum(_Enum, metaclass=EnumMeta):
    """
    Enum.
    """

    def __str__(self) -> str:
        """
        String representation.
        """

        return str(self.value)

    def __repr__(self) -> str:
        """
        Representation.
        """

        return f'{self.__class__.__name__}.{self.name}'


class Methods(Enum):
    """
    Methods.
    """

    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"


class Currencies(Enum):
    """
    Currencies.
    """

    ETH = "Ethereum"
    BTC = "Bitcoin"
    LTC = "Litecoin"
    DASH = "Dash"
    TZEC = "Zcash"
    DOGE = "Dogecoin"
    BCH = "Bitcoin Cash"
    XMR = "Monero"
    USDT = "Tether ERC-20"
    USDC = "USD Coin"
    SHIB = "Shiba Inu"
    BTT = "BitTorrent TRC-20"
    USDT_TRX = "Tether TRC-20"
    TRX = "Tron"
    BNB = "BNB Chain"
    BUSD = "Binance USD BEP-20"
    USDT_BSC = "Tether BEP-20"


class FiatCurrency(Enum):
    AED = 'United Arab Emirates Dirham'
    AFN = 'Afghan Afghani'
    ALL = 'Albanian Lek'
    AMD = 'Armenian Dram'
    ANG = 'Netherlands Antillean Guilder'
    AOA = 'Angolan Kwanza'
    ARS = 'Argentine Peso'
    AUD = 'Australian Dollar'
    AWG = 'Aruban Florin'
    AZN = 'Azerbaijani Manat'
    BAM = 'Bosnia-Herzegovina Convertible Mark'
    BBD = 'Barbadian Dollar'
    BDT = 'Bangladeshi Taka'
    BGN = 'Bulgarian Lev'
    BHD = 'Bahraini Dinar'
    BIF = 'Burundian Franc'
    BMD = 'Bermuda Dollar'
    BND = 'Brunei Dollar'
    BOB = 'Bolivian Boliviano'
    BRL = 'Brazilian Real'
    BSD = 'Bahamian Dollar'
    BTN = 'Bhutanese Ngultrum'
    BWP = 'Botswana Pula'
    BYN = 'New Belarusian Ruble'
    BYR = 'Belarusian Ruble'
    BZD = 'Belize Dollar'
    CAD = 'Canadian Dollar'
    CDF = 'Congolese Franc'
    CHF = 'Swiss Franc'
    CLF = 'Chilean Unit of Account (UF)'
    CLP = 'Chilean Peso'
    CNY = 'Chinese Yuan'
    COP = 'Colombian Peso'
    CRC = 'Costa Rican Colón'
    CUC = 'Cuban Convertible Peso'
    CUP = 'Cuban Peso'
    CVE = 'Cape Verdean Escudo'
    CZK = 'Czech Republic Koruna'
    DJF = 'Djiboutian Franc'
    DKK = 'Danish Krone'
    DOP = 'Dominican Peso'
    DZD = 'Algerian Dinar'
    EGP = 'Egyptian Pound'
    ERN = 'Eritrean Nakfa'
    ETB = 'Ethiopian Birr'
    EUR = 'Euro'
    FJD = 'Fijian Dollar'
    FKP = 'Falkland Islands Pound'
    GBP = 'British Pound Sterling'
    GEL = 'Georgian Lari'
    GGP = 'Guernsey Pound'
    GHS = 'Ghanaian Cedi'
    GIP = 'Gibraltar Pound'
    GMD = 'Gambian Dalasi'
    GNF = 'Guinean Franc'
    GTQ = 'Guatemalan Quetzal'
    GYD = 'Guyanese Dollar'
    HKD = 'Hong Kong Dollar'
    HNL = 'Honduran Lempira'
    HRK = 'Croatian Kuna'
    HTG = 'Haitian Gourde'
    HUF = 'Hungarian Forint'
    IDR = 'Indonesian Rupiah'
    ILS = 'Israeli New Sheqel'
    IMP = 'Manx pound'
    INR = 'Indian Rupee'
    IQD = 'Iraqi Dinar'
    IRR = 'Iranian Rial'
    ISK = 'Icelandic Króna'
    JEP = 'Jersey Pound'
    JMD = 'Jamaican Dollar'
    JOD = 'Jordanian Dinar'
    JPY = 'Japanese Yen'
    KES = 'Kenyan Shilling'
    KGS = 'Kyrgyzstan Som'
    KHR = 'Cambodian Riel'
    KMF = 'Comorian Franc'
    KPW = 'North Korean Won'
    KRW = 'South Korean Won'
    KWD = 'Kuwaiti Dinar'
    KYD = 'Cayman Islands Dollar'
    KZT = 'Kazakhstani Tenge'
    LAK = 'Laotian Kip'
    LBP = 'Lebanese Pound'
    LKR = 'Sri Lankan Rupee'
    LRD = 'Liberian Dollar'
    LSL = 'Lesotho Loti'
    LTL = 'Lithuanian Litas'
    LVL = 'Latvian Lats'
    LYD = 'Libyan Dinar'
    MAD = 'Moroccan Dirham'
    MDL = 'Moldovan Leu'
    MGA = 'Malagasy Ariary'
    MKD = 'Macedonian Denar'
    MMK = 'Myanmar Kyat'
    MNT = 'Mongolian Tugrik'
    MOP = 'Macanese Pataca'
    MRO = 'Mauritania Ouguiya'
    MUR = 'Mauritian Rupee'
    MVR = 'Maldivian Rufiyaa'
    MWK = 'Malawi Kwacha'
    MXN = 'Mexican Peso'
    MYR = 'Malaysian Ringgit'
    MZN = 'Mozambican Metical'
    NAD = 'Namibian Dollar'
    NGN = 'Nigerian Naira'
    NIO = 'Nicaraguan Córdoba'
    NOK = 'Norwegian Krone'
    NPR = 'Nepalese Rupee'
    NZD = 'New Zealand Dollar'
    OMR = 'Omani Rial'
    PAB = 'Panamanian Balboa'
    PEN = 'Peruvian Nuevo Sol'
    PGK = 'Papua New Guinean Kina'
    PHP = 'Philippine Peso'
    PKR = 'Pakistani Rupee'
    PLN = 'Polish Zloty'
    PYG = 'Paraguayan Guarani'
    QAR = 'Qatari Rial'
    RON = 'Romanian Leu'
    RSD = 'Serbian Dinar'
    RUB = 'Russian Ruble'
    RWF = 'Rwandan Franc'
    SAR = 'Saudi Riyal'
    SBD = 'Solomon Islands Dollar'
    SCR = 'Seychellois Rupee'
    SDG = 'Sudanese Pound'
    SEK = 'Swedish Krona'
    SGD = 'Singapore Dollar'
    SHP = 'Saint Helena Pound'
    SLL = 'Sierra Leonean Leone'
    SOS = 'Somali Shilling'
    SRD = 'Surinamese Dollar'
    STD = 'São Tomé and Príncipe Dobra'
    SVC = 'Salvadoran Colón'
    SYP = 'Syrian Pound'
    SZL = 'Swazi Lilangeni'
    THB = 'Thai Baht'
    TJS = 'Tajikistan Somoni'
    TMT = 'Turkmenistan Manat'
    TND = 'Tunisian Dinar'
    TOP = 'Tongan Paʻanga'
    TRY = 'Turkish Lira'
    TTD = 'Trinidad and Tobago Dollar'
    TWD = 'New Taiwan Dollar'
    TZS = 'Tanzanian Shilling'
    UAH = 'Ukrainian Hryvnia'
    UGX = 'Ugandan Shilling'
    USD = 'United States Dollar'
    UYU = 'Uruguayan Peso'
    UZS = 'Uzbekistan Som'
    VEF = 'Venezuelan Bolívar Fuerte'
    VND = 'Vietnamese Dong'
    VUV = 'Vanuatu Vatu'
    WST = 'Samoan Tala'
    XAF = 'CFA Franc BEAC'
    XAG = 'Silver (troy ounce)'
    XAU = 'Gold (troy ounce)'
    XCD = 'East Caribbean Dollar'
    XDR = 'Special Drawing Rights'
    XOF = 'CFA Franc BCEAO'
    XPF = 'CFP Franc'
    YER = 'Yemeni Rial'
    ZAR = 'South African Rand'
    ZMK = 'Zambian Kwacha (pre-2013)'
    ZMW = 'Zambian Kwacha'
    ZWL = 'Zimbabwean Dollar'


class TransactionType(Enum):
    CASH_IN = "cash_in"
    CASH_OUT = "cash_out"
    MASS_CASH_OUT = "mass_cash_out"
    INVOICE = "invoice"


class TransactionStatus(Enum):
    NEW = "new"
    PENDING = "pending"
    PENDING_INTERNAL = "pending internal"
    EXPIRED = "expired"
    COMPLETED = "completed"
    MISMATCH = "mismatch"
    ERROR = "error"
    CANCELLED = "cancelled"


class WithdrawType(Enum):
    CASH_OUT = "cash_out"
    MASS_CASH_OUT = "mass_cash_out"
