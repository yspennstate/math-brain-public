SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B03, 2026-09-22T22:48:14Z.
attacking: the indefinite near-square physical-pair endpoint; retain the dependence-safe independent-copy collision scale from fleet02/B03 and derive a direct translation-uniform logarithmic one-copy half-Riesz bridge.

# fleet01/B03 r18 — sign-uniform logarithmic half-Riesz bridge for an invertible physical pair

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: `Decoupled time integral`  
Classification: **ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM_PROVED / INTERMEDIATE_MECHANISM_REFUTED / FULL_TARGET_OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.


The unrestricted owner conjecture remains OPEN. Continuity is tracked separately and is not proved by the new branch below.

## 1. Designated partner result actually applied

The designated partner is fleet02/B03. I use its completed r12 report

`yspennstate/math-open-problems@c2bc78fc4f8e642f5d8c85fcc7d53956730b5cb1`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B03/20260922T211507Z-fleet02-B03-QFORM-r12/REPORT.md`.

That report proves the normalized near-square adversary showing that a dependence-safe independent-copy collision estimate cannot in general be promoted to the one-copy half-Riesz endpoint with no logarithmic loss. It also source-pins the completed ambient-pivot collision theorem: if a full quadratic form `R` has a nonzero original-coordinate diagonal coefficient `a`, then, for an independent copy `R'`,

`E |R-R'|^(-1/2) <= C_col |a|^(-1/2)`,                         (1.1)

where

`C_col = 16 sqrt(2) / 3^(3/4) = 9.926451830422...`.

Equivalently, using the exact independent-copy/Riesz identity,

`int_R |t|^(-1/2) |phi_R(t)|^2 dt
 = sqrt(2 pi) E|R-R'|^(-1/2)
 <= sqrt(2 pi) C_col |a|^(-1/2)
 < 24.882 |a|^(-1/2).`                                         (1.2)

This is the dependence-safe time integral applied below. It never conditions `X-X'` on `X+X'`; their dependence is retained inside the exact collision law.

A second completed dependency is the orientation-free rank-two report

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`

`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.

I use only its elementary translated-square kernel lemma. Define

`Psi(u)=1+log(1/|u|)` for `0<|u|<=1`, and `Psi(u)=|u|^(-1/4)` for `|u|>=1`.

Then for every probability density `f<=1`, every `h,u in R`,

`int f(x) |u-(x-h)^2|^(-1/2) dx <= 8 Psi(u).`                   (1.3)

The source also proves the generic rank-two fallback

`sup_t E|Z^T P Z + ell^T Z+c-t|^(-1/2) <=128 |det P|^(-1/4)`    (1.4)

for every invertible physical `2 x 2` symmetric block `P` and independent cap-one physical coordinates.

## 2. Elementary logarithmic averaging lemma

### Lemma 2.1 — `QFORM-QUADRATIC-PSI-AVERAGE-v1`

Let `Y` have probability density at most one. For arbitrary `r,h in R`, any sign `epsilon in {+1,-1}`, and `lambda>0`,

`W = r + epsilon lambda (Y-h)^2`

satisfies

`boxed{
 E Psi(W) <= 3 + 2 log_+(2 sqrt(2)/sqrt(lambda)).
}`                                                                  (2.1)

The estimate is uniform in translations, signs, fragmented supports, and support diameter.

### Proof

First observe the global pointwise estimate

`Psi(w) <= 1 + log_+(1/|w|)`.                                  (2.2)

For `|w|<=1` this is equality; for `|w|>=1`, `Psi(w)=|w|^(-1/4)<=1`.

For every `delta>0`, scaling `x=sqrt(lambda)(y-h)` reduces the sublevel set to

`|x^2-q|<delta`

for some real `q` and with `delta` replaced by `delta` after the obvious normalization. More explicitly,

`Leb{y: |r+epsilon lambda(y-h)^2|<delta}
 <= 2 sqrt(2 delta/lambda).`                                    (2.3)

Indeed, for `q<=-delta` the set is empty; for `-delta<q<delta` its length in `x` is `2sqrt(q+delta)<=2sqrt(2delta)`; and for `q>=delta` its two components have total length

`2[sqrt(q+delta)-sqrt(q-delta)]<=2sqrt(2delta)`,

with the maximum attained at the boundary `q=delta`.

Since the density of `Y` is at most one,

`P(|W|<delta) <= min(1, A sqrt(delta)),`

`A=2sqrt(2)/sqrt(lambda).`                                      (2.4)

Layer cake gives

`E log_+(1/|W|)
 = int_0^infinity P(|W|<e^(-v)) dv
 <= int_0^infinity min(1,A e^(-v/2)) dv
 <= 2+2 log_+ A.`                                               (2.5)

Combine (2.2) and (2.5) to prove (2.1). QED.

## 3. Main theorem: every non-pure-saddle invertible physical pair has only logarithmic endpoint loss

### Theorem 3.1 — `QFORM-PHYSICAL-PAIR-LOG-HALF-RIESZ-v1`

