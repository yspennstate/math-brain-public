# A compact reference survives finite moment calibrations

All entropy and divergence quantities are in bits. The result concerns a supplied complete reference. It does not supply the initial FEI payment.

## 1. The representation

Partition the physical coordinates into m disjoint blocks and write f=product_j f_j, where each f_j is Boolean. At every node the same factorization holds on the remaining coordinates. Empty blocks are allowed. Let p=hat(f)^2. A normalized covering reference has the form

    q(S)=sum_{r=1}^R w_r product_j nu_{rj}(S_j)+c 1[S=empty],       (1)

where the nu_{rj} are normalized nonnegative block laws, w_r>=0, c is real, and q is nonnegative and covers p. Thus sum_r w_r+c=1. Only the empty atom may have a negative coefficient; that coefficient is a representation device, not negative reference probability. In particular q(empty)>=0 is an explicit side condition. The construction stores R tables per block and one scalar c.

For any finite adaptive sequence of physical queries and finite positive cardinality tilts with vacuum calibration, R never increases. No new product component is required beyond the single signed vacuum slot. The claim concerns the number of components, not exact numerical bit complexity or entropy evaluation complexity. Block dimensions and initial R are not assumed universally bounded.

## 2. Physical inheritance is local

For a query i in block j, write local Fourier coefficients a_U=hat(f_j)(U), b_U=hat(f_j)(U+i). Define

    k_s(U)=(a_U+s b_U)^2/[2(a_U^2+b_U^2)]

when the denominator is positive, and k_+(U)=k_-(U)=1/2 otherwise. Each of the two parent sets U,U+i maps to output (s,U) with probability k_s(U). This is a stochastic kernel, since k_++k_-=1. On positive true global pairs the other blocks' squared Fourier coefficients cancel, so this is precisely the actual Boolean pair kernel. On zero true pairs this formula supplies a chosen LOCAL ghost completion; an arbitrary nonlocal ghost completion is not covered.

The true joint output law is p_s/2: the child coefficient is a_U+s b_U, and every Boolean child has squared norm one. For component r, apply this kernel only to nu_{rj}. Let its subnormalized branch law be v_{rj,s}, with mass z_{r,s}. The resulting full reference branch is

    K_s q=sum_r w_r (v_{rj,s} product_{k!=j} nu_{rk})
                + c k_s(empty) delta_empty.

Its actual mass z_s is strictly positive because q covers p and the true child has mass 1/2. Divide by z_s, normalize each nonzero v, update w_r to w_r z_{r,s}/z_s, and update c to c k_s(empty)/z_s. A zero component branch is discarded (its block law can be arbitrary). Negative c causes no problem: K_s q is nonnegative because q and K are. This proves (1) is preserved under BOTH physical branches, including singleton blocks, constants, zero local Fourier pairs and nontrivial reference branch normalizers.

## 3. Calibration remains compact

Let rho=p(empty). For rho<1, take x>0 finite and assume

    Z=sum_{S!=empty} q(S)x^{|S|}>0.

Set A=(1-rho)/Z, u(empty)=rho, and u(S)=A q(S)x^{|S|} for S!=empty. For each block put

    M_rj=sum_U nu_rj(U)x^{|U|},
    nu'_rj(U)=nu_rj(U)x^{|U|}/M_rj.

Every M_rj is positive and finite, including empty blocks. Formula (1) becomes

    w'_r=A w_r product_j M_rj,
    c'=A c + rho - A q(empty).

Hence u=sum_r w'_r product_j nu'_rj+c' delta_empty, with exactly the same R. It is manifestly nonnegative as the explicitly defined law u; the signed formula is checked by cancellation at empty. If rho=1 use delta_empty directly. A constant nonempty-cardinality support needs no nontrivial tilt.

If x matches E_u|S|=E_p|S|, the log likelihood ratio log(u/q) is constant at empty and affine in |S| off empty. Matching these two moments gives

    CE(p,q)-CE(p,u)=D(u||q)>=0.                            (2)

