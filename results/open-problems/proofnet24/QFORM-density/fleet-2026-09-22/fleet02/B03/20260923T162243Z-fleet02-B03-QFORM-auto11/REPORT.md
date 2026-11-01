SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B03, 2026-09-23T16:22:43Z.
attacking: the near-coloop/grouped-pair endpoint — keep one genuine independent scalar, identify exactly when a bounded-density dependent two-dimensional projection is enough, and test whether pair-density compression can replace the product/determinant structure in the remaining collar.

# fleet02/B03 — transverse rank-one pair curvature and a cap-only obstruction

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260923T162243Z-fleet02-B03-QFORM-auto11`  
**Assignment:** Decoupled time integral  
**Status:** `NEW SUPPORTING THEOREM + SOURCE-VALID INTERMEDIATE COUNTEREXAMPLE + NEWEST-PARTNER/PROJECTED-CROSSING APPLICATIONS / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.


## 1. Sources actually consumed

The required pinned Claude package was read at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

under `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`, including `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. In particular I retain the product-coordinate Fourier/Lp estimates, Theorem D/D'/D5 gates and all stated counterexample boundaries; no claim there closes the full theorem.

The later owner continuation required the current Claude record

`yspennstate/math-open-problems@c4c23b784395630c094ba299a50712209921d1ae`

`proofnet24/QFORM-density/interactive/20260922T231000Z-semidefinite-and-hub-reduction/README.md`.
Its newest `hub that sees P` proposal `(SP)` is explicitly OPEN, not used as a theorem here.

The newest interactive projected-crossing theorem used below is

`yspennstate/math-open-problems@4f92aeb74083c6f95cb314a11fed1b812eacef9a`

`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.
It proves the arbitrary-rank projected crossing compiler `(GC)` provided the projected crossing volume and every row-marginal gate are actually verified.

The latest designated partner fleet03/B03 result actually used below is the 16:23 exact-coloop compiler and its supplement,

`yspennstate/math-open-problems@dc887389947d0e4195eb1e28d6736060e718905c`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B03/20260923T162345Z-fleet03-B03-QFORM-r35/{REPORT.md,SUPPLEMENT.md}`.
It proves a target-scale density bound at an exact right-frame coloop and dependence-safe weighted whole-copy time estimates for the residuals.

## 2. Main new theorem — arbitrary scalar self-curvature is harmless against a transverse rank-one pair curvature

### Theorem 2.1 — `QFORM-TRANSVERSE-RANKONE-PAIR-CURVATURE-v1`

Let `X` be a real random variable with probability density `f<=1`. Let `(C,D)` be independent of `X` and have an arbitrary joint probability density `g` satisfying

`||g||_infinity <= M`.

No independence between `C` and `D` is assumed. Let `a` be arbitrary, let `beta*gamma!=0`, and allow an arbitrary affine term `ell_1 X+ell_2 C+ell_3 D+c_0`. Then

`Q = a X^2 + 2 beta X C + gamma D^2 + ell_1 X+ell_2 C+ell_3 D+c_0`

has an essentially bounded density and

`boxed:
 ||p_Q||_infinity
 <= 3(8 sqrt(2) M)^(2/3) |beta^2 gamma|^(-1/3).
}`

The constant is completely independent of the scalar self-curvature `a`. Equivalently, for the quadratic matrix

`B=[[a,beta,0],[beta,0,0],[0,0,gamma]]`,

whose determinant is `-beta^2 gamma`, the right side depends on `B` only through this determinant and the pair cap.

This is a near-null interpolation theorem: the scalar square coefficient may pass through zero without any reciprocal `|a|` loss. The structural hypothesis that the pair curvature is rank one and that the scalar couples to its null direction is essential; Section 5 gives a fixed target-scale counterexample if one discards it and remembers only a joint pair-density cap.

### Affine reduction

Because `det B=-beta^2 gamma!=0`, every affine term is removed by a deterministic translation. If `h=(1/2)B^{-1}ell`, then

`z^T Bz+ell^T z+c_0=(z+h)^TB(z+h)+constant`.

Translating `X` and translating the pair `(C,D)` by fixed vectors preserves the density caps and preserves the independence of `X` from the pair. It therefore suffices to prove the homogeneous assertion.

### Scaling reduction

Put

`C'=beta C`, `D'=sqrt(|gamma|)D`.

The joint density of `(C',D')` is bounded by

`M' = M/(|beta|sqrt(|gamma|))`,

