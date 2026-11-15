# FEIB25 proofs

Unless marked otherwise, all functions f below take values in {-1,1}, all measures are uniform, and all entropies/logarithms are in bits. Let c_S=f̂(S), μ(S)=c_S², W_d=Σ_{|S|=d}μ(S), I=Σ d W_d, and δ_i=Inf_i(f). A zero-mass summand is zero. The paper's conventions and imported results are recorded in PAPER.md.

## 1. Edge identities and the FEI equivalence — PROVED

For i fixed, write f=g+x_i h, g=E_i f, h=D_i f, and for T not containing i put a=c_T and b=c_{T+i}. Summing the squared coefficients over each pair is the distribution of U\{i}. The entropy chain rule gives

    E_i=H(1[i∈U] | U\{i})=Σ_T Φ(a²,b²).

Split Φ into its two directed summands. The upper summand is b² log2(1+a²/b²); its sum over i and T is G=Σ_d A_d. Since ln(1+t)≤t,

    Σ_{i,T} a² log2(1+b²/a²) ≤ Σ_{i,T} b²/ln 2 = I/ln 2.
    G ≤ H^−:=Σ_i E_i ≤ G+I/ln 2.                         (E1)

Choose any ordering of the coordinates. Conditioning on all other coordinates gives no more entropy than conditioning on preceding coordinates. Summing the latter conditional entropies by the chain rule proves Han's inequality here directly:

    H^−≤H(μ).                                           (E2)

For completeness, the reverse implication needs closure under restriction, not a pointwise lower bound on H^−. Let P_±(T)=(a±b)². Their average is a²+b². By the entropy formula for a mixture,

    H(f)−[H(f_{i=1})+H(f_{i=−1})]/2 = E_i+J_i,

where J_i is the Jensen–Shannon divergence of P_+ and P_−. For each pair let t=2ab/(a²+b²), |t|≤1. Its contribution to J_i is (a²+b²)[1−h_2((1+t)/2)]. The series

    1−h_2((1+t)/2)
      = (1/ln 2) Σ_{k≥1} t^{2k}/[(2k)(2k−1)] ≤ t²

follows because the coefficients are nonnegative and their sum is ln 2. Thus J_i≤Σ_T 4a²b²/(a²+b²)≤4δ_i. This nonsharp constant is sufficient.

If H^−(f)≤C I(f) for every Boolean f, a weighted average supplies a live coordinate with E_i≤C δ_i. Query that coordinate, recurse on both Boolean restrictions, and use

    I(f)=δ_i+[I(f_{i=1})+I(f_{i=−1})]/2.

Induction on the remaining dimension gives H(f)≤(C+4)I(f). Conversely FEI implies the erasure bound by (E2). Together with (E1), this proves the claimed equivalence with Σ A_d≤C'I. No equivalence is asserted for arbitrary real spectra.

## 2. Universal bounds from adjacent level masses — PROVED

The perspective F(q,p)=q log2(1+p/q) is concave and homogeneous on nonnegative arguments. Jensen, or the log-sum inequality applied with weights proportional to q, gives Σ F(q_e,p_e)≤F(Σq_e,Σp_e). Over edges from level d−1 to d,

    Σq_e=d W_d,       Σp_e=(n−d+1)W_{d−1}.

Consequently

    A_d ≤ d W_d log2(1+(n−d+1)W_{d−1}/(d W_d)).         (J)

For q=0 the limiting contribution is zero; if all q are zero then A_d=0. If p=0 all directed contributions vanish. Uniform mass within each of the two adjacent levels makes (J) an equality. Its dimension dependence cannot be removed using probability distributions alone.

The elementary inequality ln(1+x²)≤x holds for x≥0: its left derivative is 2x/(1+x²)≤1 and both sides vanish at zero. Therefore

    q log2(1+p/q) ≤ √(pq)/ln 2.

