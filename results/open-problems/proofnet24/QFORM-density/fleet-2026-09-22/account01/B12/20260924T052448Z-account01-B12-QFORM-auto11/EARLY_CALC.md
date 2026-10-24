SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B12, 2026-09-24T05:24:48Z.
attacking: relative-resonance index stability — replace a worst-direction accretive loss by the number of genuinely destructive whitened directions, then spend those directions and keep a five-mode physical cross carrier.

# Early calculation: relative-resonance index reserve

Let M be p x m with full column rank, G=M^T M, g=s_m(M)>0, and let N be an arbitrary p x m addition. Put

U = M G^{-1/2},
K = G^{-1/2} M^T N G^{-1/2},
R = (I-UU^T) N G^{-1/2}.

Then U^T U=I and U^T R=0, hence the exact identity

(M+N)G^{-1/2} = U(I+K)+R

and therefore

G^{-1/2}(M+N)^T(M+N)G^{-1/2}
 = (I+K)^T(I+K)+R^T R.

Fix alpha>0 and let r be the number of eigenvalues of Sym(K)=(K+K^T)/2 that are strictly below -1+alpha. On the spectral subspace E corresponding to eigenvalues >= -1+alpha, dim E >= m-r and for x in E,

<x,(I+K)x> = ||x||^2 + <x,Sym(K)x> >= alpha ||x||^2,

so ||(I+K)x|| >= alpha||x||. The transverse term R only helps. Courant-Fischer then gives

s_{m-r}((M+N)G^{-1/2}) >= alpha.

Since M+N = ((M+N)G^{-1/2}) G^{1/2} and s_m(G^{1/2})=g,

s_{m-r}(M+N) >= alpha g.

Thus a completely arbitrary, full-rank, unbounded addition can destroy at most r carrier singular directions when its whitened relative symmetric part has only r eigenvalues below the cancellation threshold -1+alpha. This strictly refines the scalar worst-direction theorem when r>0.

Low-spectrum compiler: if an additional symmetric spectral packet E_lo has ||E_lo||<=h and a further tail has physical cross action <=delta on the same original-coordinate block, singular-value Weyl gives

s_{m-r}(M_final) >= alpha g - h - delta.

For m-r>=5, the pinned D5 receiver can therefore be applied to the actual original-coordinate cross block, without rotating random inputs or treating a quadratic remainder as an independent convolution.

Status: early calculation only; full QFORM remains OPEN. Next: prove the full statement carefully, apply the completed account02/B12 relative-accretive theorem to an actual matrix inequality, and check a signed unbounded stress family.
