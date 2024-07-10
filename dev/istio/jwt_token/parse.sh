#!/bin/bash

# Проверка на количество аргументов
if [ "$#" -ne 7 ]; then
  echo "Usage: $0 <iss> <sub> <aud> <iat> <exp> <gty> <azp>"
  exit 1
fi

# Присваивание переменных аргументам
iss=$1
sub=$2
aud=$3
iat=$4
exp=$5
gty=$6
azp=$7

# Вывод значений
echo "Issuer: $iss"
echo "Subject: $sub"
echo "Audience: $aud"
echo "Issued At: $iat"
echo "Expiration: $exp"
echo "Grant Type: $gty"
echo "Authorized Party: $azp"

