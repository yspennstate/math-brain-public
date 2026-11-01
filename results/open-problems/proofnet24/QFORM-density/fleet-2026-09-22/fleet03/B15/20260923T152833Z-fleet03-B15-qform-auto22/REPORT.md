SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B15, 2026-09-23T15:28:33Z.
attacking: product-preserving rough-law regularity from a general physical pair plus a disjoint square, extending the newest fleet04/B15 zero-self-coupling branch without rotating independent coordinates.

# fleet03/B15 — conditional Lp regularity compiler and a general 2+1 physical branch

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T152833Z-fleet03-B15-qform-auto22`  
Status: `NEW SCOPED CONTINUOUS-DENSITY BRANCH / FULL QFORM OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact scope and dependencies

The target remains the unrestricted conjecture for arbitrary independent cap-one real input densities and every real symmetric A having at least three eigenvalues of modulus at least one. No moments, compact support, log-concavity, connected support, identical laws, or independence after rotation are used below.

Two completed supporting sources are consumed at equations rather than merely cited.

1. **Partner fleet04/B15**, `yspennstate/math-open-problems@cff8e1368d32302e6d649f776579a5c1951929b1`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B15/20260923T151702Z-fleet04-B15-pivoted-convolution-r6/REPORT.md`. For independent cap-one X,Y and b != 0,
   
   `T=aX^2+2bXY+2uX+2vY+c`
   
   has, for 1<p<infinity,
   
   `||p_T||_p <= p |b|^(-1+1/p)`,
   
   and an independent square `S=gamma Z^2+2wZ` satisfies `||p_S||_(3/2)<=2|gamma|^(-1/3)`.

2. **Physical-pair logarithmic envelope**, `yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`, path `proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`. For independent cap-one U,V and an arbitrary affine perturbation F of an invertible indefinite symmetric 2x2 physical block B, writing
   
   `D=|det B|`, `kappa=sigma_min(B)`,
   
   there is, for every r>0, a decomposition into nonnegative subprobability densities
   
   `p_F=p_far+p_near`
   
   with
   
   `p_far(t) <= 2sqrt(2)/r`,
   
   `p_near(t) <= D^(-1/2) log_+(2r^2/(kappa |t-t0|))`.
   
   The same report gives, for definite B, `||p_F||_infinity <= pi/sqrt(D)` for every affine perturbation.

Both are original-coordinate arguments. The second supporting result is source-complete but, according to current shared state, still awaits the requested independent review; the theorem below inherits that dependency status.

## 2. Rough conditional Lp-convolution regularity lemma

This is the regularity interface used below.

### Lemma 2.1

Let Y,Z,W be mutually independent random blocks. For almost every w suppose

`T_w=F_w(Y)`, `S_w=G_w(Z)`

have densities k_w and l_w satisfying, for one fixed 1<p<infinity,

`||k_w||_p <= A`, `||l_w||_(p') <= B`,

uniformly in w. Let c(w) be any measurable real function and put

`Q=T_W+S_W+c(W)`.

Then Q has a density p_Q in C_0(R) and

`||p_Q||_infinity <= AB`.

No continuity or bounded support of the source densities is required.

### Proof

Conditional on W=w, Y and Z remain independent, hence

`p_(Q|W=w)(t)=(k_w*l_w)(t-c(w))`.

Young-Hoelder gives

`||k_w*l_w||_infinity <= ||k_w||_p ||l_w||_(p') <= AB`.

Moreover L^p*L^(p') is contained in C_0. Indeed, for h in R,

`sup_t |(k_w*l_w)(t+h)-(k_w*l_w)(t)|`
` <= ||tau_h k_w-k_w||_p ||l_w||_(p') -> 0`,

and approximation of both factors by compactly supported L^p and L^(p') functions gives vanishing at infinity.

Tonelli supplies the unconditional density

`p_Q(t)=E[p_(Q|W)(t)]`.

The uniform bound AB gives `||p_Q||_infinity<=AB`. For each fixed w the conditional density is continuous and tends to zero at infinity, while its absolute value is bounded by AB. Dominated convergence therefore gives both continuity of p_Q and `p_Q(t)->0` as |t|->infinity. QED.

This lemma cleanly separates the two owner requests. The essential L-infinity estimate is the Young inequality. Continuity is the additional consequence of having two finite conjugate Lp factors; a bounded density by itself would not imply continuity.

## 3. Exact Lp estimate for a general indefinite physical pair

Let F be as in dependency 2. For any p>1 put `alpha=1-1/p`. Since p_far has mass at most one,

`||p_far||_p <= (2sqrt(2)/r)^alpha`.                                           (3.1)

For the near piece set `L=2r^2/kappa`. The exact logarithmic integral is

`int_{|x|<L} log(L/|x|)^p dx`
` = 2L int_0^infinity s^p e^(-s) ds`
` = 2L Gamma(p+1)`.

Hence

`||p_near||_p`
` <= D^(-1/2) [4 Gamma(p+1)/kappa]^(1/p) r^(2/p)`.                            (3.2)

Combining (3.1)-(3.2), for every r>0,

`||p_F||_p <= (2sqrt(2))^(1-1/p) r^(-(p-1)/p)`
`              + D^(-1/2)[4Gamma(p+1)/kappa]^(1/p) r^(2/p)`.                 (3.3)

This is finite for every 1<p<infinity despite the logarithmic point singularity of the pair density.

### The useful p=6 endpoint

For p=6, (3.3) becomes

`||p_F||_6 <= a r^(-5/6)+b r^(1/3)`,

where

`a=2^(5/4)`,

`b=2*3^(1/3)*5^(1/6) D^(-1/2) kappa^(-1/6)`.

At the exact minimizer `r^(7/6)=5a/(2b)`, elementary simplification gives

`||p_F||_6 <= C_pair D^(-5/14) kappa^(-5/42)`,                              (3.4)

with

`C_pair = 7*2^(11/14)*3^(5/21)*5^(-25/42)`
`       = 6.014067979... < 6.015`.

No small coefficient is treated as a small random perturbation; all self-curvature and affine terms inside F are already included in the pair-log source.

## 4. Rough square receiver at the conjugate exponent

Let Z have an arbitrary cap-one density and

`S=gamma Z^2+2wZ+c`, `gamma !=0`.

After completing the square and translating the output, its density h on the relevant half-line obeys

`h(u) <= |gamma|^(-1/2) u^(-1/2)`, `u>0`,                                   (4.1)

and has total mass one. For every 1<q<2, the layer-cake/bathtub extremizer under (4.1) and mass one is the saturated cap on an initial interval. Therefore

`||h||_q <= [2^(q-1)/(2-q)]^(1/q) |gamma|^(-(1-1/q))`.                       (4.2)

For completeness: with `c0=|gamma|^(-1/2)`, choose R by `2c0 sqrt(R)=1`, so `R=1/(4c0^2)`. Then

`int h^q <= int_0^R (c0 u^(-1/2))^q du`
` = [2^(q-1)/(2-q)] c0^(2q-2)`,

which is (4.2).

At the conjugate exponent `q=6/5`,

`||p_S||_(6/5) <= C_sq |gamma|^(-1/6)`,                                     (4.3)

where

`C_sq = sqrt(2)*5^(5/6)/4 = 1.351854683...`.

At q=3/2, (4.2) recovers exactly the partner fleet04/B15 bound `2|gamma|^(-1/3)`.

## 5. New general 2+1 physical continuous-density branch

Partition three ORIGINAL coordinates as (U,V,Z), and suppose their principal block is

`A_I = B direct_sum [gamma]`,                                                (5.1)

where B is invertible symmetric and `gamma !=0`. Every coefficient outside I and every coupling from outside coordinates into U,V,Z may be arbitrary. Condition on all outside original coordinates W. They only generate affine terms in U,V,Z and an output translation; U,V,Z remain mutually independent with their original cap-one densities.

### Indefinite B

Apply (3.4), (4.3), and Lemma 2.1 with p=6. The conditional and hence unconditional density belongs to C_0 and

`||p_Q||_infinity`
` <= C_* D^(-5/14) kappa^(-5/42) |gamma|^(-1/6)`,                            (5.2)

where

`C_* = C_pair C_sq`
`    = 7*2^(-5/7)*15^(5/21)`
`    = 8.130145966... < 8.131`.                                              (5.3)

Thus a well-conditioned indefinite physical pair plus one disjoint square produces a continuous density, uniformly through arbitrary source roughness and arbitrary outside spectrum/couplings.

If both eigenvalues of B have modulus at least one and `|gamma|>=1`, then `kappa>=1`, `D>=1`, and

`boxed:  p_Q in C_0(R),   ||p_Q||_infinity < 8.131.`                         (5.4)

By Cauchy interlacing such a principal block is itself a valid subfamily of the owner's target class.

### Definite B

The pair-log source gives `||p_F||_infinity<=pi/sqrt(D)`. Interpolation gives, for example,

`||p_F||_3 <= (pi/sqrt(D))^(2/3)`.

Together with the q=3/2 square bound, Lemma 2.1 proves continuity. For height, convolution with the probability density of S gives the sharper direct estimate

`boxed: p_Q in C_0(R),   ||p_Q||_infinity <= pi/sqrt(D).`                    (5.5)

In particular, if the two definite pair eigenvalues have modulus at least one, the height is at most pi.

The theorem therefore handles both signatures of any invertible 2x2 pair in the 2+1 physical pattern (5.1), while keeping the indefinite logarithmic singularity rather than asserting a false bounded pair density.

## 6. Required application of the completed partner result

The newest fleet04/B15 theorem is applied to an actual inequality, not only cited. In the special physical block

`[[a,b,0],[b,0,0],[0,0,gamma]]`, `b gamma !=0`,                             (6.1)

condition on every outside coordinate. Fleet04/B15 gives

`||p_T||_3 <= 3|b|^(-2/3)`,

and the same completed result gives

`||p_S||_(3/2) <=2|gamma|^(-1/3)`.

Lemma 2.1 therefore yields

`boxed: ||p_Q||_infinity <= 6|b|^(-2/3)|gamma|^(-1/3),  p_Q in C_0.`          (6.2)

This both verifies the new compiler on a completed partner branch and improves (5.2) on the zero-Y^2 slice. When `b^2>=|a|+1` and `|gamma|>=1`, the partner spectral calculation gives the concrete target inequality

`boxed: ||p_Q||_infinity <=6.`                                                (6.3)

## 7. Absolute continuity versus boundedness versus continuity

For the branch (5.1), the logical implications are now explicit:

1. **Absolute continuity** is already supplied by the finite-Lp pair and square pushforwards and their convolution.
2. **Essential boundedness** follows from conjugate-exponent Young, with (5.2) in the indefinite case and (5.5) in the definite case.
3. **Continuity** is strictly stronger and is proved here from `L^p*L^(p') subset C_0`; it is not inferred from the L-infinity cap.

The argument is source-rough from the beginning. It does not mollify the original product law, evaluate a conditional projected density on a quadratic surface, or invoke an unjustified limit interchange.

## 8. What this does not solve

The unrestricted three-large-eigenvalue conjecture remains OPEN. The bare spectral hypothesis does not force an original-coordinate principal block of the block-diagonal 2+1 form (5.1), let alone one with uniformly conditioned B. A general three-coordinate core can have nonzero UZ and VZ couplings, and removing them by an orthogonal rotation would destroy independence of the source coordinates. High-leverage/grouped-bank families can also spread the needed curvature over many coordinates so that every individual physical pair is poorly conditioned.

The first unpaid extension of the present mechanism is therefore precise: replace the disjoint-square requirement in (5.1) by a grouped-coordinate or slice receiver that tolerates pair-to-third-coordinate cross terms while retaining original-coordinate product provenance and a finite conjugate Lp norm. One cannot close that step by a general rotation, a worst fiber supremum, or the refuted arbitrary-joint coarea lemma.

## 9. Integrity

- Full QFORM: OPEN / NOT PROVED / NOT DISPROVED.
- New supporting lemma: conditional rough `L^p-L^(p')` convolution implies a bounded `C_0` density.
- New quantitative branch: general indefinite physical pair plus disjoint square, bound (5.2), with universal `<8.131` when all three block eigenvalues have modulus at least one.
- Definite 2+1 branch: continuous density with height at most `pi/sqrt(D)`.
- Completed fleet04/B15 applied at equations (6.2)-(6.3).
- No universal continuity modulus is claimed.
- No pointwise van-der-Corput decay, post-rotation independence, arbitrary-joint coarea, moment assumption, support restriction, or Monte Carlo evidence is used.
