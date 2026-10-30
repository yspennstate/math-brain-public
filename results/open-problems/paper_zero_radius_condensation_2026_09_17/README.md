# Uniform condensation windows for zero-radius random allocations

Yitzchak Shmalo  
Einstein Institute of Mathematics, The Hebrew University of Jerusalem  


## Contents and status

This folder contains the full manuscript source and five documented review passes, prepared on 17 September 2026. The paper proves a uniform-window theorem implying a complete-condensation subsequence for every admissible full positive-density mass path with fixed zero-radius weights. It also gives the sharp sampling criterion and a simply generated tree root consequence.

Source target: Janson, Probability Surveys 9 (2012), **Problem 19.41**, p. 228; this is **Problem 18.40** in arXiv:1112.0510v1. The positive-mean Problem 19.40 (preprint 18.39) is not addressed.

**Status:** complete research draft after five same-assistant review passes. No unresolved mathematical gap was identified in those passes. Independent referee review and publication novelty are not certified. The reports are not five independent audits. The author's general funding, competing-interest, and AI-use declarations are included in the paper.

The compiled 11-page paper and combined audit PDF are supplied with the conversation delivery; this repository folder retains their reproducible textual source. The downloadable conversation archive additionally contains the compiled PDFs.

## Build

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
python3 code/check_uniform_windows.py > /tmp/checks_uniform.reproduced.json
cmp code/checks_uniform.json /tmp/checks_uniform.reproduced.json
python3 code/audit_stress_checks.py > /tmp/checks_stress.reproduced.json
cmp code/checks_stress.json /tmp/checks_stress.reproduced.json
```

A standard TeX installation is required for the PDF. The Python scripts use only the standard library; do not run them with `python -O`, which disables assertions. The uniform-window script imports the bundled `code/check_full_path.py`, whose content hash is checked.

To compile the optional combined audit document using Pandoc:

```bash
python3 code/build_audit_report.py
pandoc audits/audit_report.md -o audits/audit_report.pdf --pdf-engine=pdflatex
```

## Evidence

The earlier output was reproduced byte-for-byte. Additional exact checks include 18,000 sharp insertion comparisons, 13,240 coarse comparisons, three complete labelled double counts, 84 geometric-tail identities, and 23,713 plane trees checking 422 conditional root identities. All final assertions passed. These tests do not replace the limiting proof.

See `audits/SUMMARY.md` and the five numbered reports. `audits/preflight.json` records label, build, page-bound and PDF metadata checks. `manifest.json` identifies the delivered textual files by SHA-256 and Git blob hash.

The predecessor is the immutable source at:

`runs/2026-09-17/direct_janson1840_uniform_windows_13-03-24Z/`

commit `5883e3eb3d9fbfe8d6fe924b1c85817ab9528037`.

No prior research report, shared source-status ledger, or scheduled task is altered by this paper package. The repository remains private.
