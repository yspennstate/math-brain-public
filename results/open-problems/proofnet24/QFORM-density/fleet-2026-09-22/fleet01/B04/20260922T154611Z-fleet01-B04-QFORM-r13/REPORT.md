# fleet01/B04 — quarter-Riesz determinant aggregation and an indefinite-face/cross splice

**Run:** `20260922T154611Z-fleet01-B04-QFORM-r13`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Product Fourier rearrangement  
**Outcome:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREMS_PROVED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and compact conditional end-to-end route

The full target remains open: for every dimension, every family of independent real random variables with one-dimensional densities bounded by one, and every real symmetric matrix `A` with at least three eigenvalues of modulus at least one, prove that `X^T A X` has an essentially bounded density with one universal constant, or give a valid target-level counterexample. Continuity is an additional requested conclusion and is not established by the theorem below.

The present route is:

1. keep all work in original product coordinates;
2. use a physical indefinite two-coordinate face to generate a deterministic quarter-power conditional density singularity;
3. pay that singularity not with a scalar square and not with a selected local minor, but with a **quarter-Riesz potential** of the full Schur residual;
4. derive that potential directly from the completed regularized-determinant/product-Fourier estimate using an aggregate elementary-symmetric cross currency `E_k`;
5. conclude a dimension-free density bound whenever the residual supplies either a leverage-valid aggregate rank-one cross currency or an unconditional aggregate rank-two cross currency.

This pays a genuine analytic splice that was missing from the preceding B04 run. The remaining issue is structural extraction from the sole three-large-eigenvalue hypothesis.

No law-uniform scalar pointwise Fresnel decay, post-rotation independence, naive fiber supremum, generic conditional-density cap, fixed principal-minor dichotomy, finite fragment-count reduction, or absolute phase-Wiener bound is used.

## 2. Source-pinned dependencies actually consumed

### 2.1 Completed fleet02/B04 aggregate determinant result

Named partner actually applied:

`yspennstate/math-open-problems@69c4571401b4376ffb84ad34aff2a748330acf8a`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B04/B04-20260922T152028Z-qform-r11/REPORT.md`.

For a physical residual cross block `C` with squared singular values `s_j^2`, write

`E_k(C)=e_k(s_1^2,s_2^2,...)`.

The completed partner argument, based on the regularized-determinant theorem, gives for `1<=q<=2`

`|phi_R(t)| <= det(I+kappa_q t^2 C C^T)^(-1/(4q)),`             (2.1)

`kappa_q=2q/(pi^2 e^2),`

with the physical range-leverage hypothesis `max diag P_range(C)<=q/2` when `q<2`, and with no leverage hypothesis when `q=2`. Expanding the determinant gives the aggregate envelope

`|phi_R(t)| <= [1+kappa_q^k E_k(C)t^(2k)]^(-1/(4q)).`           (2.2)

The partner used (2.2) with an additional original-coordinate square. Here I spend the same aggregate envelope through a different fractional-potential mechanism.

### 2.2 Completed fleet02/B04 product rearrangement endpoint

Source:

`yspennstate/math-open-problems@b7168a1b0b52fbf69705170ff9795435efeb849f`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B04/fleet02-B04-20260922T122057Z-01c809a1/REPORT.md`.

For independent `U,V` with densities bounded by one,

`p_{UV}(s) <= 4 log(1+1/(2 sqrt(|s|))),  s!=0.`                 (2.3)

I apply this directly to the exact zero-diagonal indefinite-face endpoint in Section 5.

### 2.3 Partner random-cut exterior-mass lemma

Controlling addendum:

