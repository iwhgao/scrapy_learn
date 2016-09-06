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

MYSQL_BIN=mysql
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PWD=

${MYSQL_BIN} -u${MYSQL_USER} -p${MYSQL_PWD} -h${MYSQL_HOST} < ./db_table.sql
