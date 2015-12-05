"""
   Copyright (C) 2012 Jesus Cano <jcanovel@gmail.com>.

   This file is part of IPSuite.

   IPSuite is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   IPSuite is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with Cile.  If not, see <http://www.gnu.org/licenses/>.

"""

import ping

LISTA_IPS = ['8.8.8.8',
             '8.8.8.81',
             '8.8.2.8',
             '8.8.8.8',
             '8.8.23.8',
             '8.8.8.8',
             '8.8.234.8',
             '8.8.255.8']

def ipcaida (ip):
    "Esta funcion devuelve True si la maquina esta caida. En caso contrario, devuelve False"
    # Hacemos un ping con 2 segundos de timeout y 64 bytes de datos
    estado = ping.do_one(ip, 2, 64)
    if estado is None:
        return True             # Maquina caida
    else:
        return False            # Maquina NO caida


######################### Comienienzo del programa

for i in LISTA_IPS:
    if ipcaida(i) == True:
        print('La maquina cuya ip es ' + i + ' esta caida')
