# Extension: the exact positive current also fails at the HALF-BAND live cutoff

21 September 2026. Continuation of REPORT.md, same interactive run. Full FEI remains NOT PROVED. These are analytic self-checked results, pending independent review, with no priority claim.

**This extension strengthens the earlier report.** Its Section 5 refuted full-line payment at the half-band cutoff, while Section 6 initially refuted finite-window payment only at later cutoffs. The collision argument below now proves that the same genuine Boolean family has excessive EXACT positive current on the HALF-BAND live window too. The original signed FEI ledger, a specially justified high-ratio-core restriction of the target, and the A/B/D alternatives are not refuted.

## 1. Code-coset collision bound

Let Y=(Y_1,...,Y_M) have +/-1 coordinates matching independent uniform signs through products of at most 4m distinct coordinates. Here M need not be even. Let W=sum Y_i, let Z be any real random variable with |Z|<=1 on the same probability space, and put

    phi(t)=E[Z exp(i t W)].

Then

    integral_0^pi |phi(t)|^2 dt
       <= pi Pr(W=W')
       <= pi/K_(2M,m)
       < pi/sqrt(m),                                     (1.1)

provided m>=1 and 2m<=2M; W' is an independent copy. K is the explicit Christoffel sum in REPORT Lemma 4.1.

Proof. Write a_w=E[Z 1{W=w}], p_w=Pr(W=w), so |a_w|<=p_w. All possible w have the same parity. Consequently orthogonality on [0,pi] gives the exact identity

    integral_0^pi |phi(t)|^2 dt=pi sum_w |a_w|^2
                               <=pi sum_w p_w^2.

The last sum is Pr(W=W'). The concatenated 2M signs (Y_1,...,Y_M,-Y'_1,...,-Y'_M) still match independent signs through degree 4m: a mixed product factors over the two independent copies, and each nonempty subproduct of total degree at most 4m has zero mean. Their sum is W-W'. REPORT Lemma 4.1 on these 2M coordinates gives the rest. This proof does NOT require a uniform pointwise anti-concentration estimate at every possible w or independence of Z from W. QED.

For the Reed--Muller word r in RM(d,D), remove any four physical evaluation positions and let Y_x=(-1)^{r(x)} on the remaining M=N-4 positions. They retain (2^(d+1)-1)-wise independence. We may choose

    m=2^(d-1)-1,                                         (1.2)

for d>=2 and 2m<=2(N-4). In particular this applies at d=ceil(D/2) for the dimensions used below. Multiplication by any fixed sign pattern also preserves the bound.

## 2. Restore the terminal-code coefficient BEFORE estimating it

Keep exactly the four-point Boolean source, the two original parents, and their four active singleton slice-clones from REPORT Section 5. In particular all n=D-1 original coordinates are relevant, J=I=8n/N, and H(f)<4I(f). The negative set Q is an affine two-plane.

For a triple R of the four active positions, let b_R^(0)(s) and b_R^(1)(s) be the active Walsh coefficients of the individual potentials associated with P0=RM(1,D) and P1=RM(d,D). The actual retained coefficient is

    b_R(s)=b_R^(0)(s)-b_R^(1)(s).

Put t=s/N. For r in P1 let Y_x=(-1)^{r(x)},

    W_out=sum_(x outside Q)Y_x,     Z_R=product_(x in R)Y_x.

The independent uniform active signs give the EXACT identity

    b_R^(1)(Nt)=2N sin(t)^3 cos(t) E_r[Z_R sin(t W_out)].   (2.1)

Indeed the active coefficient of exp(i t[W_out+sum_(x in Q)epsilon_x Y_x]) is exp(i t W_out) times the product of iY_x sin(t) for x in R and cos(t) for the other position. Since |R|=3, taking its real part yields (2.1). The terminal code and the active-syndrome average have not been replaced by another distribution.

Let T=1/sqrt(2n), so S_f=NT is the source canonical upper endpoint. Equation (1.1), |sin t|<=t and |cos t|<=1 give

    integral_0^(NT) [b_R^(1)(s)]^2 ds/s^3
      <=4 T^3 integral_0^T |E[Z_R exp(i t W_out)]|^2 dt
      <=4 pi T^3/sqrt(m).                                (2.2)

This bound uses only the stated exact code independence. In particular it does not assert that its entire weight distribution is binomial.

The affine coefficient is the explicitly derived formula from REPORT Section 6:

    b_R^(0)(Nt)=2N B_N(t),
    B_N(t)=sin(t)^3 cos(t)
            [sin((N-4)t)/N-(1/4-1/N)sin(4t)].              (2.3)

The exact checks compare both (2.1) and (2.3) with code/active Fourier coefficients, not just with a fitted numerical curve.

## 3. Half-band live-current countertheorem

### Theorem 3.1

At the actual half-band cutoff d=ceil(D/2), for all D>=128 the genuine Boolean family above satisfies

    integral_40^Sf E_cur(s) ds/s^3 >=7/[3145728 (D-1)^3].   (3.1)

In particular its ratio to J(f)=8(D-1)/2^D is unbounded. The same conclusion holds for the central positive current with its exact positive multiplier, and survives the source's outer original-anchor/coordinate-order average. The source functions themselves still obey H(f)<4I(f).

Proof. Set n=D-1, T=(2n)^-1/2. On the subinterval s in [NT/2,NT], REPORT Section 6 proves for D>=10 that

    E0:=integral_[NT/2,NT] [b_R^(0)(s)]^2 ds/s^3
       >=21 T^6/131072.                                  (3.2)

This follows directly from |b_R^(0)(Nt)|>=Nt^4/32; the entire interval lies in [40,S_f]. By (2.2),

    E1:=integral_[NT/2,NT] [b_R^(1)(s)]^2 ds/s^3
       <=4 pi T^3/sqrt(m).

For D>=128 and m=2^(ceil(D/2)-1)-1,

    m >=8 n^3 (2097152 pi/21)^2,                          (3.3)

so E1<=E0/4. To check (3.3) without numerical constants, use pi/21<1/6. At D=128 and 129, m>=2^62 and n<=128, while the right side is less than 2^64/9<2^62. On increasing D by two, m more than doubles, whereas n^3 grows by less than a factor two for n>=8. This proves (3.3) for every D>=128.

The reverse triangle inequality in the actual weighted L2 interval now gives

    integral_[NT/2,NT] b_R(s)^2 ds/s^3
       >=(sqrt(E0)-sqrt(E1))^2 >=E0/4.

The triple is a charged mode with exact e_R=4/9. Thus its contribution alone is at least E0/9=7/[3145728 n^3], proving (3.1). Replacing e_R by epsilon_R=11/288 gives the central conclusion. The original anchor/order event of probability at least 1/8 from REPORT Section 5 has the same four-point structure; nonnegativity retains that fixed fraction. QED.

This is not obtained from an upper bound which might be wasteful: (3.1) is a lower bound on the exact positive current itself, with the genuine current weights, actual active orbit, and actual retained half-band code.

## 4. Exact leading order, beyond one cutoff

The construction admits the sharper asymptotic

    integral_40^Sf E_cur(s) ds/s^3 ~4/[27(D-1)^3]          (4.1)

for every sequence of cutoffs satisfying

    2^d/(D-1)^3 -> infinity,

within 2<=d<=D. This includes d=ceil(D/2) and the later d>=D-2 case.

Proof. The affine calculation in REPORT gives, for each triple, weighted energy asymptotic (2/3)T^6 on the full live interval; equivalently B_N(t)=-t^4+O(t^6) plus an error of weighted norm O(1/N). The terminal bound (2.2) divided by T^6 is O(n^(3/2)/2^(d/2)), tending to zero under the stated hypothesis. Hence the weighted L2 norm of b_R^(0)-b_R^(1) has the same leading value as that of b_R^(0), regardless of their correlation. There are exactly four triple modes, each with e_R=4/9; all four singleton odd modes have q=k=1 and multiplier zero. Thus the full current asymptotic is 4*(4/9)*(2/3)T^6=4/(27n^3). QED.

No enormous code was enumerated and no asymptotic numerical fit proves (4.1). The moment bound, exact active coefficient and the written L2 comparison do so.

## 5. Consequence for the actual full-proof attempt

The newly derived sharp kernel contraction remains valid, as do the peer's PSD/window/projector identities. However BOTH of the following universally quantified positive budgets are now rigorously refuted at their stated all-Boolean scope:

    full-line/current Brownian budget <= constant*J;
    finite-half-band exact positive current <= constant*J.

Restoring the finite window is necessary to avoid one overestimate, but it is NOT by itself enough. A source-valid continuation has to retain the compensating signed R16, entropy, terminal or other originally reserved terms inside the claimed inequality, or prove that a justified reduction to a narrower critical class excludes these examples. No such compensation theorem or exclusion theorem is proved here. The identity (7.3) in REPORT is still exact but is not an O(J) estimate.

The source family's own H/I<4 is why none of these results refutes FEI. Its low-ratio status also leaves open a genuinely justified high-ratio-core approach. Merely adding that hypothesis without deriving the required reduction or estimate would not be a proof.

The useful new analytic tool beyond the counterexample is (1.1): bounded-independence anti-concentration controls the squared oscillatory coefficient even with an arbitrary dependent bounded sign multiplier. It may apply to the signed negative-credit terms too, but that application must be demonstrated rather than assumed.

## 6. Executed checks and scope

The companion `verify_halfband_collision.py` checks finite code collision and signed-coefficient inequalities with exact integers/Fractions, and verifies (2.1) as an EXACT Laurent-polynomial identity against direct code/active Fourier histograms. It also checks the coarse all-D numerical threshold through a bounded range with rational pi upper bound, supplements the written induction, and reports the asymptotic scale in clearly labelled numerical examples.

The large-D half-band theorem is analytic. These finite computations neither enumerate its huge code nor constitute an independent audit. All results remain self-checked, and full FEI remains unproved.
