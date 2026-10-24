# FEI continuation: exact collapse of global phase bounds and a coupled Shannon restriction estimate

21 September 2026. Interactive account02 continuation, not a scheduled B-slot.

**Full uniform-cube FEI remains OPEN / NOT PROVED by this work.** The main result is a complete obstruction to the global phase-template payment proposed in the preceding interactive run. It is false as a route to a uniform influence bound, even on an explicit balanced Boolean family. A second result is a universal, computer-assisted scalar inequality that gives a tighter conditional transfer from spectral erasure entropy to FEI. The global obstruction persists even in the exact quadratic-phase recursive-majority class. No finite universal erasure bound is proved. No Boolean counterexample to FEI is obtained.

MODEL: GPT-6 Astra Pro, self-report. Configured reasoning setting and provider thinking counters are not exposed. Execution: WITHOUT_VERIFIED_BRAIN. Authenticated repository retrieval was used, but the native math_brain, brain and spread_recall packages were unavailable. Independent review and publication-priority clearance are pending. All new proofs and computations below are self-checked.

## 1. Exact scope and continuity

Let f:F_2^n->{-1,1}, with normalized Walsh coefficients

    a_s = 2^{-n} sum_x f(x)(-1)^{s.x},
    p_s = a_s^2,
    H(f) = -sum_s p_s log_2 p_s,
    I(f) = sum_s |s|p_s,
    M(f) = sum_s |a_s|.

Zero entropy terms are zero. Parseval gives sum p_s=1 and M>=1. Full FEI asks for H(f)<=C I(f) with a single finite C for every n and every Boolean f.

The immediately preceding report, `fleet-2026-09-21/account02/interactive/20260921T155319Z-parity-profile-and-phase/REPORT.md`, blob `399a1a99e2efa5d20d3a3dc07573eb1a13e68e76`, proved

    H(f) <= r(Q)+2 log_2(1+2 Lambda_Q(f)),                 (1.1)

where Q is a quadratic polynomial on Fourier labels, r(Q) its polar rank, and Lambda_Q the Fourier-l1 mass of sign disagreements with (-1)^Q. It proposed, but did not prove, that optimizing this right side might have a universal O(I) bound.

This continuation directly attacks that missing implication. Sections 2-4 prove that the optimized bound is exactly the old spectral-l1/Renyi bound and is not O(I). The result supersedes that proposed implication, not the validity of (1.1), the support-compression theorem, or the restricted formula theorem in the preceding report.

After this obstruction, I also tried direct spectral erasure bounds and recursive Boolean constructions. Essential source recovery identified that the erasure reduction and several tempting stronger estimates were already investigated:

* `solo-2026-09-17/ERASURE_REDUCTION.md`, blob `770f1fc8438b360549ed89480cb260768d839923`: the exact restriction identity and K_E<=C_FEI<=K_E+2/ln2.
* `solo-2026-09-17/ADDRESSING_BARRIER_2026-09-18.md`, blob `c1e52dff50095854d85c20e8b13a5385d91efaca`: every fixed positive-power edge majorant and every superlinear logarithmic majorant fail on genuine Boolean examples.
* `solo-2026-09-17/FINAL_HANDOFF_2026-09-18.md`, blob `ab77075ab4a76d4584aa5012e9a92ba7f1bd0f8a`: an archived 80-variable witness has certified 4.007<B/I<4.008. That prior certificate was not rerun here; it prevents treating B<=4I as an unrefuted new candidate.

Paths above are relative to `proofnet24/P03-fei/`. Source master at initial recovery was `20a152a1fa9a0f62011c638e45f1efe18c1b96df`. The new work therefore does not count rediscovered erasure identities, failed absolute-overlap estimates, or small random searches as new full-problem progress.

## 2. The optimized global quadratic-phase bound collapses exactly

Write sigma_Q(s)=(-1)^{Q(s)}, and

    A_Q = sum_s sigma_Q(s)a_s = M-2 Lambda_Q.              (2.1)

### Lemma 2.1: the precise quadratic correlation ceiling

If Q has polar rank r, then

    |A_Q| <= 2^{r/2}.                                    (2.2)

Proof. Its polar form is B(s,u)=Q(s+u)+Q(s)+Q(u)+Q(0), with radical R of size 2^{n-r}. For the normalized Walsh transform of sigma_Q,

    sigmahat_Q(x)^2
      = 2^{-n} sum_{u in R} (-1)^{Q(u)+Q(0)+x.u}.         (2.3)

