# Padding strip as a C019 leaf-access mechanism

Outputs are Boolean signs on finite uniform cubes; all entropies are in bits. The local granularity parameter is U(f)=sum_nonempty hat f(S)^2(d_f(S)-|S|), and the already reviewed stage-1 inequality is H<=2I+2U-c Var, c=2-log2(e)>0. Here the stopping predicate is U<=I (b=1). This predicate is computed on actual physical restrictions, never on a spectral projection or a smoothed real field.

## 1. Exact padding-strip node formula for every seed

Let g be a Boolean seed on m variables. Fix a physical vertex x0, let s=g(x0), add r>=1 dummy variables, and flip the single vertex (x0,all +). Set N=m+r, p=2^{-N}, t=2p, and orient Fourier coefficients by b_T=s chi_T(x0) hat g(T). Let phi(x)=-x^2 log2(x^2), with phi(0)=0, and eta(q)=-q log2(q).

The edited function is F_r=g-2s indicator{x=x0,z=all +}. Its Fourier coefficients, after harmless signs, are b_T-t on the zero padding support and -t on every nonempty padding support. Hence the exact entropy is

    H(F_r)=sum_T phi(b_T-t)+8p(1-2^{-r})(N-1).         (1)

Querying any dummy padding coordinate yields g and F_{r-1}, with fair physical probabilities. Its influence is d=2p. Formula (1) remains valid for r-1=0 because its padding-tail term vanishes. Therefore the exact node drop is

    Delta_r=8p[1+2^{-r}(N-3)]
           +sum_T [phi(b_T-t)-phi(b_T)/2-phi(b_T-2t)/2]. (2)

No entropy or influence of a seed factor has been omitted. If L is the number of nonzero seed Fourier coefficients, each zero b_T contributes exactly 8p^2(3-N) to the last sum. Its cancellation against the padding term yields the sharper expression

    Delta_r=8p+8L p^2(N-3)
          +sum_{b_T !=0}[phi(b_T-t)-phi(b_T)/2-phi(b_T-2t)/2]. (3)

This is a coefficient formula, not a payment until the last sum is bounded.

## 2. Quantitative fixed-seed limit, and its uniformity scope

For r>=2 and m>=1, Boolean seed granularity gives |b_T|>=2^{1-m} when nonzero. Along [b_T-2t,b_T], absolute values are at least |b_T|/2>=2^{-m} and at most 5/4. Since

    phi''(x)=-(2 ln(x^2)+6)/ln2,

one has |phi''(x)|<=4m+6/ln2 there. The centered second-difference bound is

    |phi(b_T-t)-phi(b_T)/2-phi(b_T-2t)/2|
       <=(t^2/2)(4m+6/ln2).

Consequently

    |Delta_r/(2p)-4|
       <=4L p [|N-3|+m+3/(2ln2)].                   (4)

For every fixed finite seed, L and m are fixed and the right side tends to zero as r tends to infinity. This rigorously proves the lead's observed ratio ->4, and gives an explicit error bound. It does not claim a dimension-uniform limit when the seed changes with r. In particular, whenever 4L p[|N-3|+m+3/(2ln2)]<=epsilon, the node is paid at rate 4+epsilon. This is a measurable support-count/granularity condition on an actual padding split, not a support-only universal entropy theorem.

## 3. Exact universal rate five for point-defect stripping

For f_n=1-2 indicator{y=all +}, put p=2^{-n}. A queried coordinate has influence d_n=2p and child entropies H(f_{n-1}) and 0. Write D_n=H(f_n)-H(f_{n-1})/2. The n=1 case has D_1=0. For n>=2, (3) with the constant seed m=0 gives

    D_n=8p+8p^2(n-3)+phi(1-2p)-phi(1)/2-phi(1-4p)/2. (5)

For n>=3 the scalar interval lies in [1/2,1]. Here phi is concave and |phi''|<=6/ln2, so

    0<=the last second difference<=12p^2/ln2,
    D_n/d_n<=4+p[4(n-3)+6/ln2].                      (6)

