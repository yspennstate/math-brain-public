SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B02, 2026-09-24T06:27:14Z.
attacking: the critical rank-two Fourier endpoint behind the live carrier-aligned hub; upgrade the robust physical E2 packet from half-Riesz credit to a row-gate-free weak-L1 characteristic bound, all finite L^r output densities, and an epsilon-log(1/epsilon) small-ball estimate, then apply the newest account02/B02 receiver to the actual full-cut inequality.

# account01/B02 r46 — row-gate-free E2 critical Fourier endpoint and all finite L^r densities

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Integrated Fourier estimate  
Status: **ESSENTIAL_STEP_APPLIED / FULL QFORM OPEN / TARGET-WIDE FOURIER-L1 OPEN_NOT_REFUTED**  
Regularity: the new E2 theorem proves absolute continuity and `L^r` density for every finite `r>=2`; it does **not** prove `L^infinity` or continuity. Fourier-L1 branches cited separately below do give continuous `C0` densities.  
Brain status: `WITHOUT_VERIFIED_BRAIN`.

The exact owner target is unchanged: independent ORIGINAL real coordinates with one-dimensional probability densities at most one; arbitrary real symmetric `A`; at least three eigenvalues of modulus at least one. No Gaussianity, log-concavity, moment, compact/connected support, iid assumption, post-rotation independence, conditional projection-density cap, arbitrary-joint coarea bound, pointwise scalar quadratic-phase decay, or deletion of a nonzero coefficient tail is used.

## 1. Fresh controls and immutable mathematical sources actually used


The immediate account01/B02 predecessor is source-pinned at

`yspennstate/math-open-problems@acf321dcae5b20ea42cf55f84ced68433498a9f5`,

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B02/20260924T052052Z-account01-B02-qform-auto11-r45/REPORT.md`.

Its live unpaid carrier packet contains a literal full physical cut

`N=A[L,R]`, `L disjoint R`, `L union R=[n]`,                         (1.1)

with squared singular values `x1>=x2>=...` satisfying

`x1*x2 > kappa := 247/576`,                                        (1.2)

and, outside the already-paid transverse-E3 / near-coloop branches, a physical hub `i` and hub-disjoint block `N_(-i)` satisfying

`max_j |A_jj| < 1/222`,
`g_i > 1/(222 sqrt(2))`,
`Z := E2(N_(-i)) > Z0 := 247/2304`.                                (1.3)

The completed row-gate-free E2 half-Riesz compiler used and strengthened below is

`yspennstate/math-open-problems@cd0be625c8f7143a46ad14bb936e9c24bfb19a8d`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B06/b06-20260923T192839Z-auto11/REPORT.md`.

The newest completed designated partner read and applied below is account02/B02 auto12,

`yspennstate/math-open-problems@19a3d60ceb5d0989aa527b32d3e76f388b9419f6`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B02/20260924T060210Z-account02-B02-QFORM-auto12/REPORT.md`.

Its new theorem `QFORM-RANK2-ONEBANK-LINEAR-DENSITY-v1` states: if a literal physical cross block `M` has two positive singular values `s1>=s2>0`, one bank has arbitrary same-bank curvature, and the opposite bank is genuinely untwisted (its quadratic block is exactly zero after outside conditioning; affine terms are arbitrary), then

`||p_Q||_infinity <= 2 sqrt(pi) (s1 s2)^(-1/2)`.                  (1.4)

It also proves a stronger Fourier-L1 theorem for a literal invertible physical `2x2` crossing under the same one-sided-twist condition. I do not extend either theorem to arbitrary two-sided curvature; the partner's Gaussian/collapse obstruction makes that extension invalid without a third resource.

## 2. New theorem — the row-gate-free E2 proof actually retains a critical Fourier envelope

Let `I,J` be disjoint ORIGINAL-coordinate banks and let

`M=A[I,J]`,
`Z=E2(M)=e_2(M^T M)>0`.                                            (2.1)

All coordinates outside `I union J` may be conditioned on. Same-bank quadratic blocks, arbitrary affine terms, and every outside coupling are retained exactly.

### Theorem 2.1 — `QFORM-E2-CRITICAL-FOURIER-ALLFINITE-LR-v1`

For every admissible product law and every real `t!=0`,

`boxed:
 |phi_Q(t)| <= min{1, K_Z/|t|},
 K_Z := 2 pi sqrt(e) Z^(-1/4).
}`                                                                  (2.2)

Consequently:

1. `phi_Q` belongs to weak `L^1(R)` and to `L^p(R)` for every `p>1`;
2. `Q` is absolutely continuous;
3. for every finite `r>=2`, its density satisfies

`boxed:
 ||p_Q||_r <= [ K_Z r / pi ]^((r-1)/r)
             = [ 2 sqrt(e) r Z^(-1/4) ]^((r-1)/r).
}`                                                                  (2.3)

Thus a positive physical E2 packet buys **every finite density norm**, with the exact remaining loss linear in `r` as `r->infinity`. The theorem does not claim `r=infinity`.

### 2.1 Proof of the row-gate-free characteristic envelope

The source E2 compiler normalizes the squared literal `2x2` minors by `Z` and lets `alpha_i` be the natural row-pair inclusion marginal. Its proof is exhaustive.

**Diffuse minor law.** If every `alpha_i<=1/2`, the completed `D_2` estimate gives directly

`|phi_Q(t)|
 <= min{1, 2 pi sqrt(e) Z^(-1/4) |t|^(-1)}`.                     (2.4)

**Heavy physical row, diffuse projected residual.** If some row has `alpha_i>1/2`, write its cross row as `m` and the orthogonal residual block as `C`, with `F=||C||_F`. The exact aggregate identity in the source is

`||m||^2 F^2 = alpha_i Z`.                                        (2.5)

In the diffuse projected-row subcase its grouped-hub theorem gives

`|phi_Q(t)|
 <= min{1, 2 pi (alpha_i Z)^(-1/4)|t|^(-1)}`.                    (2.6)

Since `alpha_i>1/2` and `2^(1/4)<sqrt(e)`, (2.6) is stronger than (2.2).

**Heavy physical row, one concentrated projected row.** The source produces a literal two-row crossing area `S_2` with

`S_2 > sqrt(Z)/2`                                                  (2.7)

and its exact-rank-two crossing estimate gives

`|phi_Q(t)|
 <= min{1, pi sqrt(2) S_2^(-1/2)|t|^(-1)}
 <  min{1, 2 pi Z^(-1/4)|t|^(-1)},                                (2.8)

