#!/bin/bash

# Start SQL Server
/opt/mssql/bin/sqlservr &

echo "Waiting for SQL Server to start..."

# Loop until sqlcmd can connect
until sqlcmd -S localhost -U sa -P 'YourStrong!Passw0rd' -C -Q "SELECT 1" > /dev/null 2>&1
do
    echo "SQL Server is still starting up..."
    sleep 1
done

echo "SQL Server is up. Running restore script..."

# Debug: List backup directory contents
echo "Contents of backup directory:"
ls -la /var/opt/mssql/backup

# Debug: Check file permissions
echo "File permissions:"
ls -la /var/opt/mssql/backup/AdventureWorksDW2017.bak

# Run the restore script
sqlcmd -S localhost -U sa -P 'YourStrong!Passw0rd' -C -i /var/opt/mssql/backup/restore.sql

# Keep container running
wait