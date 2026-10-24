# FEI continuation: sharp kernel contraction, and why the full-line closing estimate fails

21 September 2026. Interactive account02 continuation, not a scheduled B-slot.

**Read `HALFBAND_COLLISION_EXTENSION.md` after this report.** The later extension proves excessive positive current even at the finite HALF-BAND live cutoff, strengthening the staged results below. It does not refute FEI or a signed ledger retaining compensating credits.

**Full uniform-cube FEI is NOT PROVED by this work.** The analytic statements below are self-checked, pending independent review; no publication-priority claim is made. This run first proves a sharper universal kernel theorem, then disproves the proposed influence payment for its full-line source bank using genuine Boolean functions, the retained Reed--Muller code, and the actual active-syndrome distribution. The valid predecessor identities are not withdrawn.

Model: GPT-6 Astra Pro, self-report. Configured reasoning effort and provider thinking counters: NOT_EXPOSED. Native `math_brain`, `brain`, and `spread_recall` were unavailable: WITHOUT_VERIFIED_BRAIN. Repository retrieval/delivery is not native brain ingestion.

## 0. Exact source dependencies and change to the full-proof plan

Sources recovered at scientific master `1d89e593ebdfded8b525eb110ee656071a9298cb`, paths relative to `proofnet24/P03-fei/`:

* account02/B18 `fleet-2026-09-21/account02/B18/20260921T200356Z-restriction-kernel-polarization/REPORT.md`, blob `f139911380f55a0dc715c4d00463b2e33a2ab947`: the Shannon/phase PSD split, the phase-to-Brownian comparison, the authentic squared-current identity, and two unpaid bank bounds.
* account01/B16 `fleet-2026-09-21/account01/B16/20260921T195223Z-square-first-window-gram/REPORT.md`, blob `ebd532a214b9b4a293363578e0237fce636bab68`: squared window domination and four-sine kernel.
* account04/B16 `fleet-2026-09-21/account04/B16/20260921T184003Z-phase-switch-dirichlet/REPORT.md`, blob `10db31ceb4c2861a014178573c0fc03a1f1f2dc0`: the UNIFORM ACTIVE-syndrome law, not a uniform law over every Boolean phase, and the exact current multipliers.
* account04/B16 `fleet-2026-09-21/account04/B16/20260921T111531Z-shapley-plaquette-bridge/REPORT.md`, blob `8f8736715bbef5a2f2619773e9afdbee1e8dbf4d`: ordered-min q-flip duals are the actual descendant subcube masks.
* account04/B16 `fleet-2026-09-21/account04/B16/20260921T191216Z-local-triple-curvature-flag/REPORT.md`, blob `7f15b21004f2285f2902d92ee3c852554b64097e`: fine slice clones and genuine doubled-parent current.
* `runs/2026-09-15/2026-09-15_20-29-28__run-report.md`, blob `6cbde473c8887b4cfbd68d0b4aa29bfae7b8beb2`: retained terminal convention D_d=RM(d,D)^perp and the distinction between a signed endpoint and positive expenditure.

A later source check also consumed account01/B16 `fleet-2026-09-21/account01/B16/20260921T204046Z-terminal-shell-feature-projector/REPORT.md`, blob `6fd80765ed5b10f52b8aaf2464d671bd29c41892`, at scientific snapshot `158ae3b5c632f7642138faab8ba95bb1d38c4b12`. Its retained-shell projector and same-syndrome radial identity remain valid; Section 5 below refutes its explicitly unpaid inequality (8.1), not merely the diagonal surrogate already refuted in that peer report.

The common brain control and research-state index were also read. Initial control main was `3195ed532ff368712c87111416c9fab3a5b5a0d4`, README blob `0fdb1331d25a60febce1d19645df6b71ab2a9e8c`, revision 2026-09-21.1, joint directive FEI-JOINT-FOUR-ACCOUNTS-2026-09-21-192650Z. No schedule, account binding, production state, privacy gate, or historical proof was changed.

