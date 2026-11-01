#!/bin/bash
cd "$(dirname "$0")"
timeout 2400 python targeted_large.py 20 > ../logs/targeted_n20.log 2>&1
timeout 2400 python targeted_large.py 22 > ../logs/targeted_n22.log 2>&1
