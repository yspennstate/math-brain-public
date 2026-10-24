# T228: an explicit contractive nonlinear SGD model with a positive exact power tail

Version 2, 23 October 2026. Candidate for independent review, not yet a final closure verdict. This revision makes two renewal-theorem conventions explicit; it does not change the theorem or estimates.

This proof addresses the actual T228 registry request for a **concrete nonlinear model**. It does not assert a universal theorem for deep networks. It builds on the existing T228 scalar and radial-tail proofs, especially the forward tilted-walk positivity argument in `rows/T228/claude_b1e26540/T3_STEP3.md`. Those results were already present on 22 October. The additional point here is a fully explicit, nonempty interval with contraction of the actual random nonlinear maps, as the registry asks, rather than only a Foster recurrence condition.

## Model and theorem

Let d=10^{-3}, let s(z)=z+d tanh(z), and take iid pairs (A_k,E_k), each consisting of two independent standard normal variables. The regression teacher is x_*=0, the response is Y_k=E_k, and the sample loss is

    f(x;A,E) = (s(Ax)-E)^2/2.

For every fixed learning rate η in [99/100,101/100], run ordinary, unclipped, constant-step, batch-one SGD

    X_{k+1}=Ψ_k(X_k),
    Ψ(x)=x−η A s'(Ax)(s(Ax)−E).

Then:

1. The random maps are contractive on average. In fact E Lip(Ψ)<q=0.98606303<1.
2. There is exactly one invariant probability law π. Every deterministic initial condition converges to π in Wasserstein distance of order one, geometrically fast.
3. There is exactly one α=α(η)>0 with

       h_η(α):=E|1−η A²|^α=1,

   and 1<α<2. The multiplier is nonarithmetic in logarithmic scale.
4. For some C_η in (0,∞),

       lim_{t→∞} t^α π({x:|x|>t})=C_η.

   The law is symmetric, so each one-sided tail has limit C_η/2. For positive p, its p-th absolute moment is finite exactly when p<α. In particular its second moment is infinite, although the input and label noise have moments of every order.

The constant has the integrable-difference formula

    C_η = E[|Ψ(X)|^α−|(1−η A²)X|^α] /
          (α E[|1−η A²|^α log|1−η A²|]),

where X has law π and is independent of (A,E). The numerator is an expectation of the difference, not a difference of two infinite expectations.

## 1. Bounds on the actual nonlinear update

Put z=Ax, t=tanh(z), and u=sech²(z). Then s'=1+du, s''=−2dut, and

    Ψ'(x)=1−η A² H(z,E),
    H=(1+du)²−2du t(z+d t−E).

The inequalities |t|≤1, 0≤u≤1 and |z|u≤1 imply

    |H−1|≤4d+3d²+2d|E|.

Consequently, with M=1−η A²,

    Lip(Ψ)≤L:=|M|+η A²(4d+3d²+2d|E|).

Also the update is asymptotically linear with a uniform random remainder:

    Ψ(x)=Mx+R(x),
    |R(x)|≤B:=η|A|[d+(1+d)(d+|E|)]   for all real x.

The derivative bound follows from expanding H; the remainder follows from

    s'(z)(s(z)−E)=z+dzu+(1+du)(dt−E).

Both B and L have all positive moments, since they are bounded by polynomials in |A| and |E|. The activation is smooth, nonlinear, and a bounded perturbation of the identity. Its derivative is between 1 and 1+d, and z times either derivative of its perturbation is bounded.

## 2. Explicit average contraction and the tail exponent

For a standard normal A with density φ,

    E|1−A²|=4φ(1)=4/sqrt(2πe)<97/100.

For example, the strict rational bound follows from π>3.14 and e>2.718. The identity follows by splitting at |A|=1, using E(1−A²)=0 and (aφ(a))'=(1−a²)φ(a).

Thus, uniformly over the stated interval,

    E|1−η A²|≤E|1−A²|+|η−1|<98/100.

Using independence, E A²=1 and E|E|<1 gives

    E L < 98/100+(101/100)(6/1000+3/10^6)
         =0.98606303<1.

In particular E log L≤log E L<0 (or this expectation is −∞, which only strengthens the contraction conclusion). Here E|log|M|| is finite: the only finite singularities occur at A=±η^{-1/2}, where they are logarithmically integrable; the Gaussian tails control infinity.

The function h_η(p)=E|M|^p is finite for all p≥0, is strictly log-convex, and has h_η(0)=1 and h_η(1)<1. Gaussian unboundedness gives P(|M|>1)>0, so h_η(p)→∞. Moreover

    h_η(2)=1−2η+3η²≥1.9603>1.

