# Conditioned blockers: the exact surviving spectral debt

All entropy is in bits. Let w>=2 and m>=1 be integers, let b_l be positive width-w conjunctions on pairwise disjoint blocks, and f=2 OR_l b_l-1. Put p=2^-w and c=(1-p)^(m-1). For j in block l, the half-difference derivative is

    d_j f = u_j C_j,
    u_j=AND(block l minus j), C_j=product_{r!=l}(1-b_r).

This is exactly the local ideal from the interrupted stage: local remainder zero, local pressure theta_j=0, and alpha_j=2pc. The distant blocker C_j is independent of u_j physically, but has nontrivial Fourier spectrum.

## Exact off-support obstruction

Call a nonempty Fourier set A good if it is contained in one original block, and bad otherwise. Each derivative Fourier index T corresponds to A=T union {j}. A is good exactly when the outside-block part of T is empty. Parseval gives ||C_j||^2=c and C_jhat(empty)^2=c^2; also ||u_j||^2=2p. Independence of the blocks therefore gives

    sum_{bad A containing j} fhat(A)^2=2p(c-c^2)=alpha_j(1-c).
    I(f)=mw*2pc.
    sum_bad |A| fhat(A)^2=I(f)[1-(1-p)^(m-1)].

For fixed w, the last ratio tends to one as m tends to infinity, while every conditioned remainder is zero. Already w=2,m=2 gives positive bad mass 3/8 and I=3/2, hence bad/I=1/4; w=2,m=4 gives bad/I=37/64. Thus the proposed substitution

    sum_bad |A| fhat(A)^2 <= sum_j ||r_local,j||^2

is false, including on read-one linear hypergraphs. This refutes a transfer shortcut, not FEI, A009's retained raw-error theorem, or the local rank bound. The erroneous step would be to say the conditioned ideals have no Fourier support outside their gate: C_j contributes outside variables.

## Why derivative entropy alone also fails

For g=1-b on one width-w block, ||g||^2=1-p. Its normalized squared spectrum has empty probability 1-p and probability p^2/(1-p) on each of its 2^w-1 nonempty subsets. Consequently

    h_g=h2(p)+p log2(2^w-1).

The normalized squared derivative spectrum is the product of a uniform spectrum on the residual width-(w-1) block and m-1 copies of this distribution. Its entropy is exactly

    H(nu_j)=w-1+(m-1)h_g.

This diverges for fixed w although theta_j=0. In particular sum_j alpha_j H(nu_j)/I(f) equals this expression, so a uniform influence-paid bound for the full normalized derivative entropy cannot be the missing bridge. Since h2(p)>=p log2(1/p)=pw, the explicit rational lower bound w-1+(m-1)pw already proves divergence. No logarithm approximation is needed for this sign.

## Whole-function product payment, with activation retained

This paragraph records the accounting that repairs this example; it is an application of known disjoint-product/read-once identities, not a new read-once FEI claim. Put a=(1-p)^m and C=product_l(1-b_l), so f=1-2C. The normalized squared spectrum P_C of C is a product distribution with entropy m h_g and empty probability a. For every nonempty A, fhat(A)^2=4a P_C(A); the actual nonempty spectral mass is v=4a(1-a). The empty output mass is (1-2a)^2=1-v. Separating empty/nonempty entropy gives the exact identity

    H(f)=h2(v)+4a[m h_g-h2(a)],
    I(f)=2mwp*a/(1-p).

The difference m h_g-h2(a) is nonnegative: it is (1-a) times the entropy of P_C conditioned nonempty. The blocker entropy is therefore paid ONCE by the whole-function activation factor 4a, not m times by derivatives. For orientation, h2(v)<=2I (the established variance entropy bound), h_g<=2wp+p log2 e, and dropping -h2(a) gives

    H(f)/I(f)<=2+4(1-p)+2(1-p)log2(e)/w<8  (w>=2).

Only the normalized finite-block masses, the full spectrum/influence, and the off-support identities are executed exact checks below. The entropy identity is proved analytically by the entropy chain rule, not certified by a floating logarithm.

## Connection to the all-density transfer

A009 FOREST_TRANSFER.tex's scalar transfer uses the unconditioned ideal G=2sum_l b_l-1, whose Fourier support is gate-contained. Replacing it by local conditioned ideals fixes physical error but loses that common gate-contained support. Further, the local ideals depend on j and need not be derivatives of one global Boolean or scalar ideal, so there is no shared amplitude on a whole A available for the old owner argument.

First unsupported line: for overlapping positive linear hypergraphs, construct ONE normalized whole-set blocker/activation reference whose expected complete label, subset, rank and normalization costs are O(I), without counting a shared blocker once per derivative. Disjoint-product factorization proves the payment above; physical conditioning alone does not supply it when blocker families overlap. The next step is a two-blocker overlap interface, retaining signed collisions and the once-paid nonempty activation mass. This is the C020 whole-set witness-cost bridge named by B03, rather than a new isolated class target.
