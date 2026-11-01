# FEI: centered restriction budgets, primitive cores, and a dyadic all-profile obstruction

21 September 2026. Interactive fleet02 continuation, run `20260921T174421Z-centered-critical-budget`. Not a scheduled B-slot.

**Full uniform-cube FEI remains OPEN / NOT PROVED by this work.** No finite universal upper bound is established. The positive results below give exact restriction accounting and a more precise class of critical cores. The main obstruction theorem constructs normalized, dyadic-square probability laws satisfying all of the specified scalar parity/profile/cylinder tests with unbounded entropy per expected size, while proving that NO assignment of signs makes them Boolean Fourier spectra. This is a counterexample to a relaxation, not a counterexample to FEI. A separate genuine Boolean majority argument rules out a fixed subquadratic-moment shortcut.

All new analytic arguments and executed computations are self-checked. Independent end-to-end review and publication-priority clearance are pending. Model self-report: GPT-6 Astra Pro. Configured reasoning level and provider reasoning counters: NOT_EXPOSED. Research was conducted WITHOUT_VERIFIED_BRAIN: authenticated repository retrieval occurred, but native mathematical/cognitive brain modules were unavailable. Repository storage is not runtime ingestion or proof of later worker uptake.

## 1. Target and source-exact starting point

For f:F_2^n->{-1,1}, write a_s=E_x f(x)(-1)^{s.x}, mu(s)=a_s^2,

    H(f)=sum_s mu(s) log_2(1/mu(s)),
    I_i(f)=Pr_mu(s_i=1),    I(f)=sum_i I_i(f).

Terms of mass zero contribute zero. FEI asks whether H(f)<=C I(f) for every such function with one finite dimension-independent C. Booleanity is equivalent to the complete signed system

    sum_s a_s a_{s+u}=1_{u=0}.                          (1.1)

The predecessor package `20260921T163318Z-template-collapse`, complete at scientific commit `d6ad8493497d3ca37bf53058b6926f938f0d16c0`, proves that the optimized global phase/rank/l1 cost is exactly 2 log_2 ||fhat||_1 and cannot have a universal influence budget. Its coupled Shannon restriction estimate remains valid; the present work does not optimize that dead global norm again.

Fresh scientific master entering this run was `3b77bf544979ac8d7197a2299b89892445386726`. Specific inputs read were:

* B12's `20260921T165622Z-depth-rigidity-obstruction`, report blob `8e497dcff529c2128a74e6d199032906fa313440`: depth-only tests are insufficient; quantitative Boolean equality stability remains unpaid.
* B13's `20260921T172807Z-affine-block-basis-profile`, blob `10568dacbe88d7b7e540c65b5b129e9d22d01abd`: minimum affine-basis influence and the universal FEI constant are orbit-equivalent; profile identities alone do not pay the residual.
* B14's `20260921T170108Z-centered-refunded-selector`: median-character centering repairs deterministic parity padding, but a useful shell/restriction argument remains conditional.
* B15's `20260921T170301Z-valuation-tail-majorization`, blob `7633ed3dca15ea17d4c17af94e621f4ab3745691`: signed packet valuations obey all-cost and depth-tail inequalities; the arithmetic remainder still needs negative information credits.
* B16's `20260921T173238Z-qflip-frame-coordinate-incidence`, blob `970930a57e00f50bfe3891804cecd8e1fdefe1c3`: fixed nonnegative q-flip frames have universal capacity exactly when original-coordinate incidence is bounded up to constants; the actual signed compiler frame is not supplied by that characterization.
* B17's `20260921T154809Z-buried-atom-cancellation-flow`, blob `657861f2bb93ddcdf15abfca3c3b6a1de863733b`: mixed-derivative lattice control and a decisive failure of receiver-only strict-superset transport.
* B18's `20260921T170605Z-qflip-dependent-triple-radon-frame`: the local dependent-triple/Radon dictionary is exact; a globally paid realization is still missing.

These paths are under `proofnet24/P03-fei/fleet-2026-09-21/fleet02/<slot>/`. Reading a report is not an independent verification of all its claims. The new proofs below are given directly, and their reliance on earlier elementary identities is made explicit. The older addressing family is from `solo-2026-09-17/ADDRESSING_BARRIER_2026-09-18.md`, blob `c1e52dff50095854d85c20e8b13a5385d91efaca`. Its construction is reused, not claimed as new.