It follows that there is a unique positive root α in (1,2), with h_η(p)<1 for 0<p<α. Its logarithmic derivative at the root

    m_α=E[|M|^α log|M|]

is positive and finite. The positive random variable ξ=|M| has a continuous distribution; log ξ is consequently nonarithmetic. The defining equation is explicit:

    (1/sqrt(2π)) ∫_R |1−η a²|^α exp(−a²/2) da = 1.

For batch size b the same asymptotically linear part is 1−(η/b)χ²_b. The theorem proved here uses b=1; its nonempty interval already supplies the requested nonempty parameter regime.

## 3. Invariant law, uniqueness and lower moments

The Markov operator maps probability laws with finite first moment into themselves because E|Ψ(0)|<∞ and E L<1. Coupling two inputs with the same fresh pair (A,E) contracts their Wasserstein-one distance by at most q. The space of laws with finite first moment is complete for this distance, so the contraction mapping theorem gives a fixed law π and geometric convergence from each deterministic start.

This uniqueness extends to every invariant probability law, without assuming that another invariant law has a first moment. Couple a chain from any finite random initial variable Z with a chain from zero. Then

    |X_n^Z−X_n^0|≤|Z|∏_{j=1}^n L_j→0 almost surely.

Indeed E∏L_j≤q^n, so the product tends to zero almost surely by Markov's inequality and Borel–Cantelli. If the initial law of Z were invariant, bounded Lipschitz test functions and dominated convergence would force it to equal π.

For every 0<p<α, the uniform bound |Ψ(x)|≤ξ|x|+B and h_η(p)<1 give a drift inequality

    E|Ψ(x)|^p≤r_p|x|^p+C_p,   r_p<1.

For p≤1 use subadditivity; for p>1 use (a+b)^p≤(1+ε)a^p+C_{p,ε}b^p and choose ε so that (1+ε)h_η(p)<1. Starting at zero yields a uniform p-moment bound. Weak convergence to π and Fatou's lemma give E_π|X|^p<∞.

The transition kernel has a density bounded below on every pair of compact intervals. To see this, restrict A to [1,2]. Conditional on A=a, Ψ(x) is Gaussian with mean x−η a s'(ax)s(ax) and standard deviation η a s'(ax). For |x|≤R these means and standard deviations stay in a compact set, with standard deviations bounded away from zero. Their densities therefore have a positive common lower bound for |y|≤R. After integrating over a∈[1,2],

    P(x,E_0)≥ε_R Leb(E_0∩[−R,R])  for |x|≤R.

Every interval of positive length consequently has positive π-mass.

## 4. Existence and formula of the exact tail limit

Use the scalar N=1 instance of Jelenković–Olvera-Cravioto, *Implicit Renewal Theory and Power Tails on Trees*, arXiv:1006.3295v5, Theorem 3.1. It is an implicit renewal theorem, not a requirement that the update itself be affine. For R_0=|X| independent of ξ, its hypotheses are: Eξ^α=1, 0<Eξ^αlogξ<∞, logarithmic nonarithmeticity, finite moments of R_0 below α, Eξ^γ<∞ for some 0≤γ<α, and integrability of the weighted discrepancy between the tails of R_0 and ξR_0. Sections 2–3 verify the moment and nonarithmetic hypotheses; γ=0 supplies the extra multiplier moment.

Stationarity and a coupling with the same independent X,(A,E) give

    ∫_0^∞ t^{α−1}|P(|X|>t)−P(ξ|X|>t)|dt
    ≤(1/α) E ||Ψ(X)|^α−|MX|^α|.

The expectation on the right is finite. For 1<α<2, the mean value theorem and |Ψ(X)−MX|≤B bound its integrand by

    c_α[B^α+B ξ^{α−1}|X|^{α−1}].

The first term is integrable, and the second is integrable by independence of X from the step, the lower moment already proved, and the Gaussian moments of B and ξ. The implicit renewal theorem gives a finite nonnegative tail limit and the displayed integrable-difference formula. Strict positivity still requires the following argument.

## 5. Positivity of the tail constant

This section specializes and credits the existing T228 forward-excursion proof. It does not infer positivity merely from the existence of an invariant distribution.

Along a trajectory, let ξ_j=|1−η A_j²| and let B_j be the bound from Section 1. The pairs (ξ_j,B_j) are iid, although their two components need not be independent. With S_n=Σ_{j≤n}logξ_j and V_n=Σ_{j≤n}e^{−S_j}B_j, repeated application of the reverse triangle inequality yields

    |X_n|≥e^{S_n}(|X_0|−V_n).

