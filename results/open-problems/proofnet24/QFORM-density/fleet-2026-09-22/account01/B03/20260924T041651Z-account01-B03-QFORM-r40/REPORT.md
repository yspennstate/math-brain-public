SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B03, 2026-09-24T04:16:51Z.
attacking: the overlap-two exterior-mass branch — replace the condition-number-sensitive physical-pair transducer by a determinant-only one-third-Riesz envelope, then combine it with the dependence-safe one-volume residual estimate.

# account01/B03 r40 — determinant-only physical-pair compiler for overlap-two exterior mass

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: `Decoupled time integral`  
Status: **NEW SUPPORTING THEOREM / ALL INVERTIBLE PHYSICAL-PAIR OVERLAP-TWO PACKETS PAID / FULL QFORM OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

## 0. Target and source-valid scope

The target remains: for independent real coordinates with probability densities bounded by one and a real symmetric matrix `A` with at least three eigenvalues of modulus at least one, prove a universal bound on the density of `Q=X^T A X`, or give a valid counterexample. No moments, compact support, connected support, log-concavity, Gaussianity, or rotation of the product law is used below.

The current corrections are retained. In particular, I do **not** conditionally re-cap one member of `(X-X',X+X')`, do not use law-uniform pointwise quadratic van der Corput, do not assume a uniformly good single minor, and do not use the refuted arbitrary-joint rank-three coarea statement.

The new result removes the `sigma_min(B)` loss from the earlier overlap-two compiler. It is based on a direct product-coordinate level-set estimate for a genuine physical `2 x 2` pair and a one-third Riesz averaging step.

## 1. Prior dependence-safe residual input

Use the proved B03 one-volume half-Frostman theorem from

`yspennstate/math-open-problems@6882d64088e54bc7f979ae8eb4a5ea9d06d1896f`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B03/20260923T185317Z-account01-B03-QFORM-r31/REPORT.md`.

For disjoint original-coordinate banks `I,J`, if

`R=F(X_I)+2 X_I^T M X_J+G(X_J)`

with arbitrary quadratic-plus-affine `F,G` inside their own banks and

`Z_1=||M||_F^2>0`,

then, uniformly in `z` and `rho>0`,

`P(|R-z|<rho) <= H_1 Z_1^(-1/4) sqrt(rho)`,                    (1.1)

where

`H_1=sqrt(2e) Gamma(1/4)=8.453631522124514356...`.              (1.2)

Its proof is product-coordinate and dependence-safe; no conjugate sum/difference conditional cap is used.

## 2. New scalar potential lemma: half-Frostman implies one-third Riesz

### Lemma 2.1

Let `R` be any real random variable such that, for all `z in R` and `rho>0`,

`P(|R-z|<rho) <= min{1,H sqrt(rho)}`.                              (2.1)

Then

`sup_z E |R-z|^(-1/3) <= 3 H^(2/3)`.                              (2.2)

### Proof

For `Z=|R-z|` and `alpha=1/3`, layer cake gives

`E Z^(-1/3)=(1/3) int_0^infty rho^(-4/3) P(Z<rho) d rho`.          (2.3)

Split at `rho_0=H^(-2)`. On `(0,rho_0)`, use `H sqrt(rho)`:

`(H/3) int_0^(H^-2) rho^(-5/6)d rho =2 H^(2/3)`.                 (2.4)

On `(rho_0,infty)`, use probability at most one:

`(1/3) int_(H^-2)^infty rho^(-4/3)d rho=H^(2/3)`.                (2.5)

Adding proves `(2.2)`.

## 3. New determinant-only pair envelope: indefinite case

Let `B` be a real symmetric invertible indefinite `2 x 2` matrix and put

`D=|det B|>0`.                                                      (3.1)

Let `X,Y` be independent cap-one probability-density variables. Arbitrary deterministic translations are allowed. Define

`T=(X+a,Y+b)^T B (X+a,Y+b)`.                                      (3.2)

### Theorem 3.1 — indefinite physical pair

For almost every `t !=0`,

`p_T(t) <= 6 D^(-1/3)|t|^(-1/3)`.                                (3.3)

The estimate is uniform in `a,b` and in the two input laws.

### Proof

Because `B` is indefinite, choose an invertible real matrix `L` such that, for `w=Lz=(u,v)`,

`z^T B z=u v`.                                                      (3.4)

Equivalently `B=L^T J L`, with

`J=[[0,1/2],[1/2,0]]`,

so

`|det L|=2 sqrt(D)`.                                                (3.5)

Put `M=L^(-1)`. The density of `w` is

`rho_W(u,v)=(2 sqrt D)^(-1) f(x(u,v)) g(y(u,v))`,                 (3.6)

where `(x,y)=M(u,v)` and translated `f,g` still have cap one and mass one.

For `t !=0`, parameterize the two branches of `uv=t` by

`u=sigma e^s`, `v=sigma t e^(-s)`, `sigma in {+1,-1}`.             (3.7)

Since `du/|u|=ds`, the exact product-density formula is

`p_T(t)=(2 sqrt D)^(-1) sum_sigma int_R f(x_sigma(s))g(y_sigma(s)) ds`.   (3.8)

Write `gamma_sigma(s)=M(sigma e^s,sigma t e^(-s))`. Each coordinate of `gamma_sigma` has the form

`A e^s+B e^(-s)`,                                                   (3.9)

hence has multiplicity at most two as a map of `s` (unless constant, in which case the derivative-large set below is empty).

Let `V(s)=gamma_sigma'(s)`. Direct calculation gives the exact tangent determinant identity

