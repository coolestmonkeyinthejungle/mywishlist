#!/bin/sh
# wait-for-mysql.sh

set -e

host="$1"
port="$2"
shift
shift
cmd="$@"

until nc $host $port; do
  >&2 echo "MySQL is unavailable - sleeping"
  sleep 1
done

>&2 echo "MySQL is up - executing command"
exec $cmd


