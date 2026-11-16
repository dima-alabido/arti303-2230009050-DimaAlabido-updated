"""A module with one function for cleaning names"""


def clean_name(raw):
    """Clean a name: remove extra whitespace and convert it to title case"""
    # TODO: collapse whitespace, then title-case 
    raw = " ".join(raw.split()).title()
    return raw
