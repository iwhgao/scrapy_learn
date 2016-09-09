#!/usr/bin/env bash

# ------------------------------
# version: v1.0.0
# author: deangao 
# license: Apache Licence
# contact: deangao@webank.com
# file: ${NAME}.sh
# time: 2016/9/6 20:08
# ------------------------------

set -u

if [ $# -lt 2 ]
then
    echo "Usage $0 [erase_db|drop_table]"
    exit
fi

MYSQL_BIN=mysql
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PWD=''

if [ $1 == "erase_db" ]
then
    ${MYSQL_BIN} -u${MYSQL_USER} -p${MYSQL_PWD} -h${MYSQL_HOST} < ./erase_db.sql
fi

if [ $1 == "drop_table" ]
then
    ${MYSQL_BIN} -u${MYSQL_USER} -p${MYSQL_PWD} -h${MYSQL_HOST} < ./drop_table.sql
fi
