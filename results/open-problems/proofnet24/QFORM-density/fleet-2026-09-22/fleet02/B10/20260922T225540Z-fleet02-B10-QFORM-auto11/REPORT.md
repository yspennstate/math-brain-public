SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B10, 2026-09-22T22:55:40.916405Z.
attacking: the heavy-null double-small-leakage chamber: seek an exact product-preserving bank shear or three-bank determinant that uses generated mismatch before any conditional-profile supremum.

# fleet02/B10 — tripartite heavy-hub delete-or-isolate reduction

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** rank-three coupled case; complementary constructions/source-valid counterexamples  
**Run:** `20260922T225540Z-fleet02-B10-QFORM-auto11`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_LEMMA / LOCAL_CANDIDATE_REFUTED`; full QFORM remains OPEN / NOT PROVED.

## 1. Exact target and correction discipline

The target is unchanged: the original coordinates are independent real random variables with densities at most one, and the real symmetric matrix has at least three eigenvalues of absolute value at least one. No moments, support bounds, Gaussianity, log-concavity, or independence after spectral rotation are assumed.

The live correction state was re-read before this report. In particular, arbitrary-joint coarea, positive conditional projection-height moments, pointwise law-uniform Fresnel decay, conditional-cap-as-independence, and reciprocal-single-minor completion are unavailable. The argument below never conditions on a spectral projection and never replaces the original product law by a projected product law. Every conditioning operation is on ORIGINAL coordinates.

## 2. Named partner result actually used

The designated partner fleet03/B10 completed r20 at

`yspennstate/math-open-problems@7acd371ee2ee83a7fae12d7bedb38bc99c051b6d`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B10/20260922T221548Z-fleet03-B10-QFORM-r20/REPORT.md`.

Its `QFORM-MIXEDBANK-TRIPARTITION-v1` and `QFORM-TRIPARTITE-GRAM-CERTIFICATE-v1` give, in every surviving exact-rank-three near-span branch, three disjoint ORIGINAL-coordinate banks `B1,B2,B3` with spectral rows `r_i in R^3`, selected Gram

`G = sum_{i in B1 union B2 union B3} r_i r_i^T <= I_3`,

and tripartite exterior packet

`T = sum_{i in B1,j in B2,k in B3} det(r_i,r_j,r_k)^2 >= 1/256`.

The inherited exact-rank-three spectral matrix `M` satisfies `|det M|>=1/2` and `sigma_min(M)>=1/2`; partner r20 also proves `det G>=1/256` and `lambda_min(G)>=1/256`.

Whiten only the deterministic spectral coefficient geometry:

`v_i = G^{-1/2} r_i`,

so `sum_i v_i v_i^T=I_3`, and put

`N = G^{1/2} M G^{1/2}`.

This is an algebraic representation of the same quadratic block on the same original coordinates; it is not a probabilistic rotation. Partner r20 gives

`|det N|>=1/512`, `sigma_min(N)>=1/512`.

The tripartite packet after whitening is

`Tbar = sum_{i in B1,j in B2,k in B3} det(v_i,v_j,v_k)^2 = T/det G >= T >= 1/256`.

This displayed inequality is the concrete use of the named partner result in the new argument.

## 3. New supporting lemma: a heavy hub can be deleted or isolated without losing rank three

### Lemma — `QFORM-TRIPARTITE-HEAVY-HUB-DELETE-OR-ISOLATE-v1`

Assume the normalized tripartite state above. Let `h in B1` be a heavy row and write

`v=v_h`, `L=||v||^2>1/2`.

Then at least one of the following alternatives holds.

**A. Deletable hub.** `1-L>=1/512`. After conditioning on the original coordinate `X_h` (and, when applying a conditional density theorem, on every original coordinate outside the remaining selected set), the residual exact-rank-three block has a normalized spectral matrix `N_-` satisfying

`|det N_-|>=2^{-18}`, `sigma_min(N_-)>=2^{-18}`.

**B. Isolatable hub.** There is a fixed-hub two-bank exterior packet