Cauchy–Schwarz on the edge sum gives the additional valid bound

    A_d ≤ √[d(n−d+1)W_d W_{d−1}]/ln 2.                (S)

Neither estimate invokes Booleanity.

## 3. No lower-level-only repair is possible — PROVED

Let m=2r+1 with r≥1, M_m be majority on y_1,...,y_m, and

    b=binom(2r,r)/4^r.

The majority function is odd, hence has zero mean. Its singleton coefficient is b: conditioning on the other 2r signs, changing y_j changes majority precisely when those signs tie. The derivative is then 1, and its mean is the tie probability b.

Take a fresh selector z and set

    h(z,y)=(1+z)/2+(1−z)M_m(y)/2.

For z=1 this is 1; for z=−1 it is M_m, so h is Boolean. Its mean, selector coefficient and m ordinary singleton coefficients are respectively

    ĥ(∅)=1/2,    ĥ({z})=1/2,    ĥ({y_j})=b/2.

It follows directly from the definition of A_1 that

    A_1(h)=1/4+(m b²/4) log2(1+1/b²),
    W_0(h)=1/4,       W_1(h)=(1+m b²)/4.               (C1)

Now take d−1 fresh variables and multiply h by their parity χ_R, |R|=d−1. Fourier support consists exactly of R∪T with coefficient ĥ(T). Thus all levels below d−1 vanish, W_{d−1}=W_0(h), W_d=W_1(h), and A_d=A_1(h). Removing any element of R leads outside the support and costs zero; removing an element of T reproduces the edge cost of h. More generally,

    W_{k+d−1}(χ_R h)=W_k(h),
    A_{k+d−1}(χ_R h)=A_k(h),     k≥1.                 (C2)

Here is a self-contained divergence estimate. Write b_r=binom(2r,r)/4^r. Then b_1²=1/4 and b_{r+1}²/b_r²=(2r+1)²/[4(r+1)²]. By induction

    1/(4r) ≤ b_r² ≤ 1/(r+1).                         (C3)

For the lower induction step the required comparison is (2r+1)²≥4r(r+1). For the upper step it is (2r+1)²(r+2)≤4(r+1)³; the difference between right and left is 3r+2. Both hold. Substituting (C3) into (C1) yields

    A_d(χ_R h) ≥ 1/4+(1/8)log2(r+2) → ∞.             (C4)

For each fixed d, every expression Σ_{k=0}^d c_{d,k} W_k with finite dimension-independent coefficients is bounded in magnitude by max_k |c_{d,k}|, since ΣW_k≤1. This contradicts (C4). In particular L1 is false for every universal C. L2 remains false after adding any fixed finite weights on W_{d−2},...,W_0. Weights may depend on d and the conclusion still holds at that fixed d. There is therefore no weakest successful choice of such lower-level weights.

This is not a FEI counterexample. The selector influence is 1/2; each y_j has influence b/2. Each parity variable is always pivotal. Hence

    I(χ_R h)=d−1/2+m b/2.

The bounds in (C3) imply m/(4√r)≤mb/2≤m/(2√(r+1)), and (C1) gives A_d≤1/4+(1/2)log2(1+4r). Thus I grows as √m and A_d grows as log m. The unresolved issue is how to charge such costs to the tail across all d without counting the same tail mass repeatedly.

## 4. Explicit low-level Boolean inequalities — PROVED

Since D_i f∈{−1,0,1}, E|D_i f|=δ_i. Every Fourier coefficient containing i is a coefficient of D_i f after deleting i, so

    |c_S|≤δ_i for i∈S.                               (B)

In particular |c_i|≤δ_i and |c_{ij}|≤min(δ_i,δ_j). This is a finite-range Boolean fact, stronger than a bound from its L2 norm.

For A_1, apply the scalar inequality in §2 with p=c_∅², q=c_i², then (B):

    A_1 ≤ |c_∅| Σ_i |c_i|/ln 2
        ≤ √W_0 I/ln 2.                               (L1-low)