and

`Q=aX^2+2XC'+sgn(gamma)D'^2`.

Thus it is enough to prove

`||p_Q||_infinity <=3(8sqrt(2)M')^(2/3)`.

### Exact scalar pushforward kernel

Fix an output level `t`. Conditional on `(C,D)=(c,d)`, the polynomial in the genuine independent scalar is

`q_{c,d}(x)=a x^2+2cx+eps d^2`, `eps in {+1,-1}`.

For almost every `(c,d,t)` its pushforward density is

`K_t(c,d)=sum_{x:q_{c,d}(x)=t} f(x)/(2|ax+c|)`.

There are at most two roots. If `K_t(c,d)>s`, at least one root obeys

`f(x)/(2|ax+c|)>s/2`,

hence, with

`u=ax+c`,

`f(x)>s|u|`.                                                        (2.1)

Parameterize such a root by `(x,u)`. Then

`c=u-ax`,
`eps d^2=t+a x^2-2ux`.                                             (2.2)

For either square-root branch the Jacobian is exactly

`|det d(c,d)/d(x,u)|=|u|/|d|`.                                    (2.3)

This identity is the key cancellation: the potentially dangerous scalar critical point contributes the same `|u|` that appears in the superlevel condition (2.1).

### Weak `L^{3/2}` superlevel estimate

Put `m=f(x)/s`. For fixed `x!=0`, set

`y=t+a x^2-2ux`.

On `|u|<m`, the corresponding `y`-interval has length `4|x|m` and `|t+a x^2-y|<=2|x|m`. Therefore, on either allowed sign half-line,

`int_{|u|<m, eps*y>0} |u|/sqrt(|y|) du
 <= 2 m^(3/2)/sqrt(|x|)`.                                          (2.4)

There are two square-root branches. Hence

`|{(c,d):K_t(c,d)>s}|
 <=4 s^(-3/2) int f(x)^(3/2)|x|^(-1/2) dx`.                        (2.5)

Since `f<=1`, `f^(3/2)<=f`. The cap-one bathtub principle for the decreasing kernel `|x|^(-1/2)` gives

`int f(x)^(3/2)|x|^(-1/2) dx
 <=int_{-1/2}^{1/2}|x|^(-1/2)dx
 =2sqrt(2)`.                                                        (2.6)

Thus uniformly in `a`, `t`, and the sign of the pair square,

`boxed:
 |{K_t>s}| <=8sqrt(2) s^(-3/2).
}`                                                                  (2.7)

### Layer cake against the dependent pair

Because `g<=M'` and `g` has mass one,

`p_Q(t)=int g(c,d)K_t(c,d) dc dd
 <=int_0^infinity min(1,8sqrt(2)M' s^(-3/2)) ds`.

At the crossover `s_0=(8sqrt(2)M')^(2/3)`, the integral is exactly

`s_0+2(8sqrt(2)M')s_0^(-1/2)=3(8sqrt(2)M')^(2/3)`.

This proves Theorem 2.1. No coordinate transformation mixes `X` with `(C,D)`; the only rotation/scaling is internal to the already-dependent pair, where independence is not asserted or needed.

## 3. Dependence-safe independent-copy integral and linear collision scale

Let

`C_Q=3(8sqrt(2)M)^(2/3)|beta^2 gamma|^(-1/3)`.

The theorem gives `||p_Q||_infinity<=C_Q`, hence

`||p_Q||_2^2<=C_Q` and `||p_{Q-Q'}||_infinity<=C_Q`

