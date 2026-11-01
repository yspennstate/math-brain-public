# A058 v2 effective-support ledger

For `K(x,z)=1-2 1_{x=-1}1_{Lz in B}`, let

- `p=|B|/2^r`, `ell=log2(1/p)`;
- `a_alpha` be the normalized Fourier coefficients of `1_B`;
- `M=#{alpha:a_alpha!=0}` and `d=log2(2M-1)`;
- `q=2p-p^2`.

The exact identities are

`sum a_alpha^2=p`,

`q_nonconstant=p^2+2 sum_{alpha!=0}a_alpha^2=2p-p^2`,

and

`I(K)=p+2 sum_{alpha!=0}|L^T alpha|a_alpha^2
     =p+I(1-2 1_A)/2`.

There are at most `2M-1` nonconstant atoms, so

`H(K)<=h2(q)+q d`.

For `p<=1/2`, physical cube isoperimetry gives

`I(K)>=p(1+ell)`.

The elementary binary-entropy estimate

`h2(q)<=q log2(1/q)+q log2(e)`

then gives

`H(K)<=p(2-p)[ell+log2(e)+d]`.

Hence `d<=2ell+1` implies

`H(K)<6p(ell+1)<=6I(K)`.

This strengthens version 1 in two independent ways:

1. the constant improves from `8` to `6`;
2. the quotient dimension `r` is replaced by the actual Fourier-
   support cost `d`, admitting 52 additional finite cases in the
   exhaustive audit through quotient dimension four.

Since `M<=2^r`, the previous simple hypothesis `ell>=r/2` remains a
corollary, now without the extra `p<=1/4` assumption.

The payment still uses the complete physical data boundary. It does
not assert selector-only payment, shared-product subadditivity, or a
fixed-Renyi bound. The optional multiplication by an unrelated leaf
continues to require disjoint tensorization.