## 2. Positive result: an exact centered-influence restriction budget

Put p_i=I_i(f), q_i=min(p_i,1-p_i), and

    J(f)=sum_i q_i.

Multiplying f by a character shifts its Fourier law by a fixed vector, preserves H and J, and can make its ordinary influence equal to J. Thus a uniform H<=C J theorem is equivalent to FEI with the same constant. This character observation is inherited; the exact restriction refund below is the new accounting step.

### Theorem 2.1 — all-block drift and the singleton refund

Fix a nonempty physical coordinate block A. For a uniform assignment z on A let f_z be the corresponding restriction and p_j(z)=I_j(f_z) for j outside A. Define

    D_A(f)=J(f)-E_z J(f_z).

Then

    D_A(f)=sum_{i in A} q_i
        +sum_{j outside A}[ E_z |p_j(z)-1/2|-|p_j-1/2| ]
        >=sum_{i in A}q_i.                              (2.1)

For A={i}, let eta_j(x)=1{f(x)!=f(x+e_j)} and b_ij=E_x (-1)^{x_i} eta_j(x). The exact finer identity is

    D_i(f)=q_i+sum_{j!=i} (|b_ij|-|p_j-1/2|)_+.         (2.2)

A summand indexed by j is zero whenever q_j<=1/4.

Proof. For j outside A, averaging its boundary indicator over z gives E p_j(z)=p_j. Use min(p,1-p)=1/2-|p-1/2|, cancel the retained-coordinate terms, and apply Jensen to absolute value. For a singleton restriction the two child influences are p_j+b_ij and p_j-b_ij. The elementary identity

    (|u+v|+|u-v|)/2=max(|u|,|v|)

gives (2.2). Both child influences lie in [0,1], so |b_ij|<=q_j. When q_j<=1/4 this is at most |p_j-1/2|=1/2-q_j. QED.

This can be a genuine refund beyond the removed coordinate's original influence. For a two-bit AND truth table, J=1 and I_i=1/2, whereas its two children are characters/constants with J=0, so D_i=1. Conversely, when all folded influences are at most 1/4, the singleton formula has no refund. The latter limitation matters in the small-influence regime; the identity is not itself a universal payment theorem.

### Corollary 2.2 — exact nonreuse along adaptive restriction trees

Consider any finite adaptive physical-block restriction tree, with uniform branches and character leaves. Character multiplication is permitted at intermediate nodes. Let pi_v be a node's probability, f_v its function, and A_v its next block. Put Delta_A(f)=H(f)-E_zH(f_z). Then

    sum_internal_v pi_v D_{A_v}(f_v)=J(f),
    sum_internal_v pi_v Delta_{A_v}(f_v)=H(f).           (2.3)

Proof. Both identities telescope on a finite tree. At a character leaf H=J=0. Intermediate character multiplications preserve H and J, and commute with physical restriction up to a character on the remaining variables and an irrelevant sign. QED.

In particular, if a strategy has Delta_A<=C D_A at every visited node, it proves H(f)<=C J(f). More generally, a total positive excess at most epsilon J gives H<=(C+epsilon)J. **No strategy with a universal C is proved here.** The useful fact is that the refund in (2.1), unlike separately charging a surviving coordinate at several nodes, is part of one exact nonreused budget.

### Theorem 2.3 — even this budget cannot pay every prescribed coordinate

For even m>=2 put N=2^m. Let g(x)=(-1)^{x_1x_2+...+x_{m-1}x_m} on m address bits, let y_a be N independent data signs, and let the sign z choose between g(x) and y_x:

    f_m(z,x,y)=[(1+z)/2]g(x)+[(1-z)/2]y_x.

This is the inherited Boolean addressing/bent family. Its address and z influences are 1/2, each data influence is 1/(2N), and J(f_m)=I(f_m)=(m+2)/2. On fixing y_a=b, the other data influences and all address influences are unchanged, while

    I_z(f_m|y_a=b)=1/2-b g(a)/(2N).

Therefore

    D_{y_a}(f_m)=1/N.                                  (2.4)

