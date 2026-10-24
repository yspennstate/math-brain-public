SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B15, 2026-09-24T00:04:13Z.
attacking: a general C0 regularity compiler from Lp residual control, and a source-valid application to the latest account02/B15 collective Schur and grouped-obstruction results without using continuity to pay height.

# account01/B15 — an L^p square-kernel C0 compiler and a fully coupled physical-triple receiver

Programme: `QFORM-DENSITY-3EIG-20260922`, activation revision `2026-09-22.5`.
Fresh owner control observed on `yspennstate/math-research-brain` main; OWNER CONTROL remains revision `2026-09-22.15`, QFORM-only, with no later stop seen before publication.
Execution: `WITHOUT_VERIFIED_BRAIN`.
Full unrestricted QFORM status: `OPEN_NOT_PROVED`.

## 1. Sources and exact scope

The newest designated partner report actually used is `account02/B15`:

`yspennstate/math-open-problems@81b639f85e91328176f0dcdd52b5f3c95ce71ab9`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260923T230534Z-account02-B15-qform-auto11/REPORT.md`.

Its completed collective rank-one Schur theorem is used below at an actual output inequality. I also use the completed physical-pair logarithmic envelope

`yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`,
`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`,

and the source-pinned fixed-matrix rough-input regularity theorem

`yspennstate/math-open-problems@9b8bb7e84811978a2c46c7bb5ec50f2570dbc056`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260922T200544Z-account02-B15-qform-r11/REPORT.md`.

The latter says that for every fixed symmetric `A` with `rank(A)>=3`, arbitrary independent cap-one inputs give an instance-dependent bounded density with a representative in `C_0(R)`. Its constants may deteriorate with the physical matrix; it does **not** solve the universal-height theorem.

No law-uniform pointwise quadratic Fourier decay, no independence after spectral rotation, no arbitrary-joint coarea cap, and no projection/X-ray-only shortcut is used below.

## 2. Regularity ledger

The logical implications are now kept strictly separate.

* **Absolute continuity:** if the joint input law is absolutely continuous and `A!=0`, then `X^TAX` is absolutely continuous. This needs neither the cap, independence, nor rank three. It follows from coarea away from `ker A` (or by original-coordinate conditioning).
* **Universal bounded density:** the central QFORM problem is the still-open estimate `||p_Q||_infinity<=C/s_3(A)` with one matrix-, law-, and dimension-independent `C`.
* **Continuous density:** for the target class, the source-pinned fixed-matrix theorem already gives an instance-dependent `C_0` representative. Therefore any subsequently proved essential height certificate transfers to that continuous representative with **the identical constant**. Continuity is not used to manufacture the height.

The new lemmas below make that separation quantitative in a coupled pivot geometry.

## 3. New target-level regularity compiler: an L^p residual envelope, p>2

### Theorem 3.1 — `QFORM-B15-LP-SQUARE-C0-COMPILER-v1`

Let `(R,V)` have a joint probability density `K(r,v)`. Assume that for almost every `r`,

`K(r,.) in C_0(R)`,

and that for some probability density `g in L^p(R)`, `p>2`,

`0 <= K(r,v) <= g(r)`                                                     (3.1)

for almost every `(r,v)`. Let `b!=0` and

`T=R+bV^2`.

Then `T` has a density in `C_0(R)` and

`boxed( ||p_T||_infinity <= C_p |b|^(-1/2) ||g||_p^[p/(2(p-1))] )`        (3.2)

with

`C_p = 2 sqrt( 2(p-1)/(p-2) ).`                                           (3.3)

At `p=3`,

`boxed( ||p_T||_infinity <=4 |b|^(-1/2)||g||_3^(3/4). )`                  (3.4)

### Proof

Put `a=|b|` and `sigma=sign(b)`. One-dimensional change of variables in `V` gives the exact density formula

`p_T(t)=1/(2sqrt(a)) int_{sigma(t-r)>0}`
` [K(r,+sqrt(|t-r|/a))+K(r,-sqrt(|t-r|/a))]/sqrt(|t-r|) dr.`              (3.5)

Using (3.1),

`p_T(t) <= a^(-1/2) int_0^infinity g(t-sigma s)s^(-1/2)ds.`               (3.6)

Let `p'=p/(p-1)` and

`alpha=1/2-1/p=(p-2)/(2p)>0`,
`A_p=[2(p-1)/(p-2)]^((p-1)/p).`

For any `L>0`, Holder on `(0,L)` gives

`int_0^L g(t-sigma s)s^(-1/2)ds <= A_p ||g||_p L^alpha`,                  (3.7)

because `p'/2<1`. Probability normalization gives

