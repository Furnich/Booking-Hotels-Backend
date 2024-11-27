#!/usr/bin/env bash

# Use this script to wait for a service to become available.
# Usage: wait-for-it.sh host:port [timeout] [-- command args]
# Example: wait-for-it.sh db:5432 -- echo "Database is up"

TIMEOUT=15
WAITFORIT_CMD="wait-for-it"

# Получаем хост и порт из первого аргумента
HOST=$1
PORT=$(echo "$HOST" | cut -d: -f2)
HOST=$(echo "$HOST" | cut -d: -f1)

# Если второй аргумент указан, используем его как таймаут
if [ $2 != "" ]; then
    TIMEOUT=$2
fi

# Сдвигаем аргументы для дальнейшей обработки
shift 2

# Проверяем, установлен ли nc
command -v nc >/dev/null 2>&1 || { echo "nc (netcat) is required but it's not installed. Aborting." >&2; exit 1; }

# Функция для проверки доступности сервиса
check_service() {
    nc -z "$HOST" "$PORT"
}

# Ожидаем, пока сервис станет доступным
echo "Waiting for $HOST:$PORT..."
for i in $(seq 1 "$TIMEOUT"); do
    if check_service; then
        echo "$HOST:$PORT is available"
        break
    fi
    sleep 1
done

if ! check_service; then
    echo "Timeout: $HOST:$PORT is still not available after $TIMEOUT seconds"
    exit 1
fi

# Если есть дополнительные команды для выполнения, выполняем их
if [ "$#" -gt 0 ]; then
    exec "$@"
fi