Tilt the joint one-step law by ξ^α and call the resulting iid law Q. For a stopping time τ and a stopped measurable event F, summing over {τ=n} gives P(F,τ<∞)=E_Q[e^{−αS_τ};F,τ<∞]. No assumption that τ is almost surely finite under P is needed. Under Q, S_n has positive finite drift m_α. For 0<θ<α,

    E_Q e^{−θlogξ}=h_η(α−θ)<1.

Three elementary consequences are needed.

(a) The probability p_+=Q(S_j>0 for every j≥1) is positive. Positive drift makes the future infimum finite almost surely. A finite sequence of increments bounded below by some positive number can first take the walk above a sufficiently large buffer; by independence, with positive probability the remaining walk never exhausts that buffer.

(b) The overshoots O_u=S_{τ_u}−u at τ_u=inf{n:S_n>u} are uniformly tight for u≥0. Here is a direct justification. Chernoff's bound gives

    Σ_{n≥0}Q(S_n≤1)≤e^θ/(1−h_η(α−θ))=:K_U.

By the strong Markov property at the first entry into any interval of length one, its expected total number of visits is at most K_U. Partitioning S_{n−1}≤u into these intervals therefore gives

    sup_{u≥0}Q(O_u>z)≤K_U Σ_{k≥0}Q(logξ>z+k)→0,

because E_Q(logξ)^+ is finite.

(c) V_∞=Σ_{j≥1}e^{−S_j}B_j is finite Q-almost surely. For 0<θ<min(1,α), subadditivity and independence across steps give

    E_Q V_∞^θ≤E[ξ^{α−θ}B^θ]/(1−h_η(α−θ))<∞.

Choose z and then K large enough that

    Q(V_∞>K/2)+sup_u Q(O_u>z)≤p_+/2.

Start the original chain at any y with 2K≤|y|≤4K, and set u=log(t/K), t>4K. The event

    {S_j>0 for j≤τ_u, V_{τ_u}≤K/2, O_u≤z}

is measurable at τ_u and has Q-probability at least p_+/2. On it the chain stays outside [−K,K] until it exceeds t. Changing measure gives a uniform lower bound

    P_y(hit {|x|>t} before [−K,K])
       ≥(p_+/2)e^{−αz}(K/t)^α.

The compact minorization in Section 3 gives a uniformly positive chance from [−K,K] to reach the annulus {2K≤|y|≤4K} in one step. Finally, stationarity gives the last-exit inequality

    π(D)≥∫_A π(dx) P_x(τ_D<τ_A^+),

for disjoint A,D, where τ_A^+ is the first strictly positive return time. For completeness, split {X_N∈D} by the last visit to A among times 0,…,N−1; the resulting events are disjoint. Stationarity converts their sum to the expected number of visits to D before the first return to A, which dominates the probability of any such visit. Let N increase.

Apply this with A=[−K,K] and D={|x|>t}. Since π(A)>0, the preceding estimates imply π(D)≥c t^{−α} with c>0. Combined with Section 4, this proves C_η>0.

## 6. One-sided tails and exact moment threshold

Oddness of s and evenness of s' imply Ψ_{A,−E}(−x)=−Ψ_{A,E}(x). The noise law is symmetric, so reflecting an invariant law produces another invariant law. Uniqueness therefore makes π symmetric and splits the absolute tail equally between its signs. The positive power-tail limit makes every moment of order p≥α infinite by the tail-integral formula; Section 3 gives finiteness below α.

## Scope, attribution, and literature boundary

The registry requests an example, rather than a theorem for every neural-network loss. This example is a genuinely nonlinear single neuron, with the requested Gaussian input, persistent Gaussian labels, unchanged constant-step SGD, actual average contraction, nonarithmetic asymptotically linear multiplier, explicit positive tail law, and α<2 throughout a nonempty learning-rate interval.

Existing Math Brain T228 proofs establish substantially more than this scalar example under their stated stability assumptions. This document consolidates their mechanism and supplies an explicit contraction regime so that closing the concrete-model request does not rely on silently weakening average contraction to recurrence. No discovery credit is reassigned.

Primary background: Gürbüzbalaban–Şimşekli–Zhu, *The Heavy-Tail Phenomenon in SGD*, arXiv:2006.04740; Jelenković–Olvera-Cravioto, arXiv:1006.3295v5, Theorem 3.1. The recent Li–Lei–Wei–Wu paper arXiv:2610.23750v1 assumes regularly varying innovations and studies a vanishing-step regime. The model here has Gaussian one-step data and a fixed step, so that paper does not directly supply this theorem. A search that finds no identical theorem is not a proof of novelty.

