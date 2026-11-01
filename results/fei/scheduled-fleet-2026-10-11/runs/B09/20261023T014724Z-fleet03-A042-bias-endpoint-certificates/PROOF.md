# A scale-aware approximation with deficit-controlled error

This repairs the all-profile approximation mechanism. It does not pay the resulting whole-set cost or prove FEI. All logarithms are natural, except explicit powers of two.

Let f:{0,1}^n->{-1,1} have any finite dimension and any independent interior product law. Set v_i=4p_i(1-p_i), v_S=product_{i in S}v_i, c_S=fhat(S)/sqrt(v_S), P(S)=v_S c_S^2. Use the actual physical coefficients throughout. Let

    E = sum_{S nonempty, P(S)>0} P(S) ln(v_S/P(S)),
    Delta = sum_{S nonempty} (|S|-1)P(S),
    R = sum_{|S|>=3} (|S|-2)P(S).

Thus E=(ln2)Hplus and Delta=I-Var. The normalized physical mixed derivative is an alternating average of Boolean values, so |c_S|<=1 for every nonempty S. Zero coefficients contribute zero.

For each t=|c_S|>0 choose the UNIQUE integer j>=0 such that 1/2<u=2^j t<=1. Set z=(1-u)/(1+u), so 0<=z<1/3. For N>=0 define

    L_N(z)=2 sum_{k=0}^{N-1} z^(2k+1)/(2k+1),
    E_N=2 sum_{S nonempty,P(S)>0} P(S)[j_S ln2+L_N(z_S)].

The sum for N=0 is empty. Dyadic boundary points choose u=1. Exact power extraction is kept as j ln2; it is not itself truncated.

For EVERY integer N>=0, with A_N=(2N+1)9^N,

    0 <= E-E_N <= (11 Delta-7R)/(2 A_N)
                  <= 11 Delta/(2 A_N).                 (1)

Also E_N<=E_(N+1)<=E. This is a dimension-independent additive approximation in the original deficit. It includes constants and biased signed literals where Delta=0: both E and E_N are exactly zero. The number of dyadic coefficient cells is unbounded; no globally fixed polynomial degree/cell count or computational complexity bound is claimed. On rational product laws the coefficients P,c,u,z are rational, so E_N is an explicit rational number plus a rational multiple of ln2.

## 1. The logarithm tail is charged to squared mass

The positive atanh series gives ln(1/u)=2sum_{k>=0}z^(2k+1)/(2k+1). Its omitted tail satisfies

    0 <= ln(1/u)-L_N(z)
       <= 2z^(2N+1)/[(2N+1)(1-z^2)].                 (2)

This follows by bounding every denominator below by 2N+1 and summing a geometric series. It is valid at z=0 by equality; convergence is uniform on [0,1/3]. The exact j ln2 cancels in E-E_N. A single coefficient's error is therefore at most

    4P(S)z^(2N+1)/[(2N+1)(1-z^2)]
       <= epsilon_N P(S), epsilon_N=3/(2 A_N).         (3)

For |S|>=2 these errors sum to at most epsilon_N(Delta-R), since sum_{|S|>=2}P(S)=Delta-R. This charges each actual spectral atom once. It does not sum a strict-superset variance once for every submask.

## 2. The near-literal singleton is not charged a fixed mass error

For coordinate i let D_i=(f(X_i=1)-f(X_i=0))/2, d_i=E D_i^2, t_i=|E D_i|=|c_i|. Booleanity gives D_i in {-1,0,1}, hence d_i>=t_i, and V_i=Var(D_i)=d_i-t_i^2>=t_i(1-t_i). Parseval gives the SAME physical reserve

    sum_i v_i V_i=sum_{|S|>=2}|S|P(S)=2Delta-R.         (4)

If 0<t_i<=1/2, then P({i})=v_i t_i^2<=v_i V_i. Equation(3) bounds its error by epsilon_N v_i V_i.

If 1/2<t_i<1, then j_i=0, u_i=t_i and z_i=(1-t_i)/(1+t_i). Dividing the first bound in (3) by v_i t_i(1-t_i) and using 1-z_i^2=4t_i/(1+t_i)^2 gives

    error/[v_i t_i(1-t_i)]
       <= (1+t_i)z_i^(2N)/(2N+1)
       <= beta_N, beta_N=2/A_N.                      (5)