Let `X,Y` be independent real random variables with probability densities bounded by one. Let

`P=[[a,b],[b,c]]`

be any invertible real symmetric matrix. Put

`D=|det P|=|ac-b^2|>0`,
`m=max{|a|,|c|}`.

Assume `m>0` (equivalently, the pair is not the exact zero-diagonal pure saddle). For arbitrary affine coefficients `ell_1,ell_2,r_0`, define

`R=aX^2+2bXY+cY^2+ell_1 X+ell_2 Y+r_0`.

Then

`boxed{
 H_(1/2)(R):=sup_t E|R-t|^(-1/2)
 <= 8 m^(-1/2)
    [3+2 log_+(2 sqrt(2) m/sqrt(D))].
}`                                                                  (3.1)

The result is sign-uniform: it covers definite and indefinite `P` with the same formula. Together with the generic rank-two estimate (1.4), one may always use

`H_(1/2)(R)
 <= min{128 D^(-1/4),
        8 m^(-1/2)[3+2log_+(2sqrt(2)m/sqrt(D))]}`               (3.2)

when `m>0`; if `m=0`, (1.4) remains available.

### Proof

Relabel `X,Y` if necessary so `m=|a|>0`. Complete the square in the ORIGINAL coordinate `X`:

`R = a (X+h(Y))^2 + delta (Y-y_0)^2 + c_0`,                    (3.3)

where the shifts `h(Y),y_0,c_0` absorb all affine terms and

`delta = c-b^2/a = det(P)/a`.                                  (3.4)

Fix `t`. Conditional on `Y`, factor the physical scale `|a|`:

`E[|R-t|^(-1/2) | Y]
 = m^(-1/2)
   E_X |u(Y)-(X+h(Y))^2|^(-1/2),`                               (3.5)

where, depending on the sign of `a`,

`u(Y)=r + epsilon lambda (Y-y_0)^2`,
`lambda=|delta/a|=D/m^2`,                                      (3.6)

for some `r in R` and `epsilon in {+1,-1}`. Translation of `X` preserves its density cap. Apply the source kernel (1.3) conditionally and then Lemma 2.1:

`E|R-t|^(-1/2)
 <=8m^(-1/2) E Psi(u(Y))
 <=8m^(-1/2)[3+2log_+(2sqrt(2)/sqrt(lambda))].`                 (3.7)

Substitute `sqrt(lambda)=sqrt(D)/m`. The bound is independent of `t`, proving (3.1). QED.

### Interpretation

In the near-square regime `D<<m^2`, the generic orientation-free payment `D^(-1/4)` is replaced by only

`m^(-1/2) log(m/sqrt(D)).`

The previous B03 r17 theorem established the analogous logarithmic conclusion under definiteness by combining a square-root and a finite ellipsoid-shell small-ball estimate. The present proof needs no finite shell volume and therefore pays the **indefinite** near-square endpoint as well.

## 4. Direct application of the named fleet02/B03 collision theorem

The same physical pair `R` has an original-coordinate diagonal coefficient of magnitude `m`. Therefore fleet02/B03's completed collision theorem (1.1) applies directly:

`boxed{
 E|R-R'|^(-1/2) <= C_col m^(-1/2),
}`                                                                  (4.1)

and hence

`boxed{
 int_R |t|^(-1/2)|phi_R(t)|^2dt
 <24.882 m^(-1/2).
}`                                                                  (4.2)

Comparing (3.1) with (4.1)-(4.2) gives a precise dependence-safe statement: the independent-copy weighted time integral already lives at the dominant physical-square scale `m^(-1/2)`, while the one-copy critical endpoint can require an additional logarithm of the pair condition parameter `m/sqrt(D)`.

No inequality of the form `H_(1/2)(R)<=C E|R-R'|^(-1/2)` is asserted; the partner's counterexample rules out such a universal promotion. The new theorem supplies the missing structural parameter and an explicit endpoint bridge instead.

## 5. New sign-indefinite obstruction: the logarithm is necessary here too

The partner's exact r12 adversary is positive definite. The same logarithmic collision-to-endpoint gap also occurs for an **indefinite** physical pair, so the logarithm in Theorem 3.1 cannot in general be removed merely by exploiting sign indefiniteness.

Let `0<eta<=1/256` and let `X,Y` be iid `Uniform[-1/2,1/2]`. Define

`R_eta^- = [(X+Y)^2 - eta (X-Y)^2]/(2eta).`                     (5.1)

Its physical coefficient matrix is

`P_eta^-=(1/(2eta))[[1-eta,1+eta],[1+eta,1-eta]].`             (5.2)

Its eigenvalues are `1/eta` and `-1`; hence it is indefinite. Moreover

`m_eta=(1-eta)/(2eta)`,
`D_eta=|det P_eta^-|=1/eta`,
`m_eta/sqrt(D_eta)=(1-eta)/(2sqrt(eta))->infinity.`             (5.3)

Put `u=X+Y`, `v=X-Y`. The transformed law has density `1/2` on the diamond `|u|+|v|<=1`, and