`int_L^infinity g(t-sigma s)s^(-1/2)ds <= L^(-1/2).`                      (3.8)

Take

`L=(A_p||g||_p)^(-p/(p-1)).`                                              (3.9)

The two terms in (3.7)--(3.8) then coincide, and their sum is

`2(A_p||g||_p)^[p/(2(p-1))]`
` = C_p ||g||_p^[p/(2(p-1))].`

This proves (3.2).

For continuity, fix `delta>0` in (3.5) and split at `|t-r|=delta`. On the far set, for almost every fixed `r`, the section `K(r,.)` is continuous and the square-root argument changes continuously with `t`; the integrand is dominated by a constant times `g(r)`, so dominated convergence applies. The two near-endpoint pieces are uniformly bounded by the right side of (3.7) with `L=O(delta)`, hence are `O(delta^alpha)`. First let `t_n->t` at fixed `delta`, then `delta->0`.

For vanishing at infinity, split (3.6) at a fixed `L`. The far term is at most `L^(-1/2)`. The near term is bounded by `A_p L^alpha` times the `L^p` norm of `g` on a translating interval of length `L`; this tends to zero as `|t|->infinity` because `g^p in L^1`. Then let `L->infinity`. Therefore `p_T in C_0(R)`. QED.

### The threshold `p>2` is real for this compiler

There is no analogous conclusion from only `g in L^2`. Let, near zero on the negative half-line,

`g(r)=c/[sqrt(-r) log(1/(-r))]`, `-e^(-2)<r<0`,                            (3.10)

with `c>0` small, and add a bounded density away from zero to make total mass one. Then `g in L^1 cap L^2`, since

`int_0^(e^-2) du/[u log^2(1/u)]<infinity`.

Let `V` be independent with the triangular `C_0` probability density `h(v)=(1-|v|)_+` on `[-1,1]`. For `T=R+V^2`,

`p_T(-tau)=int h(v)g(-tau-v^2)dv`.

As `tau downarrow0`, its contribution from small positive `v` grows like

`int dv/[sqrt(tau+v^2) log(1/(tau+v^2))]`,

which diverges. Hence the output density is unbounded. Thus `p>2` is the genuine endpoint for this abstract residual-envelope mechanism; an `L^2` residual certificate alone cannot be promoted to `L^infinity` by the square kernel.

## 4. New consequence of the completed physical-pair logarithmic envelope

Let `U_1,U_2` be independent cap-one variables and let

`F=U^T S U+2ell.U+c`,

where `S` is an invertible indefinite ORIGINAL-coordinate `2x2` matrix. Put

`D=|det S|`, `kappa=sigma_min(S)`.

The completed pair theorem gives, for every cutoff `rho>0`, a decomposition into a far subdensity with sup at most `2sqrt(2)/rho` and a near subdensity bounded by

`D^(-1/2) log_+(2rho^2/(kappa|t-t0|)).`                                   (4.1)

This immediately yields a whole `L^p` ladder.

### Lemma 4.1 — `QFORM-B15-INDEFINITE-PAIR-LP-v1`

For every `p>1`,

`||p_F||_p <= A rho^(-(p-1)/p)+B_p rho^(2/p),`                            (4.2)

where

`A=(2sqrt(2))^((p-1)/p)`,
`B_p=D^(-1/2)[4 Gamma(p+1)/kappa]^(1/p).`                                 (4.3)

Optimizing gives

`rho_*=[(p-1)A/(2B_p)]^[p/(p+1)]`                                         (4.4)

and

`boxed( ||p_F||_p <= M_p(D,kappa) )`,                                     (4.5)

`M_p(D,kappa)=(p+1)/2 * A^[2/(p+1)] * [2B_p/(p-1)]^[(p-1)/(p+1)].`        (4.6)

In particular,

`boxed( ||p_F||_3 <=4*3^(1/6) D^(-1/4) kappa^(-1/6). )`                  (4.7)

### Proof

The far subdensity has mass at most one, hence its `L^p` norm is at most `(2sqrt(2)/rho)^(1-1/p)`. For the near part, with `C=2rho^2/kappa`,

`int_R log_+(C/|u|)^p du = 2C Gamma(p+1)=4rho^2 Gamma(p+1)/kappa.`          (4.8)

Taking the `p`th root proves (4.2). Elementary one-variable minimization gives (4.4)--(4.6), and substituting `p=3`, `Gamma(4)=6`, gives (4.7). QED.

This result is useful precisely because it retains the logarithmic rank-two singularity instead of pretending that an indefinite pair has an `L^infinity` density.

## 5. A new fully coupled physical-triple receiver