The complete nonzero coefficient list has amplitudes 1/(2 sqrt(N)) with no data label and 1/(2N) with one data label, in both z parities. For one specified data bit there are 2N nonzero paired fibres. Their squared masses are 1/(4N) and 1/(4N^2). Thus, with R(t)=1-h_2(1/2+sqrt(t(1-t))),

    Delta_{y_a}(f_m)=(N+1)/(2N) [h_2(1/(N+1))+R(1/(N+1))].

The exact entropy/Jensen-Shannon restriction identity gives this last equality directly. Since R>=0 and h(t)>=t log_2(1/t),

    Delta_{y_a}(f_m)/D_{y_a}(f_m)
        >=(1/2)log_2(N+1)>m/2 -> infinity.              (2.5)

For completeness, the address influence after fixing y_a remains 1/2: the g branch contributes 1/4; each pair of distinct addressed values in the other branch disagrees with probability 1/2 even if one value is fixed, contributing another 1/4. The z influence follows by averaging its disagreement with the data branch; only the address a has a nonzero mean data value. This proves (2.4). The coefficient list follows by expanding 1{x=a}=N^{-1}sum_S(-1)^{S.a}chi_S and the two-bit bent transform (1,1,1,-1)/2. QED.

Hence a universally bounded payment for EVERY prescribed coordinate is false even with centered refunds. An existential block/coordinate strategy is not refuted by (2.5).

## 3. Positive reduction: primitive centered ratio-critical cores

A noncharacter has J>0. From the finitely many physical restriction descendants of f, maximize H/J, and among maximizing descendants choose one on the fewest relevant variables. Multiply by its median character and delete irrelevant variables. Call the result h and R=H(h)/J(h)>0. Its ratio is at least H(f)/I(f).

### Theorem 3.1 — precise critical-core properties

The core can be chosen so that:

1. Every remaining influence lies in (0,1/2], so I(h)=J(h).
2. Every proper noncharacter physical restriction g has H(g)/J(g)<R.
3. For every nonempty restricted block A,

       Delta_A(h)>=R D_A(h),                            (3.1)

   with strict inequality when at least one child is a noncharacter; equality when every child is a character.
4. h has no nontrivial disjoint-variable multiplicative factorization.
5. No projection of its Fourier support onto a proper coordinate subset is injective. In particular its support contains an edge in each coordinate direction, and its affine span is all F_2^n.

Proof. If an influence is zero the variable is irrelevant; if it is one the function has that character as a factor. Restricting such a variable preserves H and J, contrary to minimality. Median-character multiplication folds each remaining influence to (0,1/2] and preserves all restriction ratios. This proves 1 and 2. Average H(g)<=R J(g) over the children and use H(h)=R J(h) to get (3.1); the strictness statement follows from 2.

If h=u(x_A)v(x_B) on disjoint nonempty variable sets, its spectral law is a product and H,J add. Every noncharacter factor occurs, up to sign, as a proper restriction. Its ratio is at most R, while a positive-J weighted average of the factor ratios equals R. At least one factor then has ratio R, violating 2. A character factor has H=J=0 and can simply be removed, also violating minimality.

If support projection onto B is injective, fixing coordinates outside B changes the signs of coefficients but creates no Fourier collisions. Every child therefore has exactly the same nonzero squared coefficients, so has entropy H(h)>0. Its centered influence is J(h)-sum_{i outside B}q_i<J(h), giving a larger H/J ratio, impossible. For B omitting a single coordinate, noninjectivity means a support edge in that direction. The edge differences include every basis vector, proving the affine-span statement. QED.

This reduces the class to which a new universal argument must apply; it does not bound R. No claim that these properties alone characterize Booleanity or imply FEI is made.

### Theorem 3.2 — tensor replication defeats a shell condition on EVERY weak core

Call a function weakly centered restriction-critical when its H/J ratio is at least that of every noncharacter physical restriction, without the minimum-dimension requirement. If h has this property, then so does h^{tensor d}: every physical restriction factors, and its ratio is a J-weighted average of ratios at most that of h.

Let A be a coordinatewise median of the spectrum of h, c=mu(A)<1, and u=sum_i mu(A+e_i). The tensor power has J_d=d J(h), while its centered first-shell mass is d u c^{d-1}. Hence

    r_c(h^{tensor d})=(u/J(h))c^{d-1} ->0.              (3.2)

