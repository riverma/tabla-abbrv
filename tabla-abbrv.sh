#!/bin/bash
# Description: this script takes an input abbreviated Tabla bole sentence
#              and properly capitalizes it.
# Usage: $ tabla-abbrv.sh "dt dgtnkt"
#        $ DhaTi DhaGeTuNaKaTa
#

if [ $# -ne 1 ];then 
  echo "Usage: $0 <abbreviated notation>"
  echo "  example: $0 tabla-abbrv.sh 'dt dgtnkt'"
  echo "           DhaTi DhaGeTuNaKaTa"
  exit 1;
fi

echo $1 | sed -f ./tabla-abbrv.sed
