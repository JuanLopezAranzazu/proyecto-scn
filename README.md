## Proyecto Simulación y computación numérica

### Integrantes:

- Victor Manuel Álzate Morales - 202313022
- Juan Esteban López Aránzazu - 202313026

### Descripción:

- Método polinomio de taylor
- Método newton-raphson
- Método diferencias finitas
- Método sistemas de ecuaciones no lineales (jacobiano)
- Método sistema de ecuaciones lineales (jacobi)

### Entorno virtual e instalar dependencias

Para instalar las dependencias especificadas en `requirements.txt`, abre una terminal y navega hasta el directorio del proyecto. Luego, ejecuta el siguiente comando:

Para el entorno virtual en linux
```bash
python3 -m venv venv
source venv/bin/activate # Para activar el entorno virtual
deactivate # Para desactivar el entorno virtual
```

Para el entorno virtual en windows
```bash
python -m venv venv
.\venv\Scripts\activate # Para activar el entorno virtual
.\venv\Scripts\deactivate # Para desactivar el entorno virtual
```

Para instalar dependencias
```bash
pip install -r requirements.txt
```

### Ejecución del programa

Para correr el programa puedes ejecutar el siguiente comando:
```bash
python main.py
```