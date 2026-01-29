import re

def email_vali(email):
    pattern = r"[a-zA-Z0-9._%+-]{5,}[@]((gmail)|(yahoo)|outlook)[.]((com)|(us)|(uk)|(in)|(eu))"
    return re.match(pattern, email)