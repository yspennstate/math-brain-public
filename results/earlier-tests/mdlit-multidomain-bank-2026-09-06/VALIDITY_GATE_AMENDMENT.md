# Prospective validity exclusions, 2026-09-06

The sealed bank and its original review stay unchanged. A review annotation was
previously descriptive: all 23 items marked `valid: no` remained eligible, and
five appeared in the initial 320-item sample. No model comparison is established
by this finding.

The sampler now excludes every `no` or `unsure` record before drawing and binds
the exact review bytes into the sample. Missing, malformed, or changed review
metadata blocks serving and grading. Every frozen sample is checked for rejected
IDs and changed question text before the model transport is called. Both the
inherited grader and `grade_md.py` enforce the same gate, including extra arms.

Existing samples are preserved. Choose a fresh `MDLIT_RUN_DIR` for a prospective
sample, then regenerate all arms' notes for that sample. Do not append a receipt
to an old sample to disguise a retrospective population change. Samples cannot
be overwritten by the sampling command. Requests exceeding the eligible clean
or flawed population fail explicitly.

This gate excludes documented invalid items. It does not certify the remaining
unreviewed items or establish a beneficial brain effect. Any historical score
requires a separately labeled, explicit sensitivity analysis; the prospective
grader does not silently drop bad rows and retain the old result label.

Repair author: a separate repair lane. The author tested the repair; an independent
re-audit remains pending. Evidence is retained under the canonical audits home,
with answer-bearing snapshots kept private and outside retrieval ingestion.
