# ✅ Instrucciones para cualquier miembro del equipo
##    Hasta: 📅 Día 2 – Estructura del módulo y Dockerfile de Odoo
###   Objetivo Final: 🌐 Acceder a Odoo desde el navegador


---


### 1. Clonar el repositorio y entrar al proyecto

Desde PowerShell o terminal:

```bash
git clone https://github.com/kromanUMG/validador_edad_odoo.git
cd validador_edad_odoo
git checkout dev
```

Esto descarga el proyecto y cambia a la rama `dev`, que es donde está el entorno completo.

---

### 2. (Solo una vez) Verificar carpeta `addons`

Confirma que la estructura sea:

```
validador_edad_odoo/
├── addons/
│   └── validador_edad_odoo/
│       ├── __init__.py
│       ├── __manifest__.py
│       ├── models/
│       └── views/
```

Si la carpeta `addons/` no existe por algún error, créala:

```bash
mkdir addons
```

Pero si ya está todo como en el repositorio, no hay nada que hacer aquí.

---

### 3. Levantar el entorno completo con Docker

Descomentar la linea que dice Command en el archivo docker-compose.yml

Desde la raíz del proyecto:

```bash
docker-compose up -d
```

Este comando:

- Crea un contenedor para PostgreSQL (`odoo-db`)
- Crea un contenedor para Odoo (`odoo-app`)
- Expone el sistema en `http://localhost:8069`

---

detener los contenedores

```bash
docker-compose down
```

comentar nuevamente la linea Command e iniciar cotenedores

```bash
docker-compose up -d
```

### 4. Esperar a que Odoo esté listo

Puedes revisar que Odoo esté funcionando con:

```bash
docker logs -f odoo-app
```

Debes ver algo como:

```
HTTP service (werkzeug) running on <algo>:8069
```

---

### 5. Ingresar al sistema desde el navegador

Abre:

```
http://localhost:8069
```

---

### 6. Iniciar sesión

Credenciales de acceso:

- **Usuario:** `admin`
- **Contraseña:** `admin`

---

### 7. Crear su propia rama de trabajo

#### Paso a paso para crear una rama de trabajo:

1. Asegúrate de estar en la raíz del proyecto:

   ```bash
   cd validador_edad_odoo
   ```

2. Verifica que estás en la rama base (`dev`):

   ```bash
   git checkout dev
   ```

3. Actualiza tu rama base con los últimos cambios remotos:

   ```bash
   git pull origin dev
   ```

4. Crea una nueva rama basada en `dev`:

   ```bash
   git checkout -b feature/nombre-del-feature
   ```

   Reemplaza `nombre-del-feature` por algo representativo, por ejemplo:

   ```bash
   git checkout -b feature/validacion-menores
   ```

5. Ya puedes comenzar a trabajar normalmente. Para guardar tus cambios:

   ```bash
   git add .
   git commit -m "feat: implementación inicial del validador de edad"
   git push --set-upstream origin feature/validacion-menores
   ```

6. Verifica en GitHub que tu rama aparece publicada.

---

