# Rare selector certificates and unit-atom endpoint normalization

Natural corrected entropy is E=(ln2)Hplus; D=I-Var is spectral influence minus variance. All physical inputs are independent. Let h(t)=t^2ln(1/t^2), h(0)=0. The positive mean-only pair multiplier is kappa(t)=2t ln(1/t)/(1-t), 0<t<1. No positive residual is charged at mean zero or absolute mean >=1. P denotes the actual product Fourier squared spectrum.

## 1. Independently reconstructed source interface

Source A045-SHARP-MEAN-REFUND-PAIR-CONGESTION-NOGO@1, statement hash b6f5938ce1562003dfdfc4ecc4e1dbe8f30f6c9875ff965bf34bd7c1a986af9f. For an integer mixed profile Z, t=|EZ|<1 implies Var Z>=t(1-t), since Z^2>=|Z|. Hence h(EZ)<=kappa(t)Var Z. Actual AND3, selecting the two data coordinates and taking controller probability t, has Z=1_controller and attains equality. Thus no smaller nonnegative mean-only universal multiplier is available. This reconstructs the source's sharp local assertion without a source helper.

For a physical pair S, its profile is the second alternating Boolean sum divided by 2. Fair pair integration gives m_S=2 fhat(S), and Parseval gives Var(Z_S)/4=sum_{T strictly containing S}P(T). These are physical cofactor moments of the same Boolean function. They do not justify treating different pairs as independent owners.

For integer r>=1 set n=16r^2, M=n/2. On n fair data bits let N count ones, chi=(-1)^N, and

    g(N)=+1 for N<=M-r or N>=M+r, and -1 otherwise.

Let b=Pr[Bin(n-1,1/2)=M-r]. The two one-bit derivative boundaries have probabilities b and opposite signs. Conditioning a second bit on either boundary gives the exact common pair coefficient

    a=ghat({i,j})=2(2r-1)b/(n-1)>0.                  (1)

Here is an independent reconstruction of the dimension-uniform bounds used by A045. A central maximum q0=Pr[Bin(n-1,1/2)=M-1] is at least 1/(12r): Chebyshev puts at least 3/4 of the mass within distance 4r of the mean, containing at most 8r+1 integer values. Furthermore

    b/q0=product_{j=1}^{r-1}(M-j)/(M+j)>=3/4,

because each factor is at least 1-1/(4r), and the product is at least 1-(r-1)/(4r). Thus b>=1/(16r) and a>=1/[8(n-1)]. For the upper bound, with L=sum_i(2X_i-1), sum_{i<j}chi_{ij}=(L^2-n)/2. Therefore

    |a|<=E|L^2-n|/[n(n-1)]<=2/(n-1).                (2)

The source's fair-selector result follows from the rare-selector calculation below at epsilon=1/2, including the exact constants n ln((n-1)/2)/16 and ln((n-1)/2)/24. Its H/I control is also recovered below. Verdict HOLDS for the complete stated obstruction/sharp-admission claim; the source's separate A044 review is excluded. No repair is supplied.

## 2. Actual rare-selector family and exact pair ownership

For independent C with P(C=1)=epsilon, 0<epsilon<=1/2, define F=chi if C=0 and F=g if C=1. Let mu=Eg and t=E[g chi]. Every data pair has integer-profile mean

    m=2epsilon a,  0<m<1.                             (3)

Selector-containing pairs have zero mean: both g and parity have zero singleton means by complement symmetry. For a selected data pair let K~Bin(n-2,1/2) and

    Z_g(K)=[g(K+2)-2g(K+1)+g(K)]/2.

The parity profile is 2(-1)^K, of mean zero and second moment 4. Since selection is physical and independent, the data-pair profile variance is exactly

    V=4(1-epsilon)+epsilon E Z_g^2-4epsilon^2 a^2.    (4)

Thus the COMPLETE nonnegative mean-refunded pair bill and the exact signed pair residual are respectively

    L_kappa=binom(n,2) kappa(m) V/4,
    Q_pair=sum_pairs[E_S-ln4 P(S)]=binom(n,2)h(m)/4.  (5)

No selector pair contributes to either expression, because its mean is zero. In particular

    L_kappa/Q_pair=V/[m(1-m)].                        (6)

The loss from replacing the exact residual by a variance payment is visible before any whole-set summation: V tends to 4 while m tends to zero.

The two actual full-data Fourier packets (without and with C) have combined squared mass

    [(1-epsilon)+epsilon t]^2
      +epsilon(1-epsilon)(t-1)^2
      =(1-epsilon)+epsilon t^2 >=1-epsilon.           (7)

Both strictly contain every data pair. Hence V/4>=1-epsilon. This is actual shared Fourier packet ownership, not a constructed spectral marginal.

## 3. Uniform rare-selector obstruction and exact-residual comparison

By (1)-(3), epsilon/[4(n-1)]<=m<=4epsilon/(n-1). Consequently

    kappa(m)>=2m ln(1/m)
       >=epsilon/[2(n-1)] ln((n-1)/(4epsilon)).

