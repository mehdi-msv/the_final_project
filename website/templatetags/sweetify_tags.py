import sweetify
from django import template
register = template.Library()


@register.simple_tag(name='success_message')
def success_message(request, message):
    """
    Template tag to display a success message using the sweetify library.

    Args:
        request (HttpRequest): The request object.
        message (str): The success message to display.

    Returns:
        str: The HTML for displaying the success message.
    """
    # Use the sweetify library to display a success message.
    # The message is displayed using an alert box.
    return sweetify.success(request, message)
