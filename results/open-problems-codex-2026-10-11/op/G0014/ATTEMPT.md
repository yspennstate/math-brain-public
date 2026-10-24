# G0014: literal refutation and a conditional repair

Date: 2026-10-11. The source was fetched directly, not inferred from memory.

## Exact source and hypotheses

Achyut Kumar and Abhinav Duddala (not Dudeja), *Two problems for threshold cascades of interacting diffusions on unimodular random trees: front propagation with a Bramson correction, and the continuous-type limit theory*, arXiv:2608.21125v1, 21 August 2026, 9 PDF pages. Theorem 2.1 is on PDF p.3; Conjecture 3.2 is on PDF p.4; Programme 3.3 continues on p.5.

Theorem 2.1 assumes (R1), dissipation kappa<1, rho(M)>1, irreducibility of M, and phi_{i,j}(-theta_0)<infinity for some theta_0>0 and every type pair. The type set in Part I is finite. Standing conventions impose finite variance of the size-biased forward-degree distribution; R1 is the companion's front-decoupling reduction in iterated finite-graph/saturation limits. R1 is an assumed black box here, not a proved exact SDE identity in this report. The source itself describes the activation times in Section 1.2 as positive and independent given types. Its reference [1] still contains arXiv:2608.XXXXX; 2608.15987 was fetched as the intake's proposed companion, without treating that identification as a proved theorem.

The conjecture asserts, together, UI of the signed derivative martingale, positivity of its limit almost surely on survival (called equivalent), and

    F(t) = c_* t - 3/(2 theta_* c_*) log t + O_P(1),

with a randomly shifted Gumbel/decorated-process assertion. Here the source defines

    B(theta)_{i,j}=M_{i,j} E[e^{-theta A_{i,j}}],
    c_* = (inf_{theta>0} log rho(B(theta))/theta)^{-1},
    D_n = rho(B(theta_*))^{-n} sum_{|v|=n} phi_{d(v)}(T_v-n Tbar)e^{-theta_* T_v}.

We answer this literal statement, rather than silently changing UI, the speed sign, or the coefficient. It is false. The scientifically intended, corrected multitype cascade question is not solved here.

## Proposition A: UI and the asserted positive limit are incompatible

Let (D_n) be an integrable real martingale on a probability space, D_0=0. Suppose D_n converges almost surely to D, D>=0 almost surely, and P(D>0)>0. Then (D_n) is not uniformly integrable.

Proof in full. The martingale property gives E D_n=0 by iterating conditional expectation. Assume UI: for every epsilon>0 there is K such that sup_n E[|D_n|; |D_n|>K]<epsilon. UI also gives sup_n E|D_n|<infinity, by splitting at K. Fatou gives E|D|<infinity. For every fixed K>0,

    E[|D|; |D|>2K] <= liminf_n E[|D_n|; |D_n|>K].

Indeed, at each outcome with |D|>2K, eventually |D_n|>K and |D_n| tends to |D|; apply Fatou to the nonnegative truncated sequence. On the other outcomes the left integrand is zero, so the pointwise liminf inequality remains valid.

Let C_L(x)=max(-L,min(x,L)). It is continuous and bounded. For fixed L, dominated convergence gives E|C_L(D_n)-C_L(D)| -> 0. Choose K as above and L=2K. Since |x-C_L(x)| <= |x|1_{|x|>L}, the triangle inequality gives

    limsup_n E|D_n-D| <= 2 epsilon.

As epsilon is arbitrary, D_n -> D in L1. Consequently E D=lim E D_n=0. For any integer k>=1, nonnegativity gives E D >= (1/k)P(D>=1/k). Hence each of these probabilities is zero. Their union is {D>0}, a contradiction. QED.

Application to the exact conjecture: its displayed definition gives D_0=0, because the root has T_root=0 and n=0. If the source's claimed martingale property holds, Proposition A applies. On extinction D_n is identically zero from some finite generation onward, hence its limit is zero. Positivity on survival therefore makes the limit globally nonnegative. Supercritical survival has positive probability in the asserted irreducible finite-type GW representation. Thus the simultaneous UI and positivity clauses cannot hold. No tail asymptotic, x log^2 x estimate, or decorated-process theorem is needed.

Scope caveat: the printed multitype martingale formula has further issues below. Proposition A is a refutation of the source's simultaneous assertions, conditional only on its asserted martingale normalization; it does not prove that an incorrectly normalized multitype sequence is a martingale. Proposition B independently refutes the printed front formula for the stated positive-activation representation.

## Proposition B: the printed speed is negative

Let M be a finite irreducible nonnegative matrix with rho(M)>1. For each (i,j) with M_{i,j}>0, let A_{i,j}>0 almost surely and E A_{i,j}<infinity. Define B(theta) as above. Then

    -infinity < I := inf_{theta>0} log rho(B(theta))/theta < 0.

