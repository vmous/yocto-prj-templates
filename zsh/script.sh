#!/usr/bin/env zsh
# -*- shell script -*-
#
# Driver script.
#
# -e        - exit on error (ERR_EXIT)
# -u        - exit if any variable is not defined (NO_UNSET)
# +pipefail - return error if any part of a pipe returns error (PIPE_FAIL)

set -eu
setopt +pipefail

usage() {
    echo "Driver script."
    echo ""
    echo "${0}"
    echo ""
}

BUILD_NAME=bdm-prediction
INSTANCE=$(TZ=UTC date +%Y%m%d)
IS_DEBUG_MODE=false

while [ "$#" -gt 0 ]; do
    PARAM=`echo $1 | awk -F= '{print $1}'`
    VALUE=`echo $1 | awk -F= '{print $2}'`
    case ${PARAM} in
        -h | --help)
            usage; exit;;
        --build_name)
            BUILD_NAME=${VALUE};;
        --instance)
            INSTANCE=${VALUE}
        --is_debug_mode)
            IS_DEBUG_MODE=${VALUE};;
        *)
            echo "Unkown parameter \"${PARAM}\""; usage; exit 1
    esac
    shift
done

# Run driver with above user arguments
