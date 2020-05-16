"""
Escribe un programa que almacene la cadena de caracteres contraseña en una
variable, pregunte al usuario por la contraseña e imprima por pantalla si la 
contraseña introducida por el usuario coincide con la guardada en la variable 
sin tener en cuenta mayúnculas y minúscula.

"""
password = "contraseña"

password_de_usuario = input("Introduzca la contarseña: ")
password_de_usuario = password_de_usuario.lower()

if password == password_de_usuario:
    print("El password es correcto")
else:
    print("El password no coincide.")