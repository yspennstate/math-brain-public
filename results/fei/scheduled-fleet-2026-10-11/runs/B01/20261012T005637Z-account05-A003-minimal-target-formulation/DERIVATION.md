# Low-influence selection: exact constants and a stronger-rule obstruction

All logs are base two, all cubes uniform, all functions Boolean signs. I_i=alpha_i; B_i=H(S_i|S_-i), B=sum B_i. Let a=2/ln2. Let d be the number of relevant physical inputs, so dummy padding does not change the cutoff. For c in (0,1), define G_c(f)={i:alpha_i>=c I/d}. Its influence fraction beta=sum_(i in G_c)alpha_i/I is greater than 1-c and at least 1-c+c/d. This follows by bounding the sum of the d-|G| excluded influences by cI(d-|G|)/d. There is at least one included coordinate.

## 1. Added implication arrows

**Aggregate erasure-fraction.** On a restriction-closed class, B<=lambda H+K I, 0<=lambda<1, K>=0, implies H<=(K+a)/(1-lambda) I. Proof: suppose a violator exists for C=(K+a)/(1-lambda), choose one of least relevant dimension, and put delta=H-CI>0. Every child satisfies H<=C I. Therefore every relevant split obeys Delta_i H>=C alpha_i+delta and B_i>= (C-a)alpha_i+delta. Summing over all d relevant coordinates gives B>=(C-a)I+d delta. But the fraction hypothesis gives B<=(lambda C+K)I+lambda delta=(C-a)I+lambda delta, contradicting d>=1>lambda. Constants and characters cause no division problem.

**Low-influence good-coordinate localization.** Suppose tau in (0,1), lambda in [0,1), K>=0 are fixed, and every nonconstant Boolean f with max_i alpha_i<tau has some relevant i with

    B_i <= (lambda H/I + K) alpha_i.                    (L)

Then full FEI holds at

    C=max(log2(e/tau)+a,(K+a)/(1-lambda)).

For a minimal-dimension violator, every split has Delta_i>=C alpha_i+delta. If max alpha_i>=tau, use a maximum-influence coordinate and B_i<=h2(alpha_i)<=alpha_i log2(e/alpha_i); then Delta_i<=C alpha_i, a contradiction. In the weak case (L) gives Delta_i<= (lambda C+K+a)alpha_i+lambda delta alpha_i/I<=C alpha_i+lambda delta alpha_i/I, again smaller than C alpha_i+delta because alpha_i<=I and lambda<1. Conversely FEI(C) implies (L) with lambda=0,K=C for any fixed tau, by B<=H and weighted averaging. Thus this is a localization, not a solution or a stronger finiteness assertion.

**Mandatory high-average-influence selection.** If (L) requires i in G_c, the forward constant stays exactly the same. FEI(C) implies this version with lambda=0,K=C/(1-c), because B_G<=B<=CI and weighted averaging over G yields a ratio <=C/beta<=C/(1-c). For a fixed f the denominator beta is the more precise loss. Consequently a free finite K plus this cutoff is STILL FEI-equivalent. The lead's example is a stronger coordinate constraint at fixed budget, not a logically stronger finiteness endpoint. There is no well-defined smallest lemma among arbitrary universal formulations.

**Restricted high-bucket fraction.** If every weak f satisfies B_G<=lambda H+K I with 0<=lambda<1-c, then a minimal violator satisfies B_G>=(C-a)beta I+|G|delta, while the hypothesis gives B_G<= (lambda C+K)I+lambda delta. Since beta>=1-c and |G|>=1>lambda, it is enough to take

    C=max(log2(e/tau)+a, [K+a(1-c)]/[1-c-lambda]).

Here C>=a, so replacing beta by its lower bound is legitimate. This is a smaller statistic than aggregate B but leaves an unpaid universal inequality.

## 2. A fixed-budget open lemma and known-family eligibility