Combining it with (J) and (S) gives

    A_1 ≤ min{ √W_0 I/ln 2,
               W_1 log2(1+n W_0/W_1),
               √(n W_0 W_1)/ln 2 }.

Zero cases use the conventions above. If W_0=0 then A_1=0. The construction in §3 shows why W_0,W_1 alone, with fixed linear coefficients, cannot give a dimension-independent bound.

For A_2 write its two orientations explicitly:

    A_2=Σ_j Σ_{i≠j} c_{ij}² log2(1+c_j²/c_{ij}²).

The scalar inequality and (B), in sequence, imply

    A_2 ≤ (1/ln 2)Σ_j |c_j| Σ_{i≠j}|c_{ij}|
        ≤ (1/ln 2)Σ_j |c_j|(I−δ_j)
        ≤ (I²−Σ_j δ_j²)/ln 2
        ≤ (I²−W_1)/ln 2.                              (L2-low)

For the third line, use |c_j|≤δ_j and I−δ_j≥0 term by term. For the last line, square |c_j|≤δ_j and sum. This proves a clean dimension-independent A_2 inequality that uses Booleanity, albeit with a quadratic I term. It is particularly useful when I is small and is exact at zero for a dictator. No novelty claim is made and it does not prove FEI. A useful combined version is

    A_2 ≤ min{ (I²−W_1)/ln 2,
               2W_2 log2(1+(n−1)W_1/(2W_2)),
               √[2(n−1)W_1 W_2]/ln 2 }.

Why hypercontractivity alone cannot imply (L2-low): take the normalized real degree-two polynomial whose squared coefficients are 1/(2n) at each singleton and 1/(2 binom(n,2)) at each pair. It has W_1=W_2=1/2, I=3/2, and

    A_2=log2((n+1)/2) →∞.

Every real degree-two polynomial satisfies the same hypercontractive theorem. Thus (L2-low) requires an additional property, here precisely (B). This example is not Boolean: at the all-positive input the sum of its positive coefficients exceeds 1.

## 5. The known logarithmic bound in edge form — PROVED conditional on the paper's technical corollary

The imported result is Corollary 6.7, transcribed in PAPER.md. The deduction below supplies all intervening entropy/edge steps. It is not an independent proof of that deep corollary.

First work with a nonconstant indicator F in the paper's {0,1} convention and use bit logarithms; changing the paper's natural-log entropy only changes absolute constants. Choose the complement so p=EF≤1/2, and set v=p(1−p). Then ||F||_2²=p≤2v. For any projection g onto a collection of nonempty coefficients of F, ||g||_2²≤v and I_i[g]≤I_i[F]. Thus

    ||F||_2^{3/4}||g||_2^{3/4}≤2v^{3/4},
    ||F||_2||g||_2≤2v,
    I[F,g]≤I[F],          v≤I[F].                     (P1)

Choose M=10^5, B=10^6 and L=8M(B+64). For d≥1 set t_d=d log2(d+1). For k≥0 partition positive degree-d coefficients into bins

    2^{-L(k+1)t_d}√v < |F̂(S)| ≤ 2^{-Lk t_d}√v.

Zeros contribute nothing. For k≥1 let g be the projection onto this bin and m_{d,k}=<F,g>. Apply Corollary 6.7 with α=1 and

    δ=2^{-64k}(d+1)^{-B}≤d^{-96000}.

Since ĝ(S)=F̂(S) in the bin, max |F̂(S)ĝ(S)|^{1/4}≤2^{-Lk t_d/2}v^{1/4}. Multiplying v^{1/4} by the norm bound 2v^{3/4} gives 2v. Using the weaker exponent 1/32 discussed in PAPER.md gives

    m_{d,k} ≤ 2v δ^{-Md}2^{-Lk t_d/2}
                  + δ^{1/32}I[F]+2δv.                 (P2)

This is the log-bearing step. In detail,

    log2(δ^{-Md})=Md[64k+B log2(d+1)].                (*)

