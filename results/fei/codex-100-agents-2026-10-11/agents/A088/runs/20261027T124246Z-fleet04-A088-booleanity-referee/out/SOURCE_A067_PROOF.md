# Growing edit sets at one original rate 4

Rung: analytic author proof with 530,473 exact checks; independent review pending. Units are bits. The finite checks cover the cancellation and accounting identities and the smallest stated theorem boundary; the all-dimensional statement uses the argument below.

Let n=2m, m>=6, d=2^-n, A=2^-m. Let b be ANY full-rank quadratic Boolean F2 phase, including affine terms. Let E be ANY set of k distinct data vertices, 1<=k<=2^(m-2). Adjoin a dummy w. Reverse b at exactly E times {w=0}, obtaining c. Let the physical z children of G be b and c. At the original source put I_X=(I(b)+I(c))/2, D=H(G)-(H(b)+H(c))/2, S4=4I_X-(H(b)+H(c))/2, r4=S4-D. Every descendant reference is the corresponding marginal of the ORIGINAL squared Fourier law of its z child.

For EVERY finite adaptive physical restriction forest below z, let E_H be its sum, weighted by ORIGINAL reach, of entropy drop minus 4 times queried influence. Then

    r4-E_H > m/2-25/12-(2m^2+2m-1)/(4*2^m) >= 455/768 > 1/2.

The rate is chosen once at the original source. Old D, the actual removed influence J, both complete terminal CE and KL bills, and all outcomes remain. No descendant reserve is renewed. This is a growing-k supplier, not a proof of full FEI.

## 1. Actual original source

Quadratic full rank gives H(b)=n and I(b)=m. On the (n+1)-cube each undirected edge has influence weight d. At most k data edges per coordinate can have their pivotal status changed, so I(c)>=m-nkd+kd; the w influence is exactly kd. Hence I_X>=m-mkd+kd/2. Since G is Boolean on n+2 bits, H(G)<=n+2. Therefore

    r4>=2m-4mkd+2kd-2.

No source payment from another function is used.

## 2. Integer cancellation bound for the original reference

Write s_e=b(e), T(S)=d sum_(e in E) s_e chi_S(e). Then Q0(S)=(bhat(S)-T(S))^2 and Q1(S)=T(S)^2. With x=kA<=1/4,

    d(1-x)^2 <= Q0(S) <= d(1+x)^2.

After erasing any t DATA spectral labels, partition E by its input coordinates on that erased set. Orthogonality gives, on each remaining label R,

    Q1,t(R)=2^t d^2 sum_buckets (sum_(e in bucket) s_e chi_R(e))^2.

Every parenthesized sum is an integer. Consequently each POSITIVE Q1,t entry is at least 2^t d^2 and every entry is at most 2^t k^2 d^2. A further data erasure has ratio Q1,t+1/Q1,t <=2k^2 at occupied entries. Exact zeros are retained. The physical square-sum identity ensures that an actual descendant law has zero mass wherever its inherited reference is zero.

In sector W0 a data-erasure ratio is at most 1+((1+x)/(1-x))^2<=34/9<4. After w has been erased, it is at most

    1+((1+x)^2+x^2)/(1-x)^2 <=35/9<4.

Thus every W0 (or w-erased) data log price is <2. The potentially large log(2k^2) price is confined to W1, whose ACTUAL mass is small. Applying its maximum to every sector would introduce an unnecessary additional log k.

## 3. Occupation and data invoices

Prune a branch as soon as it has no surviving marked point (in particular the w=1 outcome is clean). At physical depth j below c, there are at most min(2^j,k) edited nodes. Including c's original z reach 1/2, their summed reaches L obey

    L <= (ceil(log2 k)+2)/2 <= m/2.

For k=1 use ceil(log2 k)=0; the same geometric bound applies. At a w-live node after t data restrictions, with k_v surviving marks, the ACTUAL W1 spectral mass is exactly k_v 2^t d by Parseval of the signed point mask. Its original weighted mass is k_v d/2. At any one physical depth, the surviving mark sets are disjoint; there are at most n data depths along any marked path. Therefore the summed actual W1 mass over all data queries is at most nkd/2, even when different paths choose different orders. The full inherited-reference CE decrement is expectation of log(Q_marg/Q), by the exact average-child spectral marginal identity. Subtracting 4Inf only helps. Thus

    E_Q,data < 2L + (nkd/2) log2(2k^2).