`|det(V(s),V(r))| = K |sinh(s-r)|`,
`K=|t|/sqrt D`.                                                     (3.10)

Fix `a_0>0` and let

`E_0={s: |x'(s)|<=a_0 and |y'(s)|<=a_0}`.                          (3.11)

For `s,r in E_0`, the left side of `(3.10)` is at most `2a_0^2`. Since `|sinh u|>=|u|`,

`|s-r|<=2a_0^2/K`.                                                  (3.12)

Therefore

`|E_0|<=2a_0^2/K`.                                                  (3.13)

On `E_x={|x'|>a_0}`, use `g<=1`, area formula, multiplicity at most two, and `int f=1`:

`int_(E_x) f(x(s))g(y(s)) ds <=2/a_0`.                             (3.14)

On the remaining set with `|x'|<=a_0`, `|y'|>a_0`, similarly the integral is at most `2/a_0`. Hence one hyperbola branch is at most

`4/a_0+2a_0^2/K`,                                                   (3.15)

and both branches are at most

`8/a_0+4a_0^2/K`.                                                   (3.16)

Choose `a_0=K^(1/3)`. The bracket becomes `12K^(-1/3)`. Multiplying by `(2 sqrt D)^(-1)` in `(3.8)` yields exactly

`p_T(t)<=6 D^(-1/3)|t|^(-1/3)`.                                   (3.17)

No moment or support information entered the argument.

## 4. Determinant-only pair envelope: definite case

Now let `B` be invertible definite. Reflect the output if necessary and assume `B>0`. Factor

`B=L^T L`, `|det L|=sqrt D`.                                       (4.1)

For `t>0`, writing `r=sqrt t` and

`gamma(theta)=L^(-1)(r cos theta,r sin theta)`,                    (4.2)

the exact level-set formula is

`p_T(t)=(2 sqrt D)^(-1) int_0^(2pi) f(x(theta))g(y(theta)) dtheta`. (4.3)

Also

`|det(gamma'(theta),gamma'(phi))|=K |sin(theta-phi)|`,
`K=t/sqrt D`.                                                       (4.4)

The crude joint-density cap already gives

`p_T(t)<=pi/sqrt D`.                                                (4.5)

For `K>=8`, choose `a_0=K^(1/3)` and define `E_0` as in `(3.11)` with `theta` derivatives. If `theta_0 in E_0`, then every `theta in E_0` obeys

