# Early substantive calculation — RV r=1 spectral tail plus one private square

Let `Y` be an ORIGINAL-coordinate product bank with one-dimensional density caps at most one, let `M` be a finite real matrix, and put

`S_r(M)^2 = sum_{j>r} s_j(M)^2`.

Rudelson--Vershynin, arXiv:1402.4492v2, proof of Theorem 8.1, equation (8.4), applies for every integer `r>=0`. Since a cap-one scalar law has concentration function `L(Y_i,t)<=2t`, there is one absolute published-source constant `C_*` (twice their absolute `C`, if their radius convention is used literally) such that, for every deterministic shift `alpha`,

`P{||MY+alpha||<=u} <= min(1,(C_* u/S_r(M))^r)`.

Hence for every `0<q<r`, layer cake gives

`E ||MY+alpha||^{-q} <= [r/(r-q)] (C_*/S_r(M))^q`.                 (E1)

In particular the previously used partner case is `(r,q)=(2,1)`, while the new endpoint is

`E ||MY+alpha||^{-1/2} <= 2 sqrt(C_*/S_1(M))`.                    (E2)

Now let `X,Y,W` be disjoint ORIGINAL source banks, with `W` scalar, and consider

`T=X^T M Y+alpha^T X+G(Y)+aW^2+h(Y)W+c`, `a!=0`.

For fixed `Y=y`, Rudelson--Vershynin Theorem 1.2 gives the linear form `L_y=(My+alpha)^T X` density cap

`K_y <= sqrt(2)/||My+alpha||`.

Completing the square in `W` does not improve the square singularity (consistent with the live affine-slope correction): the translated-square density has rearrangement at most `|a|^{-1/2}t^{-1/2}`. Hardy--Littlewood plus the bathtub extremizer for a probability density capped by `K_y` gives

`||p_(T|Y=y)||_infty <= 2 |a|^{-1/2} sqrt(K_y)
 <= 2^(5/4)|a|^{-1/2} ||My+alpha||^{-1/2}`.

Averaging and using (E2) yields the candidate theorem

`||p_T||_infty <= 2^(9/4) sqrt(C_*) / sqrt(|a| S_1(M))`.           (E3)

For a physical quadratic cross term `2X^T B Y`, `M=2B`, so

`||p_T||_infty <= 2^(7/4) sqrt(C_*) / sqrt(|a| S_1(B))`.           (E4)

Stress family: for `N>=5`, `delta=(N-1)^(-1/2)`,

`Q_N=2 delta sum_{j=1}^N X_jY_j + 2UV + W^2`.

Its physical spectrum is `{-1,+1,+1}` together with `N` copies each of `+/-delta`; hence it is literally in the owner target and `S_1(delta I_N)=1`. Thus (E4) is dimension-free although the top cross singular value tends to zero. The pinned e5f D5 theorem also applies to the same cross cut: `Z_5=binom(N,5)/(N-1)^5 >=1/1280`, so it gives the explicit real inequality

`||p_QN||_infty <= 5 sqrt(2e) 1280^(1/10) < 23.843`.

This is not a full-QFORM proof; the structural debt is to extract such an exact source-separated square/cross packet, or route its failure elsewhere, without deleting nonzero residual couplings.
