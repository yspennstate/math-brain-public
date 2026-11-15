#!/bin/bash
# Recheck of the two strong survivors (F12, H11) by author, 14 Nov 2026
cd "$(dirname "$0")" || exit 3
mkdir -p famous_lit_1114/rc
q() {
  curl -s --max-time 60 "https://export.arxiv.org/api/query?search_query=$2&sortBy=submittedDate&sortOrder=descending&max_results=20" > "famous_lit_1114/rc/$1.xml"
  echo "$1 $(grep -c '<entry>' "famous_lit_1114/rc/$1.xml")"
  sleep 4
}
q F12_junk 'au:Junk+AND+ti:polymer'
q F12_lacoin 'au:Lacoin+AND+ti:polymer'
q F12_crit 'ti:%22directed+polymer%22+AND+abs:%22critical+point%22+AND+abs:%22weak+disorder%22'
q H11_gl 'au:Gheissari+AND+au:Lubetzky'
q H11_sw4 'abs:%22Swendsen-Wang%22+AND+abs:%22q%3D4%22'
q H11_sw 'ti:%22Swendsen-Wang%22'
echo done
