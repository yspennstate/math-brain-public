#!/bin/bash
# arXiv check of the famous-list replacement candidates, 14 Nov 2026: newest papers first, 10 per query
cd "$(dirname "$0")" || exit 3
mkdir -p famous_lit_1114
q() {
  curl -s --max-time 60 "https://export.arxiv.org/api/query?search_query=$2&sortBy=submittedDate&sortOrder=descending&max_results=10" > "famous_lit_1114/$1.xml"
  echo "$1 $(grep -c '<entry>' "famous_lit_1114/$1.xml")"
  sleep 4
}
q F10 'abs:%22random+conductance%22+AND+abs:heavy+AND+abs:quenched'
q F12 'ti:%22directed+polymer%22+AND+abs:%22dimension+3%22'
q F12b 'ti:%22directed+polymers%22+AND+abs:%22free+energy%22+AND+abs:%22d+%3D+3%22'
q F17 'abs:interlacements+AND+abs:%22phase+transition%22+AND+abs:sharp'
q G02 'abs:%22infinite+collision+property%22'
q G07 'abs:%22internal+DLA%22+AND+abs:fluctuations'
q G09 'abs:%22random+sequential+adsorption%22+AND+abs:jamming'
q G11 'abs:%22favorite+sites%22+OR+abs:%22favourite+sites%22'
q G22 'abs:%22real+zeros%22+AND+abs:%22random+polynomials%22+AND+abs:universality'
q H11 'abs:%22Swendsen-Wang%22+AND+abs:critical+AND+abs:mixing'
q J04 'abs:%22bootstrap+percolation%22+AND+abs:%22second+term%22'
q J04b 'au:Hartarsky+AND+abs:%22bootstrap+percolation%22'
q H12 'abs:%22Boolean+model%22+AND+abs:%22critical+intensity%22'
q H18 'abs:%22site+percolation%22+AND+abs:%22square+lattice%22+AND+abs:%22exact+value%22'
echo done
