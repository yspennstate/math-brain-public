SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B15, 2026-09-23T18:05:22Z.
attacking: local-in-matrix uniform regularity and a sheetwise-continuity obstruction, with an actual use of the completed fleet02/B15 ruled-majority theorem.

# fleet01/B15 — local matrix uniformity and sheetwise continuity obstruction

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T180522Z-fleet01-B15-QFORM-auto11`  
Execution context: `WITHOUT_VERIFIED_BRAIN`  
Status: `NEW TARGET-LEVEL REGULARITY LEMMA / NEW RULED-SHEET CONTINUITY OBSTRUCTION / FULL QFORM OPEN`.

## 1. Sources and exact scope


The full target remains open: for independent real coordinates with one-dimensional probability densities bounded by one and symmetric `A` with `s_3(A)>=1`, prove one matrix-, dimension-, and law-independent bound for the density of `Q=X^TAX`.

Corrections retained throughout: no law-uniform pointwise quadratic Fourier decay, no independence after rotation, no arbitrary-joint coarea cap, no projection/X-ray-only replacement for the product-sensitive two-sheet term, and no uniformly good single physical minor.

Completed designated-partner result actually used below:

`fleet02/B15`, `yspennstate/math-open-problems@3aeee281da396345dd8e95eeb9802e3c3b73eea8`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B15/20260923T170821Z-fleet02-B15-qform-auto11/REPORT.md`.

In particular, for an invertible indefinite original-coordinate triple `S`, its rough-input majority/one-sheet output submeasure satisfies interval domination with exact ruled constant `C_S`; for signature `(2,1)` with eigenvalue magnitudes `lambda_1,lambda_2,mu`,

`C_S = integral_0^(2pi) [lambda_2 mu sin^2(theta)+lambda_1 mu cos^2(theta)+lambda_1 lambda_2]^(-1/2) dtheta`.

The same partner report also source-pins the fixed-matrix theorem: every rank-at-least-three target with cap-one product inputs has an individually bounded `C_0(R)` density. This qualitative continuity theorem is not a universal-height theorem.

