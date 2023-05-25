"""
Utils module for plisio.
"""


def to_camel_case(snake_str: str) -> str:
    """
    Convert snake_case to camelCase.
    """
    components = snake_str.split("_")
    return components[0] + "".join(x.title() for x in components[1:])
