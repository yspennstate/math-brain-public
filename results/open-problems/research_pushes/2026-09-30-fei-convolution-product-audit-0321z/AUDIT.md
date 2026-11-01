# Independent audit of normalized convolution and overlapping products

Date: 30 September 2026. Scope: two specific research packages, including the corrected provenance of the overlapping-product package. **Full FEI remains OPEN. This audit certifies neither a full FEI proof nor publication novelty.**

## Verdict

**PASS for every substantive theorem and counterexample asserted in the two audited packages.** No mathematical gap requiring a changed theorem was found. The analytic arguments, exact finite certificates, normalization conventions, and advertised limitations are consistent. Two minor wording improvements are listed below.

Audited source pins:

- [Normalized convolution report](https://github.com/yspennstate/math-open-problems/blob/2fefba564fdaf0232db13ff468a89063ab29bc6c/research_pushes/2026-09-30-fei-normalized-convolution-0236z/REPORT.md), commit `2fefba564fdaf0232db13ff468a89063ab29bc6c`; report blob `43f02ba681df60762b28515540a8f851f95286ba`
- [Corrected overlapping-product report](https://github.com/yspennstate/math-open-problems/blob/e894a01f20ba02694c099f903fbdf26cc39db0b3/research_pushes/2026-09-30-fei-overlapping-product-0302z/REPORT.md), commit `e894a01f20ba02694c099f903fbdf26cc39db0b3`; report blob `76734ba5f15292f83784573271517c61d039ffad`
- [Attribution correction](https://github.com/yspennstate/math-open-problems/blob/e894a01f20ba02694c099f903fbdf26cc39db0b3/research_pushes/2026-09-30-fei-overlapping-product-0302z/CORRECTION.md), blob `0ba6bbec4662aa78e8a13f2ffc9cc3d4a4821f6e`

All ten fetched package files were checked against their Git blob hashes. Both original verifiers were executed in isolated copies, and their generated results match the committed JSON results. No source-author file was changed during this audit.

## Statement-by-statement decisions

| Statement | Decision | Essential qualification |
|---|---|---|
| Exact tensor identities for C, Z, L, T | PASS | T is L/Z, not H(v/Z) |
| Raw all-source positive-coefficient lower payment fails | PASS | Does not refute a composition-prime-only target |
| Normalization preserves sparse one-point calibration | PASS | The error is o(old-coordinate influence) |
| Paired support and conditioned reference formulas | PASS | Pair-coordinate reference parameter is beta=p²/d |
| Conditioned tariff fails fixed-factor shape-KL recovery | PASS | An upper-recovery failure, not a lower-payment refutation |
| Completed two-shell correlation formula | PASS | Uses original product reference and explicit plus-at-zero signs |
| Completed tariff recovers this family's shape KL up to o(I) | PASS | Restricted-family result only |
| One-point surgery realizes a full-support sign completion | PASS | n>=2; realizes signs, not prescribed product magnitudes |
| Seven-variable single-point product counterexample | PASS | Distinct from the recovered eleven-variable witness |
| Eleven-variable rare-clause counterexample | PASS, RECOVERED | Already established in September 20 source |
| All-width asymptotic and actual-pivotal-overlap no-go | PASS | Does not rule out other global influence corrections |
| Averaged translation entropy identity and inequalities | PASS | Uniform average cannot be replaced by an arbitrary translate |
| Upper bound on interference information by conditional entropy | PASS | Uses the unitary Walsh uncertainty theorem |
| Averaged influence identity | PASS | Simultaneous averaging over x and translation is essential |
| Pointwise +2k shared-variable repair | PASS | k is an overlap count, not a controlled influence budget |

The proposed universal normalized KL payment is **UNPROVED**, as the source states. Nothing in this audit promotes it to a theorem.

## 1. Tensor normalization and the raw-tariff obstruction

For a real unit vector b, C(0)=1 and |C(U)|<=1. Therefore v=C² has nonnegative logarithmic summands, but it is generally not a probability law. With Z=sum v and mu=v/Z, the identity is

    T=L/Z=H(mu)-log2 Z.

Autocorrelation factorizes exactly on a tensor: C_(b tensor c)(U,V)=C_b(U)C_c(V). Thus Z multiplies and

    L_(b tensor c)=Z_c L_b+Z_b L_c,
    T_(b tensor c)=T_b+T_c.

The zero terms are handled by continuity. For support-conditioned Boolean references, support, signs, product measure, and conditioning probabilities all factor. For unconditioned completions, additivity of the abstract functional does not assert that an arbitrary completion rule commutes with products. The report explicitly preserves this distinction.

For the three-variable defect, the integer Walsh coefficients are 6,-2,...,-2, hence normalized coefficients 3/4,-1/4,...,-1/4 and coordinate influences 1/4. Direct substitution into the one-point correlation formula gives v by shell as 3/256, 9/256, 27/256, with multiplicities 3,3,1. Hence Z=319/256 and L>0. Independent entropy evaluation gives

    K=2-(9/8)log2 3,  I=3/4.

Tensoring k copies makes K and I linear but L=k Z^(k-1)L_base. Suspending by a fresh dictator adds one to influence and makes the old-coordinate product reference identical to the nonempty I-projection. Correlations shifting the dictator coordinate vanish. The exponential argument therefore refutes every fixed theta>0 and every finite additive coefficient kappa in the stated all-source raw-tariff lower bound. The k=32 rational certificates are illustrative instances, not the justification for the universal no-go.

The retained sparse calibration is also correct: L=O(m²p), Z-1=O(mp), and consequently L-L/Z=O(m³p²)=o(mp) when p=2^(1-m). The source's leading coefficient 1/4 and additive-influence correction survive normalization.

## 2. Pair support, under-recovery, and controlled remainders

The pair lift replaces each spectral coordinate with its designated two-coordinate character. Its support is the linear subgroup of pair unions, with coefficients 1-p at the empty set and -p at all other subgroup elements. There are no additional nonzero coefficients. Its entropy is unchanged and each old coordinate is duplicated in the spectral degree, so I=2mp and every physical marginal is p.

The product reference gives a pair equal-membership probability d=(1-p)²+p²; thus Q(A)=d^m. Conditional pair indicators are independent Bernoulli beta=p²/d. The residual KL formula is exactly

    K_shape=2m h2(p)-H_m+m log2 d.

A translation outside the support subgroup has disjoint support and zero correlation. Within the subgroup, writing the inverse transform as 2a^m-product(a+b x_i) gives the asserted formula at reference parameter t:

    v_r=[t(1-t)]^r [2^r-4(1-t)^(m-r)]².

The entropy and support expansions are valid with uniform absolute error constants along the stated family. In fact, a slightly more explicit audit expansion is

    K_supp=2mp/ln2+O(mp³),
    K_shape=2mp(m-3)+(4-2/ln2)p+O(mp²).

This implies the source's K_supp/I ->1/ln2 and K_shape/I=m-3+o(1).

Here is an explicit justification for the higher-shell remainder used in both packages. If v(U)<=a^|U| and a²<=1/e, monotonicity of x log2(1/x) on [0,1/e] gives, for n coordinates,

    sum_(|U|>=2) e(v(U))
      <= log2(1/a) n a [(1+a)^(n-1)-1]
      <= log2(1/a) n(n-1)a² exp(na).

This bound proves the asserted tails without a hidden fixed-dimension assumption. For n=m and a=4beta it is O(m³beta²)=o(m beta). The singleton has v_1=4beta[1+O(m beta)]. Its logarithmic correction is O(m beta log(1/beta))=o(1) in the normalized singleton bracket. Also Z-1=O(m beta). Therefore

    T_conditioned=4m beta log2(1/(4beta))+O(m³beta²),
    T_conditioned/I ~4mp ->0.

Since K_shape/I tends to infinity, no finite fixed-factor-plus-O(I) upper recovery is possible. The report correctly does not turn this into a refutation of K_shape>=T/4-kappa I. Its FEI ratio H/I tends to two, so this is not an FEI counterexample.

## 3. Completed correlations and Boolean-realizable signs

For the explicit completion, the inverse transform is B=A-2V+2c with the report's definitions. On one pair, the AV coefficients at occupancies 0,1,2 are exactly d, ab, 2a²b². If a shift singly occupies any pair, the V and V² terms vanish. If it only doubly occupies pairs, the 4V² and -4AV coefficients cancel. These facts establish both branches of the two-shell formula, including their multiplicities. The zero shift is separately 1.

The sign-independent Hellinger bound follows by triangle inequality and factorization:

    |C(U)|<=product_(i in U) 2sqrt(alpha_i(1-alpha_i)).

For the pair family this gives v(U)<=(4p)^|U| and Z-1=O(mp). The singleton formula gives v(e_i)=4p[1+O(mp)] on 2m shifts. Its total logarithmic contribution is

    8mp(m-3)+O(m³p²).

The explicit tail estimate above, now with n=2m and a=4p, gives another O(m³p²). Normalization costs at most the same order. Hence T_completed/(4I)=m-3+o(1), and comparison with the audited KL expansion yields the source's o(I) conclusion. More precisely, the same estimates yield

    T_completed/4-K_shape=-(4-2/ln2)p+O(m³p²).

No source-independent recovery theorem follows from this one family.

The surgery proof is valid for every flip point. For n>=2, all Walsh numerators have the same residue -2r modulo 4, where r counts negative truth-table values. A zero numerator forces r even and thus every numerator divisible by 4. A point flip adds -2 f(x0) chi_S(x0), which is never zero modulo 4, cannot change the sign of a previous nonzero multiple of 4, and sets the old zero signs exactly as claimed. The condition n>=2 is essential to the parity argument. The pair lift is negative at its origin, so the completion there is plus at all old zeros. Crucially, this says that the completed sign pattern is realized by another Boolean function; it does not say that square roots of the original reference probabilities form that Boolean function's spectrum.

## 4. Product witnesses, exact asymptotic, and provenance

The independent checker computes Walsh coefficients by direct summation, not the author's FWHT. It reproduces all three seven-variable signed histograms and Parseval identities. A separate 64-term rational-log implementation certifies

    H(fg)-H(f)-H(g)>0.1630852002095.

It also directly reconstructs the dimension-eleven rare-clause product, its four coefficient classes, and

    H(h_6)-2H(f_6)>0.00239650700679.

The rare-clause spectrum follows by restricting the shared selector: one branch is constant 1 and the other is a disjoint product of two (m-1)-variable defects. Averaging/differencing these branches gives exactly the four classes in the report. Their total multiplicity is 2/p²=2^(2m-1); the zero endpoint at m=2 is harmless.

Writing L=log2(1/p), independent expansion gives

    H(h_m)=8pL+4p/ln2-24p²+O(p³L),
    2H(f_m)=8pL+4p/ln2-4p²L-6p²/ln2+O(p³).

The cancellation of all p²L terms in the first line is correct. The remainders are justified by Taylor expansion of analytic factors near zero; the only nonanalytic factors are explicit powers times log p. One may restrict to 0<p<=1/8 for uniform bounds. Thus the defect is 4p²L+(6/ln2-24)p²+O(p³L), positive for sufficiently large width.

All private-coordinate pivotal probabilities remain p. The common coordinate is pivotal for the product with probability 2p(1-p). Hence I(f)+I(g)-I(fg)=2p², exactly twice the simultaneous pivotal probability p². Dividing the entropy defect by this quantity yields 2L+3/ln2-12+o(1), proving the claimed no-go for a fixed linear actual-overlap payment. Dividing instead by h2(p²) tends to two, also as stated. This calibration does not prove a universal logarithmic-overlap repair.

Disjoint tensor amplification of either positive product defect eliminates any dimension-independent additive constant. It leaves the multiplication factors sharing coordinates within each block, so it does not conflict with disjoint-variable entropy additivity.

The attribution correction is verified against the [September 20 directional-compression source, Section 7](https://github.com/yspennstate/math-open-problems/blob/fe94de760ee2b47545419a7447b492816bd16045/proofnet24/P03-fei/continuations/2026-09-20-directional-compression/REPORT.md#7-an-explicit-obstruction-to-shared-control-subadditivity). Its control convention is reversed, its k equals the present m-1, and its equation (7.6) explicitly identifies the same product-entropy defect. The eleven-variable example and broad no-go are recovered results, not newly certified progress. The seven-variable point-flip certificate is distinct. Neither this distinction nor this audit establishes publication novelty.

## 5. Averaged entropy, uncertainty, influence, and +2k

The joint law is correctly normalized. Setting r_u(z)=sum_s a_s b_(s xor u)(-1)^(s dot z), the Fourier coefficient of f(x)g(x+z) differs from r_u(z) only by a sign. Boolean Parseval gives sum_u r_u(z)²=1; averaging over z gives q_u=sum_s a_s²b_(s xor u)². Thus 2^-n r_u(z)² has uniform Z marginal and U marginal equal to the independent spectral XOR law.

Consequently H(U|Z)=E_z H(h_z), and the bijection (S,T)<->(S,U) yields the exact ledger

    H(f)+H(g)-E H(h_z)=H(S|U)+I(U;Z).

The nonnegative mutual information gives the entropy inequalities. For each q_u>0, the unit vector a_s b_(s xor u)/sqrt(q_u) has squared-coordinate law S|U=u. Its unitary Walsh transform has squared-coordinate law Z|U=u: the normalization factor is precisely 1/sqrt(2^n q_u). The standard Walsh entropic uncertainty inequality gives H(S|U=u)+H(Z|U=u)>=n, hence I(U;Z)<=H(S|U). This is a direct application of the [Maassen-Uffink uncertainty relation](https://doi.org/10.1103/PhysRevLett.60.1103), whose matrix-overlap constant here is 2^(-n/2). No extra n or factor two is missing.

The independent checker reconstructs all 128 translations of the seven-variable witness using direct Walsh sums and verifies the complete rational joint law. Its descriptive values are H(S|U)=0.28161644288267584, I(U;Z)=0.07592189375659866, and total entropy deficit 0.3575383366392745. Acceptance uses rational interval bounds, not these printed decimals.

For influence, under independent uniform x,z the pair (x,x+z) is independent uniform. Each product edge changes sign exactly when its two edge-change indicators differ. This proves the coordinate formula alpha_i+beta_i-2alpha_i beta_i and the stated total average. The independent checker verifies it as exact Fraction equality in all seven witness coordinates.

For the +2k bound, at a Boolean split both child Fourier vectors have squared norm one. The parent marginal on residual labels is q=(a²+b²)/2; its additional binary-label entropy B lies in [0,1]. The average child entropy is H(q)-JS, with JS in [0,1]. Therefore H(parent)-average H(children)=B+JS lies in [0,2]. Iterating over the k shared variables gives H(fg)<=average H(f_y g_y)+2k. The restricted factors have disjoint remaining variables, so their entropies add. Their respective average restricted entropies are at most the original entropies by the nonnegative side of the same restriction ledger. This proves the bound exactly as written. No assumption controls k by influence.

## 6. Checker audit and minor clarity recommendations

The source log routine uses range reduction to y in [1,2), z=(y-1)/(y+1), and 48 terms of the positive atanh series. After the last term, the next power is z^97. The reported tail bound 2z^97/[97(1-z²)] is valid. The dedicated ln2 branch uses z=1/3 and the same remainder. For arguments below one, reciprocal sign reversal preserves interval order; division by the positive ln2 interval is correctly oriented for both positive and negative numerators. No floating-point inequality decides either counterexample.

The source verifiers' SHA-256 values were reproduced:

- Convolution: `38a1f30b4cfcdb370796a6b0b37ded893aa99d21e82757260dafd4a3f987be47`
- Product: `d5239cd1e8c000804c65f2f1b54aa86209977e8c2408a353328643cf5dbab501`

The added independent checker additionally records exact rational endpoints, uses a 64-term enclosure, directly sums Walsh coefficients for both witnesses and every translated seven-bit product, and checks every physical flip point for all zero-supported functions in dimensions two and three: 1,056 flip cases. Its complete result is `independent_results.json`.

Optional precision improvements, communicated to the source author:

1. The convolution setup says all families have interior coordinate marginals; the explicitly added suspension coordinate has marginal one. Say “all original, nonsuspension coordinates” instead. The actual suspension proof handles the deterministic coordinate correctly, so no theorem changes.
2. The product claim ledger's first `not_refuted` list broadly names influence-dependent corrections, while a later entry refutes the specific actual-pivotal-overlap correction. Qualify the earlier list as “other/global influence-dependent corrections.” The report itself already makes this distinction.
3. The source JSON's rounded floating interval endpoints often coincide. The report properly calls them summaries. Serializing rational endpoints, as the independent checker does, makes the saved certificate easier to inspect without rerunning it. This is a reproducibility improvement, not an invalidation of the accepted exact comparisons.

The two wording changes in items 1 and 2 were subsequently applied by the source author in [commit f3726e747609b85bfd7503fff55cc93deae443ef](https://github.com/yspennstate/math-open-problems/commit/f3726e747609b85bfd7503fff55cc93deae443ef). The audit inspected that two-file diff: neither mathematical formulas nor checker code/results changed. The scientific source pins at the beginning of this audit remain the versions actually replayed.

## 7. Stopping boundary

This was an independent mathematical and implementation audit of the listed packages, not formal proof-assistant verification. The original exact tests were replayed; their floating exploratory search was not replayed and cannot establish any universal inequality. All asymptotic conclusions were checked analytically rather than inferred from finite plots.

The companion local normalized-collision admission note was also inspected: its singleton lower estimate, full-support point perturbation, rare-activation spectrum/influence formulas, and limiting argument are consistent with the report's warning that a universal low-influence full-support lower payment would imply unrestricted FEI. That inspection does not prove the lower payment. No complete FEI proof, numerical universal constant, minimal-witness result, or publication-priority determination follows from this audit.
