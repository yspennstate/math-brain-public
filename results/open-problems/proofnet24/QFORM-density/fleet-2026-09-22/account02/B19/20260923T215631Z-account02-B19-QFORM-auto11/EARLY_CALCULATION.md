SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B19, 2026-09-23T21:56:31Z.
attacking: the account03/B19 r42 pairwise-weak finite-core residue — determine what `sigma_min(A[{i,j},{i,j}])<1/64` for every physical pair actually forces, and spend any frustrated three-coordinate sign pattern at a real density inequality.

# Early calculation: pairwise-weak sign geometry

Sources pinned for this calculation:

- owner brain control resolved fresh before the write: `yspennstate/math-research-brain@c851e69b20fca80e1704fc6f8ad21560fd33047d`, OWNER CONTROL revision `2026-09-22.15`;
- designated partner: `yspennstate/math-open-problems@9862459c9cc8e534a8a49c7d20959de7cb1ad992`, `account03/B19/20260923T210457Z-account03-B19-QFORM-r42/REPORT.md`;
- required compatible completed source: `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `COUNTEREXAMPLE_SEARCH.md` Theorem A and `RESULTS.md` Theorem F.

Let `B=A[H,H]` be the physical finite-core self block in the r42 branch and suppose

` sigma_min(B[{i,j},{i,j}]) < kappa `

for every distinct physical `i,j in H`. Fix `d>2 kappa` and let

` S={i in H: |B_ii|>=d}. `

If two indices in `S` have opposite diagonal signs, Rayleigh interlacing on their literal physical 2-by-2 principal block gives one eigenvalue at least `d` and one at most `-d`, hence its smallest singular value is at least `d>kappa`, contradiction. Therefore all diagonals on `S` have a common sign `s`.

Write `u_i=sqrt(|B_ii|)` and

` r_ij = s B_ij/(u_i u_j). `

For a pair `i,j in S`, the symmetric matrix `s B[{i,j},{i,j}]` has positive diagonal entries `a,c>=d` and an eigenvalue `mu` with `|mu|<kappa`. Its characteristic equation gives

` B_ij^2=(a-mu)(c-mu). `

Consequently

` 1-kappa/d <= |r_ij| <= 1+kappa/d. `

Thus the high-diagonal subcore is an almost-complete signed rank-one matrix, except possibly for sign frustration around triangles.

For a triangle `T={i,j,k}` with negative edge-sign product, let `C` be the normalized 3-by-3 matrix with diagonal one and off-diagonal entries `r_ij,r_jk,r_ki`. Let `C0` keep only their signs. Any frustrated sign triangle is diagonal-sign conjugate to

`[[1,1,1],[1,1,-1],[1,-1,1]]`,

whose eigenvalues are `{-1,2,2}`. Since every off-diagonal magnitude differs from one by at most `kappa/d`,

` ||C-C0||_op <= 2 kappa/d, `

so

` sigma_min(C) >= 1-2 kappa/d. `

Writing `B[T,T]=s D C D`, `D=diag(u_i,u_j,u_k)`, yields

` sigma_min(B[T,T]) >= d-2 kappa. `

This is already a literal physical 3-by-3 density receiver. The completed localized Theorem A in the required pinned source gives, after conditioning every other original coordinate,

` ||p_Q||_infinity <= 6 sqrt(pi)/(d-2 kappa). `

At the live partner value `kappa=1/64`, choosing `d=1/16` gives

` sigma_min(B[T,T])>=1/32, `

hence

` ||p_Q||_infinity <= 192 sqrt(pi) = 340.311139373859... . `

If no triangle is frustrated, complete-graph sign consistency gives vertex signs `eps_i` with `sign(r_ij)=eps_i eps_j`. Then

` B[S,S]=s D(eps eps^T+E)D,  E_ii=0, |E_ij|<=kappa/d. `

Therefore, with the rank-one matrix `L=s(D eps)(D eps)^T`,

` ||B[S,S]-L||_op <= (kappa/d) sum_{i in S}|B_ii|. `

So the pairwise-weak branch does not force small self-curvature; it forces a dichotomy between a paid frustrated physical triangle and a coherent signed rank-one high-diagonal packet.

A sharp warning model is the 3-by-3 matrix

`[[1,1,1],[1,1,-1],[1,-1,1]]`.

Every physical 2-by-2 principal block is singular, while its eigenvalues are `{-1,2,2}`. Thus the naive implication “all physical 2-by-2 pairs weak implies the whole block is near rank one” is false; the missing invariant is triangle sign frustration. This model is not a QFORM counterexample because the localized Theorem A pays it directly.
