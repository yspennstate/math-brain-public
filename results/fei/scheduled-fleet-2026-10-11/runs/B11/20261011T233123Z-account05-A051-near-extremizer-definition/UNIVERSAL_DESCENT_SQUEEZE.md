# Universal relation between block descent and the FEI ratio

All functions are actual Boolean signs on the n-bit uniform cube, n>=2, and entropy is in bits. For every nonconstant f define R(f)=H(f)/I(f), and

phi(f)=min_{empty!=A proper subset [n], I_A>0} [H(f)-E_a H(f_a)]/I_A.

The full block is excluded. Define M_n=max_f R(f) over nonconstant n-bit functions, irrelevant variables permitted, and K_desc(n)=max_f phi(f). The finite maxima exist. Constants never enter the ratios. The preceding A051 stage proved well-ordered fixed-C critical witness existence; the following argument is self-contained and uses no unreviewed lead inequality.

## 1. Co-singleton bound

Fix a coordinate i and reveal A=[n] minus {i}. Every physical child is a Boolean function on one bit and hence is constant or a signed character. Its squared Fourier law is a point mass, so H(f_a)=0. Thus L_A=H(f) and I_A=I(f)-Inf_i(f).

Choose i with Inf_i(f)=min_j Inf_j(f). Since this minimum is at most I(f)/n, I_A>=I(f)(n-1)/n>0. Therefore

phi(f)<=H(f)/(I(f)-min_i Inf_i(f))<=n R(f)/(n-1).             (1)

This remains valid when H=0 (both sides vanish) or some coordinates are irrelevant. In particular every function of dimension 6,7,8,9 with positive H has phi/R at most 6/5,7/6,8/7,9/8 respectively. A proposed test that phi/R<=1.33 in this range is automatic, regardless of composition, connectedness, tensor primitivity or Boolean structure beyond the one-bit classification. It supplies no discriminating evidence for a universal block payment.

## 2. Reverse inequality at a finite-dimensional optimizer

Choose a function f attaining M_n. Every proper physical child lives on at most n-1 coordinates. Extend it by dummy coordinates if needed; its ratio is at most M_n by the definition of the n-dimensional maximum. Constants have H=I=0. Averaging each physical j-edge indicator over the coordinates in A, for j outside A, proves E I(f_a)=I(f)-I_A. For every nonempty proper A,

E H(f_a)<=M_n E I(f_a)=M_n(I(f)-I_A).

Since H(f)=M_n I(f), it follows that L_A>=M_n I_A. Every admissible A therefore has L_A/I_A>=M_n, so phi(f)>=M_n. Combining this with (1) gives the exact dimensionwise squeeze

M_n <= K_desc(n) <= n M_n/(n-1), n>=2.                    (2)

No optimizer over all dimensions is assumed. The only existence used is the finite n-bit truth-table maximum established in the previous packet. This is stronger than the lead's inductive bound M_n<=max(M_(n-1),K_desc(n)), but does not bound either quantity independently.

## 3. Consequence for the universal bridge

If C_* = sup_n M_n is finite, then M_n increases to C_* by dummy padding and (2) implies K_desc(n) tends to C_*. In particular sup_n K_desc(n)<=2 C_* is finite. Conversely if sup_n K_desc(n) is finite, (2) bounds C_* by that supremum. If C_*=infinity, (2) forces K_desc(n) to tend to infinity too. Thus the large-dimensional proper-block extremal constant and the FEI ratio are squeezed by a factor tending to one, without a tree-payment theorem.

For each epsilon>0 and n>=1+1/epsilon, K_desc(n)<= (1+epsilon)M_n. The remaining obstruction is exactly a dimension-independent bound on M_n (or K_desc(n)); (2) is not that bound. The co-singleton strategy itself spends the entire root entropy and does not make it cheaper than an already proved H/I estimate. It is therefore not a newly paid C019 restriction rule.

## 4. Scope and review

This corrects the interpretation of the lead's requested phi/R<=1.33 experiment. It does not refute the requested phi>4.54 search, since (1) controls phi by the still-variable R. Nor does it refute a structural proof paying smaller blocks, certify all Boolean functions from a NAND-family census, or disprove FEI. Reviewer A090/A094 should independently reconstruct the one-bit child entropy classification and the optimizer comparison in section 2 before acceptance.
