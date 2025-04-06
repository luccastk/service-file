#!/bin/bash

HOST=$1
PORT=$2
shift 2
CMD="$@"

TIMEOUT=120
WAIT_INTERVAL=2
ELAPSED=0

echo "⏳ Aguardando $HOST:$PORT por até $TIMEOUT segundos..."

while ! nc -z "$HOST" "$PORT"; do
  sleep "$WAIT_INTERVAL"
  ELAPSED=$((ELAPSED + WAIT_INTERVAL))
  echo "⌛ $HOST:$PORT ainda não está disponível... [$ELAPSED s]"

  if [ "$ELAPSED" -ge "$TIMEOUT" ]; then
    echo "❌ Timeout de $TIMEOUT segundos atingido. Abortando!"
    exit 1
  fi
done

echo "✅ $HOST:$PORT está disponível!"

exec $CMD

