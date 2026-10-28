# Same inherited debit at a growing reveal depth

Full FEI is OPEN. The endpoint theorem below concerns a prescribed rate-4 account. It does not assert a dimension-independent FEI inequality.

## 1. Actual Boolean family and the original debit

Use bit strings for the uniform sign cube, with bit 1 denoting the negative input. All entropy is in bits. Let g_n be -1 exactly at 0,1,2 in n physical bits. Let h be -1 on {0,1,2,4,8,16,32,6,17,40} and J(x)=-h(x xor 1). Set F_n=J(g_n,...,g_n) on six disjoint blocks. Write S=4I-H and p=3*2^{-n}.

In block 0 query original coordinate 2, retaining answer 0; then original coordinate 0, retaining answer 0. Denote root, first retained, second retained, and opposite second child by r,a,b,c. Denote by Z the FULL function with selected core fixed +1, the other five cores unchanged. It remains a nonconstant function. Selected core b is -1 on {0,1} in n-2 remaining bits, of which original bit 1 is a dummy. Core c is a point defect. Set

    e1=(S_a+S_Z)/2-S_r,
    e2=(S_b+S_c)/2-S_a,
    U_v=q0*S(selected core v),
    B2=(U_b+U_c)/2,
    D0=(2e1+e2)*U_b/B2.

This is the ORIGINAL two-query debit; it is never replaced by a new allowance. Each signed ancestor label follows the same multiplication as the net debit. For large n, B2>0 and D0>0, so these expressions are defined. The first stopped sibling Z and the opposite second child c retain their original bookings throughout.

## 2. Exact full spectra and the asymptotic inputs

For independent inner cores with minority probabilities p_j, write mu_j=1-2p_j and v_j=1-mu_j^2. Orthogonality gives the occupied-block Fourier mass

    P_T=prod_{j in T} v_j * (sum_{U containing T} Jhat(U) prod_{j in U\T} mu_j)^2.

The physical pivotal factor q_j is the probability over the other five core signs that J changes on flipping j. The sum of occupied masses containing j is q_j*v_j. Conditional on occupied T, the nonempty inner Fourier sets have their independent normalized squared spectra. Shannon's finite chain rule therefore gives

    I(F)=sum_j q_j I(g_j),
    H(F)=sum_j q_j H(g_j)+C,
    C=H((P_T)_T)-sum_j q_j h2(v_j).

Constant cores contribute zero occupancy and zero H and I, without division by v_j. These formulas include EVERY full terminal and all remaining five blocks.

Put E=log2(e), L=log2(3), a0=6L-8/3-4E, A=4a0. For any sparse remaining side B subset {0,1,2} in dimension d>=2, the empty Fourier coefficient is 1-2|B|/2^d. A nonempty coefficient with its first two frequency bits z equals -2*sum_{x in B}(-1)^{x.z}/2^d, with multiplicity 2^{d-2}-1[z=0]. Its influence is (2|B|d-4*internal_edges(B))/2^d. This proves the compressed inner spectra used here.

Expand the FINITE rational polynomials P_T and q_j and -x log2 x at their positive leading coefficients. A mass cp^r+... has a convergent Taylor expansion after factoring cp^r; omitted terms are O(p^3(1+|log p|)) for the fixed initial profiles. Exact rational coefficient collection in code/diagonal.py (calling series in the pinned bridge helper) yields

    S(g_n)=a0*p+O(p^2(1+|log p|)),
    S_Z=A*p+O(p^2(1+|log p|)),
    e1=O(p^3(1+|log p|)),
    e2=(256/3-48L)*p^2+O(p^3(1+|log p|)),
    U_b=(128/3)(2-E)*p^2+O(p^3(1+|log p|)),
    U_c=U_b/2+O(p^3(1+|log p|)),
    D0=lambda*p^2+O(p^3(1+|log p|)), lambda=1024/9-64L,
    S_b-S_Z=(256/9-64L-(128/3)E)*p^2+O(p^3(1+|log p|)).

In particular the inherited-debit difference is

    Delta_n=S_b-D0-S_Z
           =-(128/3)(2+E)*p^2+O(p^3(1+|log p|)).                 (1)

