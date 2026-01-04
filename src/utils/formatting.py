def format_response(message, data=None, status=200):
    """
    Standardizes API response format.
    Args:
        message (str): The message to include in the response.
        data (dict, optional): The data to include in the response. Defaults to None.
        status (int, optional): The HTTP status code. Defaults to 200.
    Returns:
        dict: Formatted response dictionary.
    """
    response = {
        "status": status,
        "message": message,
        "data": data
    }
    return response