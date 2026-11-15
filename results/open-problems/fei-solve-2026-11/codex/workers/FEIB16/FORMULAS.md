# Composition and family formulas

All mathematical assertions in this file marked PROVED have the argument here. CHECKED refers only to the numerical scope in validation.json; OPEN means no proof or full optimization. Entropy is in bits. Boolean values are ±1, and truth-table bit x is one when f((-1)^x)=-1.

## 1. Arbitrary biased composition (PROVED)

Let f=F(g_1,...,g_m) on disjoint blocks. Write b_j=E g_j, v_j=1-b_j², c_j(T)=ĝ_j(T), and

    K_A = sum_{B containing A} F̂(B) product_{j in B\A} b_j.

For a spectral index T=(T_1,...,T_m), put A={j:T_j nonempty}. Then

    f̂(T) = K_A product_{j in A} c_j(T_j).

Proof: substitute each inner Fourier expansion into the multilinear expansion of F. Inactive blocks contribute their constant term; active blocks must supply the specified nonconstant character. Collect outer supersets of A. Squaring and summing within a pattern gives

    p_A = K_A² product_{j in A} v_j,
    H(f) = H(p) + sum_j P_p[j in A] H( c_j(T)²/v_j : T nonempty ).

The conditional entropy in this formula equals

    (H(g_j) - eta(b_j²))/v_j + log2 v_j,
    eta(t)=-t log2 t, eta(0)=0.

A constant inner block has no active patterns, so its conditional term is omitted.

For an inner coordinate i in block j, write c=c_j({i}), delta=Inf_i(g_j),

    L_j = sum_{B subset [m]\{j}} K_{B+j}² product_{l in B} v_l,
    Phi(p,q) = eta(p)+eta(q)-eta(p+q),
    phi(a,b) = eta(a²)+eta(b²)-eta((a+b)²)/2-eta((a-b)²)/2.

Then the exact formulas are

    Inf_i(f) = L_j delta,
    f̂({i}) = K_{ {j} } c,
    E_i(f) = L_j [ E_i(g_j)-Phi(b_j²,c²) ]
             + sum_B product_{l in B}v_l Phi(K_B², K_{B+j}² c²),
    D_i(f) = L_j [ D_i(g_j)-phi(b_j,c) ]
             + sum_B product_{l in B}v_l phi(K_B, K_{B+j} c).

Proof: fix the nonempty spectral blocks B outside j. If the remaining spectral index inside j, excluding i, is nonempty, both ends of the i-edge use K_{B+j}. Sum these contributions using degree-two homogeneity of Phi and phi. The missing inner edge at empty remainder originally had amplitudes (b_j,c); replace it by (K_B,K_{B+j}c). Sum the outside products. Parseval for the derivative gives the influence formula. Finally H^-=sum_i E_i. No composite truth table is required, even at three or more levels.

CHECKED: validate.py checks these quantities against independently assembled composite truth tables, including biased and constant inner blocks, to tolerance 1e-12. See validation.json for counts and residuals. The formulas are exact; floating-point evaluation is not exact arithmetic.

Balanced identical inner functions give K_A=F̂(A), L_j=Inf_j(F), and H(f)=H(F)+I(F)H(g), I(f)=I(F)I(g). The E,D formulas still retain a boundary correction involving the singleton coefficient c. Knowing H,I,H^- alone is insufficient.

## 2. Tribes at arbitrary width and count (PROVED)

Let f be OR of s disjoint width-w ANDs, with either global output sign. Set delta=2^-w, a=1-delta, q=a^s, b=2q-1,

    d=2 delta a^(s-1), c=d, p=c²,
    M=4q(1-q), K=4s delta q, n=ws.

Then every coordinate has influence d and

    H = eta(b²)-2M-2(log2 delta-log2 a)K-2s(log2 a)M,
    E = 2d(1-2delta) + (2delta d-p) Phi((a/delta)²,1) + Phi(b²,p),
    D = 4d(1-2delta) + (2delta d-p) phi(a/delta,1) + phi(b,c).

