# account03/B17 QFORM r13 — fixed-frame Edgeworth barrier for sharp witnesses

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Worker:** account03/B17  
**Run:** 20260922T170559Z-account03-B17-QFORM-r13  
**Classification:** SUBCLASS SHARP-CONSTANT CONSTRAINT / NEW WITNESS EXCLUSION; **not** a proof of full QFORM  
**Brain status:** WITHOUT_VERIFIED_BRAIN

## 1. Exact target and purpose

The unrestricted target remains: for independent real coordinates with densities bounded by one, and real symmetric `A` having at least three eigenvalues of magnitude at least one, prove a universal finite essential-density bound for `Q=X^T A X`, or give a counterexample. No Gaussian, moment, compact-support, connected-support, or eigenbasis-independence assumption is allowed.

B17's assignment is sharp constants and witnesses. Earlier B17 runs showed that disjoint three-bank repeated frames cannot create a finite-`m` spike above a universal `2 pi` bound, and that some small exact rotations increase the peak relative to a diagonal control without beating the established lower bound `3 sqrt(2)`. The first genuinely unresolved sharp-witness mechanism is therefore a **shared-coordinate rank-three frame**: every physical coordinate may load several active eigen-directions, while the matrix still has exact nonzero spectrum `{1,1,-1}`.

This report proves that every *fixed* shared-coordinate tight-frame architecture, repeated with centered density-one interval inputs, approaches the Gaussian lower-bound value `3 sqrt(2)` from **below**, with an explicit strictly positive first correction. It also determines the sharp infimum of that first correction across all fixed finite frame patterns.

This does not settle arbitrary cap-one laws, frames changing on the same scale as `m`, fragmented/mesoscopic laws, or the full QFORM theorem.

## 2. Exact repeated-frame stress family

Fix an integer `d>=3` and a real `d x 3` matrix `W` whose rows are `w_1,...,w_d in R^3` and whose columns are orthonormal:

`W^T W = I_3`, equivalently `sum_k w_k w_k^T = I_3`.

For each integer `m>=1`, form the `dm x 3` matrix `R_m` by repeating each row `w_k/sqrt(m)` exactly `m` times. Then

`R_m^T R_m = I_3`.

Let

`Lambda = diag(1,1,-1)`,  `A_m = R_m Lambda R_m^T`.

Therefore `A_m` has **exact** nonzero eigenvalues `1,1,-1` for every `m`; the remaining `dm-3` eigenvalues are zero. This is an exact source-valid spectral stress family, not an approximate eigenvalue construction.

Let all `dm` physical coordinates `X_{k,r}` be iid `Unif[-1/2,1/2]`, whose density is exactly one. Define

`Y_m = R_m^T X = (1/sqrt(m)) sum_{k=1}^d sum_{r=1}^m w_k X_{k,r}`.

Then

`Q_m = X^T A_m X = Y_{m,1}^2 + Y_{m,2}^2 - Y_{m,3}^2`.

The physical coordinates remain independent. The active coordinates `Y_{m,j}` generally are **not** independent; shared rows of `W` create exactly the eigen-coordinate dependence that a general rotation introduces.

Set `Z_m=sqrt(12) Y_m`. Since `Var(X_{k,r})=1/12`,

`Cov(Z_m)=I_3`, and `Q_m=(1/12) q(Z_m)`, where `q(z)=z_1^2+z_2^2-z_3^2`.

## 3. First-order multivariate Edgeworth expansion

For `U=sqrt(12) X` with `X~Unif[-1/2,1/2]`,

`E exp(i s U) = sinc(sqrt(3) s)`.

Hence the characteristic function of `Z_m` is exactly

`Phi_m(t) = product_{k=1}^d sinc(sqrt(3) (w_k dot t)/sqrt(m))^m`.

The Taylor expansion

`log sinc z = -z^2/6 - z^4/180 + O(z^6)`

gives, using `sum_k (w_k dot t)^2=|t|^2`,

`Phi_m(t)=exp(-|t|^2/2) [1 - (1/(20m)) sum_k (w_k dot t)^4 + O_W(m^-2 P_8(t))]`

on the small-frequency region, for a fixed polynomial `P_8`. Because `W` is fixed and spans `R^3`, the repeated sinc factors give an integrable Gaussian-type majorant on moderate frequencies and an exponentially/super-polynomially small contribution after the usual fixed-dimensional Fourier split. In particular one obtains the weighted density expansion

`g_m(z)=phi_3(z) [1 - (1/(20m)) sum_k H_{4,w_k}(z)] + O_W(m^-2 (1+|z|)^(-K))`

for any fixed sufficiently large `K`, where `phi_3` is the standard Gaussian density and

`H_{4,w}(z)=(w dot z)^4 - 6 |w|^2 (w dot z)^2 + 3 |w|^4`.

For completeness, the only properties required for this Fourier step are: finite fixed frame `W`, bounded interval summands, the exact spanning identity `W^T W=I_3`, and repeated factors. No claim about arbitrary bounded densities or law-uniform pointwise quadratic-phase decay is used.

