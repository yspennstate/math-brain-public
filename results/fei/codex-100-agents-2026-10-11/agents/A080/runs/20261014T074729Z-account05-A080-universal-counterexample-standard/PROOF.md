# Exact entropy localization by tensoring before activation

All cubes are finite and uniform, all functions have sign values, and entropy is in bits. Define R(g)=H(g)/I(g) for nonconstant g. Write p(g) for its minority probability. No FEI premise is used below.

## 1. Complete actual spectrum and physical edges

Fix any nonconstant g on n bits. Let G be the product of t copies of g on disjoint supports. Integer t is positive. Its Fourier coefficients are products, so H(G)=t H(g), I(G)=t I(g), and its mean is m=m(g)^t. Put p=(1-m)/2; this need not be the minority of G, but lies strictly between zero and one.

On k fresh selector bits let A be the indicator of the all-zero vertex, a=2^-k. Define the actual sign function F=1+A(G-1): it equals G on the activating selector vertex and +1 elsewhere. With selector Fourier set T and data Fourier set S, every Fourier coefficient is

* 1-2ap for T=S=empty;
* -2ap for S=empty, T nonempty;
* a Ghat(S) for S nonempty, every T.

The signs assume the all-zero vertex is sign +1 in every selector coordinate; another point gives harmless selector character signs. These formulas retain the constant atom. Data-coordinate influences are a times their G influences. Every selector-coordinate influence is 2ap: both selector endpoints must have the remaining k-1 selectors zero and G=-1. Consequently

    P(F=-1)=ap,  I(F)=a[t I(g)+2kp].                 (1)

Let ell(x)=x log2(1/x), ell(0)=0. Summing every squared atom yields the exact entropy identity

    H(F)=a[t H(g)-ell(m^2)+2k(1-m^2)]
          +ell((1-2ap)^2)+(2^k-1)ell(4a^2 p^2).    (2)

Every ell term is nonnegative; ell(m^2)<=1/(e ln2)<1. Hence

    H(F)>=a[t H(g)-1].                              (3)

This is a lower bound with the full seed entropy present. It requires no assumption on G's conditional nonempty spectrum or singleton coefficients.

## 2. A finite schedule with vanishing bias and influence

Take integers k tending to infinity with k>=max(1,I(g)), and set t=ceil(k^2/I(g)). Then

    k^2<=t I(g)<=k^2+k,
    0<p(F)<=2^-k,
    0<I(F)<=2^-k(k^2+3k).                            (4)

The last inequality uses 2kp<=2k for every orientation; it therefore needs no bias asymptotics or complementation. Each F has exactly tn+k finite physical bits. Since g is nonconstant, |m(g)|<1 and eventually p<=1/2+o(1); however (4) already proves both smallness requirements. There is no infinite cube output.

From (1),(3), once t H(g)-1>=0,

    R(F)>= [R(g)-1/(t I(g))]/[1+2kp/(t I(g))]
          >=R(g)/(1+2/k)-1/k^2.                     (5)

If H(g)=0, R(g)=0 and the same final bound follows simply from H(F)>=0. Thus (5) holds for every nonconstant seed and every eligible k. In particular liminf R(F)>=R(g).

For any fixed delta,eta>0 define C(delta,eta) as the supremum of H/I over actual nonconstant functions with p_min<=delta and I<=eta. Every sufficiently large member of (4) belongs to this domain. Since this construction applies to each seed,

    C(delta,eta)=sup_(all actual nonconstant g) H(g)/I(g),

including extended-real infinity. The upper inequality is domain inclusion; the lower is (5) followed by a limit. This exact equality needs neither A075 localization nor the six-bit admission theorem. A finite C(delta,eta)=K therefore proves full FEI with the SAME constant K. A finite seed above K is not a disproof of the existence of an absolute constant.

## 3. Output-entropy-gap normalization

For minority p<=1/16, put D(g)=I(g)-h2(p). Entropy tensorization of the indicator of the minority set gives p log2(1/p)<=I/2: in a uniform two-point fiber the indicator's functional entropy is 1/2 exactly when the edge crosses the set. Tensorization follows by the log-sum inequality, or inductively from convexity of x log x under coordinate averaging. Thus I>=2p L, L=log2(1/p)>=4. The scalar inequality -(1-p)ln(1-p)<=p gives h2(p)<=p L+p/ln2; ln2>2/3 follows from the first two terms of its positive atanh series. Therefore

    h2(p)/I<=1/2+3/(4L)<=11/16,
    (5/16)I<=D<I,
    H/I<=H/D<=(16/5)H/I.                             (6)

For any delta<=1/16 and eta>0, the rare-gap supremum K_gap is finite if and only if full FEI holds. More quantitatively C_full<=K_gap<=(16/5)C_full. In particular a universal rare-gap bound K already gives full FEI(K), without an additive admission or JS loss. This does not prove K finite. The denominator is positive on the entire frozen rare domain, including arbitrarily small influence.

The activation schedule also survives this normalization asymptotically. For k>=1, h2(ap)<=h2(a)<=a(k+3/2), since ap<=a<=1/2. With I(F)>=a k^2,

    0<=h2(p(F))/I(F)<=(k+3/2)/k^2 ->0.              (7)

Thus the seed localization cannot hide a growing ratio in the discarded output-entropy term. For the conditioned-nonempty normalization, let v=Var(F), rho be its squared Fourier law conditioned nonempty. Then H(F)=h2(v)+v H(rho). For k>=3, v<=4a<=1/2 and h2(v)<=h2(4a)<=4ak. Therefore h2(v)/I(F)<=4/k, and

    H(rho)/(I(F)/v)=H(F)/I(F)-h2(v)/I(F).

The difference vanishes along the schedule. Natural-log entropy just multiplies ratios by ln2; output complement, dummy padding and disjoint sign tensoring preserve ordinary H/I. Conditional normalization must divide influence by v as well; otherwise it changes the target.

## 4. Actual sequence standard and exact first unsupported line

Given any hypothetical sequence of actual seeds g_j with R(g_j)->infinity, choose k_j>=max(j,I(g_j),3) and t_j=ceil(k_j^2/I(g_j)). The finite functions F_j above have p_min->0, I->0, and R(F_j)>=R(g_j)/(1+2/k_j)-1/k_j^2->infinity. Equation (6) transfers divergence both ways for H/D; (7) and the nonempty identity transfer it without an output-entropy artifact. This is a conditional construction from genuine high-ratio seeds, not an actual FEI disproof: no unbounded seed sequence is produced here.

The first unsupported universal line remains a dimension-independent bound for H/D of arbitrary rare actual cores, or the construction of actual seeds whose ordinary H/I is unbounded. Any signed child-surplus argument proposed to pay that rare terminal entropy must now prove precisely such a bound; rarity, small influence and the denominator change alone provide no restriction on the FEI supremum.
