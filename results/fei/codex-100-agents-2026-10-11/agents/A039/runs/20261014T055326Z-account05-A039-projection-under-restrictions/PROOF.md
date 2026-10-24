# Final-frontier compensation under two physical restrictions

All entropy and KL units are bits. Let F(x,a,b,z) be -1 on x=0,a=1, v(z) on x=1,b=1, and +1 otherwise. This is the actual reached root after exposing the essential first u bit of the priority fixture u=(-1,-1,-1,+1) at zero. Let P be its squared Fourier law. Complete the canonical nonempty information projection by M(empty)=P(empty), M(S)=(1-P(empty))Q_r(S) for nonempty S, r_j=Inf_j/(1-P(empty)). Set A=D(P||M). This reference is fixed at the root, rather than replaced at intermediate nodes.

At a queried coordinate i erase its spectral indicator, obtaining q(T). For the actual physical children P_y use k(y|T)=P_y(T)/(2q(T)) when q(T)>0 and k=1/2 otherwise. Erase the current inherited reference Q as well, apply this SAME kernel, and normalize its two outcome-conditioned laws Q_y. Physical outcomes have probabilities 1/2. The erasure KL E and outcome KL O obey

    D(P||Q)=E+O+(D(P_0||Q_0)+D(P_1||Q_1))/2.

This is two applications of the KL chain rule, first to the erased indicator and then to the common kernel. E is nonnegative conditional KL, not a fresh root credit. Source-zero rows are still present in Q and use the declared fair kernel; none may be dropped merely because they carry no source mass.

Query a, then independently select one original data coordinate in each a branch. Let E_tot and O_tot be the first charge plus half the two second-node charges. Let K_end be the mean inherited KL at the four equiprobable final leaves, and TC_end their mean KL to their own product projections. Telescoping gives

    A=E_tot+O_tot+K_end,
    sigma_end=TC_end-K_end,
    D_end=sigma_end-E_tot=O_tot+TC_end-A.                 (1)

There is just ONE final conversion. No intermediate converted-product surplus or erasure account is spent a second time. Mean final H and I are retained explicitly.

## Exhaustive non-flat three-bit interface

For every essential, non-flat Boolean v on three labelled data bits, and every one of the nine adaptive choices of the next data coordinate, the exact certificate proves

    D_end < -19/100.                                    (2)

Here non-flat means that its positive squared Fourier coefficients are not all equal. The frozen domain includes all 256 sign tables and applies this exact filter, with no symmetry quotient; it yields 128 cores and 1,152 policies. Thus the original root account pays the entire final conversion, without withdrawing any terminal surplus. Every actual final leaf also has its directly certified 4I-H>=0. That supplementary finite fact is not used to establish (2).

At each final leaf let Z be the two remaining data coordinates and T=(x,b). Define conditional KL C(P,Q)=D(P||Q)-D(P_T||Q_T). If R is that leaf's product projection, the conditional and quotient conversion debits are

    sigma_Z=C(P,R)-C(P,Q),
    sigma_T=D(P_T||R_T)-D(P_T||Q_T).

They sum exactly to sigma_end after averaging. This explicitly keeps the nonmatching conditional reference bill. The checker finds positive conditional debit in this same domain, despite (2): a favorable total account does not imply componentwise monotonicity. No source-zero erased fibers occur in the frozen non-flat three-bit domain, a checked fact rather than an assumption about general cores.

The certificate uses exact Walsh/influence arithmetic and rational outward enclosures of the root and logarithms. Root c solves 1-c=product_j(1-cr_j); g(0)=0, g'(0)>0 and strict concavity yield the unique positive crossing. Each completed bracket checks g(lo)>0>g(hi), lo>0; all reference marginals and normalization are enclosed. Forty-term atanh logarithms on [1,2] have tail bounded by 2*9/(81*8*3^81); fixed-point outward rounding is at 2^-110. Policy bounds in out/MIXED_CHECK.json are rational certificates, not decimal search evidence. Proof identities justify the tiny enclosure overlap checks; interval overlap alone is not claimed to prove an identity.

## Arbitrarily large parity cores: the second query does not erase the obstruction

Consume the independently reconstructed A038-CERTIFIED-CHILD-SURPLUS-CONVERSION@1. For parity on n>=2 data bits, after querying a the only data spectral supports are empty and the complete parity mask. Erasing any one data coordinate leaves these supports distinct. Restricting that coordinate changes only the sign of the parity block, so the two physical CHILD SQUARED laws coincide exactly. Hence k=1/2 on all fibers, including every source-zero fiber. Its reference outcome is exactly fair: O_second=0. Both child entropies remain H_c=4-(9/8)log2(3), while the queried data marginal 1/4 disappears. Therefore

    D_end=D_first-h2(1/4),
    mean S4_end=mean S4_first-1=n+2-H_c.                 (3)

A038's exact bounds D_first>(n+1)/64-1 and D_first<n/8 give

    D_end>(n+1)/64-2,
    [D_end]_+ < (n-1)/8 < mean S4_end/8, n>=2.          (4)

The first uses h2(1/4)<1; the second uses h2(1/4)>1/8 and H_c<9/4. Thus a single withdrawal of at most one eighth of the ACTUAL final-frontier certified surplus pays the positive debit, while all four terminal entropies are retained. No first-frontier surplus is withdrawn. For n>=128 the debit is positive; this refutes free final conversion for all cores, even after one genuine data restriction in each branch. Since Inf_a=1/2 and the weighted second-query influence is 1/4, the total queried influence is 3/4 independent of n: no finite price by just these two queried influences can pay (4). It is a reference-payment obstruction, not an FEI counterexample. Reference-only data fibers in this parity family are explicitly propagated by the fair kernel and require no hypothetical zero-mass deletion.

## First unsupported universal line

For an arbitrary remaining non-flat core in arbitrary dimension, no proved rule selects a controller/data policy whose previously unused final-frontier budget pays [D_end]_+, the other owned controller cost, and the complete terminal/core bills. Nor may one assume 4I-H>=0 universally. The finite no-withdrawal certificate and the all-dimensional parity payment isolate that ownership requirement; neither proves the universal eligibility statement or full FEI.