Thus H/I=H/(nd), H^-/I=E/d, R=D/d. To prove this, a nonempty spectral set touching k tribes has squared coefficient 4 delta^(2k) a^(2(s-k)). Summing over its block patterns gives total nonempty mass M and weighted number of touched tribes K. Edges whose remainder meets i's tribe have equal squared coefficients, giving erasure/influence 2 and D/influence 4. On the other edges their amplitude ratio is a/delta; the exceptional edge at the empty set uses b,c. This gives the displayed sums.

Fixed w, s→infinity (PROVED):

    H/I → 4a - 4a² log2(a)/(w delta),
    H^-/I → 2(1-2delta)+2delta Phi((a/delta)²,1),
    R → 4(1-2delta)+2delta phi(a/delta,1).

Use M/q→4, K/q=4s delta and I/q=2sw delta/a; the empty-edge term divided by influence tends to zero. For w→infinity on balanced tribes (s delta→ln 2), H/I→4, H^-/I→2, R→4. For fixed s and w→infinity the same limits hold.

For all s (PROVED), H/I≤4a-4a² log2(a)/(w delta)≤4+4/(w ln 2). To see the first inequality, divide the exact entropy by I and subtract its fixed-width limit. The remainder is

    4a q log2(a)/(w delta) + a[eta(b²)/q-8(1-q)]/(2sw delta),

which is nonpositive: eta(b²)≤(1-b²)/ln 2=4q(1-q)/ln 2. For w≥2, a corresponding uniform erasure bound is

    H^-/I ≤ 2 + 8w delta + 4delta/ln 2,
    R ≤ H^-/I + 2/ln 2.

Indeed discard negative terms in E/d; Phi(r²,1)≤log2(r²)+1/ln 2 with r=a/delta, and Phi(b²,d²)/d≤h(d²)/d≤d[log2(1/d²)+1/ln 2]. Here d≤2delta and the last function increases on this interval for w≥2. These bounds control large widths without underflow.

## 3. Parity, majority, bent, address and products (PROVED)

If f(-x)=±f(x), Fourier support has a single degree parity. Therefore every i-edge has a zero endpoint: E_i=D_i=0. This applies to odd majority and to compositions entirely of odd gates. In recursive odd majority, H_d/I_d=H(g)/(I(g)-1)*(1-I(g)^(-d)) and H^-=R=0. The singleton coefficient decays as c(g)^d.

For any bent function on even n, mu is uniform, so H=n, I=n/2, E_i=1 and D_i=2: the three ratios are 2,2,4. This covers every Maiorana–McFarland bent function f(x,y)=(-1)^(x·pi(y)+h(y)), for a permutation pi. Proof of bentness: summing over x fixes pi(y) to the frequency, leaving one term of magnitude 2^(-n/2).

For the complete quadratic q(x)=sum_{i<j} x_i x_j over F_2, its polar matrix is J+Id. It has rank n when n is even, giving the bent case; when n is odd its kernel is the all-ones vector. The spectrum is uniform on an affine hyperplane of 2^(n-1) frequencies. For n≥3 each marginal is 1/2, H=n-1,I=n/2, and each coordinate is determined by parity of the others: H/I=2-2/n, H^-/I=R=0. The n=1 case is constant and ratios are undefined.

The address function with a address bits and 2^a data bits has coefficients ±2^-a, one data bit and any address subset. Therefore H=2a, I=1+a/2. Every address coordinate has E=1, D=2, Inf=1/2; every data coordinate has E=D=0, Inf=2^-a. Thus H^-=a, sum_i D_i=2a, H^-/I=a/(1+a/2), and R=0. To count an address edge, fix the selected data bit and the other a-1 address bits: there are 2^(2a-1) equal-amplitude edges. Removing a data coordinate leaves the zero-data layer, which has zero mass.

For f=F(x) XOR g(y) (±1 product), spectra are independent products: H,I,H^- add, per-coordinate D,E,Inf are inherited unchanged, and R is the minimum of the two component R values. Thus none of the three ratios can increase past the maximum component ratio. AND is the two-input instance of Section 1, valid for arbitrary biases.

OPEN: a uniform upper bound for unrestricted Boolean functions or for every unrestricted composition family. A bounded numerical scan proves no such bound.

## 4. Stable AND/OR recursion at extremely small probabilities (PROVED)

For a transitive monotone inner function g on n bits write p=P[g=-1], d=Inf_i(g)=ĝ({i}), v=4p(1-p), b=1-2p. Store

    T_E = E_i/d - Phi(b²,d²)/d,
    T_D = D_i/d - phi(b,d)/d,
    Q = [H(g)-eta(b²)+v log2 v]/I(g).

