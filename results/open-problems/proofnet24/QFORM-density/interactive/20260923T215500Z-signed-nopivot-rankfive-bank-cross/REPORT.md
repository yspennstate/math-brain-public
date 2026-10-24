# Signed no-pivot near-coloop with unavoidable rank-five bank cross term

**Status:** Proved algebraic obstruction to a literal reduction of arbitrary-rank signed matrices to a rank-three canonical quadratic plus bank-local quadratic phases. This is **not** a counterexample to the QFORM bounded-density conjecture: the additional cross terms may improve Fourier decay or supply another receiver.

Fix ε∈(0,1/4], for example ε=10^−6, a tail strength t∈(0,1/2], and an odd integer m>10^18. Let h be one physical hub coordinate, and index m physical leaf coordinates by j=0,…,m−1, with θ_j=2πj/m. Define five mutually orthonormal leaf vectors

ℓ_j=m^−1/2,
v_j=(2/m)^1/2 cos(2θ_j), p_j=(2/m)^1/2 sin(2θ_j),
w_j=(2/m)^1/2 cos(θ_j), z_j=(2/m)^1/2 sin(θ_j).

The finite Fourier orthogonality identities prove the claimed orthonormality. Extend them by zero at h, write h for the physical basis vector at the hub, and define the real symmetric matrix

A=hℓᵀ+ℓhᵀ+ε(ℓpᵀ+pℓᵀ)+vvᵀ+t(wwᵀ−zzᵀ).                 (1)

Thus with H=X_h, L=ℓ·X_leaf, V=v·X_leaf, P=p·X_leaf, W=w·X_leaf and Z=z·X_leaf, the quadratic is

XᵀAX=2HL+2εLP+V²+t(W²−Z²).                               (2)

## Exact spectral and no-pivot properties

On the orthonormal basis (h,ℓ,p,v,w,z), the matrix is the direct sum of

[[0,1,0],[1,0,ε],[0,ε,0]], [1], [t], [−t].

Its nonzero eigenvalues are ±√(1+ε²), 1, t, −t. In particular rank(A)=5 and s3(A)=1. The hub's squared leverage in the top-three spectral subspace is 1/(1+ε²), so it tends to one as ε→0. For ε>0, e_h is NOT itself in that subspace or in range(A): the orthogonal null vector of the three-by-three hub block is proportional to εh−p.

This is an explicit matrix without a 10^−15 physical coordinate pivot. Indeed A_hh=0 and A_hj=1/√m. All leaf entries satisfy |A_ij|≤(3+2√2ε)/m<4/m, since the v contribution is at most 2/m, the t-weighted w/z difference is at most 1/m, and the ε contribution at most 2√2ε/m. Thus every diagonal has modulus <4/m<10^−15. Every hub-leaf principal 2×2 determinant equals −1/m, and every leaf-leaf principal 2×2 determinant has modulus ≤32/m². Both are <10^−15. These are precisely the diagonal and two-by-two determinant conditions of the no-pivot branch.

## Every substantial physical cut keeps a rank-five cross term

For a partition of the leaf indices into I,J with |I|,|J|≥5, let U_I,U_J be restrictions of the five-column frame U=(ℓ,v,p,w,z). Every such restricted frame has rank five. To see this, a linear dependence among its columns would be a trigonometric polynomial of degree at most two vanishing at at least five distinct θ_j. After multiplying by e^{2iθ}, it becomes a complex polynomial of degree at most four with five distinct roots, so every coefficient vanishes.

The leaf-to-leaf cross block has the factorization

A_{I,J}=U_I C U_Jᵀ,

where C has the nonzero ℓ,p entries C_{ℓp}=C_{pℓ}=ε and diagonal entries C_vv=1, C_ww=t, C_zz=−t. Thus C is invertible for ε,t>0, and rank(A_{I,J})=5 for EVERY such cut. The hub coordinate may belong to either bank; restricting its full mixed Hessian to leaf variables already has this rank-five block.

Any three-direction canonical quadratic, even after changing its three linear forms, has a cross-bank matrix of rank at most three. Adding arbitrary bank-local quadratic phases φ_I(X_I)+φ_J(X_J) changes no mixed-bank Hessian entries. Consequently (1) cannot be represented as a three-direction canonical quadratic plus bank-local phases for ANY cut with at least five leaves in each bank. This algebraic statement makes no assertion about other reductions that retain and exploit the additional mixed terms.

In particular, a quantitative two-bank split for the light frame (ℓ,v,p) with Gram matrices U_{I,3}ᵀU_{I,3},U_{J,3}ᵀU_{J,3}≽κI_3 must satisfy |I|,|J|≥κm: each leaf row has squared (ℓ,v,p)-leverage exactly 3/m, so trace of either restricted Gram is 3|I|/m≥3κ. Whenever κm≥5, including the usual fixed κ=1/4 diffuse-frame splits, the rank-five obstruction applies to all such physically useful cuts.

**Scope:** The extra W,Z saddle has singular values t, which can be arbitrarily small or can help the original QFORM density problem; the report only rules out discarding it **exactly** into bank-local phases. A structural proof can still handle such mixed terms by a separate higher-rank Fourier or coarea receiver. No product-source distribution or output density counterexample is claimed.

Small operator norm alone does not justify discarding the tail uniformly over the allowed input laws. For each t>0 let the leaf originals be X_j=Y_j+t^{−1}w_j, with independent Y_j uniform on [−1/2,1/2]. Orthogonality leaves L,V,P,Z equal to their Y-projections, but W=t^{−1}+w·Y. After subtracting the deterministic constant t^{−1}, the tail t(W²−Z²) equals 2w·Y+t((w·Y)²−(z·Y)²), which converges to the nonzero random affine form 2w·Y as t↓0. This observation only blocks a naive norm-small truncation; it does not rule out a proof that handles the induced affine terms.