FULL-PROBLEM CHANGE: no finite universal FEI constant is proved. MECHANISM CHANGE: the entire Shannon-plus-phase Gram bank has a sharp Brownian comparison, but its proposed universal O(J) closing estimate is false, even with actual current-sector weights. Keeping the genuine live cutoff, rather than replacing it by the whole half-line, is quantitatively essential at the half-band cutoff. At a later cutoff an even stronger finite-window positive-current estimate is false. Neither statement is a counterexample to FEI or to a signed estimate retaining other negative credits.

## 1. Normalization and the source bank

For f on F_2^D with values +/-1, use normalized Walsh coefficients a_S, p_S=a_S^2, entropy H in bits and I=sum |S|p_S. Let J=sum_i min(Inf_i,1-Inf_i). Our counterfunctions are already centered, so J=I. Put N=2^D.

Let P0=RM(1,D), P1=RM(d,D), d>=1, and

    alpha_r = 1{r in P0}/(2N) - 1{r in P1}/|P1|.

A word r is evaluated on the physical cube. For an actual Boolean phase h put

    U_r = N^-1 sum_x h(x)(-1)^{r(x)},
    V_r = N^-1 sum_x f(x)h(x)(-1)^{r(x)},
    R_h(s) = 2N sum_r alpha_r [cos(s U_r)-cos(s V_r)].       (1.1)

This is the predecessor's retained phase switch. Define its signed squared-magnitude tail profile

    A_h(u) = sum_r alpha_r [1{u<=V_r^2}-1{u<=U_r^2}], u>0.  (1.2)

All signs and the entire terminal subtraction remain inside A_h. Its Brownian bank is

    Q_M(h)=integral_0^infinity A_h(u)^2 du.                  (1.3)

Because both code laws are pairwise independent,

    integral A_h(u) du = sum_r alpha_r(V_r^2-U_r^2)=0.       (1.4)

The source averages h=g_S over the uniform subset S of its ACTIVE q-flip generators. It does not average over arbitrary independent truth-table signs.

## 2. Sharp universal domination of the entire Shannon/phase kernel

Write X=x^2, Y=y^2. In this section the kernels are in NATURAL logarithms:

    S(X,Y) = (X+Y) ln(X+Y) - X ln X - Y ln Y,
    P(X,Y) = (X+Y) D(2 sqrt(XY)/(X+Y)),
    D(t) = [(1+t)ln(1+t)+(1-t)ln(1-t)]/2,
    G=S+P,        M(X,Y)=min(X,Y).                          (2.1)

Use continuous zero values. These are ln(2) times the predecessor's bit-normalized S,P,G. They are PSD: S has its Laplace feature representation, G has its sine-square representation, and P has the positive Laplace series obtained by expanding D(t)=sum_{k>=1} t^{2k}/[2k(2k-1)].

### Theorem 2.1 -- sharp Loewner inequalities

For arbitrary finite nonnegative points X_j and arbitrary real coefficients c_j,

    S <= pi M,
    P <= (pi^2/2-pi) M,
    G <= (pi^2/2) M                                      (2.2)

in positive-semidefinite / quadratic-form order. Every constant is optimal for the class of all finite such Gram comparisons. In the predecessor's bit normalization divide all three constants by ln(2). These are kernel constants, NOT FEI constants.

### Proof

The mixed derivatives on the positive quadrant, interpreted through their locally integrable diagonal values, are

    L_S(u,v) = 1/(u+v),
    L_G(u,v) = [1/(2 sqrt(uv))] ln[(sqrt(u)+sqrt(v))/|sqrt(u)-sqrt(v)|],
    L_P=L_G-L_S >=0.                                     (2.3)

For example, if z=(ln u-ln v)/2, then

    L_G = atanh(sech z)/(2 sqrt(uv)),
    L_S = sech z/(2 sqrt(uv)),

so the final inequality is atanh(t)>=t. Differentiating (2.1), or the exact identity

    G(X,Y)=F(sqrt(X)-sqrt(Y))+F(sqrt(X)+sqrt(Y))
           -2F(sqrt(X))-2F(sqrt(Y)),   F(a)=a^2 ln|a|,

