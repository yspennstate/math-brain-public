# Exact spectral independence and the remaining aggregate erasure gap

20 September 2026. Further mathematical work on the unrestricted FEI target. **Full FEI is not proved here.** The statements below have direct proofs. Their publication priority has not been checked. The companion checker is `check_erasure_rigidity.py`; its actual output is `erasure_rigidity_checks.json`.

Write N=2^n, a_S=fhat(S), p_S=a_S^2, alpha_i=Pr_p(i in S), and B_i=H(S_i|S_-i). All entropies are in bits. Walsh coefficients W_S=N a_S are integers for Boolean sign functions.

## 1. One exactly independent spectral bit must be fair or deterministic

**Theorem 1.** If S_i is independent of S_-i under the squared Fourier distribution of a Boolean function, then

    alpha_i in {0,1/2,1}.

**Proof.** The deterministic cases require no argument. Suppose 0<alpha_i<1. Independence says that for every T not containing i,

    |W_(T+i)| / |W_T| = sqrt(alpha_i/(1-alpha_i))

whenever either entry is nonzero, and both entries are zero together. At least one pair is nonzero, so this ratio is rational. Write it as c/b for coprime positive integers b,c. For every pair there is a nonnegative integer k_T such that

    |W_T|=b k_T,   |W_(T+i)|=c k_T.

Indeed, c|W_T|=b|W_(T+i)| and coprimality give the required divisibilities. Parseval now gives

    N^2=(b^2+c^2) sum_T k_T^2.

Thus the positive integer b^2+c^2 divides the power of two N^2 and must itself be a power of two. If b,c have opposite parity, their sum of squares is odd and greater than one, impossible. They cannot both be even. If both are odd, their squared sum is 2 modulo 8, so the only possible power of two is 2. Therefore b=c=1 and alpha_i=1/2. QED.

**Corollary 1.1.** If all spectral bits are mutually independent, the squared Fourier law is uniform on a coordinate face with an even number r of free coordinates. The function is a character times a Boolean function on those r coordinates with flat Fourier magnitudes. In particular,

    H(f)=r=2J(f)<=2I(f).

To see the form of the function, fixed spectral bits factor out a character and leave no dependence on the other fixed coordinates. The remaining independent fair bits give 2^r masses, all 2^(-r). The coefficient magnitudes are 2^(-r/2); they are rational Walsh coefficients, so r is even. Such flat Boolean functions are commonly called bent functions. Conversely, a character times a bent function on a coordinate subset has precisely this product spectral law. This is an exact characterization, not a quantitative stability estimate.

## 2. Almost independent spectral bits can still have an unbounded local erasure ratio

The rigidity theorem cannot be converted into a uniform local bound B_i<=C alpha_i merely by continuity. There is an explicit family in which the spectral mutual information tends to zero quadratically in alpha_i, while B_i/alpha_i diverges.

Let m>=2 be even, N=2^m and delta=1/N. On y in F_2^m take the quadratic bent function

    g(y)=(-1)^(y_1 y_2 + y_3 y_4 + ... + y_(m-1) y_m).

Its Fourier coefficients are all +/-1/sqrt(N), and g(0)=1. Introduce one physical bit t and set

    F(t,y)=g(y)(1-2 t 1_{y=0}).

The two restrictions at t=0,1 are g and g-2 1_{y=0}. Consequently, for every Fourier label s on the y coordinates,

    u_s=Fhat(0,s)=ghat(s)-1/N,
    v_s=Fhat(1,s)=1/N.

It follows at once that alpha_t=sum_s v_s^2=delta. Let P be the joint spectral law of (S_t,S_y), let P_y have masses m_s=u_s^2+v_s^2, and let U be the uniform law on y-labels. The conditional law of S_y given S_t=1 is exactly U.

**Theorem 2.** This family has the exact chi-square mutual information

    chi^2(P || P_t tensor P_y) = 4 delta^2/(1+4 delta^2).

Therefore, with h_2 the binary entropy,

    0 < h_2(delta)-B_t(F)
      <= log_2(1+4 delta^2/(1+4 delta^2))
      <= 4 delta^2/ln 2,

and hence

    B_t(F)/alpha_t(F)
      = log_2(1/delta)+1/ln 2+O(delta) -> infinity.

### Proof of the chi-square identity

Put r=sqrt(delta)=1/sqrt(N). Since the sum of the Fourier coefficients is g(0)=1, the proportions of positive and negative coefficients are (1+r)/2 and (1-r)/2 respectively. The corresponding marginal masses are

    m_s=(1/N)(1+2delta-2sqrt(delta))  [positive ghat],
    m_s=(1/N)(1+2delta+2sqrt(delta))  [negative ghat].

For a binary mixture with first-branch probability delta, first conditional law U, and marginal P_y, direct expansion of the chi-square divergence gives

    chi^2(P || P_t tensor P_y)
      = delta/(1-delta) [sum_s U(s)^2/m_s - 1].

Here

    sum_s U(s)^2/m_s
      = (1+r)/(2(1+2r^2-2r)) + (1-r)/(2(1+2r^2+2r))
      = (1+4delta)/(1+4delta^2).

Substitution gives the asserted 4delta^2/(1+4delta^2). All denominators are positive. Relative entropy in bits is at most log_2(1+chi^2), by Jensen applied under the first law to the likelihood ratio. Mutual information equals h_2(delta)-B_t, so the upper estimates follow. It is strictly positive because the two displayed marginal masses are different and the first conditional law is uniform. Finally h_2(delta)/delta=log_2(1/delta)+1/ln 2+O(delta), proving the asymptotic. QED.

### Why this does not refute the aggregate target or FEI

For every background coordinate j, the original g has influence 1/2. At t=1, the origin and its j-neighbor both originally had value +1, so the single flip increases the averaged physical influence by delta. Thus

    Inf_j(F)=1/2+delta,
    I(F)=m(1/2+delta)+delta.

The background already has a large influence budget. Nothing in this example makes sum_i B_i/I diverge. The remaining target is an aggregate bound over all coordinates or a correctly quantified hereditary allocation bound, not a per-coordinate inequality for every possible chosen coordinate.

## 3. Another tested shortcut: replacing the JS payment by 2J

Let Z(f)=sum_i JS(q_i^+,q_i^-), with the restriction spectral laws as in the existing erasure reduction. The retained valid theorem is Z<=2J/ln 2. The stronger proposal Z<=2J is false.

For the three-variable one-point defect f=(-1,1,1,1,1,1,1,1), the exact checker encloses

    J=3/4,
    Z/J in (2.195179762781593, 2.195179762781596).

It computes the entropy and the binary erasure expression with rational logarithm intervals, so this is not just the floating-point observation from the initial search. It is not a claim that the supremum of Z/J has been determined, and the old 2/ln2 payment remains valid.

## 4. Actual checks and scope

The completed checker reports PASS for all 65,812 Boolean truth tables in dimensions one through four, comprising 262,948 coordinate-independence tests. It also verifies the controlled bent formulas and the exact chi-square identity in background dimensions 2,4,6,8,10, and certifies the three-variable JS counterexample. The checker uses integer Walsh transforms and rational logarithm bounds from the main continuity checker.

Run:

    python3 check_erasure_rigidity.py --output erasure_rigidity_checks.json

The first theorem is a qualitative Boolean arithmetic constraint. The second theorem proves why that qualitative fact is insufficient to finish the local entropy argument. These results are preserved as usable mathematics and explicit limitations; they are not another claim that the remaining universal FEI estimate has been proved, a replacement for the aggregate problem, or a first-priority assertion.
