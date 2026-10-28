SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B03, 2026-09-24T03:26:19Z.
attacking: a zero-diagonal physical hyperbola plus one Schur square by a critical translation-uniform L^3 x L^(3/2) compiler; then convert the determinant-scale one-copy density bound into the assigned whole-copy weighted time integral.

# account03/B03 r47 — determinant-scale hyperbola/square compiler

Status: **NEW SUPPORTING THEOREM / LINEAR SMALL-BALL SCALING / WHOLE-COPY TIME ESTIMATE / FULL QFORM OPEN**.
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted owner target remains OPEN. This report does not assume moments, compact or connected support, log-concavity, Gaussianity, iid laws, a diagonal eigenbasis, or independence after rotation. It does not use a law-uniform pointwise quadratic-phase decay estimate. All probabilistic conditioning below is on genuine disjoint original-coordinate sources.

A source search found the earlier `QFORM-ZEROPAIR-THIRD-RIESZ-COAREA-v1` route, which already shows that a physical zero-diagonal pair can be paid against a residual fractional Riesz potential. I do **not** re-claim that mechanism. The new point here is a critical `L^3-L^(3/2)` sharpening: one actual Schur square can be combined directly with the translated hyperbola, and the powers cancel the hyperbola coefficient exactly against the physical `3x3` determinant.

Fresh inherited frontier also remains the account03/B20 two-sided nested-rank-two/finite-hub packet; the theorem below is a receiver for its literal zero-pair + scalar-Schur exits, not a claim that the global frontier always contains such a packet.

## 1. Uniform translated-product envelope in L^3

Let `U,V` be independent real random variables with densities `f,g` satisfying `0<=f,g<=1`. Translations do not change either independence or the cap, so it is enough to treat `W=UV` after replacing `f,g` by translated densities.

For `w!=0`,

`p_W(w)=int_R f(u) g(w/u) du/|u|`.                              (1.1)

Put `r=|w|`.

If `0<r<=1`, split the integral into `|u|<r`, `r<=|u|<=1`, and `|u|>1`. In the first region substitute `v=w/u`; since then `|v|>1`,

`int_(|u|<r) ... <= int_(|v|>1) g(v) dv <=1`.                    (1.2)

In the middle region use only `f,g<=1`, obtaining

`int_(r<=|u|<=1) du/|u| = 2 log(1/r)`.                            (1.3)

In the last region use `1/|u|<=1` and `g<=1`, obtaining at most `int f=1`. Hence

`p_W(w) <= 2+2 log(1/|w|)`,     `0<|w|<=1`.                       (1.4)

For `|w|>=1`, the completed designated-partner account04/B03 hyperbola lemma gives

`p_W(w) <= 2 |w|^(-1/2)`.                                        (1.5)

For completeness, (1.5) is the unscaled form of the partner bound `p_(2mu UV)(y)<=sqrt(2)|mu|^(-1/2)|y|^(-1/2)` and follows by splitting at `|u|=sqrt(|w|)`.

Define the common translation-uniform envelope

`K_0(w) = 2+2log(1/|w|)` for `0<|w|<=1`,
`K_0(w) = 2|w|^(-1/2)`      for `|w|>=1`.                         (1.6)

Then every translated product density is bounded by `K_0`. Moreover

`int_(|w|<=1) K_0(w)^3 dw
 =16 int_0^infinity (1+u)^3 e^(-u) du
 =256`,                                                            (1.7)

because `int (1+u)^3 e^(-u)du = 1+3+6+6=16`, while the partner half-power tail gives the actual inequality

`int_(|w|>=1) K_0(w)^3 dw
 =2 int_1^infinity 8 w^(-3/2) dw
 =32`.                                                             (1.8)

Thus

`boxed: ||K_0||_3^3 <=288.`                                       (1.9)

For `H=2mu(U+a)(V+b)`, `m=|mu|`, the scaled envelope

`K_mu(y)=(2m)^(-1) K_0(y/(2m))`                                   (1.10)

satisfies

