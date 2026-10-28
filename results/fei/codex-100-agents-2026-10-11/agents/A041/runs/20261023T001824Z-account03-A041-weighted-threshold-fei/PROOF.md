# Scope and notation

All logarithms here are natural. Let F be an actual Boolean sign on two disjoint physical blocks A,B under an interior product law. Write P(S)=Fhat(S)^2 in the normalized biased basis, I=sum_S |S|P(S), M=sum_mixed P(S), and D=sum_mixed (|S|-1)P(S). Mixed means that S meets both blocks. These are spectral quantities; conditioning the physical input on an output is a different operation.

The previously defined canonical count-tail reference is used unchanged. For a two-weight threshold and nonempty T in B, write h_T(k)=Fhat_B(T;N_A=k)/sqrt(v_T)=constant+sum_j alpha_Tj g_j(A), where g_j=2*1{N_A>=j}-1. Set K_A(U,T)=v_T sum_j alpha_Tj^2 ghat_j(U)^2 and define K_B with the blocks reversed. K*=max(K_A,K_B) is summed on the COMPLETE mixed label space, including P=0 labels. Z=sum K*, C*=sum P ln(1/K*), R=P/M, Q=K*/Z when M>0. The prior exact identity is E_mix=C*+M ln(Z/M)-M KL(R||Q), with Z<=D+M<=2D. No new Boolean-admission assumption is imposed on Q.

# 1. General physical pivotal-cap bank

This part holds for EVERY Boolean sign F, without monotonicity or a threshold assumption. For i in A let d_i=(F(X_i=1)-F(X_i=-1))/2, and q_i(x_(A\i))=E_B[d_i^2]. Set beta_i=max q_i, and reverse the blocks for i in B. Let v_i=4p_i(1-p_i). Then

    I_i=v_i E[d_i^2],
    I_pure=sum_i v_i E[(E_opposite d_i)^2].

The second equality follows from Parseval applied to the conditional expectation of F onto each physical block and then its derivative. Since d_i belongs to {0,1,-1}, |E_opposite d_i|<=E_opposite |d_i|=q_i. Thus (E_opposite d_i)^2<=q_i^2<=beta_i q_i. Summing proves

    I_pure <= sum_i beta_i I_i,
    I_mix >= sum_i (1-beta_i) I_i,
    D >= (1/2) sum_i (1-beta_i) I_i.                 (1)

For the last line every mixed label has degree at least two, so D=I_mix-M>=I_mix/2. In particular beta_i<=beta<1 gives D>=(1-beta)I/2. There is no assertion that a uniform beta<1 holds on all biased thresholds. This is a physical pivotal PROBABILITY cap, not a unit-credit bound on a logarithmic charge.

# 2. An actual threshold family with unbounded pointwise coherence

For m>=1 take |A|=|B|=m and F_m=2*1{N_A+N_B>=m+1}-1. It has a genuine unequal two-weight representation: assign weight 1+epsilon to A, weight 1 to B, and threshold m+1, where 0<epsilon<1/m. The function itself remains symmetric. Everything in this section holds at every labelled interior product bias.

Let S=A union B be the full label, v_S=product_i v_i, V=binom(2m-1,m-1), w_d=binom(m-1,d)binom(m,m-1-d) for d=0,...,m-1, and W=sum_d w_d^2. Then

    P(S)=v_S V^2 / 4^(2m-1),
    K_A(S)=K_B(S)=v_S W / 4^(2m-1).              (2)

To check (2) without assuming fair biases: the normalized full Fourier coefficient is sqrt(v_S) times the full discrete difference divided by 2^(2m). For a sign threshold at count k that difference has magnitude 2 binom(2m-1,k-1). The same difference calculation on each block gives each canonical tail contribution magnitude sqrt(v_S)*w_d/2^(2m-1), in reversed count order if necessary. Their signs agree. Squaring before summation gives K; squaring their sum gives P. All bias factors are common and cancel in P/K*. Vandermonde gives sum w_d=V. Thus

    P(S)/K*(S)=1/sum_d q_d^2,  q_d=w_d/V.       (3)

This is the reciprocal collision probability of a hypergeometric law, not an asymptotic heuristic. For m=3 the exact ratio is 100/46=50/23>2. This does not contradict the previously proved sharp factor two for TWO-jump profiles: this example has three jumps.