These quantities avoid subtracting a mean rounded to ±1. For AND_k(g), let A=p^(k-1), p'=p^k, d'=Ad, n'=kn. Then

    T_E' = T_E + d(1-A) Phi((2p/d)²,1),
    T_D' = T_D + d(1-A) phi(2p/d,1),
    Q' = Q + 4p/[k n d] * [k h(p)-h(p^k)].

Proof: the nonempty outer-block edge amplitudes have ratio 2p/d; their upper squared mass is d²(A-A²). Dividing by Ad gives the first two increments. For Q, the conditional outer-block pattern is a Bernoulli(1-p) subset conditioned to be nonempty. Its entropy is [k h(p)-h(p^k)]/(1-p^k); multiply by Var(f)/(k A I(g))=4p(1-p^k)/(k I(g)). Recover

    E_i/d = T_E+Phi(b²,d²)/d,
    D_i/d = T_D+phi(b,d)/d,
    H/I = Q + [eta(b²)-v log2 v]/(nd).

For OR_k exchange p and 1-p before the AND step and exchange the output probabilities afterwards. All displayed quantities are invariant under global output negation. Dictator initialization is p=1/2,d=1,n=1,T_E=T_D=Q=0. Thus any regular AND/OR tree, including recursive tribes, has an exact scalar recursion.

CHECKED: stable_readonce.py uses 65 decimal digits for log p, log(1-p), log d and the normalized quantities, rather than for p itself. log(1-exp(x)) is evaluated with log1p or expm1. This retains probabilities whose exponents exceed ordinary floating-point range. See stable_readonce_audit.json. Exact formulas, rather than printed zero probabilities, define these functions.

## 5. Bent functions with fresh dictators (PROVED)

Let h be a bent Boolean function on m bits and P={p_1,...,p_r}. Replace h(p_j) by a fresh dictator z_j. For a core frequency S,

    a_S = ĥ(S)-2^-m sum_j h(p_j) chi_S(p_j),
    f̂(S union {z_j}) = 2^-m chi_S(p_j).

All coefficients with two fresh variables vanish. These formulas follow by writing f=h+sum_j 1[x=p_j](z_j-h(p_j)). With delta=2^-m,

    H = sum_S eta(a_S²) + r*2^m eta(delta²),
    Inf_{z_j}=delta,
    E_{z_j}=sum_S Phi(a_S²,delta²),
    D_{z_j}=sum_S phi(a_S,delta).

For a core coordinate i, use the edge sums of a_S and add r delta/2 to influence, r delta to E_i, and 2r delta to D_i. This evaluates arbitrary point sets with O(m 2^m) work, independently of the exponentially larger composite truth table.

For inner-product bent h and P the subspace with the first t coordinates free (m,t even), this compresses further. Put A=2^(-m/2), B=2^(t/2-m), l=m-t. There are 2^t(2^l±2^(l/2))/2 core frequencies with a_S²=(A∓B)². For a fixed core pair outside P, remove its two coordinates and use counts (2^(l-2)±2^((l-2)/2))/2 to form the edge sums. Free core coordinates have Inf=1/2,E=1,D=2; fixed core coordinates have Inf=1/2+r delta. The implementation bent_subspace in families.py writes the resulting two-term sums explicitly. These formulas cover m=200 and r=2^200 without allocating r dictators. At t=0, a fresh dictator has E/Inf=m+O(1), but every core coordinate has a bounded ratio; at t=m, this becomes the address function and R=0. When r/2^m→0, H/I→2, H^-/I→2 and R→4 (along even m→infinity in this subspace family).

## 6. PM(K33) tower paths (PROVED)

The base record is the nine-edge perfect-matching host with nine independent coin sites. A coin controls a cross or that cross with its central edge removed. All 18 coordinates are monotone. It is balanced, and its coordinate types are

    C: nine core coordinates, Inf=c=57/256;
    K: nine coin coordinates, Inf=c=1/256.