Equations (5),(7) imply

    L_kappa>=n epsilon(1-epsilon)/4 ln((n-1)/(4epsilon)).   (8)

Physical data influence is (1-epsilon)n+epsilon I(g), and selector influence is 2epsilon(1-epsilon)(1-t). Since I(g)<=n and |t|<=1,

    (1-epsilon)n<=I(F)<=n+1,
    (1-epsilon)n-1<=D(F)<=n+1.

Thus, since n>=16 and epsilon<=1/2,

    L_kappa/D >=epsilon(1-epsilon)/6 ln((n-1)/(4epsilon))
               >=epsilon/12 ln((n-1)/(4epsilon)).     (9)

Rarity alone does not control this ledger. For the explicit diagonal

    epsilon=1/k, r=2^(k^2), n=16*2^(2k^2), k>=2,

equation (9) gives L_kappa/D>=k ln2/6, tending to infinity while epsilon tends to zero. This extension changes the physical endpoint law of the already identified obstruction rather than proposing another scalar multiplier.

In contrast the exact residual is small. Because m<=4epsilon/(n-1)<=2/15 and h is increasing on [0,2/15], (5) gives

    Q_pair<=4n epsilon^2/(n-1) ln((n-1)/(4epsilon)).

The lower deficit bound is D>=n/2-1>=7n/16, whence

    0<=Q_pair/D<=10epsilon^2/n ln((n-1)/(4epsilon)).    (10)

On the same explicit diagonal this tends to zero (indeed O(1/n)). There is no contradiction: L_kappa is an unnecessarily large funding upper bound for the actual residual. Ordinary Fourier entropy obeys H(F)<=n+1, while I(F)>=n/2, so H/I<=2+2/n. Also corrected entropy is no larger than ordinary entropy since every physical variance factor is <=1. This is a rigorous obstruction to a bookkeeping mechanism, not an FEI counterexample.

## 4. General parity unit-atom endpoint expansion

Fix n>=1 fair data bits, N0 the complete data set, chi their parity character, and ANY Boolean g on that same cube. Let mu=ghat(empty), t=ghat(N0), and b_T=ghat(T)-1_{T=N0}. Define

    J=sum_{T subset N0} b_T^2 ln(4/b_T^2),
    Z=1-t^2-mu^2=sum_{nonempty T!=N0}ghat(T)^2,
    B=sum_{nonempty T!=N0}h(ghat(T))-J-3(1-t)^2.

Zero terms are interpreted continuously; J includes the empty DATA coefficient because adjoining the selector makes that atom nonempty. In the same rare selector F, the nonselector coefficients are 1+epsilon(t-1) at N0 and epsilon ghat(T) elsewhere. The selector-containing coefficients are sqrt(epsilon(1-epsilon))b_T. Its exact natural corrected entropy is therefore

    E=h(1+epsilon(t-1))
      +sum_{nonempty T!=N0}h(epsilon ghat(T))
      +epsilon(1-epsilon)J.                           (11)

Taylor expansion at the unit coefficient gives

    E=epsilon[2(1-t)+J]+2Z epsilon^2 ln(1/epsilon)
         +B epsilon^2+O_g,n(epsilon^3).               (12)

The coefficient Z EXCLUDES mu^2: the empty nonselector spectral atom is excluded by corrected entropy. Omitting this subtraction would, for example, incorrectly predict a logarithmic term for a constant g. No fixed-n remainder from (12) is used on the growing diagonal of section3, whose bounds were uniform and exact.

The exact deficit is

    D=n-1+epsilon[I(g)-n+2-2t]
           -epsilon^2[2-2t-mu^2].                    (13)

This follows either from the spectrum or from data influence (1-epsilon)n+epsilon I(g), selector influence 2epsilon(1-epsilon)(1-t), and Var F=1-epsilon^2 mu^2. At epsilon=0 there is a unit spectral atom; if n>=2 its deficit is n-1, not zero, and corrected entropy tends to zero. At n=1 the unit atom is a literal with zero deficit. The four possible branches g give: g=chi leaves E=D=0 identically; g=-chi has E/D->1 in natural units; g=+1 or -1 has E/D->2+4ln2 (bit ratio 4+2/ln2). These exhaust the zero-deficit unit-atom special case. There is no first-order epsilon ln(1/epsilon) term in corrected entropy.

## 5. Universal frontier

The A045 obstruction already ruled out all-pairs mean-only variance funding at a fair selector. The present result proves that arbitrarily rare selectors do not rescue it and quantifies the exact-residual/variance-price gap at a parity unit-atom endpoint. It neither refutes A044's valid local profile lemma nor supplies a complete conditional reference. The first unsupported universal line remains a selected or merged packet reference that pays exact signed residuals, full higher-degree/singleton/empty and terminal costs from one conserved deficit account. Any use of mean-only all-pairs funding must confront (8)-(10), even in a vanishing-bias regime.
