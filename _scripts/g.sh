#!/bin/bash
# usage: g.sh URL [outfile]
if [ -n "$2" ]; then curl -sSL --cacert <SCRATCH>/bundle2.crt -m 180 --retry 2 -A "Mozilla/5.0 (X11; Linux x86_64)" -o "$2" -w "%{http_code} %{size_download}\n" "$1"; else curl -sSL --cacert <SCRATCH>/bundle2.crt -m 120 --retry 2 -A "Mozilla/5.0 (X11; Linux x86_64)" "$1"; fi
