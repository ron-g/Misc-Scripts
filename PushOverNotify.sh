#!/bin/bash

ConfFile="$0"
ConfFile=$(basename "$ConfFile")
ConfFile="${ConfFile%.sh}.conf"

if [ -f "$ConfFile" ]
then
	source "$ConfFile"
else
	printf -- "\"${ConfFile}\" wasn't found. This is fatal.\n\n"
	exit 1
fi

if [ -z "$1" ]
then
	printf -- "Provide (quoted) message.\n\n"
	exit 2
else
	POmsg="$1"
fi

curl -s \
  --form-string "user=${POuser}" \
  --form-string "token=${POtoken}" \
  --form-string "message=${POmsg}" \
  "${POurl}"
