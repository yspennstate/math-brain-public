#!/bin/zsh
# Read-only extraction of the supplied PDF; outputs stay in this directory.
set -eu
date '+%Y-%m-%d %H:%M:%S %Z'
pdftotext -layout PAPER.pdf audit_pdf.txt
rg -n 'Theorem 1.1|Proposition 3.1|Lemma 3.2|Lemma 4.1|Proposition 4.2|Lemma 4.3|Proposition 4.4|Remark 4.5|Lemma 5.1|Lemma 5.2' audit_pdf.txt
du -sh .
