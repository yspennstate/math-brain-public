# Flat spectra do not constrain the Boolean cores in their physical descendants

The flat-parent contraction obstruction of A032 and the high-moment query-loss obstruction of A097 both hold at their stated scopes. The additional consequence here is an exact description of every mask-query prefix for an arbitrary Boolean phase. A flat Boolean root can have an arbitrary Boolean core at every terminal, up to a character. This is an inheritance obstruction, not an FEI counterexample or a new entropy inequality.

All logarithms are base two. Physical inputs below are bits, with characters (-1)^(a dot x); this is the usual uniform sign cube in bit notation.

## 1. The complete hierarchy and the imported controls

For a real multilinear function f=sum_S c_S chi_S, the COMPLETE signed-convolution hierarchy is

    sum_S c_S c_(S xor U) = 1[U=empty]  for EVERY U subset [n].       (1)

These are exactly the Fourier coefficients of f^2=1, so (1) is equivalent to pointwise Booleanity. Equivalently, every physical face has norm one, including the zero-dimensional faces. At any split f=A+x_i B, complete Booleanity gives A B=0 and A^2+B^2=1 pointwise. Iteration retains those identities on every face. The multiplicative derivative is M_i f(x)=f(x)f(x xor e_i), a sign; the exact pivotal indicator is (1-M_i f)/2. The full hierarchy here includes the consistency of these derivatives with ONE original f; it does not replace them by unrelated sign-valued variables.

The October 11 A033 source already imports the normalized dyadic fixed-signed-order G_(K,w) family from ROUTE_MAP_CURATED section 3 / BOOLEANITY_ORDER Theorem 2.1. It defeats each fixed signed-order relaxation, not (1). The distinct fixed atom-cap cyclic obstruction is available in the audited campaign summary only. Its original definition and checker have not been recovered in this stage. That provenance gap remains open: no parameters or original-source verification are invented. Neither control is an actual Boolean FEI counterfamily. Increasing a fixed prefix, retaining dyadic coefficients or making a square defect small supplies no new premise here.

The construction in section 2 satisfies (1) EXACTLY in every dimension, so its descendant behavior cannot be excluded by asking for a stronger Booleanity prefix or the complete hierarchy. The present stage consumes the newer physical-inheritance objection rather than reopening the earlier phase-degree payment.

## 2. Arbitrary-core flat completion, including every physical prefix

Fix m>=0 and ANY Boolean g on m bits. On two disjoint m-bit blocks define

    F_g(x,y)=(-1)^(x dot y) g(y).

Summing first over x gives, for all frequency labels a,b,

    Fhat_g(a,b)=2^-m (-1)^(a dot b) g(a).                         (2)

The x character average is zero unless y=a, and is one when y=a. Since g(a)^2=1, every squared coefficient is 2^-2m. Therefore H(F_g)=2m. For m>=1 each x_j influence is 1/2, since its derivative is (-1)^y_j. Each y_j derivative contains the fresh fair factor (-1)^x_j, independently of its other factors, so its influence is also 1/2. Thus I(F_g)=m. At m=0 the parent is constant and H=I=0. This is the familiar Boolean bent completion; no novelty is claimed for its existence. The phase g(a), absent from its squared spectrum, is retained in (2).

Now fix ANY queried mask set K subset [m], a physical assignment t to x_K, and J=[m]\K. Put r=|J|, k=|K|. Write g_a(z)=g(y_J=a,y_K=z), an actual k-bit restriction of the core. Residual frequencies consist of a on x_J, b on y_J, and c on y_K. Exactly the same character sum gives

    Fhat_(K,t)(a,b,c)=2^-r (-1)^(a dot b) ghat_a(c xor t).       (3)

All r,k=0 boundary cases use the one-point zero-bit cube. In (3) the squared law has uniform independent labels a,b and the conditional law of c is the translated squared Fourier law of g_a. Consequently

    H(F_(K,t))=2r+2^-r sum_a H(g_a),                           (4)

independently of t. These are labelled physical restrictions; no linear change of physical coordinates is used.

At K=[m], EVERY one of the 2^m terminals is

    g_t(y)=(-1)^(t dot y)g(y),   P_(g_t)(c)=P_g(c xor t).       (5)

Hence every terminal retains H(g). More generally any spectral-law quantity invariant under complementing coordinate labels is identical on every terminal: optimal marginal-KL contraction coefficient, total correlation and minimum exact coordinate-product-mixture cardinality are examples. This follows by pushing every candidate law or mixture through the same bijection; both KL and product structure are preserved. Infinite divergences and deterministic marginals follow under that bijection without division by a zero probability.

The individual terminal influence is

    Inf_j(g_t)=Inf_j(g) if t_j=0, and 1-Inf_j(g) if t_j=1.      (6)

Thus D_can(g)=sum_j min(Inf_j(g),1-Inf_j(g)) is retained at EVERY terminal, whereas ordinary influence is not. For any fixed C>=0, an assertion H<=C D_can for all descendants of all these flat roots is equivalent to full FEI with the same C. One direction uses t=0 and D_can<=I. Conversely FEI applied to a character minimizing influence proves H(g)<=C D_can(g), for every g; (5) preserves both sides. This is an equivalence, not a proved universal helper.

## 3. The original account and the alternate-policy guard

During any x-only prefix each still unqueried x_j has influence exactly 1/2. Querying all m mask variables spends original reach-weighted influence m/2. Averaging (6) over ALL complete terminals gives terminal influence m/2, so the exact original account is

    m = m/2 + E_t I(g_t).                                    (7)

At depth k the expected residual influence is m-k/2. A particular terminal may have much smaller influence, but it has not received a fresh original reserve. In particular the t=0 branch has reach 2^-m; the claim about all-terminal entropy does not turn that branch into a free new source.

