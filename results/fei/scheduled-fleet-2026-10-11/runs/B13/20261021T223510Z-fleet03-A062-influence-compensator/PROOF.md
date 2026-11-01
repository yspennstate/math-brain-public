# Raising the early-tag price does not repair the graft

All entropies are in bits. This extends the pending A062 reserve candidate by consuming A065's early-tag objection. It does not change the hidden-tag theorem.

For every real C>=6 and every positive even k, let b_k(x)=(-1)^(x0*x1+...+x[k-2]*x[k-1]), let v_k be b_k with its value at zero flipped, and let a be majority on three independent sign bits. On disjoint seed, data and fresh tag blocks put

    A=(b_k+v_k)/2, B=(b_k-v_k)/2, t=2^-k,
    M=A+wB, F=A+w*a*B.

Use for the seed its increasing-coordinate complete tree, and for M increasing adjacent data pairs followed by the tag (irrelevant coordinates may be skipped). Write Q_C for the least nonnegative reserve of the prescribed complete tree, with constant leaves zero. Then

    Q_C(a)=Q_C(M)=0.

Nevertheless the complete F tree beginning with tag, then seed, and only then data has

    Q_C(F) >= epsilon_C
       = D_w(M)+t*2-C*t*(5/2)
       > t*(k-(5/2)C).

Thus every fixed finite C>=6 fails once an even k>(5/2)C is chosen. The SAME inherited graft reserve t Q_C(a)+Q_C(M) is zero. No larger constant price repairs this early-tag extension. This statement concerns a prescribed policy, not existence of a different paid policy.

## 1. Exact stopped account and terminals

The fresh tag separates A and aB in Fourier labels. Hence H(F)=H(M)+t H(a), including the empty seed coefficient. After tag and all seed coordinates are exposed, actual terminals are b_k and v_k, each with total physical probability 1/2. Expected terminal entropy is therefore (H(b_k)+H(v_k))/2. Query influence equals t[1+I(a)]: the tag costs t and all seed bits cost t I(a), since the function on each disagreement input is a sign times w*a. Majority3 has four Fourier coefficients of magnitude 1/2, H(a)=2 and I(a)=3/2.

Consequently the exact stopped debt is epsilon_C displayed above. Summing the finite reserve inequalities to this cut retains its terminal entropy and gives Q_C(F)>=epsilon_C. Continuing the data tree cannot invalidate that lower bound. The complete whole-path entropy-minus-influence is not being used as a positive-debt test.

## 2. All-width zero profile reserve (the new step)

Let E_k denote M above. Also let O_j be the profile whose clean core is b_j independent of one dummy y and whose edited core flips only (y=0,x=0); the tag remains hidden. Set b_0=1. Increasing data-pair order has just one exceptional branch at every query:

* E_k, first data bit zero: O_(k-2). First data bit one: the two cores coincide with a character times b_(k-2), whose complete reserve is zero at C>=4.
* O_j, dummy zero: E_j. Dummy one: clean b_j, also zero reserve.

The unedited character-times-bent branches are paid directly: revealing a first pair member drops entropy by 2 with influence 1/2, while the mate becomes a dictator of entropy 0; all further pairs repeat this. A dictator query has entropy drop zero. Thus price 4 suffices. The subsequent proof assumes C>=6 throughout.

For even j>=0, put N=2^j, r=2^(j/2), n_+=(N+r)/2, n_-=(N-r)/2. E_j has coefficient numerators r-1 (n_+ times), -r-1 (n_- times), and 1 (N times), all divided by N. O_j has numerators 2r-1 (n_+ times), -2r-1 (n_- times), and 1 (3N times), all divided by 2N. These formulas include j=0 with zero terms omitted; E_0=w, H(E_0)=0, while O_0 is AND/OR2 up to signs, H(O_0)=2. Its dummy influence is 1/2, so Q_C(O_0)=0 at C>=4.

The physical influences at the exceptional queries are

    d_Ek=1/2+2^-k,    d_Oj=2^(-j-1).

They follow either by direct disagreement counts or by Fourier mass containing the queried coordinate.

For even k>=4 the tag-present E_k sector has mass delta=2^-k. BOTH normalized sectors have support at most 2^k, so

    H(E_k) <= k+h2(delta) <= k+delta*(k+log2(e)).

