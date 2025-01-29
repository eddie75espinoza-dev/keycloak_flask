# cloaktest

![Static Badge](https://img.shields.io/badge/Estatus-En%20Desarrollo-yellow)
![Static Badge](https://img.shields.io/badge/Versi%C3%B3n-1.0.0-blue)
![Static Badge](https://img.shields.io/badge/Lenguaje-Python-blue)
![Static Badge](https://img.shields.io/badge/Pruebas-En%20Desarrollo-yellow)

## **Descripción General**

Prueba de login con keycloak

## Índice

* [Requisitos de Instalación](#requisitos-de-instalación)
* [Guía de Configuración](#guía-de-configuración)
* [Descripción de Endpoints](#descripción-de-endpoints)
* [Pruebas](#pruebas)

## Requisitos de Instalación

Para ejecutar **cloaktest**, necesitas tener instalados los siguientes programas:

### Instalación de Docker
- [Docker](https://docs.docker.com/get-docker/): Para gestionar contenedores.

### Instalación de Docker Compose
- [Docker-compose](https://docs.docker.com/compose/install/): Para definir y ejecutar aplicaciones multi-contenedor.

## Guía de Configuración

### Configurar el archivo .env

Crea un archivo _.env_ en la base del proyecto con las siguientes variables

```bash
# AMBIENTE DE LA APLICACIÓN (seleccionar uno: production, development, staging)
ENVIRONMENT=production

HOST=0.0.0.0
PORT=5700

BASE_URL=services/pulso/login # Usado solo en producción

BACKEND_CORS_ORIGINS=http://localhost,http://localhost:5700

TOKEN_SECRET_KEY=<token_secret_key>
SUB=cloaktest # Identificador usuario token

# Configuración de la base de datos
POSTGRES_USER=<usuario_de_postgres>
POSTGRES_PASSWORD=<contraseña_de_postgres>
POSTGRES_HOST=<host_de_postgres>
POSTGRES_PORT=<puerto_de_postgres>
POSTGRES_DB=<nombre_de_la_base_de_datos>
```

### Construir y Levantar los Contenedores

Ejecuta los siguientes comandos para construir y levantar los contenedores:

```bash
docker-compose build
docker-compose up -d
```
Para detener el servicio, ejecutar el siguiente comando en la terminal:

```bash
docker-compose down -v
```

## Descripción de Endpoints


## Pruebas

Para verificar el correcto funcionamiento del servicio web, ejecute el siguiente comando en la terminal mientras el contenedor Docker esté activo:

```bash
docker exec -it cloaktest pytest
```