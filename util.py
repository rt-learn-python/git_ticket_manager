"""
TODO:
"""


def translate_to_branch(ticket_id, description):
    """
    TODO
    """
    encoded_desc = (
        description.replace(" - ", "-")
        .replace(".", "_")
        .replace(",", "_")
        .replace("/", "")
        .replace("[", "(")
        .replace("]", ")")
        .replace(": ", "-")
        .replace(":", "-")
        .replace(" ", "-")
        .replace("'", "")
        .rstrip("_")
    )

    return f"feature/{ticket_id}-{encoded_desc}"