The weighted remainder is integrable against the cone coarea measure below, so the expansion may be integrated over `q(z)=0` term-by-term.

## 4. Gaussian cone measure and an exact directional Hermite average

For standard Gaussian `G in R^3`, write `q(G)=G_1^2+G_2^2-G_3^2`. Since `G_1^2+G_2^2 ~ chi^2_2` and `G_3^2 ~ chi^2_1` independently,

`p_{q(G)}(0)=1/(2 sqrt(2))`.

Therefore the density at zero of `(1/12)q(G)` equals

`12/(2 sqrt(2)) = 3 sqrt(2)`.

To compute the Edgeworth correction exactly, normalize the Gaussian coarea measure on the cone `q(z)=0`. In cylindrical coordinates

`z_1=r cos(theta)`, `z_2=r sin(theta)`, `z_3=sigma r`,

where `theta` is uniform on `[0,2pi)`, `sigma` is uniform on `{+1,-1}`, and `u=r^2` has the Gamma distribution

`u ~ Gamma(shape=1/2, rate=1)`.

Thus `E u=1/2`, `E u^2=3/4`.

For a row `w=(w_1,w_2,w_3)`, put

`x=w_1^2+w_2^2`,  `y=w_3^2`.

A direct angular/sign/radial average gives

`E_cone[(w dot Z)^2] = (1/2)(x/2+y)`,

`E_cone[(w dot Z)^4] = (3/4)(3x^2/8 + 3xy + y^2)`.

Substituting into `H_{4,w}` yields the exact identity

`E_cone H_{4,w} = (3/32) (19 x^2 + 40 x y + 8 y^2)`.

Every coefficient is positive. In particular this is strictly positive for every nonzero row.

Define

`A_W = (3/32) sum_{k=1}^d (19 x_k^2 + 40 x_k y_k + 8 y_k^2)`.

Since `W^T W=I_3`,

`sum_k x_k=2`, `sum_k y_k=1`.

## 5. Main theorem: every fixed shared frame approaches 3 sqrt(2) from below

Combining the density Edgeworth expansion with the cone average and the scaling `Q_m=q(Z_m)/12` gives

**Theorem.** For every fixed finite tight frame `W` as above,

`p_{Q_m}(0) = 3 sqrt(2) [ 1 - A_W/(20m) + O_W(m^-2) ]`.

Equivalently,

`p_{Q_m}(0) = 3 sqrt(2) [1 - (3/(640m)) sum_k (19x_k^2+40x_k y_k+8y_k^2) + O_W(m^-2)]`.

Because `A_W>0`, every fixed architecture approaches the Gaussian value `3 sqrt(2)` **strictly from below**. Consequently no fixed repeated shared-coordinate frame with centered unit-interval physical inputs can improve the known universal lower bound `C >= 3 sqrt(2)` by taking `m` large.

This statement is substantially stronger than a diagonal/disjoint-bank CLT control: rows `w_k` can have all three entries nonzero, so active eigen-coordinates may be strongly dependent at every finite `m`.

The theorem is a sharp-witness exclusion only. It does not provide a uniform upper bound for arbitrary QFORM inputs.

## 6. Universal sharp first-order barrier across fixed patterns

The first correction itself has a universal frame lower bound. For `x,y>=0`,

`19x^2+40xy+8y^2 >= (sqrt(19)x + sqrt(8)y)^2`,

because `40 >= 2 sqrt(152)`. Therefore by Cauchy-Schwarz,

`sum_k (19x_k^2+40x_k y_k+8y_k^2)`

`>= (1/d) (sqrt(19) sum x_k + sqrt(8) sum y_k)^2`

`= (1/d)(2 sqrt(19)+sqrt(8))^2`.

Hence

`A_W >= (63+6 sqrt(38))/(8d)`.

Let `N=dm` be the physical dimension. Then

`A_W/(20m) >= gamma_*/N`,

where

`gamma_* = (63+6 sqrt(38))/160 = 0.6249155251113366...`.

Thus every fixed-frame repeated-uniform family obeys

`p_{Q_m}(0) = 3 sqrt(2) [1 - gamma_W/N + O_W(N^-2)]`,

with

`gamma_W >= gamma_* > 0`.

### Sharpness of gamma_*

This coefficient barrier is sharp over finite frame patterns. Split the frame into:

- `p` rows contained in the positive two-plane, forming an equal-norm 2D tight frame, so each has `x=2/p,y=0`;
- `q` rows on the negative axis, each with `x=0,y=1/q`.

Then `d=p+q` and

`A_W=(3/32)(76/p+8/q)`,

so the coefficient expressed in total dimension is

`gamma_{p,q}= d A_W/20 = (3d/640)(76/p+8/q)`.

As `p/q -> sqrt(76/8)=sqrt(19/2)`,

`gamma_{p,q} -> gamma_*`.

Therefore `gamma_*` is the exact infimum of the first-order coefficient over this fixed-pattern architecture.

The very small gap between the simple choice `(p,q)=(3,1)` and the optimum is useful:

`gamma_{3,1}=5/8=0.625`,

