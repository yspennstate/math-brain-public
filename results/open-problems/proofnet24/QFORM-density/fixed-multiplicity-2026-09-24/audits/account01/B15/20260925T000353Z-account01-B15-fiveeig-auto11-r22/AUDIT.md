# account01/B15 r22 — source-pinned full audit

Objective: QFORM-FIXED-MULTIPLICITY-AUDIT-20260924.

Fresh controls:
- AGENTS.md blob 207b1dfce26c35dd8437cb469a807071aa5a0f08.
- CURRENT_OBJECTIVE.md blob c76cecdc06d46bee93bd2021cfe49ee0fe35b0cc.

Historical source pin:
- commit 7c0d6e60946b19423e6400a12d34b473cf0591e2
- manuscript blob 183ccd294763214e6a707e8d4749ff9a8cf7006d
- SHA-256 9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69
- 790 lines.

Current owner source:
- proofnet24/QFORM-density/five-eigenvalues-paper-2026-09-25/paper.tex
- current blob bbebd6f6c5a27e9f639186a305008ab43a481e70
- manifest SHA-256 040d03beea0f9d652992b9ea9dca71e4f2df98cdeef942b291b1c73ec65cdab3
- 715 lines.

## Fatal defects

NONE.

## Historical 790-line baseline

Verdict after exact repair bookkeeping: theorem chain PASS, with two local source findings.

- lines 1–269: PASS.
- line 270: exposition wording should say zero-beta factors are **bounded by one** and can be dropped. The mathematical step is valid; there may be several such factors.
- lines 271–471: PASS.
- lines 472–474: GAP (repairable presentation gap). The negative hyperbola tail cannot reuse the coordinate chosen large for the positive-tail vector. Choose a fresh coordinate i' with |w_{i'}| >= rho_0/sqrt(2). Since |u|=|w|, the cutoff and every constant are unchanged. This is exactly the repair now present in the five-eigenvalue source.
- lines 475–781: PASS after that repair.
- lines 782–789: UNCHECKED external bibliography metadata.
- line 790: PASS.

No FALSE mathematical conclusion follows from either local source issue.

Fourier/Riesz lens:
- Gaussian coefficient 1/(2 sqrt(pi v)): PASS.
- negative-half Riesz coefficient 1/sqrt(2 pi): PASS.
- historical order three gives |t|^{-3/4}: not L1, but with |t|^{-1/2} Riesz weight gives |t|^{-5/4}: PASS.
- historical order five gives |t|^{-5/4} directly and therefore C0: PASS.
- singular Schur limiting argument: PASS.

Historical verify.py/checks.json were read. Recorded result is PASS (534 exact interpolation seeds, 18 exact volume cases, 240 numerical Schur threshold cases, 30 graph-weight cases). Fresh execution in this invocation: UNCHECKED.

## Current 715-line five-eigenvalue source

- lines 1–246: PASS.
- line 247: same wording ambiguity as historical line 270; read as “the zero-beta factors are bounded by one and are dropped.” Mathematical step PASS; wording edit recommended.
- lines 248–455: PASS.
- lines 456–466: PASS with the repaired separate-coordinate negative-tail argument.
- lines 467–686: PASS.
- lines 687–714: UNCHECKED external bibliography metadata.
- line 715: PASS.

Independent mathematical verdict:
s_5(A)>=s => ||p_Q||_(infinity,ess) <=270 K^2/s: PASS.
s_3(A)>=s => sup_a E|Q-a|^{-1/2} <=77 K/sqrt(s): PASS.

Fresh Python/Lean execution was not rerun here and is UNCHECKED. Repository-recorded check/Lean logs were read only as corroboration.

## New four-direction finding

See the companion improvement. The naive extension of the zero-hub two-hub lemma to an arbitrarily small nonzero hub block is false without using the s_4 spectral residual. There is an explicit no-pivot, rank-two family with nonsingular cross Gram and unbounded density. Under s_4(A)>=1 the Schur residual must instead have two singular values >=1, so any valid small-hub receiver must exploit that residual.

Four eigenvalues: OPEN.
Three-eigenvalue bounded-density conjecture: OPEN.
