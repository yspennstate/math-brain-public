#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
command -v pdflatex >/dev/null || { echo 'pdflatex is required.' >&2; exit 1; }
for n in 1 2 3; do
  pdflatex -interaction=nonstopmode -halt-on-error paper.tex > "compile_pass${n}.log"
done
printf 'Built paper.pdf from paper.tex. PDF bytes may vary by TeX version and build timestamp.\n'