for an independent copy `Q'`. Therefore

`boxed:
 P(|Q-Q'|<=eps) <=2 C_Q eps.
}`                                                                  (3.1)

This is already linear small-ball scaling. The assigned whole-copy Fourier identity is used only at the output level,

`|phi_Q(t)|^2=E exp(it(Q-Q'))`,                                    (3.2)

so no conjugate sum/difference pair is ever declared independent.

The cap `p_{Q-Q'}<=C_Q` and the one-dimensional bathtub bound imply

`E|Q-Q'|^(-1/2)<=2sqrt(2C_Q)`.

Using the exact one-dimensional Riesz identity in the same convention as the B03 partner results,

`int_R |t|^(-1/2)|phi_Q(t)|^2 dt
 =sqrt(2pi) E|Q-Q'|^(-1/2)`,

we obtain the dimension-free integrated estimate

`boxed:
 int_R |t|^(-1/2)|phi_Q(t)|^2 dt
 <=4sqrt(pi C_Q).
}`                                                                  (3.3)

Thus the new real-space weak-kernel theorem also supplies the requested dependence-safe fractional time integral.

## 4. Actual owner-target corridor: a nonzero near-null physical scalar plus a dependent product projection

Let `Y=(Y_1,...,Y_m)` have independent cap-one coordinates and let `v,w in R^m` be orthonormal. Put

`C=v.Y`, `D=w.Y`.

The proved two-dimensional orthonormal product-projection estimate gives

`||p_(C,D)||_infinity<=2`.

Let `X_0` be another original independent cap-one coordinate. For every `|a|<=1`, define

`Q_a=aX_0^2+4X_0 C+D^2`,                                          (4.1)

with arbitrary affine terms also allowed. In the orthonormal grouped basis `(X_0,C,D)`, the nonzero quadratic matrix is

`B_a=[[a,2,0],[2,0,0],[0,0,1]]`.

Its eigenvalues are

`1`, `(a+sqrt(a^2+16))/2`, `(a-sqrt(a^2+16))/2`.

For `|a|<=1`, the smaller modulus of the last two is

`(sqrt(a^2+16)-|a|)/2 >=(sqrt(17)-1)/2>1`.

Hence every `Q_a` is a genuine arbitrary-dimensional owner-target form: its matrix has three eigenvalues of modulus at least one, and the original inputs remain independent.

Theorem 2.1 with `M=2`, `beta=2`, `gamma=1` gives the uniform near-null bound

`boxed:
 ||p_{Q_a}||_infinity
 <=3(16sqrt(2))^(2/3)4^(-1/3)
 =15.1190525988... .
}`                                                                  (4.2)

Consequently

`P(Q_a in I)<=15.120 |I|`,
`P(|Q_a-Q_a'|<=eps)<=30.239 eps`,

and

`boxed:
 int |t|^(-1/2)|phi_{Q_a}(t)|^2dt
 <=27.5674894246... .
}`                                                                  (4.3)

This pays a bona fide nonzero near-null corridor without a reciprocal scalar-pivot factor. It does not pay a general coloop packet: the rank-one/transversality geometry of the pair block is the exact hypothesis doing the work.

## 5. Source-valid obstruction — a joint pair-density cap alone cannot replace product/determinant provenance

The preceding theorem might tempt one to compress every remaining physical bank to an arbitrary dependent pair with bounded joint density and then forget how that pair arose. That interface is false even for a fixed three-dimensional matrix whose three eigenvalues stay uniformly outside `[-1,1]`.

### Proposition 5.1 — `QFORM-INDEPENDENT-SCALAR-JOINT-PAIR-CAP-ARBITRARY-3X3-FALSE-v1`

For every sufficiently large `R`, let

`eps_R=4/log R`,
`c_1=eps_R/10`, `c_0=c_1/R`,

and let `(C,D)` have density one on