This follows by expanding the square, substituting t=s+u, and summing the character (-1)^{B(s,u)} over s. On R, Q(u)+Q(0) is linear. Thus the right side is either zero or 2^{-r}, according to whether x extends that linear functional. Exactly 2^r labels extend it. Hence

    ||sigmahat_Q||_1 = 2^{r/2}.

Fourier duality gives A_Q=sum_x sigmahat_Q(x)f(x), whose absolute value is at most that l1 norm because |f(x)|=1. QED.

### Theorem 2.2: no optimization gain, for any Boolean f

For every Boolean function,

    inf_Q [r(Q)+2 log_2(1+2 Lambda_Q(f))]
      = 2 log_2 M(f),                                   (2.4)

where the infimum is over every quadratic template, including affine ones.

Proof. Put b=2^{r/2}>=1. Equation (2.1) and Lemma 2.1 imply

    M = A_Q+2 Lambda_Q <= b+2 Lambda_Q
                            <= b(1+2 Lambda_Q).          (2.5)

Taking twice the logarithm proves that every proposed bound is at least 2 log_2 M. Conversely, choose any x and c in F_2 with (-1)^c f(x)=1, and take Q(s)=x.s+c. Its polar rank is zero and A_Q=1. Therefore 1+2 Lambda_Q=M, giving equality. QED.

The ordinary Shannon-versus-Renyi inequality is

    H(f) <= 2 log_2 M(f).

For completeness, with S sampled from p, Jensen gives H/2=E log_2(1/|a_S|)<=log_2 E(1/|a_S|)=log_2 M. Consequently (1.1) is valid but never improves this standard scalar estimate. It should not be presented as a stronger universal entropy bound.

### Generalization: changing the template family alone does not fix this

Let sigma be ANY Boolean sign function on the Fourier labels, b_sigma=||sigmahat||_1, and let Lambda_sigma be the l1 mass of disagreements. Fourier duality still gives |A_sigma|<=b_sigma, and b_sigma>=1 by Parseval. The same argument shows

    2 log_2(b_sigma+2 Lambda_sigma) >= 2 log_2 M,
    2 log_2 b_sigma+2 log_2(1+2 Lambda_sigma) >= 2 log_2 M. (2.6)

For every family containing affine signs, optimizing either expression gives equality with 2 log_2 M. Replacing quadratic templates by higher-degree Boolean templates, while charging them by this spectral-norm price, cannot rescue the proposal.

## 3. Even the rank-priced fibre refinement has the same obstruction

For a quadratic template, partition the Fourier labels by the radical cosets. In fibre t let l_t=sum_{s in t}|a_s|, with G_t and B_t the agreeing and disagreeing l1 masses. The previous exact Boolean restriction identity gives

    sum_t(G_t-B_t)^2=1,
    C_Q:=sum_t l_t^2=1+4 sum_t G_t B_t.                  (3.1)

There are 2^r fibres, including empty ones. Cauchy-Schwarz gives

    M^2=(sum_t l_t)^2 <= 2^r sum_t l_t^2.

Therefore the more precise rank-priced bound also obeys

    r+log_2(1+4 sum_t G_t B_t) >= 2 log_2 M,              (3.2)

and optimizing over Q again gives equality, attained by an affine template. In fact this conclusion is generic: for ANY partition into k cells, log_2 k+log_2 sum_t l_t^2>=2 log_2 M. The obstruction is not peculiar to quadratic Gauss sums.

This does not refute an entropy-aware adaptive partition. It says exactly what must not be discarded: the actual distribution of mass among fibres and the gap between Shannon and Renyi entropy within them.

Here is a precise accounting identity, included as a diagnostic rather than a new bound on FEI. For positive fibre masses m_t=sum_{s in t}p_s, define

    p_t(s)=p_s/m_t,
    e_t(s)=|a_s|/l_t,
    q_t=l_t^2/C_Q.

Then, in bits,

    H(p)=H(m)+log_2 C_Q-D(m||q)
                     -2 sum_t m_t D(p_t||e_t).          (3.3)

Proof. Within a fibre,

    2D(p_t||e_t)=2 log_2(l_t/sqrt(m_t))-H(p_t).

Average, apply H(p)=H(m)+sum m_t H(p_t), and expand D(m||q). QED. Zero-mass cells are omitted. Both negative relative-entropy terms are real, nonnegative credits. Dropping them and substituting H(m)<=r is exactly the scalar overestimate isolated above. Formula (3.3) does not prove that these credits have the required influence relation.

