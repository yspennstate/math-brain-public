SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B14, 2026-09-23T15:13:18Z.
attacking: one-shot affine-extreme localization plus a mass-homogeneity criterion for safe active refinement; apply the completed account02/B14 r37 interval-budget identity to a target-valid family with arbitrary unbounded random translations.

# account01/B14 r39 — affine-extreme localization and random-translation fragment barrier

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T151318Z-account01-B14-QFORM-r39`  
Status: `NEW CONSTANT-PRESERVING LOCALIZATION THEOREM + NEW RANDOM-TRANSLATION TARGET FAMILY / FULL QFORM OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact scope and sources

The target remains the unrestricted statement: independent real coordinates with probability densities at most one, arbitrary symmetric `A` with at least three eigenvalues of modulus at least one, no moments, no centering, no identical-law assumption, no connected-support assumption, and no independence after spectral rotation.


The designated partner result actually used is the completed `account02/B14` r37 report:

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B14/20260923T135912Z-account02-B14-QFORM-r37/REPORT.md`.

Its exact translated-interval identity says that if `V` has density `1_[a,a+1]`, the interval is partitioned into cells of lengths `ell_j`, and the unnormalized cells are pushed by `v -> 2 z v`, then

`m_j=ell_j`, `k_j^*(z)=sup_(t!=0)|t||hat nu_j^z(t)|=1/|z|`,

and the square-root critical budget is

`B_P(z)=|z|^(-1/2) sum_j sqrt(ell_j)`.

For `N` equal cells, `B_N(z)=sqrt(N/|z|)`. For `Z~Unif[1,2]` this yields

`K_eff,N=(12-8sqrt(2))N`,

and the optimized partner pair-certificate diverges as `N -> infinity`, although the probability law itself is unchanged.

## 2. New theorem: affine-extreme localization preserves the exact constant

Let `B` be any fixed real symmetric `k x k` matrix. Define its affine-uniform concentration constant

`C_aff(B) := sup P{x^T B x + ell^T x + c in J}/|J|`,             (2.1)

where the supremum ranges over

- all independent active coordinates `x_i` with probability densities `0<=f_i<=1`,
- all `ell in R^k`, `c in R`, and
- all nondegenerate bounded intervals `J`.

Define `C_ext(B)` by the same supremum but require every marginal to have density `1_E`, where `E` is a bounded finite union of intervals and `|E|=1`. No uniform bound on the number of components, their separation, or their diameter is imposed.

### Theorem 2.1 (`QFORM-AFFINE-EXTREME-LOCALIZATION-v1`)

`boxed: C_aff(B)=C_ext(B).`                                      (2.2)

Thus the optimal affine-uniform small-ball/density constant for an active block is unchanged by one-shot localization to compact finite-fragment extreme marginals.

### Proof

The inequality `C_ext(B)<=C_aff(B)` is immediate. For the reverse inequality, fix admissible product densities `f_1,...,f_k`, affine data `(ell,c)`, an interval `J`, and `epsilon>0`. Put

`E = {x: x^T Bx + ell^T x + c in J}`.

Replace the marginals one at a time. With all coordinates except `x_i` fixed in law, the event probability has the form

`int w_i(s) f_i(s) ds`,                                          (2.3)

for a measurable `0<=w_i<=1`. The cap-one/mass-one bathtub variational principle gives

`sup_{0<=f<=1, int f=1} int w_i f = sup_{|F|=1} int_F w_i`.       (2.4)

No attainment is needed: choose a measurable `F_i` of measure one whose value is within `epsilon/(4k)` of the supremum. Hence replacing `f_i` by `1_(F_i)` decreases the current event probability by at most `epsilon/(4k)`. Iterate through all `k` coordinates. After these replacements we have a product of indicator densities of measurable sets `F_i`, each of measure one, and the event probability has fallen by less than `epsilon/4`.

For every finite-measure measurable `F_i`, regularity of Lebesgue measure gives a bounded finite union of intervals `G_i` with

`|F_i triangle G_i|<delta`.                                      (2.5)

If `|G_i|` is not exactly one, add or remove a finite union of intervals of total measure `||G_i|-1|`; this changes the symmetric difference by at most another `delta`. Thus we may assume `|G_i|=1` and

`||1_(F_i)-1_(G_i)||_1 < 2delta`.                                (2.6)

For product probability densities bounded by one, a telescoping replacement of the coordinates gives total variation change in any event probability at most the sum of the one-dimensional `L^1` changes. Choosing `delta<epsilon/(8k)` therefore changes the event probability by less than `epsilon/4`.

We have produced bounded finite-union extreme marginals with the same affine data and interval `J`, and event probability at least the original probability minus `epsilon/2`. Since the initial law/event were arbitrary and `epsilon` is arbitrary, `C_aff(B)<=C_ext(B)`, proving (2.2). `square`

This theorem is deliberately one-shot. It does **not** say that, after choosing an extreme set `E`, its interval components may be normalized separately before paying an analytic certificate.

## 3. Outside-conditioning compiler: arbitrary shifts/supports cost exactly zero

Let a full symmetric matrix be partitioned in original coordinates as

`A = [[B,C],[C^T,D]]`,                                           (3.1)

with active coordinates `X` and outside coordinates `Y`, all original coordinates mutually independent and cap-one. Then

`Q(X,Y)=X^T B X + 2 X^T C Y + Y^T D Y`.                         (3.2)

Conditioning on the **outside original coordinates** `Y=y` leaves the active product law unchanged and produces only affine data

`ell_y=2Cy`, `c_y=y^T D y`.                                     (3.3)

Therefore, directly from the definition of `C_aff(B)`, for every interval `J`,

`P{Q in J | Y=y} <= C_aff(B)|J|`                                (3.4)

for almost every `y`. Integrating gives

`boxed: P{Q in J} <= C_aff(B)|J|.`                               (3.5)

Hence arbitrary outside quadratic curvature, arbitrary active-outside couplings, arbitrary outside translations/fragments, unbounded outside supports and absence of every moment bound preserve **exactly the same active-block constant**. Combining with Theorem 2.1, all law-level compact/extreme localization may be done before or after this outside conditioning without changing the constant.

This is `QFORM-OUTSIDE-AFFINE-ZERO-TAX-v1`.

## 4. New subprobability hyperbolic `L^p` lemma with exact mass powers

The next lemma identifies the mass homogeneity of a physical-space certificate and will be used at `p=2`.

Let `f,g` be subprobability densities satisfying `0<=f,g<=1`, with masses `m,n`, and let `U,V` be independent with these densities. For arbitrary shifts `a,b`, `c!=0`, and `1<=p<infinity`, the product variable

`H=2c(U-a)(V-b)`

has density obeying

`boxed: ||p_H||_p <= p |c|^(-1+1/p) (mn)^(1/p).`                 (4.1)

Indeed, the product-density formula and Minkowski give

`||p_H||_p <= (2|c|)^(-1+1/p) n^(1/p)
               int f(a+u)|u|^(-1+1/p) du`.                     (4.2)

For `alpha=1-1/p`, the cap-one bathtub estimate at mass `m` is

`int f(a+u)|u|^(-alpha)du
 <= int_(-m/2)^(m/2)|u|^(-alpha)du
 = 2^alpha m^(1-alpha)/(1-alpha)
 = 2^(1-1/p) p m^(1/p)`.                                       (4.3)

The powers of two in (4.2)-(4.3) cancel exactly, yielding (4.1).

At `p=2`, a full probability law gives

`||p_(2c(U-a)(V-b))||_2 <= 2/sqrt(|c|)`.                         (4.4)

For two independent shifted hyperbolic blocks on disjoint original-coordinate pairs, Young/Cauchy-Schwarz therefore gives

`boxed: ||p_(H_1+H_2)||_infinity <= 4/sqrt(|c e|).`              (4.5)

This argument is completely translation uniform and uses no support or moment parameter.

## 5. Target-valid family with arbitrary unbounded random translations

Let `W=(W_1,...,W_m)` have arbitrary independent cap-one coordinates, independent of cap-one `X_1,X_2,Z,V`. Let `a,b,c,d in R^m` and `H=H^T` be arbitrary. Consider

`Q = 2 X_1 X_2 + 2 Z V
     +2(a^T W)X_1 +2(b^T W)X_2
     +2(c^T W)Z   +2(d^T W)V
     +W^T H W`.                                                  (5.1)

The principal block on `(X_1,X_2,Z,V)` is

`[[0,1],[1,0]] direct_sum [[0,1],[1,0]]`,                        (5.2)

with eigenvalues `{1,1,-1,-1}`. By Cauchy interlacing the full ambient matrix has at least two eigenvalues `>=1` and at least two eigenvalues `<=-1`, so (5.1) lies in the owner's exact target for every `m,a,b,c,d,H`.

Condition on `W=w`. Completing each hyperbolic block gives

`2X_1X_2+2(a^T w)X_1+2(b^T w)X_2
 =2(X_1+b^T w)(X_2+a^T w)-2(a^T w)(b^T w)`,                     (5.3)

and

`2ZV+2(c^T w)Z+2(d^T w)V
 =2(Z+d^T w)(V+c^T w)-2(c^T w)(d^T w)`.                         (5.4)

The two completed terms depend on disjoint independent active pairs. Translation preserves the cap-one density condition. Applying (4.4) twice and then `L^2*L^2 -> L^infinity` yields, pointwise in every `w`,

`||p_(Q|W=w)||_infinity <=4`.                                   (5.5)

Averaging over `W` therefore proves the target-level theorem

`boxed: ||p_Q||_infinity <=4.`                                  (5.6)

The constant is independent of `m`, all outside couplings, every translation generated by `W`, the outside quadratic block, fragment geometry, support radius and all moments.

## 6. Completed partner r37 applied at an actual random-translation inequality

Now specialize (5.1) only for the stress test by taking `d=0`,

`Z ~ Uniform[1,2]`, `V ~ Uniform[0,1]`,                          (6.1)

while **keeping `W` arbitrary, unbounded and moment-free**, and keeping arbitrary `c`. Conditional on `W=w`, equation (5.4) becomes

`2 Z (V+c^T w)`.                                                 (6.2)

Thus the active `V` interval has been translated by the random amount `c^T w`, which can be arbitrarily large. Partition that translated interval `[c^T w,c^T w+1]` into `N` equal cells before applying the designated partner r37 critical-Fourier compiler.

Partner r37 is exactly translation invariant: the cell location contributes only a unimodular Fourier phase. Therefore for every fixed `w,z`, each cell has mass `1/N`, exact unnormalized critical coefficient `1/z`, and square-root budget

`B_N(z,w)=sqrt(N/z)`.                                            (6.3)

Averaging over `Z~Unif[1,2]` gives

`b_N(w)=sqrt(N) int_1^2 z^(-1/2)dz
       =2sqrt(N)(sqrt(2)-1)`,                                    (6.4)

hence the exact effective partner parameter is

`boxed: K_eff,N(w)=(12-8sqrt(2))N`,                              (6.5)

**independent of the random translation `c^T w`**.

Partner r37 further proves for its optimized physical-pair envelope `F_(1,1)` that

`F_(1,1)(K_eff,N(w)) -> infinity` as `N -> infinity`.             (6.6)

But our direct target-level estimate (5.5) gives, for the same conditional law and every `w`,

`boxed: ||p_(Q|W=w)||_infinity <=4`,                             (6.7)

and hence the unconditional density is also at most four.

Equations (6.5)-(6.7) are the promised actual application of the completed designated partner result. They strengthen its fixed-translation stress test to **arbitrary random translations generated by an unbounded outside product law**: the true output bound is unchanged, while fragment-first absolute critical budgets still diverge exactly as before.

Thus translations, distant locations and unbounded supports are not the cause of the loss. The loss is the order `split active interval -> normalize cells -> discard inter-cell phase -> pay reciprocal certificate`.

## 7. General mass-homogeneity test for positive localization compilers

Let a positive analytic proof decompose an active subprobability into pieces `nu_j` of masses `m_j`, and suppose after all other parameters are frozen its piece contribution is bounded by

`C m_j^alpha K_j^beta`.                                         (7.1)

If equal refinement into `N` pieces leaves `K_j` bounded below and above by constants independent of `m_j` (as in partner r37, where the exact unnormalized interval coefficient is independent of cell length), then summing positive piece bounds produces the factor

`N (1/N)^alpha = N^(1-alpha)`.                                  (7.2)

Hence arbitrary-refinement zero tax is impossible for such a positive piecewise interface when `alpha<1`. Linear mass homogeneity (`alpha=1`) is the exact safe threshold unless another parameter itself improves with the fragment mass or cancellation is retained before absolute values.

For partner r37 the relevant budget atom is `sqrt(m_j k_j)`. Since `k_j` is exactly constant under active interval subdivision, its mass exponent is `alpha=1/2`; (7.2) gives the exact `sqrt(N)` budget loss proved there.

This is `QFORM-POSITIVE-COMPILER-MASS-TEST-v1`. It does not refute QFORM; it rules out a class of recursive localization proof interfaces.

## 8. Localization rule now justified at the exact constant level

The safe order is:

1. **one-shot law-level localization** by Theorem 2.1, allowing arbitrary finite fragment number/separation;
2. keep every certificate-active extreme marginal whole;
3. pay an affine-uniform whole-active certificate (physical `L^p`, D'/D5 volume, ridge, grouped-bank, Schur-slope, fractional trace, or another mass-linear unnormalized estimate);
4. condition/localize outside original coordinates freely, using (3.5).

Unsafe without an additional mass-homogeneity proof:

`extreme localization -> recursively normalize active interval components -> take positive/absolute certificate pieces -> sum`.

Partner r37 and Section 6 show that this can diverge even after adding arbitrary random translations, while the exact target law remains uniformly bounded.

## 9. Remaining full-QFORM debt

Full QFORM is still OPEN. The localization/support part is not the remaining obstacle in the branches covered here. The first unpaid structural implication is to show that the bare hypothesis `s_3(A)>=1` forces, before active refinement, some whole-active affine-uniform certificate with universal parameters: a good physical pair/grouped pair, a D'/D5 volume exit, a ridge exit, a mixed-hub/grouped-bank exit, or a new mass-linear aggregate mechanism.

No uniformly good single physical minor, universal rank-three cross cut, bounded-diameter reduction, fixed-fragment-count reduction, pointwise quadratic Fourier decay, or post-rotation independence is asserted.

Independent review status: this r39 theorem has not yet received an independent end-to-end review.
