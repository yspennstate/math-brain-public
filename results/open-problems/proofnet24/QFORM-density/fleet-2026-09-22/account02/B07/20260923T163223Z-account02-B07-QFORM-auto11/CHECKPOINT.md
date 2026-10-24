SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B07, 2026-09-23T16:32:23Z.
attacking: the partner r33 aggregate cross-rectangle E2 branch — prove a bounded-support physical spectral-core receiver, then stress it with an exact diffuse rank-two target family rather than selecting one minor.

# Substantive checkpoint

Current partner: account03/B07 r33, canonical math `yspennstate/math-open-problems@316522c99a92f168d0e0dcfe3be3aa032bdf53f9`.

Its aggregate branch supplies, at the current strict-N3 scale

`h=(2sqrt(2)-1)/1572864`,

`|A_uv|<=h/8` for physical off-diagonal entries, `|A_uu|<h^2/128`, and a four-bank cross-rectangle determinant packet

`Omega=sum (A_ij D_kl-B_il C_kj)^2`

with

`sqrt(Omega)>462.4798790835328 h^2`.

New calculation: normalize these squared physical 2x2 determinants. If row and column physical supports `R0,C0`, each of cardinality at most `m`, have total inclusion-marginal tail `delta_R+delta_C<=1/2`, then at least half the determinant mass lies on pairs entirely inside `R0 x C0`. Hence for `K0=A[R0,C0]`,

`E2(K0)>=Omega/2`.

If `p=|R0|,q=|C0|,r=min(p,q)`, then

`E2(K0)<=binom(r,2)||K0||op^2 s2(K0)^2`

and the physical coefficient cap gives `||K0||op<=sqrt(pq)h/8`. Therefore, for `p,q<=m`,

`s2(K0) > [8*462.4798790835328/sqrt(2)]/[m sqrt(binom(m,2))] * h`.

Let `H=R0 union C0`. Split its symmetric physical principal block as the pure bipartite block

`O=[[0,K0],[K0^T,0]]`

plus the two same-side principal blocks. The latter have operator norm at most

`mu_m=(m-1)h/8+h^2/128`.

Since `s4(O)=s2(K0)`, Weyl's singular-value inequality gives

`s4(A[H,H]) >= s2(K0)-mu_m`.

For every `m<=31` this is positive; the worst case is `m=31`, where

`s4(A[H,H]) > 0.163629064895129 h`.

Thus this determinant-weighted bounded-support branch contains four actual eigenvalues of modulus at least that fixed scale. Conditioning only outside `H` and applying the completed finite-dimensional projected-gradient theorem gives a universal full-form density bound. No determinant is individually selected or inverted.

The intended regression family for the complementary support-diffuse branch is the pure bipartite matrix with cross block

`K_N=diag(J_N/N,J_N/N)`.

Then `s(K_N)=(1,1)`, the symmetric completion has spectrum `{1,1,-1,-1}`, the four-bank packet has `Omega=1`, every nonzero contributing determinant is exactly `N^-2`, every packet inclusion marginal is `1/N`, and every fixed-cardinality physical principal core has operator norm `O(1/N)`. For `N` large it also satisfies the strict partner coefficient cap. This is not a QFORM counterexample: the required pinned e5 Fresnel-Brascamp-Lieb theorem applies to its exact rank-four, leverage-`1/N` range and gives `||p_Q||inf<=8`.

First unpaid implication after this checkpoint: the partner r33 aggregate-E2 branch can now survive only with determinant-weight support genuinely spread beyond every 31-by-31 physical support; the global rank-one-tube sibling remains a separate low-tail/hub obligation.
