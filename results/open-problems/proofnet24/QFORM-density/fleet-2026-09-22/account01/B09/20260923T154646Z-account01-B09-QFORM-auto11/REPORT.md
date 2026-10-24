SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B09, 2026-09-23T15:46:46Z.
attacking: the invertible-indefinite physical-pair branch by proving that exact Schur elimination retains the third singular-value resource and paying that residual resource through a dimension-free fractional-potential dichotomy.

# account01/B09 — every quantitative indefinite physical pair retains a payable third spectral resource

## Status

**ESSENTIAL_STEP_APPLIED / NEW SUPPORTING THEOREM / FULL QFORM OPEN.**

The unrestricted owner target is not proved or disproved here. Full-target continuity remains open. This run proves two supporting statements and splices them to remove the explicit nonzero-Schur-cross hypothesis from the preceding B09 pair theorem:

1. an arbitrary quadratic form with one nonzero spectral direction has a universal `1/12`-fractional potential bound under independent cap-one inputs, with arbitrary affine terms;
2. after eliminating any invertible physical two-coordinate block, the exact Schur complement necessarily has operator norm at least the third singular value of the original matrix.

Combining these with the completed physical-pair logarithmic envelope pays **every quantitatively invertible indefinite physical pair** in a matrix with three large singular/eigenvalue directions. No rotation of the random vector, moment assumption, compact support, log-concavity, connected support, Gaussian assumption, or law-uniform pointwise stationary-phase estimate is used.

## 1. Sources used at their exact scopes

### 1.1 Fractional cross-volume compiler

From account03/B01:

`yspennstate/math-open-problems@936b0f0bad22de82921c2a743fb0738226270348`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/account03-B01-20260923T013054Z-auto11/REPORT.md`.

For disjoint ORIGINAL-coordinate banks `I,J`,

`R=F(X_I)+2 X_I^T M X_J+G(X_J)`

with arbitrary measurable same-bank functions `F,G`, let

`Z_k=e_k(M^T M)>0`.

For the determinant-square `k`-volume sampling row marginals `alpha_i`, if `alpha_i<=q/2`, then for

`0<gamma<min(1,k/(2q))`

one has

`H_gamma(R):=sup_s E|R-s|^(-gamma)
 <= C_(k,gamma,q) Z_k^(-gamma/(2k))`,

where

`C_(k,gamma,q)
 =[2k c_gamma e^gamma pi^gamma q^(-gamma/2)]
   /[gamma(k-2q gamma)]`,

`c_gamma=2^(1-gamma) Gamma((1-gamma)/2)
          /(2 sqrt(pi) Gamma(gamma/2)).`

For `k=1,q=2`, the row condition is automatic because every one-volume marginal is at most one. Arbitrary same-bank quadratic curvature and outside-generated affine terms remain allowed.

### 1.2 Physical-pair logarithmic envelope

From

`yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`

`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.

For two independent cap-one physical coordinates, an invertible indefinite symmetric pair matrix `E`,

`D=|det E|`, `kappa=sigma_min(E)`,

and arbitrary deterministic affine shift, the conditional pair law has for every `r>0` the logarithmic envelope

`p_pair(t)
 <=2 sqrt(2)/r
   +D^(-1/2) log_+(2r^2/(kappa |t-t0|)).`                    (1.1)

The two coordinate shifts may depend arbitrarily on all remaining original coordinates after conditioning.

## 2. New lemma: one spectral direction gives a universal fractional potential

### Lemma `QFORM-ONE-SPECTRAL-DIRECTION-H1/12-v1`

Let `S` be any nonzero real symmetric `m x m` matrix and set

`s=||S||_op>0`.

Let `Y_1,...,Y_m` be independent real random variables with densities bounded by one. For arbitrary `b in R^m`, `c in R`, put

`R=Y^T S Y+b^T Y+c`.

Then

`boxed:
 sup_t E|R-t|^(-1/12)
 <= K_0 s^(-1/12),`                                         (2.1)

where

`K_0=2.058622929949779...<2.059.`                            (2.2)

No rank, sign, leverage, support, or moment condition is imposed.

### Proof

Write

`O=S-diag(S)`.

We split according to whether the spectral size is carried substantially by off-diagonal or diagonal physical coefficients.

#### Case A: `||O||_F >= s/2`

