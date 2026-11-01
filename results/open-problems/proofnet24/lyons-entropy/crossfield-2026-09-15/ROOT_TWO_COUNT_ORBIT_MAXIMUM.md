# Root derivation — the two-count envelope is attained on every balanced block orbit

Status: exact entropy-maximization identity, not a full-Hessian theorem and not another sub-agent. Supplied to X044 as a constructive continuation of X030.

For K(Z)=I4/2+[[0,Z],[Z*,0]], put C=2Z and let r,s in [0,1] be the eigenvalues of CC*. Let N_A,N_B be the occupation counts in the two measured pairs. Their joint law depends only on r,s, since its generating polynomial is

    h(z)^2 h(w)^2 − ||Z||F² (z−1)(w−1)h(z)h(w)
                         + |det Z|² (z−1)^2(w−1)^2,
    h(z)=(1+z)/2.

This follows from the block determinant generating function and is invariant under separate block unitaries. Define the two-count envelope

    Phi(r,s)=H(N_A,N_B)+E log[binom(2,N_A) binom(2,N_B)].

Conditioning on the two counts gives H(P_K(Z))≤Phi(r,s). This upper bound is attained somewhere on every block-unitary orbit.

For r+s>0, set a=(r+s)/4 and choose phi in [0,pi] with

    cos(phi)=1−8rs/(r+s)^2.

The expression lies in [-1,1] by (r−s)^2≥0. The equal-modulus matrix

    C_* = sqrt(a) [[1,1],[1,exp(i phi)]]

satisfies tr(C_*C_*†)=r+s and |det C_*|²=rs, so it has the same singular values as C. It therefore belongs to the same left/right unitary orbit. Put x=N_A−1 and y=N_B−1. Centered inclusion moments and Boolean inversion give each measured atom at this matrix as

    p(S,T)=1/16 [1−4a xy+rs(2x²−1)(2y²−1)].

This depends only on the two counts, so the conditional distribution in each count fiber is uniform. The entropy upper bound is equality. At r=s=0 the product law proves the same statement directly, and boundary cases follow either from the polynomial formula or continuity. Hence

    max_{U,V in U(2)} H(P_K(U Z V)) = Phi(r,s).

This maximizes measured entropy over a block-unitary orbit; it does not identify measured entropy at every point of that orbit. The envelope has an invariant Hessian, while the actual entropy need not. A proof of the envelope's full Hermitian Hessian sign at balanced bases would transfer to the actual entropy at these touching equal-modulus bases. X030 proves the rank-one case; the all-parameter Hessian claim is left to X044 and is not assumed here.