`T_h := sum_{j in B2,k in B3} det(v,v_j,v_k)^2 >=1/512`.

After conditioning on the original coordinates in `B1\{h}` (and outside the selected core), the active set `{h} union B2 union B3` is still exact rank three. Its normalized spectral matrix `N_h` satisfies

`|det N_h|>=2^{-18}`, `sigma_min(N_h)>=2^{-18}`.

Consequently, in either alternative, if the newly active normalized physical frame is diffuse (all normalized leverages at most `1/2`), the reviewed Fresnel--Brascamp--Lieb theorem used by partner r20 yields the explicit conditional and hence unconditional bound

`||p_Q||_infinity <= 12 (2^{-18})^{-1/3}=768`.

#### Proof

Split the tripartite packet into the triples using `h` and those not using it:

`Tbar = T_h + T_rest`.

The residual rows `S\{h}` have Gram

`H = I_3-vv^T`.

By Cauchy--Binet, the sum of squared determinants over ALL three-row minors of the residual frame equals `det H`. The tripartite residual packet `T_rest` is a sub-sum of these nonnegative minors. Hence

`T_rest <= det(I_3-vv^T)=1-L`,

where the last equality is the rank-one matrix determinant lemma. Therefore

`T_h >= Tbar-(1-L)`.                                          (3.1)

If `1-L>=1/512`, then `H` is positive definite with eigenvalues `1,1,1-L`. Conditioning on the ORIGINAL coordinate `X_h` preserves independence of all residual original coordinates; couplings to `X_h` become an arbitrary affine term. Whitening the residual coefficient geometry gives

`N_- = H^{1/2} N H^{1/2}`.

Thus

`|det N_-| = (1-L)|det N| >= (1/512)^2=2^{-18}`,

and

`sigma_min(N_-) >= lambda_min(H) sigma_min(N) >= (1/512)^2=2^{-18}`.

This proves Alternative A.

If Alternative A fails, then `1-L<1/512`. Since `Tbar>=1/256`, (3.1) gives

`T_h > 1/256-1/512 = 1/512`.

Let

`K = vv^T + sum_{j in B2} v_jv_j^T + sum_{k in B3}v_kv_k^T`.

This is a sub-Gram of the Parseval frame, so `0<K<=I_3`. Cauchy--Binet for `det K` contains all fixed-hub `B2-B3` minors among its nonnegative terms, hence

`det K >= T_h >=1/512`.

Because all eigenvalues of `K` are at most one, `lambda_min(K)>=det K>=1/512`. Condition on ORIGINAL coordinates in `B1\{h}`; the remaining active variables `{h} union B2 union B3` are still mutually independent at the coordinate level, and the active quadratic matrix is represented after whitening by

`N_h=K^{1/2} N K^{1/2}`.

Therefore

`|det N_h|=det K |det N|>=2^{-18}`,

`sigma_min(N_h)>=lambda_min(K)sigma_min(N)>=2^{-18}`.

This proves Alternative B.

Finally, in either alternative the active matrix has determinant magnitude at least `2^{-18}`. If its normalized row leverages are all at most one half, the reviewed diffuse-core Fresnel--Brascamp--Lieb theorem applied exactly as in partner r20 gives `12|det N_active|^{-1/3}<=768`, uniformly in every conditioned affine shift. Averaging the conditional densities preserves the same bound. QED.

## 4. Why this is new relative to the previous B10 leakage split

The previous B10 endpoint tracked two small leakage parameters and risked another local reciprocal-minor payment. The lemma above changes mechanism: first use the partner's full tripartite determinant packet, then use Cauchy--Binet and the determinant lemma before any local inversion.

The point is topological as well as quantitative. A heavy normalized physical row cannot simultaneously (i) be too close to unit leverage and (ii) avoid carrying a constant amount of the tripartite exterior packet. If it is not close to unit leverage, it may be conditioned away while leaving a uniformly nonsingular exact-rank-three residual block. If it is close to unit leverage, its own bank may be conditioned away except for the singleton hub while preserving a uniformly nonsingular exact-rank-three block on `hub + two independent banks`.

