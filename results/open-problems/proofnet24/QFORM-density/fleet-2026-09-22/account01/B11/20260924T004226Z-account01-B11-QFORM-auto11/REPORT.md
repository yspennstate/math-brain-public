SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B11, 2026-09-24T00:42:26Z.
attacking: the rank-one transverse shared-hub collar; prove that bilateral off-axis leakage forces a genuine rank-three source crossing and pay it by the completed account02/B11 three-bank theorem.

# account01/B11 — rank-one transverse crossing with bilateral leakage

Programme: `QFORM-DENSITY-3EIG-20260922`.
Status: **NEW EXACT STRUCTURAL IDENTITY / PARTNER RESULT APPLIED / NEW CONTINUOUS SUBBRANCH / FULL QFORM OPEN**.
Execution: `WITHOUT_VERIFIED_BRAIN` (authenticated GitHub repository retrieval was used, but repository transport is not being represented as verified native brain ingestion).

The full owner target remains open. This report continues the exact-rank-three indefinite shared-hub analysis from the preceding B11 rank-two-transverse theorem. It closes the rank-one-transverse branch when both off-axis leakage vectors are nonzero. It does not close the one-sided leakage endpoint, the vanishing-transverse-crossing endpoint, or arbitrary additional nonseparable spectrum.

No Gaussianity, log-concavity, moments, bounded/connected support, diagonal-basis independence, conditional-density-cap shortcut, arbitrary-joint coarea theorem, pointwise law-uniform van-der-Corput decay, or deletion of a small nonzero coefficient is used.

## 1. Source state and dependencies

Fresh control read from `yspennstate/math-research-brain` main during this run retained OWNER CONTROL revision `2026-09-22.15`, active programme `QFORM-DENSITY-3EIG-20260922`, and the full conjecture as OPEN. `AGENTS.md`, `scheduled_tasks/README.md`, `scheduled_tasks/fleet.json`, `scheduled_tasks/roles.json`, `scheduled_tasks/PROTOCOL.md`, the programme `MANIFEST.json`, `CURRENT_RESEARCH.md`, `CLAIMS.json`, live `CORRECTION_INBOX.json`, `MEMORY_PROTOCOL.md`, and the account01/B11 assignment were refreshed. The existing canonical login for account01/B11 in UTC hour `2026-09-24T00Z` was preserved rather than overwritten.

The immediate inherited B11 theorem is:

`yspennstate/math-open-problems@fc8a0b4bb5856e26723fbbce97474eac66ec8bfb:proofnet24/QFORM-density/fleet-2026-09-22/account01/B11/20260923T234226Z-account01-B11-QFORM-auto11/REPORT.md`.

For a physical hub `i`, disjoint ORIGINAL-coordinate banks `L,R`,

`a=A_ii`, `c=A[L,i]`, `r=A[i,R]`, `N=A[L,R]`,

`alpha=||c||_2`, `beta=||r||_2`, `e=c/alpha`, `f=r/beta`, and

`C=P_e N P_f`,

that theorem proves `rank C<=2`. If `rank C=2`, then `a!=0`, `rank N=3`, and

`Delta_3(N)=alpha beta D_2(C)/|a|`,

which, after the scalar-pivot/crossing interpolation, pays that branch continuously. Hence the first genuinely different endpoint is `rank C<=1`.

The completed partner theorem actually applied below is account02/B11's three-dimensional cross-bank estimate, source-pinned in the preceding B11 report to canonical mathematics

`yspennstate/math-open-problems@25c25e15fa0f570e7b0b1a2a9fab0811eda07113:proofnet24/QFORM-density/fleet-2026-09-22/account02/B11/20260923T201026Z-account02-B11-QFORM-auto11/REPORT.md`.

For two source-disjoint ORIGINAL-coordinate product banks, arbitrary within-bank quadratic/affine phases, and a rank-three cross matrix `K`, it yields

`||p_Q||_infinity <= 6 Delta_3(K)^(-1/3)`

with a continuous `C_0` density, where `Delta_3(K)` is the product of the three nonzero singular values. This is the partner result used at an actual inequality in Section 4.

The newest account02/B11 handoff read in this run, canonical math commit `87c8e16cf9e56242b702321f91e2043e9a44972e`, supplies a complementary `L2` hyperbolic-pair receiver and preserves the logarithmic rank-two obstruction. The newest account03/B11 r45 handoff, canonical math commit `12e2174445fbc824279bf1376da1346454d7060a`, identifies the exact near-coloop puncture model and likewise leaves an orthogonal-product-projection collar open. Neither source claims the bilateral-leakage identity below.

## 2. Canonical rank-one-transverse block

Let `A` be real symmetric with `rank A<=3`. Fix one ORIGINAL coordinate `i` and disjoint ORIGINAL-coordinate sets `L,R`, disjoint also from `{i}`. Consider the rectangular submatrix with rows `{i} union L` and columns `{i} union R`:

```
B = [ a    r^T ]
    [ c     N  ].
```

