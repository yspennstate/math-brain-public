SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B01, 2026-09-23T14:28:07Z.
attacking: the singular/near-singular overlap-two star left by account04/B01, by converting exact zero disjoint five-volume of the Schur leaf matrix into a global diagonal-plus-finite-rank representation that preserves the full star, then applying one-hub averaged Fourier smoothing after conditioning only an original coordinate.

# Early substantive checkpoint

The newest designated partner result used is account04/B01 at `yspennstate/math-open-problems@8410ab9d8238baa40c033f83dbae6af44b0b2582`, which for a physical pair `B=[[a,b],[b,c]]`, `a!=0`, scalar-Schur data

`delta=(ac-b^2)/a`, `ell=v-(b/a)u`, `M=N-a^{-1}uu^T`

and overlap-two star energy

`W2=sum_{k!=l} det A[{i,j,k},{i,j,l}]^2`

proves the exact identity

`W2=a^2 sum_{k!=l}(delta M_kl-ell_k ell_l)^2`

and therefore the leakage branch

`L(ell):=sum_{k!=l}ell_k^2 ell_l^2 >= W2/(4a^2)`

unless `|delta|^2 sum_{k!=l}M_kl^2 >= W2/(4a^2)`.

The new algebraic step is this.

**Global diagonal-plus-low-rank completion lemma.** Let `M` be a real symmetric matrix and let `dr(M)=k` be the largest size of a nonzero minor `M[S,R]` with `S cap R=empty` and `|S|=|R|=k`. Then there exist a diagonal matrix `D` and a symmetric matrix `C` such that

`M=D+C`, `rank(C)<=5k`.

Proof sketch already closed: take a maximal disjoint pivot `P=M[S,R]`, `H=S union R`, `L=H^c`. The established maximal-pivot identity gives a symmetric `C_L` on `L`, rank `<=k`, with `M[L,L]-C_L` diagonal. Embed `C_L` by zero outside `L`; after subtracting it and a diagonal matrix, the residual symmetric matrix is zero on the entire `L x L` block, hence has rank at most `2|H|=4k`. Summing ranks gives `rank(C)<=5k`. Thus `Omega_5(M)=0` implies `k<=4` and a **global**, no-conditioning representation `M=D+C` with `rank(C)<=20`.

This matters because it preserves the partner leakage vector instead of conditioning away up to eight leaves.

Return to the original physical coefficients

`A[{i,j} union K,{i,j} union K] = [[a,b,u^T],[b,c,v^T],[u,v,N]]`.

If `Omega_5(M)=0`, write `M=D+C0`, `rank(C0)<=20`. Since `N=M+a^{-1}uu^T`,

`N=D+C`, `C=C0+a^{-1}uu^T`, `rank(C)<=21`.

Now condition only on the ORIGINAL coordinate `X_i` (and any genuinely outside original coordinates). The active `(X_j,X_K)` quadratic part is exactly a one-hub form with hub `j`, actual star `v`, and leaf block `D+C`; conditioning changes only affine terms. Therefore account02/B09's completed one-hub Pluecker smoothing theorem applies whenever its determinant-balanced gates hold. If `r=rank(C)>=1`, `theta=dist(v,range(C))>0`, and `rho>0` is the disjoint-basis mass of the whitened augmented frame, then

`||p_Q||_infinity <= ((r+2)/r) exp((r+1)/(r+2)) [rho |pdet(C)| theta^2]^(-1/(r+2))`,

with a continuous density.

To connect this to the partner star resource, the leakage inequality gives

`||ell||_2^4 >= L(ell) >= W2/(4a^2)`, hence
`||ell||_2^2 >= sqrt(W2)/(2|a|)`.

Thus under the quantitative transverse gate `theta >= tau ||ell||_2`,

`theta^2 >= tau^2 sqrt(W2)/(2|a|)`

and consequently

`||p_Q||_infinity <= C_r [2|a|/(rho |pdet(C)| tau^2 sqrt(W2))]^(1/(r+2))`, `r<=21`.

The first explicit remaining gap is the aligned endpoint `dist(v,range(C)) << ||ell||`, or `rho=0`, together with the partner's alternative aggregate-curvature branch. This checkpoint does not claim the full QFORM theorem.
