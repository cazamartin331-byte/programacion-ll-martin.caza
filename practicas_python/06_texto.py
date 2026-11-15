# Práctica 06: Manejo de texto
# Autor: Martin Caza

frase = "  Ceviche de camarón con chifles  "

print(frase.strip())
print(frase.upper())
print(frase.lower())
print(frase.strip().title())
print(frase.replace("camarón", "pescado"))
print(len(frase.strip()))
print("camarón" in frase)

palabras = frase.split()
print(palabras)
print("-".join(palabras))

# Indexado y rebanado
plato = "Hornado"
print(plato[0], plato[-1], plato[1:4], plato[::-1])

# f-strings con formato
precio = 5.5
print(f"{plato} cuesta ${precio:.2f}")