gives (2.3). Boundary values at X=0 or Y=0 vanish, so each kernel K is the double primitive of L_K.

For A(u)=sum_j c_j 1{u<=X_j}, this gives the EXACT identity

    sum_jk c_j c_k K(X_j,X_k) = integral integral A(u)L_K(u,v)A(v) du dv,
    sum_jk c_j c_k M(X_j,X_k) = integral A(u)^2 du.          (2.4)

Let w(u)=u^-1/2. Direct substitution v=u t^2 yields

    integral L_S(u,v)w(v)dv = pi w(u),
    integral L_G(u,v)w(v)dv = (pi^2/2)w(u).                (2.5)

The second constant is

    integral_0^infinity ln[(1+t)/|1-t|] dt/t = pi^2/2.

Indeed inversion t->1/t makes this twice the integral on (0,1); expansion of ln((1+t)/(1-t)) gives 2 sum_{j>=0}1/(2j+1)^2=pi^2/4 on that interval. The first integral is the elementary integral of v^-1/2/(u+v). Subtraction gives the P constant.

The weighted Schur proof can be written without citing an operator theorem. For any of these kernels, with C its constant in (2.5), symmetry gives

    C integral A^2 - integral integral A(u)L_K(u,v)A(v)
      = (1/2) integral integral L_K(u,v)w(u)w(v)
             [A(u)/w(u)-A(v)/w(v)]^2 du dv >=0.           (2.6)

This proves (2.2), for signed coefficients as well as positive ones. Every integral is finite by the same bound; approximation handles the diagonal singularity.

For sharpness, make the unitary change u=e^t, B(t)=e^{t/2}A(e^t). The integral operators become convolution by the nonnegative integrable kernels

    k_S(t)=1/[2 cosh(t/2)],
    k_G(t)=(1/2)ln coth(|t|/4),
    k_P=k_G-k_S >=0,

whose masses are respectively pi, pi^2/2, and pi^2/2-pi. On B=1[-T,T], the Rayleigh quotient is integral (1-|t|/(2T))_+ k(t)dt, tending to the full mass. Finite step profiles are dense in L2(0,infinity), and each compactly supported step profile is a finite signed sum of interval indicators 1{u<=X}. Therefore no smaller finite-Gram constant works. QED.

The Shannon part is the classical Hilbert/Carleman integral inequality in these variables, not a claimed discovery of that classical operator. The predecessor's phase constant 2 improves to pi^2/2-pi, but the more important transfer is that the entire Shannon bank also has a dimension-free signed quadratic-form comparison.

**Not an entrywise comparison.** S(X,Y)/min(X,Y) diverges when X/Y diverges. That fact does not contradict (2.2): the diagonal terms and signed quadratic form matter. Replacing either comparison by an entrywise argument would be incorrect.

### Remark on moment cancellations

Even requiring sum c_j=0 and sum c_j X_j=0 does not lower these optimal universal kernel constants. One can scale the preceding almost-extremal profile to A_T(u)=u^-1/2 1[e^-T,1], whose squared norm is T and whose integral stays below 2. Subtract a fixed supported function times a bounded coefficient to make its integral zero. This changes its L2 norm by O(1) and its quadratic form by O(sqrt(T))+O(1), so the quotient still tends to C. Approximate by step profiles with the same integral constraint and zero values near zero. They represent finite coefficients with both stated cancellations. This is an operator-level sharpness statement, not a construction of Boolean spectra.

## 3. Exact source transfer, including current-sector weights

The predecessor's four-sine identity, or two integrations of (2.3), gives

    integral_0^infinity R_h(s)^2 ds/s^3
      = N^2 Q_G(h) <= (pi^2/2) N^2 Q_M(h),                (3.1)

where Q_G uses the doubled signed measure on V_r^2 and U_r^2. Thus, conditionally, a genuine O(J) bound on the single Brownian bank would pay both predecessor banks. Section 5 proves that this particular universal bound is FALSE; (3.1) itself remains valid.

