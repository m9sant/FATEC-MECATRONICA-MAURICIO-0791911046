#Metodos de strings
texto = "a vingança nunca é plena, mata a alma e envenena (Madruga, 1981)"

print(texto.capitalize())
print(texto.casefold())
print(texto.count("madruga"))
texto_minusculo = texto.lower()
print(texto_minusculo)
print(texto_minusculo.count("madruga"))
texto_mausculo = texto.upper()
print(texto_mausculo)
print(texto_minusculo.find(','))
print(texto_minusculo[:texto_minusculo.find(',')])
