# 🐍 Fundamentos de Programación Orientada a Objetos en Python

Este repositorio contiene una colección de ejercicios prácticos que ilustran los principios fundamentales de la Programación Orientada a Objetos (POO) en Python. Cada proyecto demuestra conceptos clave mediante implementaciones concretas y ejemplos ejecutables.

## 📚 Tabla de Contenidos

1. [Conceptos Cubiertos](#-conceptos-cubiertos)
2. [Estructura del Proyecto](#-estructura-del-proyecto)
3. [Cómo Utilizar Este Repositorio](#-cómo-utilizar-este-repositorio)
4. [Contribuciones](#-contribuciones)

## 🧩 Conceptos Cubiertos

### Principios Básicos de POO
- **Encapsulación**: Ocultamiento de datos mediante atributos privados/protegidos
- **Abstracción**: Creación de interfaces simplificadas
- **Herencia**: Mecanismo de reutilización y extensión de código
- **Polimorfismo**: Capacidad de objetos diferentes de responder al mismo mensaje

### Elementos Específicos
- Métodos estáticos (`@staticmethod`)
- Métodos de clase (`@classmethod`)
- Decoradores `@property` para getters/setters
- Métodos especiales (Dunder methods: `__str__`, `__repr__`, etc.)
- Variables de clase vs. variables de instancia

## 📂 Estructura del Proyecto

### [🧬 animalHerenciaPolimorfismo](animalHerenciaPolimorfismo/)
- **animalHerencia.py**: Demuestra herencia con clases base `Animal` y subclases específicas
- **animalPolimorfismo.py**: Implementa polimorfismo mediante métodos con el mismo nombre en diferentes subclases

### [🔒 atributosPrivadosProtegidos](atributosPrivadosProtegidos/)
- **automovilProtegido.py**: Ejemplo de encapsulación usando atributos protegidos (`_variable`) y privados (`__variable`)

### [🚗 automovilHerrenciaPolimorfismo](automovilHerrenciaPolimorfismo/)
- **automovil.py**: Sistema jerárquico de vehículos que aplica herencia y polimorfismo

### [⚙️ automovilStaticClassMethod](automovilStaticClassMethod/)
- **automovilClassMethod.py**: Uso de `@classmethod` para métodos alternativos de construcción

### [📚 bibliotecaLibros](bibliotecaLibros/)
- **libroClassMethod.py**: Implementación de métodos de clase para manipular estado compartido
- **libroStaticMethod.py**: Ejemplo de métodos estáticos para funciones utilitarias

### [🧮 calculadoraStaticClassMethod](calculadoraStaticClassMethod/)
- **calculadoraStaticMethod.py**: Demostración de métodos estáticos para operaciones matemáticas

### [💰 cuentaBancaria](cuentaBancaria/)
- **cuentaBancaria.py**: Sistema bancario con encapsulación de datos sensibles y métodos de operación

### [👨‍🎓 estudiantesVariableClase](estudiantesVariableClase/)
- **escuelaClassVariable.py**: Uso de variables de clase para almacenar estado compartido

### [🔷 figurasGeometricas](figurasGeometricas/)
- **calculadorAreaPerimetro.py**: Implementación básica con herencia
- **calculadorAreaPerimetroClassMethod.py**: Uso de métodos de clase para constructores alternativos
- **calculadorAreaPerimetroProperty.py**: Implementación con decoradores `@property`

### [⚖️ methosSeterGetter](methosSeterGetter/)
- **edadSetterGetter.py**: Manejo de atributos con métodos setter/getter tradicionales

### [✨ metodosEspeciales](metodosEspeciales/)
- **frutas.py**: Implementación de métodos especiales (`__str__`, `__len__`, etc.)
- **libroSpecialMethods.py**: Ejemplo avanzado de dunder methods en un sistema de biblioteca

### [📱 tecnologiaMovilPolimorfismo](tecnologiaMovilPolimorfismo/)
- **tecnologiaMovilPolimorfismo.py**: Sistema de dispositivos móviles que implementa polimorfismo

### [🎮 tiendaGamer](tiendaGamer/)
- **tiendaGamer.py**: Sistema completo de tienda que integra múltiples conceptos de POO

## 🚀 Cómo Utilizar Este Repositorio

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/AlxSAGA/python_fundamentos_poo.git
   cd poo-python-fundamentals
   ```

2. **Explorar los proyectos**:
   ```bash
   # Ejecutar un ejemplo específico
   python3 animalHerenciaPolimorfismo/animalHerencia.py
   
   # Explorar un concepto específico
   cd figurasGeometricas
   python3 calculadorAreaPerimetroProperty.py
   ```

3. **Recomendaciones de aprendizaje**:
   - Comenzar con `animalHerenciaPolimorfismo` para entender los conceptos básicos
   - Continuar con `figurasGeometricas` para ver diferentes implementaciones del mismo concepto
   - Explorar `metodosEspeciales` para comprender cómo personalizar el comportamiento de objetos

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si deseas agregar más ejemplos o mejorar los existentes:

1. Haz un fork del repositorio
2. Crea una rama con tu nueva característica (`git checkout -b nueva-caracteristica`)
3. Realiza tus cambios y haz commit (`git commit -am 'Agrego nueva funcionalidad'`)
4. Push a la rama (`git push origin nueva-caracteristica`)
5. Abre un Pull Request