### Theorem 5.1 — `QFORM-B15-COUPLED-PIVOT-INDEFINITE-SCHUR-C0-v1`

Let `Y=(U_1,U_2,Z)` have independent probability densities bounded by one. Let

`B=[[C,a],[a^T,b]]`                                                       (5.1)

be an invertible symmetric `3x3` matrix, where `b!=0`. Put

`S=C-aa^T/b`, `D=|det S|`, `kappa=sigma_min(S)`.

Assume

1. `S` is indefinite (hence invertible), and
2. `a!=0`.

Then every affine quadratic

`Y^T B Y+2ell^T Y+c`

has a density in `C_0(R)`, and

`boxed( ||p||_infinity <= 8sqrt(2) 3^(1/8)`
`        * |b|^(-1/2) D^(-3/16) kappa^(-1/8). )`                         (5.2)

The constant is uniform over all affine terms and all cap-one input laws.

### Proof

Translate the three ORIGINAL coordinates by `B^(-1)ell`; this preserves independence and the cap. Up to an output translation,

`Y^TBY = R(U)+b(Z+M(U))^2`,                                               (5.3)

where

`R(U)=U^T S U`, `M(U)=(a/b)^T U`.                                        (5.4)

Because `a!=0`, the map

`Psi(U)=(R(U),M(U))`

has differential with rows `2SU` and `a/b`. Its rank drops only when `SU` is parallel to `a/b`, a one-dimensional line. This is a Lebesgue-null subset of `R^2`, so coarea on compact sets away from that line shows that `(R,M)` has a joint density `H(r,m)`.

Let `f_Z` be the independent pivot density. The pair `(R,V)` with `V=Z+M` has joint density

`K(r,v)=int H(r,m)f_Z(v-m)dm.`                                           (5.5)

For almost every `r`, `K(r,.)` is a convolution of two `L^1` functions and hence belongs to `C_0`. Also, because `f_Z<=1`,

`0<=K(r,v)<=int H(r,m)dm=p_R(r).`                                        (5.6)

By Lemma 4.1,

`||p_R||_3 <=4*3^(1/6) D^(-1/4)kappa^(-1/6).`                            (5.7)

Apply Theorem 3.1 at `p=3` with `g=p_R`. Then

`||p||_infinity <=4|b|^(-1/2)||p_R||_3^(3/4)`,

which is exactly (5.2), and Theorem 3.1 simultaneously yields `p in C_0`. QED.

### Ambient version

If an ambient symmetric matrix `A` contains such an ORIGINAL-coordinate principal triple `B`, condition on every coordinate outside that triple. Only affine and constant terms change. The conditional bound (5.2) is independent of those terms and the conditional densities are `C_0`; the dominated conditional-`C_0` compiler therefore gives the same bound and `C_0` conclusion for the full ambient quadratic form.

This is a product-preserving receiver. It never diagonalizes the input law.

## 6. A physical-triple dichotomy and the designated partner theorem

The newest `account02/B15` theorem pays the complementary geometry. Let `B` be an invertible indefinite physical `3x3` block.

### Case A: an indefinite physical principal pair exists

Let that pair be `D_2`, with

`Delta=|det D_2|`, `kappa_2=sigma_min(D_2)`.

Its scalar Schur complement in the `3x3` block is a nonzero number `sigma`. The completed partner theorem `QFORM-B15-COLLECTIVE-RANK1-SCHUR-REPAIR-v1` gives, uniformly over every cap-one product law and every affine term generated by outside conditioning,

`boxed( ||p||_infinity <=8sqrt(2)(Delta*kappa_2*|sigma|)^(-1/4). )`       (6.1)

The scalar affine remainder automatically lies in the range of the nonzero scalar Schur complement. This is an **actual application** of the completed designated-partner result.

The source-pinned fixed-matrix rank-at-least-three theorem independently supplies a `C_0` representative. Therefore the essential bound (6.1) holds pointwise for that representative with **no loss of constant**. Continuity is an after-the-height upgrade, not a premise of (6.1).

### Case B: no physical principal pair is indefinite

Then every nonzero diagonal entry of `B` has the same sign: two opposite-sign diagonals would themselves form an indefinite principal pair. There is at least one nonzero diagonal, because an invertible all-zero-diagonal matrix has a nonzero off-diagonal entry and hence an indefinite zero-diagonal pair.

Multiply `B` by `-1` if necessary and choose a positive diagonal pivot `b>0`. Write it as in (5.1). If `det B>0`, then `det S=det B/b>0`; moreover the assumption that neither principal pair through the pivot is indefinite implies the two diagonal entries of `S` are nonnegative. Thus `S` would be positive definite, and Sylvester inertia additivity would make `B` positive definite, contradiction. Hence `det B<0`, so