For precision, retain the actual multipliers too. On a paired active syndrome R let q=|R| and k be the number of clone pairs met oddly. For odd q (hence odd k>=1), put

    e_R=2(1/(qk)-1/q^2),
    epsilon_R=2*(2^-q/q)*(2^-k/k-2^-q/q).                 (3.2)

Both vanish for q=k. Let b_R(s) be the Walsh coefficients of Psi_s(g_S), where Psi_s(h)=2N sum alpha_r cos(s U_r). Define

    E_cur(s)=sum_(R odd) e_R b_R(s)^2.                    (3.3)

Let W_cur be the positive operator on the active-syndrome cube whose Walsh multiplier is e_R/4 on odd R and zero on even R. Then

    E_cur(s)=<R(s),W_cur R(s)>.

The Schur identity (2.6) also holds for Hilbert-valued A. Applying it to W_cur^(1/2) A_(g_S)(u) gives

    integral_0^infinity E_cur(s) ds/s^3
       <= (pi^2/2) Gamma_cur,
    Gamma_cur=N^2 integral <A(u),W_cur A(u)> du.            (3.4)

The analogous statement holds with epsilon_R. Since e_R<=4/9, (3.4) implies the predecessor-style upper bound

    integral_W E_cur(s) ds/s^3
       <= (pi^2/18) N^2 E_S Q_M(g_S),                    (3.5)

for every window W. The exact-weight form is stronger. The next section shows that neither full-line quantity in (3.4) admits the proposed universal O(J) payment either. Deleting the uncharged q=k sector does NOT fix the full-line problem.

## 4. A self-contained zero-atom bound for Reed--Muller cosets

This lemma is used to keep the counterexample at the actual half-band terminal cutoff, rather than replacing the code by an unrelated relaxation.

### Lemma 4.1

Let Y_1,...,Y_N be +/-1 variables matching independent uniform signs through moments of degree 4m, N even and 2m<=N. Then

    Pr(sum Y_i=0) <= 1/K_(N,m),
    K_(N,m)=sum_(j=0)^m binom(N/2,j)^2/binom(N,2j)
            >=(2m+1) binom(2m,m)/4^m > sqrt(m).           (4.1)

The strict final inequality is for m>=1.

### Proof

On independent signs, the normalized elementary symmetric Walsh sums

    q_j(Y)=binom(N,j)^(-1/2) sum_(|A|=j) product_(i in A)Y_i

are orthonormal. They depend only on W=sum Y_i. At W=0 their generating polynomial is (1-t^2)^(N/2), so q_(2j)(0)=(-1)^j binom(N/2,j)/sqrt(binom(N,2j)). The polynomial

    P(W)=K^-1 sum_(j=0)^m q_(2j)(0)q_(2j)(W)

has P(0)=1, degree 2m, and E P(W)^2=1/K. The same expectation holds under the stated 4m-moment matching. Since 1{W=0}<=P(W)^2, the first bound follows.

For each j,

    binom(N/2,j)^2/binom(N,2j)
      =[binom(2j,j)/4^j] product_(a=0)^(j-1)(N-2a)/(N-2a-1)
      >=binom(2j,j)/4^j.

The partial sum of these central-binomial terms equals (2m+1)binom(2m,m)/4^m. Induction from m=1 using ((2m+1)/(2m+2))^2>=m/(m+1) gives binom(2m,m)/4^m>=1/(2sqrt(m)). Hence K>=sqrt(m)+1/(2sqrt(m)). QED.

Uniform signs (-1)^r from r in RM(d,D), and every deterministic sign-twisted coset, match independent signs through degree 2^(d+1)-1. Here is an elementary justification. A nonempty evaluation set annihilating every degree<=d binary monomial has size at least 2^(d+1): split on a coordinate; if both slices are nonempty, each annihilates degree<=d-1 and has size at least 2^d; if only one is nonempty, induct on the ambient dimension at the same d. The base d=0 is the even-cardinality condition. Thus no smaller set gives a deterministic product of evaluations. Uniform linear-code orthogonality makes all those nonempty products have expectation zero. A fixed sign twist preserves this property.

