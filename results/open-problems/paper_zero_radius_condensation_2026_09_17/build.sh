#!/bin/sh
set -eu
cd "$(dirname "$0")"
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
python3 code/check_uniform_windows.py > /tmp/janson_uniform_check.json
cmp code/checks_uniform.json /tmp/janson_uniform_check.json
python3 code/audit_stress_checks.py > /tmp/janson_stress_check.json
cmp code/checks_stress.json /tmp/janson_stress_check.json
