SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B01, 2026-09-24T00:29:41Z.
attacking: the pivot-free small-diagonal branch by product-preserving double decoupling; obtain a dimension-free Holder concentration bound and signed-Fejer estimate, then combine it with the logarithmic physical-pair theorem to pay every remaining large physical edge.

# fleet03/B01 — double-decoupled small-diagonal concentration and large-edge payment

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `fleet03-B01-20260924T002941Z-auto11`  
Assignment: oscillatory replacement / quantitative inequalities and rigorous computations  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **NEW TARGET-LEVEL DISTRIBUTION-FUNCTION THEOREM / NEW LARGE-EDGE DENSITY BRANCH / FULL QFORM OPEN**

## 1. Exact target and refreshed correction boundary

Let `X=(X_1,...,X_n)` have independent real coordinates with probability densities `0<=f_i<=1`, and let `A` be real symmetric. The owner target assumes at least three eigenvalues of `A` have absolute value at least one, equivalently `s_3(A)>=1`, and asks for one universal bound on the density of `Q=X^T A X`.

No Gaussian, moment, compact-support, connected-support, log-concavity, iid, or spectral-coordinate independence assumption is introduced below. Every random vector split is a split of the original independent coordinates. Singular-vector calculations are used only for deterministic coefficient norms after conditioning; no rotated random coordinates are declared independent.

Immediately before publication the control branch was refreshed at

`yspennstate/math-research-brain@241a2237302d7069aa9b25660a73075266f866c6`,


The full conjecture remains OPEN.

## 2. Source-pinned inputs actually used

### 2.1 Designated partner fleet04/B01: signed Fejer interface

Canonical mathematics:

`yspennstate/math-open-problems@a3693ed6d50e8e4143b2f33bf997c5de2cb52d79`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B01/20260922T141507Z-b01-qform-fejer-r1/REPORT.md`.

For a probability law `mu` with characteristic function `phi`, fleet04/B01 defines

`D_T mu(y)=(1/(2*pi)) int_{-T}^T (1-|t|/T) Re(exp(-ity) phi(t)) dt`.

It proves that `D_T mu` is convolution with the nonnegative Fejer kernel

`F_T(u)=(1-cos(Tu))/(pi*T*u^2)`, with `F_T(0)=T/(2*pi)`,

and that whenever `mu` has a bounded density,

`||p_mu||_infinity = sup_{T>0,y} D_T mu(y)`.

I apply this result below at two actual inequalities: first to turn the new small-diagonal concentration estimate into a quantitative signed-frequency bound, and then to transfer the new large-edge density payment to a uniform Fejer bound.

### 2.2 Logarithmic physical-pair envelope

Canonical mathematics:

`yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`

`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.

For an invertible indefinite original-coordinate `2x2` block `B`, write

`D=|det B|`, `kappa=sigma_min(B)`.

After completing that pair, if the remaining scalar random variable is `R`, the source proves for every `r>0`

`p_Q(t) <= 2*sqrt(2)/r + D^(-1/2) E log_+(2r^2/(kappa*|t-R|))`.       (2.1)

It also proves the square-root small-ball compiler: if

`sup_t P(|R-t|<rho)<=H sqrt(rho)`,

then

`||p_Q||_infinity <=4 sqrt(2H) (D*kappa)^(-1/4)`.                 (2.2)

The pair shifts may depend arbitrarily on the same remainder variables.

### 2.3 Product linear-form density bound

I use the programme-standard product linear-form theorem in exactly the form used and proved into the current tree by fleet02/B04, canonical report

`yspennstate/math-open-problems@dfe442ee899867f5677e5ced85a196eca922fe64`.

If independent real variables have densities bounded by one and `c` is a deterministic coefficient vector, then

`||p_(c dot Z)||_infinity <= sqrt(2)/||c||_2`.                    (2.3)

The same statement applies to coordinatewise differences `Z_i-Z_i'`, because their densities are still bounded by one.

### 2.4 Previous B01 high-diagonal payment

The immediately preceding B01 theorem is source-pinned at