Zero-mass empty cells contribute zero; covering ensures all logarithms used under p or u are finite on their support. This reconstructs A096 section 2 at finite positive tilts. The existence criterion is that the required nonempty conditional mean lies strictly between the smallest and largest q-supported nonempty sizes; derivative with respect to log x is positive conditional variance. At extreme means A096 uses conditioning on an extreme level. Such ENDPOINT conditioning is not asserted to preserve (1). No limit of the displayed signed weights is taken. This explicit restriction prevents a hidden unbounded-cancellation argument.

## 4. The original account pays actual query losses

For any node let L be the KL contraction under its stochastic pair kernel, and let O=D((1/2,1/2)||(z_+,z_-)) be the actual reference outcome divergence. Finite data processing and the branch chain rule give

    D(p||q)=L+O+(D(p_+||q_+)+D(p_-||q_-))/2.              (3)

Data processing here follows the finite conditional KL chain rule after retaining the parent set as a hidden variable; thus L>=0. Both branches have positive z_s. Put DeltaH=H(p)-(H(p_+)+H(p_-))/2. This is nonnegative for Boolean restrictions, since it equals the entropy of the queried membership conditional on the rest plus Jensen-Shannon divergence of the child spectra. Combining (2),(3), every finite adaptive tree, with any allowed calibrations between queries, satisfies the EXACT ledger

    CE(root)=E CE(leaf)
             +sum_queries reach*(DeltaH+L+O)
             +sum_calibrations reach*D(u||q).             (4)

All full terminal costs and all query contraction/outcome costs appear. An original owner B with old commitments U and B>=U+CE(root) pays the entire right side from B-U. Calibration releases are inside this equality, not a renewed source. The same calculation works with an inherited common scalar penalty by adding it to both sides. No altered scalar normalization is silently discarded.

## 5. The atom-count witness has a three-term representation

For every even n>=4, take f to be the product of n/2 AND2 signs. Its true spectrum P is uniform on 2^n sets, H=n, I=n/2. The original source q=(P+delta_full)/2 has TWO product components on those blocks and c=0. Since q>=P/2, CE(P,q)<=n+1<=(5/2)I. Apply vacuum and influence calibration with the finite tilt x described in A096 section 3. Equivalently calibrate q directly: vacuum calibration rescales all nonempty masses uniformly, which cancels from the subsequent normalized tilt. Writing M=2^n and

    Z_n(x)=(1+x)^n-1+M x^n,
    A=2(M-1)/Z_n(x),

the final law is

    u = [A(1+x)^n/(2M)] Ber(x/(1+x))^{tensor n}
         + [A x^n/2] delta_full
         + [(1-A/2)/M] delta_empty.                       (5)

Here x is the positive finite solution from A096, not an asserted rational number. Formula (5) follows directly by checking every nonempty set and the empty set. It is a nonnegative probability law even if its last coefficient is negative. A096 proves that positive true-law-plus-individual-atom representations need exactly 2^n-n atom locations. There is no contradiction: (5) changes the product base and allows the one signed vacuum correction. It has TWO nonnegative product terms and ONE signed vacuum term, through every finite allowed adaptive history. The block tables have at most four entries each, so the number of stored real entries is O(n), independently of the exponential atom count. This is a representation count; root solving and numerical precision are separate.

## 6. Scope and first unsupported line

The representation bottleneck for A096's explicit Boolean witness is removed at finite interior calibrations, with the complete physical-query bill retained. General disjoint tensor factors and a supplied finite product-mixture source obey the same closure theorem. Neither arbitrary nonlocal ghost completions nor extreme-cardinality conditioning are included. No stopping class has been shown FEI-certified merely by this representation. For arbitrary cores, taking a single huge block is a vacuous representation, and the initial CE(root)<=C I(root) is still unpaid. The next universal step is to construct a useful bounded-size physical factor/source decomposition at original O(I) cost, or prove a necessary entropy-decaying stopping rule financed by its same unused account.