Set m=4096. If d>=14 and N>=8192, the required 16384 moments match and (4.1) gives, uniformly in every Boolean phase h,

    Pr_(r in RM(d,D))[sum_x h(x)(-1)^r(x)=0] < 1/64.       (4.2)

The large-dimensional statement is proved analytically, not tested by enumerating its codewords.

## 5. Genuine Boolean obstruction at the HALF-BAND cutoff

### Theorem 5.1 -- full-line current and Brownian closing bounds are false

There is a sequence of centered Boolean functions, using all their original coordinates and then one source-required dummy coordinate, for which the displayed active-syndrome and retained-code objects satisfy

    N^2 E_S Q_M(g_S) / J(f) -> infinity,
    Gamma_cur / J(f) -> infinity,
    [integral_0^infinity E_cur(s)ds/s^3] / J(f) -> infinity. (5.1)

This holds at d=ceil(D/2). It also survives averaging the original anchor and coordinate order. The functions themselves satisfy H(f)<4I(f). Thus this refutes the proposed stronger closing estimates, NOT FEI.

### Construction

Take D>=27, n=D-1, N=2^D. In the original n-cube choose u=(1,...,1) and v=u+e_2+e_3. Let the original f be -1 exactly at u,v and +1 elsewhere. Append the dummy coordinate y and keep f independent of y. Its negative set Q consists of the four points (u,0),(u,1),(v,0),(v,1).

Fix the ordered-min q-flip basis with original coordinate 1 first and y last, anchor zero. Both u,v begin with 1 and have weight>=2. The normalized exponent vanishes at zero and all coordinate vectors. Its ordered-min syndrome b_w=q(w)+q(w-e_min(w)) is therefore nonzero only at u and v: neither has any earlier-coordinate child. Their dual generators are singleton defects. After the dummy split, there are exactly FOUR active singleton generators, the two genuine slice clones of each original parent. Thus g_S flips precisely the subset S of Q, uniformly among sixteen subsets. This is the actual fine active law, not a substitute random-phase law.

All n original coordinate directions are relevant because u+v has weight two, not one. Each has influence 8/N; the dummy has influence zero. Hence

    J(f)=I(f)=8n/N ->0.                                  (5.2)

### Source Fourier/zero-count calculation

Let z_0(S) be the fraction of zero Fourier coefficients of g_S, equivalently the fraction of zero correlations under P0. For |S|=0,1,2,3,4 respectively it is

    1-1/N,   0,   1/2,   0,   3/4.                      (5.3)

For odd |S|, every nonempty Fourier sum is a sum of an odd number of signs and is nonzero; its mean is also nonzero. Two distinct points give half the frequencies nonzero. Four points form an affine two-plane and give exactly N/4 nonzero frequencies, including the mean. These observations prove (5.3).

Let z_1(S) be the corresponding zero-correlation fraction under P1=RM(d,D). With d=ceil(D/2)>=14, Lemma 4.1 gives 0<=z_1(S)<1/64 for every S. Define beta_0(S)=z_0(S)-z_1(S), the zero-cosine-frequency coefficient of Psi_s(g_S)/(2N).

For any three-element R among the four active generators, direct Walsh averaging of (5.3) gives

    z0hat(R)=1/64-1/(16N).

A nonconstant Walsh coefficient of a function taking values in [0,1/64] has absolute value at most 1/128. Therefore

    beta0hat(R) >= a_N:=1/128-1/(16N) >=1/256.             (5.4)

Every such R doubles one original parent and hits the other oddly. In particular q=3,k=1, so

    e_R=4/9,       epsilon_R=11/288.                      (5.5)

These are genuine CHARGED current modes, not the uncharged q=k sector.

For 0<u<=4/N^2, nonzero correlations have squared magnitude at least u. Consequently the tail field (1.2) has Walsh coefficient 2 beta0hat(R). Parseval gives

    N^2 E_S Q_M(g_S) >=16 a_N^2,
    Gamma_cur >=(16/9)a_N^2.                             (5.6)

