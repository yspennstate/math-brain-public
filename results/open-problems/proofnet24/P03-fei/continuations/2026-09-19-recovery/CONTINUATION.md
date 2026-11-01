# FEI continuation: collision-free support patching and the spectral-distance boundary

19 September 2026. Owner-requested continuation of the recovered FEI session.

**Status: PARTIAL. The unrestricted Friedgut–Kalai conjecture is not proved here.** The statements below have written proofs and finite checks, but have not received independent audits or proof-assistant verification. They are improvements to the recovered repository arguments; publication novelty is not asserted. In particular, the partition argument uses an established asymptotic-equipartition method and must be attributed accordingly.

Read the [recovery handoff](../../handoffs/2026-09-19__FROZEN_SESSION_RECOVERY.md) first. It flags the false pointwise erasure inequality in an older handoff. That inequality is not used below.

## 0. Main changes and conventions

For a Boolean f on a uniform cube, put p_f(S)=fhat(S)^2, H(f)=sum_S p_f(S) log_2(1/p_f(S)), and I(f)=sum_S |S|p_f(S). All entropies and KL divergences below use bits. A singleton Fourier support has separation infinity and entropy zero.

The substantive changes are:

1. **Collision-free subcube patching.** For a partition into selector subcubes on each of which f is a signed parity of the selector and data variables, H(f)<=2H(J), with arbitrary repeated parity labels and arbitrary interference. Under the previously defined boundary-separation hypothesis, H(f)<=4 I_x(f). Neither a bound on Lambda nor flatness of the incoherent group mixtures is needed. The proof is an application/extension of the published partition-entropy method, not a new proof method claimed here.
2. **Every sublinear erasure scale retains the full FEI constant.** The earlier o(N/log N) coding regime improves to every k_N=o(N), using redundancy O(k_N log(N/k_N)). The statement also holds for an arbitrary prescribed sublinear profile in the *final* dimension.
3. **A complementary positive separation bound.** If the Fourier support has M>=2 points and minimum Hamming distance d, then

       H(f) <= [2 + 2 log_2(M)/d] I(f).

   In particular d>=delta*n gives H(f)<=(2+2/delta)I(f). Thus fixed positive relative separation and merely sublinear separation behave differently in this reduction.
4. **General signed-interference identity.** For non-subcube cells, retain the entropy-excess correction rather than replacing it by a worst-case collision multiplier. Its exact sign, a quasi-flat estimate, and the remaining unpaid term are recorded in Section 4.

These changes do not advance or reset the separate native P03 finite-dimension atlas. Its latest certified value must be recovered from its own current report. No schedule is altered by this research note.

## 1. Collision-free support patching

### 1.1 An orthogonal support lemma

Let u_1,...,u_t be nonzero, pairwise orthogonal functions on a fixed n-dimensional cube, normalized so that sum_j ||u_j||_2^2=1. Set f=sum_j u_j, delta_j=||u_j||_2^2, and M_j=|supp(uhat_j)|. The functions may be real-valued; f need only have L2 norm one. Then

       H(fhat^2) <= H(delta) + sum_j delta_j log_2 M_j.                 (1)

**Proof.** Set a=H(delta) and b=sum delta_j log_2 M_j. For a positive integer m, expand the tensor power f^{tensor m} as the sum of tensor products u_{j_1} tensor ... tensor u_{j_m}. These products are orthogonal, and their squared norms are delta_{j_1}...delta_{j_m}.

For fixed epsilon>0, retain those tuples for which both

       |m^{-1} sum_l (-log_2 delta_{j_l}) - a| <= epsilon,
       |m^{-1} sum_l log_2 M_{j_l} - b| <= epsilon.

Under independent sampling from delta, their probability tends to one by the ordinary law of large numbers. Write alpha_m for the omitted probability. Every retained tuple has probability at least 2^{-m(a+epsilon)}, so there are at most 2^{m(a+epsilon)} such tuples. Each corresponding tensor product has at most 2^{m(b+epsilon)} Fourier coefficients. The union U_m of their Fourier supports consequently has cardinality at most 2^{m(a+b+2epsilon)}.