When c=0, it is zero already for d>=2. The entropy/influence ratio does not change. All assertions follow by independence of the spectral factors and additivity of H,J. This is an all-dimensional proof, not a finite extrapolation.

For an explicit example take h to be two-bit AND. Every restriction is AND, a character or a constant; h is weakly critical with H/J=2. Its d-fold tensor has

    H=2d, J=d, r_c=(1/2)(1/4)^{d-1}.

Thus a positive shell lower bound for every weakly critical function is impossible on any nonvacuous attained ratio range. It remains possible to select a useful minimum-dimensional core or a descendant; (3.2) does not refute that existential quantifier or the valid B14 selector inequality.

## 4. Full-problem obstruction: dyadic squares plus all specified scalar tests are insufficient

This section constructs a family nu_m of probability laws on F_2^n, n=2^m, m>=7, satisfying all the following simultaneously:

* Every probability is the square of a dyadic rational and their sum is exactly one, on a common amplitude grid coarser than the ordinary Boolean Walsh grid.
* Every affine cylinder C of codimension k>=1 satisfies, for every xi in C,

       sqrt(nu_m(xi)) <= 2^{k-1} nu_m(C).                (4.1)

* For every nonzero parity J, either parity outcome of positive probability r, every Hamming centre T and every s in [0,1],

       E[s^{|X+T|} | parity_J=y] <= r^{(1-s)/(1+s)},
       E[|X+T| | parity_J=y] >=(1/2)log_2(1/r).          (4.2)

* The specified spectral Bayes-Han necessary profile inequalities hold at every cardinality (defined below).
* H(nu_m)/E_{nu_m}|X| tends to infinity.
* **No assignment of signs to sqrt(nu_m) can satisfy Booleanity.**

The word 'all' in this theorem refers to these explicitly named tests. It does NOT mean all Boolean constraints, all possible projection inequalities, or all noise inequalities after arbitrary changes of Hamming geometry. The theorem rules out this combined scalar relaxation, not FEI.

### 4.1 Why (4.1) is genuinely necessary for Boolean spectra

An invertible linear change of input variables and a character multiplication convert an arbitrary affine spectral cylinder of codimension k to the event that its first k frequency bits equal one; they send a chosen atom in it to one with remaining frequency bits zero. The k-fold derivative of the resulting Boolean function is an alternating average of 2^k signs, so it takes values in delta Z with delta=2^{1-k}. Its expectation is the chosen coefficient a_xi and its squared L2 norm is the cylinder mass. Pointwise |D|<=D^2/delta. Taking expectations proves |a_xi|<=2^{k-1}mu(C). This proof preserves actual Boolean realizability; it is not an assertion about arbitrary squared vectors.

### 4.2 A robust product seed with a tiny uniform component

Put

    n=2^m, D=2^n, alpha=4m/n, w=32/n^2,
    P=Ber(alpha)^{tensor n},    mu=(1-w)P+w Unif(F_2^n).

Here alpha<=1/4. We have

    mu(s)>=w/D,    max_s mu(s)<=2/n^4,                 (4.3)
    I_mu=(1-w)4m+16/n,
    H(mu)>=(1-w)4m log_2(n/(4m)).                      (4.4)

Indeed (1-alpha)^n<=exp(-4m)<=n^{-4}, and w/D<=n^{-4}; entropy concavity gives the last inequality. The uniform component costs only 16/n in the first moment.

### 4.3 Exact square normalization and a forced parity defect

Let K=3n, let L be the least power of two at least 6n, write ell=log_2 L, and put

    d=n-1-ell,    M=2^d=D/(2L),    epsilon=1/M.

Thus L>=2K and L<12n. Reserve K labels: the all-ones label, all n co-singletons, and the first 2n-1 co-pairs in lexicographic order. Call their set R. Every reserved label has weight at least n-2.

Outside R put b_s=floor(M sqrt(mu(s))). Let q=n-d+1=ell+2 and C_0={s:support(s) is contained in the first q coordinates}. It is disjoint from R. If sum_{s in C_0}b_s is even, decrement b_0 by one. Otherwise make no change. The resulting sum on C_0 is odd.

The remaining integer square deficit is

    R_0=M^2-sum_{s outside R}b_s^2,   0<=R_0<M^2.

