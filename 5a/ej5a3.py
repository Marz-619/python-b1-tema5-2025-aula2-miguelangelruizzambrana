"""
Enunciado :
Crea una clase llamada "SafeWalletCredentials" que represente una
billetera electrónica que almacena monedas digitales y permite
establecer y obtener la contraseña de la billetera usando
encapsulamiento.

El constructor debe tener el parámetro password.

Parámetros:
    - password: una cadena que representa la contraseña de la
    billetera electrónica.

Métodos:
    - set_password(password): establece la contraseña de la billetera.
    - get_password(): devuelve la contraseña de la billetera.

Ejemplo:
    Entrada:
        safe_wallet = SafeWalletCredentials("1234")
        print(safe_wallet.get_password())
        safe_wallet.set_password("5678")
        print(safe_wallet.get_password())

    Salida:
        1234
        5678

"""

class SafeWalletCredentials:
    def __init__(self,password):
        self.__password = password

    def set_password(self, new_password):
        self.__password = new_password

    def get_password(self):
        return self.__password
    


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script

# pedro_wallet = SafeWalletCredentials("1234A")
# print(pedro_wallet.get_password())
# pedro_wallet.set_password("A1B2c3")
# print(pedro_wallet.get_password())
