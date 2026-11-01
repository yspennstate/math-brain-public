#!/bin/bash
cd "$(dirname "$0")"
timeout 1500 python attack_corollary.py 10 2 40 11 pw > ../logs/corollary_n10_k2_pw.log 2>&1
timeout 1500 python attack_corollary.py 10 3 30 12 pw > ../logs/corollary_n10_k3_pw.log 2>&1
timeout 1500 python attack_corollary.py 14 2 25 13 > ../logs/corollary_n14_k2.log 2>&1
timeout 1500 python attack_corollary.py 14 3 25 14 > ../logs/corollary_n14_k3.log 2>&1