Write R_0 in base four. Each digit e_j in {0,1,2,3} contributes e_j copies of the square (2^j)^2. There are at most 3d<=K such squares. Assign their nonnegative square roots in the fixed reserved-label order, and set unused reserved amplitudes to zero. Define

    nu(s)=b_s^2/M^2.                                  (4.5)

This is an exact probability law of dyadic squares. The smallest positive amplitude is at least epsilon=2L/D, larger than the minimal Boolean grid 2/D. The construction is finite, deterministic and succinct by Hamming-weight multiplicities and K exceptions. It is not an enumeration of all D entries at large n.

### 4.4 Quantitative construction estimates

Set tau=97n/sqrt(D). For n=2^m,m>=7,

    nu(s)>=mu(s)/2  for s outside R,
    TV(nu,mu)<=tau<=1/n^2,
    max_s nu(s)<=2/n^4,
    TV(nu,P)<=delta:=33/n^2<=alpha/2.                  (4.6)

Here are full estimates. The two possible rounding steps lose at most 2epsilon from any nonreserved amplitude. Its original amplitude is at least sqrt(32)/(n sqrt(D)), so its relative loss is at most

    48n^2/(sqrt(32)sqrt(D)) <=1/4.

This proves the first inequality of (4.6), and b_0 is certainly at least two before the optional decrement. Total square-mass loss from rounding is at most 4epsilon sum_s sqrt(mu(s))<=8L/sqrt(D)<96n/sqrt(D). On a reserved label P(s)<=alpha^{n-2}<=16/D^2<=w/D, so mu(R)<=192/(nD). The mass reassigned to R is therefore at most tau. Total variation from mu is no larger than that reassigned mass: outside R all mass decreases, and inside R the sum of the two absolute masses bounds the discrepancy. This proves the second inequality. Each new reserved atom is at most tau<=2/n^4; nonreserved atoms only decreased. Finally TV(mu,P)<=w, proving the delta bound.

The elementary bounds used here, together with tau<=1/16, n tau<=1/4 and 4n tau<=alpha/2, hold at n=128. They continue to hold when n doubles: polynomial factors grow by a fixed power of two while sqrt(D)=2^{n/2} gains a factor 2^{n/2}. This supplies all m>=7, not just the three executed examples. The checker verifies the corresponding rational squared inequalities directly for those examples.

For any nonempty event E of cardinality e, a stronger inequality than (4.1) holds:

    nu(E)>=2(e/D) sqrt(max_{s in E}nu(s)).              (4.7)

When e<=L, let u be its largest nonzero amplitude. Then u>=epsilon=2L/D>=2e/D and nu(E)>=u^2>=2(e/D)u; a zero-mass event is trivial. When e>L, at least e-K>=e/2 labels are unreserved, each of mass at least w/(2D). Hence nu(E)>=we/(4D), which dominates the right side because w/4=8/n^2>=2sqrt(2)/n^2. Apply this to e/D=2^{-k} to prove (4.1) for all affine cylinders.

### 4.5 Parity conditioning and all noise parameters

We use an elementary product-parity lemma from the preceding continuation, restated with its proof. For independent Bernoulli disagreement bits Z_i with arbitrary parameters theta_i, conditioning on a specified parity event of probability r changes E sum_i Z_i by at most 1-r, hence at most one. Write c_i=1-2theta_i and C=prod_{i in J}c_i. Direct expansion gives

    E[sum Z_i | parity=y]-E sum Z_i
      =-y/[2(1+yC)] sum_{i in J}(1-c_i^2)prod_{j in J,j!=i}c_j.

The inequality

    sum_i(1-x_i^2)prod_{j!=i}x_j<=1-(prod_i x_i)^2,

for x_i in [0,1], follows by induction from

    1-a^2b^2-b(1-a^2)-a(1-b^2)=(1-a)(1-b)(1-ab)>=0.

Taking absolute values proves the lemma, including zero c_i by continuity.

Under P every nonempty parity event has probability at least alpha. For any centre T put K_T=|X+T|. Its independent disagreement probabilities are alpha or 1-alpha. If 0<=s<=1/2, discarding the conditioning event gives

    E_P[s^{K_T}|E]<=alpha^{-1}(1-alpha+alpha s)^n
      <=alpha^{-1}e^{-2m}<=1/(4mn).                   (4.8)