Choose a random Bernoulli partition of the ORIGINAL coordinates into disjoint banks `I,J`, each coordinate independently assigned to either side with probability `1/2`. For the physical cross block

`C=S[I,J]`,

`E_partition ||C||_F^2
 =(1/4) sum_(i!=j) S_ij^2
 =(1/4)||O||_F^2.`                                          (2.3)

Hence one deterministic partition satisfies

`||C||_F >= ||O||_F/2 >= s/4.`                               (2.4)

Relative to this partition, all diagonal and within-bank quadratic terms, together with `b^T Y+c`, are absorbed into arbitrary same-bank functions `F(Y_I),G(Y_J)`, while the cross term is exactly `2Y_I^T C Y_J`.

Apply the source fractional compiler with

`k=1`, `q=2`, `gamma=1/12`.

The row-marginal condition is automatic. Since

`Z_1=||C||_F^2 >= s^2/16`,

we obtain

`H_(1/12)(R)
 <=36 c_(1/12)e^(1/12)pi^(1/12)2^(-1/24)
    Z_1^(-1/24)`

`<=36 c_(1/12)e^(1/12)pi^(1/12)2^(1/8)
    s^(-1/12)`

`=2.058622929949779... s^(-1/12).`                           (2.5)

Here

`c_(1/12)=0.0438556136991933256...`.

#### Case B: `||O||_F < s/2`

Since `||O||_op<=||O||_F`,

`||diag(S)||_op
 >=||S||_op-||O||_op
 >s/2.`                                                       (2.6)

Thus some original coordinate `i` has

`|a|:=|S_ii|>s/2.`                                           (2.7)

Condition on all other ORIGINAL coordinates. The remaining output is a scalar quadratic

`aY_i^2+lY_i+d`.

For every `u>0` and every target value, completing the square shows that the inverse image of an interval of radius `u` has total Lebesgue length at most

`2 sqrt(2u/|a|)`.

Since the conditional scalar density cap is still one,

`P(|R-t|<u | Y_-i)
 <=min(1,2 sqrt(2u/|a|))
 <=min(1,4 s^(-1/2)u^(1/2)).`                                (2.8)

Average the conditioning. The layer-cake identity for `0<gamma<1/2` gives from a small-ball bound `min(1,L sqrt(u))`

`sup_t E|R-t|^(-gamma)
 <=[1/(1-2gamma)] L^(2gamma).`                                (2.9)

With `gamma=1/12`, `L=4s^(-1/2)`,

`H_(1/12)(R)
 <=(6/5)2^(1/3)s^(-1/12)
 =1.5119052598738478...s^(-1/12),`                            (2.10)

which is smaller than (2.5). This proves (2.1). QED.

### Remarks

The partition in Case A is only a deterministic existence device on original coordinates; no rotated random coordinates are introduced. The source compiler permits arbitrary same-bank curvature, so no quadratic remainder is discarded. Case B conditions only an original coordinate and keeps its cap-one density.

## 3. Exact structural identity: the Schur remainder retains the third singular value

Let `P` be two ORIGINAL physical coordinates and reorder the matrix as

`A=[[E,K^T],[K,D0]],`                                        (3.1)

where the `2 x 2` physical pair `E` is invertible. Define the exact Schur complement

`S=D0-K E^(-1) K^T.`                                        (3.2)

### Lemma `QFORM-SCHUR-THIRD-SINGULAR-RESOURCE-v1`

`boxed:
 ||S||_op >= sigma_3(A).`                                    (3.3)

### Proof

Put

`L=[I_2; K E^(-1)]`

and

`R_2=L E L^T
 =[[E,K^T],[K,K E^(-1)K^T]].`                               (3.4)

Because `rank(R_2)<=2`, while

`A-R_2=diag(0,S)`,                                           (3.5)

Eckart--Young in operator norm gives

`sigma_3(A)
 =inf_(rank R<=2)||A-R||_op
 <=||A-R_2||_op
 =||S||_op.`                                                  (3.6)

QED.

In particular, under the owner target hypothesis, `sigma_3(A)>=1`, hence **every invertible physical pair leaves an exact Schur residual with operator norm at least one**. No individual residual cross coefficient, principal minor, or rotated-coordinate independence is required.

## 4. New theorem: every quantitative indefinite physical pair is payable

### Theorem `QFORM-INDEFINITE-PAIR-THIRD-SPECTRAL-SMOOTHING-v1`