Let g_m be the retained sum. Orthogonality gives ||f^{tensor m}-g_m||_2^2=alpha_m. Since ghat_m vanishes outside U_m, Parseval implies that the spectral probability of f^{tensor m} outside U_m is at most alpha_m. A distribution on 2^{nm} points with mass beta_m outside U_m has entropy at most

       1 + log_2 |U_m| + beta_m*n*m.

The entropy on the left is m H(fhat^2). Divide by m, take m to infinity, and then epsilon down to zero. This proves (1). No control of pointwise interference has been used. QED.

**Attribution.** This is the tensor-typical-support mechanism used for partition entropy by Arunachalam, Chakraborty, Koucky, Saurabh and de Wolf, *Improved bounds on Fourier entropy and Min-entropy*, arXiv:1809.09819, Sections 3.1 and 3.1.1 (v2, 17 September 2021): https://arxiv.org/html/1809.09819v2 . Their published theorem H(f)<=2 aUC^oplus(f) and its proof are essential prior art. The formulation (1) is written out here to check exactly how signed parity pieces fit the existing FEI track. Do not present the underlying method as newly discovered.

### 1.2 Arbitrarily repeated subcube-parity labels

Let x be selector variables and y data variables. Let C_j partition the selector cube into subcubes of codimension r_j, with delta_j=2^{-r_j}. On C_j suppose

       f(x,y) = epsilon_j chi_{T_j}(x) chi_{D_j}(y),
       epsilon_j in {-1,1}.

The sets T_j and D_j and their repetitions are unrestricted. Put

       u_j = epsilon_j 1_{C_j} chi_{T_j} chi_{D_j}.

These pieces have disjoint physical supports and squared norms delta_j. The Fourier support of 1_{C_j} has exactly 2^{r_j} points. Multiplication by a character merely translates it, including in the data coordinates. Hence M_j=2^{r_j}. Applying (1), and using H(J)=sum delta_j r_j, gives

       H(f) <= 2 H(J).                                               (2)

In particular, refining each data parity into two monochromatic cells is unnecessary; it would introduce an avoidable additive cost. The support argument treats that parity as a single Fourier translation.

For each selector edge x--x^{(i)} crossing between distinct cells, assume the two y-fibers of f are not identical. Since each fiber is a signed character, they disagree with probability at least 1/2 under uniform y. A point in C_j has exactly r_j selector neighbors outside C_j. Consequently

       H(J) = sum_i P[J(x) != J(x^{(i)})] <= 2 I_x(f).

Combining with (2) proves

       H(f) <= 4 I_x(f) <= 4 I(f).                                  (3)

This supersedes the earlier 4*Lambda*I_x estimate for this class, including nonflat group mixtures and unbounded repeated-label multiplicity. It does **not** establish that an arbitrary Boolean function has a representation satisfying the hypotheses.

### 1.3 The exact physical-boundary debt

Without boundary separation, define

       A = sum_i P[J(x)!=J(x^{(i)}) and the two y-fibers are identical].

All other crossing edges cost at least 1/2 in selector influence. Thus H(J)<=2I_x(f)+A, and (2) gives

       H(f) <= 4I_x(f)+2A.                                          (4)

The missing universal step is not a worst-case collision estimate in this subcube class. It is a representation with the artificial-boundary cost A controlled by genuine influence, or another valid way of avoiding that cost. Merging identical neighboring fibers can produce cells that are not subcubes, so it does not automatically preserve the argument.

### 1.4 Concrete checks

For f(a,b,y)=Address_s(a,y)*chi_[r](b), use point cells in (a,b) and group them by the address. Then

       H(f)=2s, I_x(f)=s/2+r, Lambda=2^r.

The old multiplier can diverge while (2)--(3) remain valid. The checker evaluates s=2 and r=0,...,4 exactly.

A nonflat repeated-label example uses selector subcubes 0**,10*,110,111, signs +,+,+,- and data labels y_1,y_2,y_3,y_1. Here H(J)=7/4, I_x=1, Lambda=25/17, and H(f) is approximately 3.240222972541423, below 2H(J)=7/2. The normalized incoherent law for the repeated label is not flat. The inequality is checked using rational logarithm enclosures, not a floating-point acceptance test.

