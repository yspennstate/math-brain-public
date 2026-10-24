SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B16, 2026-09-24T09:52:33Z.
attacking: QFORM-OVERLAPPING-PROJECTEDSQUARE-RANK2-PREABSOLUTE-v2 by keeping a dependent two-dimensional same-bank projection intact through a square plus hyperbolic product, and using both its true joint projection cap and a true scalar marginal cap before nonlinear integration.

# account03/B16 r46 — shared-bank square-hyperbolic projection-product theorem

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T095233Z-account03-B16-QFORM-auto11-r4`  
Role: Projection-product interaction  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: `NEW SUPPORTING THEOREM + PREVIOUS B16 OVERLAP FRONTIER CLOSED + PARTNER APPLIED / FULL QFORM OPEN`  
Regularity: the theorem below proves an essentially bounded density. Continuity in this scope is not proved here; full-target continuity remains open.

## 1. Correction boundary and exact advance

The unrestricted owner target remains OPEN / NOT PROVED / NOT DISPROVED. No post-rotation independence, conditional-density cap, arbitrary-joint indefinite coarea estimate, compact support, moments, log-concavity, or law-uniform pointwise oscillatory decay is used.

The preceding account03/B16 run, source

`yspennstate/math-open-problems@fb28047260afcaa64675fef64af6457e2815af2d`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B16/20260924T085813Z-account03-B16-QFORM-auto11-r3/REPORT.md`,

closed only rank-one shared overlap and left the state where a square scalar and the transverse hyperbolic scalar are two genuinely dependent projections of the same original product bank. The present run closes the canonical square-hyperbolic normal form of exactly that state.

The analytic inputs are source-valid:

