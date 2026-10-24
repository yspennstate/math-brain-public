SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B04, 2026-09-22T18:16:20Z.
attacking: dense-curved-bank routing via a product-space matching extraction, aiming to convert large center-to-bank mass into an exact disjoint hyperbolic-pair smoother or a quantified residual certificate while preserving arbitrary quadratic curvature.

# account01/B04 — two-hyperbolic-pair convolution and zero-diagonal bank pattern trichotomy

**Run:** `20260922T181620Z-account01-B04-QFORM-r15`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Fresh prepublication owner control:** revision `2026-09-22.11`, brain main observed at `fb48babff3d0a2b078a9df38923eb2f45bc3f3fa`  
**Assignment:** Product Fourier rearrangement  
**Outcome:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREMS_PROVED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Full target and changed mechanism

The target remains the unrestricted statement: for every dimension, every independent product input with one-dimensional densities bounded by one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove a universal finite essential-supremum bound for the density of `X^T A X`, or give a valid counterexample. Continuity is tracked separately.

The immediately preceding B04 run used a one-center half-Riesz/star mechanism and proper coloring of a zero-diagonal bank. The first unpaid branch was a bank whose exact interaction graph had no quantitatively useful large independent set. This run changes mechanism: it uses **two independent logarithmically singular hyperbolic products and an L2 convolution**, rather than another one-center half-Riesz estimate. The result pays an induced matching of size two without requiring any residual density premise. Combined with the previous coloring theorem and the account02/B04 pure-cross triangle theorem, this yields an exhaustive **support-pattern trichotomy** for an exact zero-diagonal Schur bank.

This does not solve the full conjecture. The remaining issue is quantitative coefficient aggregation and nonzero bank diagonals; small quadratic coefficients cannot be discarded without moments or support control.

## 2. Source-pinned dependencies and corrections

### Latest designated partner actually used

The completed account02/B04 report is

`yspennstate/math-open-problems@4bea103ece44732c1c7c31368fec4e33b35e1fdd`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B04/B04-20260922T174702Z-r15/REPORT.md`, blob `7c1bf677f5ca43e52f6b165f19c8fe0690a12f51`.

It proves `QFORM-HYPERBOLIC-PAIR-DENSITY-TRANSFER-v1` and, inside its proof, the translated product envelope: for independent cap-one `U,V`, `c!=0`, and arbitrary deterministic translations of `U,V`, the density `g_c` of `2cUV` satisfies

`g_c(s) <= |c|^(-1) [1 + log_+(2|c|/|s|)]`.                (2.1)

The present report applies (2.1) quantitatively to an L2 rearrangement and later applies the partner's full transfer theorem to a three-pair inequality.

### Earlier partner pure-cross theorem used in the structural synthesis

Account02/B04 also proved `QFORM-PURE-CROSS-TRIPLE-v1` at

`yspennstate/math-open-problems@b7168a1b0b52fbf69705170ff9795435efeb849f`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B04/account02-B04-20260922T122057Z-01c809a1/REPORT.md`, blob `fa94d255369a9ad6475ebc66b2f158066e588a8b`.

For an all-zero-diagonal invertible physical triple `T`, it proves

`||p||_infinity <= C_cross |det T|^(-1/3)`,                (2.2)

with

`C_cross = 2^(4/3)[log(1+sqrt(2))+sqrt(2)log(1+1/sqrt(2))]
          = 4.126732796441510...`,

uniformly under arbitrary affine terms produced by conditioning outside the triple.

### Previous account01/B04 theorem used in the synthesis

The preceding run proved `QFORM-AFFINE-STAR-HALF-RIESZ-v1` and its coloring corollary at