## 4. A balanced genuine Boolean family disproves the proposed O(I) payment

This section uses disjoint tribes, a standard Boolean construction, to settle the specific proposed template-payment question. It does not claim a new example for FEI itself.

For integer w>=1 put s=2^w and split ws independent bits into s blocks of w bits. Let A_j indicate that every bit in block j is one, and define

    g_w=2 prod_{j=1}^s(1-A_j)-1,
    F_w=z g_w,                                          (4.1)

where z is one additional independent uniform sign. Thus F_w is exactly balanced. Let delta=1/s, q=1-delta and u=q^s.

A factor 1-A_j has empty Fourier coefficient q, every nonempty coefficient of magnitude delta, squared norm q, and l1 norm 2q. Product factorization therefore gives

    M(F_w)=M(g_w)=|2u-1|+2[(2q)^s-u]
                    =1+2(2q)^s-4u.                     (4.2)

For s>=2, u<1/2. A bit is pivotal precisely when its other w-1 block bits are one and no other tribe fires. Consequently

    I(g_w)=2w q^{s-1},
    I(F_w)=1+2w q^{s-1} <= w+1.                         (4.3)

The last inequality follows from (1+1/(s-1))^{s-1}>=2. Also q^s>=1/4 for integers s>=2: the function t log(1-1/t) is increasing for t>=2, since -log(1-x)<=x/(1-x). Substitution into (4.2) gives

    M(F_w)=1+u(2^{s+1}-4) >= 2^{s-1}.

By Theorem 2.2 and (4.3),

    inf_Q [r(Q)+2 log_2(1+2 Lambda_Q(F_w))] / I(F_w)
      >= 2(2^w-1)/(w+1) -> infinity.                    (4.4)

The same lower bound applies to the optimized rank-priced fibre expression (3.2), and to the broader spectral-norm template expressions (2.6). Thus the proposed uniform payment is FALSE, not merely awaiting a clever choice of template. Balance does not rescue it.

### The actual Shannon ratio stays bounded

An exact calculation shows how severely the surrogate overcounts. Normalize the squared Fourier coefficients of 1-A_j by q. Its probability law beta has mass q at the empty set and delta^2/q at each nonempty set. Hence

    H(beta)=h_2(delta)+delta log_2(s-1)
           =(2delta-1)log_2 q+2w delta.

Let v=4u(1-u), the nonempty spectral mass of g_w. Conditional on being nonempty, its spectral law is beta^{tensor s} conditioned away from its empty atom of mass u. Therefore

    H(F_w)=H(g_w)=h_2(v)+4u[sH(beta)-h_2(u)].             (4.5)

As w tends to infinity, u->e^{-1}, sH(beta)=2w+1/ln2+o(1), and

    H(F_w)=8w/e+O(1),
    I(F_w)=2w/e+O(1),
    H(F_w)/I(F_w)->4.                                   (4.6)

No large truth tables are being inferred from a search. Equations (4.2)-(4.6) are analytic. For w=10, the exactly balanced function has 10,241 variables, the surrogate/influence ratio is at least 186, while its actual H/I from (4.5) is approximately 3.64842. For w=16 the corresponding lower bound is 7,710, while H/I is approximately 3.77224. These are evaluations of the proved formulas, not enumerations.

With one fibre, (3.3) reduces to H=2 log_2 M-2D(p||e), where e_s=|a_s|/M. Thus this family has an enormous relative-entropy correction that cannot be discarded. This is not a refutation of FEI: the genuine Shannon ratio tends to four.

### A stronger obstruction inside the exact quadratic-phase class itself

The failure is not merely caused by tribes lacking a suitable exact quadratic phase. The recursive-majority family already used for sharpness in the previous report also refutes the global payment, even though it HAS an exact quadratic Fourier phase.

Let f_0=x_1 and f_{d+1}=Maj_3(f_d^{(1)},f_d^{(2)},f_d^{(3)}) on disjoint copies. The gate is (x+y+z-xyz)/2. Every nonzero spectral set has odd size and coefficient sign

    sign(a_s)=(-1)^{(|s|-1)/2}
             =(-1)^{sum_{i<j} s_i s_j}.                 (4.7)

