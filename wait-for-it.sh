#!/bin/bash
# wait-for-it.sh

set -e

host="$1"
shift
cmd="$@"

until mysql -h"$host" -P"3306" -u"$DB_USERNAME" -p"$DB_PASSWORD" -e 'select 1'; do
  >&2 echo "MySQL is unavailable - sleeping"
  sleep 1
done

>&2 echo "MySQL is up - executing command"
exec $cmd 