Thus the r20 survivor `QFORM-TRIPARTITE-HEAVY-INTERNAL-TRANSVERSE-v1` reduces to two strictly sharper shapes, both at fixed spectral condition number scale. The diffuse child of either shape is now paid by `768`.

## 5. Source-valid construction refuting a single-local-certificate upgrade

The near-unit Alternative B does NOT imply one uniformly large physical scalar pivot, pair determinant, or principal triple determinant.

Fix `0<epsilon<1/512` and integer `m>=2`. In the normalized spectral basis `e1,e2,e3`, take the following disjoint original-coordinate rows:

- bank `B1`: one hub `h=sqrt(1-epsilon)e1`;
- bank `B2`: `m` rows `sqrt(epsilon/m)e1` and `m` rows `m^{-1/2}e2`;
- bank `B3`: `m` rows `m^{-1/2}e3`.

Their Gram is exactly `I_3`. Bank `B2` has genuine internal transverse rank two. Take

`M = [[0,1,0],[1,0,0],[0,0,1]]`,

whose eigenvalues are `{1,-1,1}`. Hence the resulting physical symmetric matrix is an exact target matrix with three nonzero eigenvalues of modulus one.

The hub leverage is `L=1-epsilon>511/512`, and

`T_h = 1-epsilon`.

Indeed the only nonzero fixed-hub tripartite minors use one `e2` row from `B2` and one `e3` row from `B3`; each has squared determinant `(1-epsilon)/m^2`, and there are `m^2` of them.

Nevertheless every local certificate vanishes with `m`:

- every scalar pivot on the `e1` and `e2` rows is zero, while each `e3` scalar pivot has magnitude `1/m`, so `max_i |A_ii|=1/m`;
- the largest absolute determinant of a physical pair involving the hub is `(1-epsilon)/m`;
- the largest absolute determinant of a physical principal triple is `(1-epsilon)/m^2`.

Thus a constant fixed-hub exterior packet cannot be converted by pigeonhole into one constant scalar pivot, pair determinant, or principal triple determinant. The correct next payment must remain aggregate at bank level. This is a counterexample only to that local-selection mechanism, NOT to QFORM.

The construction is deliberately within the target and preserves original-coordinate product provenance. Algebraically its three spectral-axis aggregates arise from disjoint original-coordinate subgroups, showing why aggregate smoothing can survive while every individual local determinant tends to zero.

## 6. First unpaid implication

The remaining sharp obstruction is

`QFORM-SINGLETON-HUB-TWOBANK-AGGREGATE-PAYMENT-v1`:

> In an exact-rank-three active block with `|det N|, sigma_min(N)>=2^{-18}`, one original coordinate is a singleton hub and the other active coordinates are partitioned into two disjoint original-coordinate banks with fixed-hub exterior packet at least `1/512`. Prove a universal density bound without selecting a single edge/triple and without taking a conditional-profile supremum; or give a genuine target counterexample.

The complementary deletable-hub child is the same uniformly conditioned rank-three problem on one fewer active physical coordinate. Repeated deletion alone is not accepted as closure because earlier B10 constructions show that heavy-row peeling may continue for arbitrarily many stages. Therefore the next mechanism must aggregate the two-bank cross energy/exterior mass before reciprocal inversion.

A promising concrete interface is to combine the fixed-hub packet with a whole-bank bilinear/Fresnel estimate: condition only on coordinates outside `hub+B2+B3`, keep all same-bank quadratic curvature inside the oscillatory integral, and pay a determinant/mixed-discriminant norm of the two banks rather than `max_j |A_hj|` or one principal minor.

## 7. Status and provenance

`ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_LEMMA / LOCAL_CANDIDATE_REFUTED`.

Full exact-rank-three closure is not claimed. The full arbitrary-matrix QFORM conjecture remains OPEN. No projected-coordinate independence, hidden moment/support bound, numerical census, or perturbative deletion of dense self-couplings is used.