The construction is in composition.py:pm_gate. Its full dyadic spectrum is saved in pm_record_spectrum.npy. For each type j, let h_j(a,b) count its outer spectral edges with absolute amplitudes (a,b), and define

    L_j^E(d) = sum_{a,b} h_j(a,b) Phi(a²,b² d²)/(alpha_j d),
    L_j^D(d) = sum_{a,b} h_j(a,b) phi(a,b d)/(alpha_j d).

A leaf of depth q is indexed by a word w in {C,K}^q, written from the bottom gate to the root. It has multiplicity 9^q and influence d_w=product alpha_{w_t}. Exactly

    E_w/Inf_w = sum_{t=1}^q L_{w_t}^E(product_{u<t} alpha_{w_u}),
    D_w/Inf_w = sum_{t=1}^q L_{w_t}^D(product_{u<t} alpha_{w_u}).

These are the exact coordinate-orbit formulas, including enormous depths whose orbit list cannot be expanded. Distinct words need not give distinct numerical ratios; grouping solely by the number of C letters gives a mean E ratio and minimum D ratio, not a single orbit.

Proof: specialize Section 1 to balanced inners, whose singleton coefficient equals their influence because the whole formula is monotone. The missing empty-inner edge has Phi(0,d²)=phi(0,d)=0. Each level adds exactly L_j. Influences and singleton coefficients multiply.

The minimum D can be computed with q+1 dynamic states at depth q: retain the minimum for each number of C positions. The inner influence depends only on that count, so extending any state adds the same cost for a chosen outer type. Averaging E uses exact binomial word counts, weighted by d_w. tower.py implements this recurrence independently of composition.py:compose; highprecision.py repeats it with 80-decimal arithmetic.

The tower has finite limits (PROVED). For any fixed finite outer gate, Phi(a²,b² d²) and phi(a,b d) are O(d²(1+log(1/d))) as d→0, with zero contribution if a or b vanishes. Since d≤(57/256)^(t-1), all path increments are bounded by a fixed multiple of t(57/256)^t, a summable series. The averages and path minima therefore converge. H/I tends to H(base)/(I(base)-1) by the balanced entropy recursion. CHECKED: finite-depth values and high-precision comparisons are in tower.json and highprecision.json. No numerical infinite-limit equality is asserted without a tail enclosure.

## 7. Large majority (PROVED)

For n=2r+1, the degree-(2s+1) coefficient is

    a_(2s+1)=(-1)^s [C(2r,r)/2^(2r)] C(r,s)/C(2r,2s).

One proof expands the majority derivative: it is the indicator that the other 2r variables have equal numbers of ±1; its Fourier coefficients are the central-layer Krawtchouk coefficients. The influence is n C(2r,r)/2^(2r) ~ sqrt(2n/pi). Consequently, writing t=(2s+1)/n, Stirling's formula gives the level weight

    C(n,2s+1) a_(2s+1)²
       ~ 4/[pi sqrt(2pi) n^(3/2) t^(3/2) sqrt(1-t)]

on compact subintervals of (0,1), while -log2(a²)=n h(t)+O(log n) uniformly away from the exactly treated endpoints. The uniform Stirling upper bound has the same integrable kernel after multiplying by h(t); the tails contribute O(sqrt(epsilon) log(1/epsilon)), plus O(log n/sqrt n). Taking the odd-level Riemann sum therefore gives

    lim H(MAJ_n)/I(MAJ_n)
      = (1/pi) integral_0^1 h(t)/(t^(3/2) sqrt(1-t)) dt
      = 2/ln 2.

For the last evaluation, integrate by parts using d sqrt((1-t)/t) = -dt/[2t^(3/2)sqrt(1-t)]. The remaining beta integral is 2 B(1/2,3/2)[psi(3/2)-psi(1/2)]/ln 2 = 2pi/ln 2. The erasure and minimum-drop ratios are identically zero by parity. CHECKED: majority_large.py evaluates the exact coefficient formula up to n=1,000,001 and checks the integral separately; numerical scope and Parseval residuals are in majority_large.json.

## Numerical normalization (CHECKED)

The general evaluator stores the nonempty spectral mass separately from the rounded mean. In composing, compute V_out=sum_{A nonempty} K_A² product v_j, then use eta(1-V_out)=-(1-V_out)log1p(-V_out)/ln 2 for the empty entropy. This prevents a tiny Parseval rounding error at the empty coefficient from dominating a tiny true influence. Both the native scanner and Python evaluator use this normalization. Rounded means still limit arbitrary-depth biased composition, so the specialized log-probability recursion is used for extreme AND/OR trees.

