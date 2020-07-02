# iFaces for MacOS

Script que devuelve las IPs asignadas a las interfaces de red de un MacOS.

Si llamamos al script sin argumentos, nos devuelve una lista con todas las IPs asignadas, pero si añadimos el argumento `default` nos devuelve la IP de la interfaz prioritaria del sistema.
```
> python3 main.py
192.168.0.10
192.168.0.11

> python3 main.py default
192.168.0.10
```
