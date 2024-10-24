# Proyecto de Cálculo de Media y Desviación Estándar
## INTEGRANTES:
| Apellidos y Nombres | Correo|
|---------------------|-------|
| MEZA CALDERON Ana Critina | 72415738@continental.edu.pe |
| VASQUEZ MIRANDA Luis Alexis | 73870803@continental.edu.pe |
## DOCUMENTACIÓN:
### Calculadora de Promedio y Desviación Estándar
Este proyecto es una aplicación en Python que calcula el promedio y la desviación estándar de una lista de números enteros, utilizando la técnica de Test Driven Development (TDD).
#### Requisitos
- Python 3.x
- pip (gestor de paquetes de Python)
- Un entorno virtual (opcional pero recomendado)
#### Instalación
##### 1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/tu_usuario/nombre_del_repositorio.git
   cd nombre_del_repositorio
   ```
##### 2. **Crea y activa un entorno virtual (opcional):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Linux o Mac
  .\venv\Scripts\activate   # En Windows
   ```
#### Ejecución de la aplicación
   ```python
   from src.logica.Calculadora import Calculadora

   calculadora = Calculadora()
   promedio = calculadora.media([1, 2, 3, 4, 5])
   desviacion = calculadora.desviacion_estandar([1, 2, 3, 4, 5])
   print("Promedio:", promedio)
   print("Desviación Estándar:", desviacion)
   ```
#### Ejecución de las Pruebas
   ```bash
   Copiar código
   python -m unittest discover -s tests -p "*.py"
   ```