One concrete operational target, not asserted true, is

    (P4) For every nonconstant f with max_i alpha_i<1/4,
    some i with alpha_i>=I/(2d) obeys B_i<=4 alpha_i.

It would imply FEI at C=4+2/ln2: the strong-coordinate bound log2(4e)+a=2+3/ln2 is smaller, since ln2>1/2. FEI at that final constant does not, by the proved averaging arrows, supply P4 at its prescribed K=4 and c=1/2: the resulting cutoff price is larger. This is an explicit quantitative and witness-location gap, rather than an unspecified constant hidden in a reformulation. It is an OPEN target, not a third positive universal candidate.

Consume A001's stage-2 family formulas instead of rediscovering their minima. For X009 on k even >=4 data bits plus selector: alpha_data=1/2+delta, alpha_selector=delta, delta=2^-k. Every data coordinate is above I/(2(k+1)), and B_data/alpha_data<2. The root is outside the weak regime, so this tests the coordinate cutoff but is not evidence for the weak hypothesis. For B05 with r=2k controls, p=delta^2, s=sqrt(delta), u=1/2+delta, A=1-s+delta:

    alpha_data=p u, alpha_control=p A, alpha_selector=p delta,
    I=p[k u+2k A+delta], d=3k+1.

Every data coordinate and every control is in G_(1/2). For data, after multiplying by 2d/p, the required difference is k(5u-2A)+2u-delta=k(1/2+2s+3delta)+1+delta>0. Controls follow from A>=u. The selector need not qualify. All alphas are below 1/4. A001/A089's selectable B ratio is data at k=4 (<2) and control at even k>=6 (<2+7/1024); both eligible coordinates satisfy P4 at these roots. No descendant guarantee follows from this root certificate.

## 3. Retained-coordinate invariance under balanced block substitution

Let f(y,x_1,...,x_q) be any Boolean sign, and replace each x_j by a balanced Boolean h_j on disjoint fresh physical blocks. Keep y unchanged. Let F(y,z)=f(y,h_1(z_1),...,h_q(z_q)). The squared spectrum of each balanced h_j has zero empty mass. A frequency tuple (R_1,...,R_q) identifies an outer spectral label T exactly by j in T iff R_j is nonempty. Its two y-sector coefficients are a_(0,T) product_j hhat_j(R_j) and a_(1,T) product_j hhat_j(R_j). Homogeneity of Phi(u,v)=(u+v)h2(v/(u+v)) and Parseval in the encoders give

    alpha_y(F)=alpha_y(f), B_y(F)=B_y(f).

The same argument preserves Delta_y and JS_y, since the two children remain encoded by the SAME balanced blocks; no spectral row is independently declared Boolean. For an encoder bit ell in block j,

    alpha_(j,ell)(F)=alpha_j(f) alpha_ell(h_j),

by actual pivotal-edge counting and uniformity of every other encoded sign.

If h_j is odd under simultaneous input negation (in particular odd Majority_M), all its nonzero Fourier sets have odd cardinality. For a pair differing by one internal bit ell, both nonempty internal endpoints cannot have positive mass. The only possible surviving pair is empty versus {ell}, which changes whether outer coordinate j occurs. Thus, for Majority_M with rho=alpha_ell(h)=hhat({ell}),

    B_(j,ell)(F)=sum_(T not containing j) Phi(p_T,rho^2 p_(T+j)),

where T ranges over all other outer coordinates INCLUDING the retained y. The weight of every other encoded block sums to one. This formula is new here; it explains how a background coordinate can become a cheap, eligible alternative while the retained bad coordinate keeps its entire erasure.

For 0<t<=1, Phi(u,tv)<=tv/ln2+tv[log2(1/t)+log2(1+u/v)]. Set t=rho^2, sum, use L_j<=B_j<=h2(alpha_j)<=alpha_j log2(e/alpha_j). This gives

    B_(j,ell)/alpha_(j,ell)
      <= rho[log2(1/alpha_j)+2log2(1/rho)+2/ln2].       (D)