`boxed: ||K_mu||_3^3 <=72 m^(-2),
        ||K_mu||_3 <=72^(1/3)m^(-2/3).}`                          (1.11)

The account04/B03 partner theorem has therefore been applied at an actual quantitative step: its tail estimate contributes exactly `8m^(-2)` of the scaled cubic budget in (1.11); the logarithmic near-zero part contributes `64m^(-2)`.

## 2. Sharp-enough L^(3/2) bound for one physical square

Let `Z` have density `h<=1` and let `S=(Z+a)^2`. For `s>0`, write `r=sqrt(s)` and

`G(r)=h(r-a)+h(-r-a)`.

Then `0<=G<=2`, `int_0^infinity G(r)dr=1`, and

`p_S(s)=G(sqrt(s))/(2sqrt(s))`.                                   (2.1)

Therefore

`int_0^infinity p_S(s)^(3/2) ds
 =2^(-1/2) int_0^infinity G(r)^(3/2) r^(-1/2) dr`.                (2.2)

The weight `r^(-1/2)` is decreasing. Under `0<=G<=2` and `int G=1`, the bathtub/rearrangement maximum is attained by `G=2` on `[0,1/2]`. Hence

`int p_S^(3/2)
 <=2^(-1/2) 2^(3/2) int_0^(1/2) r^(-1/2)dr
 =2sqrt(2)`.                                                       (2.3)

Taking the `2/3` power gives the particularly simple bound

`boxed: ||p_S||_(3/2) <=2.`                                       (2.4)

After scaling and reflection, for every `d!=0`,

`boxed: ||p_(d(Z+a)^2)||_(3/2) <=2 |d|^(-1/3).}`                  (2.5)

This estimate is uniform in the translation `a` and uses no support or moment assumption.

## 3. Main analytic compiler with shifts depending on the square variable

### Theorem 3.1 — `QFORM-HYPERBOLA-SQUARE-L3-COMPILER-v1`

Let `U,V,Z` be mutually independent cap-one real variables, and let `E` be any independent environment. Let `mu,d` be nonzero constants. Allow arbitrary measurable functions

`a=a(Z,E)`, `b=b(Z,E)`, `h=h(E)`, `R=R(E)`.

Define

`Q = 2mu [U+a(Z,E)][V+b(Z,E)] + d[Z+h(E)]^2 + R(E)`.              (3.1)

Then `Q` is absolutely continuous and

`boxed:
 ||p_Q||_(infinity,ess)
 <= 576^(1/3) |mu|^(-2/3)|d|^(-1/3)
 = 8.320335292207616... |mu|^(-2/3)|d|^(-1/3).`                  (3.2)

Consequently every interval `I` satisfies

`boxed:
 P(Q in I)
 <=576^(1/3)|mu|^(-2/3)|d|^(-1/3)|I|.`                          (3.3)

#### Proof

Fix `E=e`. Conditional on `Z=z,E=e`, the first two source variables remain genuinely independent translations of cap-one variables. Its conditional density is therefore bounded pointwise by the **same** function `K_mu`, regardless of the values of `a(z,e),b(z,e)`.

For a target `q`, integrate first over `Z`:

`p_(Q|E=e)(q)
 <= int h_Z(z) K_mu(q-R(e)-d[z+h(e)]^2) dz`.                       (3.4)

The right side is precisely the convolution of `K_mu` with the density of `d[Z+h(e)]^2`, evaluated at `q-R(e)`. Young's inequality with exponents `3` and `3/2`, followed by (1.11) and (2.5), gives

`||p_(Q|E=e)||_infinity
 <= 72^(1/3)|mu|^(-2/3) * 2|d|^(-1/3)
 =576^(1/3)|mu|^(-2/3)|d|^(-1/3).`                               (3.5)

The bound is independent of `e`; averaging over `E` proves (3.2). Absolute continuity follows from the conditional product densities and Tonelli. Equation (3.3) follows by integrating the density over `I`. QED.