If 1/2<=s<=1, exponential tilting by s^{K_T} preserves independence, and each tilted disagreement probability is at least alpha s. The product-parity lemma then yields

    d/ds ln E_P[s^{K_T}|E]
      =E_{P,s}[K_T|E]/s>=4m-2.

Integrating to s=1 gives

    E_P[s^{K_T}|E]<=exp(-(4m-2)(1-s)).                 (4.9)

Let r=nu(E). From (4.6), r>=alpha/2. The conditional total variation is at most delta/P(E)<=delta/alpha<=33/(4mn). To verify this standard inequality directly, suppose one event mass is the larger, say r_P>=r_nu. The overlap of the two conditional distributions is at least their unnormalized overlap on E divided by r_P. Its deficit is at most TV(P,nu)/r_P. The other ordering is symmetric. Denote this bound by V.

The expectations of s^{K_T} under the two conditional laws differ by at most V min{1,n(1-s)}. On s<=1/2, (4.8) therefore bounds the new expectation by 34/(4mn)<=alpha/2<=r^{(1-s)/(1+s)}.

For s>=1/2 set t=1-s, A=4m-2 and B=(2/3)ln(2/alpha)<=m/2. The desired right side is at least exp(-Bt). The gap from the P upper bound is

    exp(-Bt)-exp(-At)=exp(-Bt)(1-exp(-(A-B)t)).

When 0<=t<=1/m, A-B>=3m and (A-B)t<=4. Using 1-e^{-u}>=u/(1+u) and e^{-1/2}>1/2, the gap is at least 3mt/10. This dominates Vnt<=33t/(4m) for m>=7. When 1/m<=t<=1/2, the gap is at least (1/2)e^{-B/2}=(1/2)(alpha/2)^{1/3}>=alpha/4=m/n, which dominates V. This proves the first half of (4.2) on the ENTIRE noise interval.

For dispersion, the product-parity lemma gives E_P[K_T|E]>=4m-1. Conditional total variation changes a [0,n]-valued mean by at most nV. Thus

    E_nu[K_T|E]>=4m-1-33/(4m)>=m/2
       >=(1/2)log_2(1/r),                              (4.10)

because r>=alpha/2=2m/n>=2^{-m}. This proves the second half of (4.2). All atom, small-ball and two-parity averaged consequences of these stated inequalities follow as well.

### 4.6 The spectral Bayes-Han profile tests also pass

For any law let h_q be the average entropy of its q-coordinate marginals, H its full entropy, and A_q=h_q-(q/n)H. For q<n let epsilon_q be the average optimal error probability for predicting a coordinate outside a q-subset from the coordinates in that subset. Then for the constructed law

    0<=A_q<=2(n-q)epsilon_q
             <=(2/ln2)(n-q)epsilon_q.                  (4.11)

The lower bound is the averaged chain-rule/Shearer inequality: conditioning on fewer coordinates increases each chain-rule term, then average over all q-subsets.

To prove the upper bound, for the mixture mu introduce its binary mixture label Z. Conditional on Z all coordinates are independent. If v=(1-w)h_2(alpha)+w, then h_q(mu)<=qv+h_2(w), while H(mu)>=nv. Hence A_q(mu)<=h_2(w). Entropy continuity at total variation tau on at most D points gives |H(nu)-H(mu)|<=h_2(tau)+n tau, and the analogous marginal bound. Therefore

    A_q(nu)<=h_2(w)+2h_2(tau)+2n tau<=alpha.            (4.12)

The final estimate uses h_2(w)<=w(log_2(1/w)+2)<=64m/n^2<=alpha/2, h_2(tau)<=n tau, and 4n tau<=alpha/2. Entropy continuity itself follows by coupling two variables with disagreement probability at most tau: each conditional entropy is at most h_2(tau)+tau log_2(D-1), and the chain rule bounds the entropy difference.

Under the independent P law every prediction error is alpha. Bayes error is an infimum over bounded classification losses and is therefore 1-Lipschitz in total variation. Thus epsilon_q(nu)>=alpha-delta>=alpha/2. Together with q<n and (4.12), this proves (4.11). These are the specified NECESSARY spectral inequalities, not an assignment of the missing signed recombination terms or a physical restriction tree.

### 4.7 Unbounded ratio and impossibility of every Boolean signing

