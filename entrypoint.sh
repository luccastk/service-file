#!/bin/bash

echo "⏳ Aguardando Eureka em $1:$2..."
/wait-for-it.sh $1 $2

echo "🚀 Aplicando migrations..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "🟢 Iniciando servidor Django..."
exec python manage.py runserver 0.0.0.0:8000