`|sin(theta-theta_0)|<=2a_0^2/K=2K^(-1/3)<=1`.                    (4.6)

Thus `E_0` lies in two arcs around `theta_0` and `theta_0+pi`, with total measure at most

`4 arcsin(2K^(-1/3)) <=4pi K^(-1/3)`.                             (4.7)

Each coordinate of `gamma(theta)` is a sinusoid and has multiplicity at most two. The same area-formula partition as above therefore gives

`int_0^(2pi) f(x(theta))g(y(theta))dtheta
 <=4K^(-1/3)+4pi K^(-1/3)`.                                       (4.8)

Using `(4.3)`,

`p_T(t)<=2(1+pi) D^(-1/3)t^(-1/3)` for `K>=8`.                    (4.9)

For `0<K<8`, `(4.5)` implies the same bound because

`pi <= 2(1+pi) K^(-1/3)` when `K<8`.                              (4.10)

Hence for either definite sign and for almost every nonzero output value,

`p_T(t) <= C_pair D^(-1/3)|t|^(-1/3)`,
`C_pair=2+2pi=8.283185307179586...`.                              (4.11)

Combining Sections 3 and 4, `(4.11)` is valid for **every invertible real symmetric physical pair**, since the indefinite constant `6` is smaller than `C_pair`.

## 5. Random-center compiler

Let `E` denote arbitrary external original coordinates, independent of the two genuine physical coordinates `X,Y`. Suppose after exact pair completion the full form is

`Q = Z(E)^T B Z(E)+R(E)`,                                          (5.1)

where the two entries of `Z(E)` are `X,Y` plus arbitrary measurable `E`-dependent translations, and `B` is a fixed invertible symmetric physical pair with `D=|det B|`.

Suppose the residual obeys `(2.1)`. Conditional on `E`, `(4.11)` applies with exactly the same constant; therefore for almost every `s`,

`p_Q(s)
 <= C_pair D^(-1/3) E |s-R|^(-1/3)
 <= 3 C_pair D^(-1/3) H^(2/3)`.                                   (5.2)

Thus

`boxed: ||p_Q||_infinity <=3(2+2pi) D^(-1/3) H^(2/3).`             (5.3)

This proves absolute continuity and essential boundedness in the stated scope. This argument does **not** by itself prove continuity.

For an indefinite pair one may retain the sharper constant `18 D^(-1/3)H^(2/3)` from `(3.3)`.

## 6. Overlap-two exterior mass: exact determinant cancellation

Fix a genuine physical coordinate pair `S={h_1,h_2}` with invertible principal matrix

`B=A[S,S]`, `D=|det B|`.                                           (6.1)

Define the localized overlap-two third-minor mass

`J_2(S)=sum_(i!=j, i,j notin S) det A[S union {i}, S union {j}]^2`. (6.2)

Let `C` be the Schur complement of `B` in the external coordinates. Block determinant expansion gives the exact identity

`J_2(S)=D^2 sum_(i!=j) C_ij^2`.                                    (6.3)

Choose a random literal bipartition `L|R` of the external original coordinates. Then

`E_cut ||C[L,R]||_F^2 = J_2(S)/(4D^2)`.                            (6.4)

Hence some physical cut satisfies

`Z_1=||C[L,R]||_F^2 >= J_2(S)/(4D^2)`.                             (6.5)

Apply the one-volume half-Frostman theorem `(1.1)` to the Schur residual:

`H <= H_1 Z_1^(-1/4)
   <= sqrt(2) H_1 D^(1/2) J_2(S)^(-1/4)`.                          (6.6)

Substitute `(6.6)` into `(5.3)`. The determinant cancels exactly:

`D^(-1/3) [D^(1/2)]^(2/3)=1`.                                     (6.7)

Therefore

`boxed:
 ||p_Q||_infinity
 <= C_2 J_2(S)^(-1/6),
 C_2=3(2+2pi) 2^(1/3) H_1^(2/3)
    =129.924435862525374... .}`                                    (6.8)