`E_R={c_0<=c<=c_1, -eps_R/(4c)<=d<=0}`.                            (5.1)

The area is

`int_{c_0}^{c_1} eps_R/(4c) dc=(eps_R/4)log R=1`,

so this is a probability density with cap one. Set

`Y=4CD`.

Under `(c,d)->(c,y)`,

`p_(C,Y)(c,y)=1/(4c)` on `[c_0,c_1] x [-eps_R,0]`.

The marginals are

`p_C(c)=1/(c log R)`, `p_Y(y)=1/eps_R`,

and their product is exactly `1/(4c)`. Hence

`boxed: C and Y are independent, and Y~Uniform[-eps_R,0].}`        (5.2)

Let `X~Uniform[0,1]` be independent of the pair and consider

`Q_R=2X^2+XC+4CD`.                                                  (5.3)

The quadratic matrix is the fixed matrix

`B=[[2,1/2,0],[1/2,0,2],[0,2,0]]`.                                 (5.4)

At zero coupling between the first two coordinates the comparison matrix has spectrum `{-2,2,2}`. The perturbation has operator norm `1/2`, so Weyl's inequality gives

`boxed: every eigenvalue of B has modulus at least 3/2.}`           (5.5)

Thus the matrix itself is stronger than the target spectral hypothesis.

On the event

`0<=X<=sqrt(eps_R)/4`,

which has probability `sqrt(eps_R)/4` for `eps_R<=16`, we have

`0<=S:=2X^2+XC<=eps_R/8+eps_R/10=9eps_R/40`.                       (5.6)

By (5.2), `Y=4CD` is uniform on `[-eps_R,0]` and is independent of `(X,C)`, hence of `S`. For every `0<h<=eps_R/2`, (5.6) implies `S+h<eps_R`, and therefore

`P(Q_R in[-h,0] | S)=h/eps_R`

on the displayed event. Consequently

`boxed:
 P(Q_R in[-h,0])/h
 >=1/(4sqrt(eps_R))
 =sqrt(log R)/8 -> infinity.
}`                                                                  (5.7)

Therefore there is no universal density bound for a theorem whose only stochastic hypotheses are “one cap-one scalar is independent of an arbitrary two-dimensional joint density of cap one”, even with a fixed coefficient matrix satisfying three `|lambda|>=3/2`.

This is **not a QFORM counterexample**: `C,D` are dependent and have not been realized as two original independent coordinates or as a source-valid product projection with the additional Fourier/determinant structure needed by the fleet theorems. It refutes only the cap-only grouped interface. In particular, the current Claude `(SP)` proposal and the projected-crossing theorem cannot be replaced by a black-box joint-pair cap.

## 6. Newest projected-crossing theorem applied to an actual physical partition

The later owner continuation specifically asks B01-B04 workers to check the new arbitrary-rank projected-crossing theorem `(GC)` on an actual physical partition rather than merely cite it. Here is an exact target-valid application with every gate computed.

Take eight disjoint original coordinates

`H,L,X_1,X_2,X_3,X_4,Y_1,Y_2`

with arbitrary independent cap-one laws and set

`Q_cross=2HL + sqrt(2)(X_1+X_2)Y_1 + sqrt(2)(X_3+X_4)Y_2`.         (6.1)

With

`U_1=(X_1+X_2)/sqrt(2)`, `U_2=(X_3+X_4)/sqrt(2)`,

its nonzero matrix is three orthogonal hyperbolic pairs, so its nonzero spectrum is

`{+1,-1,+1,-1,+1,-1}`.

It is therefore an exact owner-target form.

Apply `(GC)` with one genuine hub `H` (`k=1`, `M_H=1`) and light split

`I={X_1,X_2,X_3,X_4}`,
`J={L,Y_1,Y_2}`.

The hub cross row on `J` is

`M_J=(1,0,0)`,

so `rank(M_J)=1` and its singular-value product is `S=1`. After projection orthogonal to `row(M_J)`, the crossing matrix is