Here h2(delta)<=delta*log2(1/delta)+delta*log2(e). The bound log2(e)<3/2 follows from ln(2)>2/3 (the first positive atanh-series term). The dyadic sequence (k+3/2)/2^k decreases for k>=4. Consequently H(E_4)<4+11/32 and H(E_k)<k+15/128 for even k>=6. Counting the tag sector's internal entropy is essential.

For even j>=4 the largest squared O_j coefficient is at most 81/(64*2^j). Therefore

    H(O_j)>=-log2(max p)>=j-log2(81/64)>j-1/2,

because 81^2<2*64^2. At j=2 the explicit spectrum gives

    H(O_2)=6-(54 log2(3)+50 log2(5))/64 > 2,

using log2(3)<8/5 and log2(5)<7/3, certified by 3^5<2^8 and 5^3<2^7.

For an O_j dummy query, the one-bit conditional-entropy/channel bound gives

    D_Oj <= h2(d)+2*log2(e)*d
           <= d[log2(1/d)+3*log2(e)]
           < 2^(-j-1)*(j+11/2) <= 15/16       (even j>=2).

The last sequence decreases as j increases by two; its first value is 15/16. The channel bound is the baseline JS<=2 log2(e) min(d,1-d), and B<=h2(d). No new universal erasure bound is assumed.

Now induct on even k. If Q_C(E_j)=0, then Q_C(O_j)<=15/16 for j>=2, since its only nonzero candidate child reserve is Q_C(E_j)/2. At E_(j+2) for j>=4, its other child has reserve zero, so

    D_E < 2+15/128+1/4 = 303/128,
    D_E-C*d_E+Q_C(O_j)/2 <303/128-3+15/32=-21/128<0.

Thus Q_C(E_(j+2))=0. E_0 and O_0 were handled explicitly. E_2 has H(E_2)<=3, D_E2=H(E_2)-1<=2, d_E2=3/4 and both child reserves zero, so it is paid at C>=6. Finally, at E_4 use H(O_2)>2 and H(E_4)<4+11/32; adding its half-child reserve gives less than 2+11/32+15/32=45/16<3<=C*d_E4. This closes every base case and proves zero profile reserve for every even k without a numerical extrapolation or dropping an unmatched mate.

For majority3, its first query has entropy decrement zero and influence 1/2; each child is AND/OR2 with H=2 and increasing-coordinate reserve zero at C>=4. Hence its reserve is zero as asserted.

## 3. Explicit all-price divergence

For the tag query in E_k, each Fourier packet has amplitudes alpha=(+/-r-1)/N and beta=1/N. Let q=alpha^2+beta^2. The retained logarithmic charge is

    lambda=sum beta^2 log2(q/beta^2).

For k>=2, r>=2 and q/beta^2 >=(r-1)^2+1>r^2/4=2^(k-2). There are N such packets. Thus lambda>t(k-2). The exact singleton identity and nonnegativity imply D_w(M)=B+JS>=B>=lambda. Substitution gives epsilon_C>t[k-(5/2)C]. Every denominator here is positive. The zero empty coefficients at the k=0 base are excluded before taking logarithms, and k=0 is not used in this lower bound.

Equivalently, the entropy cost before the data terminals divided by its actual queried influence exceeds 2k/5. This is a ratio of stopped entropy cost to PREFIX influence, not H(F)/I(F).

For any positive integer L take L independent modules and expose every tag and seed before stopping. Product entropy, terminal entropy and queried influence add exactly, so the debt exceeds L*2^-k*(k-(5/2)C). In particular L=2^k gives a debt exceeding k-(5/2)C along the even widths with fixed C. Root influence also grows; this is not a Boolean unbounded-H/I family.

## 4. Scope and first unpaid step

The result independently reconstructs A065's exact terminal account and extends its finite-price witness to every C>=6 and every sufficiently large even k. It leaves A062's delayed-tag hypothesis intact. No randomized stopping or unbounded-depth passage is needed: each k,L gives a finite physical tree; every sum has finitely many terms. Independent policy randomization is a finite-dimensional conditional averaging of the already proved hidden-tag interface, not a way around this fixed-policy counterexample.

The first unpaid universal step is a selected reveal policy or an additional genuinely unused ancestor source that pays the signed early-tag collision and both continuations. Raising a fixed price on the prefix alone is excluded. A087/A094 should independently reconstruct the two exceptional-state entropy bounds and their base cases; A064 should preserve the tag priority when carrying the same zero initial bank.