For an indefinite pair the sharper constant is

`boxed:
 ||p_Q||_infinity
 <=94.1119371673922894... J_2(S)^(-1/6).}`                         (6.9)

This is the main advance of the run: the entire **invertible physical-pair overlap-two packet** is now paid with no `sigma_min(B)` or determinant loss. In particular, it strictly extends the previous double-zero-diagonal nonzero-offdiagonal subbranch.

At the illustrative structural threshold `J_2(S)>=1/144`, `(6.8)` gives

`||p_Q||_infinity <=297.45270437507936...`.                         (6.10)

The constant is not optimized; the point is the complete cancellation of the physical-pair conditioning scale.

## 7. Assignment-specific whole-copy estimate

The proof above does not split a conjugate sum/difference pair. The independent-copy identity is retained only as the whole-output identity

`|phi_Q(t)|^2 = E exp(it(Q-Q'))`.                                  (7.1)

Let `M=C_2 J_2(S)^(-1/6)` be the bound in `(6.8)`. The difference density obeys

`||p_(Q-Q')||_infinity <=M`.                                       (7.2)

For any `R_0>0`,

`E|Q-Q'|^(-1/2)
 <=4M sqrt(R_0)+R_0^(-1/2)`.                                      (7.3)

Optimizing at `R_0=(4M)^(-1)` gives

`E|Q-Q'|^(-1/2) <=4 sqrt(M)`.                                     (7.4)

Using the standard one-dimensional Riesz Fourier identity (obtained rigorously by Gaussian regularization),

`int_R |t|^(-1/2)|phi_Q(t)|^2 dt
 =sqrt(2pi) E|Q-Q'|^(-1/2)`,                                      (7.5)

hence

`boxed:
 int |t|^(-1/2)|phi_Q(t)|^2dt
 <=4 sqrt(2pi C_2) J_2(S)^(-1/12)
 =114.28660859120921... J_2(S)^(-1/12).}`                          (7.6)

This collision estimate is a **posterior consequence** of the stronger one-copy small-ball compiler, not an invalid attempt to deduce `L^infinity` from weighted collision energy alone.

For the sharper indefinite constant `(6.9)`, the coefficient in `(7.6)` improves to `97.26851419367874...`.

## 8. Designated partner account02/B03 applied to an actual inequality

The latest completed designated-partner handoff consumed in this run is account02/B03's `QFORM-DISJOINT-EXTERIOR-MASS-EXIT-v1`, committed in `math-research-brain@c2cf502ba91445ad3119cfb9991131ec7d32d725`, with canonical mathematics `math-open-problems@5e5366b98337d13ba24bf666f4e42155553de7c2`.

For the global overlap decomposition

`e_3(A^2)=E_0+E_1+E_2+E_3 >=1`,                                   (8.1)

the partner theorem gives the actual implication

`E_0>=1/4  ==>  ||p_Q||_infinity
 <=16.9060424511... E_0^(-1/6)
 <=21.301`.                                                        (8.2)

Thus the disjoint exterior sector is closed by the designated partner. If `E_0<1/4`, at least one overlap-heavy sector `E_1,E_2,E_3` exceeds `1/4`; the theorem of this report addresses the `E_2` portion whenever a quantitatively relevant overlap-two packet is carried by an invertible physical pair.

## 9. Remaining implication

Full QFORM is still **OPEN**. The new theorem eliminates the condition-number obstruction for every invertible physical pair in the overlap-two route, but the bare spectral hypothesis does not yet force a single pair `S` with both `J_2(S)` bounded below and `A[S,S]` invertible. The genuinely remaining overlap-two collar is mass supported on singular physical pairs, together with the independent overlap-one/principal-overlap structural debt. Those cases must be routed by aggregate identities, grouped carriers, finite hubs, ridge windows, or another product-preserving mechanism without selecting and inverting a vanishing individual minor.

Continuity for the full target remains open. The new pair-plus-residual compiler establishes an essentially bounded density but not a continuous representative.