The rational expansions, exact cancellations of log p, and explicit interval signs are saved in out/DIAGONAL_ANALYTIC.json. Coefficient equality is algebraic, not inferred from overlapping numerical intervals.

## 3. Telescoping the SAME debit

Continue by querying original padding coordinates 3,4,..., always retaining zero. At depth j>=0 after the two initial queries, the selected core is the pair defect in n-2-j bits. Let S_j be the full capacity; the one child is always the same full function Z. Set e_j=(S_{j+1}+S_Z)/2-S_j and prescribe

    D_{j+1}=2(D_j+e_j),

with zero booking on the new Z sibling. Every inherited signed label is multiplied by 2 in the zero child and 0 in the one child; the new label is handled identically, so each conditional mean and every earlier stopped label is preserved. This definition is an algebraic continuation; it does not assume the result is affordable.

Subtraction gives exactly

    D_{j+1}-S_{j+1}=2(D_j-S_j)+S_Z,
    R_j:=S_j-D_j=S_Z+2^j*Delta_n.                              (2)

Thus for any fixed n with Delta_n<0 the FULL remaining capacity decreases strictly with j. Raw selected capacity U_j or raw full capacity S_j alone cannot replace R_j.

## 4. A growing-depth endpoint theorem

Fix d>=2 and take j=n-d-2. Then 2^j*p=3/2^{d+2} EXACTLY. Equations (1),(2), without interchanging a nonuniform fixed-depth expansion, imply

    R_{n,d}/p -> K_d=A-2^{5-d}(2+E).                           (3)

Indeed only the FIXED initial profiles and Z were expanded; multiplication of the error in (1) by 2^j leaves O_d(p^2(1+|log p|))=o(p). The original fixed-depth result and this result are compatible: j now grows with n.

Directed rational bounds prove

    4.2893126964 < A < 4.2893126965,
    -2.5960773854 < K_4 < -2.5960773853,
    0.8466176555 < K_5 < 0.8466176556,
    1.6932353110 < A+K_4 < 1.6932353111.

Consequently, for all sufficiently large integer n, the prescribed no-transfer continuation cannot be fully feasible through j=n-6: its final remaining capacity is negative. This contradiction does NOT require assuming every earlier debit was legal. In fact (2) and K_5>0 show all earlier FULL residuals are positive for large n. Nonnegativity of every intermediate NET debit for all n is a separate condition and is NOT asserted here; it is checked on the three explicitly frozen complete finite chains only.

For clarity the last parent and child themselves have positive capacities and nonnegative booked debits eventually. To see this independently of (3), put u=2^{1-d}, so the remaining pair core has the spectrum of an AND on d-1 active bits plus one dummy. Its capacity is

    s(u)=8u(1-u)-8u^2 log2 u+2(1-2u)^2 log2(1-2u).

With the other cores rare, q0=4p+O(p^2), sum_{j>0}q_j=4(1-u)+O(p). The first-order occupied masses are: empty 1-16(1-u)p; four singletons 4(1-u)^2 p; four selected/singleton pairs 4u(1-u)p; others O(p^2). Hence

    C/p -> C1(u)
      =-32(1-u)^2 log2(1-u)+32u(1-u)+8(1-2u)^2 log2(1-2u),
    S_{n,d}/p -> G(u)=A(1-u)+32[(1-u)^2 log2(1-u)-u^2 log2 u].

The exact polynomial calculation independently agrees with both displayed closed forms. Certified intervals give

    d=4: G in (0.5333441997,0.5333441999), G-K4 in (3.1294215850,3.1294215853);
    d=5: G in (1.9025286543,1.9025286545), G-K5 in (1.0559109987,1.0559109990).

The last parent thus admits its inherited nonnegative debit, but its prescribed zero-child debit exceeds that child's FULL capacity. This is an accounting obstruction even with positive full terminal S; it is distinct from A089's negative full S witnesses.

## 5. Sharp local repair with bookings fixed

At the query from remaining dimension 5 to 4, keep all prescribed old and new debit labels EXACTLY unchanged. The zero child has debit D_{n,4}; the new Z sibling has debit 0. Let a_n=-R_{n,4}>0. Give zero child flow +a_n and its sibling flow -a_n. The mean transfer is zero and residuals become 0 and S_Z-a_n=S_Z+R_{n,4}. By A+K4>0 the latter is positive for all sufficiently large n. The last sibling has never been debited by this prescribed policy. All earlier stopped functions, labels, probabilities and debit owners remain unchanged. No prior source is renewed.