Here is an elementary all-m lower bound. Put c_r=binom(2r,r)/4^r. Induction using c_(r+1)/c_r=(2r+1)/(2r+2) proves c_r^2>=1/(4r) for r>=1 and c_r^2<=1/(r+1) for r>=0. The lower induction uses ((2r+1)/(2r+2))^2>=r/(r+1); the upper uses the reverse comparison with (r+1)/(r+2). Consequently each binomial row satisfies binom(N,k)^2<=4^N/(floor(N/2)+1). Also V^2=binom(2m,m)^2/4>=4^(2m)/(16m). Hence

    max_d q_d^2 <= 4m/[(floor((m-1)/2)+1)(floor(m/2)+1)] <=16/m.

Because sum q_d^2<=max q_d, equation (3) yields (P/K*)^2>=m/16, or P/K*>=sqrt(m)/4. Therefore no arity-independent pointwise domination P<=c K* is possible for these actual thresholds. This is an obstruction to this reference domination mechanism, not a counterexample to FEI or FEI+.

# 3. The averaged reference payment survives on fair balanced controls

ONLY in this section all inputs are fair. A pivotal event for any coordinate requires that the other 2m-1 bits contain exactly m ones. Averaging its indicator over the opposite block gives a single Binomial(m,1/2) atom or zero. Its maximum a_m is at most 1/2: convolution with a fair bit cannot increase a distribution's largest atom, starting from a_1=1/2. Apply (1) to obtain I_pure<=I/2 and D>=I/4. The exact influence is

    I=2m*binom(2m-1,m)/2^(2m-1)=2m c_m>=sqrt(m).

Canonical Cauchy on at most m nonzero tails gives P<=m K_A<=m K*. Let Gamma=sum_mixed P [ln(P/K*)]_+. Therefore Gamma<=M ln m<=ln m. The elementary maximum of ln x/sqrt(x) is 2/e (or apply ln y<=y-1 to y=sqrt(x)/e), giving

    Gamma <= (8/e)D <3D.                       (4)

The supplied uniform threshold theorem A gives H_bits(F)<9 I, hence E_mix<=H_nats(F)<9 ln(2) I<=36 ln(2)D. As C*=E_mix+sum P ln(P/K*), (4) proves

    C* < (36 ln(2)+8/e)D <28D.                 (5)

For a rational check of the final numerical comparison, ln2<25/36 follows from the atanh series at 1/3 (first two terms 56/81 and tail at most 1/540), and e>8/3 from the first four terms and positive remaining terms. The entropy bound used here is a known uniform-threshold theorem; (5) is a stress test and payment for this complete reference, not a new proof of uniform-threshold FEI. It pays both retained terminal spectral entropy and coherence with the SAME D. There is no sum of local renewed root budgets and no erasure of off-support reference atoms.

# 4. Independent reconstruction of the new rational-admission obstruction

Source A045-RATIONAL-MEAN-CONDITIONING-ADMISSION-OBSTRUCTION@1, exact statement SHA256 f1b8daa6656f1a9aab06f61363d05dcdc5fd3beda9b808b29348a41c90bad341. For fair AND on d>=2, put a=2^(d-1). The empty squared coefficient is (a-1)^2/a^2; every nonempty label has mass 1/a^2. Retain empty and r nonempty labels, 1<=r<=2a-2. After normalization Q(empty)=(a-1)^2/((a-1)^2+r). The denominator is strictly between consecutive squares (a-1)^2 and a^2, so its square root is irrational. A nonzero rational numerator divided by that root stays irrational. Thus sqrt(Q(empty)) is irrational. Every Boolean mean under any FINITE rational product-bias law is rational, a finite sum of rational input probabilities times signs. No choice of Fourier phases, dimension or new rational product biases can admit Q as a Boolean spectrum while preserving the empty label. Both endpoints are admitted; irrational biases are excluded from this theorem. For d=2,r=1, the resulting (1/2,1/2) spectrum is admitted by a one-bit sign at p=(1+1/sqrt(2))/2. This is not a prohibition on using Q as a non-Boolean reference and not a claim about removing the empty label. No substantive source repair was needed.

# 5. Exact open line and preserved scopes

For arbitrary real weighted thresholds and arbitrary interior biases, the first unsupported line remains

    C* - M KL(R||Q) <= K D

for an absolute K and a suitable complete actual-gate reference (with the count-tail reference above currently defined only for two weight groups). Equation (1) gives a useful bank only when its physical caps leave reserve; it does not pay Gamma in general. Equation (3) decisively rules out replacing this open averaged estimate by a uniform pointwise multiplier. The next mechanism must keep the average profile likelihood and the KL cancellation, with gate-specific physical derivative reserve. The recovered OR(heavy,AND(light)) controls and their coefficient-one pivotal-credit failure remain valid; none of (1)-(5) repairs that coefficient-one claim or establishes its failure for all larger constants. Conditional-input total correlation, spectral total correlation and spectral good-coordinate erasure remain three distinct quantities. The full FEI conjecture is OPEN.