1. The actual two-dimensional bounded-density projection theorem, as pinned and applied in account04/B16 r4,
   `yspennstate/math-open-problems@7f2bb2d330022b09a6af6e39ab09d054caeaa346`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account04/B16/20260924T041516Z-account04-B16-QFORM-r4/REPORT.md`:
   every orthonormal two-dimensional projection of a cap-one product law has joint density cap at most `2`.
2. The source-pinned scalar projection bound used in the preceding B16 report:
   for a unit scalar projection of a cap-one product law, the density cap is at most `sqrt(2)`.

The new argument does **not** infer a nonlinear bound from the joint cap alone. It simultaneously uses the joint cap of `(S,T)`, the genuine one-dimensional marginal cap of `S`, and independence of a third original-coordinate bank.

## 2. A normalized nonlinear kernel theorem

Let `(S,T)` be an arbitrary dependent pair with joint density `h`, and assume

`0 <= h(s,t) <= M`,

while the true marginal density

`m(s)=integral h(s,t) dt`

satisfies

`0 <= m(s) <= K`, `integral m=1`.

Let `V` be independent of `(S,T)`, with density `g` satisfying `0<=g<=1`. Put

`F=S^2+2TV`.

### Theorem 2.1 — `QFORM-SHAREDBANK-SQUAREHYPERBOLIC-KERNEL-v1`

The law of `F` has an essentially bounded density and

`boxed:
 ||p_F||_infinity
 <= C1 sqrt(MK) + C2 M^(3/4) K^(-1/4),`

where

`C1=sqrt(2)(5+2 log 2)=9.03158409880257...`,
`C2=sqrt(12)=3.46410161513775...`.

### Proof

For fixed `q`, Fubini and the change of variables in the independent scalar `V` give, for almost every `q`,

`p_F(q)
 = (1/2) integral_R integral_R
     h(s,t) g((q-s^2)/(2t)) / |t| dt ds.`                 (2.1)

Define

`k_s(w)=integral h(s,t) g(w/t)/|t| dt`.                    (2.2)

We establish two complementary bounds on this exact kernel.

#### Power bound

For any `R>0`, split at `|t|=R`. On `|t|<=R`, use `h<=M` and substitute `y=w/t`:

`integral_|t|<=R h(s,t)g(w/t)/|t| dt
 <= M integral_|y|>=|w|/R g(y)/|y| dy
 <= M R/|w|.`                                             (2.3)

On `|t|>R`, use `g<=1` and the actual marginal mass `m(s)`:

`integral_|t|>R ... <= m(s)/R.`                            (2.4)

Optimizing `MR/|w|+m(s)/R` gives

`boxed: k_s(w) <= 2 sqrt(M m(s)/|w|).`                     (2.5)

#### Logarithmic bound

Set `R=m(s)/M` when `m(s)>0`. The large part is at most `M`. For the small part, the same substitution gives

`M integral_|y|>=A g(y)/|y| dy`,
`A=|w|M/m(s).`                                             (2.6)

Among all probability densities bounded by one, the last weighted tail is maximized by filling the points closest to `+/-A`; hence

`integral_|y|>=A g(y)/|y| dy
 <= 2 log(1+1/(2A)).`                                      (2.7)

Therefore

`boxed:
 k_s(w) <= M + 2M log(1+m(s)/(2M|w|)).`                    (2.8)

Now put

`d=|q-s^2|`, `delta=K/M`.

Because `w=(q-s^2)/2`, equations (2.1), (2.5), (2.8) give the two pointwise integrands

`(1/2)k_s(w) <= sqrt(2M m(s)/d)`,                          (2.9)

and

`(1/2)k_s(w)
 <= M/2 + M log(1+m(s)/(Md)).`                             (2.10)

We use (2.10) on `d<=delta` and (2.9) on `d>delta`.

Two elementary one-dimensional facts are needed. Uniformly in `q` and `eta>0`,

`|{s: |q-s^2|<=eta}| <= 2 sqrt(2 eta).`                    (2.11)

Also layer cake applied to (2.11) gives

`integral_|q-s^2|<=delta log(delta/|q-s^2|) ds
 <= 4 sqrt(2 delta).`                                      (2.12)

Since `m(s)<=K`, on the near region

`log(1+m(s)/(Md)) <= log(1+delta/d)
                  <= log 2 + log(delta/d).`                (2.13)

Using (2.11)-(2.13),

`N(q)
 <= M sqrt(2delta) [1+2 log2+4]
 = C1 sqrt(MK).`                                           (2.14)

For the far region, Cauchy-Schwarz and `integral m=1` yield

`F_far(q)
 <= sqrt(2M)
    [integral_{d>delta} ds/d]^(1/2).`                       (2.15)

The reciprocal quadratic tail satisfies the uniform estimate

`boxed:
 sup_q integral_|q-s^2|>delta ds/|q-s^2|
 <= 6 delta^(-1/2).`                                       (2.16)

For completeness, scale to `delta=1`. If `q<=-1`, the full integral is at most `pi`; if `-1<q<0`, writing `a=-q`, either `a<=1/2` and the excluded interval leaves a tail bounded by `2sqrt(2)`, or `a>1/2` and the full Cauchy integral is below `pi sqrt(2)`. At `q=0` the value is `2`. For `0<q<=1`,

`H(q)=2/sqrt(q) artanh sqrt(q/(q+1)) < 3.`                  (2.17)

For `1<q<=4`,

`H(q)=2/sqrt(q)[artanh sqrt(1-1/q)+artanh sqrt(q/(q+1))]
 <6.`                                                       (2.18)

For `q>=4`, each `artanh` is bounded by the corresponding logarithm, giving

`H(q)<=q^(-1/2) log(16q(q+1))<3.`                           (2.19)

This proves (2.16). Substitution into (2.15) gives

`F_far(q)
 <= sqrt(12) M^(3/4)K^(-1/4)
 = C2 M^(3/4)K^(-1/4).`                                    (2.20)

Adding (2.14) and (2.20) proves the theorem. QED.

The proof retains dependence between `S` and `T` throughout. The use of `m(s)` is essential: replacing all source information by only `h<=M` would lose the large-`|t|` integrability and is exactly the invalid shortcut excluded by the owner correction.

## 3. Scale, shear, and translated outside baggage

Let `(S,T)` satisfy the same caps `M,K`. Let `V` be independent with density cap `L`. Let `a,b` be nonzero. For arbitrary real `c,d,alpha,beta,r`, define

`Q=a(S+d)^2+2b(T+cS+alpha)(V+beta)+r`.                       (3.1)

The map `(S,T)->(S+d,T+cS+alpha)` has Jacobian one; it preserves the joint cap `M` and the first-coordinate marginal cap `K`. Scale

`x=sqrt(|a|)(S+d)`,
`z=(|b|/L)(T+cS+alpha)`,
`v=L(V+beta)`.

After harmless output and coordinate sign changes, Theorem 2.1 applies. Thus:

### Theorem 3.1 — `QFORM-SHAREDBANK-SQUAREHYPERBOLIC-PROJECTIONPRODUCT-v1`

`boxed:
 ||p_Q||_infinity
 <= C1 [LMK/(|ab|)]^(1/2)
  + C2 (LM)^(3/4)K^(-1/4)|a|^(-1/4)|b|^(-3/4).`             (3.2)

The same estimate holds if `c,d,alpha,beta,r` are measurable functions of an additional original-coordinate bank `W` disjoint from all sources above: condition on `W`, apply (3.2), and average. No conditional projection cap is inferred; all caps are for unconditional projections of their own disjoint product banks before conditioning.

## 4. Actual product-projection corollary and strict owner-target family

Let `U` be an orthonormal two-dimensional projection of one original-coordinate product bank and write

`(S,T)=U^T X_I`.

Let `V` be a unit scalar projection of a disjoint original-coordinate product bank. The actual projection theorems give

`M<=2`, `K<=sqrt(2)`, `L<=sqrt(2)`.                           (4.1)

Therefore (3.2) gives

`boxed:
 ||p_Q||_infinity
 <= 18.06316819760514 |ab|^(-1/2)
  + 6.928203230275509 |a|^(-1/4)|b|^(-3/4).`                (4.2)

In particular, for the genuinely shared-bank packet

`Q_*=S^2+2TV`,                                                (4.3)

where **no independence between `S` and `T` is assumed**, the effective matrix in `(S,T,V)` is

`B_*=[[1,0,0],[0,0,1],[0,1,0]]`,                             (4.4)

with exact spectrum

`{-1,1,1}`.                                                   (4.5)

Thus this is a strict instance of the owner's three-large-eigenvalue target, and for every admissible original-coordinate product law,

`boxed: ||p_(Q_*)||_infinity < 24.992.`                       (4.6)

This closes the canonical nonlinear state identified as the first unpaid B16 implication in r45: the projected square scalar and the transverse hyperbolic scalar may be genuinely dependent projections of the same product bank. It does **not** prove that every remaining full QFORM matrix can already be reduced to the normal form (3.1).

## 5. Designated account04/B16 theorem applied to a new strict-target inequality

Use the completed account04/B16 r4 definite projected-plane result:

`||p_Q||_infinity <= 2pi/sqrt(|det H|)`                      (5.1)

when, after conditioning on disjoint sources, an orthogonal 2D projection enters through a definite matrix `H`.

Let `R` be a unit scalar projection of one product bank and let `Z=(Z1,Z2)` be an orthonormal 2D projection of a disjoint bank. Consider

`Q_partner=-3R^2+4RZ1+3Z1^2+2Z2^2.`                         (5.2)

Conditioning on `R` leaves the definite plane

`H=diag(3,2)`, `det H=6`,                                    (5.3)

so the partner theorem gives the actual inequality

`boxed:
 ||p_(Q_partner)||_infinity <= 2pi/sqrt(6)
 =2.565099660323728... .`                                    (5.4)

The effective matrix is

`[[-3,2,0],[2,3,0],[0,0,2]]`,                                (5.5)

whose eigenvalues are exactly

`{-sqrt(13),2,sqrt(13)}`.                                    (5.6)

Hence this is again a genuine owner-target family, not a two-eigenvalue control.

## 6. Exact frontier after this run

The new theorem pays the previously unpaid **two-dimensional same-bank overlap normal form** whenever the packet can be written, after source-preserving shear and conditioning on disjoint baggage, as

`a(S+d)^2+2b(T+cS+alpha)(V+beta)+r`,                          (6.1)

with `(S,T)` an orthogonal 2D projection of one product bank and `V` a scalar projection of another disjoint bank.

The first remaining B16 implication is now structural rather than this nonlinear integral:

`QFORM-SHAREDBANK-NORMALFORM-OR-EXIT-COMPILER-v1`:

> In the live exact-rank-three / small-pivot shared-bank collar, prove that the coefficient geometry forces either (i) a source-preserving representation of the form (6.1) with quantitatively nontrivial `a,b`; (ii) the account04 definite projected-plane exit; (iii) the completed source-preserving phase-aligned exit; or (iv) another already-paid fresh-source crossing. If not, identify the residual coefficient invariant that obstructs all four.

That structural reduction has **not** been proved here. Full QFORM and full-target continuity therefore remain OPEN.

## 7. Deterministic checks

The committed checker verifies the constants in (4.2), the `<24.992` strict-family bound, the strict spectra in (4.5) and (5.6), and a dense numerical regression of the reciprocal-tail function underlying (2.16). The numerical scan is only a regression check; the proof of (2.16) above is analytic.
