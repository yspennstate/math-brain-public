# FEI continuation: sharp-order spectral entropy continuity

20 September 2026. Owner-requested research continuation. Authoring assistant: GPT-6 Astra Pro; a separately configurable reasoning level is not exposed.

**The unrestricted Fourier entropy–influence conjecture is not proved here.** This report proves an auxiliary theorem answering the asymptotic gap asked in Rani Hod's Section 6, item 3, and develops an affine-subspace version. It also constructs explicit Boolean lower examples. Publication priority has not been cleared, and no independent review or formal verification is claimed.

## 1. Statements and relation to the source question

For a Boolean sign function f on F_2^n with uniform measure, write

    a_s = E_x f(x)(-1)^{s dot x},   N = 2^n,
    H(f) = -sum_s a_s^2 log_2(a_s^2),
    I(f) = sum_s |s| a_s^2.

Zero entropy summands are zero. Let Lambda_n be the maximum of |H(f)-H(g)| over Boolean functions on n bits differing at exactly one physical input.

Define

    kappa = max_{u >= 0} u/(2 cosh u),
    C_* = 16 kappa / ln 2.

The maximum is attained at the unique positive root u_* of u tanh u = 1. An exact rational certificate in the accompanying checker gives

    7.649093155814870 < C_* < 7.649093155814873 < 7.65.

**Theorem 1 (one-point continuity, no logarithmic loss).** For every n and every such pair,

    |H(f)-H(g)| <= C_* / sqrt(N).

The elementary, slightly weaker constant 16/(e ln 2) < 8.5 is also proved without locating u_*.

**Theorem 2 (affine-subspace flip).** For every Boolean f and every nonempty affine subspace A of density delta,

    |H(f(1-2 1_A))-H(f)| <= C_* sqrt(delta).

The constant is independent of ambient dimension, the orientation of A, and f. No independence between A and f is assumed. For codimension r, delta=2^(-r). This order is necessary already when A is a point.

**Theorem 3 (explicit lower examples).** There are explicit Boolean one-point pairs with

    limsup_{n -> infinity} sqrt(2^n) Lambda_n
      >= (225/128) log_2 15 + (31/256) log_2 31
       = 7.467503334554009... .

A simpler construction proves

    liminf_{n -> infinity} sqrt(2^n) Lambda_n >= log_2 3 > 0.

Consequently Lambda_n = Theta(2^(-n/2)) over all dimensions. The exact optimal constant is not determined. The upper constant C_* is the constant furnished by our amplitude argument, not an assertion of optimality over Boolean functions.

**Source comparison.** Hod, arXiv:1711.00762, Lemma 5.2 proves 12 n/sqrt(N); Section 6, item 3 asks to close the gap between an Omega(1/sqrt(N)) example and that upper bound. Theorem 1 removes the n factor, and Theorem 3 supplies independent lower constructions, stronger along a subsequence than the Niho benchmark quoted there. This answers the mathematical asymptotic question in that source. A bounded current literature search does not establish that no later author has answered it. Hod's problem is auxiliary to FEI, not the full conjecture.

## 2. A dimension-normalized amplitude lemma

For a real or complex vector a of Euclidean norm one, define its entropy to be the Shannon entropy of |a_j|^2. We first prove a statement that does not require Booleanity.

**Lemma 2.1.** If a,b are unit vectors in C^M, then

    |H(a)-H(b)| <= (8 kappa/ln 2) sqrt(M) ||a-b||_infinity.

### 2.1 Scalar inequality and constant

For every x>0,

    x |ln x| <= kappa (1+x^2).

Indeed, the quotient x|ln x|/(1+x^2) is invariant under x -> 1/x. On setting x=exp(u), u>=0, it becomes u/(2 cosh u). Its derivative has the sign of 1-u tanh u. The map u tanh u is strictly increasing for u>0, is zero at zero, and tends to infinity. Thus there is exactly one positive maximizer.

For a wholly elementary alternative, -x ln x <= 1/e when 0<x<=1, and x ln x <= x^2/e when x>=1, the latter following by maximizing (ln x)/x. Hence kappa <= 1/e. Both scalar estimates extend to x=0 by continuity.

### 2.2 Proof of the amplitude lemma