Since beta_N>=epsilon_N and V_i>=t_i(1-t_i), every singleton error is <=beta_N v_i V_i. At t_i=0 or1 it is zero directly; no zero denominator is cancelled. Thus singleton errors sum to at most beta_N(2Delta-R). Adding the high-degree error in (3) proves (1): beta_N(2Delta-R)+epsilon_N(Delta-R)=(11Delta-7R)/(2A_N).

Every sum over Fourier sets is finite. The only infinite series has a uniform geometric majorant. No exchange with a growing-dimensional limit is used. At deterministic input endpoints contract those inputs first; applying (1) at every remaining interior law proves a relative-error bound along arbitrary approach rates, without dividing by Delta. When Delta>0 the ratio error is bounded by the displayed constant even as Delta tends to zero.

## 3. Consequences and the precise change of mechanism

For example N=1,2,3 give error <=11Delta/54, 11Delta/810, 11Delta/10206. These are different truncation orders, not revisions of one reported constant. The universal corrected FEI+ statement E<=C Delta is equivalent, up to this explicit additive constant, to E_N<=C_N Delta for any one fixed N. In particular the N=0 statement asks to pay the ACTUAL dyadic-scale cost 2ln2 sum P(S)j_S. This is a localization of the unpaid logarithm, not a reduction to an easier class.

The A043 singleton hierarchy remains valid; this approximation is different. It extracts an unbounded dyadic scale and uses rational functions on bounded scale cells. It is not a fixed-degree global polynomial in the original cofactor mean. Thus it does not contradict A043's sharp 4/(m+1) error or A044's exponential fixed-order all-profile obstruction. Its tail is proportional to P(S), rather than the first power of a small mean times a profile-dependent scaling. The singleton reserve in (4) is used ONCE at its original degree multiplicity.

On A044's actual bent tensor f_r=(-1)^(sum_{j=1}^r x_(2j-1)x_(2j)) with fair inputs, all |c_S|=2^-r. Therefore j_S=r, u_S=1, z_S=0 and E_N=E for EVERY N, including N=0. Precisely,

    H_nats(full spectrum)=2r ln2,
    E=2r ln2(1-4^-r),
    Delta=r-1+4^-r.

The empty-atom entropy is 2r ln2*4^-r. It is omitted from corrected E by definition and retained in the full entropy above. Thus the former exponential truncation-error witness has zero error here while its complete Fourier law and all empty/nonempty atoms remain unchanged. No selected spectral fragment is declared Boolean and no new normalized reference Q is introduced.

More generally this is exact at N=0 whenever every occupied nonempty |c_S| is an inverse power of two; it makes no statement that all product-biased Boolean spectra have this property.

## 4. Failure tests and first unsupported line

The dyadic scale term cannot be dropped. On the same bent tensor, L_N(z_S)=0 for every nonempty S, but E/Delta tends to 2ln2. On a biased near-literal, a uniform per-singleton error epsilon_N P({i}) would not be O(Delta); (5) is the necessary endpoint repair. Boolean singleton admission is also necessary for the relative-deficit conclusion: the real-valued fair one-bit f(x)=x-1/2 has Delta=0 and a nonzero logarithm remainder whenever |c_1| is not an exact dyadic point after a suitable non-dyadic rescaling. Concretely f(x)=(2/3)(2x-1) has t=2/3, Delta=0, z=1/5 and E-E_N>0 for every finite N. Its derivative has d=4/9<t=2/3, violating the hypothesis used in (4)-(5).

Cell boundaries may create jumps in the finite approximant, but (1) holds on both sides and at the specified boundary. No continuity of E_N is asserted. Rational evaluation must first test c=0 exactly and compare powers of two exactly. Uncertain real-coefficient input intervals require separate cell/zero certificates; this is not an automatic real-oracle algorithm.

The first unsupported universal line is to bound E_N, or its exact dyadic-scale whole-set charge, by a dimension-independent multiple of the SAME unused deficit through a complete conditional reference, including ordinary KL, mass normalizer, off-support atoms and both terminal laws. Inequality(1) removes approximation error as a dimension-dependent obstacle. It neither pays E_N nor changes the full-FEI OPEN status.