**Why the exponents are critical.** For a general Young pair `p,q` with `1/p+1/q=1`, scaling would pay `|mu|^(-1/q)|d|^(-1/p)`. The determinant identity in Section 4 contains `mu^2 d`, and the hyperbola coefficient cancels exactly only at `p=3,q=3/2`. Thus the cubic compiler is not an arbitrary choice of norm.

## 4. Physical zero-pair + one Schur diagonal: determinant-only receiver

### Theorem 4.1 — `QFORM-ZEROPAIR-PRINCIPAL3-DET-L3-v1`

Let `A` be any real symmetric matrix and `X` an admissible independent cap-one product source. Affine terms may also be added. Suppose two **original physical coordinates** `i,j` satisfy

`A_ii=A_jj=0`, `mu=A_ij!=0`.                                      (4.1)

Let `H={i,j}`, `K=H^c`, and let

`B_H=A[H,H]=[[0,mu],[mu,0]]`.

Form the exact Schur complement

`S=A[K,K]-A[K,H] B_H^(-1) A[H,K]`.                               (4.2)

If some original coordinate `k in K` has

`d=S_kk!=0`,                                                       (4.3)

then the full ambient law has an essentially bounded density with

`boxed:
 ||p_(X^TAX)||_(infinity,ess)
 <=576^(1/3) |mu|^(-2/3)|d|^(-1/3).`                             (4.4)

The block determinant identity gives

`det A[H union {k},H union {k}]
 = det(B_H) d
 = -mu^2 d`.                                                       (4.5)

Therefore the scale collapses to the physical principal determinant alone:

`boxed:
 ||p_(X^TAX)||_(infinity,ess)
 <=576^(1/3)
   |det A[H union {k},H union {k}]|^(-1/3).}`                     (4.6)

All coefficients outside this physical triple, all signs, all same-bank curvature, all affine terms, all outside couplings, and all additional spectrum are unrestricted.

#### Proof

Complete the two original coordinates in `H` exactly. The quadratic polynomial becomes

`2mu[U+a(X_K)][V+b(X_K)] + X_K^T S X_K + affine`,                 (4.7)

where `U,V` are the original `i,j` variables and remain independent of `X_K`. Split `X_K=(Z,E)` with `Z=X_k`. Since `d=S_kk!=0`, complete this original scalar coordinate:

`X_K^T S X_K + affine
 = d[Z+h(E)]^2 + R(E)`.                                           (4.8)

The translations `a,b` in (4.7) may depend on both `Z` and `E`; Theorem 3.1 was designed to allow exactly that dependence. Applying it proves (4.4). Equation (4.5) is the standard Schur block determinant identity and yields (4.6). QED.

This is stronger in geometry than a smallest-singular-value principal-triple receiver: a highly ill-conditioned physical triple can still be paid at determinant scale. It is also nonperturbative in the ambient matrix: no outside coefficient is deleted as a small random error.

## 5. Assigned whole-copy decoupled-time estimate

Let

`D_3=|det A[H union {k},H union {k}]|`,
`H_0=576^(1/3) D_3^(-1/3)`.                                      (5.1)

Theorem 4.1 gives `||p_Q||_infinity<=H_0`. Let `Q'` be an independent copy of the **whole scalar output**. The difference density is the convolution `p_Q*p_(-Q')`, hence is also bounded by `H_0`.

For any real random variable with density cap `H`, layer cake gives

`E|Y|^(-1/2) <=2sqrt(2H)`.                                       (5.2)

Indeed `P(|Y|<r)<=min(1,2Hr)` and one splits the layer-cake integral at `sqrt(2H)`.

Using the angular Fourier/Riesz identity only at the level of the whole copy difference,

`int_R |t|^(-1/2)|phi_Q(t)|^2 dt
 =sqrt(2pi) E|Q-Q'|^(-1/2)`.                                     (5.3)

Combining (5.1)-(5.3),

`boxed:
 int_R |t|^(-1/2)|phi_Q(t)|^2 dt
 <=4sqrt(pi) 24^(1/3) D_3^(-1/6)
 =20.450566438865533... D_3^(-1/6).}`                             (5.4)