Proof. Put a_max=max_{M_{i,j}>0} E A_{i,j}<infinity. Jensen gives E exp(-theta A_{i,j}) >= exp(-theta E A_{i,j}) >= exp(-theta a_max). Thus entrywise B(theta)>=exp(-theta a_max)M. Nonnegative spectral-radius monotonicity gives

    log rho(B(theta))/theta >= log rho(M)/theta-a_max >= -a_max.

For completeness, monotonicity follows from C<=D implying C^n<=D^n and from the spectral-radius formula for a matrix norm (or Perron comparison). B has exactly the same support as M, since its Laplace factors are strictly positive, and hence rho(B)>0. On the other hand exp(-theta A_{i,j})->0 almost surely as theta->infinity and is bounded by 1. Dominated convergence makes every entry of B tend to zero. Its maximum row-sum norm tends to zero, so rho(B(theta))->0. At some finite theta its Perron root is less than 1, making the displayed ratio strictly negative. These lower and upper conclusions prove -infinity<I<0. QED.

The exponential-moment hypothesis in Theorem 2.1 implies the required finite means. Its strictly positive activation times are the ones described in Section 1.2 (continuous diffusion passage from below threshold also has strictly positive passage time). Consequently c_* = 1/I is finite and negative. F(t) is a depth and is >=0 when the root seed is included. It cannot satisfy F(t)=c_*t+o(t), nor the proposed logarithmic expansion. In particular, subtracting the printed linear/logarithmic centering leaves a deterministic lower bound tending to +infinity, so the remainder is not tight. If an infinite front occurs, the claimed finite expansion fails as well.

This proof assumes strictly positive activation on each nonzero type transition, as the source's description does. With zero-time atoms allowed, the negativity step can fail; that is not needed for Proposition A. With infinitely many types, the finite-matrix proof would require additional bounds; the source's Part I explicitly uses finite matrices.

The physically consistent candidate time-per-generation speed is

    a = sup_{theta>0} [-log rho(B(theta))/theta] = -I,
    c = 1/a = -1/I > 0.

We do not call the associated LLN proved for the original SDE merely by correcting the sign.

## Proposition C: rigorous inversion of a generation-time log correction

Work on survival. Let T_n be the minimum activation time to generation n. Assume T_n is nondecreasing, tends to infinity, and

    T_n = a n + b log n + R_n,  a>0,  (R_n) tight as n->infinity.

Define F(t)=max{n:T_n<=t}. Then

    F(t) = t/a - (b/a) log t + O_P(1).

Proof. Put h(t)=t/a-(b/a)log t. For fixed K, choose n_+(t)=ceil(h(t)+K) and n_-(t)=floor(h(t)-K). Both go to infinity. Write n_+=h+K+e_+, e_+ in [0,1], and n_-=h-K+e_-, e_- in [-1,0]. Since n_±/t ->1/a, log n_±=log t-log a+o(1). Hence

    a n_± + b log n_± -t = ±aK + a e_± - b log a + o(1).

Given epsilon, tightness provides L and N such that P(|R_n|>L)<epsilon for all n>=N. Take aK>L+|b log a|+a+2. For all sufficiently large t, the deterministic expression for n_+ exceeds L+1 and that for n_- is less than -L-1. Monotonicity gives {F(t)>=n_+}={T_{n_+}<=t}, a subset of {R_{n_+}<-L}; and {F(t)<n_-}={T_{n_-}>t}, a subset of {R_{n_-}>L}. The union has probability at most 2epsilon. Outside it F(t) differs from h(t) by at most K+1. This is tightness. QED.

If the standard minimum-time BRW term is b=3/(2 theta_*), inversion gives 3c/(2 theta_*), not 3/(2 theta_* c). The difference is a factor c^2. This is a conditional reduction with explicit hypotheses, not a proof of the required multitype generation-time estimate.

## Proved conditional special case: bounded-offspring, single-type BRW

Consider an independent single-type BRW with N<=K children, m=E N>1, positive activation A, and common edge law independent of reproduction. Assume there is a finite theta>0 with f(theta)=log E sum_{children} exp(-theta A) and f(theta)=theta f'(theta), and let a=-f(theta)/theta>0. Also assume the resulting displacement law is nonlattice and has positive tilted variance. Define V=theta A+f(theta)=theta(A-a) for each child. Direct differentiation gives

    E sum e^{-V}=exp(-f(theta))E sum e^{-theta A}=1,
    E sum V e^{-V}= -theta f'(theta)+f(theta)=0.

Moreover V>=f(theta)=:ell. Thus Y=sum e^{-V}<=K exp(-ell), Z=sum V_+ e^{-V}<=K/e, and sum V^2 e^{-V}<=K sup_{v>=ell} v^2 e^{-v}<infinity. These are all the moment conditions in Chen's Theorem 1.1 and Aidekon's Theorem 1.1. The tilted variance is positive by assumption; supercriticality is m>1; nonlattice is expressly assumed. Invoking those proved theorems gives a nonnegative derivative-martingale limit positive on survival, and tightness of

    min_{|v|=n} V_v - (3/2)log n.

