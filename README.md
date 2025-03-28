# Servidor TCP en Python

Este proyecto implementa un **servidor TCP multicliente** en Python, permitiendo que múltiples clientes se conecten simultáneamente y envíen mensajes al servidor, el cual les responde con una confirmación.

## 🚀 Características

✅ Soporte para múltiples clientes simultáneamente usando **hilos (threading)**.  
✅ El servidor recibe y responde mensajes de los clientes.  
✅ Manejo de excepciones para evitar fallos inesperados.  
✅ Código limpio y bien documentado.  

## 🛠️ Instalación y Uso

### 1️⃣ Clonar el repositorio  
```sh
git clone https://github.com/tu-usuario/servidor-tcp-python.git
cd servidor-tcp-python
```

### Iniciar Servidor
```sh
py Server.py
```

![alt text](https://github.com/JazielRod99/PruebaTecnica/blob/main/src/IniciarServer.png?raw=true)

### Iniciar Cliente
```sh
py Cliente.py
```

![alt text](https://github.com/JazielRod99/PruebaTecnica/blob/main/src/IniciarCliente.png?raw=true)

### Mandar Mensaje ('Hola Mundo')
![alt text](https://github.com/JazielRod99/PruebaTecnica/blob/main/src/MandarMensaje.png?raw=true)

### Escuchar Mensaje ('Hola Mundo')
![alt text](https://github.com/JazielRod99/PruebaTecnica/blob/main/src/EscucharMensaje.png?raw=true)

### Mandar Mensaje ('DESCONEXION')
![alt text](https://github.com/JazielRod99/PruebaTecnica/blob/main/src/DesconexionMensaje.png?raw=true)

### Escuchar Mensaje ('DESCONEXION')
![alt text](https://github.com/JazielRod99/PruebaTecnica/blob/main/src/EscucharDesconexion.png?raw=true)