Let `A` be any real symmetric matrix, `X` have independent real coordinates with densities bounded by one, and suppose an ORIGINAL physical pair `P` has invertible indefinite principal matrix

`E=A[P,P]`.

Set

`D=|det E|>0`,
`kappa=sigma_min(E)>0`,
`rho=sigma_3(A)>0`.

Then `Q=X^T A X` has an essentially bounded density satisfying

`boxed:
 ||p_Q||_infinity
 <=12.181 D^(-3/7)(kappa rho)^(-1/14).`                       (4.1)

Consequently every interval `I` satisfies

`boxed:
 P{Q in I}
 <=12.181 D^(-3/7)(kappa rho)^(-1/14)|I|.`                    (4.2)

Under the full owner hypothesis `rho>=1`, this simplifies to

`boxed:
 ||p_Q||_infinity
 <=12.181 D^(-3/7)kappa^(-1/14).`                             (4.3)

Continuity is **not claimed** by this theorem.

### Proof

Write `A` in the block form (3.1). Completing the physical pair exactly gives

`Q=(X_P+E^(-1)K^T X_R)^T E
   (X_P+E^(-1)K^T X_R)
   + X_R^T S X_R`,                                           (4.4)

where `S` is (3.2). More generally affine terms generated by conditioning unused original coordinates can be retained; they are allowed by both inputs used below.

By Lemma (3.3),

`||S||_op>=rho.`                                              (4.5)

Applying Lemma (2.1) to the exact Schur residual

`R=X_R^T S X_R`

gives

`H_(1/12)(R)
 :=sup_t E|R-t|^(-1/12)
 <=K_0 rho^(-1/12).`                                         (4.6)

Condition on the residual coordinates and apply the pair-log envelope (1.1). Averaging gives, for every `r>0`,

`p_Q(t)
 <=2sqrt(2)/r
 +D^(-1/2) E log_+(2r^2/(kappa|t-R|)).`                      (4.7)

For `x>=1` and `gamma>0`,

`log x <= x^gamma/(e gamma)`.

With `gamma=1/12`, (4.6) implies

`p_Q(t)<=A r^(-1)+B r^(1/6),`                                (4.8)

where

`A=2sqrt(2)`,

`B=D^(-1/2)kappa^(-1/12)rho^(-1/12)
    (12/e)2^(1/12)K_0.`                                      (4.9)

For `m=1/6`,

`min_(r>0)(A/r+B r^m)
 =(7/6)(6A)^(1/7)B^(6/7).`                                   (4.10)

Therefore

`||p_Q||_infinity
 <=K_pair D^(-3/7)(kappa rho)^(-1/14),`                       (4.11)

where

`K_pair
 =(7/6)(12sqrt(2))^(1/7)
  [(12/e)2^(1/12)K_0]^(6/7)`

`=12.180357268765312...<12.181.`                              (4.12)

This proves (4.1). The conditional pair kernels and their averages provide an absolutely continuous law; the uniform essential-supremum bound gives (4.2).

The matrix scaling is exact. Under `A -> uA`, `D -> u^2D`, `kappa -> |u|kappa`, `rho -> |u|rho`, so the right side of (4.1) scales by `|u|^(-1)`.

## 5. What has been removed relative to the preceding B09 pair theorem

The preceding B09 theorem `QFORM-INDEFINITE-PAIR-PLUS-ONECROSS-v1` required a nonzero explicit cross block in the Schur residual and paid it through a `1/8` fractional potential. The present theorem removes that structural assumption completely.

For an invertible indefinite physical pair, the exact low-rank identity (3.4)--(3.6) says the third singular-value resource cannot disappear under Schur elimination. Lemma 2 pays that resource whether it appears as:

- diffuse off-diagonal physical curvature, in which case a Bernoulli original-coordinate cut exposes aggregate one-volume; or
- a large physical diagonal, in which case one scalar original-coordinate quadratic supplies the fractional potential.

Thus no assertion of a universally good individual Schur cross entry or rank-two cross block is needed.

The remaining problem is quantitative **physical-pair degeneration**: the bare three-large-eigenvalue hypothesis does not force one indefinite pair with `D` and `kappa` bounded below. Definite pairs, singular pairs, near-coloops, grouped-square banks, and diffuse aggregate mechanisms must still be spliced to close that structural alternative.

