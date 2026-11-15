#!/bin/bash
# Batch 5 source search, 14 Nov 2026: recent open-problem collections in probability on arXiv
cd "$(dirname "$0")" || exit 3
mkdir -p famous_lit_1114/b5
q() {
  curl -s --max-time 60 "https://export.arxiv.org/api/query?search_query=$2&sortBy=submittedDate&sortOrder=descending&max_results=25" > "famous_lit_1114/b5/$1.xml"
  echo "$1 $(grep -c '<entry>' "famous_lit_1114/b5/$1.xml")"
  sleep 4
}
q OP1 'cat:math.PR+AND+ti:%22open+problems%22'
q OP2 'cat:math.PR+AND+ti:%22open+questions%22'
q OP3 'cat:math.PR+AND+ti:problems+AND+ti:survey'
q OP4 'cat:math-ph+AND+ti:%22open+problems%22'
q OP5 'cat:math.CO+AND+cat:math.PR+AND+ti:%22open+problems%22'
echo done
