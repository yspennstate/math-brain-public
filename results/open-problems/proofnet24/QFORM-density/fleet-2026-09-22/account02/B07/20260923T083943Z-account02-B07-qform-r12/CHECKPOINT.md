SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B07, 2026-09-23T08:39:43Z.
attacking: latest account03/B07 r28 four-hub failure branch — pay every bounded-support incident Schur packet by an actual finite physical spectral core, and stress the residual with a target-valid diffuse C21 construction.

# Early substantive checkpoint

Programme `QFORM-DENSITY-3EIG-20260922`; full conjecture remains OPEN. Current control revision is `2026-09-22.15`. Execution remains `WITHOUT_VERIFIED_BRAIN`.

## First unpaid implication

`QFORM-R28-SCHUR-SUPPORT-DIFFUSE-RECEIVER-v1`: in the partner r28 cross-disjointness-failure branch, the residual `N` has a fixed two-row/two-column E2 compound hub, while the incident anchored Schur packet has mass `J=a^2 E2(S)>xi^2 F^6/36`. Prove that every bounded-support part of that Schur packet is an actual bounded physical spectral core, so only a quantitatively support-diffuse incident packet survives. Do not select a reciprocal local minor.

## New exact core calculation

For `B0=[[a,r^T],[c,N]]`, `a!=0`, set `S=N-cr^T/a` and normalize the squared `2x2` minors of `S` to a law `nu_S`. Let `alpha_i,beta_j` be its row/column inclusion marginals and set

`R_*={i:alpha_i>1/2}`, `C_*={j:beta_j>1/2}`.

Because each sampled residual set has size two, `|R_*|,|C_*|<=3`. Put

`delta_R=sum_(i notin R_*) alpha_i`, `delta_C=sum_(j notin C_*) beta_j`.

If `delta_R+delta_C<=1/2`, then the union bound under `nu_S` gives

`E2(S[R_*,C_*]) >= E2(S)/2`.

Every such Schur minor is a literal physical anchored minor:

`det B0[{x} union R,{y} union T] = a det S[R,T]`.

Hence the physical cross block

`M=B0[{x} union R_*,{y} union C_*]`

has at most four rows and four columns and satisfies

`E3(M)>=J/2`.

In the live no-pivot class `N3(tau)`, every cross entry obeys `|A_uv|^2<tau+tau^2`, so `||M||op^2<=16(tau+tau^2)`. Since `rank M<=4`,

`E3(M)<=4 ||M||op^4 s3(M)^2`,

and therefore

`s3(M)>=sqrt(J)/(32 sqrt(2)(tau+tau^2))`.

The symmetric principal block on the at-most-eight original coordinates containing this cross block has third singular value at least `s3(M)`. The completed finite-dimensional spectral receiver (`math-open-problems@472b70d...`, Corollary 4.1) therefore yields

`||p_Q||infinity <=256 sqrt(6 pi)(tau+tau^2) J^(-1/2)`.

Using partner r28's `J>xi^2 F^6/36`,

`boxed: ||p_Q||infinity <1536 sqrt(6 pi)(tau+tau^2)/(xi F^3).`

At `tau=1/128`, `xi=1/16`, the coefficient is `<840.102 F^(-3)`.

If instead `delta_R+delta_C>1/2`, let `Y` be the number (0 through 4) of residual row/column indices outside the two heavy supports. Then `EY>1/2`, hence `P(Y>=1)>1/8`. Thus more than `J/8>xi^2 F^6/288` of the actual anchored third-minor mass touches a residual coordinate whose original `nu_S` marginal is at most `1/2`. This is the genuine support-diffuse survivor.

## Source-valid obstruction to strengthening this into unconditional bounded-core extraction

Fix `0<eps^2<tau` and, for large `m`, form a `3 x (1+3m)` cross block `C_m` on disjoint column groups `{v0},G1,G2,G3` by

- row 1: coefficient `eps` at `v0` and `sqrt((1-eps^2)/m)` on `G1`;
- row 2: coefficient `1/sqrt(m)` on `G2`;
- row 3: coefficient `1/sqrt(m)` on `G3`.

Then `C_m C_m^T=I_3`, so `A_m=[[0,C_m],[C_m^T,0]]` has nonzero spectrum `{1,1,1,-1,-1,-1}` and satisfies `N3(tau)` for large `m`. Take fixed row hub pair `H={1,2}` and fixed column pair `L={v0,w}` with `w in G3`. The exact `(2,1)` four-hub E2 class has mass

`sum_(|T cap L|=1) det C_m[H,T]^2 = eps^2`,

independent of `m`. Nevertheless, for every fixed physical core size `M`, the third largest absolute eigenvalue of every principal core of size at most `M` is at most `sqrt(M/m)`, hence tends to zero. Therefore constant four-hub C21 mass does NOT force a bounded physical spectral core.

This is not a QFORM counterexample. It is paid by the required e5 hub theorem: take physical hubs `{1,2}` and all right-bank coordinates as the leaf bank. Their coupling Gram is exactly `I_2`, all leaf curvature is diagonal zero, and the largest leaf leverage is `max(eps^2,(1-eps^2)/m,1/m)<=1/2`. The e5 Theorem H gives

`|phi_Q(t)|<=4 pi^2 |t|^-2`, hence `boxed: ||p_Q||infinity<=4`.

The final report will splice this with the full source-pinned partner r28 four-hub statement and preserve only the genuinely diffuse arbitrary-curvature remainder.