To justify conditioning and inversion: on extinction the generation is eventually empty, so subtracting its asymptotic mass P(extinction) from Aidekon's tail convergence and dividing by P(survival)>0 gives a proper conditional limiting distribution, since D_infinity>0 on survival. Thus the centered minima are tight on survival. Nonexplosion also holds: choose s>0 so m E exp(-s A)<1 (positive A and bounded convergence). By the branching identity and Markov's inequality, P(T_n<=j) <= exp(s j)[m E exp(-s A)]^n for every positive integer j. The sum over n is finite. Borel-Cantelli for each integer j, followed by a countable intersection, proves T_n->infinity almost surely. Monotonicity follows because each descendant path contains an ancestor path and nonnegative increments. Since V_v=theta(T_v-a n), the generation-time correction is b=3/(2theta). Proposition C therefore proves, for this explicitly specified single-type BRW on survival,

    F(t)=c t - (3c/(2theta))log t+O_P(1), c=1/a.

Its untruncated derivative martingale is not UI, by Proposition A. This is a full reduction to the stated external theorems with their hypotheses checked. It is NOT asserted that all original multitype OU cascades satisfy this special case, or that this proves a decorated-process limit for the time-indexed cascade.

## Proposition D: scalar continuous Gumbel convergence needs a lattice qualification

For any integer-valued F(t), let h(t)=ct-d log t with c>0. There is no weak limit in distribution for F(t)-h(t) as t ranges over all real times tending to infinity.

Proof. For large t, h is continuous, strictly increasing, and unbounded. There are sequences t_k,s_k tending to infinity with h(t_k)=k and h(s_k)=k+1/2. Since F(t) is integer,

    E exp(2 pi i [F(t)-h(t)]) = exp(-2 pi i h(t)).

These values are 1 along t_k and -1 along s_k. Weak convergence would force convergence of expectations of the bounded continuous cosine and sine, which is impossible. QED.

This does not forbid tightness, lattice subsequential limits, or a suitably formulated lattice point-process statement. It prevents reading the source's scalar-front claim as ordinary all-time convergence to a continuous randomly shifted Gumbel law.

## Hostile-referee checks and unresolved issues

1. A signed derivative martingale can have a positive limit without UI. The proof does not assume D_n>=0; only the asserted terminal limit is nonnegative. On extinction that limit is zero. No unproved Cauchy-tail assertion is used.
2. UI of a truncated, nonnegative derivative martingale is a different claim. The source defines the untruncated signed object; replacing it by a truncation changes the question.
3. A left Perron vector does not generally weight offspring correctly for a row-parent mean matrix. Conditional expectation requires B h=rho h, a RIGHT vector. Also h(theta) normally depends on theta and must be differentiated. The source's proposition ignores these terms. An auxiliary 2x2 calculation exhibits the left/right discrepancy; it is not advertised as an OU cascade counterexample. A repaired multitype construction must address this before using Chen, which is a single-type theorem.
4. Finite activation exponential moments do not alone establish existence of a finite boundary optimizer or positive tilted variance. Deterministic A=1 gives f(theta)=log m-theta with the infimum attained only at infinity. This auxiliary example highlights a missing assumption, without claiming deterministic passage times for an elliptic OU model.
5. Positive activation, finite types, and finite means are stated at each use in Proposition B. Zero-time atoms and infinite-type extensions require new arguments.
6. Proposition C uses only marginal uniform tightness over deterministic generations, not independent errors or a pathwise uniform coupling. Its event identities follow from monotonicity.
7. The finite algebra/terminal expectation steps are checked in obstruction.lean; the full stochastic Vitali argument, matrix argument, and source-to-SDE reduction are NOT Lean-formalized. The final Lean invocation returned EXIT_CODE=0 (one unused-variable warning). The kernel checked the nonnegative-zero-integral lemma and the two algebraic obstructions; there is no sorry, axiom added, or native_decide. See lean_check.txt for the actual result.
8. Binary offspring with Exp(1) activation is a reproducible numerical boundary test (numerical_checks.py/json): theta=3.311070407..., positive c=4.311070407..., printed c=-4.311070407...; corrected inverse coefficient=1.953025703..., printed coefficient after sign-only repair=0.105084274.... This is auxiliary evidence, not a model-matching counterexample.
9. Prior memory's claim that the repaired bounded-degree MULTITYPE martingale half is automatic is not accepted here without a correct eigenvector/spine construction. Our proved special case is expressly single-type.

## Remaining gap and verdict

SOLVED in the literal negative sense: Conjecture 3.2 as posed has mutually incompatible UI/positivity clauses, and its printed speed gives the wrong sign under its positive-activation finite-type representation. These are complete obstructions, not a proof sketch of a corrected theorem.

The corrected intended problem remains open in this report: construct the correct normalized multitype derivative martingale (with right eigenfunction and derivative terms), establish a finite optimizer/nondegenerate tilted walk and nontrivial limit for the actual offspring law, prove the generation-time minimum and extremal-process estimates under exactly the cascade assumptions and decoupling limits, invert with coefficient 3c/(2theta), and formulate the time-depth limit with the necessary lattice/subsequence qualification. No claim of SOLVED_IN_LITERATURE is made; database throttling limits the status search.