Because k≥1 and log2(d+1)≥1, the bracket is at most (B+64)k log2(d+1). The negative exponent Lk t_d/2 is four times that upper bound. Thus the first term of (P2) is at most 2v·2^{-3M(B+64)k d log2(d+1)}, which is bounded by 2^{-k}(d+1)^{-10}I[F]. The other two terms are also at most that same bound: δ^{1/32}=2^{-2k}(d+1)^{-31250}, and 2δv≤2^{1−64k}(d+1)^{-B}I[F]. Therefore

    m_{d,k}≤3·2^{-k}(d+1)^{-10}I[F].                 (P3)

For a coefficient in bin (d,k), its entropy multiplier is at most

    log2(1/F̂(S)²)≤2L(k+1)t_d+log2(1/v).

The k≥1 part involving t_d is consequently bounded by

    6L I[F] Σ_{d≥1} d log2(d+1)/(d+1)^10
                    Σ_{k≥1}(k+1)2^{-k} = O(I[F]).

Both sums converge, as is also clear by comparison with Σd^{-8} and the differentiated geometric series. For k=0 the same multiplier bounds its t_d part by 2LΣ_d t_d W_d(F). Across every bin, the remaining log2(1/v) part is at most v log2(1/v), since total nonempty Fourier weight is v.

For clarity that last term is O(I[F]) for an indicator: edge isoperimetry gives I[F]≥(p/2)log2(1/p) in the paper's spectral convention. Here is the elementary induction: assume pivotal influence B of each section of density a or b is at least 2a log2(1/a) or 2b log2(1/b). The internal coordinates contribute their average, and the new coordinate contributes at least |a−b|. Hence B_n≥a log2(1/a)+b log2(1/b)+|a−b|. With p=(a+b)/2, the deficit between the first two terms and 2p log2(1/p) is 2p[1−h_2(a/(a+b))]≤|a−b|, from h_2(t)≥1−|2t−1|. The base dimension is immediate, so the induction proves B_n≥2p log2(1/p). Dividing by four proves the displayed spectral bound. Also v≥p/2 and v≤p, so

    v log2(1/v)≤p[log2(1/p)+1]≤2p log2(1/p)≤4I[F].

The empty-character entropy p² log2(1/p²)≤2p log2(1/p) is paid by the same influence bound. Hence

    H_2(F̂²)≤C[Σ_{d≥1} d log2(d+1)W_d(F)+I[F]].      (P4)

This proves the full-entropy consequence for the chosen small-mean indicator, which is sufficient for the conversion below. It also explains the additive term in Theorem 1.3. Constant ±1 functions have zero entropy and influence and are handled directly.

Convert to the brief's convention with F=(1+f)/2, choosing the sign of f so EF≤1/2. For S≠∅, μ_f(S)=4F̂(S)² and I(f)=4I[F]. Thus

    Σ_{S≠∅} μ_f(S)log2(1/μ_f(S))
      =4Σ_{S≠∅}F̂(S)²log2(1/F̂(S)²)−2Σ_{S≠∅}μ_f(S)
      ≤4H_2(F̂²).

For x=W_0(f), x log2(1/x)≤(1−x)/ln 2≤I(f)/ln 2. Combining this fact with (P4), and noting d log2(d+1)≥d, gives

    H(μ_f)≤C_0 Σ_d d log2(d+1)W_d(f).

Finally use (E2), without a new loss:

    Σ_i E_i(f)≤H(μ_f)≤C_0 E[|U|log2(|U|+1)].        (LOG)

No explicit optimized C_0 is claimed. All constants above were deliberately loose to make the deduction robust to the exponent discrepancy in the accessible technical corollary.

## 6. Exactly what is and is not tight — PROVED examples; unresolved Boolean sharpness

