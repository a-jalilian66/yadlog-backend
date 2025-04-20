#!/bin/bash

# Settings
DB_CONTAINER="yadlog_postgres"
BACKUP_DIR="/var/backups/db"
DATE=$(date +"%Y-%m-%d_%H-%M")


# Create a backup directory
mkdir -p BACKUP_DIR

# Taking a backup of the database
docker exec $DB_CONTAINER pg_dump -U $POSTGRES_USER $POSTGRES_DB | gzip > $BACKUP_DIR/db_backup_$DATE.sql.gz


# Delete files older than 10 days
find $BACKUP_DIR -type f -mtime +10 -name '*.sql.gz' -exec rm {} \;
