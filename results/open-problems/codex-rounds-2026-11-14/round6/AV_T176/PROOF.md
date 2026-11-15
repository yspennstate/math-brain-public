# The tagged-flow identity for physical Thorp shuffles

Source: OpenAI, *Optimal-order mixing of the Thorp shuffle*, September 26, 2026, and its Lean files [MaskedResampling.lean](sources/MaskedResampling.lean) and [ConditionalLaw.lean](sources/ConditionalLaw.lean). The identities checked here are physicalFlow_joint, flow_joint_identity and tagged_deviation_identity. The dimension below is D; the Lean parameter d in these declarations has D=d+1.

## 1. Independent recheck of round 5

For a deterministic free set of size m, let a input pairs contain two free points and b pairs contain one. Then m=2a+b and the number X of free points in either output half distinguished by the last coordinate is a+Bin(b,1/2). These are the prepared rotating halves, rather than the first-bit halves of the physical deck. Thus E X=m/2. For b>0 the event X<m/4 is a downward deviation greater than m/4. The centered Bernoulli log moment generating function is bounded by θ²/8, giving

\[
 \Pr(X<m/4)\le \inf_{\theta>0}
 \exp(-\theta m/4+b\theta^2/8)
 =\exp(-m^2/(8b))\le \exp(-m/8).
\]

For b=0 the bad event is empty. Since exp(1/8)>1+1/8=9/8>10/9, exp(-m/8)<(9/10)^m for m>0. A union bound gives the earlier 2(9/10)^m estimate for the two halves. This argument does not use random initial labels. Direct rational multiplication also gives the earlier pair factors

\[
 (5/8)(1+(4/5)^4)=881/1000\le9/10,
 \qquad (5/4)^2(4/5)^4=16/25\le(9/10)^2.
\]

For the inverse-square Fourier route, the input norm estimate is of order D_ρ^(-1/4). Eight powers, squaring and two degree factors leave exponent 2-16/4=-2. Its constants check as k²N/4=98·2^(3j) for k=7·2^j and N=8·2^j, 98·32=3136, 8·4·3=96, and 8·200=1600 physical steps per dimension. The independent import traversal in check_conditional.py also confirms Main's 51-module acyclic OAI closure, 55 saved modules in total, Mathlib as the only external import, and FirstMain outside Main's closure. These checks preserve round 5's local conclusion.

## 2. Model and flow

Let D≥1, N=2^D and V={0,1}^D. Write a position as (b,u), where u has D-1 bits. For a bit array c indexed by u, one physical shuffle is the permutation

\[
 P_c(b,u)=(u,b\mathbin{\mathrm{xor}}c(u)). \tag{1}
\]

This is the cut-and-drop shuffle: (0,u) and (1,u) are corresponding positions in the two halves; their outputs are the adjacent positions (u,0) and (u,1). The same convention is used by step_cons in the saved source. Different time layers have independent uniform arrays c.

Let B⊆V be any free set and w:V→R any signed weight. The raw identity imposes neither positivity nor support nor zero total mass on w. Define K_(B,c)w by processing each input pair with weights a=w(0,u), b=w(1,u). If both endpoints are in B, put (a+b)/2 at each output (u,0),(u,1). Otherwise put a at P_c(0,u) and b at P_c(1,u). This is physicalFlow. The next free set is P_c B, which is physicalFree.

The raw iteration starts with (B,w), applies this update at each step, and writes its result as (B_t,W_t). Let G_t=P_(C_(t-1))⋯P_(C_0), so G_0 is the identity. The inverse-image definition of physicalFree gives

\[
 B_t=G_tB. \tag{2}
\]

Let e be any indexed collection of exposed starting positions outside B. Repetitions are allowed. Its endpoint collection is E_t=G_t∘e, and by (2) every entry of E_t lies outside B_t.

## 3. One-step masked resampling

Define the pair mask M_B(u)=1 exactly when both (0,u) and (1,u) are in B. For fixed c and an independent uniform array R, replace c(u) by R(u) on this mask and keep c(u) elsewhere. Denote the result by c'=c[B,R].

At each output y, averaging the transported weight over R gives exactly