There is at least one strict data ratio whenever such a node is queried; the final theorem below also has an independent strict bound from 2kd>0, so it includes the empty forest.

## 4. All possible w queries

At W0, Q1,t/Q0,t <= k^2 d/(1-x)^2 <=1/9. Using ln2>2/3, the w log price is <1/6. The w-query nodes form an antichain of total original reach<=1/2, giving <1/12. At occupied W1 labels,

    (Q0,t+Q1,t)/Q1,t <= 1+(1+x)^2/d <=4/d,

so the log price is <=n+2. The actual W1 mass equals Inf_w at each such node, and each original marked point is counted at most once. Its total original weighted mass is <=kd/2. After subtracting the actual rate4 influence, this gives

    E_Q,w < 1/12 + (n-2)kd/2.

For no w queries the bound is still strict. Here n>=12 ensures the last coefficient is nonnegative, so replacing the actual mass by its upper bound is legitimate.

## 5. Both full terminal KL bills and clean continuation

For a pruned leaf at depth j, its inherited law averages the squared spectra over ALL 2^j restrictions of its particular queried coordinate set. Hence P_leaf<=2^j Q_leaf pointwise and KL(P_leaf||Q_leaf)<=j. The weighted sum of depths is the sum of edited-node reaches L; the original b sibling contributes KL0 before clean continuation. Thus the COMPLETE terminal KL K<=L, and

    E_H = E_Q + K
        < 3L+1/12+(nkd/2)log2(2k^2)+(n-2)kd/2.

This uses CE_root=H_root and BOTH children at every split; it is not a bound on a clipped or reset terminal functional. Full later KL can increase and is NOT bounded again by L.

Every clean exit is a restriction of a quadratic F2 phase. Such a phase has H=rank of its alternating polar matrix. A physical query with nonzero polar row has influence 1/2 and entropy rank drop 0 or 2; a zero row is a dummy or a character and has entropy drop0 and influence0 or1. Thus its actual entropy-drop-minus4Inf is nonpositive. Attach ANY adaptive clean forests, including a forest in the original b sibling: E_H cannot increase. This step is Boolean-specific, and uses discrete quadratic rank, not merely a normalized real Fourier law.

## 6. Uniform positive original remainder

Use L<=m/2, kd<=2^(-m-2), log2(2k^2)<=2m-3, and discard the positive source term 2kd. Substitution yields

    r4-E_H > m/2-25/12-(2m^2+2m-1)/(4*2^m).

At m=6 this is 455/768. The subtracted sequence decreases: if a_m=2m^2+2m-1, then 2a_m-a_(m+1)=2m^2-2m-5>0 for m>=3. The m/2 term increases. Hence the claimed bound holds for every integer m>=6. The actual removed influence remains in the telescope; legacy rate2 accounting is E2=E4+2J, not a hidden rate change.

## 7. Independent reconstruction of A088 and the unpaid step

A088's two-edit proof has the correct parity-hyperplane W1 law, <=3/2 edited occupation, unchanged original reserve, and clean quadratic payment. Its <=131/49 ratio bound follows at A<=1/16, and its 39/32 endpoint at m=4 is exact. The present proof uses a new source estimate with the sharper k-data-edge count; no repair to A088 is required. This is reconstruction, with independent finite validation pending; it does not claim external acceptance of either result.

The first unsupported universal line is an original O(I) source and affordable CLEAN exits for arbitrary nonquadratic seeds, or a source-conditioned replacement when kA is no longer small. Growing k itself no longer forces a second log k loss: isolate the rare W1 mass before summing data prices. The dependence L=O(log k) remains, and arbitrary cores cannot simply inherit the quadratic nonpositive-clean-debit theorem. Fixed Renyi hypercontractive or support-granularity envelopes still fail the point-defect test; no such envelope is used here.