From entropy continuity, (4.4) and (4.6), the entropy loss from mu is at most h_2(tau)+n tau<1; the first moment changes by at most n tau<1. Thus the explicit lower bound is

    H(nu_m)/E_nu_m|X|
      >={(1-32/n^2)4m[m-2-ceil(log_2 m)]-1}/(4m+2)
      ->infinity.                                    (4.13)

Indeed h_2(tau)<=h_2(1/16)<3/8 and n tau<=1/4, proving the stated entropy-loss bound without relying on a decimal.

Now give every nonzero amplitude an ARBITRARY sign, c_s=+/- b_s, and suppose its inverse Walsh transform were Boolean. Then

    B(x):=sum_s c_s(-1)^{s.x}=M f(x),  f(x) in {-1,1}.

Let T be the first q=n-d+1 coordinates. Sum this identity over inputs with x_T=0. Character orthogonality gives

    sum_{s subseteq T}c_s
      =2^{d-n+q}sum_{x:x_T=0}f(x)
      =2 sum_{x:x_T=0}f(x),                            (4.14)

an even integer. But signs do not change parity, and the construction deliberately made sum_{s subseteq T}b_s odd. Reserved labels do not lie in this cube. This is a contradiction for EVERY signing. QED.

The obstruction identifies one joint integer-parity constraint that the scalar tests miss. It does not prove that satisfying this one missing constraint would suffice: further constraints remain. The family also has unbounded H divided by minimum affine-basis influence, since that minimum is at most its current first moment. We do not assert that the all-Hamming-centre noise inequalities survive arbitrary invertible changes of Hamming geometry.

## 5. Genuine Boolean obstruction to fixed subquadratic moments

### Theorem 5.1

For every fixed 0<p<2 and rho>0 there is no finite A such that every Boolean f satisfies

    sum_S rho^{|S|}|fhat(S)|^p<=1+A I(f).               (5.1)

Proof. Let n=2m+1 and f=Maj_n. Put a_n=binom(2m,m)/4^m. The first derivative of majority is the indicator of the middle slice on the other 2m bits, so I(f)=n a_n. Its odd-level coefficients, for k=2r+1, are

    fhat(S)=(-1)^r a_n binom(m,r)/binom(2m,2r),         (5.2)

and its even-level coefficients vanish. To see (5.2), the middle-slice character moments are the even coefficients of (1-t^2)^m, divided by binom(2m,2r). This is an exact formula.

For m>=1, elementary induction using the central-binomial ratio (2m+1)/(2m+2) gives

    1/(2sqrt(m))<=a_n<=1/sqrt(m+1).

For fixed r and sufficiently large m, the binomial quotient in (5.2) is bounded below by a positive r-dependent constant times m^{-r}. Therefore a level-k coefficient has magnitude at least c_k n^{-k/2}; the level contains at least c'_k n^k coefficients, whereas I(f)<=sqrt(2n). Its contribution divided by influence is consequently at least

    c_{p,k}rho^k n^{[k(2-p)-1]/2}.                     (5.3)

Choose an odd fixed k>1/(2-p). The expression diverges, proving (5.1) impossible. The additive one is negligible since I tends to infinity. QED.

The same argument rules out any fixed degree weights that are positive at such a k. It does not address exponent p>2 lower bounds, a parameter tending to two with dimension, or a direct Shannon/negative-credit argument. Majority is a standard construction and (5.2) is a standard Fourier calculation, derived here to make the exact obstruction self-contained. No novelty claim is made for the ingredients or for the entire statement without a fuller comparison.

## 6. Executed checks and non-improving exploration

The main suite `verify_budget.py --part all --output verification.json` executed successfully. It records:

* 984,884 exact block-drift instances over every Boolean truth table through four variables and every nonempty restricted block;
* 262,948 exact singleton-refund instances and 228,304 exact low-folded-influence zero-refund checks;
* complete integer Walsh transforms of the addressing family at m=2 (128 input values) and m=4 (2,097,152 values), including all nonzero coefficient identities; data-coordinate drift checked for all four data bits at m=2 and one at m=4;
* 43,690 exact majority coefficient checks through fifteen variables;
* exact tensor-AND examples through twelve variables;
* a preliminary unrounded uniform-dust variant with weight 4/n^2, including 8,384 exact coordinate-cylinder types. That preliminary variant is distinct from the final weight-32/n^2 square-normalized construction and is not substituted for it.

