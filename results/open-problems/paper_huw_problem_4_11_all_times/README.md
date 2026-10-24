# Hasebe–Ueda–Wang Problem 4.11: all-time failure of strong log-unimodality

## Source question

Takahiro Hasebe, Yuki Ueda and Jiun-Chau Wang, *Log-unimodality for free positive multiplicative Brownian motion*, arXiv:2009.13848 (2020), journal version *Colloquium Mathematicum* 169 (2022), 209–226, Problem 4.11.

The source asks whether the free positive multiplicative Brownian law `sigma_t` fails free multiplicative strong log-unimodality for **every** `t>0`. The source's Theorem 4.9 proves failure only for sufficiently small positive time.

## What this package proves

For every real `t>0`, the explicit log-unimodal witness

```text
ell(t) = max(100, 95*pi*t)
d      = 19/20
b(t)   = sqrt(pi*d*t/ell(t))
p(t)   = 8/(5*ell(t))

log_* nu_t
  = p(t) delta_0
    + (1-p(t))/(ell(t)b(t)) 1_{[-ell(t)b(t),0]}(y) dy
```

satisfies that `sigma_t boxtimes nu_t` is **not** log-unimodal. Hence `sigma_t` is not `boxtimes`-strongly log-unimodal for any `t>0`.

The proof is source-literal: it uses Hasebe–Ueda–Wang Lemma 4.1, constructs four positive roots of the exact source level equation, and verifies the source admissibility condition `a(t) in (0,1/t)` through the exact identity

```text
a(t)*pi*t = b(t) < pi.
```

The fixed R18 metric is therefore `T=+infinity`.

## Files

- `main.tex` — self-contained proof of the source-matching theorem.
- `check.py` — exact `Fraction`-arithmetic checker for every finite numerical inequality used in the proof.
- `check.out` — archived PASS output of the checker.

The checker is the same finite core that was independently re-executed by P26; the theorem-sized analytic argument is written in `main.tex`.

## Independent audits

Two distinct external repository tracks independently audited the source-matching claim `R18-I0080-C007` end to end:

1. `R17-AUDIT-R18-I0080-C007-ENDTOEND-002 = PASS_FULL_MATHEMATICAL_PROOF`
   - report: `runs/R17/20260916_1515Z_spantrunc_a63e.md`
2. `P26-AUDIT-R18-I0080-C007-ENDTOEND-05 = PASS_FULL_MATHEMATICAL_PROOF / SOURCE_LITERAL_PASS / FINITE_CERT_REEXECUTED`
   - report: `proofnet24/P26-proof-audit-recovery/runs/2026-09-16/2026-09-16_21-58-44__run-report.md`
   - reexecution transcript: `proofnet24/P26-proof-audit-recovery/artifacts/2026-09-16/2026-09-16_21-58-44__r18_c007_exact-reexecution.txt`

The later atomless strengthening `R18-I0080-C008` is deliberately **not** used in this paper package because the two full closure audits were performed on the source-matching C007 theorem. The package therefore does not silently enlarge the audited claim.

## Prior-art check and status discipline

A bounded current-status search was performed on 2026-09-16 using the exact arXiv identifier/title, `Problem 4.11`, `boxtimes-strongly log-unimodal`, the three author names, later author papers, and accessible citing/related records. No accessible later paper was found claiming this exact all-time resolution. Recent related work on explicit representations of free positive multiplicative Brownian motion does not, in its accessible abstract/search record, claim to settle Problem 4.11.

This negative search is **not** a proof of global novelty or absence from all literature. Before public submission, run a normal author-level bibliography search again and check citing papers manually.

## Scope exclusions

This package does **not** address:

- Hasebe–Ueda additive Problem 3.3 (already a different posted/settled track in this repository),
- Hasebe–Ueda–Wang multiplicative Problem 4.7,
- Hasebe–Ueda–Wang Problem 4.3 (the separate P20 track),
- the stronger atomless-witness claim C008.

It proves exactly the source-level Problem 4.11 statement described above.

## Repository closure status

Under the repository protocol, the source-matching mathematical target is **PROVED / AUDIT-COMPLETE / PACKAGED**. This is an internal closure label, not a claim of external peer review or public publication.