## 6. Literal target-valid regression

Take

`A0=[[0,1,0],
    [1,0,0],
    [0,0,1]].`

Its eigenvalues are exactly `{-1,1,1}`, so `rho=sigma_3(A0)=1`. For the physical pair `P={1,2}`,

`E=[[0,1],[1,0]]`,

so

`D=1`, `kappa=1`.

The Schur residual is the scalar matrix `[1]`, also of operator norm one. The theorem gives for **every** admissible independent cap-one product law

`boxed:
 ||p_(2X1X2+X3^2)||_infinity<12.181,`

`boxed:
 P{2X1X2+X3^2 in I}<12.181|I|.`                              (6.1)

Both scalar diagonals in the indefinite physical pair are exactly zero.

## 7. Designated partner account02/B09 actually applied

The newest completed designated-partner result consumed in full is

`QFORM-ONE-ANCHOR-THREEVOLUME-HYBRID-v1`

at

`yspennstate/math-open-problems@59ccddd0766b466b30abd645926887f907b0bcd7`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B09/20260923T134326Z-account02-B09-QFORM-r13/REPORT.md`.

It proves that for a literal source-coordinate cross matrix, if every selected physical `3 x 3` minor contains one distinguished physical row `h`, total determinant-square mass is `Z>0`, anchor cross-row norm is `||a||`, and every other selected row marginal is at most `1/2`, then the full quadratic output (arbitrary same-side curvature included) has a continuous density with

`||p_Q||_infinity
 <=5*2^(4/5)*sqrt(e) ||a||^(1/5) Z^(-1/5).`                  (7.1)

Apply it to the cross-only target

`A_s=[[0,M_s],[M_s^T,0]]`,

where `s>=1` and the five rows of `M_s` are

`(s,0,0),`
`(0,1/sqrt(2),0),`
`(0,1/sqrt(2),0),`
`(0,0,1/sqrt(2)),`
`(0,0,1/sqrt(2)).`

Then

`M_s^T M_s=diag(s^2,1,1)`,

so the nonzero spectrum of `A_s` is exactly

`{+s,-s,+1,-1,+1,-1}`.

Select the four nonzero `3 x 3` minors containing the first row, one of rows 2--3, one of rows 4--5, and all three columns. Each squared determinant is `s^2/4`, hence

`Z=s^2`, `||a||=s`,

and every non-anchor selected row marginal is exactly `1/2`. The partner theorem gives the actual target inequality

`boxed:
 ||p_(X^T A_s X)||_infinity
 <=5*2^(4/5)*sqrt(e) s^(-1/5)`                               (7.2)

with a continuous density and the same coefficient multiplying every interval length.

At `s=243=3^5`,

`boxed:
 ||p_(X^T A_243 X)||_infinity<4.785,`

`boxed:
 P{X^T A_243 X in I}<4.785|I|.`                              (7.3)

This is an actual application of the designated partner result, not a citation-only use.

## 8. Correction audit and remaining implication

The proof respects the current source corrections:

- no law-uniform pointwise van-der-Corput/Fresnel decay is used;
- no independence is claimed after an orthogonal spectral rotation;
- no unrestricted joint-density coarea lemma is used;
- no dimension-free worst-fiber supremum is used;
- no assertion is made that a scalar pivot forces a rank-two cross block;
- no individual cross minor is inferred from spectral size;
- no small quadratic remainder is dropped perturbatively.

The first B09 structural debt is now

`QFORM-INDEFINITE-PAIR-DEGENERATION-OR-PAID-EXIT-v1`:

> Under `sigma_3(A)>=1`, route the case in which every physical indefinite pair has degenerating determinant/minimum singular value into a definite-pair, singular-pair, near-coloop/collar, grouped-square, ridge/diffuse, or aggregate cross-volume mechanism, without trying to infer a uniformly conditioned physical pair from spectral size alone.

The exact Schur identity above means that once a quantitative indefinite physical pair is found, **no separate third-direction extraction is needed**.

## 9. Full-target status

The universal bounded-density conjecture remains **OPEN / not proved / not disproved**. Full-target continuity remains **OPEN**. The new theorem is a supporting target-level branch pending independent mathematical review.

Execution label: `WITHOUT_VERIFIED_BRAIN`; repository retrieval and delivery do not establish native learned-memory ingestion.