Let E denote the average over M coordinates and put

    w(t) = sqrt(M) ((1-t)a + t b),
    v = sqrt(M)(b-a),   0<=t<=1.

The endpoint second moments are one. Convexity of squared norm gives E|w(t)|^2<=1 for every t. Define G(z)=|z|^2 ln |z|^2 with G(0)=0. The identity

    H(a) = log_2 M - E G(sqrt(M)a)/ln 2

holds because a is normalized, and likewise for b. Thus the common log_2 M term cancels exactly before any inequality is applied.

The real differential of G on C, identified with R^2, gives

    d/dt G(w(t))
      = 2 Re(v conjugate(w(t))) [ln|w(t)|^2 + 1].

At a zero of w the derivative extends continuously by zero, since r ln r -> 0. Therefore this expression can be integrated even when a coefficient changes sign or passes through zero.

The term containing +1 has integral

    integral_0^1 E 2 Re(v conjugate(w(t))) dt
      = E|w(1)|^2 - E|w(0)|^2 = 0.

This second cancellation is essential. Estimating that term or the log M term separately would introduce an unnecessary dimensional loss. The remaining integral is bounded by

    |H(b)-H(a)|
      <= (4/ln 2) ||v||_infinity
                    integral_0^1 E[|w(t)| |ln|w(t)||] dt
      <= (4 kappa/ln 2) ||v||_infinity
                    integral_0^1 (1+E|w(t)|^2) dt
      <= (8 kappa/ln 2) sqrt(M) ||b-a||_infinity.

This proves Lemma 2.1. The segment itself need not remain on the sphere; equal endpoint norms and its norm-at-most-one property are enough.

**Equal-mass version.** If sum|a_j|^2=sum|b_j|^2=m, write the unnormalized entropy as Hcal(a)=-sum|a_j|^2 log_2|a_j|^2. Scaling by sqrt(m), and canceling the common -m log_2 m, proves

    |Hcal(a)-Hcal(b)|
      <= (8 kappa/ln 2) sqrt(M m) ||a-b||_infinity.

For m=0 both vectors vanish and the conclusion is immediate.

## 3. Proof of one-point and affine-subspace continuity

### 3.1 One-point change

If f and g differ only at x_0, then

    ghat(s)-fhat(s) = -2 f(x_0) (-1)^{s dot x_0}/N.

Both amplitude vectors have norm one by Parseval, and every amplitude changes by magnitude 2/N. Apply Lemma 2.1 with M=N. This gives C_*/sqrt(N), proving Theorem 1. Input translation and interchanging the pair handle every point and either sign at that point.

### 3.2 Fourier-coset reflection for an affine flip

Let A=x_0+V, where V is a linear subspace of codimension r. Let W=V^perp and M=|W|=2^r=1/delta. The Fourier coefficients of 1_A are

    (1_A)hat(w) = M^(-1) (-1)^{w dot x_0} 1_{w in W}.

Partition all Fourier labels into cosets c+W. In a fixed coset define

    u_c = sum_{w in W} (-1)^{w dot x_0} a_{c+w},
    m_c = sum_{w in W} |a_{c+w}|^2.

Convolution with 1-2 1_A sends the amplitudes in that coset to

    b_{c+w} = a_{c+w} - (2/M) (-1)^{w dot x_0} u_c.

For clarity, substituting t=w+v in the convolution uses
(-1)^{v dot x_0}=(-1)^{w dot x_0}(-1)^{t dot x_0}; no sign depending on c has been omitted. This map is reflection in the direction of the flat unit vector M^(-1/2)((-1)^{w dot x_0})_w. It is orthogonal (unitary for complex amplitudes). Therefore the coset mass m_c is exactly preserved, and the infinity norm of its amplitude displacement is 2|u_c|/M.

Apply the equal-mass lemma in every coset, then sum:

    |H(f(1-2 1_A))-H(f)|
      <= (16 kappa/(sqrt(M) ln 2)) sum_c sqrt(m_c)|u_c|.

We have sum_c m_c=1. To identify the other squared sum, restrict f to A. The restricted characters are indexed by the quotient of Fourier labels by W; its coefficient at that quotient label is (-1)^{c dot x_0}u_c. Parseval on the finite group V gives

    sum_c |u_c|^2 = E_{x in A}|f(x)|^2 = 1.