## 2. Constant-preserving coding at every sublinear scale

### 2.1 A near-rate-one systematic code

Let 1<=k=k_N=o(N), and set

       L=log_2(eN/k), r=ceil(2kL).

Then r=o(N), and eventually r<=N. Choose a uniformly random binary r-by-N matrix A. For each fixed nonzero s, As is uniform on F_2^r. Therefore

 P[there exists s!=0 with |s|+|As|<=k]
 <= 2^{-r} sum_{j=1}^k binom(N,j) sum_{ell=0}^{k-j} binom(r,ell)
 <= 2^{-r} sum_{h=0}^k binom(N+r,h).

For k<=(N+r)/2, the Hamming-ball bound gives

       sum_{h=0}^k binom(N+r,h) <= [e(N+r)/k]^k.

One proof bounds the sum by 2^{(N+r)h_2(k/(N+r))} and uses -(1-q)ln(1-q)<=q. Since N+r<=2N, the failure probability is at most

       2^{-2kL} (2eN/k)^k = 2^{-k(L-1)} < 1.

Thus some A has systematic code C_A={(s,As):s in F_2^N} of minimum distance greater than k, with redundancy

       r=O(k log(N/k))=o(N).                                        (5)

This replaces the recovered note's coarser O(k log N) estimate. Random linear coding and Hamming-ball bounds are standard; the new item for this track is the larger range in the constant-preserving FEI reduction.

### 2.2 The exact Boolean Fourier lift

For a Boolean h on F_2^N define

       F_A(x,z)=h(x+A^T z).

Expanding in characters shows that each Fourier coefficient hhat(s) is moved to the single location (s,As). No coefficients merge because the map is systematic. Thus

       H(F_A)=H(h),
       I(F_A)=I(h)+sum_s hhat(s)^2 |As|,
       I(h)<=I(F_A)<=I(h)+r.                                       (6)

The Fourier support inherits the code distance. If X is its spectral sample and T is any block of at most k coordinates, then

       H(X_T | X_{T^c})=0.                                          (7)

Indeed two support points agreeing outside T would have distance at most k, which is impossible. This holds simultaneously for every such block, not merely blocks chosen in advance.

### 2.3 Equality of the unrestricted and separated worst constants

Let C_FEI be the supremum H(g)/I(g) over all nonconstant Boolean functions in all dimensions, allowing infinity. Fix a nonconstant g on n variables, and use h=g^{tensor m}, N=mn. Then H(h)=mH(g), I(h)=mI(g). Equations (5)--(6) imply

       H(F_A)/I(F_A) -> H(g)/I(g).

Consequently every sublinear separation requirement preserves the unrestricted worst ratio in a dimension-unbounded supremum.

For precision when the requirement is specified in the FINAL dimension, let (k_D) be any nonnegative integer sequence with k_D=o(D), without a monotonicity assumption. For each message dimension N set

       K_N=max(1, max_{N<=D<=2N} k_D).

Then K_N=o(N). Apply (5) with k=K_N and take D=N+r. Eventually D<=2N, so the resulting spectrum has distance greater than k_D. It follows that

 limsup_{D->infinity} sup {H(f)/I(f): f Boolean on D bits, I(f)>0,
                         distance(supp fhat)>k_D} = C_FEI.           (8)

The upper inequality is definitional; the lower inequality follows along the constructed dimensions for every fixed g. The same argument applies when C_FEI is infinite by first fixing an arbitrarily large witnessed ratio.

Examples allowed by (8) include k_D=floor(D/log log D) for sufficiently large D. Nothing here proves or disproves finiteness of C_FEI. In particular (7) does not invalidate the correctly quantified universal implication from erasure bounds to FEI, because physical restrictions can destroy code separation.

### 2.4 Why this redundancy scale is natural

If a binary systematic linear code has length D=N+r and distance greater than k, disjoint balls of radius t=floor(k/2) give

       2^r >= sum_{j=0}^t binom(D,j).

For t>=1 this implies r>=t log_2(N/t). Puncturing any k coordinates also gives r>=k. Thus, away from the trivial k=1 endpoint, the order k log(N/k) is correct up to constants in the small-relative-distance regime. A fixed positive relative distance requires a positive-order redundancy. This is a limitation of the vanishing-redundancy argument, not an impossibility theorem for every conceivable FEI transformation.