For a numerical tail enclosure in the PM tower (PROVED bound), let

    C_j^E = sum_{a,b!=0} h_j(a,b) b² log2(1+a²/b²)/alpha_j + 1/ln 2,
    C_j^D = C_j^E + 2/ln 2.

For 0<d≤1, L_j^E(d)≤d[2log2(1/d)+C_j^E], and likewise for D. This follows from Phi(p,q)≤q[log2(1+p/q)+1/ln 2] and the sharp J≤(2/ln 2)q bound. With alpha=57/256 and depth cutoff q≥1, d log(1/d) is increasing on [0,alpha^q]. Therefore both the average E ratio and the minimum D ratio have remaining tail at most

    alpha^q [ 2log2(1/alpha)(q/(1-alpha)+alpha/(1-alpha)²)
                + max_j C_j/(1-alpha) ].

CHECKED: tail_bounds.py applies this bound after depth 30 and records the finite-depth value and upper enclosure in tail_bounds.json. Logarithms are evaluated at 80 decimal digits, with independent double-precision agreement; these are not directed-rounding interval certificates.

## 8. Limits of regular recursive tribes and AND/OR trees (PROVED)

For recursive (w,s)-tribes, the output probability obeys

    p_0(r)=r, p_(d+1)(r)=G(p_d(r)),
    G(p)=1-(1-p^w)^s.

Here r is the common probability that an underlying input bit is -1; evaluation uses r=1/2. For w,s≥2 there is exactly one interior fixed point p*. Indeed G' is positive, zero at both endpoints, and has exactly one maximum: the derivative of log G' changes sign once, at p^w=(w-1)/(ws-1). Hence G-p is negative before its unique interior zero and positive afterwards; that zero has derivative G'>1. Also 1/2 is not fixed: (2^w-1)^s=2^(ws-1) would equate an odd integer greater than one to an even integer. Thus every fixed integer (w,s) starting at 1/2 polarizes to zero or one.

Let q_d be the smaller output-event probability near its limiting endpoint. Near zero, G(p)=s p^w(1+O(p^w)); near one, 1-G(1-q)=w^s q^s(1+O(q)). Write m=w or s for the corresponding escape degree. Then

    c(r)=lim_d [-log q_d(r)]/m^d >0

exists locally in that basin. This follows by dividing the logarithmic recurrence by m^(d+1); the error terms form an absolutely convergent series. Differentiating that series is valid on a compact neighborhood inside the basin after finitely many iterates. The normalized logarithmic derivative tends to |c'(r)|>0: its factors are m times 1+O(q_d^a), whose correction product converges to a positive value.

Russo's derivative identity at r=1/2 is |q_d'(1/2)|=I(f_d). Consequently I(f_d)/q_d ~ |c'(1/2)|m^d. The Q increments in Section 4 are O(m^-d) at the near-one steps and super-exponentially smaller at the near-zero steps, so Q converges to its positive-increment series Q_infinity. Recovering entropy gives the exact finite limit expression

    lim_d H(f_d)/I(f_d)
      = Q_infinity + 4c(1/2)/(|c'(1/2)| ln 2).

This is an exact series/escape-rate formula, not a claimed elementary closed form. family_limits.json evaluates the recursion at depths six and twenty; its final-step differences are observations, not certified tail bounds for this limit.

Erasure and minimum drop converge for any regular monotone AND/OR construction with each nontrivial fan-in at least two. At an intermediate level with n leaves, transitivity and monotonicity imply d=I/n≤1/sqrt(n): I=E[f sum_i x_i]≤sqrt(n). Each positive T_E or T_D increment is at most

    d[2 log2(1/d)+log2(5)+3/ln 2],

using 2p≤2, the Phi bound and the J bound. Since n grows at least geometrically along levels, these increments are summable. The final empty-edge term tends to zero, so the limiting H^-/I and R are precisely the positive series for T_E and T_D. For a transitive function R is its common D_i/Inf_i. Equal-fan-in alternating AND/OR trees are the w=s case after grouping two levels; adding a final single level changes each limiting ratio by zero. Thus every fixed recursive family in the requested survey has finite limits for all three statistics.