The sole source of the degree logarithm in the deduction (P1)–(LOG) is (*) with polynomially small δ: canceling exp(Θ(d log d)) requires a cutoff of that scale. The subsequent bin-zero entropy estimate retains this cutoff. Removing log d from that estimate without strengthening its input would be unjustified.

A normalized non-Boolean spectrum can really have edge cost of this size. Put uniform mass 1/2 on level d−1 and uniform mass 1/2 on level d in dimension n=d². Every relevant lower/upper ratio is (n−d+1)/d, so

    G=A_d=(d/2)log2(1+(n−d+1)/d),   I=d−1/2.

Thus G/I grows logarithmically in d and (J) is an equality. Positive square-root Fourier coefficients realize this as a real polynomial, which exceeds 1 at the all-positive input. In contrast, mass uniformly on level d alone also has large entropy but zero erasure entropy. Passing through H^−≤H can therefore hide major slack.

Booleanity does not prohibit an individual degree-d coefficient as small as exp(−Θ(d log d)) after variance normalization. For AND on m coordinates, c_S=±2^{1−m} for every nonempty S and var=2^{2−m}(1−2^{-m}); choosing m of order d log d gives that scale. But its total influence pays for these low-level coefficients. It does not saturate the global logarithmic FEI upper bound.

I do not know a Boolean family that makes the paper's global d log d loss necessary, nor a proof that all Boolean families avoid it. The construction in §3 shows that substantial fixed-level edge cost is possible for Boolean functions, but its tail pays. It would be false to say the logarithm has been shown to arise only for non-Boolean spectra.

The unused stronger Boolean identities are pointwise g h=0 and g²+h²=1 in f=g+x_i h. In Fourier variables the first imposes signed convolution cancellation at every character; the second constrains the sum of two autocorrelations. The paper's norm/maximum estimates use finite-range derivative norms but discard much of this signed information. The exact restriction identity in §1 gives another route: control E_i at one suitable coordinate of every restriction. Neither observation by itself supplies the missing inequality.

## 7. Proof of the two elementary imported lemmas — PROVED

For Lemma 2.7, set J=[n]\I. Fix S⊆I. The restricted coefficient is

    ĝ_{J→z}(S)=Σ_{R⊆J} ĝ(S∪R)χ_R(z).

Squaring and averaging over uniform z∈{0,1}^J eliminates terms R≠R′ by orthogonality. The remaining terms sum to Σ_{R⊆J} ĝ(S∪R)², precisely the claimed slice. This is the restriction mechanism that turns generalized Fourier information into ordinary coefficients.

For Lemma 3.5, pointwise max_i h_i²≤(Σ_i h_i^4)^{1/2}. Concavity of the square root gives

    E max_i h_i² ≤ (Σ_i E h_i^4)^{1/2}.

The paper's Theorem 2.8 at q=4 gives E h_i^4≤9^d||h_i||_2^4. Hence the last display is at most

    3^d (Σ_i ||h_i||_2^4)^{1/2}
      ≤3^d max_i ||h_i||_2 (Σ_i ||h_i||_2²)^{1/2},

which is the statement. Notice that this estimate uses the degree bound and norms, with no signed cancellation.

## 8. Matching-tower recurrence — PROVED; implementations CHECKED NUMERICALLY

Let F be the Boolean nine-input perfect-matching host and let an identical Boolean g of mean a be substituted into every disjoint block. Write P(t)=Σ_{k≥1}W_k(g)t^k and

    b_R(a)=Σ_{Q⊇R} F̂(Q)a^{|Q|−|R|}.

Expanding each g into its mean plus its nonempty Fourier terms shows that a coefficient whose nonempty blocks are exactly R is b_R(a) times the product of the corresponding nonempty coefficients of g. Summing their squares by total degree proves

    W_{F∘g}(t)=Σ_R b_R(a)² P(t)^{|R|}.