## 3. Positive FEI bounds from spectral separation

### 3.1 An atom-entropy lemma

For every Boolean f and every Fourier atom p_S=fhat(S)^2,

       h_2(p_S) <= 2I(f).                                           (9)

Here h_2 is binary entropy.

For S nonempty, choose i in S. Writing D_i f=(f(x)-f(x^{(i)}))/2 gives

       |fhat(S)|=|E[D_i f chi_S]|<=E|D_i f|=I_i(f).

The elementary scalar inequality h_2(a^2)<=2a for 0<=a<=1 finishes this case. For completeness, if a>=1/2 use h_2<=1. For a<=1/2, the usual entropy bound gives

       h_2(a^2)/a <= a(1-2ln a)/ln 2 <= (1+2ln 2)/(2ln 2) <= 2.

The middle inequality follows by monotonicity of a(1-2ln a) on (0,1/2].

For S empty let alpha=min(P[f=1],P[f=-1]) and v=1-fhat(empty)^2=4alpha(1-alpha). The cube edge-isoperimetric inequality gives I(f)>=2alpha log_2(1/alpha). If alpha<=1/4 then 3alpha<=v<=4alpha, and

 h_2(v)<=v log_2(1/v)+v/ln 2
       <=4alpha[log_2(1/alpha)-log_2 3+1/ln 2]
       <=4alpha log_2(1/alpha)<=2I(f).

If 1/4<=alpha<=1/2, then 4alpha log_2(1/alpha)>=1>=h_2(v). The constant case is immediate.

The edge inequality used here can be established without FEI: an m-vertex subset of a cube has at most (m log_2 m)/2 internal edges. Induct on cube dimension, splitting into parts of sizes a,b and bounding the matching edges by min(a,b); the required scalar inequality is h_2(a/(a+b))>=2min(a,b)/(a+b), a consequence of concavity. Subtract internal edges from total incident edges to obtain the stated boundary estimate.

The empty-atom entropy cost is closely related to the standard 2I overhead in Wan, Wright and Wu, *Decision Trees, Protocols, and the Fourier Entropy-Influence Conjecture*, arXiv:1312.3003, Lemma 1.5: https://arxiv.org/html/1312.3003v1 . No novelty claim is made for (9).

### 3.2 Separation theorem

Suppose M=|supp fhat|>=2 and its minimum Hamming distance is d. There is at most one support point of weight strictly less than d/2.

If there is none, I(f)>=d/2, and H(f)<=log_2 M gives H(f)<=(2log_2 M/d)I(f).

Otherwise let S_* be that unique point, p_*=p_f(S_*), q=1-p_*. Every other point has weight at least d/2. Therefore q<=2I(f)/d. Splitting the entropy at S_* and applying (9),

       H(f)=h_2(p_*)+q H(X | X!=S_*)
           <=2I(f)+q log_2(M-1)
           <=[2+2log_2(M)/d]I(f).                                  (10)

This proves the claimed bound in all cases. The result uses pairwise separation, not an unjustified assumption that the empty Fourier coefficient belongs to the support.

Since log_2 M<=n, distance at least delta*n gives the dimension-free constant 2+2/delta. More generally distance at least delta*log_2 M suffices for the same constant.

The contrast with (8) is precise: every prescribed sublinear distance scale retains the unrestricted optimal constant, whereas a fixed positive relative separation yields a bound depending only on that separation fraction. This is not a proof for the missing low-separation class. Publication priority for this elementary consequence has not been established.

## 4. Entropy-sensitive interference for general signed cells

Return to the more general setup in INTERFERENCE_PATCHING_THEOREM_2026-09-18.md. Put v_j=1_{C_j}sigma_j, delta_j=||v_j||_2^2, and f(x,y)=sum_j v_j(x)chi_{D_j}(y), with disjoint cells but otherwise arbitrary signs. For a parity label A let G_A={j:D_j=A}, delta_A=sum_{j in G_A}delta_j, and

 q_A(S)=(sum_{j in G_A} vhat_j(S))^2/delta_A,
 m_A(S)=sum_{j in G_A} vhat_j(S)^2/delta_A.