`yspennstate/math-open-problems@ffc6e40587293d6019b29680fff19eb0d9179fb5`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B04/B04-20260922T152028Z-qform-r11/RANK2_RANDOM_CUT_ADDENDUM.md`.

If a rank-two residual has nonzero eigenvalues `mu_1,mu_2` and spectral frame of maximum physical row leverage `rho<1/2`, some fair physical cut has

`E_2(C) >= (mu_1 mu_2)^2 (1-2rho)/16.`                          (2.4)

This is inserted into the new unconditional quarter-Riesz splice in Section 6, giving an actual new inequality rather than a citation-only dependency.

### 2.4 Underlying determinant theorem checked at source

The underlying regularized determinant proof was also read at

`yspennstate/math-open-problems@a302aab3477c64757b511e80d3907f982e04873a`

`proofnet24/QFORM-density/interactive/20260922T131746Z-regularized-determinant/REPORT.md`.

It retains arbitrary within-block quadratic phases, induced linear terms, outside coordinates and outside couplings. Thus it applies to the Schur residual below without silently dropping self terms.

## 3. New fractional-potential theorem from aggregate determinant mass

### Lemma 3.1 — Fourier-to-Riesz conversion

Let `R` be a real random variable with characteristic function `phi_R`. Fix `0<alpha<1`. If

`int_0^infinity t^(alpha-1)|phi_R(t)| dt < infinity`,

then for every `u in R`,

`E|R-u|^(-alpha)
 <= [Gamma(alpha) cos(pi alpha/2)]^(-1)
    int_0^infinity t^(alpha-1)|phi_R(t)| dt.`                    (3.1)

#### Proof

For `epsilon>0`, define

`K_epsilon(x)= [Gamma(alpha)cos(pi alpha/2)]^(-1)
 int_0^infinity e^(-epsilon t) cos(tx)t^(alpha-1)dt.`

The Laplace integral equals

`Re[(epsilon-i x)^(-alpha)]/cos(pi alpha/2)`,

so `K_epsilon(x)>=0`, and for `x!=0`,

`K_epsilon(x) -> |x|^(-alpha)` as `epsilon downarrow0`.

Fatou and Fubini therefore give

`E|R-u|^(-alpha)
 <= liminf E K_epsilon(R-u)
 <= [Gamma(alpha)cos(pi alpha/2)]^(-1)
    int_0^infinity t^(alpha-1)|phi_R(t)|dt.`

The assumed absolute integrability justifies the last expression. QED.

### Theorem 3.2 — `QFORM-AGGREGATE-QUARTER-RIESZ-v1`

Assume the physical residual cross block `C` satisfies the completed determinant estimate (2.1) for some `1<=q<=2`. Let `k>=1` and `E_k(C)>0`. If

`2k>q`,                                                               (3.2)

then

`boxed(
 sup_u E|R-u|^(-1/4)
 <= K(q,k) E_k(C)^(-1/(8k)),
)`                                                                  (3.3)

where

`K(q,k)
 = kappa_q^(-1/8)
   B(1/(8k), 1/(4q)-1/(8k))
   / [2k Gamma(1/4) cos(pi/8)],`                                    (3.4)

`kappa_q=2q/(pi^2 e^2)`.

#### Proof

From (2.2),

`|phi_R(t)| <= [1+kappa_q^k E_k t^(2k)]^(-1/(4q)).`

Apply Lemma 3.1 with `alpha=1/4`. Put

`gamma=kappa_q^(1/2) E_k^(1/(2k)).`

Then

`int_0^infinity t^(-3/4)(1+(gamma t)^(2k))^(-1/(4q))dt`

`= gamma^(-1/4)/(2k)
   B(1/(8k),1/(4q)-1/(8k)).`

The beta integral is finite exactly under (3.2). Since

`gamma^(-1/4)=kappa_q^(-1/8)E_k^(-1/(8k)),`

(3.3)-(3.4) follow. QED.

Important explicit endpoints are

`K(1,1)=3.663273516008612...`,                                     (3.5)

and, **without any leverage assumption**,

`K(2,2)=3.413019108855586... .`                                   (3.6)

Thus a leverage-valid aggregate one-cross currency `E_1=||C||_F^2` already has a bounded quarter-potential, while the unconditional mechanism needs only aggregate rank-two exterior mass `E_2>0`.

This is an integrated product-space statement. It does not assert the refuted law-uniform scalar pointwise quadratic-phase decay.

## 4. Indefinite physical face: quarter-power conditional density

Take two original coordinates `Y,Z` with an indefinite physical block

`H=[[alpha,c],[c,beta]],`

`Delta=c^2-alpha beta>0.`                                         (4.1)

Let

`m=max(|alpha|,|beta|).`

For any deterministic affine perturbation of this binary quadratic, separate translations of `Y,Z` remove the affine terms because `H` is invertible; those translations preserve independence and density caps.

Assume `m>0`, and after swapping coordinates take `m=|beta|`. For fixed `Y=y`, solving the quadratic equation in `Z` shows that the sum of the two inverse-Jacobian contributions is at most

`(Delta y^2+beta s)_+^(-1/2).`

Therefore, using the completed quarter-power rearrangement calculation from the preceding B04 run,

`p_H(s)
 <= int f_Y(y)|Delta y^2+beta s|^(-1/2)dy
 <=4 Delta^(-1/4)m^(-1/4)|s|^(-1/4).`                            (4.2)

The bound is uniform over all affine translations of the two original coordinates.

## 5. Main theorem: indefinite face plus aggregate cross residual

Partition the original coordinates as `(Y,Z,W)`, with `(Y,Z)` the physical pair from Section 4, and write the full symmetric matrix as

`A=[[H,L],[L^T,G]].`

Because `H` is invertible, completing the square in the two **original** coordinates gives

`Q
 =(V+H^(-1)LW)^T H (V+H^(-1)LW)
 + W^T S W,`                                                     (5.1)

where `V=(Y,Z)^T` and

`S=G-L^T H^(-1)L`                                                (5.2)

is the Schur residual. Conditional on `W=w`, the two shifted coordinates remain independent and retain density cap one.

Choose disjoint original-coordinate sets `I,J` inside the `W` bank and put

`C=S[I,J]`.

### Theorem 5.1 — `QFORM-INDEFINITE-FACE-AGGREGATE-CROSS-v1`

Assume `m>0`. Suppose `C` satisfies the determinant hypothesis for some `1<=q<=2`, and `E_k(C)>0` with `2k>q`. Then `Q` has an essentially bounded density and

`boxed(
 ||p_Q||_infinity
 <=4 K(q,k)
    Delta^(-1/4)m^(-1/4)E_k(C)^(-1/(8k)).
)`                                                                  (5.3)

#### Proof

From (4.2) and the conditional decomposition (5.1),

`p_Q(t)
 <=4 Delta^(-1/4)m^(-1/4)
    E_W |t-W^T S W|^(-1/4).`

Apply Theorem 3.2 to the residual quadratic form `W^T S W`. QED.

Two endpoints matter.

**Leverage-valid one-cross aggregate (`q=1,k=1`).** If one side of `C` has range-projection diagonal at most `1/2`, then

`boxed(
 ||p_Q||_infinity
 <=14.6530940641
    Delta^(-1/4)m^(-1/4)E_1(C)^(-1/8).
)`                                                                  (5.4)

Since `E_1(C)=||C||_F^2`, no selected physical cross entry is paid.

**Unconditional rank-two aggregate (`q=2,k=2`).** With no leverage assumption at all,

`boxed(
 ||p_Q||_infinity
 <=13.6520764355
    Delta^(-1/4)m^(-1/4)E_2(C)^(-1/16).
)`                                                                  (5.5)

This is the main new splice: an indefinite physical pair can be smoothed by aggregate two-cross exterior mass in the Schur residual without any fresh scalar square.

### Exact zero-diagonal face

Now let `m=0`. Then

`H=[[0,c],[c,0]],  c!=0.`

After the conditional translations in (5.1), the physical pair equals `2cUV` with independent translated cap-one `U,V`. Apply the completed fleet02/B04 product rearrangement (2.3):

`p_(2cUV)(s)
 <=2|c|^(-1) log(1+sqrt(|c|/(2|s|))).`                           (5.6)

For `x>=0`,

`log(1+x)<=sqrt(x)`

because the derivative of `sqrt(x)-log(1+x)` is

`(sqrt(x)-1)^2/[2sqrt(x)(1+x)]>=0`.

Hence

`p_(2cUV)(s)
 <=2^(3/4)|c|^(-3/4)|s|^(-1/4).`                                (5.7)

Combining with Theorem 3.2 gives

`boxed(
 ||p_Q||_infinity
 <=2^(3/4) K(q,k)
   |c|^(-3/4)E_k(C)^(-1/(8k)).
)`                                                                  (5.8)

In particular, the unconditional `q=2,k=2` endpoint is

`boxed(
 ||p_Q||_infinity
 <=5.7399910677
   |c|^(-3/4)E_2(C)^(-1/16).
)`                                                                  (5.9)

This is a direct actual application of the named partner's product-density theorem, not merely a reference.

## 6. Direct application of the latest fleet02/B04 random-cut theorem

Suppose the Schur residual `S` in (5.2) has rank two, nonzero eigenvalues `mu_1,mu_2`, and spectral frame of maximum physical row leverage `rho<1/2`. The latest fleet02/B04 random-cut theorem (2.4) supplies a physical cut with

`E_2(C)>=(mu_1mu_2)^2(1-2rho)/16.`

Insert this into the **unconditional** endpoint (5.5). No leverage condition on the chosen cross block is needed in the present step. For `m>0`,

`boxed(
 ||p_Q||_infinity
 <=16.2351464316
   Delta^(-1/4)m^(-1/4)
   |mu_1mu_2|^(-1/8)
   (1-2rho)^(-1/16).
)`                                                                  (6.1)

At the particularly useful partner threshold `rho<=1/34`, the partner gives `E_2(C)>=(mu_1mu_2)^2/17`, and therefore

`boxed(
 ||p_Q||_infinity
 <=16.2967787222
   Delta^(-1/4)m^(-1/4)|mu_1mu_2|^(-1/8).
)`                                                                  (6.2)

This is a genuinely new inequality obtained by inserting a completed partner structural result into the new quarter-Riesz splice.

## 7. Fully coupled explicit target instance

The theorem gives a clean target-valid rotated indefinite example with all six eigenvalues outside `[-1,1]`.

Let

`H=[[1,2],[2,-1]],`

and let the four-coordinate Schur residual be

`S=[[0,0,2,0],
    [0,0,0,2],
    [2,0,0,0],
    [0,2,0,0]].`

Thus `Delta=5`, `m=1`. With the physical cut `{3,4}|{5,6}`, the residual cross block is `C=2I_2`, so

`E_2(C)=16.`

Take

`L=(1/10)[[1,2,3,4],
          [4,3,2,1]]`

and define the full `6x6` matrix

`A=[[H,L],[L^T,S+L^T H^(-1)L]].`                                (7.1)

Explicitly,

`L^T H^(-1)L =`

`[[1/500, 3/125, 23/500, 17/250],
  [3/125,19/500, 13/250, 33/500],
  [23/500,13/250,29/500, 8/125],
  [17/250,33/500, 8/125,31/500]].`

Every entry of `L` is nonzero, so the indefinite physical pair is genuinely coupled to the residual bank. Completing the pair square gives exactly the residual `S`, hence (5.5) yields for every admissible independent product law

`boxed(||p_(X^T A X)||_infinity <=7.6771267543).`                (7.2)

The target spectral hypothesis holds with room to spare. The block-diagonal reference `diag(H,S)` has eigenvalues

`{-sqrt(5),-2,-2,2,2,sqrt(5)}`.

Moreover

`||L||=1/sqrt(2),  ||H^(-1)||=1/sqrt(5),`

so

`||A-diag(H,S)||
 <= ||L||+||H^(-1)|| ||L||^2
 =1/sqrt(2)+1/(2sqrt(5))
 =0.930713579... <1.`

Weyl's inequality therefore gives

`min_j |lambda_j(A)|
 >=2-[1/sqrt(2)+1/(2sqrt(5))]
 >1.06928.`

Thus this is a fully coupled, genuinely non-diagonal, indefinite target instance and the density estimate (7.2) is completely law-independent.

## 8. What is paid and what remains unpaid

Paid here:

1. an exact aggregate quarter-Riesz theorem from the completed product determinant estimate;
2. a one-cross leverage-valid endpoint based on `E_1=||C||_F^2`, without selecting a physical cross entry;
3. an unconditional two-cross endpoint based on `E_2`, requiring neither a fresh scalar square nor a leverage condition;
4. the exact zero-diagonal physical-pair endpoint using the designated fleet02/B04 product rearrangement;
5. a direct insertion of the latest fleet02/B04 rank-two random-cut theorem into a new dimension-free density inequality;
6. an explicit fully coupled rotated indefinite target matrix with universal density bound `<7.678`.

The full conjecture remains OPEN. The first structural debt is now

`QFORM-INDEFINITE-FACE-AGGREGATE-EXTRACTION-v1`:

> Starting only from three eigenvalues of modulus at least one, route every matrix not already in the completed diffuse/ridge/scalar-square/hyperbolic branches to either (a) a physical indefinite pair with a leverage-valid residual `E_1` currency bounded below, or (b) a physical indefinite pair with unconditional residual `E_2` currency bounded below, without paying a reciprocal tiny local principal minor.

The current correction `QFORM-ONE-TRIPLE-RANK2-AGGREGATE-UNIFORM-FALSE-v1` prevents replacing this by a claim that one fixed physical triple must carry the whole currency. Any full proof must aggregate or route failures globally.

Continuity is **not proved** by Theorem 5.1. The argument proves absolute continuity and an `L^infinity` density bound through conditional density construction and a finite quarter-Riesz potential. No novelty claim is made.

## 9. Numerical constants check

Using the exact formula (3.4):

`K(1,1)=3.6632735160086121886...`

`K(1,2)=2.4554737540722656805...`

`K(2,2)=3.4130191088555859422...`

`K(2,3)=2.5614387320081337811...`

Consequently

`4K(2,2)=13.6520764354223438...`,

`2^(3/4)K(2,2)=5.7399910676581791...`,

and the explicit example constant is

`4K(2,2)5^(-1/4)16^(-1/16)=7.6771267542953379...`.

These evaluations only instantiate exact beta/gamma formulas; no simulation or histogram is used as proof.