`yspennstate/math-open-problems@0c69ee2f962d8fe4e998a69ed41a29c100a742fd`,

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B04/20260922T174812Z-account01-B04-QFORM-r15/REPORT.md`.

After a scalar pivot `a!=0`, if the zero-diagonal bank interaction graph is `chi`-colorable and total center-to-bank Euclidean cross norm is `B_0`, it gives

`||p_Q||_infinity <= 2^(11/4) chi^(1/4) / sqrt(|a| B_0)`. (2.3)

### Corrections respected

Fresh controls and the live correction inbox were re-read before publication. No uniform pointwise quadratic-phase decay, post-rotation independence, conditional projection cap, arbitrary-joint coarea bound, one-good-minor dichotomy, one-Schur-rank-two extraction, or fiberwise trace estimate is used. In particular the argument retains original-coordinate product independence and never treats a small coefficient multiplying an unbounded random square as a small perturbation.

## 3. An L2 rearrangement theorem for one hyperbolic product

The partner envelope (2.1) is logarithmically singular at zero but is square-integrable after the probability-mass constraint is imposed.

### Lemma 3.1 — `QFORM-HYPERBOLIC-PRODUCT-L2-v1`

Let `U,V` be independent real random variables with densities bounded by one, let `c!=0`, and allow arbitrary deterministic translations of `U,V`. If `g_c` is the density of the resulting `2cUV`, then

`||g_c||_2^2 <= K_2 / |c|`,                                 (3.1)

where

`K_2 = z + z^(-1) = 5.194878272562849...`,                 (3.2)

and `z>2` is the unique solution

`4 z exp(-(z-2)) = 1`, equivalently
`z = -W_{-1}(-e^(-2)/4) = 4.994664629781440...`.            (3.3)

Hence

`||g_c||_2 <= 2.279227560504402... |c|^(-1/2)`.             (3.4)

#### Proof

By the partner theorem,

`0 <= g_c(s) <= k_c(s):=|c|^(-1)[1+log_+(2|c|/|s|)]`,
`int g_c = 1`.                                               (3.5)

The envelope `k_c` is symmetric and decreasing in `|s|` on its high-value region. Let `L>0` solve

`4 e^(-L)(L+2)=1`,                                           (3.6)

and put `r=2|c|e^(-L)`. Direct integration gives

`int_{|s|<=r} k_c(s) ds
 =4 e^(-L)(L+2)=1`.                                           (3.7)

Let `g_c^*` be the decreasing rearrangement of `g_c` and let `k_c^*` be the decreasing rearrangement of the envelope. Pointwise domination gives `g_c^*<=k_c^*`. Define `h` by filling the highest-cap region of `k_c^*` until mass one, namely the rearrangement of `k_c 1_{[-r,r]}`. For every initial segment,

`int_0^x g_c^* <= min(1, int_0^x k_c^*) = int_0^x h`,        (3.8)

so `h` majorizes `g_c^*`. Convex rearrangement/Karamata for `u -> u^2` yields

`int g_c^2 = int (g_c^*)^2 <= int h^2
            = int_{|s|<=r} k_c(s)^2 ds`.                    (3.9)

Now substitute `s=2|c|u`, `a=e^(-L)`:

`int_{|s|<=r} k_c(s)^2 ds
 = (4/|c|) int_0^a (1+log(1/u))^2 du
 = (4a/|c|)(L^2+4L+5).`                                     (3.10)

Using `4a(L+2)=1` from (3.6),

`4a(L^2+4L+5)
 = ((L+2)^2+1)/(L+2)
 = z+z^(-1)=K_2`.                                           (3.11)

This proves (3.1). QED.

The probability mass is essential here: the raw envelope itself has a constant tail and is not in L2. The rearrangement first spends exactly one unit of allowable mass on its highest-cap region.

## 4. Two disjoint hyperbolic pairs give a bounded continuous density

### Theorem 4.1 — `QFORM-TWO-HYPERBOLIC-PAIR-CONVOLUTION-v1`

Let

`U_1,V_1,U_2,V_2,W_1,...,W_m`

be independent real random variables with densities bounded by one. Let `c_1,c_2` be nonzero. Let `L_i,M_i` be arbitrary real linear forms of `W`, and let `R(W)` be any measurable quadratic residual. Define

`Q = 2c_1 U_1V_1 + 2U_1 L_1(W)+2V_1 M_1(W)
    +2c_2 U_2V_2 + 2U_2 L_2(W)+2V_2 M_2(W)
    +R(W)`,                                                  (4.1)

with **no quadratic coupling among the four selected coordinates other than the two displayed pair edges**.

Then `Q` has a continuous density and

`boxed: ||p_Q||_infinity <= K_2 / sqrt(|c_1 c_2|)`.          (4.2)

Numerically the coefficient is `5.194878272562849...`.

#### Proof

Condition on `W=w`. Complete each pair separately:

`2c_i U_iV_i +2U_i L_i(w)+2V_i M_i(w)
 =2c_i (U_i+M_i(w)/c_i)(V_i+L_i(w)/c_i)
  -2L_i(w)M_i(w)/c_i`.                                      (4.3)

Thus, given `w`, the random part is the sum of two independent translated hyperbolic products, plus a deterministic shift. By Lemma 3.1 their conditional densities `g_{1,w},g_{2,w}` satisfy

`||g_{i,w}||_2 <= sqrt(K_2/|c_i|)`.                          (4.4)

Cauchy-Schwarz/Young gives

`||g_{1,w}*g_{2,w}||_infinity
 <= ||g_{1,w}||_2 ||g_{2,w}||_2
 <= K_2/sqrt(|c_1c_2|)`.                                    (4.5)

The convolution of two L2 functions is continuous: for every `h`,

`sup_t |(g_1*g_2)(t+h)-(g_1*g_2)(t)|
 <= ||g_1||_2 ||tau_h g_2-g_2||_2 ->0`.                     (4.6)

Therefore each conditional density is continuous. It is uniformly bounded by (4.5), so averaging in `w` and applying dominated convergence preserves both the density bound and continuity. QED.

This result is stronger than applying a density bound to either single pair: one opposite-sign/hyperbolic pair can have a logarithmically unbounded density, while two disjoint product pairs cancel that singularity by L2 convolution.

## 5. Scalar-pivot corollary

The standard square-pivot rearrangement gives a useful target-facing consequence.

### Lemma 5.1 — capped half-Riesz potential

If `T` has probability density bounded by `M`, then

`sup_t E |T-t|^(-1/2) <= 2 sqrt(2M)`.                        (5.1)

This is the exact bathtub value: fill the interval of length `1/M` centered at the singularity at height `M`.

### Corollary 5.2 — `QFORM-PIVOT-INDUCED-2K2-v1`

Suppose a physical scalar pivot `Y` has coefficient `a!=0`. After completing the square in `Y`, suppose the Schur residual contains four original coordinates whose principal block has zero diagonal and exactly two disjoint nonzero edges with coefficients `c_1,c_2`, with no other edges among the four. All remaining coordinates and all couplings to them are arbitrary.

Then the full quadratic form has an essentially bounded density and

`boxed: ||p_Q||_infinity
 <= 2 sqrt(2K_2) |a|^(-1/2)|c_1c_2|^(-1/4)`                 (5.2)

with

`2 sqrt(2K_2)=6.446629055599740...`.                        (5.3)

#### Proof

Condition all residual coordinates outside the four selected vertices. Theorem 4.1, including arbitrary affine contamination from the conditioned variables, gives a residual density cap

`M=K_2/sqrt(|c_1c_2|)`.                                     (5.4)

Completing the original-coordinate pivot gives the conditional square kernel bounded by `|a|^(-1/2)|u|^(-1/2)`. Average it against the residual and apply (5.1). This yields (5.2). QED.

Continuity of the **full scalar-pivoted form** is not asserted by this argument; only essential boundedness is proved. The residual four-coordinate smoother itself is continuous by Theorem 4.1.

## 6. Full application of the designated partner theorem

Theorem 4.1 also supplies an actual density premise for the latest account02/B04 transfer theorem rather than merely reusing its envelope.

Take a third original-coordinate hyperbolic pair `(U_0,V_0)` with coefficient `c_0!=0`, whose completion leaves as `H` a residual satisfying the hypotheses of Theorem 4.1 with pair coefficients `c_1,c_2`. The partner theorem `QFORM-HYPERBOLIC-PAIR-DENSITY-TRANSFER-v1` says

`||p_Q||_infinity <= |c_0|^(-1)+4 ||p_H||_infinity`.         (6.1)

Substituting the newly proved bound (4.2) gives the explicit product-space inequality

`boxed: ||p_Q||_infinity
 <= |c_0|^(-1) + 4K_2/sqrt(|c_1c_2|).`                       (6.2)

Thus the completed partner result is applied at its exact hypotheses to a new residual certificate; no conditional independence beyond the original disjoint product coordinates is invented.

## 7. A support-pattern trichotomy for an exact zero-diagonal Schur bank

This section combines the present theorem with the preceding B04 coloring theorem and the account02/B04 pure-cross theorem.

Let `K` be a bank of original coordinates after a scalar pivot, assume

`S[j,j]=0` for every `j in K`,                                (7.1)

and let `G` be the simple graph on `K` in which `jk` is an edge iff `S[j,k]!=0`.

### Lemma 7.1 — triangle / induced-2K2 / 3-colorable trichotomy

Every simple graph satisfies at least one of:

1. it contains a triangle;
2. it contains an induced `2K2` (two disjoint edges and no other edge on their four endpoints);
3. it is 3-colorable.

#### Proof

Assume no triangle and no induced `2K2`. If the graph is edgeless it is 1-colorable. Otherwise fix an edge `uv`. Put

`A=N(u)\{v}`, `B=N(v)\{u}`,
`C=V(G)\({u,v} union A union B)`.

Triangle-freeness makes `A` and `B` independent, makes them disjoint, and implies `A union {v}` and `B union {u}` are independent. If `C` contained an edge `xy`, then the induced subgraph on `{u,v,x,y}` would consist exactly of `uv` and `xy`, an induced `2K2`, contradiction. Thus `C` is independent. These three independent sets form a 3-coloring. QED.

### Consequence for the scalar-pivot bank

In the exact zero-diagonal bank branch, one of three analytic exits is therefore always available:

**Color exit.** If `G` is 3-colorable, (2.3) gives

`||p_Q||_infinity
 <= 2^(11/4) 3^(1/4) / sqrt(|a|B_0)
 = 8.853455357602572... / sqrt(|a|B_0)`,                    (7.2)

where `B_0` is the center-to-bank Euclidean cross norm from the previous run.

**Triangle exit.** If `G` has a triangle, its three vertices form an invertible all-zero-diagonal physical residual triple. Conditioning every other residual coordinate and applying the account02/B04 pure-cross theorem gives residual cap

`M <= C_cross |det T|^(-1/3)`.                              (7.3)

One outer scalar square then gives

`||p_Q||_infinity
 <= 2 sqrt(2C_cross)|a|^(-1/2)|det T|^(-1/6)
 = 5.745769084424824... |a|^(-1/2)|det T|^(-1/6)`.          (7.4)

**Induced-matching exit.** If `G` has an induced `2K2`, Corollary 5.2 gives (5.2).

Hence **graph complexity itself is no longer an unpaid obstruction on an exact zero-diagonal Schur bank**. The remaining issue is quantitative: a triangle or induced matching may use arbitrarily tiny edge coefficients, while the 3-color exit requires quantitative center-to-bank mass. A dimension-free argument must aggregate these weights or route their failure into a square/ridge/grouped-coordinate certificate. This statement does not claim that one local triangle or `2K2` is uniformly conditioned under the bare spectral hypothesis.

## 8. Explicit genuinely rotated indefinite target example

The new induced-matching corollary yields an all-law estimate for a fully coupled five-coordinate target example with exactly three eigenvalues of modulus above one.

Set the scalar pivot

`a=2`, `b=(0.10,-0.08,0.12,-0.05)`,

and prescribe the Schur residual

`S = [[0,1.3,0,0],
      [1.3,0,0,0],
      [0,0,0,0.4],
      [0,0,0.4,0]]`.                                       (8.1)

Define `C=S+bb^T/a` and

`A=[[a,b^T],[b,C]]`.                                        (8.2)

Numerically this is

`A = [[ 2,      .1,    -.08,    .12,    -.05],
      [ .1,     .005,   1.296,  .006,   -.0025],
      [-.08,    1.296,  .0032, -.0048,   .002],
      [ .12,    .006,  -.0048,  .0072,   .397],
      [-.05,   -.0025,  .002,   .397,    .00125]]`.          (8.3)

The independent checker records

`eig(A)=(-1.296824830584,
         -0.398797373217,
          0.399695084276,
          1.299817319969,
          2.012759799556)`.                                  (8.4)

Thus exactly three eigenvalues have modulus at least one, with both signs present; every row has off-diagonal coupling and the matrix is not diagonal in the independent coordinates. Its Schur complement at the first coordinate is exactly (8.1), so `c_1=1.3`, `c_2=0.4`. Formula (5.2) gives, for **every** admissible independent cap-one product law,

`boxed: ||p_{X^TAX}||_infinity <= 5.368053648350387.`        (8.5)

The numerical script also verifies the Schur reconstruction error is zero at displayed precision. The full-form continuity conclusion is not claimed.

## 9. First unpaid implication after this run

The next precise implication is

`QFORM-ZERODIAG-WEIGHTED-PATTERN-AGGREGATION-v1`:

> In the scalar-pivot high-overlap branch, for a zero-diagonal Schur bank, turn the global spectral/regularized-determinant currency into at least one quantitatively paid quantity among
> `(i) |a| B_0`,
> `(ii) |a|^3 |det T|` for an internal triangle, or
> `(iii) |a|^2 |c_1c_2|` for an induced `2K2`,
> **or** route failure into an already completed ridge/square/grouped-coordinate branch.

The support-pattern part is now exhaustive. The weighted part is not. Moreover, if bank diagonal entries are nonzero, even if individually tiny, they cannot simply be deleted because the input laws have no moments or bounded support. A complete proof must address that branch as well.

## 10. Finite calculation and integrity record

Harmless finite calculations are stored beside this report:

- `check_constants.py`
- `check_output.txt`

They verify the root in (3.3), `K_2`, the three displayed analytic coefficients, the matrix eigenvalues in (8.4), the exact Schur reconstruction, and the bound (8.5). The mathematics above does not rely on Monte Carlo or histogram evidence.

The changed-file set contains only this mathematical report and the displayed deterministic checker/output. A manual narrow privacy review found no credentials, scheduler identifiers, machine paths, unrelated private data, benchmark material, or external paid-call content. No repository-wide secret-scanner execution interface was exposed in this connector-only run.

**Full-target status:** OPEN.  
**Essential boundedness:** proved only in the scopes stated above.  
**Continuity:** proved in Theorem 4.1 for the two-pair smoother; not proved for the scalar-pivot full-form corollary or the full conjecture.  
**No counterexample to the full conjecture is claimed.**
