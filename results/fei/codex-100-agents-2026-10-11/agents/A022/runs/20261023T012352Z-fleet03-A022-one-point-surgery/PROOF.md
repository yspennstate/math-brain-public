# Long block-first histories preserve the original reference reserve

Full FEI is OPEN. Entropies are in bits; no novelty claim is made.

## 1. Family, references and original ownership

Let g be -1 exactly at000 on three bits, b=g tensor t, t>=2, k=3t, delta=8^{-t}. At any vertex v, activate a point flip by an arbitrary independent control indicator A:

    F(x,z)=b(x)(1-2*1_{x=v}A(z)), alpha=EA, a=1-2A, L=delta H(a).

The ORIGINAL seed reference is Q=P_b, a product of q=(9/16,1/16,...,1/16). The ORIGINAL controller reference is R(empty)=1-V, R(T)=delta ahat(T)^2 for nonempty T, V=4delta alpha(1-alpha). Pass this SAME R to every descendant. Zero R rows have zero mass in every physical data child by the point-surgery coefficient formula, and are omitted without division. Old bookings satisfy0<=U<=t/64 throughout.

A021-NONFLAT-INHERITED-REFERENCE-DATA-QUERY@1, run20261023T001013Z, pays the first query and preserves at least11t/64. Its exact formulas are reconstructed here. The smaller13t/576 guarantee below covers a substantially longer history, not a revision of that first-query number.

Fix an order of the t blocks and an order of each block's three coordinates. Complete each block before entering the next. At depth d=3r+j, j=0,1,2, retain ALL2^d physical children with original reaches2^{-d}. The paid domain is r<=floor(t/2), equivalently d<=3floor(t/2)+2. Partial entry into the next block is allowed. No control bit is exposed, and no claim for unequal-depth adaptive stopping cuts is made.

## 2. Complete positive terminal references

Untouched blocks retain ORIGINAL q. Completed blocks have no frequency label and reference1. In a current partial block use:

* After one query: uniform4 if that physical bit is0, otherwise(13/16,1/16,1/16,1/16).
* After two queries: probability15/16 on the UNEDITED one-bit seed's Fourier label and1/16 on the other label. The favored label is1 when both fixed bits are0 (a character), and0 otherwise (a constant).

Tensor these references with untouched q and SAME R. They are normalized and strictly positive on data labels. Signs from completed blocks do not change squared spectra. Let C_d be average COMPLETE terminal cross-entropy, H_d average terminal Fourier entropy, D_d=C_d-H_d average complete terminal KL, and I_d average remaining DATA influence. Keep individual terminal CE/KL expressions as well as their sums. The actual remaining bank is

    B_d=4I_d+L-C_d-U.                                      (1)

It is never restored when a block changes.

## 3. Exact costs, including the effect of earlier exposed blocks

Put l=log2(3), p=log2(13), q15=log2(15), h=4-(9/8)l, beta=(9/8)l-1, c1=3-p/2, c2=4-q15. Local J(000)=-7l/4 and J(u)=5l/4 otherwise; the signed neighbor sum s(u) is-3 at000,1 at weight1,3 otherwise. Thus

    X(u)=4J(u)-8s(u)<=24-7l<118/9, beta>3/4.              (2)

These use14/9<l<8/5, certified by3^9>2^14 and3^5<2^8. Nonzero-vertex alternatives are smaller than the000 cost.

At d=3r let n=t-r and T_d be the n untouched blocks. Exact physical and Fourier formulas give

    C_{3r}=H(R)+nh+4delta alpha sum_{b in T_d}J(v_b).       (3)

At j=1,2 there are n-1 intact blocks and one partial block. If i is the first queried bit of that partial block, set w1=0 for v_i=0, and w1=3p for v_i=1. Then

    C_{3r+1}=H(R)+(n-1)h+c1
                 +4delta alpha sum_intact J(v_b)+delta alpha w1;
    C_{3r+2}=H(R)+(n-1)h+c2
                 +4delta alpha sum_intact J(v_b)+2delta alpha q15. (4)

All untouched-block costs and the R cost are invariant IN EXPECTATION under the physical data queries, by Parseval. Exactly one terminal cylinder contains the edit. Its original reach times its conditional point density is always ORIGINAL delta. At j=1, an edit in outcome1 contributes three nonempty local masses; their code-length difference is p, giving3delta alpha p. The outcome0 reference is uniform. At j=2 the opposite one-bit Fourier label has added mass twice the conditional point density times alpha; the code-length difference is q15, giving2delta alpha q15 after reach. This derives(3),(4) without Fourier independence or a conditional reset.