To check the induction, a singleton outer Fourier term inherits one child sign. The triple term adds one minus sign to the product of three child signs, giving exponent 1+sum_j(|s_j|-1)/2=(|s|-1)/2. Disjointness and zero child means exclude Fourier collisions. Thus the phase in (4.7) really is quadratic in the original coordinates at every depth.

The same disjoint expansion gives the exact recursions

    M_0=1,        M_{d+1}=(3M_d+M_d^3)/2,
    I_d=(3/2)^d,  H_d=4((3/2)^d-1).                     (4.8)

Here M_1=2, and M_{d+1}>=M_d^3/2 implies

    2 log_2 M_d >= 3^{d-1}+1  (d>=1).                  (4.9)

Indeed, b_d=log_2 M_d satisfies b_1=1 and b_{d+1}>=3b_d-1, yielding b_d>=(3^{d-1}+1)/2. Theorems 2.2 and (3.2) therefore imply

    optimized global phase cost / I_d >= 2^d/3,        (4.10)

whereas H_d/I_d=4(1-(2/3)^d)<4.

There is an additional useful conclusion: EVERY exact quadratic completion for f_d, not only the displayed complete-graph completion, has

    r(Q) >= log_2 |supp fhat_d| >= 2*3^{d-1}.           (4.11)

Indeed support size satisfies k_1=4 and k_{d+1}=3k_d+k_d^3, so k_d>=4^{3^{d-1}}. The preceding support-compression theorem says k_d<=2^{r(Q)} for every exact completion. Even without that theorem, Lemma 2.1 with Lambda_Q=0 gives the weaker lower bound r(Q)>=2 log_2 M_d>=3^{d-1}+1. Thus changing the exact completion cannot make polar rank O(I) on this family. The obstruction persists inside balanced, odd, read-once ternary-majority formulas for which FEI is already proved sharply. Recursive majority and its H/I formula are prior ingredients; the new conclusion is their obstruction to all optimized global template and rank budgets.

## 5. Continuing at Shannon scale: a coupled local inequality

The previous section rules out one global sufficient target. It does not rule out direct logarithmic/erasure estimates. The established erasure formulation is the appropriate starting point rather than a fresh positive-power majorant.

Let h=h_2 and define, for x in [0,1],

    R(x)=1-h(1/2+sqrt(x(1-x))).

### Theorem 5.1: a certified scalar tradeoff

For every x in [0,1],

    R(x) <= h(x)/8+(9/4)min{x,1-x}.                     (5.1)

The proof combines analytic endpoint bounds and an exact rational interval certificate for a compact interval.

Proof. It suffices by symmetry to consider 0<=x<=1/2. Put y=2sqrt(x(1-x)). For 0<x<1/2,

    R'(x)=2(1-2x)atanh(y)/(y ln2),
    0<=R'(x)<=2/ln2<3.                                 (5.2)

The middle inequality follows from atanh(y)<=y/sqrt(1-y^2): subtract their derivatives and integrate from zero. Continuity handles the endpoints. For 0<=x<=1/64, h(x)>=x log_2(1/x)>=6x. Thus h(x)/8+9x/4>=3x>=R(x), using R(0)=0.

On [1/65,1/2], let d(x)=9x/4+h(x)/8-R(x). Since 0<=h'(x)<=6 and (5.2) holds, |d'(x)|<=3. To certify d>0 throughout this interval, use the 225 rational nodes

    t_k=k/256, k=32,...,256,
    x_k=t_k^2/(1+t_k^2),
    q_k=(1+t_k)^2/[2(1+t_k^2)].

Then x_32=1/65, x_256=1/2 and (q_k-1/2)^2=x_k(1-x_k), with q_k>=1/2. Thus

    d(x_k)=9x_k/4-1+h(x_k)/8+h(q_k)

can be enclosed using rational logarithm intervals with no square-root approximation. The checker proves, for every one of the 224 adjacent cells,

    min{lower(d(x_k)),lower(d(x_{k+1}))}
      -(3/2)(x_{k+1}-x_k) > 1/1000.                    (5.3)

Every point in a cell is within half its width of an endpoint. The Lipschitz bound and (5.3) certify the full interval. It overlaps the analytic tail, so all x<=1/2 are covered. Reflecting x proves (5.1) on the other half. QED.

The logarithm enclosure is self-contained. Reduce a positive rational to 2^k y with 1<=y<2, set z=(y-1)/(y+1), and use 40 terms of

    ln y=2 sum_{j>=0} z^{2j+1}/(2j+1).