Cauchy–Schwarz now bounds sum_c sqrt(m_c)|u_c| by one. The result is C_*/sqrt(M)=C_*sqrt(delta), proving Theorem 2.

The proof also gives, for any normalized real or complex f,

    |H(f(1-2 1_A))-H(f)| <= C_* ||f 1_A||_2.

Here entropy means the normalized squared Fourier law, and multiplication by the sign preserves its normalization. The Boolean hypothesis specializes ||f 1_A||_2 to sqrt(delta). Thus this continuity result alone is not a use of all the rigidity available from Booleanity.

### 3.3 Influence and the limitation of a per-modification payment

Let k(A) be the number of physical coordinate directions e_i not belonging to V. A coordinate in V preserves A. A coordinate outside V maps A to a disjoint coset. Consequently, for q=1-2 1_A,

    I(q) = 2 delta k(A).

The edge disagreement sets of f and fq differ only on edges where q changes. Hence

    |I(fq)-I(f)| <= I(q) = 2 delta k(A).

For a coordinate subcube k(A)=r, but for an oblique affine subspace it may be larger. The entropy modulus sqrt(delta) is substantially larger than r delta for rare cells. The lower constructions below show that this mismatch is real, not just slack in an upper estimate.

## 4. An elementary explicit lower construction

This section proves a matching scale without using a deep exponential-sum formula.

Let m>=2 be even, M=2^m, and U=M/2. Use inputs (x,y) in F_2^(m-1) x F_2^m, so n=2m-1 and N=MU=M^2/2.

### 4.1 A partition of nonzero vectors into triples

On each adjacent pair of y coordinates define J(a,b)=(b,a+b). Applied blockwise, J satisfies J^2+J+Id=0 and J^3=Id. It has no nonzero fixed vector: J(a,b)=(a,b) forces a=b=0 on every pair. Therefore all nonzero vectors partition into triples

    {y,Jy,J^2y}.

Each triple is the set of nonzero vectors of the two-dimensional binary subspace spanned by y and Jy, since y+Jy+J^2y=0. There are L=(M-1)/3 triples. As L<=U-1, assign them distinct nonzero labels in F_2^(m-1), and set pi(0)=0. One fully deterministic labeling enumerates the smallest not-yet-labeled y in integer order and assigns the next positive integer label to its orbit.

Define

    f_m(x,y)=(-1)^{x dot pi(y)}.

It is Boolean and f_m(0,0)=1. Let g_m differ from f_m only at the origin, where it takes value -1.

### 4.2 Exact Fourier histogram

First average over x. For a Fourier label (u,v),

    fhat_m(u,v) = M^(-1) sum_{y:pi(y)=u} (-1)^{v dot y}.

The fiber u=0 is the singleton {0}, producing +1/M for every v, hence M such coefficients. A triple fiber W\{0} produces +3/M when v is in W^perp and -1/M otherwise, because the complete character sum on W is 4 or zero. There are M/4 annihilating v and 3M/4 nonannihilating v per triple. Every unused label produces zeros. The signed coefficient histogram is therefore

| Coefficient | Multiplicity |
| --- | ---: |
| +1/M | M |
| +3/M | LM/4 |
| -1/M | 3LM/4 |
| 0 | (U-L-1)M |

The multiplicities sum to N; their squared coefficient sum is one. After flipping the origin, every coefficient is reduced by 2/N.

### 4.3 A finite-support limit lemma

Let t_N be the random variable obtained by choosing a Fourier label uniformly and taking sqrt(N) times the coefficient of a Boolean function with value +1 at the origin. Suppose these random variables are uniformly bounded and converge in law to T. Necessarily E t_N=1/sqrt(N) and E t_N^2=1, so E T=0 and E T^2=1.

Put eta=N^(-1/2) and G_2(t)=t^2 log_2(t^2), continuously extended at zero. For an origin flip,

    sqrt(N)[H(g)-H(f)]
       = E[(G_2(t_N)-G_2(t_N-2 eta))/eta].