Assume `c!=0`, `r!=0`, define `alpha,beta,e,f` as above, and suppose now

`rank C = rank(P_e N P_f)=1`.

Let `sigma>0` be its unique nonzero singular value and choose unit singular directions `u in e^perp`, `v in f^perp` so that

`C = sigma u v^T`.

Decompose

`e^perp = span{u} direct_sum E_0`,
`f^perp = span{v} direct_sum F_0`.

In the resulting orthonormal source bases, `B` has the exact form

```
B ~ [ a      beta    0       0   ]
    [ alpha  d       q1      q0^T]
    [ 0      p1      sigma   0   ]
    [ 0      p0      0       0   ],
```

where

`p0 = P_{E_0} N f`,
`q0 = P_{F_0} N^T e`.

Thus `p0` and `q0` are the two off-axis leakage vectors not seen by the rank-one transverse operator `C`. No random variable has been rotated and declared independent; these are deterministic orthogonal changes used only to analyze matrix rank and singular values.

Eliminating the invertible scalar block `sigma` by exact row/column operations gives

`rank B = 1 + rank R`,

with

```
R = [ a      beta    0   ]
    [ alpha  delta   q0^T]
    [ 0      p0      0   ],
```

and

`delta = d-q1 p1/sigma`.

Because `B` is a submatrix of `A`, `rank B<=3`, hence

`rank R<=2`.                                                     (2.1)

## 3. New theorem: bilateral leakage forces zero pivot and rank-three crossing

### Theorem 3.1 — `QFORM-RANK1-TRANSVERSE-DOUBLELEAKAGE-v1`

Under the hypotheses of Section 2, assume additionally

`p0!=0` and `q0!=0`.

Then:

1. the physical pivot vanishes exactly,

`a=A_ii=0`;                                                     (3.1)

2. the ORIGINAL-coordinate interbank crossing `N=A[L,R]` has rank exactly three;

3. writing `Delta_3(N)` for the product of its three nonzero singular values,

`Delta_3(N)=sigma ||p0||_2 ||q0||_2`.                          (3.2)

In particular, a rank-one transverse crossing plus bilateral off-axis leakage is not a rank-two source interaction: exact rank three reconstructs an honest three-dimensional source-crossing volume.

### Proof

Choose unit vectors `p_hat=p0/||p0||` and `q_hat=q0/||q0||`. The `3x3` minor of the residual matrix `R` in (2.1), using rows `(hub,e,p_hat)` and columns `(hub,f,q_hat)`, is

```
[ a      beta    0      ]
[ alpha  delta   ||q0|| ]
[ 0      ||p0||  0      ].
```

Its determinant is

`-a ||p0|| ||q0||`.

Since `rank R<=2` and both leakage norms are positive, this determinant must vanish, proving `a=0`.

Now analyze `N` itself in the same orthonormal bases:

```
N ~ [ d    q1      q0^T]
    [ p1   sigma   0   ]
    [ p0   0       0   ].
```

Eliminating the `sigma` entry leaves the residual block

```
S = [ delta   q0^T]
    [ p0      0   ].
```

Because `p0,q0` are both nonzero, `S` has rank two. Therefore `rank N=1+rank S=3`.

Finally rotate only inside the null source spaces `E_0,F_0` so that `p0=||p0|| e_1` and `q0=||q0|| f_1`. All remaining rows and columns are identically zero. Hence `N` is orthogonally equivalent to one active `3x3` matrix plus zero rows/columns. Its determinant, after the same exact elimination, is

`-sigma ||p0|| ||q0||`.

For a rank-three rectangular matrix supported on a `3x3` active block, the product of the three nonzero singular values is the absolute determinant of that active block. This proves (3.2). QED.

### Corollary 3.2 — nonzero pivot implies one-sided leakage

Still in the rank-one-transverse branch,

`a!=0  =>  p0=0 or q0=0`.                                     (3.3)

Thus the genuinely bilateral leakage geometry is confined to the exact zero-pivot endpoint. Conversely, at zero pivot, bilateral leakage itself automatically creates the missing third source direction.

## 4. Actual partner-theorem application: a continuous density bound

Now assume `A=R M R^T` has exact rank three, `R^T R=I_3`, and `M` is invertible with indefinite signature `(2,1)` or `(1,2)`. Keep the source-disjoint ORIGINAL-coordinate banks `L,R`, and suppose the hypotheses of Theorem 3.1 hold.

Condition on the ORIGINAL hub variable `X_i` and every ORIGINAL coordinate outside `L union R union {i}`. This conditioning preserves independence between the `L` bank and the `R` bank. Every hub/outside term becomes an affine term internal to one bank, while `A[L,L]` and `A[R,R]` remain arbitrary within-bank quadratic phases. The only interbank quadratic term is

`2 X_L^T N X_R`.

Theorem 3.1 gives `rank N=3` and

`Delta_3(N)=sigma ||p0|| ||q0||`.