`yspennstate/math-open-problems@319a41e1179abcd7827abc2a54b117b4d1276dcf`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B01/fleet03-B01-20260923T233049Z-auto11/REPORT.md`.

It proves that under `s_3(A)>=1`, every nonzero literal diagonal pivot `a=A_ii` satisfies

`||p_Q||_infinity <137 |a|^(-1/2)`.                              (2.4)

Hence the whole branch `max_i |A_ii|>=1/64` is already paid by `<1096`.

## 3. Preserve the phase-aligned pointwise counterexample

The false pointwise mechanism stays false. Fix any `s!=0` and `eta in (0,pi/2)`. The set

`E={x: dist(s x^2,2*pi*Z)<=eta}`

has infinite Lebesgue measure: near the positive roots `sqrt(2*pi*k/|s|)` its component lengths are comparable to a constant times `k^(-1/2)`, and the sum diverges. Choose a finite union `E_0 subset E` of total measure one and put `f=1_(E_0)`. Then `f` is a probability density with `0<=f<=1`, while

`Re E exp(i s X^2) >= cos(eta)`.

Thus no positive law-uniform pointwise power decay in `|s|` can be recovered. The argument below instead passes to a distribution-function estimate after two original-coordinate differences.

## 4. A deterministic cross-cut lemma from a small physical diagonal

### Lemma 4.1 — `QFORM-SMALLDIAG-CROSSCUT-v1`

Let `A` be real symmetric, put `s=||A||_op>0`, and assume

`max_i |A_ii| <= theta*s`, with `0<=theta<1`.                     (4.1)

Then there is a literal partition of the original coordinates

`[n]=I disjoint_union J`

such that for the physical cross block `B=A[I,J]`,

`||B||_op >= (1-theta)s/2`.                                     (4.2)

#### Proof

Write `A=D+O`, where `D=diag(A)` and `O` has zero diagonal. Then

`||O||_op >= ||A||_op-||D||_op >= (1-theta)s`.                  (4.3)

For a sign vector `eps in {+1,-1}^n`, let `S=diag(eps)` and define

`C_eps=(O-S O S)/2`.                                            (4.4)

If `I={i:eps_i=+1}` and `J={i:eps_i=-1}`, then after ordering the coordinates by this partition,

`C_eps=[[0,B],[B^T,0]]`,

so `||C_eps||_op=||B||_op`. Because `O` has zero diagonal and independent random signs satisfy `E eps_i eps_j=0` for `i!=j`,

`E_eps S O S=0`, and hence `E_eps C_eps=O/2`. Convexity of the operator norm gives

`E_eps ||C_eps||_op >= ||E_eps C_eps||_op=||O||_op/2`.          (4.5)

Some physical cut therefore satisfies (4.2). QED.

This lemma aggregates many weak physical coefficients before selecting anything. It does not claim a single large matrix entry or a fixed-size good minor.

## 5. Double decoupling: the full quadratic form reduces to one bilinear small-ball event

Fix any original-coordinate cut `I,J` and write the corresponding independent coordinate banks as `Y=X_I`, `Z=X_J`. Thus

`Q(Y,Z)=F(Y)+2Y^T BZ+G(Z)`                                     (5.1)

for arbitrary same-bank quadratic functions `F,G`.

Let `K` be an interval of length `h>0`, and put

`p=P(Q(Y,Z) in K)`.

Take independent copies `Y',Z'`. Conditional Cauchy-Schwarz in the `Y` bank gives

`p^2 <= P(|Q(Y,Z)-Q(Y',Z)|<=h)`.                                (5.2)

For fixed `Y,Y'`, let

`r(Y,Y')=P_Z(|Q(Y,Z)-Q(Y',Z)|<=h)`.

Applying Cauchy-Schwarz once more and using two events of width `h`,

`p^4 <= P(|Delta(Z)-Delta(Z')|<=2h)`,                            (5.3)

where `Delta(z)=Q(Y,z)-Q(Y',z)`. The same-bank `F` part cancels in the second difference and the `G` part had already cancelled in the first difference. Exactly,

`Delta(Z)-Delta(Z')=2(Y-Y')^T B(Z-Z')`.                         (5.4)

Therefore, with

`U=Y-Y'`, `V=Z-Z'`,

we obtain the exact product-preserving reduction

`boxed: p^4 <= P(|U^T B V|<=h).`                                (5.5)

The coordinates of `U` and of `V` are independent, the two banks are independent of one another, and every difference coordinate still has density at most one because

`p_(X_i-X_i')(u)=int f_i(x) f_i(x-u) dx <= int f_i(x) dx=1`.    (5.6)

No conditional projected-density claim is used.

## 6. A one-singular-direction bilinear small-ball estimate

### Lemma 6.1 — `QFORM-BILINEAR-SMALLBALL-ONE-SINGULAR-v1`

Let `U,V` be independent product vectors whose scalar coordinate densities are bounded by one. Let `B` be deterministic with largest singular value `sigma=||B||_op>0`. Then for every `h>0`,

`P(|U^T B V|<=h) <= 4 sqrt(2/e) sqrt(h/sigma)`,                 (6.1)

where the right side may of course be capped at one.

#### Proof

Condition on `U`. By (2.3), the linear form in `V` has density at most

`sqrt(2)/||B^T U||_2`.

Hence

`P(|U^T B V|<=h | U)
 <= min(1, 2 sqrt(2) h / ||B^T U||_2)`.                         (6.2)

Choose deterministic top singular vectors `u,v` so that `Bv=sigma u`. Then

`||B^T U||_2 >= sigma |u dot U|`.                               (6.3)

Set `W=u dot U`. Again by (2.3), since `||u||_2=1`, the scalar `W` has a density bounded by

`K=sqrt(2)`.                                                     (6.4)

Put

`eta=2 sqrt(2) h/sigma`, `x=2K eta=8h/sigma`.                  (6.5)

For every probability density `g<=K`, the symmetric decreasing function `min(1,eta/|w|)` is maximized by the cap-saturated centered interval. Thus, when `x<=1`,

`E min(1,eta/|W|)
 <=2K eta [1+log(1/(2K eta))]
 =x(1+log(1/x)).`                                               (6.6)

For `0<x<=1`, writing `x=e^{-q}` shows

`sqrt(x)(1+log(1/x))=e^{-q/2}(1+q) <=2/sqrt(e)`.                (6.7)

Hence (6.6) is at most `(2/sqrt(e))*sqrt(x)`. For `x>=1`, the probability is at most one, which is also at most `(2/sqrt(e))*sqrt(x)`. Substituting `x=8h/sigma` yields (6.1). QED.

## 7. Main new distribution-function theorem for the pivot-free branch

### Theorem 7.1 — `QFORM-SMALLDIAG-DOUBLE-DECOUPLED-HOLDER-v1`

Let `A` be real symmetric, `s=||A||_op>0`, and suppose

`max_i |A_ii| <= theta*s`, `0<=theta<1`.                        (7.1)

For every independent cap-one input law and every interval `K` of length `h>0`,

`boxed:
 P(X^T A X in K)
 <= min{1, C_theta (h/s)^(1/8)},
 C_theta=2^(3/4) e^(-1/8) (1-theta)^(-1/8).
}`                                                                  (7.2)

#### Proof

Choose the physical cut from Lemma 4.1, so

`sigma=||A[I,J]||_op >=(1-theta)s/2`.                            (7.3)

Apply (5.5) and Lemma 6.1:

`p^4 <=4 sqrt(2/e) sqrt(h/sigma)`.                              (7.4)

Taking fourth roots and using (7.3),

`p <=[4 sqrt(2/e)]^(1/4) [2h/((1-theta)s)]^(1/8)
   =2^(3/4)e^(-1/8)(1-theta)^(-1/8)(h/s)^(1/8)`.               (7.5)

QED.

### Target normalization

In the current unpaid branch from the preceding B01 run,

`max_i |A_ii|<1/64`, while `s_3(A)>=1` implies `s=||A||_op>=1`.

Thus (7.1) holds with `theta=1/64`, and

`boxed:
 sup_{intervals K, |K|=h} P(Q in K)
 <1.488 h^(1/8).
}`                                                                  (7.6)

The exact computed constant is

`C_(1/64)=1.487101509895742...`.

This is a target-level statement for the entire small-diagonal branch. It does not by itself imply an `L^infinity` density; a Frostman-type exponent `1/8` is weaker than the required linear small-ball bound.

## 8. Actual designated-partner application: signed Fejer growth

Fleet04/B01 gives the exact positive-kernel representation

`D_T mu(y)=int F_T(y-x) dmu(x)`,

with

`F_T(u)<=min(T/(2*pi), 2/(pi*T*u^2))`.                           (8.1)

Assume the interval concentration estimate

`mu(I)<=K |I|^alpha`, with `alpha=1/8`.                          (8.2)

Split the line into `|u|<=1/T` and the dyadic shells

`2^m/T<|u|<=2^(m+1)/T`, `m>=0`.

The central contribution is at most

`K T^(1-alpha) 2^alpha/(2*pi)`.                                 (8.3)

The `m`-th shell is at most

`K T^(1-alpha) (2/pi) 2^(2alpha) 2^{-(2-alpha)m}`.              (8.4)

Summing gives

`D_T mu(y)
 <=K C_F(alpha) T^(1-alpha)`,                                   (8.5)

where

`C_F(alpha)=2^alpha/(2*pi)
 +(2/pi) 2^(2alpha)/(1-2^{-(2-alpha)}).`                         (8.6)

For `alpha=1/8`,

`C_F(1/8)=1.214391144769096...`.

Combining with (7.6) gives the actual designated-partner inequality

`boxed:
 sup_y D_T law(Q)(y) <1.806 T^(7/8)
}`                                                                  (8.7)

for every `T>0` throughout the target branch `max_i|A_ii|<1/64`.

The exact constant from the computation is `1.805922904990142...`.

This is a genuine signed/averaged-frequency replacement for the false pointwise Fresnel estimate. It is weaker than the desired `O(1)` Fejer bound by the explicit growth exponent `T^(7/8)`; that remaining exponent is now visible rather than hidden inside an invalid pointwise estimate.

## 9. General eighth-root compiler for the logarithmic physical pair

The new Holder estimate can also be fed back into the logarithmic pair theorem.

Suppose the remainder `R` in (2.1) satisfies for some `K>0`

`sup_t P(|R-t|<rho) <=K rho^(1/8)`.                              (9.1)

By layer cake,

`E log_+(a/|t-R|)
 =int_0^infinity P(|t-R|<a e^{-v}) dv
 <=8K a^(1/8)`.                                                  (9.2)

Taking `a=2r^2/kappa` in (2.1) gives

`p_Q(t)
 <=A_0/r+B_0 r^(1/4)`,                                          (9.3)

where

`A_0=2sqrt(2)`,

`B_0=D^(-1/2) 8*2^(1/8) K kappa^(-1/8)`.                        (9.4)

The exact minimizer is

`r_*=(4A_0/B_0)^(4/5)`,                                         (9.5)

so (9.3) is finite for every positive `D,kappa,K`. This extends the source pair-log compiler from a square-root remainder small-ball estimate to the eighth-root estimate produced by Theorem 7.1.

## 10. New target-level large-physical-edge payment

### Theorem 10.1 — `QFORM-SMALLDIAG-LARGEEDGE-PAIRLOG-PAYMENT-v1`

Assume the owner target `s_3(A)>=1` and

`max_i |A_ii|<1/64`.                                            (10.1)

If some literal off-diagonal coefficient obeys

`|A_ij|>=1/32`,                                                  (10.2)

then `Q=X^T A X` has an essentially bounded density satisfying

`boxed: ||p_Q||_infinity <463.`                                  (10.3)

Consequently, by fleet04/B01,

`boxed: sup_{T>0,y} D_T law(Q)(y)<463.`                          (10.4)

#### Proof

Take the actual physical pair

`B=[[A_ii,A_ij],[A_ij,A_jj]]`.

Let `theta=1/64`, `beta=1/32`. Because the pair diagonals have magnitude below `theta` while `|A_ij|>=beta`, the pair is indefinite and

`D=|det B| >= beta^2-theta^2=3/4096`,                            (10.5)

while Weyl's inequality against `[[0,A_ij],[A_ij,0]]` gives

`kappa=sigma_min(B)>=beta-theta=1/64`.                          (10.6)

Complete this original-coordinate pair. Let `S` be its Schur complement on the remaining original coordinates. There is an exact decomposition

`A=diag(0_2,S)+R_2`, with `rank(R_2)<=2`.                        (10.7)

Rank-two singular-value interlacing therefore gives

`||S||_op=s_1(S)>=s_3(A)>=1`.                                   (10.8)

Let the Schur critical-value random variable be `R=Z^T S Z` (affine terms could be retained without changing either branch below).

**Case 1: a residual diagonal is at least `1/64`.**

Condition all other original coordinates. For an interval of radius `rho`, the inverse image under one scalar quadratic with coefficient `d`, `|d|>=1/64`, has total length at most `2sqrt(2rho/|d|)`. Hence

`sup_t P(|R-t|<rho) <= H sqrt(rho)`,

with

`H=2sqrt(2/(1/64))=16sqrt(2)=22.6274169979...`.                 (10.9)

Using (2.2), (10.5), and (10.6),

`||p_Q||_infinity
 <=4sqrt(2H)(D*kappa)^(-1/4)
 <=462.6442258483... <463.`                                     (10.10)

**Case 2: every residual diagonal is below `1/64`.**

By (10.8), Theorem 7.1 applies to `S` with `theta=1/64`. For an interval of radius `rho`, length `2rho`,

`sup_t P(|R-t|<rho)
 <=K rho^(1/8)`,                                                  (10.11)

where

`K=2^(1/8) C_(1/64)=1.621695695799...`.                         (10.12)

Apply the eighth-root compiler (9.3)-(9.5). At the worst permitted values in (10.5)-(10.6),

`B_0<=879.1843400198...`,

`r_*=0.03073406693478...`,

and

`||p_Q||_infinity <=460.1452731179... <461.`                    (10.13)

Thus both residual branches satisfy (10.3). The pair-log source gives absolute continuity and essential boundedness; continuity is not obtained. Finally the designated partner's exact Fejer equivalence gives (10.4). QED.

## 11. Structural synthesis with the preceding B01 run

The previous B01 theorem (2.4) pays

`max_i |A_ii|>=1/64`

by the universal bound `<1096`.

Theorem 10.1 now pays the complementary small-diagonal state whenever

`max_{i!=j}|A_ij|>=1/32`

by `<463`.

Therefore, subject to the already source-pinned supporting theorems, every still-unpaid target matrix may now be assumed to satisfy the literal entrywise collar

`boxed:
 max_i |A_ii|<1/64,
 max_{i!=j}|A_ij|<1/32,
 s_3(A)>=1.
}`                                                                  (11.1)

This is not a low-rank or small-operator-norm assumption. The matrix can have large operator norm through many weak entries. Rather, (11.1) identifies the genuinely diffuse physical-coordinate regime in which the next proof must aggregate many weak couplings instead of inverting one local coefficient.

Theorem 7.1 still gives that entire diffuse regime the universal concentration estimate `<1.488 h^(1/8)` and the partner-fed signed-Fejer estimate `<1.806 T^(7/8)`.

## 12. Deterministic and numerical checks

The sibling checker verifies:

1. `C_(1/64)=1.487101509895742... <1.488`;
2. the dyadic Fejer factor gives `1.805922904990142... <1.806`;
3. for `beta=1/32`, `D_min=3/4096` and `kappa_min=1/64`;
4. the square-root residual pair-log branch is `462.6442258482... <463`;
5. the eighth-root residual branch is `460.1452731179... <461` at its exact optimizer;
6. an exhaustive sign-cut computation on a fixed symmetric zero-diagonal matrix satisfies `E C_eps=O/2` and `E||C_eps||>=||O||/2`;
7. seeded finite-dimensional tests satisfy `s_1(S)>=s_3(A)` after a two-coordinate Schur complement;
8. seeded direct calculations verify the exact double-difference identity (5.4).

The random finite tests are diagnostics only; the proof is the algebra above.

## 13. What remains

The first unpaid B01 implication is now

`QFORM-DIFFUSE-ENTRY-COLLAR-FEJER-SATURATION-v1`:

> Under `s_3(A)>=1`, `|A_ii|<1/64`, and `|A_ij|<1/32` for every `i!=j`, improve the universal `h^(1/8)` concentration / `T^(7/8)` signed-Fejer growth to an `O(h)` small-ball bound or an `O(1)` signed-Fejer bound, using aggregate original-coordinate structure before any reciprocal local coefficient is selected.

The entrywise collar is deliberately compatible with known diffuse star/rank-one-bank stress families; no fixed-size physical minor is asserted. The natural next mechanisms are grouped-hub/ridge/Fresnel aggregation or an iteration of the double-difference estimate that spends the extra two large singular directions without taking absolute values too early.

## 14. Continuity and status

- `QFORM-SMALLDIAG-DOUBLE-DECOUPLED-HOLDER-v1`: distribution-function statement only; it does not establish a density and therefore does not establish continuity.
- `QFORM-SMALLDIAG-LARGEEDGE-PAIRLOG-PAYMENT-v1`: establishes an essentially bounded density with bound `<463`; continuity is not proved by the logarithmic averaging argument.
- Full unrestricted QFORM: **OPEN**.
- Full continuous-density conclusion: **OPEN**.
- Native learned-memory ingestion: not established; execution remains `WITHOUT_VERIFIED_BRAIN`.

No scheduler/task state, email/push setting, permissions, public-release state, cross-account authentication, paid model/API call, or remote workflow was changed.