For n>=4 the right-hand correction decreases with n: its numerator increases by 4 when its denominator doubles, and at n=4 the numerator exceeds 4. At n=4 it is (4+6/ln2)/16<1 because ln2>1/2. Thus D_n<5d_n for n>=4. At n=2, H(f_2)=2, H(f_1)=0, d_2=1/2, hence D_2/d_2=4. At n=3 the exact ratio is 12-(9/2)log2 3<5, certified without approximate logarithms by 3^9>2^14. Therefore

    0<=D_n<=5d_n for every n>=1; D_n/d_n ->4.          (7)

The lower inequality follows either from the physical restriction identity or from entropy concavity plus the nonnegative conditional spectral term. The result concerns these actual padding/point-defect nodes, not all Boolean nodes.

## 4. U<=I stopping trees on the two nonhereditary stress families

First consider dictator surgery g_n=x_1 f_n, n>=2. Query only coordinates other than x_1 until U<=I. Each split produces the clean dictator and g_{n-1}. Multiplication by x_1 preserves entropy and does not change the erasure or influence of a queried different coordinate, so its node drop is exactly D_n and its queried influence is d_n. Stage 1 gives

    I(g_n)=1+(2n-4)p,
    U(g_n)=n-1-(2n-4)p-4np^2.

The g_2 leaf has I=1,U=1/2 and the clean dictator has U=0. For n>=3,

    U-I=n-2-(4n-8)p-4np^2>0.

Indeed (4n-8)p<=1/2 for all n>=3 (its maximum is 1/2 at n=3,4), and 4np^2<=3/16. Thus the specified predicate stops exactly at g_2 on the edited path, or immediately on a clean branch. All leaves satisfy U<=I. The edited path reaches dimension k with probability 2^{-(n-k)}. Every visited level has expected queried-influence cost d_n, so

    queried influence=(n-2)d_n,
    E I(leaf)=1,
    E H(leaf)=2^{3-n},
    cumulative drop=H(f_n)-2^{3-n} <=5(n-2)d_n.        (8)

Next consider M_n=Maj3(z) f_n(y) on disjoint variables. Query y coordinates until U<=I. Each split gives Maj3 and M_{n-1}; the seed entropy cancels exactly. For n>=2,

    I(M_n)=3/2+2np,
    U(M_n)=3/2+n-2np.

At n=2, U=I=5/2; at n>=3, U-I=n(1-4p)>0. The n=1 leaf also satisfies U<=I (the defect factor is a pure character). The clean Maj3 leaf has U=I=3/2. Therefore for n>=2 the exact tree stops on M_2 or clean Maj3, and

    queried influence=(n-2)d_n,
    E I(leaf)=3/2+2^{2-n},
    E H(leaf)=2+2^{3-n},
    cumulative drop=H(f_n)-2^{3-n} <=5(n-2)d_n.        (9)

This explicitly handles the arbitrary-tensor-factor guard from stage 1 for this concrete fixed seed. Applying H(leaf)<=4I(leaf)-c Var(leaf) and the exact influence telescope yields H(root)<=5I(root) for both entire unbounded families. The class FEI results themselves were already known; the new result is the exact paid access tree for the previously failing U predicate. It does not assert hereditary U control.

## 5. A growing-seed guard: fixed-r node rate is not uniform

Let m be even and g_m the quadratic bent sign (-1)^(u_1u_2+...+u_{m-1}u_m), with its +1 vertex at u=0, in bit notation. Every coefficient has magnitude lambda=2^{-m/2}, L=2^m. At a fixed number r>=2 of dummy pads, define p=2^{-(m+r)}, t=2p and u=t/lambda. Then u tends to zero as m grows.

For all large m, Taylor's theorem about each signed coefficient gives the centered second difference

    -(t^2/2)phi''(signed lambda)+O(t^3/lambda),