The omitted tail is between zero and 2z^{81}/[81(1-z^2)]. The same construction encloses ln2, with certified 2/3<ln2<3/4. All arithmetic in (5.3) uses Python Fraction and integer comparisons. The minimum certified cell margin is approximately 0.001818814; the theorem uses only its exact lower bound 1/1000, not that decimal. An initial 128-step exploratory enclosure was too coarse; that failed enclosure was not a counterexample to (5.1).

### Theorem 5.2: a universal restriction estimate

Let X have spectral law p. Write

    B_i(f)=H(X_i|X_{-i}),
    m_i(f)=sum_{T:i notin T} min(p_T,p_{T+i}),
    Delta_i=H(f)-[H(f_{i=0})+H(f_{i=1})]/2.

Then every Boolean f and every coordinate i satisfy

    Delta_i <= (9/8)B_i+(9/4)m_i
             <= (9/8)B_i+(9/4)Inf_i(f).                 (5.4)

Proof. On a Fourier pair u=a_T, v=a_{T+i}, write m=u^2+v^2 and x=v^2/m, excluding m=0. The conditional spectral entropy contribution is m h(x). Restricting the physical bit gives Fourier coefficients u+v and u-v, so the exact Jensen-Shannon contribution is mR(x). Thus

    Delta_i=B_i+sum_T mR(x).

Apply (5.1) and sum: m min(x,1-x)=min(u^2,v^2). Finally m_i<=sum_T v^2=Inf_i. No independence of spectral bits is assumed. QED.

### Corollary 5.3: conditional transfer, not an unconditional FEI bound

Define K_E=sup_f B(f)/I(f), B=sum_i B_i, and C_FEI=sup_f H(f)/I(f), over nonconstant Boolean functions in all dimensions. Then

    K_E <= C_FEI
        <= min{K_E+2/ln2, (9/8)K_E+9/4}.                (5.5)

The first and the first upper bound are inherited. For the second, assume a finite uniform B<=K I. Summing (5.4) gives sum_i Delta_i<=(9K/8+9/4)I. Irrelevant coordinates have Delta_i=0, so a relevant coordinate obeys Delta_i<=(9K/8+9/4)Inf_i. The exact physical restriction identity is I(f)=Inf_i+[I(f_0)+I(f_1)]/2. Induction on n proves H<=(9K/8+9/4)I. Taking infima in K yields (5.5); if K_E is infinite the implication supplies no finite bound.

The new upper comparison is smaller than K_E+2/ln2 when K_E<16/ln2-18, approximately 5.08312. It is an auxiliary improvement in the conversion of a still-unproved estimate. In particular, K_E=4 is not an admissible proved input: the already archived 80-variable example refutes it. No concrete universal FEI constant is announced here.

## 6. Attempts that did not improve the full-problem bound

The exploratory algorithms and actual outputs are preserved separately and labelled floating/unverified. Their internal names referring to a lower value do not constitute rigorous interval lower bounds.

First, exhaustive small-cube calculations reproduced maximum B/I values approximately 2, 2.67249 and 2.70415 in dimensions two, three and four. They do not provide a universal bound.

Second, I examined recursive balanced monotone gates. The complete five-input seed enumeration contains 621 balanced monotone truth tables, grouped into 15 signatures used by the exploratory recursion. The largest computed depth-30 erasure ratio was approximately 3.52347. This is below the already archived >4.007 witness, so it is not a new lower-bound record. A four-input recursion also reproduced growing absolute adjacent-amplitude overlap relative to influence; the archived addressing/overlap results already rule out that kind of majorant. It is not counted as a new obstruction.

Third, a seeded search of 20,000 disjoint AND/OR-tree iterations, allowing up to 512 leaves, found a best floating erasure ratio about 3.15063 on 459 leaves. The code had a 35-second safety cap but completed all 20,000 iterations in the observed run. No independent exact certificate was made for that candidate because it did not improve the known frontier. Its expression and output are retained, not promoted to a theorem.

These failures motivated the return to exact Shannon-level inequalities in Section 5. A repeated small search or another fractional-power penalty is not the next proposed route.

## 7. Exact remaining full-scope obligation

A source-exact live target remains

    sum_{unordered spectral cube edges {S,T}}
        min(p_S,p_T) |log_2(p_S/p_T)|
       <= C sum_S |S|p_S,                               (7.1)

with zero-endpoint terms set to zero, under ALL signed Boolean constraints

    sum_S a_S a_{S xor U}=1_{U=0}.                       (7.2)

