#!/usr/bin/env bash

bold()   { printf "\033[1m%s\033[0m" "$1"; }
green()  { printf "\033[32m%s\033[0m" "$1"; }
blue()   { printf "\033[34m%s\033[0m" "$1"; }
yellow() { printf "\033[33m%s\033[0m" "$1"; }
red()    { printf "\033[31m%s\033[0m" "$1"; }

route_message() {
    mode="$1"
    shift
    msg="$*"

    case "$mode" in
        direct) printf "%s %s\n" "$(green "[direct]")" "$msg" ;;
        wide)   printf "%s %s\n" "$(blue "[wide]")" "$msg" ;;
        all)    printf "%s %s\n" "$(yellow "[all]")" "$msg" ;;
        auth)   printf "%s %s\n" "$(red "[auth]")" "$msg" ;;
        *)      printf "%s Unknown route: %s\n" "$(red "[error]")" "$mode"; exit 1 ;;
    esac
}

