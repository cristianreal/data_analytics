# Data Analytics

## Ejecutar servidores de los almacenes de datos
```bash
docker network create data_analytics_project
cd infrastructure/datastores
docker-compose -f docker-compose.minio.yml up -d 
docker-compose -f docker-compose.postgresql.yml up -d

```

# Crear esquema de lago de datos
- Crear un bucket llamado `datalake` y crear un estructura como la siguiente:
```bash
.
└── datalake/
    ├── datos crudos
    ├── datos procesados
        ├── año
            ├── mes
                ├── data.parquet
    └── datos con errores
        data.parquet
```

# Instalar Dagster
```bash
cd infrastructura/automatizacion
docker-compose -f docker-compose.dagster.yml  up --build -d
docker logs -f dagster
```
# Webservers
- Minio: https://localhost:9001
- Dagster: https://localhost:3000

# Superset
```bash
docker exec -it superset superset fab create-admin \
              --username admin \
              --firstname Superset \
              --lastname Admin \
              --email admin@data_analytics.com \
              --password data_analytics

docker exec -it superset superset db upgrade
docker exec -it superset superset init
```
