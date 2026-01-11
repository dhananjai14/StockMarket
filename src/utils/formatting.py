from typing import Dict, Any
def format_response(message, data=None, status=200) -> Dict[str, Any]:
    """
    Standardizes API response format.

    :param message (str): The message to include in the response.
    :param data (dict, optional): The data to include in the response. Defaults to None.
    :param status (int, optional): The HTTP status code. Defaults to 200.
    Returns:
        dict: Formatted response dictionary.
    """
    response = {
        "status": status,
        "message": message,
        "data": data
    }
    return response