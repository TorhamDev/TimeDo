from string import ascii_uppercase, ascii_lowercase, digits
from random import choices
from api_v1.models import Timer


def create_short_link_for_timer(link_length: int, base_url: str) -> str:
    ascii_chars = list(ascii_uppercase + ascii_lowercase + digits)
    random_link = ""
    while True:
        random_link = choices(ascii_chars, k=link_length)
        if Timer.objects.filter(short_link=random_link).exists():
            continue
        else:
            break

    result_link = base_url + "timer/" + "".join(random_link)
    return result_link