with an absolute constant, since |phi'''(x)|=4/(ln2 |x|) and all intervening magnitudes are at least lambda/2. As phi''(lambda)=2m-6/ln2, sum (3) to get

    Delta_r/(2p)=4+2^{1-r}[m+2r-6+3/ln2]+O(2^{-r}u),
    (Delta_r/(2p))/m ->2^{1-r}.                       (10)

Thus there is no dimension-independent padding-node rate for arbitrary varying Boolean seeds at fixed r. This is a failure of the unrestricted node-payment shortcut, not FEI or the fixed-seed ratio-four theorem. For example r=2 gives asymptotic slope 1/2. The large-seed boundary reserve must be retained or the stopping rule must stop before entering such nodes. Bent seed influence is m/2, so its terminal/root influence is not negligible.

## 6. Universal padding-tree reserve, without a uniform node bound

The growing-seed obstruction does not obstruct a paid complete padding tree. Put delta=2^{-r}, d=2^{1-m-r}, and query padding coordinates until all have been exposed (or stop early at U<=I). While an edited node still has k padding bits, its reach probability is 2^{k-r}, and its queried influence is 2^{1-m-k}. Their product is exactly d. Clean branches carry no remaining padding influence. Thus a complete padding tree spends I_pad=r d, and the surviving core influence is I_core=I(F_r)-r d=E I(leaf).

For m>=1,k>=2, (4) and L<=2^m give the upper node-rate bound

    Delta_k/d_k <=4+4*2^{-k}[2m+k-3+3/(2ln2)].

For k=1, C005 and B_i<=h2(d_i)<=d_i log2(e/d_i) give

    Delta_1/d_1<=m+3/ln2.

The correction above a rate of four is nonnegative in both displayed upper bounds. Using sum_{k>=2}2^{-k}=1/2 and sum_{k>=2}k2^{-k}=3/2, its total is at most

    [4m+3/ln2]+[m-4+3/ln2]=5m-4+6/ln2
       <=(1+6/ln2)m.

Let A=1+6/ln2. The sum of every actually visited padding-node drop therefore satisfies

    Q_pad <=4 I_queried + A m d.                      (11)

This holds for the full padding tree and for early stopping at any predicate that stops each clean branch and takes only padding queries along the edited branch. The same constant reserve is allocated once, not anew at every padding level.

We now pay m d by retained core influence. A nonconstant Boolean function on an m-cube has I(g)>=m2^{1-m}: every nontrivial cut has at least m undirected boundary edges. Here is a short proof of the edge-connectivity fact. Slice the cut in the last coordinate. If both slices are nontrivial, their boundaries total at least 2(m-1)>=m for m>=2. If exactly one slice is nontrivial, it has at least m-1 internal boundary edges and at least one vertical boundary edge. If both slices are trivial, the nontrivial full cut consists of opposite constant slices, yielding 2^{m-1}>=m vertical edges. The m=1 case is immediate. Induction proves the assertion.

Flipping one physical vertex changes each core-coordinate influence by either +d or -d, so I_core>=I(g)-m d. Since m d=delta*m2^{1-m}<=delta I(g) and delta<=1/2, it follows that m d<=I_core. If g is constant, every core edge at the edited vertex becomes pivotal and I_core=m d exactly. Thus for every seed on m>=1 variables, including seeds with dummy core coordinates,

    Q_pad <=4 I_queried + A I_core.                   (12)

If an early stopping tree has all leaves in U<=bI, then I_core<=E I(leaf), and the exact influence telescope gives the explicit complete ledger

    H(F_r)<=4 I_queried +(A+2+2b) E I(leaf)
           <=(3+2b+6/ln2) I(F_r),                    (13)

for b>=0. With b=1 this constant is 5+6/ln2<14. The reserve and terminal certificate use one combined price A+2+2b on retained leaf influence; no separate ancestral reserve is charged again at descendants. A sufficient structural admission is U(g)<=bI(g) and U(F_0)<=bI(F_0): the complete padding tree then terminates in these two certified sources, and stopping sooner whenever U<=bI is also allowed. The m=0 constant-seed case is the ordinary point defect and is paid by the rate-five proof in Section 3.

This theorem pays padding access for arbitrary Boolean seeds. It does not certify the two core leaves for arbitrary seeds, since an unmodified arbitrary Boolean g remains an actual positive-probability leaf. That terminal obligation is the precise full-FEI gap.

## 7. Edited tribes: exact finite stopping test and first universal gap

For each frozen edited-tribes truth table, use padding-first restriction and then the first remaining core coordinate; stop at U<=I. Every leaf's U condition is tested by integer/rational arithmetic. Compute the actual node entropy intervals, terminal entropy and influence, and complete queried-influence telescope. A bounded finite validation is not an all-width tribes tree theorem. The exact first unsupported line for the intended universal C019 bridge is a dimension-independent payment of core access to certified leaf-U sources. Padding access is now paid in (12), with its nonreusing retained-core reserve; formula (10) rules out replacing that reserve by a fixed node rate.
