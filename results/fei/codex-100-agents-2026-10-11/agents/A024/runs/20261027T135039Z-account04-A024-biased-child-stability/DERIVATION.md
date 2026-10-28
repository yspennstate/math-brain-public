# A newly bad physical query: exact failure of the Xi odd-face conversion

All entropies are bits. Write B_i for true spectral erasure, d_i for physical influence, and q_i(f)=I(f_0 f_1)/2 for the full odd-face query cost. All physical inputs are uniform and all composition blocks below are disjoint.

## 1. A fixed inner K4-good query which becomes actually K4-bad

Let g on three bits be +1 exactly at {0,1,2}, and let g' differ from g only at vertex4, which changes from -1 to +1. Put w(s,x)=g(x) when s=0 and g'(x) when s=1. The physical query is s. Direct truth-table counting gives

    Ew=-1/8, b=(Eg-Eg')/2=-1/8, d_s(w)=1/8,
    t=Pr(w=-1)=9/16, I(w)=3/2, q_s(w)=3/8.

Let L(a,b)=e(a²)+e(b²)-e(a²+b²), e(u)=-u log2 u. Its exact Fourier fiber multiset is certified by code/check.py. In particular

    B_s(w)=4 L(1/8,1/8)+3 L(3/8,1/8)+L(5/8,1/8).

The multiplicities4,3,1 come from all eight actual Walsh fibers. They are independently checked; no hypothetical squared spectrum is substituted for a Boolean function.

For every integer N>=1, take a disjoint block u in {0,1}^3 and N parity bits z. Define h_N=-1 exactly when u belongs to {0,1,2} AND parity(z)=-1; otherwise h_N=+1. This is an actual Boolean family with

    r=Pr(h_N=-1)=3/16, I(h_N)=(3N+5)/8.

Indeed each parity bit is pivotal on a controller event of probability3/8; each controller edge is pivotal with probability1/2, and the sign of {0,1,2} has influence5/4. Independence is essential to this counting. Put F_N=1-(1-w)(1-h_N)/2. The exact activation identities give

    d_s(F_N)=3/128,
    B_s(F_N)=(3/16) B_s(w)+R_(3/16)(-1/8,-1/8),
    q_s(F_N)=(3/16)(3/8)+(1/2)(1/8)I(h_N)
            =(3N+14)/128,
    I(F_N)=(27N+81)/128.

The q formula also follows directly without the mixed-face identity: the product of the two physical s-children is 1-2*1_{x=4}*1_{h_N=-1}. Its three x-coordinate influences sum to9/64, and its h-coordinate influences sum to I(h_N)/8. Half of their sum is exactly(3N+14)/128.

Only B_s(F_N) is independent of N, not the whole spectrum. Exact rational-log certificates establish

    B_s(w)<4d_s(w)=1/2,
    1/128 < E:=B_s(F_N)-4d_s(F_N) < 1/120.          (1)

Thus this is a NEWLY bad lifted K4-query: its inner query is strictly good and its actual lifted query is strictly bad. It meets the good-inner hypothesis of the v7 paid-excess statement. Moreover

    q_s(F_N)/E > (15/16)(3N+14) -> infinity.        (2)

No dimension-independent multiple of the positive erasure excess alone can pay the full localized odd-face debit even at these newly bad queries. The same is true of the scalar R alone, since R is a fixed positive constant. This is not an FEI counterfamily. In fact F_N is F_1 with its single balanced parity input replaced by the balanced character on N bits. This maps each nonzero Fourier atom injectively to a new label with the SAME coefficient, so H(F_N)=H(F_1)<=8, and H(F_N)/I(F_N)<=1024/(27N+81) tends to zero. Separately, q_s/I(F_N)=(3N+14)/(27N+81) tends to1/9.

## 2. The SAME Xi transaction fails with both terminal reserves retained

The v7 original reserve is

    Xi(w,h)=5[r(1-r)I(w)+t(1-t)I(h)].

At this query, its exact physical drift is

    D_N=Xi(w,h_N)-(Xi(g,h_N)+Xi(g',h_N))/2
       =5[r(1-r)/8 + (1/64)I(h_N)/4]
       =5(3N+44)/2048.

Consequently

    q_s(F_N) + (Xi(g,h_N)+Xi(g',h_N))/2 - Xi(w,h_N)
       = (33N+4)/2048 >0.                         (3)

This refutes the proposed coefficient-ONE replacement of the paid positive R/erasure-excess by the FULL odd-face cost in the SAME original Xi account, retaining BOTH actual full terminal Xi reserves. Adding the SAME carried U or the SAME separately stated terminal entropy/reference/KL obligations to both candidate sides leaves(3) unchanged. No actual physical-query KL refund is asserted. Formula(3) does not refute an enlarged bank, a different selected tree, or a joint bank with an independently proved extra payer. It is a K4 obstruction, not an asserted new K10-bad witness. The old v7 positive-R theorem survives unchanged.

## 3. A valid replacement: pay the actual erasure drop directly

There is no need to inflate a paid erasure excess into q for an entropy telescope. Let T be ANY finite adaptive physical stopping tree on disjoint w,h, retaining each actual residual. For a query in w, set rate rho=r_v and inner (B,d)=(B_i(w_v),d_i(w_v)); exchange blocks for an h-query. The exact identity is B_i(F_v)=rho B+R_v, d_i(F_v)=rho d. The v7 Xi inequality gives R_v<=Xi_v-avg Xi_children. For every real K,

    sum_internal p_v [B_i(F_v)-K d_i(F_v)]
       <= sum_internal p_v rho_v [B_inner-K d_inner]
          +Xi_root-sum_terminal p_l Xi_l.         (4)

Both terminal Xi reserves are retained. The inner term is SIGNED and belongs to the actual queried inner residual, not a newly selected or reset source. For entropy use the established physical identity

    H(F_v)-avg H(F_children)=B_i(F_v)+JS_i(F_v),
    0<=JS_i(F_v)<=(2/ln2)d_i(F_v).

The exact influence telescope then yields

    H(F_root)-sum_l p_l H(F_l)
       <= (K+2/ln2)[I(F_root)-sum_l p_l I(F_l)]
          +Xi_root-sum_l p_l Xi_l
          +sum_v p_v rho_v[B_inner-K d_inner].    (5)

This is a full actual-entropy stopping ledger. All actual terminal H, I and Xi remain. Existing old debit and reference/KL bills remain independent carried liabilities; (5) grants no credit for their contraction. There is no reset, normalization conversion, or claim to have paid physical-query KL in a reference-based account.

If each actual inner query is K-good, the last sum is nonpositive. If queries follow supplied hereditary good-inner policies to constants, (5) gives H(F)<=(K+2/ln2)I(F)+Xi_root. For arbitrary Boolean children, the last signed sum remains unpaid. Equation(5) is therefore a useful exact C024 transfer, not an arbitrary-core FEI proof. It bypasses the FALSE full-q conversion rather than claiming to repair it. Corrected FEI+ still uses product INPUT variances; no output-variance numerator or variance division is introduced, and deterministic child outputs contract before normalized composition.

## 4. Remaining universal gap

The first unsupported step is an original influence-priced upper bound for the signed inherited inner ledger in(5), compatible with necessary actual queries and all old debits/full terminals. For the lead's odd-face formulation, a different funded reserve or a proved selected policy is required after(3); the coefficient-one Xi bank cannot be reused. Independent review is pending. Full FEI remains OPEN.