Supply the original normalized UNIFORM reference Q on 2m spectral bits. It is exactly P_F, has CE=2m=2I(F), and root divergence zero. Its spectral projection along every query remains uniform on the remaining coordinates. At each complete terminal it is uniform on m bits, so

    CE_terminal=m,   D_terminal=m-H(g),                       (8)

at every terminal, and no terminal cost vanishes. Each x query decreases inherited full CE by exactly one. The full identity CE_root= m + E CE_terminal is therefore 2m=m+m. The terminal source is a cheap reference relative to the PADDED original budget, not a noncircular O(I(g)) source for an arbitrary core.

For the explicit projection convention let B_i=H(P)-H(pi_i P) and L_i=D(P||Q)-D(pi_i P||pi_i Q). Because Q is uniform, B_i+L_i=1 on these queries. If J_i=average child D(P_child||pi_i P), the exact divergence increment is J_i-L_i. Summing through the full x tree gives

    sum_v reach_v (J_v-L_v)=m-H(g).                           (9)

The nonnegative terminal mismatch in (8) is generated by signed recombination. Root exactness does not make all descendant references exact. Equation (9) neither clips signs nor invents an initial KL bank.

There is also an easy alternate physical policy: query all y bits first. Every terminal is the character (-1)^(x dot y) times the sign g(y), so terminal entropy is zero. Each queried y_j still has influence 1/2 while x_j is free, and mean terminal influence is m/2. This prevents the false conclusion that every policy inherits a hard core, or that the construction refutes a selected stopping strategy. Flat-parent root FEI is already H/I=2. The obstruction concerns automatic descendant admission from root spectral properties.

## 4. Independent reconstruction of A032's flat-parent claim

The unchanged source is A032-FLAT-PARENT-INHERITED-CONTRACTION-OBSTRUCTION@1, hash 057a2714601cd4fcd943859c497c78a24cd1856102edd1720324d92e4b089e64, PROOF section 2 in run 20261027T071919Z. Equation (2) applies with g(y)=(-1)^(y_1 sum_(j>=2)y_j). Query x_2,...,x_m. Direct character summation gives the uniform four-atom law

    S_x1=A, S_y1=B, S_yj=A xor t_j,

where A,B are independent fair bits. Its entropy is 2 and every remaining influence is 1/2. For any law R on those four atoms,

    sum_i D(R_i||(P_t)_i)=m D(R_A||U_1)+D(R_B||U_1)
      <=m [D(R_A||U_1)+D(R_B||U_1)] <=m D(R||U_2).

The last inequality is the finite identity D(R||U_2)=D(R_A||U_1)+D(R_B||U_1)+I_R(A;B); m>=1 is used. Conditioning on A=1 and keeping B fair attains ratio m. A law outside the four-atom support has infinite full KL and does not alter the finite optimum. At every partial restriction of these mask coordinates the same summation gives entropy 2(m-k), all remaining influences 1/2 and the claimed account. The two product components obtained by conditioning A realize P_t exactly. Their posterior information is one bit, while TC=m-1. One product cannot realize the nontrivial deterministic relation when m>=2; m=1 has an independent product. Thus every asserted endpoint and every terminal in the source holds without repair. The TC cost equals twice original spent query influence; no amortized-payment impossibility follows.

Verdict: HOLDS unchanged at the full named scope, including the selected-policy and amortization guards. This stage does not review A079's separate 7/4 theorem.

## 5. Independent reconstruction of A097's high-moment claim

The unchanged source is A097-HIGH-MOMENT-MATCHED-QUERY-LOSS@1, hash f3b5c69ef59c7d95ba81cee06034cdf49115a0a5036e75101f19a6ba1bd7064d, PROOF section 3 in run 20261027T092641Z. For even n>=4 the true Boolean two-bit-defect tensor has uniform spectrum P, H=n and every influence 1/2. On the face S={n} union V, V subset [n-1], perturb uniform masses by the alternating factor 1+(1-epsilon)(-1)^|V|, epsilon=2^-4n. Other masses stay uniform. Normalization and positivity are exact; the vacuum is outside the face.

Every marginal on at most n-2 coordinates leaves at least one free face coordinate unsummed in its prescribed event, so parity cancellation makes the perturbation zero. Coordinate projections i<=n-1 likewise cancel pairwise. A quarter of all atoms have likelihood epsilon and a quarter have 2-epsilon, so

    L_i=D(P||Q)=-(1/4)log2(epsilon(2-epsilon))
               =n-(1/4)log2(2-epsilon).

Since 1<2-epsilon<2, n-1/4<L_i<n, CE=n+L_i<2n=4I. The strictly positive denominator and n>=4 side conditions hold. Q is already feasible for any affine matching calibration using those moments, so its unique relative-entropy projection from itself is itself, with zero fee and release. This does not contradict the original-source ledger: this exact initial mismatch is consumed at the first projection.

Verdict: HOLDS unchanged at the named scope. The affine-history theorem of that run is not reviewed here. Matching order n-2 is not confused with complete Booleanity: the actual f is Boolean already, whereas Q is a supplied reference and need not be the spectrum of a Boolean function.

## 6. What remains unpaid

Full Booleanity (1) allows the complete arbitrary-core terminal family (5). A root-only product or flat-source admission condition cannot certify a restrictive hereditary core class without a separate phase-sensitive argument. A condition that simply promises canonical FEI at all those descendants is full FEI itself. The original flat root has influence m; this construction supplies no O(I(g)) initial source when I(g) is small. The remaining universal line is an original arbitrary-core complete source of price O(I(g)), or a justified useful selected policy with all source changes, query losses, old debits and full terminals paid from the same unused original account. Equations (3)--(9) identify the exact retained quantities for such a policy; they do not solve that line.