This subsidy is minimal with these bookings fixed: child residual positivity forces any incoming flow to be at least D_{n,4}-S_{n,4}=a_n. The root reach of this zero child is 2^{-(j+2)}=2^{4-n}=(16/3)p. Its minimum root-weighted gross incoming flow therefore satisfies

    root_cost/p^2 -> Gamma4=-(16/3)K4
       =(32/3)(2+E)-(16/3)A in (13.8457460552,13.8457460553).

This is local payment of an explicitly supplied inherited account, not a proof that every earlier nonnegative-debit history is admissible for all n. Three complete finite histories (n=8,12,24) separately certify every prefix net debit and full residual before the last repair. The other three frozen n values certify ONLY their d=5 and d=4 endpoints.

There is a useful adversarial qualification: the positive transfer cost is forced ONLY when the prescribed descendant bookings are fixed. Both raw full children here have positive S. If their NEW descendant bookings may instead be reassigned with the same conditional means, put B=(S_child+S_Z)/2, T=D_child/2, k_i=S_i/B. Since B-T=R_parent>0 eventually, d_i=T*k_i and f_i=0 are feasible. Transport each signed old/new label by the same k. This retains their means and needs no transfer. Thus Gamma4 is the cost of the specified all-to-zero routing, not a lower bound over all admissible payment policies. In contrast, A089's negative full terminals force positive flow even when booking reassignment is allowed. This distinction is central to the next universal admission test.

## 6. Independent reconstruction of A089's signed terminal theorem

Source: A089-SIGNED-TERMINAL-COMMON-KERNEL-REPAIR@1, source declared digest 7de96cb26ca33032ed22556b3aa7b89ca42d5acb81822f1715144de96cf8c25d. This review keeps the report's explicit positive-weight-support convention.

For signed capacities s_b and nonnegative bookings d_b of prescribed mean T>=0, zero-mean flows f_b and nonnegative residuals imply T<=mean s. On each negative s_b the flow must be at least -s_b, so gross incoming flow has lower bound N=mean(-s)_+. Put P=mean(s)_+. If P>0 and T<=P-N, take k=s_+/P, d=T*k, f=(-s)_+-N*k. On negative states residual is zero; on nonnegative states it is (P-N-T)*k>=0. The gross flow is exactly N. All signed old labels L and the new label e can be multiplied by k, preserving their conditional means even if T=0. If P=0, feasibility forces N=T=0 and s=0 on positive-weight support; choose d=f=0 and k=1. Zero-weight states are omitted. This proves the generic theorem without treating the aggregate condition as automatic.

Own code/review_signed.py constructs every core from its ORIGINAL six-bit truth table, uses direct physical edges for influence, checks that against FWHT influence, and then reconstructs the full occupied-set spectrum. The domain is all 18 labelled restrictions specified in A089's report. Exactly two have negative full S: bit4=bit5=0 with block1 bit0=b. Their necessary subsidies are in (0.055,0.056) and (0.045,0.046). This is an independent review of the generic theorem and the 18 physical signs. The four source whole-history allocations and the old parked2tau ancestry are NOT newly independently accepted by this stage; their source scope and prior accepted dependencies are preserved separately.

## 7. Honest universal gap and the strongest objection

An objection to a broader conclusion is decisive: a formula for a formal debit does not establish nonnegative debit legality at every growing-depth ancestor, and a local sibling payment does not supply admission on arbitrary non-flat component histories. This proof explicitly does neither. Its unconditional conclusions are the exact ledger identity, asymptotic endpoint signs, the impossibility of uniform no-transfer continuation, and the sharp last-row repair of the supplied account. The bounded certificates settle their frozen finite domains only.

First unsupported universal line: derive the signed conditional admission bound for a further physical query AFTER the recipient has received its exact subsidy, while retaining the donor's already spent outgoing flow, all prior bookings, and every full terminal. Computing full S everywhere and assuming its mean covers the debit merely restates the unpaid entropy bill. A074/A092 should check the quantifiers and the endpoint proof; A089/A072 should carry the same credit into that next physical query. Full FEI remains OPEN.