I also use the completed finite-block theorem from
`yspennstate/math-open-problems@47dc925729bbf269333cc6e1256178a538d2f553`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B15/20260922T120320Z-fleet01-B15-qform/REPORT.md`:

- every rank-at-least-three symmetric matrix has an invertible original-coordinate principal block of order `3` or `4`;
- an invertible affine `3 x 3` block has density height at most `(2*pi+3*sqrt(3))/sigma_min(B)`;
- an invertible affine `4 x 4` block has density height at most `(4*pi+8)/sigma_min(B)`;
- conditioning on all outside original coordinates preserves these bounds for the ambient form.

No rotated-coordinate independence is used in any step below.

## 2. New target-level lemma: the worst-law height is locally bounded in the matrix

For fixed dimension `n`, define on the rank-at-least-three locus

`H_n(A) = sup ||p_(X^T A X)||_infinity`,

where the supremum ranges over all independent one-dimensional probability densities bounded by one.

### Theorem 2.1 — local matrix uniformity

Let `A` be any real symmetric `n x n` matrix with `rank(A)>=3`. Then there exist an open operator-norm neighborhood `U_A` of `A` and a finite constant `M_A` such that

`sup_(B in U_A) H_n(B) <= M_A < infinity`.

More quantitatively, choose an original-coordinate principal block `A_(I,I)` of order `d in {3,4}` which is invertible, and put

`kappa = sigma_min(A_(I,I)) > 0`, `C_4=4*pi+8`.

Then every symmetric `B` satisfying

`||B-A||_op < kappa/2`

obeys

`boxed( H_n(B) <= 2 C_4 / kappa = (8*pi+16)/kappa. )`  (2.1)

### Proof

Restriction to a principal coordinate block cannot increase operator norm, hence

`||B_(I,I)-A_(I,I)||_op <= ||B-A||_op < kappa/2`.

Weyl's singular-value perturbation inequality gives

`sigma_min(B_(I,I)) >= kappa - ||B_(I,I)-A_(I,I)||_op > kappa/2`.

Condition on every original coordinate outside `I`. The conditional polynomial in `X_I` is

`X_I^T B_(I,I) X_I + 2 b^T X_I + c`,

where `b,c` depend on the frozen outside coordinates. The active coordinates remain independent and each active density is still bounded by one. If `d=3`, apply the completed three-variable affine theorem; if `d=4`, apply the completed four-variable affine theorem. Since the three-variable constant is smaller than `C_4`, every conditional output measure has density height at most

`C_4 / sigma_min(B_(I,I)) <= 2 C_4/kappa`.

Averaging the conditional measures preserves domination by the same multiple of Lebesgue measure. This proves (2.1). `QED`.

### Corollary 2.2 — compact matrix families are uniformly paid

If `K` is any compact subset of the rank-at-least-three locus of `Sym_n`, then

`boxed( sup_(A in K) H_n(A) < infinity. )`  (2.2)

Indeed, the neighborhoods from Theorem 2.1 form an open cover of `K`; a finite subcover gives the maximum of finitely many local constants.

### Corollary 2.3 — bounded spectral aspect ratio is harmless in fixed dimension

For fixed `n` and `L<infinity`, there is a finite `C_(n,L)` such that every symmetric `A` with `s_3(A)>0` and

`||A||_op <= L s_3(A)`

satisfies, uniformly over all cap-one product laws,

`boxed( ||p_(X^T A X)||_infinity <= C_(n,L)/s_3(A). )`  (2.3)

Proof: scale by `s=s_3(A)` and put `A_tilde=A/s`. Then `s_3(A_tilde)=1` and `||A_tilde||_op<=L`. The set

`K_(n,L)={B in Sym_n: s_3(B)=1, ||B||_op<=L}`

is compact and lies in the rank-at-least-three locus, so (2.2) gives a finite height bound on it. Finally `X^TAX=s X^T A_tilde X`, and one-dimensional density scaling contributes the factor `1/s`.

Consequently any sequence for which

`s_3(A_m) ||p_m||_infinity -> infinity`

must, after passing to a subsequence, have either dimensions `n_m -> infinity` or spectral aspect ratios

`||A_m||_op/s_3(A_m) -> infinity`.

This does not solve QFORM: the missing theorem is precisely a bound uniform through both noncompact directions. But it removes a regularity ambiguity: no blow-up can occur by varying the rough input laws and matrices inside a compact rank-three-or-higher matrix family.

## 3. Absolute continuity and continuity: exact logical ledger

### 3.1 Absolute continuity

If `A!=0` and the full joint input law is absolutely continuous, then `X^TAX` is absolutely continuous. Product structure, the cap one, and rank three are unnecessary. This follows by applying coarea on sets where `|2Ax|` is bounded away from zero; the critical set `ker A` is a null proper subspace.

Thus under the owner hypotheses, existence of some density is strictly easier than the universal height problem.

### 3.2 Instancewise continuity

The completed fleet02/B15 fixed-matrix theorem gives, for every rank-at-least-three `A` and every cap-one product law,

`p_Q in C_0(R) cap L^infinity(R)`

with a matrix-dependent height constant. Since every owner target has rank at least three, qualitative continuity is already an instancewise theorem.

### 3.3 Same-constant closure once the universal essential bound is proved

Suppose the central theorem is eventually proved with

`||p_Q||_(L^infinity,ess) <= C/s_3(A)`.

Take the `C_0` representative supplied by the fixed-matrix theorem. If at some point `t_0` this continuous representative exceeded `C/s_3(A)`, continuity would make it exceed the same number on an interval of positive measure, contradicting the essential bound. Therefore

`boxed( sup_t p_Q(t) <= C/s_3(A). )`  (3.1)

So the stronger continuous-density conclusion costs **no additional universal constant** once the central essential-height theorem is paid. No target-uniform continuity modulus is needed for this implication, and the designated partner's high-frequency core construction shows that no such common modulus should be expected.

## 4. New obstruction: the ruled majority component need not have a continuous density

The completed partner theorem is a height theorem for a one-sheet submeasure. It must not be silently upgraded to componentwise continuity. The failure already occurs in the simplest exact target.

Let

`A=diag(1,1,-1)`,

and let `X_1,X_2,X_3` be iid `Uniform[-1/2,1/2]`. Their densities are exactly one, and `s_3(A)=1`. Put

`Q=X_1^2+X_2^2-X_3^2`.

Let `V=X_3^2`. Its density is

`g(v)=v^(-1/2) 1_(0,1/4)(v)`.

Let `U=X_1^2+X_2^2`. For `0<u<1/4`, both square summands automatically lie in `(0,1/4)`, so

`p_U(u)=integral_0^u [r(u-r)]^(-1/2) dr = pi`.

Since `U` and `V` are independent, the continuous full output density satisfies

`p_Q(0)=integral_0^(1/4) p_U(v) g(v) dv`

`       = pi integral_0^(1/4) v^(-1/2) dv`

`       = pi`.  (4.1)

Continuity at zero can also be seen directly from `p_Q=p_U * p_(-V)`: the two-square density `p_U` is bounded, `p_(-V)` is in `L^1`, and translations are continuous in `L^1`.

Now form the deterministic majority/one-sheet submeasure

`mu_+(E)=P(Q in E, Q>=0)`.

Its Radon-Nikodym density is, almost everywhere,

`p_+(t)=p_Q(t) 1_[0,infinity)(t)`.

This submeasure has **no continuous density representative**. Indeed, any continuous representative equal to zero almost everywhere on `(-infinity,0)` must equal zero on that whole open half-line and hence at zero. On `(0,infinity)` it equals the continuous function `p_Q` almost everywhere, hence everywhere, forcing its right-hand limit at zero to be `p_Q(0)=pi`, a contradiction.

Thus

`boxed( full output p_Q is continuous, but the raw majority one-sheet subdensity is not. )`  (4.2)

This is exactly why continuity cannot be inferred component-by-component from the partner's ruled domination.

## 5. Actual application of the completed fleet02/B15 ruled theorem

For `B=diag(1,1,-1)`, the partner's exact ruled constant has `lambda_1=lambda_2=mu=1`, so

`C_B = integral_0^(2pi) dtheta/sqrt(sin^2(theta)+cos^2(theta)+1)`

`    = 2pi/sqrt(2) = sqrt(2) pi`.

The completed rough one-sheet theorem therefore gives, for every interval `I`,

`P(Q in I, Q>=0) <= sqrt(2) pi |I|`.  (5.1)

For intervals `I subset (0,infinity)`, the majority condition is redundant. Dividing by interval length and shrinking to zero, using the continuous representative of the full density, yields the concrete pointwise inequality

`boxed( p_Q(0)=pi <= sqrt(2) pi. )`  (5.2)

The inequality is deliberately not sharp in this example. Its value here is logical: (5.1) is a valid raw rough-input height estimate for the one-sheet component, while (4.2) proves that this same component can fail continuity. Height and continuity are genuinely different outputs of the analysis.

## 6. What is now paid and what remains open

The regularity hierarchy is now precise:

1. `A!=0` plus an absolutely continuous joint input law implies absolute continuity of `X^TAX`.
2. `rank(A)>=3` plus the cap-one product structure implies an individually bounded `C_0` density.
3. On every compact rank-at-least-three matrix family in fixed dimension, the height is uniformly bounded over **all** cap-one product laws.
4. If the universal essential-height theorem is proved, the existing fixed-instance `C_0` theorem upgrades it to a universal pointwise bound with the **same constant**.
5. The ruled majority submeasure need not itself have a continuous representative; continuity is recovered only after the full quadratic output is reassembled.

The first unpaid implication for the full owner target is still global: control sequences in which dimension and/or spectral aspect ratio escape and every cost-efficient physical block degenerates, while retaining original-coordinate product provenance through the minority/two-sheet or grouped/ridge receiver. The new local compactness theorem shows that this is a genuine noncompact matrix-geometry problem, not an unresolved fixed-matrix regularity problem.

Full unrestricted QFORM status: `OPEN_NOT_PROVED`.