This satisfies the B03 assignment while respecting the sum/difference correction: the identity `|phi_Q(t)|^2=E exp(it(Q-Q'))` is invoked only for the **entire scalar output**. No coordinatewise `X-X'` is declared independent of `X+X'`, and no conditional density cap for a conjugate variable is used.

The crucial point is that linear one-copy small-ball scaling was proved first in (4.6); (5.4) is a valid consequence, not an invalid attempt to infer `L^infinity` merely from finite half-Riesz collision energy.

## 6. Concrete target-valid control family

Take a physical principal block

`A_0=[[0,1,0],[1,0,0],[0,0,1]]`.                                 (6.1)

Its eigenvalues are `{1,1,-1}` and its determinant has magnitude one. Any symmetric ambient extension that keeps this as a principal block lies in the owner target by Cauchy interlacing: it has two eigenvalues at least one and one eigenvalue at most minus one.

Theorem 4.1 applies regardless of every coupling from these three coordinates to the outside variables and gives

`boxed: ||p_Q||_(infinity,ess) <=576^(1/3)<8.321.`                (6.2)

The same family therefore obeys

`int |t|^(-1/2)|phi_Q(t)|^2dt <=20.451`.                          (6.3)

This is a control/application, not a claim that every owner-target matrix contains such a triple.

## 7. Scope, comparison, and next implication

- Full QFORM conjecture: **OPEN / NOT PROVED / NOT DISPROVED**.
- Full-target continuity: **OPEN**.
- New branch conclusion: absolute continuity plus an essentially bounded density and linear interval small-ball scaling.
- Continuity of the new branch is **not proved by this argument**; the proof uses density domination/Young rather than an `L^1` characteristic-function estimate.
- General rotations are not used to assert independence.
- Fragmented and unbounded-support cap-one inputs are allowed.
- The earlier zero-pair fractional-Riesz coarea theorem remains valid and is not duplicated; the new gain is the critical determinant-invariant `L^3 x L^(3/2)` sharpening and the exact constant `576^(1/3)`.

The current global account03/B20 frontier has moved to a fixed-hub / two-sided nested-rank-two packet. The first B03 use of the present theorem should be structural: whenever that recursion exposes a literal zero-diagonal hyperbolic pair and **any** nonzero physical Schur diagonal, the entire ambient law is immediately paid by the principal determinant (4.6), without requiring a residual rank-two minor or a residual half-Riesz theorem. The genuinely unpaid residue is therefore the nested rank-two chamber in which zero-pair Schur complements also suppress their physical diagonals; that residue still needs an aggregate time-integrated curvature mechanism rather than another local reciprocal-minor selection.

## 8. Source pins used in this run

- Previous account03/B03 r46: `yspennstate/math-open-problems@4da579fc8bcb3169099543b99ef99e1a829b3833`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B03/20260924T025916Z-account03-B03-QFORM-r46/REPORT.md`.
- Designated partner account04/B03 r3: `yspennstate/math-open-problems@19345adf8bb78f11da95a556d6fdcc47af957b19`, `proofnet24/QFORM-density/fleet-2026-09-22/account04/B03/20260924T021651Z-account04-B03-hyperbola-fourvolume-r3/REPORT.md`; its translated hyperbola half-power theorem is applied quantitatively in (1.8)/(1.11).
- Earlier zero-pair fractional-Riesz comparison source: `proofnet24/QFORM-density/fleet-2026-09-22/account01/B05/20260922T155803Z-account01-B05-qform13/REPORT.md`, read from repository state `c1d2f72c5206c55f41c229457b6407d9e23c0b20`.
- Fresh global frontier consumed before writing: account03/B20 r45, `yspennstate/math-open-problems@9e25c4e61cfe9aa9700419517b5d73b72a3e1fb1`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B20/20260924T031641Z-account03-B20-QFORM-auto11-r45/REPORT.md`.

Final controls/corrections are refreshed separately immediately before publication/writeback.