The derivative G_2' is continuous, including at zero. On a common compact interval it is uniformly continuous. By the integral form of the difference quotient, the displayed integrand converges uniformly to 2G_2'(t_N). Passing to the limiting law therefore gives

    lim sqrt(N)[H(g)-H(f)]
       = 2 E G_2'(T)
       = (8/ln 2) E[T ln|T|],

where the term proportional to E T vanishes. This proves the limit and justifies it at zero atoms; a formal Taylor expansion with an unbounded second derivative is not needed.

### 4.4 Applying the lemma and covering all dimensions

For the triple construction, T has values 3/sqrt(2), -1/sqrt(2), 0 with respective probabilities 1/6, 1/2, 1/3. The singleton fiber has vanishing probability. Direct substitution yields

    lim_{m even -> infinity} sqrt(N)[H(g_m)-H(f_m)]
       = 2 sqrt(2) log_2 3.

To cover every large n, choose the largest n_0=2m-1 congruent to 3 modulo 4 not exceeding n, and let d=n-n_0, so 0<=d<=3. Extend f_m by d irrelevant coordinates and flip just one physical point of the enlarged cube. The new normalized coefficient law has the old nonzero law multiplied by 2^(d/2), with its probability multiplied by 2^(-d); all other Fourier labels are zero. Its limiting first logarithmic moment is the old one times 2^(-d/2): the extra logarithmic term cancels because E T=0. Thus the limiting scaled change in residue class d is

    2 sqrt(2) log_2 3 * 2^(-d/2) >= log_2 3.

There are only four residue classes, proving the liminf claim in Theorem 3. The first, three-variable triple example actually has a negative signed change; the theorem is asymptotic, and does not assert positivity for every finite member. The checker records signed changes correctly.

## 5. A stronger lower constant from mixed subspace fibers

Here we construct explicit finite spectra approaching 7.467503334554009... in the same scaled continuity problem. These are not FEI-ratio lower bounds.

### 5.1 General subspace-fiber construction

Take x in F_2^k, y in F_2^m, M=2^m, U=2^k. Suppose the nonzero y vectors partition into fibers of the form W\{0}, where each W is a binary subspace of size q=2^r. Let L_q be the number of such fibers, with L=sum_q L_q<=U-1. Assign distinct nonzero x-labels to these fibers and label y=0 by zero. For f(x,y)=(-1)^{x dot pi(y)}, the same character-sum proof gives

| Coefficient | Multiplicity |
| --- | ---: |
| +1/M | M |
| +(q-1)/M, for each q | L_q M/q |
| -1/M | sum_q L_q M(q-1)/q |
| 0 | (U-L-1)M |

The partition identity sum_q L_q(q-1)=M-1 ensures normalization. The raw Walsh coefficients are these values multiplied by N=MU, so all histogram checks can be done with integers without enumerating the truth table.

### 5.2 Existence of the mixed partition in every specified dimension

Let m=20s with s>=1, and set M=2^m, U=M/16, k=m-4, N=M^2/16. Regard the y space as the field F_(2^(20s)), and let K be its subfield F_(2^20). The nonzero vectors partition into the nonzero parts of one-dimensional K-subspaces. There are

    B=(M-1)/(2^20-1)

such blocks, each a 20-dimensional binary subspace.

The field K has subfields F_16 and F_32, since 4 and 5 divide 20. Within any K-line, choosing its F_16-lines partitions its nonzero vectors into fibers of size 15; choosing its F_32-lines instead partitions them into fibers of size 31. These partitions are only used within separate outer blocks, so all resulting fibers remain disjoint. The finite-field existence and subfield statements are standard algebra; nothing about the FEI conjecture is assumed.

Put

    D=2^20-1,   a16=D/15=69905,   a32=D/31=33825,
    A=floor((U-1-a32 B)/(a16-a32)).

Use the 16-type refinement in A outer blocks and the 32-type refinement in the others. This gives

    L16=A a16,   L32=(B-A)a32.

The numerator defining A is nonnegative: a32 B=(M-1)/31<=M/16-1 for M>=2^20. Also U-1< (M-1)/15=a16 B, so A<B. Thus 0<=A<=B. By the floor definition, L16+L32<=U-1, and fewer than a16-a32 labels remain unused. Distinct nonzero labels therefore exist. Ordering field elements in any fixed polynomial basis makes all choices deterministic; different valid choices have the same signed spectral histogram.