Applying the completed account02/B11 three-dimensional cross-bank theorem uniformly in all conditioned values therefore gives

`||p_Q||_infinity <= 6 [sigma ||p0|| ||q0||]^(-1/3)`.          (4.1)

The same uniform Fourier envelope gives a continuous `C_0` conditional density and hence a continuous `C_0` unconditional density after averaging. No post-rotation independence is used: the only probabilistic split is the original-coordinate partition `L | R | conditioned complement`.

Equation (4.1) has the correct scale. If `A` is multiplied by `s`, then each of `sigma,||p0||,||q0||` scales by `s`; the bracket scales by `s^3`, and the density bound scales by `s^{-1}`.

For the normalized quantitative subbranch

`sigma>=eta_1 s`, `||p0||>=eta_2 s`, `||q0||>=eta_3 s`,

(4.1) becomes

`||p_Q||_infinity <= 6 (eta_1 eta_2 eta_3)^(-1/3) s^(-1)`.     (4.2)

This is the promised actual application of a completed account02/B11 result to the live rank-one collar.

## 5. Relation to the shared-hub rank-one tensor receiver

The completed account03/B11 rank-one shared-hub tensor theorem pays a different currency involving the star strengths and the rank-one transverse crossing, schematically

`T = alpha^2 beta^2 sigma^2`.

The new theorem pays the complementary bilateral-leakage currency

`L = sigma^2 ||p0||^2 ||q0||^2`.

Therefore a rank-one transverse collar with substantial star geometry or substantial bilateral leakage has two independent exact exits. What is not yet proved is that the bare three-large-eigenvalue hypothesis forces either currency to be uniformly large. If `sigma`, one leakage vector, or both are small, the third spectral direction may reside in same-bank curvature, and that curvature cannot be discarded for arbitrary unbounded-support inputs.

## 6. Mandatory opposite-sign rank-two control and the role of the third direction

For centered unit uniforms `X,Y`,

`p_{2XY}(t)=log(1/(2|t|)),  0<|t|<1/2`.

Thus one opposite-sign rank-two hyperbolic pair genuinely has an unbounded density. Any proof that silently declares it bounded is wrong.

Theorem 3.1 gives a precise third-direction mechanism in the present rotated shared-hub geometry. The visible transverse operator `C` has only rank one, so by itself it still resembles a rank-two saddle. But if both source-side leakages survive, exact rank three forces the full interbank crossing to have three-dimensional singular volume

`Delta_3(N)=sigma ||p0|| ||q0|| >0`.

That third source volume is exactly what allows the completed three-dimensional cross-bank estimate to replace the logarithmic singularity by an integrable three-direction Fourier/coarea bound. At the exact zero pivot the third direction is therefore not a hidden independent eigen-coordinate and not a scalar square; it is reconstructed from the two opposite leakage vectors in the ORIGINAL-coordinate product geometry.

## 7. Exact remaining implication

The rank-one-transverse shared-hub collar is now reduced to the one-sided/degenerate cases

`rank(P_e N P_f)<=1`, with either

`p0=0` or `q0=0`,

or to the quantitative collar where `sigma ||p0|| ||q0||` is small. In particular, by (3.3), every nonzero-pivot rank-one-transverse case is necessarily one-sided.

The next B11 target is therefore

`QFORM-R43-ONESIDED-RANK1-SAMEBANK-CURVATURE-v1`:

retain the surviving same-bank quadratic curvature and prove a uniform receiver when one off-axis leakage vector vanishes (including the `sigma->0` transition), or force an already-paid physical-pair, scalar-pivot, volume, rank-one tensor, projective-bank, or hyperbolic-pair exit. The newest account02/B11 `L2` hyperbolic receiver pays genuinely source-disjoint second pairs, but does not justify treating two projections of one product bank as independent. The newest account03/B11 puncture normal form likewise shows that the residual orthogonal product-projection provenance must be retained.

Arbitrary additional nonseparable spectrum remains a separate bridge beyond exact rank three.

## 8. Finite algebra check

A deterministic numerical checker accompanying this report generated 5,000 random canonical rank-one-transverse bilateral-leakage blocks with `a=0`. In every case the block had rank three and

`Delta_3(N)=sigma ||p0|| ||q0||`

held with maximum relative discrepancy below `9.2e-15`. A separate 2,000-instance check with `a!=0` and both leakages nonzero always produced rank four, verifying the contrapositive of (3.1) at finite precision. These checks support the exact algebra but are not substitutes for the proof above.

## 9. Scope/status

- New theorem scope: exact rank-three (or rank<=3 for the structural identity), rank-one transverse shared-hub block, bilateral off-axis leakage.
- Density conclusion in the paid branch: bounded and continuous `C_0`.
- Full QFORM conjecture: OPEN.
- Full-target continuity: OPEN.
- No counterexample to the owner conjecture is claimed.
- `WITHOUT_VERIFIED_BRAIN` retained: repository retrieval/use is documented separately from native brain ingestion.