`quantized_relaxation.py` constructs the final family succinctly at m=7,9,11, with ambient dimensions 128,512,2048. Exact integer/rational checks verify norm one, the odd-cube parity obstruction, amplitude-grid and maximum-atom bounds, preservation of the nonreserved uniform floor, total-variation bounds, and the scalar margins used in the analytic all-noise proof. The all-parity/all-cylinder/all-cardinality assertions are established by the written analytic cover and these invariants, not by enumerating exponentially many tests. At n=2048 the displayed floating entropy/first-moment ratio is about 6.96677; **this is a provably non-Boolean surrogate, not an FEI lower-bound record.** The rigorous bound used for the infinite family is (4.13).

The fixed-p finite majority examples at n=101,1001,10001 have not yet crossed one in the selected level-three ratio; their exact comparisons are retained as false flags. The divergence is proved by (5.3), not inferred from those examples.

Exploratory floating searches examined strict restriction-critical functions through four variables, five-variable functions with minority size at most seven, and faces of selected tribes functions. They did not produce a new full-bound improvement or a non-unate strict-core counterexample. Their absence is not a theorem that all critical cores are unate, and the five-bit search is not exhaustive over all truth tables. The actual scripts/results are preserved separately rather than promoted to a universal conclusion.

## 7. Full-proof checklist and exact remaining task

PROVED here, self-checked:

* exact centered block/singleton refunds and adaptive telescoping;
* primitive centered ratio-critical reduction and the tensor quantifier obstruction;
* failure of prescribed-coordinate centered payment on a genuine Boolean family;
* a normalized dyadic-square counterfamily passing the specified complete scalar test families, with unbounded H/mean and a proof that no signing is Boolean;
* failure of every fixed p<2 degree-damped moment upper payment.

INHERITED / NOT REANNOUNCED:

* character folding, the exact erasure/Jensen-Shannon identity, addressing and recursive-majority constructions;
* the previous global phase-cost collapse and the coupled scalar restriction theorem;
* the valid source-scoped results of B12-B18.

OPEN:

* a realizable adaptive restriction strategy controlling the total entropy cost by a finite universal multiple of J;
* an inequality on primitive critical Boolean cores excluding arbitrarily large H/J;
* a signed or joint-arithmetic mechanism that pays a universal entropy remainder, not merely the scalar tests refuted in Section 4;
* full FEI.

A usable next target is to combine the exact nonreuse in (2.3) with a theorem applying to the primitive cores of Section 3. The construction in Section 4 says that neither dyadic-square normalization nor the full named list of marginal/cylinder/parity conditions can replace genuine joint Boolean realizability. The witness in Section 2 says that the next selector must be existential/adaptive, not a bound for every prescribed coordinate. These narrow the admissible proof mechanisms; they are not a hidden claim that the last universal step has been proved.

## 8. Literature, source limitations and durable delivery

Current primary sources checked include Xiao Han, *A New Bound for the Fourier-Entropy-Influence Conjecture*, Combinatorica 45 (2025), article 4, DOI 10.1007/s00493-024-00133-z / arXiv:2312.08271; its moment method uses exponents above two and retains the sum of marginal-influence logarithms. The no-go in Section 5 is not a refutation of that theorem. Current restriction and class results checked include Gonzalez--MacManus--Pereyra, arXiv:2606.00246; O'Donnell--Tan, arXiv:1304.1347; and Potapov, arXiv:2609.21563. They are not imported as a full unconditional proof. The official optimization-constants project entry 71a records a certified lower bound above 6.521845710923046575 from an 18-variable monotone seed and amplification. Its certificate was not independently rerun here.

Searches included FEI with Renyi/majority, Han's exact theorem, and the current constant. These were bounded applicability checks, not exhaustive novelty clearance. The complete arguments used for the new claims are written above. The source reports and prior public mechanisms retain their attribution and exact restrictions.

The owner's request for ongoing work is implemented through the existing seven fleet02 FEI tasks and existing B20 caretaker, not an extra schedule or a guarantee of a proof date. Actual prompt update and reporting/engineering observations are recorded separately in the brain handoff. No historical proof is overwritten, no production truth status is promoted, and no native brain ingestion or other-account uptake is claimed. Purely mathematical artifacts and sanitized operational records only are authorized for this private delivery.
