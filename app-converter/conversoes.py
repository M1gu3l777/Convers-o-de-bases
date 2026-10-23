
DIGITOS = "0123456789ABCDEF"
BASES_PERMITIDAS = (2, 8, 10, 16)


def decimal_para_base(numero, base):
    if base not in BASES_PERMITIDAS:
        raise ValueError("Base não suportada.")

    if numero == 0:
        return "0"

    negativo = numero < 0
    numero = abs(numero)
    resultado = ""

    while numero > 0:
        resto = numero % base
        resultado = DIGITOS[resto] + resultado
        numero //= base

    if negativo:
        resultado = "-" + resultado

    return resultado


def base_para_decimal(numero, base):
    if base not in BASES_PERMITIDAS:
        raise ValueError("Base não suportada.")

    numero = numero.strip().upper()

    if not numero:
        raise ValueError("Digite um número.")

    negativo = numero.startswith("-")

    if numero[0] in "+-":
        numero = numero[1:]

    if not numero:
        raise ValueError("Digite os algarismos do número.")

    resultado = 0

    for digito in numero:
        valor = DIGITOS.find(digito)

        if valor < 0 or valor >= base:
            raise ValueError(
                f"O algarismo '{digito}' não é válido na base {base}."
            )

        resultado = resultado * base + valor

    if negativo:
        resultado = -resultado

    return resultado


def converter(numero, base_origem, base_destino):
    decimal = base_para_decimal(numero, base_origem)
    return decimal_para_base(decimal, base_destino)