Zero probabilities are handled by continuity, and only alpha_j>0 are divided.

## 4. Maximum-influence selection is false, even with all influences tiny

Take the original B05 function f_k, k even >=4, with its k data bits, 2k controls, and one selector y. Keep y and replace ALL 3k background inputs by disjoint Majority_M blocks, where

    R=2^(2k+2), M=2R+1=2^(2k+3)+1,
    rho=binom(2R,R)/2^(2R).

This defines an actual finite Boolean function F_k on D=3kM+1 inputs for every k; no exponential truth table is simulated. The central-binomial ratio gives rho_{R+1}/rho_R=(2R+1)/(2R+2). Induction from rho_0=1 proves rho_R<=1/sqrt(R+1), since (2R+1)^2(R+2)<=4(R+1)^3, whose right-minus-left is 3R+2. Hence rho<2^(-k-1)=delta/2. Also M rho>=1, since the largest binomial coefficient is at least the average of the 2R+1 coefficients.

Each original background alpha lies in [p/2,p], and the selector alpha_y=pdelta. Therefore after substitution

    alpha_y(F_k)=pdelta=d_k,
    0<alpha_background(F_k)<=p rho<d_k/2.

So y is the UNIQUE maximum-influence coordinate; max alpha=d_k=2^(-3k)->0. By the retained-coordinate invariant and the already-established B05 lower bound,

    B_y(F_k)/alpha_y(F_k)
       =B_y(f_k)/(pdelta)>=(1-delta)(k-2)->infinity.

For every finite K and every tau>0, some actual F_k has all influences <tau but its only maximum-influence coordinate has B_i>K alpha_i. This refutes a fixed-price maximum-coordinate rule with lambda=0. The actual entropy-decrement version is also refuted because Delta_y>=B_y. It does not refute a rule with an additional lambda H/I term, the high-average-influence cutoff, existential selection, or FEI. Diluting the background increases its total influence relative to f_k; no H/I divergence is asserted. Even its total influence still tends to zero: M rho<2^(k+2)+2^(-k-1), so I(F_k)<=2^(-3k)+3k*2^(-2k)[2^(k+2)+2^(-k-1)]->0.

In fact the prescribed high-average cutoff survives emphatically. For an encoded data bit, eligibility alpha>=I(F_k)/(2D) is equivalent to

    M rho k(5u-2A)+2u rho>=delta.

Its left side is at least k/2>=2>delta, since M rho>=1 and 5u-2A=1/2+2s+3delta. Controls are larger and eligible too. All 3kM background coordinates are in G_(1/2), while y is included as the maximum.

Using alpha_j(f_k)>=p/2 in (D), log2(1/alpha_j)<=2k+1. The function rho[C+2log2(1/rho)+2/ln2] increases for rho<=1 when C>=0. Consequently every encoded background ratio satisfies

    B_background/alpha_background
       <=(4k+3+2/ln2)/2^(k+1)<1  (k even>=4).

The last inequality follows from 2/ln2<4, value (4k+7)/2^(k+1)<=23/32 at k=4, and its decrease thereafter. Thus every background bit is an eligible coordinate satisfying P4 at these roots, while the unique maximum bit has arbitrarily bad ratio. This gives an exact separation of the two stronger-coordinate proposals.

## 5. Exact first unsupported line

P4 has not been proved or disproved on arbitrary weak-influence Boolean sources or on all their reached restrictions. Neither high-bucket averaging nor balanced substitution supplies its fixed price 4. A universal erasure-fraction estimate, or a high-bucket fraction with lambda<1-c, is likewise unpaid. The constructed family only retires maximum-coordinate fixed-price selection and exhibits why the surviving cutoff must allow alternatives. C020's weighted coding-divergence payment from stage 1 remains open and is not advanced by renaming these selection statistics.