Both are probability distributions by disjoint-support orthogonality, and q_A is supported where m_A>0. Let E_j=H(vhat_j^2/delta_j). Under the joint law P(J=j,S)=vhat_j(S)^2, write L=D_J. Direct entropy accounting gives the EXACT identity

 H(f)=H(J)+sum_j delta_j E_j-H(J|L,S)
      +sum_A delta_A Delta_A,
 Delta_A=H(q_A)-H(m_A)
        =sum_S (q_A-m_A)(-log_2 m_A)-D_2(q_A||m_A).                 (11)

This retains both the sign of the entropy change and the nonnegative mixing slack. Neither term may be silently discarded in a direction that weakens an upper bound incorrectly.

Let t_A=TV(q_A,m_A), M_A=|supp m_A| and

       R_A=log_2(max_S m_A(S)/min_{m_A(S)>0} m_A(S)).

Centering the bounded surprisal variable gives a covariance upper bound R_A t_A. Pinsker's inequality in bits gives D_2(q_A||m_A)>=(2/ln 2)t_A^2. Thus

 Delta_A <= R_A t_A-(2/ln 2)t_A^2 <= (ln 2/8)R_A^2.

Also Delta_A<=log_2 M_A-H(m_A). Consequently, with

       epsilon_A=min(log_2 M_A-H(m_A), (ln 2/8)R_A^2),

we have

       H(f)<=H(J)+sum_j delta_j E_j+sum_A delta_A epsilon_A.          (12)

Pinsker's form follows by grouping the positive and negative parts of q-m (log-sum inequality) and using the binary relative-entropy curvature bound 1/[u(1-u)]>=4; after conversion from natural logarithms this gives the stated constant.

For flat m_A, Delta_A=-D_2(q_A||m_A)<=0 exactly. But Section 1 is stronger for subcube-parity pieces: it does not need flat m_A at all. Equation (12) remains useful for nonflat, non-subcube cells where local spectral entropy is much smaller than log support size.

Under the earlier boundary-separation and local hypotheses E_j<=C D(v_j)/delta_j, with D(v)=sum |S|vhat(S)^2, the existing physical estimates give

       H(f)<=(C+2)I_x(f)+sum_A delta_A epsilon_A.                     (13)

The last sum is **not** proved universally bounded by influence. Controlling it, or exploiting the negative and conditional-entropy terms in (11), is a concrete remaining route. Replacing log M_j by E_j in (1) for arbitrary orthogonal pieces is not justified by its proof: spectral truncations of distinct pieces need not stay orthogonal.

## 5. Checks, limitations and next useful work

Run `python3 check_recovery.py > checks.json` in this directory. The checker uses only the Python standard library. Fourier transforms, spectral probabilities, code distances and erasure injectivity are exact. Logarithms needed for finite entropy inequalities are enclosed with rational atanh-series bounds.

The executed checks cover all 276 Boolean functions in dimensions 1--3, 128 deterministic-seed samples in dimension 4, and 3205 spectral-atom inequalities. Two systematic lifts have exact minimum distances 3 and 4, with every erasure block of size at most 2 and 3 checked respectively (37 and 378 blocks). Additional exact Hamming-volume inequalities and repeated-label examples pass. This is finite verification, not an independent proof audit, Lean verification, a full-dimensional enumeration, or a proof of FEI.

For continuation:

- Do not spend further effort bounding Lambda for boundary-separated subcube-parity pieces: (1)--(3) already remove it. Investigate boundary debt and general-cell compression instead.
- Test a genuinely new general-cell strategy against (8): even all sublinear spectral-block erasures can vanish at ratios approaching the unrestricted supremum.
- Preserve the exact logarithmic K(f)<=C I(f) target and the correctly quantified hereditary erasure reduction from the recovered work. Never reinstate the false pointwise H<=B+(2/ln 2)I claim.
- Audit (1), (8), (9)--(10), the physical boundary normalization, and prior-art scope before promoting any statement to a manuscript or a solved-problem ledger.

The global missing assertion remains a finite universal bound for H(f)/I(f) on every Boolean function. No such bound has been established in this continuation.