only about `8.45e-5` above `gamma_*`.

## 7. Exact fully shared and control examples

### 7.1 Fully shared four-row Hadamard frame

Take three columns of a normalized `4 x 4` Walsh-Hadamard matrix. Every row has

`x=1/2`, `y=1/4`,

so every physical coordinate loads all three active eigendirections. The theorem gives

`A_W = 123/32`,

and with `N=4m`,

`p_{Q_m}(0)=3 sqrt(2)[1 - 123/(160N)+O(N^-2)]`.

Thus a genuinely shared-coordinate rotation still approaches `3 sqrt(2)` from below.

### 7.2 Disjoint three-bank control

For `W=I_3`,

`A_W=69/16`,

so

`p_{Q_m}(0)=3 sqrt(2)[1-69/(320m)+O(m^-2)]`

`=3 sqrt(2)[1-207/(320N)+O(N^-2)]`.

This matches the sign and scale expected from the prior disjoint-bank analysis.

### 7.3 Near-optimal split frame `(p,q)=(3,1)`

Use three equal-norm vectors at angles `0, 2pi/3, 4pi/3` in the positive plane, each of squared norm `2/3`, plus one unit vector on the negative axis. Then

`A_W=25/8`, `N=4m`,

and

`p_{Q_m}(0)=3 sqrt(2)[1-5/(8N)+O(N^-2)]`.

This family is within `0.000085` in the `1/N` coefficient of the optimal fixed-pattern barrier.

## 8. Application of compatible account04 mathematics

The designated partner `account04/B17` has no completed QFORM handoff visible in the source tree at this run. I therefore did not invent or attribute a nonexistent result. I applied the compatible completed `account04/B18` Schur-pivot theorem instead. Its proved inequality is:

if a physical `3 x 3` principal block `B` has a nonzero pivot `a` whose Schur complement is definite, then

`||p_Q||_infinity <= 2 sqrt(pi) / |a det B|^(1/4)`.

Apply this to the near-optimal `(p,q)=(3,1)` frame above. Select two distinct positive-plane physical rows and one negative-axis row. After ordering the negative row as pivot, the principal block is

`B_m=(1/m) [[2/3,-1/3,0],[-1/3,2/3,0],[0,0,-1]]`.

Its negative pivot is

`a=-1/m`,

its Schur complement is the positive definite upper `2 x 2` block, and

`det B_m=-1/(3m^3)`.

Therefore the account04/B18 theorem gives the exact applied inequality

`||p_{Q_m}||_infinity <= 2 * 3^(1/4) * sqrt(pi) * m`

`= 4.665360904668642... m`.

The theorem is valid, but on this sharp repeated-frame stress it grows linearly while the actual zero-density converges to `3 sqrt(2)`. This quantitatively identifies the loss in a single-physical-triple payment: local determinants shrink as `m^-3` even though the aggregate rank-three spectral mass stays fixed.

This is consistent with the current correction that a proof cannot extract one good physical minor and pay an inverse power of that minor without an aggregate mechanism.

## 9. What this rules out, and what remains viable

This run rules out a substantial witness mechanism:

> **No fixed finite shared-coordinate tight-frame pattern, repeated with centered density-one interval inputs, can beat `3 sqrt(2)` asymptotically. In fact its zero-density has a universal strictly negative first correction, with optimal total-dimension coefficient `gamma_*=(63+6sqrt(38))/160`.**

Therefore a sharp lower-bound witness exceeding `3 sqrt(2)`, if one exists, must leave at least one ingredient of this regime. Plausible remaining mechanisms include:

1. finite/mesoscopic dimension rather than a fixed-pattern large-repetition limit;
2. nonuniform or fragmented cap-one laws whose local limit is not governed by the ordinary fixed-frame Edgeworth correction;
3. a frame pattern whose complexity grows with `m` in a genuinely multiscale way;
4. interactions with additional spectral directions rather than an exact rank-three architecture.

The next B17 attack should therefore not rerun another fixed-frame CLT family. A materially different target is a **growing-pattern shared frame with fragmented density-one inputs**, designed so that no fixed finite row-type Edgeworth expansion captures the cone mass.

## 10. Density/continuity scope

For the repeated-uniform subclass above and sufficiently large `m`, the projected `Z_m` has a continuous density obtained by convolution/Fourier inversion, and the coarea calculation defines the point density `p_{Q_m}(0)` with the stated expansion. This report proves the stated pointwise asymptotic at zero for this subclass.

It does **not** prove the full target's essential-density bound, nor the full target's requested continuity. Those remain separate open obligations.

## 11. Status

- New mathematics: fixed-frame shared-coordinate Edgeworth barrier, exact cone-Hermite average, sharp first-order coefficient `gamma_*`, and explicit partner-inequality stress application.
- Existing result consumed: account04/B18 Schur-pivot square smoothing theorem.
- Designated partner account04/B17: no completed current-QFORM artifact visible; no claim fabricated.
- Full QFORM conjecture: **OPEN / NOT PROVED**.
- Brain status: **WITHOUT_VERIFIED_BRAIN**.