This proves existence of the claimed Boolean function in every specified dimension, not merely feasibility of an abstract probability distribution.

### 5.3 Limit and exact constant

As s grows, the fraction of outer blocks receiving the 16-type refinement tends to

    (1/16-1/31)/(1/15-1/31)=225/256.

It follows that L16/U -> 15/16 and L32/U -> 1/16. The singleton and unused-label fractions tend to zero. Since sqrt(N)=M/4, the limiting normalized coefficient law is

    T=15/4 with probability 15/256,
    T=31/4 with probability 1/512,
    T=-1/4 with probability 481/512.

One checks E T=0 and E T^2=1 exactly. The limit lemma applies because these supports are uniformly bounded, including their vanishing singleton/zero components. Its logarithmic first moment gives

    lim sqrt(N)[H(g)-H(f)]
      = (225/128) log_2 15 + (31/256) log_2 31.

The checker encloses this constant between 7.467503334554009 and 7.467503334554010. It also gives finite symbolic examples at n=36, 76 and 116. At n=76 the scaled signed increase is between 7.467500937624214 and 7.467500937624215; at n=116 it lies between 7.467503334551302 and 7.467503334552186. These certificates use the proved histogram, not an enumeration of 2^76 or 2^116 points.

The smallest n=36 member has only one outer block, so it does not approximate the optimized mixture closely. Its smaller value is retained in the output, not discarded.

## 6. A rigorous barrier to a tempting full-FEI shortcut

The preceding lower examples rule out a universal constant K for

    |H(fq)-H(f)| <= K I(q)

over Boolean f and q. Take q to flip a single point and take f from the triple family. The left side is asymptotic to a positive constant divided by sqrt(N), whereas I(q)=2n/N. Their ratio tends to infinity. This is a failure of relative entropy stability in the influence of the modifier, not a failure of FEI for either endpoint.

Even adding a universal bounded correction cannot repair that statement. More precisely, no fixed finite K,D can make

    |H(fq)-H(f)| <= K I(q)+D

hold for all dimensions and Boolean f,q. To prove this, first choose an example with a positive signed change Delta>K I(q). On k disjoint copies, entropy and influence add exactly:

    H((fq)^(tensor k))-H(f^(tensor k)) = k Delta,
    I(q^(tensor k)) = k I(q).

For k>D/(Delta-K I(q)) the proposed inequality fails. This also defeats any correction uniformly bounded over the full modifier class, including a bounded function of its negative density. The tensor products preserve Booleanity and use disjoint physical coordinates.

Thus a successful full-FEI proof built from modifications cannot simply pay each entropy change from the modifier's own influence, even after an additive constant. It must retain information about the background function, a non-reused global budget, or cancellations between modifications. The new continuity theorem does not supply that missing amortized estimate.

## 7. What remains of the original FEI target

The original target is one finite C with H(f)<=C I(f) for every Boolean f in every dimension. That is not obtained above. In particular, the number 7.65 is a continuity constant, **not an FEI constant**.

The live repository route remains the uniform erasure bound

    B(f)=sum_i H(S_i | S_{-i}) <= K_E I(f),

where S has law fhat(s)^2 and K_E is independent of f and dimension. The already-proved, correctly quantified restriction argument would imply FEI with constant K_E+2/ln 2. No such universal K_E is proved here. The false pointwise inequality H<=B+(2/ln2)I is not used.

The normalization cancellation in Lemma 2.1 removes a real logarithmic loss in one auxiliary problem. It does not remove the separate hypercontractive loss in the Kelman–Kindler–Lifshitz–Minzer–Safra multiscale FEI argument. Applying it there still requires a theorem controlling the aggregate perturbations while retaining Boolean structure; filtered intermediate Fourier pieces are not generally Boolean.

## 8. Actual validation and reproducibility

Run `python3 verify_continuity.py --output verification.json` from this directory. Python's standard library suffices.

The completed run reports PASS for:

