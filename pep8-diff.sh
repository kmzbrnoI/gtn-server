#!/usr/bin/env bash

# Obtain the path to the work directory
RELATIVE_SOURCE_PATH=`dirname ${BASH_SOURCE[@]}`
SOURCE_PATH=`readlink -f ${RELATIVE_SOURCE_PATH}`

if [ "$1" == "" ]
then

    echo "./pep8-diff.sh (show|apply)"

elif [ "$1" == "apply" ]
then

    autopep8 --max-line-length=100 --in-place -aaa -r ${SOURCE_PATH}/gtn_server/

elif [ "$1" == "show" ]
then

    TMP_FILE=`mktemp`

    autopep8 --max-line-length=100 --diff -aaa -r ${SOURCE_PATH}/gtn_server/ >> ${TMP_FILE}

    if [ -s ${TMP_FILE} ]
    then
        cat ${TMP_FILE}
        rm -f ${TMP_FILE}
        exit 1
    else
        rm -f ${TMP_FILE}
        exit 0
    fi

fi