Let sigma_i=g(v_block(i))g(v_block(i) xor e_i), with e_i interpreted in that block. Physical edges give

    I_d=(3t-d)/4+2delta alpha sum_{i unqueried}sigma_i.      (5)

Every coefficient uses ORIGINAL delta.

## 4. Second query in the ALREADY converted block

If sigma is the second coordinate's neighbor sign, the reference-capacity loss is exactly

    ell2=4*actual_query_mass-(C_{3r+1}-C_{3r+2})
        =2+p/2-q15+delta alpha(8sigma-w1+2q15).             (6)

The constant is negative since15^2>16*13. The perturbation coefficient is<16, since sigma<=1,w1>=0 and q15<4. Therefore ell2<16delta<=1/4 for all t>=2. For t>=3 it is negative:15^32>2^65*13^16 certifies2+p/2-q15<-1/32, while16delta<=1/32. A021's actual B_1>=11t/64 consequently gives B_2>=3t/64. This is reference-capacity payment, not an all-coordinate entropy-decrement bound.

## 5. Completion and long-history invariant

The SAME original control cost obeys

    H(R)-L=kV+phi(1-V)-delta phi((1-2alpha)^2)
           <=delta alpha(12t+6),                          (7)

using phi(1-V)<=log2(e)V, log2(e)<3/2 and V<=4delta alpha. The negative phi term is dropped only in this upper estimate. No controller entropy is charged again.

At complete-block depths, equations(1)--(3),(5),(7), U<=t/64 and delta<=1/64 give

    B_{3r}>=(3/4)n-delta[12t+6+(118/9)n]-t/64
           >=(314n-117t-54)/576>=13t/576.                 (8)

The last step uses n>=t/2 and40t-54>=13t for t>=2.

The unedited partial-block banks are b1=2-c1=-1+p/2>5/6 and b2=1-c2=q15-3>5/6. The inequalities follow from13^3>2^11 and15^6>2^23. Their signed edit costs satisfy

    Y1=w1-8 sum_two_remaining sigma_i<=16;
    Y2=2q15-8sigma_last<16.                               (9)

For Y1, v_i=0 has maximum16 at000; v_i=1 has both remaining signs+1 and Y1=3p-16<0 because13<16. Consequently

    B_{3r+j}>=(3/4)(n-1)+5/6
               -delta[12t+6+(118/9)(n-1)+16]-t/64
             >=(314n-117t-32)/576>=13t/576, j=1,2.        (10)

Here n>=t/2 and27t>=32. Thus EVERY admitted prefix retains13t/576 of the ORIGINAL account after old U. This exceeds the original t/64 by t/144. It pays completion of already converted blocks and continued entry into later blocks without new source admission. It is a uniform bound through3floor(t/2)+2 queries; the earlier first-query11t/64 estimate stays valid.

## 6. Both terminal KLs and signed history remain explicit

At each depth the actual entropy decrement equals complete-reference drop plus D_{d+1}-D_d. Also B_{d+1}=B_d-[4*query_mass-reference_drop]. Let E_d be the accumulated SIGNED physical query account sum reach*(4Inf-DeltaH). Then

    B_d+D_d+E_d=B_0+D_0.                                 (11)

This identity keeps every terminal KL, both descendants at each query, old U and full L. It never asserts every entropy decrement is<=4Inf. Equations(3)--(5) compute actual remaining capacity after earlier exposures, not a newly granted child bank.

## 7. Final reference-only collapse is genuinely obstructed

If ALL data coordinates are exposed, H_final=L exactly: only vertex v retains the controller a; other vertices give constant leaves. The retained ORIGINAL R gives C_final=H(R), hence

    B_final=L-H(R)-U, D_final=H(R)-L.                     (12)

For the one-bit literal A(z)=z, a is a Fourier character, L=0 and R=(1-delta,delta). Thus B_final=-h2(delta)-U<0, an actual Boolean obstruction to unconditional nonnegative FINAL CE-bank extension, already at t=2. It does not refute FEI: final leaf entropies are0, and their positive KL cancels the negative reference-only balance before the old booking is redeemed through(11). Dropping that refund or resetting R would give the false stronger statement.

## First unsupported universal line

The theorem covers the prescribed block-first data histories, not arbitrary nonflat source admission, arbitrary unequal-depth stopping cuts or a controller-reference conversion after a physical controller query. Next expose one controller bit after a paid data prefix while retaining ORIGINAL R's conversion cost, the actual remaining13t/576, old U, full source-controller terminals and both descendant KLs. The final-collapse witness shows why a nonnegative CE-only account cannot serve as the universal invariant.