Both are bounded below by positive constants while (5.2) tends to zero. Through the newly consumed account01/B16 exact same-syndrome identity, the first bound is a counterexample to its target (8.1) WITH the retained shell and every same-syndrome signed sum intact. It is not obtained by removing that projection, replacing active phases by all truth-table phases, or discarding negative within-code terms.

To handle the actual full-line current rather than just its upper bound, observe that every correlation is an integer multiple of 2/N. Hence s->b_R(s) is a finite cosine polynomial of period pi N. Its mean over [pi N,2 pi N] is exactly 2N beta0hat(R). Cauchy--Schwarz gives

    integral_(pi N)^(2 pi N) b_R(s)^2 ds/s^3
       >= beta0hat(R)^2/(2 pi^2).

Using the actual multiplier (5.5),

    integral_0^infinity E_cur(s)ds/s^3 >=2a_N^2/(9 pi^2),  (5.7)

and the central current similarly has lower bound 11a_N^2/(576 pi^2). This proves all divergences in (5.1).

### Why original anchor/order averaging does not remove it

The two original defects differ in exactly two coordinates. A uniform coordinate order begins with a coordinate outside that pair with probability (n-2)/n. Conditional on this, a uniform anchor makes both translated defects have first bit 1 and neither be a unit vector with probability at least 1/2-2/2^n. On this event the same two-singleton / four-clone construction applies. The product of these probabilities is at least 1/8 for n>=4. The nonnegative banks therefore retain at least one eighth of the preceding lower bounds under the same outer averages. This does not assume independence of a fictitious new phase process.

### Why this is not FEI failure

The Fourier support of f is the annihilator of span(e_2+e_3,e_D), of size N/4. Its mean coefficient is 1-8/N and its other nonzero coefficients have magnitude 8/N. Put q=4/N, c=D-2. Then

    H(f)=phi((1-2q)^2)+8q(1-q)(c-1),  phi(t)=t log_2(1/t).

Since phi(t)<(1-t)/ln2 for 0<t<1 and 2/ln2<4,

    H(f)<8q(1-q)c<8qc<=4I(f).

All original influences are small and the source Booleanity is exact.

### The time window is the important distinction

At the source endpoint S_f=2sqrt(N/J)=N/sqrt(2n), the interval [pi N,2 pi N] used in (5.7) lies entirely OUTSIDE the live corridor [40,S_f]. The square-first domination is mathematically correct, but throwing away its subtracted outside-window energy creates a stronger full-line target which is false. Theorem 5.1 does NOT refute the half-band live-window estimate with its full original signed ledger.

## 6. A later-cutoff warning: a positive live-current payment can also fail

For the same family the binary exponent of f has degree D-2: the leading degree-n terms of the two original point indicators cancel, and at least one degree-(n-1) term remains. Thus for d>=D-2, f belongs to P1. The terminal-code potential is invariant under h->fh; its odd active Walsh coefficients vanish exactly.

For a three-element R, the affine part can now be calculated completely. With t=s/N,

    b_R(s)=2N sin(t)^3 cos(t)
       *[sin(s-4t)/N -(1/4-1/N)sin(4t)].                 (6.1)

To derive it, group physical Fourier characters by their restriction to the affine two-plane Q. Nonconstant balanced patterns contribute only even active Walsh degrees. The constant pattern has N/4 frequencies, one of them the empty frequency. Expanding their cosine functions gives (6.1). The checker independently compares it with direct Walsh spectra.

For D>=10 put n=D-1 and T=1/sqrt(2n), so S_f=NT. On t in [T/2,T], elementary sine bounds give

    |sin(t)^3 cos(t)|>=t^3/16,
    |sin((N-4)t)/N -(1/4-1/N)sin(4t)|>=t/4.

Here N>=8+8/T, T<pi/8 and NT/2>=40; the inequalities hold at D=10 and persist by induction. Hence b_R(Nt)^2>=N^2 t^8/1024, and

    integral_40^Sf E_cur(s)ds/s^3 >= 7/[786432 n^3].       (6.2)

Dividing by J=8n/N diverges. Outer anchor/order averaging retains the factor at least 1/8 from Section 5.

