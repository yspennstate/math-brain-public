# fleet03/B18 r11b — application to the new thirteen-eigenvalue L2 theorem

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T131003Z-fleet03-B18-fixedmult-audit-r11b`

During the prepublication refresh, fleet04/B01 committed `beb9cc5cbb78b4fd4a8411862ac99fd7b7976034`, proving that the pinned manuscript machinery already yields a genuine dimension-free `s_13` theorem in `L^2`: in the no-pivot branch the order-four characteristic-function envelope is `1/|t|`, hence square integrable even though it is not absolutely integrable. This does **not** by itself give `L^infinity`.

The source-sharp Rudelson--Vershynin graph determinant proved in this B18 run improves that peer theorem quantitatively.

## Theorem

Let `X=(X_1,...,X_n)` have independent real coordinates with probability densities bounded by `K`, let `A=A^T`, `b in R^n`, `c in R`, and suppose

\[
s_{13}(A)\ge s>0.
\]

Then `Q=X^TAX+b^TX+c` has an `L^2(R)` density and

\[
\boxed{
\|p_Q\|_2<\sqrt{3810}\,{K\over\sqrt s}.
}
\]

No sign, moment, support, smoothness, identical-law, or remaining-spectrum assumption is imposed. Continuity is not asserted.

## Proof

Normalize `K=s=1`.

### No pivot

The manuscript's `k=4` spectral-to-volume argument gives a physical original-coordinate cut with

\[
Z_4(M)\ge 4^{-4}\kappa^4,
\qquad \kappa=1/80^2,
\]

so `Z_4(M)^(-1/8)<=160`. The source-sharp graph determinant from this run is

\[
|\phi_Q(t)|\le
\det\!\left(I+{t^2\over2\pi^2e}M^TM\right)^{-1/8}.
\]

Retaining the order-four coefficient gives

\[
|\phi_Q(t)|\le
\min\left\{1,{u\over|t|}\right\},
\qquad
u=\pi\sqrt{2e}\,Z_4(M)^{-1/8}
\le160\pi\sqrt{2e}.
\]

Therefore

\[
\|\phi_Q\|_2^2
\le4u
\le640\pi\sqrt{2e}.
\]

The Gaussian-mollification/Plancherel argument in fleet04/B01 identifies the law with an `L^2` density and gives

\[
\|p_Q\|_2^2
={1\over2\pi}\|\phi_Q\|_2^2
\le320\sqrt{2e}
<747.
\]

### Pivot branches

The scalar-pivot Schur complement under `s_13(A)>=1` retains at least twelve unit spectral directions and hence satisfies the improved `s_9` half-potential theorem from the companion B18 note:

\[
\sup_a E|R-a|^{-1/2}<381.
\]

The scalar-square profile then gives

\[
\|p_Q\|_\infty<3810,
\]

hence `||p_Q||_2^2<=||p_Q||_infty||p_Q||_1<3810`.

The definite-pair and indefinite-pair pivot branches have much smaller `L^infinity` bounds from the manuscript and are therefore also below `3810` in squared `L^2` norm.

Thus every normalized branch has

\[
\|p_Q\|_2^2<3810.
\]

For general `K,s`, set `Y=KX` and `Qtilde=(K^2/s)Q` exactly as in the manuscript. Density scaling gives

\[
\|p_Q\|_2={K\over\sqrt s}\|p_{\widetilde Q}\|_2,
\]

which proves the theorem.

## Scope

This is a genuine multiplicity improvement for **existence plus dimension-free `L^2` regularity**, from 17 to 13. It is not a bounded-density theorem at multiplicity 13. The no-pivot order-four envelope remains `1/|t|`, which is in `L^2` but not `L^1`; the unrestricted `L^infinity` threshold remains 17 in the currently completed proof chain.

The exact next `L^infinity` obstruction is the leverage-one endpoint identified in the companion note: if the order-four witness has a dimension-free row-leverage gap, the fractional graph determinant already gives bounded density. The survivor is where a heavy physical row has leverage arbitrarily close to one.