\[
 K_{B,c}w(y)=\mathbb E_R w(P_{c'}^{-1}y). \tag{3}
\]

To verify (3), fix a pair u. If M_B(u)=0, then c'(u)=c(u), so the preimage and its weight are fixed. If M_B(u)=1, the preimage of either output is each of the two input points with probability 1/2. Its average weight is (a+b)/2. These are all cases; no assumption on the signs or support of w was used.

Every exposed point e(i) is outside B, so its pair cannot have M_B=1. Therefore

\[
 P_{c'}\circ e=P_c\circ e. \tag{4}
\]

Also P_(c')B=P_cB: masked pairs contribute both outputs to either image set, and unmasked pairs use the same coin. This observation explains why the update of the free set can use the original c.

When C and R are independent uniform arrays and B is fixed, C'=C[B,R] is itself uniform. Each output coordinate selects one of two independent fair input bits using a deterministic mask; selections at distinct coordinates use disjoint input bits. Equivalently, exchanging the C and R coordinates on the mask is an involution on all pairs of arrays and preserves uniform counting measure. Uniformity of C' does not assert independence from C or from exposed endpoints.

For any real test f of an exposed collection and one position, finite summation, (3), a permutation change of variable, (4), and finally uniformity of C' give

\[
\begin{aligned}
 &\mathbb E_C\sum_y K_{B,C}w(y) f(P_C\circ e,y)\\
 &=\mathbb E_{C,R}\sum_y w(P_{C'}^{-1}y)f(P_C\circ e,y)\\
 &=\mathbb E_{C,R}\sum_x w(x)f(P_C\circ e,P_{C'}x)\\
 &=\mathbb E_{C,R}\sum_x w(x)f(P_{C'}\circ e,P_{C'}x)\\
 &=\mathbb E_C\sum_x w(x)f(P_C\circ e,P_Cx). \tag{5}
\end{aligned}
\]

This is physicalFlow_joint. It preserves the joint test, including its dependence on exposed positions. Merely observing that C' is uniform would not justify the third equality without (4).

## 4. Iterating the joint identity

We prove for every t≥0 and every f that

\[
 \mathbb E\sum_x w(x)f(E_t,G_tx)
 =\mathbb E\sum_y W_t(y)f(E_t,y). \tag{6}
\]

At t=0 both expressions are Σ_x w(x)f(e,x). Suppose (6) holds at t for every test. For a given next-step test f, define the deterministic test

\[
 F(z,x)=\mathbb E_C f(P_C\circ z,P_Cx).
\]

Independence of the next array from the past changes the left side of (6) at time t+1 into E Σ_x w(x)F(E_t,G_tx). The induction hypothesis changes it into E Σ_y W_t(y)F(E_t,y). Conditional on a fixed past, B_t,W_t,E_t are fixed, with E_t outside B_t. Applying (5) to them changes this expression into

\[
 \mathbb E\sum_y K_{B_t,C_t}W_t(y)
                    f(P_{C_t}\circ E_t,y),
\]

which is the right side at time t+1. This completes the induction and proves flow_joint_identity for arbitrary raw weights. Dependence of B_t on past coins is harmless: the mask is fixed before C_t is sampled. No independence between W_t and B_t is assumed.

## 5. Centering at a tagged position

Take tag∈B, put m=|B|>0, and start the raw flow with

\[
 w(x)=\mathbf1_{\{x=\mathrm{tag}\}}-m^{-1}\mathbf1_B(x).
\]

This is centeredPoint and its iteration agrees with iterateState: both use the same free-set and weight updates. Its mass is 1-m/m=0, it is supported on B, and its squared energy is (1-1/m)²+(m-1)/m²=1-1/m. For each realized G_t, permutation reindexing gives

\[
 \sum_x w(x) f(E_t,G_tx)
 =f(E_t,G_t\mathrm{tag})-m^{-1}\sum_{y\in G_tB}f(E_t,y).
\]

Substitution in (6) proves the precise tagged_deviation_identity:

\[
 \mathbb E\left[f(E_t,G_t\mathrm{tag})-
                  m^{-1}\sum_{y\in B_t}f(E_t,y)\right]
 =\mathbb E\sum_y W_t(y)f(E_t,y). \tag{7}
\]

This statement is an identity of averaged tests, not a pathwise identity after revealing every original coin. The transported uniform vector agrees with m^(-1)1_(B_t) pathwise: a both-free pair averages equal weights; on another pair transport moves exactly its free entries. Linearity therefore makes the centered evolution exactly the difference between the point evolution and this uniform vector.

For |f|≤1, the triangle inequality and Cauchy–Schwarz, first over positions and then over histories, give

\[
 |\mathbb E\sum_y W_t(y)f(E_t,y)|
 \le \mathbb E\sum_y|W_t(y)|
 \le \sqrt{N\,\mathbb E\sum_y W_t(y)^2}. \tag{8}
\]

This is tagged_deviation_bound. If e lists all positions outside B, then B_t is the complement of its endpoint collection. The second term in (7) is consequently the test for appending a uniform available point to that collection. This is the use in prefix_one_step_bound. The conversion from a supremum over tests |f|≤1 to TV contributes the usual factor 1/2; it is absent from the test bound (8) itself. The energy-decay and representation inputs needed to finish mixing remain separate.

## 6. A second derivation with complete exposed paths

When e lists all of V\B, fix a feasible complete exposed path history through time t. At each time it prescribes the value of the coin on every pair visited by an exposed card. If two exposed cards share a pair, feasibility makes their prescriptions consistent. Conversely those prescriptions force exactly the specified paths, by induction on time. Thus the conditioning event is a cylinder in the independent time/pair coins, and every unvisited time/pair coin is still independent and fair.

The free sets at all times are determined by those paths. A pair with two free inputs has no exposed visitor; its coin is unconstrained. A pair with one free input has an exposed visitor; its coin is prescribed. A pair with no free input carries no tagged probability. Therefore the conditional tagged law is obtained by averaging its two masses in the first case and transporting its mass in the second, precisely the flow update. Future exposed-path constraints fix only visited time/pair coins and cannot constrain an unvisited earlier coin. Starting from δ_tag gives the conditional point law, and subtracting the transported uniform law gives W_t.

This second argument proves the conditional interpretation in the full-complement case, and hence (7) there by averaging. It does not identify W_t with a conditional law for an arbitrary smaller collection e. The more general averaged identity (6) was proved without that identification.

## 7. Attempts to break the identity

The outside-B requirement matters. With N=2, B=V, tag=0, w=δ_0, expose the free point e=0 and take f(z,y)=1_(z=y). Actual transport gives expectation 1 because tag and exposed position coincide. The flow averages w to (1/2,1/2), giving expectation 1/2. This invalid variant fails exactly because (4) fails.

The past-measurability of the mask also matters. With one pair, let the mask equal its current coin C, rather than be fixed before C. Then C'=R when C=1 and C'=0 when C=0, so P(C'=1)=1/4. The uniform-array step in (5) would fail. In the audited iteration B_t uses only earlier arrays, so this example does not apply.

Raw weights may lie outside B and may have either sign: (3) and (5) still hold, as checked on every initial basis weight in the finite tests. A zero-sum or support restriction must not be inserted into the raw theorem. For m=1 the tagged centered weight vanishes and so does (7). For B empty the raw theorem remains meaningful, but no tagged theorem with tag∈B is asserted. For B=V there can be no exposed point; the joint identity becomes an unobserved marginal identity. D=1 and t=0 need no special repair. Repeated exposed labels cause no difficulty because (4) holds entrywise.

The exact computation in [check_conditional.py](check_conditional.py) checks all initial basis weights and endpoint-indicator tests in the cases listed in [check-output.json](check-output.json). It also independently groups full exposed-path cylinders and checks both conditional point masses and their centered versions. Physical permutations are constructed directly by cutting and interleaving a deck, and compared with (1). All comparisons use integer cross multiplication, with no rounding or sampled tests.

## 8. Scope

The tagged-flow and test-deviation identities hold with the hypotheses stated above. No defect was found in this link. The result checks a finite conditional-law component of the dyadic proof; it supplies no argument for non-powers of two and no new mixing constant. In particular it does not check HalfHistories' rotating-half reindexing, the half-factorization in EnergyDecay, the representation classification/projector chain, or a Lean kernel/Comparator build.