There are also exact asymptotics at this later cutoff. Put

    B_N(t)=sin(t)^3 cos(t)[sin((N-4)t)/N-(1/4-1/N)sin(4t)],
    B_inf(t)=1/64-(1/32)cos(2t)+(1/32)cos(6t)-(1/64)cos(8t).

Then B_N=(1-4/N)B_inf+u_N with |u_N(t)|<=N^-1 min(t^3,1). Hence its weighted L2 error against dt/t^3 is O(1/N). All four triple modes are identical and all remaining odd modes have zero current multiplier. The full-line current therefore tends to

    L=(-16 ln 2+63 ln 3+25 ln 5-49 ln 7)/144
      =0.02089284586301349... >0.                         (6.3)

For the exact evaluation, expand B_inf into the four displayed cosine weights beta_k at k=0,1,3,4. The cancellation sum beta_k=0 gives

    integral B_inf(t)^2 dt/t^3
      =sum_(j,k) beta_j beta_k[F(j-k)+F(j+k)],

with F(a)=a^2 ln|a| and F(0)=0. Multiplication by 64/9 and collection of the logarithms gives (6.3). Positivity is also certified by the integer inequality 3^63*5^25>2^16*7^49. This uses an analytic cosine identity, not large truth-table enumeration.

On the actual live window, B_inf(t)=-t^4+O(t^6) as t->0 and T=1/sqrt(2n). The u_N term has weighted norm O(1/N), negligible relative to the main norm of order n^-3/2. The omitted interval below 40/N is negligible as well. It follows that

    integral_40^Sf E_cur(s)ds/s^3 ~4/(27 n^3).             (6.4)

Thus the coarse lower bound (6.2) reflects a genuine polynomial-scale positive current, not a numerical artifact.

This is a theorem at the LATER cutoff d>=D-2. It is NOT a proof that (6.2) holds at d=ceil(D/2). In particular it must not be used to claim the remaining half-band source inequality has been refuted. It does show that a proof cannot assume every legitimate terminal cutoff has a positive-current O(J) estimate without using the other reserved negative terms.

## 7. Executed replacement: preserve the finite-band transform and its exact credits

The new universal kernel theorem remains usable, but not through the refuted unweighted full-line payment. The following reformulation retains the cutoff and the exact current multipliers.

From integration of each threshold indicator,

    R_h(s)=Ns integral A_h(u) sin(s sqrt(u))/sqrt(u) du.    (7.1)

Equation (1.4) permits subtracting s from the integrand kernel in (7.1) without changing its value. Thus the distance-four cancellation is retained BEFORE any norm. For the actual current operator W_cur,

    integral_W E_cur(s)ds/s^3
      =N^2 integral_W || integral W_cur^(1/2)A(u)
                       sin(s sqrt(u))/sqrt(u) du ||_2^2 ds/s.  (7.2)

This is a finite-band sine-transform energy of the genuine signed threshold profile. It contains the actual parent/mode multiplier, rather than the scalar cap.

There is also an exact, nonnegative-deficit form. Let B(u)=W_cur^(1/2)A(u), and define

    D_cur=(N^2/2) integral integral L_G(u,v)/(sqrt(uv))
                     ||sqrt(u)B(u)-sqrt(v)B(v)||_2^2 du dv,
    T_(W^c)=N^2 integral_(s outside W)
                     || integral B(u)sin(s sqrt(u))/sqrt(u)du ||_2^2 ds/s.

Then (2.6) and (7.2) prove

    boxed: integral_W E_cur(s)ds/s^3
       =(pi^2/2)Gamma_cur - D_cur - T_(W^c).              (7.3)

Both displayed subtractions are nonnegative. The terminal subtraction and all within-code cancellation are still inside A. Theorem 5.1 proves that the outside-window credit cannot simply be dropped in a universal half-band payment. Section 6 separately warns that the remaining positive current need not suffice at every later cutoff either.

