SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B10, 2026-09-22T23:46:58.333783Z.
attacking: the near-null heavy physical direction on the two-sheet side; isolate a uniformly curved spectral screen and identify the aggregate packet that remains after local-minor atomization.

# fleet02/B10 — near-null screen curvature and null-hub packet invariants

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Rank-three coupled case  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_LEMMAS / LOCAL_MECHANISM_REFUTED / FULL_TARGET_OPEN`.

The full conjecture remains OPEN. Throughout this report `A=RMR^T`, `R^TR=I_3`, `M` is real symmetric indefinite, and every eigenvalue of `M` has modulus at least `s>0`. The physical coordinates are the original independent cap-one inputs. No statement below treats the projected spectral coordinates as independent.

## 1. Completed sources actually consumed

The newest source package `e5f71d79eff325201dd0274053d20268ce65b837` supplies two facts used here. First, the rough ruled one-sheet theorem bounds the one-sheet side of an exact rank-three indefinite form by `pi sqrt(2)/s`; hence only the two-sheet side remains in the present near-null analysis. Second, the newer Fourier report raises the volume-sampling row-marginal threshold for Theorem D to every `h<3/4`, but does not prove the hybrid heavy-row chamber.

The designated partner `fleet03/B10`, run `20260922T231827Z-fleet03-B10-QFORM-r21`, canonical bundle `3136d1f31dd7e723ddef05d06edce6fe769dc384`, proves the exact null-ray/rank-two-bank packet theorem

`||p_Q||_infinity <= 12 P^(-1/3)`,

where `P` is the structured total physical principal-triple determinant packet of a rank-two bank against a disjoint exact null ray. The theorem preserves the original-coordinate product provenance and allows arbitrary outside affine terms. It is applied quantitatively to the cascade family in Section 4.

## 2. Near-null screen curvature cannot degenerate

Let `u` be any unit vector with

`q := u^T M u`, `|q|<s`.

Put

`gvec := P_(u^perp) M u = M u-q u`, `g:=||gvec||`.

Since `||Mu||>=s`,

`g^2=||Mu||^2-q^2 >= s^2-q^2>0`.

Let `w=gvec/g`, and let `v` be either unit vector orthogonal to both `u` and `w`. Then

`u^T M v=(Mu) dot v=0`.

### Theorem 2.1 — `QFORM-NEARNULL-SCREEN-CURVATURE-v1`

With `lambda:=v^T M v`, one has

`|lambda|>=s`.

Moreover `lambda` has the majority sign of the inertia of `M`. In the orthonormal basis `(u,w,v)`,

`M = [[q,g,0],[g,b,c],[0,c,lambda]]`.

After the determinant-one shear `V -> V+(c/lambda)T`, the associated quadratic polynomial in the three spectral projection coordinates `(S,T,V)` is

`q S^2 + 2g S T + beta T^2 + lambda V^2`,

where `beta=b-c^2/lambda`, and

`|q beta-g^2| = |det M|/|lambda| >= s^2`.

#### Proof

The compression of `M` to the two-plane `span(u,v)` is diagonal with eigenvalues `q` and `lambda`. If `M` has inertia `(2,1)`, Cauchy interlacing for a two-dimensional compression says its larger compression eigenvalue is at least the second full eigenvalue, which is at least `s`. Since `q<s`, the larger compression eigenvalue must be `lambda`; hence `lambda>=s`. For inertia `(1,2)`, apply the same argument to `-M` to get `lambda<=-s`.

The displayed matrix form follows from the definitions of `w,v`. Completing the `v` square gives `beta=b-c^2/lambda`, and expanding the determinant gives

`det M = lambda(q beta-g^2)`.

Finally, if the three absolute eigenvalues of `M` are `d_1,d_2,d_3>=s` and `D=max d_i=||M||`, then `|det M|>=s^2 D`, while `|lambda|<=D`. Therefore `|det M|/|lambda|>=s^2`. QED.

This is a spectral statement only. The three random projections `(S,T,V)` are generally dependent. Its use is to show that a near-null heavy physical direction does not lose the third curvature: the screen square remains at scale at least `s`, and the complementary hyperbolic Schur determinant remains at scale at least `s^2`. Thus the surviving obstruction is source overlap, not spectral degeneration.

For the owner normalization `s=1`, the newest ruled theorem pays the one-sheet side by

`p_Q(t) <= pi sqrt(2)`

on that side. Hence the first unpaid geometry after Theorem 2.1 is the two-sheet side with a product-overlapping near-null hub, despite `g>=sqrt(1-q^2)`, `|lambda|>=1`, and `|q beta-g^2|>=1`.

## 3. Aggregate packet invariants at a physical hub

Fix a physical row

`r_0=sqrt(h) u`, `0<h<=1`.

For every other row write

`r_j=alpha_j u+v_j`, `v_j in u^perp`.

Parseval gives the exact identities

`sum_(j!=0) alpha_j^2=1-h`,
`sum_(j!=0) alpha_j v_j=0`,
`sum_(j!=0) v_j v_j^T=I_(u^perp)`.

### Theorem 3.1 — `QFORM-FIXED-HUB-TRIPLE-PACKET-IDENTITY-v1`

For every such physical row, without a null assumption,

`sum_(j<k; j,k!=0) |det A[{0,j,k},{0,j,k}]| = h |det M|`.

#### Proof

For a physical triple `T={0,j,k}`,

`det A[T,T]=det(M) det(R_T)^2`.

Because longitudinal components along `u` disappear from the three-row determinant,

`det(R_T)^2=h det_(u^perp)(v_j,v_k)^2`.

Cauchy-Binet in the two-dimensional transverse frame gives

`sum_(j<k) det(v_j,v_k)^2 = det(sum_j v_jv_j^T)=1`.

Summation proves the identity. QED.

At exact nullity `q=u^TMu=0`, write `gvec=Mu` (which lies in `u^perp`). Then additionally

`A_00=0`,
`A_0j=sqrt(h) gvec dot v_j`.

### Theorem 3.2 — `QFORM-NULL-HUB-PAIR-PACKET-IDENTITY-v1`

At exact nullity,

`sum_(j!=0) |det A[{0,j},{0,j}]|
 = sum_(j!=0) A_0j^2
 = h ||Mu||^2
 >= h s^2`.

Thus an exact null heavy physical row always carries a dimension-free amount of aggregate indefinite pair mass and aggregate principal-triple determinant mass. What can fail is only localization of that mass into one usable atom.

## 4. Arbitrarily deep high-leverage null cascades atomize every local certificate

Fix any `theta in (0,1)`, any integer `K>=2`, and any integer `N>=1`. Let

`M_0=[[0,1,0],[1,0,0],[0,0,1]]`.

Take `K` physical rows on the null ray `e_1` with squared weights

`w_k=theta(1-theta)^(k-1)` for `k<K`,
`w_K=(1-theta)^(K-1)`.

Take `N` rows `e_2/sqrt(N)` and `N` rows `e_3/sqrt(N)`. The rows form a Parseval frame, so `A=R M_0 R^T` has exact nonzero spectrum `{-1,1,1}`.

### Theorem 4.1 — `QFORM-ARBITRARY-THRESHOLD-NULL-CASCADE-v1`

After deleting the first `k-1` null-ray rows and renormalizing the surviving frame, the leverage of the next ray row is exactly `theta` for every `k<K`; the last one has leverage one. Therefore for every proposed fixed diffuse threshold `theta_0<1` and every proposed bounded peeling depth, choosing `theta>theta_0` and then `K` larger than that depth defeats any proof strategy that only repeats `delete a leverage-heavy zero-pivot row until the normalized residual frame is diffuse`.

At the same time, as `N` tends to infinity,

- the largest scalar physical pivot is `1/N`;
- the largest physical principal-pair determinant involving a ray row is at most `theta/N`;
- the largest nonzero physical principal-triple determinant is at most `theta/N^2`;

while for the first ray row the aggregate pair packet is exactly `theta` and the aggregate triple packet is exactly `theta`.

#### Proof

The ray weights sum to one. If `R_k=sum_(j>=k)w_j`, then `R_k=(1-theta)^(k-1)` and `w_k/R_k=theta` for `k<K`, while `w_K/R_K=1`. The pivot and determinant claims follow by direct evaluation with `M_0`: only the `e_3` rows have nonzero scalar pivot; a ray/e2 pair has determinant magnitude `w_k/N`; and a ray/e2/e3 triple has determinant magnitude `w_k/N^2`.

This family does not challenge QFORM. Group all ray coordinates into one rank-one null bank `C` (total mass `m=1`) and all `e_2,e_3` coordinates into the transverse rank-two bank `B` (Gram determinant `h_B=1`, transversality `delta=1`, `|det M_0|=1`). The designated partner fleet03/B10 theorem gives the actual uniform inequality

`||p_Q||_infinity <= 12 [1*1*1*1]^(-1/3)=12`

for every `K,N` and every admissible product law. This is an equation-level use of the completed partner theorem. In particular, taking `theta=7/8` shows that merely replacing a `1/2` local diffuse threshold by a threshold below `3/4`, as in the newest D' volume theorem, cannot by itself make sequential heavy-row deletion terminate; the useful mechanism is whole-bank aggregation, not a better fixed local threshold.

## 5. What remains

The newest ruled theorem has already removed the one-sheet side. Theorem 2.1 removes spectral degeneration from the near-null two-sheet side: there is always a screen direction with curvature at least `s` and a complementary hyperbolic determinant at least `s^2`. Theorems 3.1-3.2 show that at a null hub the physical pair/triple certificates are also present in aggregate at constant scale. Theorem 4.1 shows why one cannot pay them by one local pivot/minor or by bounded-depth leverage peeling.

The first unpaid implication is therefore:

`QFORM-NEARNULL-TWOSHEET-UNSTRUCTURED-PACKET-COMPILER-v1`.

Starting from an indefinite exact-rank-three product projection with a leverage-heavy physical row satisfying `|u^TMu|<1`, use the canonical screen direction and the fixed-hub aggregate packet to obtain a product-preserving whole-bank density estimate on the two-sheet side. At exact nullity the compiler must reduce to the partner rank-two-bank/null-ray theorem when the packet is planar, but it must also handle arbitrary longitudinal overlap. It may not take a conditional-height supremum, declare spectral projections independent, perturb away small coefficients using moments/support, select one reciprocal minor, or rely on any fixed leverage threshold below one.

Continuity is not claimed for this new structural reduction. The full exact-rank-three theorem and full QFORM conjecture remain open.