`|R_eta^-|^(-1/2)=sqrt(2eta)|u^2-eta v^2|^(-1/2).`             (5.4)

Restrict the integral to

`0<=v<=1/4`, `2sqrt(eta)<=u<=1/4`.                              (5.5)

For `eta<=1/256` this rectangle lies inside the diamond. On it `u^2-eta v^2>0` and

`sqrt(u^2-eta v^2)<=u`.

Therefore

`H_eta^-(0):=E|R_eta^-|^(-1/2)
 >= [sqrt(2eta)/8] log(1/(8sqrt(eta))).`                         (5.6)

Multiplying by `sqrt(m_eta)` gives

`boxed{
 H_eta^-(0) sqrt(m_eta)
 >= [sqrt(1-eta)/8] log(1/(8sqrt(eta))) -> infinity.
}`                                                                  (5.7)

Thus the candidate mechanism

`H_(1/2)(R) <= C m^(-1/2)`                                      (5.8)

is false even for an indefinite invertible pair with iid compactly supported cap-one inputs. This is a counterexample only to the intermediate no-log endpoint mechanism, **not** to the full QFORM conjecture.

At the same time, fleet02/B03's collision theorem still gives

`E|R_eta^- - (R_eta^-)'|^(-1/2)
 <= C_col m_eta^(-1/2).`                                       (5.9)

Hence the logarithmic separation between dependence-safe collision scale and one-copy endpoint is present in both signatures.

## 6. Ambient linear-small-ball consequence after one genuine physical square

Condition on arbitrary outside ORIGINAL coordinates. Suppose a genuine original-coordinate square completion gives

`Q = d (Z+h(X,Y,w))^2 + R_w(X,Y)`, `d!=0`,                    (6.1)

where the quadratic coefficient matrix of `R_w` in the still-independent original pair `(X,Y)` is the fixed invertible `P` above. Outside conditioning changes only affine terms in `R_w`, so `D,m` are independent of `w` and Theorem 3.1 is uniform in those affine shifts.

The translated-square density envelope gives

`||p_(Q|w)||_infinity
 <= |d|^(-1/2) H_(1/2)(R_w).`                                  (6.2)

Averaging the conditional laws yields the linear small-ball/density estimate

`boxed{
 ||p_Q||_infinity
 <= 8 |d|^(-1/2)m^(-1/2)
       [3+2log_+(2sqrt(2)m/sqrt(D))].
}`                                                                  (6.3)

This proves absolute continuity and essential boundedness in the stated branch. It does **not** prove continuity.

If `P` is exactly the two-coordinate Schur residual of a physical principal triple `T` after pivoting the coefficient `d`, then

`D=|det T|/|d|`,                                                (6.4)

so (6.3) becomes

`||p_Q||_infinity
 <=8(|d|m)^(-1/2)
   [3+2log_+(2sqrt(2)m sqrt(|d|)/sqrt(|det T|))].`              (6.5)

This is a product-preserving local certificate; it is not an assertion that the bare spectral hypothesis forces a favorable physical triple.

## 7. Relation to current corrections and the remaining proof debt

The proof survives the current correction set for a simple reason: every conditioning step is on other ORIGINAL coordinates. The two active input variables remain genuinely independent with their original cap-one densities. The only rotation-like algebra is completion of a scalar physical square; no spectral coordinates are declared independent. The sublevel estimate in Lemma 2.1 is a physical-space integrated estimate, not forbidden law-uniform pointwise oscillatory decay.

Theorem 3.1 closes the **analytic** indefinite near-square pair endpoint left by B03 r17. It does not close the full conjecture. The remaining first-order debt is structural/aggregate: starting from only `s_3(A)>=1`, force a dimension-free product-preserving certificate before reciprocal local selection. Current frontier reports show genuine diffuse O0/two-anchor and heavy-null/two-bank packets where no single physical pair or triple need carry a universal determinant floor.

A useful successor for B03 is therefore an **aggregate logarithmic-pair compiler**: average the pair-level logarithmic singularities against determinant/exterior weights before paying `m^-1/2` or a local determinant reciprocal. That would address many-small-pair/heavy-star states without selecting one vanishing atom. This successor remains on the same QFORM target and is not claimed proved here.

## 8. Status

- `QFORM-QUADRATIC-PSI-AVERAGE-v1`: **PROVED**.
- `QFORM-PHYSICAL-PAIR-LOG-HALF-RIESZ-v1`: **PROVED**, both signatures, arbitrary affine shifts.
- fleet02/B03 dependence-safe collision/time integral: **APPLIED TO THE SAME PAIR** in (4.1)-(4.2).
- no-log physical-pair endpoint `H<=C m^(-1/2)`: **REFUTED**, including the indefinite signature, by (5.1)-(5.7).
- outer physical square + invertible Schur pair linear-small-ball branch: **PROVED ESSENTIALLY BOUNDED**.
- continuity in this branch: **NOT PROVED**.
- full QFORM universal theorem: **OPEN / NOT PROVED / NOT DISPROVED**.
