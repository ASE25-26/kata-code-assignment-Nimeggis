import re


def add(numbers: str) -> int:
    # Regel 1: Leerer String -> 0
    if not numbers:
        return 0

    # Regel 5: Benutzerdefinierter Delimiter
    delimiters = [",", "\n"]
    if numbers.startswith("//"):
        delimiter_section, numbers = numbers.split("\n", 1)

        # Delimiter mit eckigen Klammern (z. B. //[***][%%])
        matches = re.findall(r"\[(.*?)\]", delimiter_section)
        if matches:
            delimiters = matches
        else:
            # Einfacher Delimiter (z. B. //;)
            delimiters = [delimiter_section[2:]]

    # Regex für beliebige Delimiter
    pattern = "|".join(map(re.escape, delimiters))
    tokens = re.split(pattern, numbers)

    # Konvertiere Tokens zu Zahlen, leere ignorieren
    values = [int(t) for t in tokens if t]

    # Regel 6: Negative Zahlen prüfen
    negatives = [n for n in values if n < 0]
    if negatives:
        raise ValueError(f"Negatives not allowed: {', '.join(map(str, negatives))}")

    # Regel 7: Zahlen > 1000 ignorieren
    values = [n for n in values if n <= 1000]

    return sum(values)