The archived results prove that finiteness in (7.1) is equivalent, up to additive constants, to finiteness of K_E and full FEI. They also prove that fixed positive-power substitutes are false. This continuation does not remove that gap.

What changed is precise. The proposed global phase-l1 budget is now ruled out even after optimal template selection and even for exactly balanced f. The same obstruction applies to rank-priced global fibre norms and broader spectral-norm template families. A viable phase argument must retain mass-weighted Shannon information or supply an actual nonreusing physical restriction payment; it cannot close the conjecture by improving the scalar global-template optimizer.

The remaining challenge is not the already-paid Jensen-Shannon scalar remainder alone. Equation (5.4) improves that accounting, but the unbounded-dimensional logarithmic erasure term still requires a genuinely Boolean allocation argument. Formula (3.3) identifies which negative credits cannot be dropped, without asserting that writing those credits down bounds them.

## 8. Verification, sources, and delivery discipline

`verify_continuation.py --part all --output verification.json` executed successfully twice in separate local processes, with byte-identical JSON output. It checks:

* all 2,198 quadratic templates across dimensions zero through four, including their exact Walsh supports and amplitudes;
* all 134,250,772 Boolean-function/template pairs in those dimensions, with exact correlation ceilings and the optimized scalar equality;
* all 33,044 Boolean-function/template fibre cases through dimension three, with the exact norm/cancellation identities;
* the 224 rational interval cells for Theorem 5.1, combined with its analytic tails and Lipschitz proof;
* full integer truth tables for tribes at w=1,2 and their balanced lifts, exact M and I formulas, and rational-interval consistency of the entropy formula;
* exact majority-recursion bounds through depth eight and a separately materialized nine-bit case verifying the phase, M=7, I=9/4, H=5 and support 76.

The large pair count is a finite exhaustive test, not millions of independent discoveries and not universal FEI coverage. Sections 2-4 have analytic proofs independent of the finite checks. Theorem 5.1 is explicitly computer-assisted through its finite rational certificate. Large-w formula evaluations are not large-dimensional truth-table enumerations. The exploratory searches are not certificate inputs.

Primary literature consulted on 21 September 2026 includes O'Donnell-Tan, arXiv:1304.1347, for established composition methodology; Shalev, arXiv:1806.03646, for spectral-norm/extremal-class context; and Gonzalez-MacManus-Pereyra, arXiv:2606.00246, for the existing restriction/stopping framework and known tribes examples. Searches concerning spectral norms, Renyi entropy, quadratic signs, erasure entropy, and the rational comparison constants were bounded, not exhaustive priority clearance. The proofs above do not depend on importing an unverified new full-FEI theorem.

The report intentionally uses the actual erasure source rather than a pointwise shorthand in an old synthesis: K_E<=C_FEI<=K_E+2/ln2 is a comparison of universal suprema obtained by induction. It does not state H(f)<=B(f)+(2/ln2)I(f) separately for every f. No such stronger pointwise assertion is used here.

Claim ledger:

    PROVED_ANALYTIC_SELF_CHECKED:
      exact optimized global phase-template collapse;
      general spectral-norm template and rank-priced partition obstructions;
      balanced Boolean counterfamilies to every proposed global O(I) payment;
      unbounded minimum exact quadratic-phase rank/influence on recursive majority;
      exact tribes norms, influence, entropy formula and Shannon-ratio limit;
      mass-aware relative-entropy accounting identity.

    PROVED_WITH_RATIONAL_INTERVAL_CERTIFICATE_SELF_CHECKED:
      R(x)<=h2(x)/8+(9/4)min(x,1-x);
      Delta_i<=(9/8)B_i+(9/4)m_i;
      conditional universal-constant comparison (5.5).

    PRIOR_RESULTS_NOT_REANNOUNCED:
      erasure equivalence, logarithmic target, positive-power obstructions;
      B/I>4.007 archived witness; composition and tribes methodology.

    EXPLORATORY_NO_IMPROVEMENT:
      balanced monotone-gate recursion and randomized AND/OR-tree searches.

    OPEN:
      any finite universal upper bound on K_E or (7.1);
      full FEI and the unrestricted quadratic-phase Shannon inequality.

Prior reports remain unchanged. This package is private research input, not public publication, production truth promotion, an audit certificate, or a statement that another worker has consumed it. A separate source-bound handoff is delivered to the brain repository. Native database ingestion is not claimed.
