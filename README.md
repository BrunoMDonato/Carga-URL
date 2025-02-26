# Carga-URL-Main: Aplicación en Django

Este proyecto es una aplicación web en **Django** que permite ingresar datos de personas a través de la URL y almacenarlos en una base de datos **SQLite3**.

## 📌 Funcionalidad

- La aplicación solicita ingresar en la URL un **DNI, edad y nombre**.
- Los datos se almacenan en una base de datos **SQLite3**.
- Luego, se redirige a una página donde se muestran los datos ingresados.

## 🔧 Instalación y Configuración

### 1️⃣ Clonar el Repositorio
```bash
git clone https://github.com/BrunoMDonato/carga-datos-URL.git
cd Carga-URL-Main
```

### 2️⃣ Crear un Entorno Virtual (Opcional)
```bash
python -m venv env
source env/bin/activate   # En Linux/Mac
env\Scripts\activate      # En Windows
```

### 3️⃣ Instalar Dependencias
```bash
pip install django
```

### 4️⃣ Aplicar Migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Ejecutar el Servidor
```bash
python manage.py runserver
```

## 📂 Estructura del Proyecto

```bash
Carga-URL-Main/
│── ent_MVT/            # Aplicación Django
│   ├── templates/      # Archivos HTML
│   ├── views.py        # Lógica de las vistas
│   ├── models.py       # Modelo de base de datos
│   ├── urls.py         # Configuración de rutas
│── db.sqlite3          # Base de datos SQLite3
│── manage.py           # Script de administración de Django
│── README.md           # Documentación
```

## 📌 Notas Importantes
- **No es necesario un entorno virtual**, pero es recomendable.
- **Asegurarse de configurar correctamente la carpeta `templates` en `settings.py`**.

## 📜 Licencia
Este proyecto está bajo la licencia **MIT**.