again stronger than (2.2).

These three cases are exhaustive, so the single envelope (2.2) is row-gate-free. Notice what is being bounded: the **full coupled quadratic characteristic function** through a genuine physical rank-two crossing. This does not contradict the live correction refuting a law-uniform pointwise decay bound for one isolated scalar chirp.

### 2.2 Every finite `L^r` density norm

Fix `1<p<=2`. From (2.2), splitting the frequency integral at `K_Z`,

`||phi_Q||_p^p
 <= 2 K_Z + 2 K_Z^p integral_(K_Z)^infinity t^(-p) dt
 = 2 K_Z p/(p-1).`                                                 (2.9)

Put `r=p/(p-1)`, so `r>=2`. To avoid assuming a density before proving it, mollify the law by an independent centered Gaussian of variance `delta^2`. Its density has Fourier transform

`phi_Q(t) exp(-delta^2 t^2/2)`.

Inverse Hausdorff--Young, with our convention `hat f(t)=integral e^(itx)f(x)dx`, gives

`||p_delta||_r <= (2 pi)^(-1/p) ||phi_Q||_p`.                     (2.10)

The right side is independent of `delta`. Since finite `r>1` is reflexive, take a weakly convergent `L^r` subsequence as `delta->0`; the corresponding measures converge weakly to the original law, hence the weak `L^r` limit is its density. Combining (2.9)-(2.10) and using `p/(p-1)=r` gives exactly

`||p_Q||_r
 <= (2 pi)^(-1/p) (2 K_Z r)^(1/p)
 = (K_Z r/pi)^((r-1)/r).`                                        (2.11)

This proves (2.3). The endpoint `p=1`, equivalently `r=infinity`, is precisely where the `|t|^-1` integral diverges.

## 3. Near-linear small-ball control with only one logarithm left

The same critical Fourier envelope yields a sharper concentration statement than the previously recorded half-Riesz `O(sqrt(epsilon))` estimate.

For every `epsilon>0` and every level `s`, use

`1_{|x-s|<=epsilon}
 <= exp(1/2) exp(-(x-s)^2/(2 epsilon^2)).`                         (3.1)

The Gaussian Fourier identity and (2.2) give

`P(|Q-s|<=epsilon)
 <= exp(1/2) epsilon/sqrt(2 pi)
    integral_R exp(-epsilon^2 t^2/2)|phi_Q(t)|dt`.                 (3.2)

Let `E1(x)=integral_x^infinity exp(-u) du/u`. Splitting at `K_Z` gives the exact convenient bound

`boxed:
 P(|Q-s|<=epsilon)
 <= sqrt(e/(2 pi)) epsilon K_Z
    [2 + E1((epsilon K_Z)^2/2)].
}`                                                                  (3.3)

For `epsilon K_Z<=1`, `E1(x)<=log(1/x)+1`; simplifying yields the all-scale statement

`boxed:
 sup_s P(|Q-s|<=epsilon)
 <= min{1,
    sqrt(2e/pi) epsilon K_Z
    [2+log_+(1/(epsilon K_Z))] }.
}`                                                                  (3.4)

Thus the E2 packet misses linear small-ball control by only a single logarithm. This is consistent with the exact two-large-eigenvalue hyperbolic controls, where a logarithmic density singularity really occurs. The target's third spectral resource must remove this endpoint log; E2 alone cannot do so.

## 4. Quantitative application to the live account01/B02 carrier packet

On the current unpaid branch, (1.3) gives