- 32,906 exhaustive origin-flip pairs through dimension four, modulo exchanging the pair. Translation identifies flips at other input points with these cases.
- All Boolean functions and all affine-subspace flips through dimension three: 13,244 cases, across 65 affine gate descriptions in dimensions one, two and three.
- 840 deterministic-seed sampled affine-flip cases in dimensions four through ten.
- Four explicit triple-spread truth tables at n=3,7,11,15, with exact comparison to their predicted signed Walsh histograms.
- Three finite-field Niho benchmark truth tables at n=4,8,12, compared to the published benchmark histogram. These are validation benchmarks, not inputs needed for the new lower proof.
- Three symbolic mixed-spread certificates at n=36,76,116, with exact integer histogram counts, Parseval, origin value, label budgets, and rational entropy intervals.

All entropy comparisons use rigorous logarithm enclosures, not floating-point tolerances. For x in [1,2], with z=(x-1)/(x+1), the checker bounds ln x by the first 48 terms of 2 sum z^(2j+1)/(2j+1), with tail at most 2 z^97/[97(1-z^2)]. Integer arguments are range-reduced, and bounds are rounded outward to denominator 2^100. Square roots are enclosed by integer square roots. Printed decimal endpoints are rounded outward.

A 96-term positive exponential series with geometric tail certifies the root bracket

    1.1996786402577338 < u_* < 1.1996786402577340,

using the equivalent sign equation (u-1)exp(2u)-(u+1)=0. It then encloses kappa and C_*; all tested continuity inequalities use the lower endpoint of this certified C_* interval on their right side, a stricter finite check than using the upper endpoint.

The first checker version incorrectly required every signed lower-family change to be positive, including n=3. That auxiliary assertion failed: the true change there is approximately -0.216917186688699. It was removed, signed interval multiplication was corrected to handle either sign, and the universal check was expressed in absolute value. The complete corrected run passed. No all-dimensional theorem depended on that false finite positivity claim. The output preserves the negative example.

The accompanying WORKLOG records the other full-FEI attempts and their limitations. Finite checks support the written proofs; they are neither independent review nor unrestricted FEI evidence by extrapolation.

## 9. Sources and dependency boundaries

1. Rani Hod, *Improved Lower Bounds for the Fourier Entropy/Influence Conjecture via Lexicographic Functions*, arXiv:1711.00762. https://arxiv.org/abs/1711.00762 . Lemma 5.2 and Section 6 item 3 were read directly, including PDF page images 16, 18 and 19 (zero-based). The source's single-point upper bound and asymptotic question are the comparison, not the new proof.
2. Esty Kelman, Guy Kindler, Noam Lifshitz, Dor Minzer and Muli Safra, *Towards a Proof of the Fourier–Entropy Conjecture?*, arXiv:1911.10579v2. https://arxiv.org/abs/1911.10579 . The multiscale argument and Corollary 6.7 were consulted for the unresolved full-FEI attack, not assumed to have no logarithmic loss.
3. Maria Jose Gonzalez, Paul MacManus and Maria Cristina Pereyra, *Further evidence towards the Fourier Entropy-Influence conjecture*, arXiv:2606.00246v2. https://arxiv.org/abs/2606.00246 . Consulted for contemporary FEI context; no theorem above relies on an unproved lemma from that paper.

Repository material consumed includes the current `proofnet24/P03-fei/README.md`, starting blob `9201da45afcf21156ae078cc505d37b57a1ae4b7`; the complete earlier erasure reduction at `solo-2026-09-17/ERASURE_REDUCTION.md`; and the older `FINAL_HANDOFF_2026-09-18.md`, blob `ab77075ab4a76d4584aa5012e9a92ba7f1bd0f8a`. The historical handoff's pointwise erasure converse is superseded by the current entrypoint and is not reused. Its exact 80-variable B/I>4 certificate was recognized as prior work after reproducing that phenomenon experimentally; the reproduction is not credited as a new discovery.

The preceding quadratic-symmetry continuation is retained unchanged. The new proofs above do not depend on its class theorem. No old overlap, resolvent, affine-drift, or zero-debt decomposition shortcut is reinstated. No schedule, source ownership, native finite-dimensional metric, or peer proof is changed by this report.

Searches for later work on Hod's Lipschitz question and one-point spectral entropy did not establish a matching earlier proof, but this was not an exhaustive review. Claims of first discovery or publication novelty remain unverified. The algebraic constructions, proofs and actual checks are supplied so that the result can be evaluated on its mathematics.