`C=[[0,1/sqrt(2),0],
    [0,1/sqrt(2),0],
    [0,0,1/sqrt(2)],
    [0,0,1/sqrt(2)]]`.

Its two nonzero singular values are both one, hence

`Z_2=e_2(CC^T)=1`.

Because this is exact rank two, its squared-two-volume row marginals are its row leverages, all equal to `1/2`. Thus the theorem's nontrivial gate `alpha_i<=1/2` holds exactly, not approximately.

With `ell=2`, `d=k+ell=3`, `(GC)` gives

`boxed:
 ||p_{Q_cross}||_infinity
 <=3*2^(7/6)*exp(1/3)
 =9.39913188785... .
}`                                                                  (6.2)

This is an equation-level use of the newest projected-crossing result on a genuine original-coordinate target matrix. It also illustrates why Section 5 matters: `(GC)` retains the volume sampling of the projected crossing; replacing it merely by a bounded joint law for some compressed pair is invalid.

## 7. Latest designated partner fleet03/B03 applied to an actual exact-coloop target

Take four independent cap-one original coordinates `X_0,R_1,R_2,U` and

`Q_col=(X_0+R_2)^2+2UR_1`.                                        (7.1)

The square block has eigenvalues `{2,0}` and the hyperbolic block has eigenvalues `{+1,-1}`, so the nonzero spectrum is

`{2,+1,-1}`.

Thus `s_3(A)=1` and this is again exactly in the owner target.

It fits the latest fleet03/B03 r35 packet with

`a=m=rho=y=sigma=1`, `beta=0`,
`v=(1,0)`, `q=(0,1)`

on the right bank `(R_1,R_2)`. The row `R_1` is an exact coloop:

`eta_1=v_1^2+q_1^2=1`,

and it is exactly the singular angular case for the physical pivot,

`h_1=beta v_1+m q_1=0`, `h_c=1`.

Therefore the partner's `QFORM-EXACT-COLOOP-AGGREGATE-HALFRIESZ-v1` applies without any limiting argument and yields

`boxed:
 ||p_{Q_col}||_infinity
 <=2^(13/4)e^(3/4)
 =20.1404118577... .
}`                                                                  (7.2)

Its completed collision consequence gives, for an independent whole copy,

`boxed:
 P(|Q_col-Q_col'|<=eps)
 <=2^(17/4)e^(3/4) eps
 =40.2808237155... eps.
}`                                                                  (7.3)

This is the required actual application of the latest compatible designated-partner result. The proof keeps the complete-copy identity and never treats a coordinate sum and difference as independent.

## 8. What is now paid and what remains

This run changes the near-coloop map in two ways.

First, **nonzero scalar self-curvature itself is not the obstruction** when the dependent pair curvature is rank one and the scalar couples transversely to its null direction: Theorem 2.1 is completely uniform in `a`, and the target family (4.1) gives a concrete nonzero near-null corridor with a universal density bound below `15.120`.

Second, the exact construction in Section 5 shows that one cannot close the remaining collar by compressing the light side to an arbitrary two-dimensional law and retaining only a joint `L^infinity` cap. Even a fixed target-scale 3x3 coefficient matrix then admits density blowup of order `sqrt(log R)`. The extra product/determinant/Fourier provenance in the newest projected-crossing theorem and in fleet03/B03's aggregate compiler is mathematically necessary information, not bookkeeping.

The first unpaid implication for this slot is therefore a **regularized near-coloop interpolation retaining the weak physical direction**: in the fleet03/B03 collar `c->1`, `h_r->0`, `c<1`, use the strong one-dimensional aggregate direction together with the weak complement before compression. A viable proof must preserve either the projected crossing volume/marginals of `(GC)`, the exact product-bank selector structure of the partner packet, or another equivalent source-valid invariant. A cap-only two-dimensional grouped receiver is now ruled out.

The unrestricted arbitrary-dimensional QFORM theorem remains **OPEN**, and full-target continuity remains **OPEN**.