This is a completed analytic replacement of the full-line relaxation, NOT a claim that the right side of (7.3) is now O(J). The remaining useful task is a source-admissible estimate of the retained finite-band expression, jointly with the actual R16/terminal/negative-entropy ledger when needed. Renaming Gamma_cur as an unpaid positive budget would repeat the refuted route.

## 8. Verification, exploratory failures, and claim ledger

`verify_threshold_contraction.py --part all` was executed. It includes:

* 124 exact central-binomial/Christoffel comparisons, 22 exact reproducing-polynomial norm checks, and the exact m=4096 central-binomial bound;
* four exhaustively enumerated SMALL Reed--Muller codes (128, 2048, 32768 and 65536 words), sixteen phase states each, with exact histograms, code moment identities and signed threshold energies;
* 208 exact code-coset moment checks and the actual four-generator syndrome checks;
* eight directly materialized four-point spectra through D=12, exact zero-frequency coefficients and anchor/order event bounds;
* high-precision mixed-derivative, kernel-mass, trigonometric and finite-window transform checks, plus finite-grid generalized eigenvalue diagnostics for the three sharp kernel inequalities.

The numerical inequalities are labelled diagnostics; the analytic proofs establish the all-dimensional claims. The D>=27 counterfamily and its degree-14-or-higher code were NOT enumerated. The low-D examples include a negative triple coefficient at D=5,d=2, which is preserved; the large-D proof uses its explicit moment hypothesis, not a extrapolation from small signs. Initial tests with the FULL truth-table terminal code are not used as source-valid evidence for the half-band theorem.

The independent mechanism changes actually executed were: deriving the Shannon Carleman comparison rather than another phase-only estimate; testing the new proposed closing bank on genuine sparse Boolean sources; replacing full-line dominance by the exact cutoff/current-weighted sine-transform identity. No full FEI candidate is being sent for a ceremonial audit.

PROVED_ANALYTIC_SELF_CHECKED: sharp signed kernel comparisons; exact Schur deficit and finite-band representation; Reed--Muller-coset zero-atom bound; actual active-syndrome half-band full-line counterfamily; later-cutoff live positive-current counterfamily with its distinct cutoff hypothesis.

REFUTED_STRONGER_TARGETS_NOT_FEI: universal O(J) payment of N^2 E Q_M; universal O(J) payment of the exact-weight full-line current; universal live positive-current payment at every late cutoff d>=D-2. Valid predecessor identities, PSD facts, finite-window domination and the original signed FEI question remain intact.

OPEN: the half-band finite-window/current-and-negative-credit estimate; or the complementary adaptive restriction, joint derivative or arithmetic routes sufficient for full FEI. No universal FEI constant, proximity percentage, publication priority or independent verification is asserted.

## 9. Literature and delivery scope

The Hilbert/Carleman norm pi, weighted Schur method, Krawtchouk orthogonality and Reed--Muller dual-distance mechanism are established mathematics. Their proofs needed here are included rather than invoked with unverified hypotheses. Bounded public searches concerned the Carleman kernel, entropy kernels and FEI/Riesz work; they do not establish novelty. The primary research paper by Sra, *Metrics induced by Jensen-Shannon and related divergences on positive definite matrices* (Linear Algebra Appl. 616, 2021, 125--138), concerns metric properties, not a supplied universal FEI theorem. No external current resolution is assumed from a search miss. A later primary-source lookup recovered Yafaev, *Spectral and scattering theory for perturbations of the Carleman operator*, arXiv:1210.5709, as classical operator context, and Gonzalez--MacManus--Pereyra, *Further evidence towards the Fourier Entropy-Influence conjecture*, arXiv:2606.00246, as restriction-framework context. Their abstracts were checked; no uninspected theorem is used in our proofs.

All new artifacts are private research inputs. The shared recipients are account01/B16, account02/B15/B16/B18, account03/B16/B18 and account04/B16, with the A/B workers free to continue their independent restriction and stability routes. The handoff must prominently mark the full-line closing target as REFUTED AT ITS STATED SCOPE, while preserving the valid kernel theorems. Publication of the handoff is not evidence every worker has consumed it. No scheduler changes or native production activation are part of this run.
