# Actual product-reference reset cannot be paid by local information or marginal-entropy loss

Author proof; independent review pending. This is an actual Boolean family of reference-payment obstructions, NOT a counterexample to FEI or a good-coordinate theorem. It strengthens the diagnostic separation of physical revelation from reference outcome mismatch.

## Boolean family and the source actually used

Let n=2r>=4, z=(u_1,v_1,...,u_r,v_r), all bits uniform. Define two actual Boolean functions

    g_dense(z)=(-1)^(sum_j u_j v_j),
    g_sparse(z)=(-1)^((sum_j u_j mod2)(sum_j v_j mod2)).

Let F(x,z)=g_dense(z) for x=0 and g_sparse(z) for x=1. Use the ACTUAL FULL PRODUCT of the root spectral marginals as the incoming normalized reference Q. Query x, use the actual coherent kernel, then actually reset BOTH child references to the ACTUAL child marginal products. No source replacement or asymptotic non-Boolean spectrum is involved.

Each two-bit gate (-1)^(uv) has Fourier amplitudes (1,1,1,-1)/2. Tensoring r gates gives the dense squared spectrum p_dense(T)=1/N for every T, N=2^n. Substituting the two nonempty disjoint parities U=sum u_j and V=sum v_j into that same gate gives the sparse spectrum uniform on the four masks {empty,U,V,U union V}. Call their support C. Every z coordinate belongs to exactly one of U,V, so BOTH children have actual influence1/2 on EVERY z coordinate. Therefore Q erased at x is exactly the uniform law1/N. Its spectator Jensen loss Gamma is exactly zero.

For completeness the source queried influence is d_x=(1-<g_dense,g_sparse>)/2. Writing the two gates as bilinear forms, their product has matrix I_r+J_r over F2. Averaging over u first gives <g_dense,g_sparse>=2^-rank(I+J). The rank is r for even r and r-1 for odd r: a kernel vector must be (sum v_j)1, and summing again decides whether the constant vector is admitted. Thus d_x is positive for r>=2 and <=1/2. Q genuinely supports the full root squared law.

## Exact physical and reference outcome laws

The erased source q=(p_dense+p_sparse)/2 is positive everywhere. Its physical coherent kernel is k_y(T)=p_y(T)/(p_dense(T)+p_sparse(T)). On C the sparse kernel probability is N/(N+4), and off C it is zero. Applying the erased REFERENCE, which is uniform, gives

    pi_sparse=4/(N+4),  pi_dense=N/(N+4).

The physical branch marginal is fair, as always. The reference outcome mismatch is exactly

    O_n=(1/2)log2((N+4)^2/(16N)) >=(n-4)/2.             (1)

Meanwhile actual branch revelation is J_n=JS(p_dense,p_sparse)<=1, and spectral erasure B_x<=1. With the genuine incoming product reference, the signed cost of the exercised child-product reset is

    sigma_n=J_n+O_n-Gamma=J_n+O_n >=(n-4)/2.             (2)

The information actually revealed is at most ONE bit; reference renormalization can cost arbitrarily many bits. Erasure KL remains E_x=h2(d_x)-B_x and is not identified with either J_n or O_n. Each child's entropy and KL remain in sigma_n's definition. This does not assert a negative total KL or pay a new source for free.

The actual marginal-entropy drift is exactly

    Delta M=M(F)-mean M(child)=h2(d_x)<=1,               (3)

since every spectator influence is1/2 in both children. For every fixed finite c, a sufficiently large even n makes sigma_n>c Delta M, and also sigma_n>c J_n or c B_x. No universal local payment sigma_+<=c Delta M, or sigma_+<=c times the actual physical revelation, can cover every exercised product-reference reset. This conclusion uses a fixed real query; it does NOT say every coordinate is bad.

An exact small certificate is n6: d_x=3/8, all six spectator marginals are1/2, reference outcomes are (16/17,1/17), and O_6=(1/2)log2(289/64)>1 because289>256. Hence the positive reset already exceeds the entire marginal-entropy drop h2(3/8)<1 on this explicit seven-variable Boolean source.

## What survives and what must change

The original source's FULL KL and the complete terminal entropies remain in the account. In particular I(F)=n/2+d_x grows with n. The obstruction therefore leaves open payment from a genuinely unused ORIGINAL global influence-scale owner. It excludes only the hoped-for repair replacing depth-times-M by a universal per-query marginal-entropy drift price, without using that global owner or source-specific inherited credits.

This differs from A087's point-family Q=p obstruction, where O=0 and initial reference eligibility is the issue: here Q is the actual marginal product, Gamma=0, physical information<=1, and O itself diverges. The first universal unpaid line is to charge this reference outcome mismatch to an eligible original nonlocal owner without spending the parent KL/influence allowance twice. NEXT must retain original source K, E and all old debits and analyze the minimal signed pending reserve, or select a different query; it must not assume a local information/drift payment contradicted by (1)-(3).
