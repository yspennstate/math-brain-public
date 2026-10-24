# account03/B08 r43 handoff — Pythagorean scalar-Schur area

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T191921Z-account03-B08-qform-diffuse-r43`  
Status: supporting theorem proved; full QFORM and global continuity remain OPEN.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

Fresh final control observed at brain main `74d9d27ac15202296478999e802d1421ac814fa1`; `scheduled_tasks/README.md` still carries owner continuation `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`, all-QFORM revision `2026-09-22.5`, and owner-control revision `2026-09-22.15`. `CORRECTION_INBOX.json` SHA remained `6bdbd9987a4eefeba79d53915cfe7e232263f8ec`; no later stop/reassignment was found.

Canonical mathematics:

`yspennstate/math-open-problems@9257ca12771fa4e7f18a4a5f96e5c9a2e5039cef`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260923T191921Z-account03-B08-qform-diffuse-r43/REPORT.md`

with `CHECKS.py`, `CHECKS.txt`, and `CLAIMS.json` in the same immutable run folder.

## New exact identity

For a physical scalar pivot `a!=0`, two physical hub rows `M in R^{2xm}`, pivot-to-hub vector `h=(h1,h2)`, and pivot-to-partner row decomposed orthogonally as

`b=k^T M+e`, `e perpendicular row(M)`,

put `d=a-k.h` and `M'=M-hb/a`. Then

`det(M'M'^T)
 =(d^2/a^2)det(MM^T)
 +(||(-h2,h1)M||^2/a^2)||e||^2.`

The two terms are orthogonal exterior components. Orthogonal leakage therefore cannot cancel aligned Schur area.

Using the exact-rank-two crossing estimate from the reviewed projected-crossing source plus a self-contained dependence-safe half-kernel estimate gives

`||p_Q||_infinity <= C_* |a|^(-1/2)[s1(M')s2(M')]^(-1/4)`,

`C_*=8(2/3)^(1/4)=7.228816028878758...`,

for the full conditional/unconditional form with arbitrary same-bank quadratic-affine curvature retained. This proves essential boundedness, not continuity.

## Actual r42/R2 compiler

For the r42 R2 state `s1(C)>3L/8`, `s2(C)>=L/8`, let `p` be a designated physical scalar pivot with `|a|>=tau L` and let the other two triangle coordinates be the physical pair.

Either the pivot-incidence exterior bank is localized:

`V_p1+V_p2>9L^4/8192`,

or the pivot-excluding pair has

`s1(M)s2(M)>[3/(64sqrt2)]L^2`.

In the latter case, if either

`|a-k.h|>=|a|/2`

or

`||(-h2,h1)M|| ||e|| >= [3/(128sqrt2)]|a|L^2`,

then

`||p_Q||_infinity <20.148 tau^(-1/2)/L`.

Otherwise the previously vague aligned survivor is sharpened to the simultaneous packet

`|a-k.h|<|a|/2`

and

`||(-h2,h1)M|| ||e||<[3/(128sqrt2)]|a|L^2`.

No half-bank split is required in this receiver.

## Necessary obstruction and partner application

A target-valid 5x5 matrix in the report has characteristic polynomial

`(lambda-1)(lambda+1)^2(lambda^2-2lambda-1)`

but exact adaptive factor `d=a-k.h=0`; therefore the bare three-large-eigenvalue condition cannot force `d` away from zero. This refutes only that possible intermediate shortcut, not QFORM.

Designated partner `account04/B08`, source

`yspennstate/math-open-problems@abbec61f52e1f4b4d367fd67e73e4d2501ac9c74`,

applies to the exact endpoint

`Q=LX0^2+2LRU1V1+2LR^{-1}U2V2`, `R>=3`,

and gives the actual inequality `||p_Q||_infinity<7.251/L`. In the new variables this endpoint has `a=d=L`, `h=b=e=0`, and partner singular product `L^2`, so it lies exactly in the Schur-survival branch.

## Next B08 implication

Attack the simultaneous adaptive-cancellation packet by combining the surviving rank-one post-Schur channel with the pivot-induced outside square direction, while retaining arbitrary same-bank curvature. In parallel, hand the aggregate pivot-incidence exterior bank to a localized-coordinate receiver without selecting a single minor. R1 and small/zero-pivot states remain separate debts.

Regression: 5,000 seeded instances of the exact identity; max normalized discrepancy `2.554e-11`; checker terminates `QFORM_B08_R43_CHECK_PASS`.
