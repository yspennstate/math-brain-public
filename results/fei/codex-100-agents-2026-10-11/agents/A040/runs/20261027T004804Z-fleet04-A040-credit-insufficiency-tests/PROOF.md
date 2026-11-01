# The chi-square surrogate can exceed its entire original payer

All information is in bits. This tests the sufficient charge proposed in A040 stage10, not the true outcome invoice. The policy is prescribed to start with the rare coordinate j. No claim is made about every possible first coordinate or every stopping policy. Full FEI remains open.

## 1. Exact original-source payment survives

Read A050-FIXED-PROFILE-ZERO-COST-REPAIR@1, PROOF sections1-3, and A049's independent reconstruction in its 20261026T221646Z PROOF section4. For any finite adaptive physical tree, transport an admitted support-matched reference through erasure and the actual signed-amplitude kernel, using its own outcome normalizers. With no refreshes,

    K_root = sum_h w_h(E_h+O_h) + E K_leaf.

Here K=D(P||Q), E is KL lost under erasure and O=D(fair||reference outcomes). Every term is nonnegative. Consequently the actual cumulative outcome invoice never exceeds the SAME original K. This is a supplied-source statement. Source cross entropy is H+K, so it does not pay H or provide an influence-priced initial supplier. With old conversion Sigma_old and old debit omega, the complete ledger still has residual min(S,M0-Sigma_old)-omega, where M0=4I0-H0-K0 and S=E(4I_leaf-H_leaf). Neither terminal entropy nor either physical branch disappears.

The present calculation tests replacing the exact O_h by the larger stage10 sufficient charge. It supplies no new independent acceptance of A050 (A049 has already reconstructed it).

## 2. Actual Boolean family and exact geometry

For integer r>=3 put d=2^-r, w in {0,1}^r, e=(1,1,0,...,0), and

    v(j,z,w)=(-1)^z(1-2*1[w=0 or (j=1,w=e)]),
    G(x,j,z,w)=1 when x=0, v when x=1.

The core v is balanced because of z. Let p be the full Fourier law of G. Supply exactly the support-matched activated full-spike reference used in A040 stages9-10: keep the two controller-only atoms p=1/4 unchanged, and on the active half replace the core P_v by (1-alpha)P_v+alpha delta_FULL. Thus q>=beta p, beta=1-alpha, and the full reference mass remains one. Query j FIRST and thereafter carry its inherited reference. No optional refresh is required.

Write the coefficients of v paired across j as A_W,B_W, suppressing its compulsory z bit. If s_W=(-1)^(W dot e), then

    W=empty: A_W=1-3d, B_W=d;
    W!=empty: A_W=-(2+s_W)d, B_W=s_W*d.

There are 1/(2d)-1 nonempty W with s_W=1 and 1/(2d) with s_W=-1. For the erased law pbar and score s=ab/(a^2+b^2) of G, define V=E_pbar s^2 and X=chi2(qbar||pbar). Direct summation gives

    eta=Inf_j(G)=d/2,
    V=1/2*[d^2(1-3d)^2/((1-3d)^2+d^2) + 7d/10 -9d^2/10],
    X=alpha^2/2*[1/(10d^2)-1],
    t=E_qbar s=-3alpha/20,
    O=-log2(1-9alpha^2/100)/2.                         (1)

The two activated copies of the erased core full row have combined source mass 5d^2 in G and both have score -3/10. The reference adds combined mass alpha/2 there and subtracts alpha times the active source law. The active source score has mean zero, giving t. X follows from the chi-square divergence between the core erased law and its full-row spike, multiplied by the active weight 1/2. Controller-only rows have score zero and unchanged reference mass. Every denominator is positive for r>=3. All displayed core coefficients are nonzero; the reference has exactly source support.

For source KL, with m=d^2,

    K=1/2*[(1-m)log2(1/beta)+m log2(m/(alpha+beta*m))]. (2)

It is strictly positive because the reference differs from its source and m<1. Source mean-score zero is the actual Boolean Parseval identity; this construction does not substitute an arbitrary law for a Boolean spectrum.

## 3. A quantitative obstruction to the proposed cumulative charge

Set alpha=r^-2 once at the root. Let L=ln(2). The two stage10 sufficient outcome bounds are

    C_V = 2 X V/[beta(2-beta)L],
    C_eta = 2 X eta(1-eta)/[beta(2-beta)L].

Both are positive and O<=C_V<=C_eta. The first uses the EXACT variance, so replacing eta(1-eta) by V does not repair this obstruction. From (1)-(2),

    V~7d/20, X~alpha^2/(20d^2), K~alpha/(2L),
    O~9alpha^2/(200L),
    C_V~7alpha^2/(200Ld), C_eta~alpha^2/(20Ld).

Consequently

    C_V/O~7/(9d),       C_eta/O~10/(9d),
    C_V/K~7*2^r/(100r^2), C_eta/K~2^r/(10r^2),
    O/K~9/(100r^2) ->0.                              (3)

These are asymptotic equivalences as r tends through the integers. A one-node nonnegative surrogate sum already has unbounded ratio to the entire original K. Any tree REQUIRED to start with j inherits this obstruction at its first node, even though its exact complete cumulative outcome sum is <=K by section1. Optional coordinate avoidance is not refuted.

For completeness, the expansion of (2) is uniform at alpha=r^-2: its first term is alpha/L+O(alpha^2+alpha*m). The second has absolute magnitude O(m(r+log r)), which is o(alpha). Thus K~alpha/(2L). Taylor's integral bounds on -ln(1-u) give the O expansion with error O(alpha^4). V and X have explicit rational formulas, so their limits require no exchange of sums or dimensions. beta(2-beta)=1-alpha^2 tends to one. Every cancellation divides by a positive quantity. The reference forward divergence D(Q||P)~1/r and reverse K~1/(2Lr^2) both vanish; this is the same two-way-KL regime established in stage10.

The previous five positive credits have E~9rd^2, J~(1+c)d/2, posterior~rd/2, Gamma~g rd, TC~3r^2d/2, with c=18-5log2(10)>0 and g=1-(3/2)log2(3/2)>0. Dividing by O~9/(200Lr^4) makes all five tend to zero. This is retained context from stage10, not a newly checked five-credit theorem in this stage. H(G)->2 and H/I->2, so none of these ratios is an FEI disproof.

## 4. What this retires and what it leaves

Retire A040 stage10's suggested universal cumulative chi-square-times-variance payment from the same original KL account for arbitrary prescribed histories. It can overprice a completely paid inherited-reference history by an exponential factor. Upper bounds that fail payment need not represent genuine unpaid entropy. A050's exact telescope survives; no conclusion changes for a selected policy that avoids j or for a separately supplied larger influence surplus.

The first unsupported universal line is still a noncircular influence-priced ORIGINAL source and a useful stopping policy with sufficient full terminal surplus, or a necessary stronger terminal profile whose actual excess conversion can be paid from that SAME unused owner. The next test should compare the exact required profile invoice, not the generic chi-square majorant, against that owner. Analytic proof and exact finite checks are separate rungs; Lean and external independent review remain pending.
