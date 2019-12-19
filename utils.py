import re

def mask_sensitive_info(ads: str) -> str:
    email_regex = '\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})'
    personal_no_regex = '\d{6,8}[-|(\s)]{0,1}[T|\d]\d{3}'
    telephone_regex = r'(?:\B\+ ?49|\b0)(?: *[(-]? *\d(?:[ \d]*\d)?)? *(?:[)-] *)?\d+ *(?:[/)-] *)?\d+ *(?:[/)-] *)?\d+(?: *- *\d+)?'
    result = re.sub(email_regex, 'EMAIL', ads)
    result = re.sub(personal_no_regex, 'PERSONAL NO', result)
    result = re.sub(telephone_regex, 'TELEPHONE NO', result)
    return result