`det S=det B/b<0`;                                                       (6.2)

therefore `S` is indefinite. Also `a!=0`, because `a=0` would make `S=C` itself an indefinite physical principal pair. Thus Theorem 5.1 applies.

Consequently **every invertible indefinite original-coordinate physical triple has an explicit `C_0` receiver**: either the partner collective rank-one Schur bound (6.1), or the new coupled-pivot bound (5.2). This is a local theorem, not a universal structural reduction; the constants can still deteriorate on delocalized matrices.

## 7. A genuine exact-target example in the new branch

Consider

`B_* = [[5/4,-9/8,-9/8],`
`       [-9/8,5/4,-9/8],`
`       [-9/8,-9/8,5/4]].`                                               (7.1)

Its eigenvalues are

`19/8, 19/8, -1`,                                                         (7.2)

so it is itself an exact three-dimensional owner-target matrix. Every physical `2x2` principal pair has eigenvalues `19/8` and `1/8`, so **no** physical pair is indefinite; partner Case A cannot be selected.

Use the third coordinate as pivot. Then

`b=5/4`,

and the Schur complement has eigenvalues

`19/8, -19/10`.                                                          (7.3)

Hence

`D=361/80`, `kappa=19/10`.

Theorem 5.1 gives, for arbitrary independent cap-one laws and arbitrary affine terms,

`boxed( p in C_0(R),  ||p||_infinity < 8.077. )`                          (7.4)

Thus the new receiver covers a literal target matrix in the chamber where every physical pair is definite.

## 8. A second concrete application of account02/B15: delocalized rank-one Schur banks

The partner report studies

`Q_m=(P_1+L_1)^2-(P_2-L_2)^2+Y_m^2`,
`Y_m=m^(-1/2)sum_{j=1}^m W_j`,                                           (8.1)

whose spectrum is `{2,-2,1,0,...,0}`. Selecting the ORIGINAL pair `(P_1,P_2)` gives

`Delta=1`, `kappa_2=1`,

and a collective rank-one Schur remainder with nonzero eigenvalue `sigma=1`, even though its individual physical coefficients are only `1/m`. Applying the designated partner theorem gives the dimension-free inequality

`boxed( ||p_{Q_m}||_infinity <=8sqrt(2) )`                                (8.2)

for every `m` and every admissible product law. This explicitly shows the gain from aggregating the Schur bank before paying a reciprocal physical coefficient.

The same source separately proves the sharper special-family bound `pi sqrt(2)`; (8.2) is recorded because it is the direct application of the collective theorem.

There is also a useful regularity consequence. If two admissible product input laws `F,G` for the same `A_m` have full `L^1` distance `delta`, their output laws contract total variation:

`||p_F-p_G||_1<=delta`.

By (8.2), `||p_F-p_G||_infinity<=16sqrt(2)`. Hence, for every finite `1<=r<infinity`, interpolation gives

`boxed( ||p_F-p_G||_r <= (16sqrt(2))^(1-1/r) delta^(1/r). )`              (8.3)

For product sources one may use

`delta <= sum_i ||f_i-g_i||_1`.

Thus the partner's aggregate rank-one Schur theorem yields a dimension-free finite-`L^r` rough-source stability modulus on this genuinely delocalized target family. As expected, it does not give an `r=infinity` approximation modulus.

## 9. What this does and does not settle

The new square-kernel compiler isolates a precise regularity threshold: once the residual density is controlled in **any** `L^p` strictly above `2`, the coupled square pivot has a bounded `C_0` density. The completed physical-pair logarithmic estimate supplies such `L^p` control for every finite `p>1`, and therefore pays a fully coupled physical-triple chamber with explicit constants.

This does not solve full QFORM. The bare spectral hypothesis `s_3(A)>=1` does not force an invertible physical triple whose parameters in (5.2) or (6.1) are uniformly nondegenerate; known delocalized examples make every single physical minor small. The still-unpaid implication is structural/aggregate: retain enough original-product smoothing across many small physical coordinates before inversion, or route the matrix into an already-proved volume/ridge/grouped receiver.

The latest partner obstruction also remains important: allowing an arbitrary nonzero leaf-leaf quadratic block and then taking a worst fibre can expose an unbounded rank-two hyperbolic density even inside a full target instance whose unconditional law is bounded. The third smoothing resource must remain inside the analytic receiver. Theorem 3.1 gives one exact way to do so when that resource enters through a coupled square pivot and the residual crosses the `L^p`, `p>2`, threshold.

Full unrestricted QFORM: `OPEN_NOT_PROVED`.
