# fleet02/B09 early substantive checkpoint — small mixed-hub disjointness is not forced by N3

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T044544Z-fleet02-B09-QFORM-auto11`  
Status: substantive checkpoint; full target OPEN.

## First unpaid implication attacked

`QFORM-HUB-PLUCKER-SMALLRHO-OR-DEGENERATE-G-ROUTING-v1` from the immediately preceding B09 run. The question tested here is whether the strict no-pivot target chamber can itself force a universal positive lower bound on the mixed-hub determinant-weighted disjoint-basis mass `rho` once `det G` and the Fresnel coefficient are nondegenerate.

It cannot.

## Exact strict-N3 family

Fix any `tau in (0,1]` and any `eta>0`. Choose integers `M,N` and `epsilon in (0,1/2)` so that

- `1/M<tau`,
- `(1-epsilon)epsilon/N<tau`,
- `2 epsilon<eta`.

Use five pairwise disjoint original-coordinate groups: physical hubs `j,h`, an `M`-coordinate bank `U`, an `M`-coordinate bank `C`, and an `(N+1)`-coordinate bank `V`.

Let

`u=M^(-1/2)(1,...,1)` on `U`,
`c=M^(-1/2)(1,...,1)` on `C`,

and let `v` on `V` have squared coordinates

`p_0=1-epsilon`, `p_1=...=p_N=epsilon/N`.

Define the symmetric matrix by the only nonzero blocks

`A[j,U]=u^T`, `A[h,C]=c^T`,
`A[V,V]=v v^T-diag(v_i^2)`.

Thus

`Q=2 X_j <u,X_U> + 2 X_h <c,X_C>
   + <v,X_V>^2 - sum_i v_i^2 X_i^2`.                         (1)

All physical diagonals vanish. Hence every physical `2 x 2` principal determinant is `-A_ab^2`. The star-edge squares are `1/M<tau`; in the dense same-side `V` block the largest edge square is `(1-epsilon)epsilon/N<tau`. Therefore this is literally in strict N3(tau).

The two disjoint star blocks have spectra `{+1,-1}` and `{+1,-1}`. Hence the full matrix has at least four eigenvalues of modulus one, independently of the `V` block. In particular `s_3(A)=1`.

## Mixed-hub packet and exact disjointness

Take `h` as the source-coordinate hub, `I=C union V` as its leaf bank, and put the entire `(j,U)` star in the arbitrary outside bank allowed by newest-Claude Theorem H. On `I`,

`A_II = v v^T + D`, `D=-diag(v_i^2)`,

and the hub-star vector is `c`. Since `v` and `c` have disjoint supports and unit norm,

`G=[v,c]^T[v,c]=I_2`, `det G=1`, `lambda=1`.

The natural mixed leverage of the heavy `V` coordinate is `1-epsilon>1/2`, so the raw leverage gate in Theorem H fails whenever `epsilon<1/2`.

For the whitened frame `[v,c]`, every Pluecker basis consists of one `V` coordinate and one `C` coordinate. Its determinant weight is `p_a/M`. Two independent bases are disjoint iff both choices differ. Therefore the exact disjoint-basis mass is

`rho_epsilon
 = [1-((1-epsilon)^2+epsilon^2/N)] (1-1/M)
 = [2epsilon-epsilon^2(1+1/N)](1-1/M)
 <= 2 epsilon < eta`.                                             (2)

Thus no universal lower bound on `rho` follows from the full target spectral condition plus strict N3, even with `det G=1` and `|lambda|=1`. The mixed-hub Pluecker bound from the preceding run necessarily degrades like `rho^(-1/3)` on this family; that degradation is structural, not a bad constant.

This also disproves the stronger hoped-for implication `small rho => a uniformly good physical pair`: all physical pair determinants are already `<tau` and `tau` is arbitrary.

## The required newest-Claude result applied to a real member

At the endpoint `epsilon=1/2`, every row leverage of `[v,c]` is at most `1/2`. Applying Theorem H from

`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`,

with one physical hub and one Fresnel leaf direction gives

`|phi_Q(t)| <= 4 pi^(3/2) |t|^(-3/2)`.

Integrating `min(1,4 pi^(3/2)|t|^(-3/2))` and dividing by `2pi` yields the actual target-valid inequality

`||p_Q||_infinity <= 3*2^(4/3) < 7.560`.                           (3)

The arbitrary outside `(j,U)` star and all its couplings are within Theorem H's stated outside-block scope.

## Source-valid escape when rho is tiny

The small-rho family is not a counterexample to QFORM. The first two terms in (1) are two genuinely independent hyperbolic packets on four disjoint source banks. Fleet03/B09's completed `QFORM-FOUR-BANK-HYPERBOLIC-CONVOLUTION-v1` gives, using cap one for the two physical hubs and cap `sqrt(2)` for each unit bank projection,

`||p_{2 X_j<u,X_U> + 2 X_h<c,X_C>}||_infinity <= 8 sqrt(2)`.      (4)

The final dense same-side `V`-curvature term is independent of those four banks, so convolution cannot increase the supremum. Hence for every `epsilon`, `M`, `N` above and every admissible product law,

`||p_Q||_infinity <= 8 sqrt(2) < 11.314`,                          (5)

with the corresponding direct `O(|L|)` interval bound. No probability squaring or square-root small-ball conversion occurs.

So the correct small-`rho` proof-map obligation is not to force `rho` back up or force a local minor. It must inspect the outside target directions and route a near-coloop mixed frame to an external hyperbolic/ridge/finite-core smoother when one exists.

Candidate correction id for the final report:
`QFORM-N3-MIXED-HUB-RHO-LOWER-BOUND-FALSE-v1`.
