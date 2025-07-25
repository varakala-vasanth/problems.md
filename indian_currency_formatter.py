def format_indian_currency(number):
    s = f"{number:.10f}".rstrip('0').rstrip('.')
    if '.' in s:
        int_part, dec_part = s.split('.')
    else:
        int_part, dec_part = s, ''
    n = len(int_part)
    if n <= 3:
        formatted = int_part
    else:
        formatted = int_part[-3:]
        int_part = int_part[:-3]
        while len(int_part) > 2:
            formatted = int_part[-2:] + ',' + formatted
            int_part = int_part[:-2]
        if int_part:
            formatted = int_part + ',' + formatted
    return formatted + ('.' + dec_part if dec_part else '')
