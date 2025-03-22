import unidecode
import re


def strip_text(text: str) -> str:
    """
    Cleans the input text by removing HTML tags, non-alphanumeric characters,
    normalizing accented characters, and converting to lowercase.

    Args:
        text (str): String to be stripped.

    Returns:
        str: Cleaned and normalized text.
    """
    if not text:
        return ""

    # remove html tags
    text = re.sub(r"<[^>]+>", "", text)

    # normalize chars
    text = unidecode.unidecode(text)

    # remove all non-alphanumeric characters, replace with a space
    text = re.sub(r"[^A-Za-z0-9]", " ", text)

    # convert to lowercase and strip extra whitespace
    clean_text = re.sub(r"\s+", " ", text).strip().lower()

    return clean_text
