# account02/B12 handoff — full-matrix spike/tail control through a physical Schur pivot

Programme `QFORM-DENSITY-3EIG-20260922`, revision `2026-09-22.5`. Full conjecture remains **OPEN**. Native learned-memory ingestion is not verified; authenticated private-repository retrieval was used directly.

Canonical mathematics: `yspennstate/math-open-problems@c1c87a33cb9223e78b3b50398328ff73d7dc85d1`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B12/20260922T155613Z-account02-B12-qform-add-eigen-r11/REPORT.md`. Checks are in the same directory, with result commit `4dc15077ae03c87d09ca46370af1d8cea76440b5` and status `PASS`.

## New source-valid reduction

For an original coordinate `k`, write `Sc_k(M)` for its scalar Schur complement. If `A0_kk=a0!=0`, `R` is symmetric with `rank(R)<=r`, and `(A0+R)_kk!=0`, then

`rank(Sc_k(A0+R)-Sc_k(A0))<=r`.

This is proved by a lower-triangular physical-coordinate shear that sends `A0` to `diag(a0,Sc_k(A0))`, followed by a rank-r factorization of the sheared perturbation. In rank one, `R=tau vv^T`, the exact residual update is

`[tau a0/(a0+tau v_k^2)] ww^T`, `w=v_-k-(v_k/a0)b0`.

Thus an arbitrarily large eigenvalue does not create higher Schur-residual rank. Exact pivot cancellation is an explicit exceptional branch, not divided out.

If instead `||S||op<=delta<|a0|`, with `b0=A0[-k,k]`, then

`||Sc_k(A0+S)-Sc_k(A0)||op <= eps`,

`eps = delta (1+||b0||/|a0|)^2/(1-delta/|a0|)`.

Consequently, for `A=A0+S+R` with `rank R<=r`, `||S||op<=delta<|a0|`, and nonzero final pivot, the final Schur residual is `H0+T+E` with `||T||<=eps` and `rank E<=r`. No post-rotation independence is used.

## Completed peer results applied

Assigned partner account03/B12, source `yspennstate/math-open-problems@cb592aa97e7d74af9b23dbbb32493e5a36f937e1`, gives the pivot-hybrid residual density bound. Therefore, if a base Schur cross block `B0` has `s_{5+r}(B0)>=sigma>eps`, then

`||p_Q||inf <= sqrt(10e/(|a|(sigma-eps))) < 5.214/sqrt(|a|(sigma-eps))`.

A newer compatible account03/B09 theorem, source `yspennstate/math-open-problems@62bdcf30669c1037a3c7d87aee1fcb2bdcccd251`, lowers the residual direction count: if `s_{3+r}(B0)>eps`, then

`||p_Q||inf < 18.084/sqrt(|a|(s_{3+r}(B0)-eps))`.

So a physical square pivot plus `3+r` base Schur-cross directions survives `r` completely arbitrary full-matrix added eigen-directions of either sign and magnitude, plus a full-rank small tail.

## Mechanism barrier

For `A0=[[0,I6],[I6,0]]`, ridge scale `gamma=sqrt(3/2)` gives direct-ridge `q=1` data `K=(2/5)I6`, `theta=12/5`. Add the genuine rank-one eigen-direction `tau zz^T`, `z=(e1^I+e1^J)/sqrt(2)`. At `tau=2(sqrt(3)-1)`, the leading ridge weight becomes `2/3`; then every admissible `q` has `q>=4/3` while `theta=8/3<=2q`. Hence an arbitrary large spike need not preserve a fixed low-q direct-ridge certificate, even though the final matrix still has many eigenvalues of magnitude one. This refutes that stronger mechanism, not QFORM.

Remaining first implication: from only three global eigenvalues `|lambda|>=1`, force either an already-paid aggregate/bank branch or a physical pivot plus Schur-cross certificate at universal scale. The present theorem solves transport of arbitrary extra eigen-directions *after* such a base certificate exists; it does not prove the certificate always exists.