`Z > Z0=247/2304`.                                                  (4.1)

Therefore

`K_Z < K0
 := 2 pi sqrt(e) (2304/247)^(1/4)
 = 18.103956177059132... .`                                        (4.2)

The live carrier packet now has an actual density, and for every finite `r>=2`,

`boxed:
 ||p_Q||_r
 < [ 2 sqrt(e) (2304/247)^(1/4) r ]^((r-1)/r)
 < [5.762669 r]^((r-1)/r).
}`                                                                  (4.3)

Also, uniformly in the target level,

`boxed:
 P(|Q-s|<=epsilon)
 < min{1,
  23.815560 epsilon
  [2+log_+(1/(18.103957 epsilon))] }.
}`                                                                  (4.4)

This is a strict analytic strengthening of the prior half-Riesz statement `O(sqrt(epsilon))`: the only remaining concentration loss is logarithmic. It also proves absolute continuity on this live branch, though not boundedness or continuity of the density.

## 5. Required equation-level application of the newest account02/B02 partner

The newest designated partner auto12 proves the one-bank theorem (1.4) for an arbitrary physical cross block. Apply it to the **actual live full cut** `N` from (1.1)-(1.2). If either bank is genuinely untwisted after outside conditioning, transpose if necessary so that it is the partner's `V` bank. The two leading singular values satisfy

`s1*s2 = sqrt(x1*x2) > sqrt(kappa)`,
`kappa=247/576`.                                                    (5.1)

Feeding this literal inequality into the partner theorem gives

`boxed:
 ||p_Q||_infinity
 < 2 sqrt(pi) kappa^(-1/4)
 = 4.380627392825819... .
}`                                                                  (5.2)

This is an **essential-density** payment; the partner explicitly does not infer continuity from its broad one-bank theorem. Its separate fully-entangled physical `2x2` theorem does give genuine Fourier `L1` and a continuous `C0` density whenever a literal invertible `2x2` source crossing is isolated with the same one-sided-twist hypothesis.

Therefore a still-unpaid carrier packet is now forced into a genuinely **two-sided-twisted** configuration: both physical banks carry nonzero same-bank quadratic curvature that cannot be silently discarded even if its coefficient norm is small. This sharpens the local frontier; it is not an assumption added to the owner target.

## 6. What this resolves and the first unpaid implication

The full conjecture remains OPEN. The target-wide universal unweighted Fourier-L1 assertion also remains `OPEN_NOT_REFUTED`; no exact-target counterexample was found in this run.

The new result changes the live B02 endpoint as follows.

- A robust physical E2 packet no longer means merely finite half-Riesz credit. It implies the full characteristic envelope (2.2), weak `L1` in frequency, absolute continuity, every finite density norm (2.3), and the near-linear logarithmic small-ball profile (3.4).
- On the concrete carrier branch `E2>247/2304`, the constants are dimension-free and explicit in (4.2)-(4.4).
- The newest account02/B02 theorem completely pays the one-sided-twist version of the same robust rank-two crossing at height `<4.381`.
- Hence the only endpoint left at this interface is a **two-sided-twisted** rank-two crossing plus the fixed physical carrier hub / overlap-one third resource. The third resource must remove exactly one critical logarithm.

The first unpaid B02 implication is therefore

`QFORM-E2-EXP-L-ENDPOINT-PLUS-CARRIER-HUB-TWOSIDED-TWIST-v1`:

starting from the live `E2>247/2304` packet, the physical carrier-aligned hub, and genuine quadratic curvature on both banks, prove a uniform endpoint upgrade from (2.2)/(3.4) to Fourier `L1` or linear small-ball `O(epsilon)`. A correction-safe route is to retain the actual hub modulation and prove decay of the residual mixed norm before taking a supremum; alternatively physicalize one bank's twist into an overlap-one/grouped-pivot packet and invoke the partner's fully-entangled one-sided receiver. Do not delete a small twist, rotate the random variables, or infer `L^infinity` merely from all finite `L^r` norms.

## 7. Integrity / regularity ledger

- Full QFORM: **OPEN / not proved / not disproved**.
- Full-target continuity: **OPEN**.
- Target-wide universal `integral |phi_Q|`: **OPEN_NOT_REFUTED**.
- New E2 theorem: proves absolute continuity and `p_Q in L^r` for every finite `r>=2`; no `L^infinity`, no continuity.
- New logarithmic small-ball theorem: (3.3)-(3.4), uniform in dimension/laws/level.
- Newest account02/B02 one-bank subbranch: essential density `<4.381`; continuity not claimed by that theorem.
- Existing physical-E3 / spectral-window branches remain genuine Fourier-L1 branches with continuous `C0` density.
- The refuted scalar pointwise van-der-Corput route, post-rotation independence, arbitrary-joint coarea, fiber-sup integration, coefficient-tail deletion, and `E2 => L^infinity` shortcut are not used.

Model self-report: GPT-5.6 Sol. Configured thinking level and provider reasoning telemetry are not exposed and are recorded as `UNKNOWN/null`.