Suppose the singleton coefficients of g are all c, as they are for these transitive towers, and g has n coordinates. Let A_int(t)=Σ_{k≥2}A_k(g)t^k. An edge deleting a variable within a block has two cases. If that block stays nonempty, both coefficients retain the same b_R factor, so its ratio is the inner ratio and its total cost is the inner A_int times the other blocks' squared weights. If the block becomes empty, its upper coefficient contains c while its lower coefficient changes b_R to b_{R\j}. Therefore

    A_{F∘g}(t)
      = A_int(t) Σ_R |R| b_R² P(t)^{|R|−1}
        +t n c² Σ_{R≠∅} Σ_{j∈R}
              b_R² log2(1+b_{R\j}²/(b_R²c²)) P(t)^{|R|−1}.

Zero upper coefficients contribute zero. This proves towers.py and towers_decimal.py. They compute derivatives b_R by a weighted superset transform and polynomial coefficients by convolution. The recurrence was checked against the host truth table and a nine-variable truth table for a biased three-input composition (tower_audit.json). The initial binary64 output underflowed in extremely small tails. The primary full profiles, towers_decimal_50.json, use 50-digit Decimal arithmetic with an extended exponent range; an independent 40-digit run checks precision stability at every W and A coefficient (tower_precision_audit.json). These are exact algebraic recurrences evaluated numerically, not symbolic exact logarithms or large-tower truth-table enumerations.

## 9. What I would try next — HEURISTIC, one-page assessment

The obstruction is not a missing coefficient on W_{d−2}. At a fixed d, the selector-majority construction defeats every finite linear combination of W_0,...,W_d. Its many small singleton coefficients create a logarithm beside a constant mean. An independent parity moves that configuration to any desired level. The Boolean constraint is fully respected. Any successful level argument must see higher degrees or use a potential that transfers payment between levels.

The evidence for a tail-payment approach is concrete. For selector-majority the cost is logarithmic while influence is of square-root order. For the matching towers, all computed level costs remain small relative to the full influence even as the adjacent-level ratio rises. The candidate A_d≤C[dW_d+(d−1)W_{d−1}+Σ_{k>d}kW_k] survives the saved finite data with C=1. This is only a computational observation. Summing it over d charges one coefficient many times and cannot prove FEI.

The evidence against an easy fix is equally concrete. Normalized real polynomials supported on two adjacent levels can have edge entropy of order d log d and influence of order d. They saturate the elementary level Jensen bound exactly. Thus replacing it with a distribution-only inequality cannot work. The paper's polynomial δ cutoff produces the same scale through a maximum-coefficient estimate. Booleanity must do more than supply Parseval or ordinary hypercontractivity.

What Booleanity offers is signed compatibility across the spectrum. For f=g+x_i h, the pointwise identities gh=0 and g²+h²=1 couple the derivative spectrum with the complementary spectrum at every shift. The elementary bound |f̂(S)|≤Inf_i already gives a useful low-level improvement, A_2≤(I²−W_1)/ln 2. But it loses the placement and signs of the derivative coefficients, and its quadratic influence term is too large for the intended conjecture.

The next lemma I would try is a transport statement with a bounded payment budget: find nonnegative charges Q_d(f) with A_d≤C dW_d+Q_d and Σ_d Q_d≤C I. The charges should be built from the signed convolution identities, not from a full tail sum assigned independently to every d. One concrete starting point is to prove the truncated estimate Σ_{d≤D} A_d≤CΣ_{d≤D}dW_d+CΣ_{d>D}dW_d uniformly in D, first for the selector/composition class with its exact boundary recurrence. The all-D version includes FEI at D=n, so that target is a research program rather than a claimed reduction in difficulty. A more modest first milestone is the same estimate at D=2 with a linear I term and a short proof using gh=0, improving the quadratic estimate above without importing the paper's technical theorem.

I believe the failure is in paying for overlapping edge costs without reuse. The calculations support that view but do not identify the required transport. The general log removal, the best tail weights, and any asymptotic Boolean sharpness of the paper's logarithmic bound remain open here.
