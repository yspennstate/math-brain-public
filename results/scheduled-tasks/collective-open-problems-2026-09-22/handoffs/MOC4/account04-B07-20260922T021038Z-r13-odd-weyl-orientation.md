# MOC4 handoff — account04/B07 r13

Run: `20260922T021038Z-account04-B07-MOC4-r13`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

Canonical scientific report: `proofnet24/collective-MOC4/account04/B07/20260922T021038Z-account04-B07-MOC4-r13/REPORT.md` in `yspennstate/math-open-problems`, first report commit `89fe5ebe78b671f1a7f46624ebcd385ceea91ddd`. Preserve-history notation correction: `CORRECTION.md`, commit `b2bebad230023a41b0fbe1b4092679ee9aa0304f`.

## Exact new result

Write each `2 x 2` exterior-square block of `O=Lambda^2 U in SO(6)` as the real map `z -> m z + n zbar`. Then the exact oriented minor channels are

`q+ = |m|^2 = (r+d)/2`, `q- = |n|^2 = (r-d)/2`,

and the full structured support objective is

`Q = sum[(K+X/2)q+ + (-K+X/2)q-]`.

Nonnegativity plus row/column transport alone has 48 coloured matching vertices. The 24 even-minus vertices are exactly the genuine `S4`/`SO(6)` endpoints; the 24 odd-minus vertices lie in the orientation-reversing `O(6)` component.

Using the exact structured `(K,X)` from account01/B07 `20260922T013731Z-b07-moc4-r11b`, exact Fraction enumeration gives

`best_even = 13195057/5120000`,

`best_odd = 20773731/5120000`,

`best_odd-best_even = 3789337/2560000 > 0`.

Thus the orientation-forgetting 48-state Weyl/Birkhoff relaxation is false on an actual source-valid MOC4 coefficient pair. This is not a target counterexample.

The replacement exact orientation theorem is:

For every `O in SO(6)`, every `rho in S3`, and every odd sign pattern epsilon,

`sum_alpha sqrt(q^{epsilon_alpha}_{alpha,rho(alpha)}) <= 2`,

hence also `sum q_selected <= 2`.

Proof: phase-optimize each selected `2 x 2` block against an orthogonal block of the requested orientation, assemble the resulting odd block-monomial `J in O(6)` with `det J=-1`, and use `tr(J^T O)<=4` for every orientation-reversing orthogonal `6 x 6` matrix. Each optimized block pairing equals `2 sqrt(q_selected)`.

## Inputs applied

- Team lead account03/B07 latest complete version read: `20260922T013930Z-account03-B07-MOC4-r11`, zero-entry common-lift no-go, blob `47f09f9f722aa8501330ca532a2ca261474c681c`.
- Named partner account01/B08 latest complete result read and applied: `20260922T013942Z-b08-moc4-r11`, exact roof/parity refutation. It forces retention of the full `X`-dependent support objective.
- Exact structured witness source: account01/B07 `20260922T013731Z-b07-moc4-r11b`.

## Next unpaid implication

Use the odd-Weyl overlap inequality together with the full off-diagonal block-orthogonality equations to prove that the structured spectral weights cannot convert the forbidden odd endpoint advantage into an actual `SO(6)` support violation. Do not return to the refuted parity roof or any unrestricted positive common lift.
