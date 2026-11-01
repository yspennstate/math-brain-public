# T421: complete classification conditional on convergence of the second moments

Status: **proved conditional lemma; not a solution of T421.**

The remaining hypothesis is substantial: this note does not prove convergence of the second moments, give its probability under standard initialization, or certify the reported exceptional fast-tail starts. It does not establish novelty relative to all existing worker notes.

## Exact target and provenance

The current target is T421, “Adaptive edge of stability: the preconditioned sharpness,” in `<private-repo>`, `06_math_research/frontier/rows/T421/DOSSIER.md`. Inspected main head: `7db35f690af10b1ee850623c8caef38d6721a244`; dossier blob `844ff1ee84129df07c6a928787d928bdee244d7e`; registry `list.jsonl` blob `b8d4607e60eafcce5b3e8286cf882e8931737bd6`.

Target 1 asks for the long-run active curvature times eta for a two-eigenvalue diagonal quadratic, Adam beta1=0.9, beta2=0.999, epsilon=eta^p. Target 2 asks when the top preconditioned sharpness stays above the threshold while active curvature equals it. The broader row additionally asks for random initialization, burn-in, an o(1/eta) band and nonmonotonic loss decrease, without yet specifying complete quantifiers.

The current moves file already records a claimed reviewer-checked local standard-start theorem near lambda=38 and an exact two-cycle stability window, claim `T421-W706-006`. That proof was not available in the inspected tree and is not re-proved or endorsed here.

The active-curvature definition below agrees with Fong–Yang, arXiv:2608.20638v2, Section 2, equation (5), after removing their normalization c*eta. Their Proposition F.8 constructs exceptional supercritical convergent trajectories by selecting nonzero initial momentum and a positive initial second moment. It therefore does not by itself certify standard initialization m0=v0=0.

Primary source inspected: https://arxiv.org/html/2608.20638v2 . Current v2 is dated 1 October 2026; v1 and v2 have different titles and scopes.

## Algorithm and observables

Fix a positive definite diagonal quadratic

    f(x) = (1/2) sum_i lambda_i x_i^2,    lambda_i > 0,

and fixed eta>0, epsilon>0, 0<b<1 and 0<=q<1. Use the standard bias-corrected Adam equations, with m_0=v_0=0:

    g_i,t       = lambda_i x_i,t,
    m_i,t+1     = b m_i,t + (1-b) g_i,t,
    v_i,t+1     = q v_i,t + (1-q) g_i,t^2,
    d_i,t      = sqrt(v_i,t+1 / (1-q^(t+1))) + epsilon,
    x_i,t+1     = x_i,t - eta m_i,t+1 / ((1-b^(t+1)) d_i,t).

Set c=(1-b)/(1+b) and K=2/c. At b=0.9, K=38. The scalar preconditioned curvatures, top sharpness, and active curvature are

    C_i,t = lambda_i/d_i,t,
    S_t   = max_i C_i,t,
    Cact_t = [sum_i (g_i,t^2/d_i,t) C_i,t] / [sum_i g_i,t^2/d_i,t].

Cact is defined when g_t is nonzero. The same theorem applies to uncorrected Adam, by omitting both bias-correction factors. The proof also applies to other finite initial moments whenever these displayed recurrences are used and v remains nonnegative.

## Theorem

Assume every v_i,t has a finite limit. Then each coordinate has exactly one of these two behaviors:

1. **Inactive limit:** v_i,t -> 0 and x_i,t -> 0. Then C_i,t -> lambda_i/epsilon.
2. **Oscillatory limit:** there is a phase sigma_i in {-1,1} such that

       x_i,t - (-1)^t sigma_i a_i -> 0,
       a_i = eta*c/2 - epsilon/lambda_i > 0.

   In this case v_i,t -> lambda_i^2 a_i^2, d_i,t -> eta*c*lambda_i/2 and C_i,t -> K/eta. The signs alternate at every sufficiently late step.

Let A be the set of oscillatory coordinates and I its complement. If A is nonempty, then

    Cact_t -> K/eta,
    S_t -> max( K/eta, max_{i in I} lambda_i/epsilon ),
    f(x_t) -> (1/2) sum_{i in A} lambda_i a_i^2.

The inner maximum is omitted if I is empty. Consequently, conditional on convergence of all second moments and the existence of an oscillatory coordinate, a strict limiting separation of top sharpness from active curvature occurs **if and only if** there is an inactive coordinate i with

    eta*lambda_i/epsilon > K.

## Proof

It is enough first to consider one coordinate, writing lambda for its eigenvalue and V for the assumed limit of v_t. From the exact second-moment recurrence,

    lambda^2 x_t^2 = (v_t+1 - q v_t)/(1-q) -> V.

Thus |x_t| -> a=sqrt(V)/lambda. If V=0 this proves the inactive alternative and d_t -> epsilon proves its curvature assertion.

Suppose V>0, so a>0. Write

    alpha_t = eta / ((1-b^(t+1)) d_t).

Then alpha_t -> alpha=eta/(sqrt(V)+epsilon)>0 and alpha_t/alpha_t-1 -> 1. Eliminate momentum using x_t-x_t-1=-alpha_t-1 m_t. For t>=1 the exact recurrence is

    x_t+1 = [1 + b alpha_t/alpha_t-1 - (1-b)lambda alpha_t] x_t
            - b alpha_t/alpha_t-1 x_t-1.

For all sufficiently large t let s_t=sign(x_t), and let r_t=s_t*s_t-1 in {-1,1}. Since |x_t| -> a>0, division by x_t gives

    r_t+1 + b r_t -> 1+b-k,    k=(1-b)lambda alpha>0.

The four possible values of r_t+1+b r_t are 1+b, 1-b, -1+b, and -1-b. They are distinct because 0<b<1. A convergent sequence taking values in this finite set is eventually constant. Moreover each value determines the ordered pair (r_t,r_t+1) uniquely. Hence that ordered pair is eventually fixed. Consistency between two successive overlapping pairs forces its two entries to agree: eventually r_t=r_t+1=r, where r is either 1 or -1.

If r=1 the displayed limit forces k=0, contradicting k>0. Therefore r=-1, and k=2(1+b). Consequently

    sqrt(V)+epsilon = eta*(1-b)*lambda/[2(1+b)] = eta*c*lambda/2.

Since sqrt(V)=lambda*a, this gives a=eta*c/2-epsilon/lambda>0, the asserted curvature limit and eventual alternating signs. Eventual alternating signs together with |x_t| -> a yields the stated phase sigma.

Apply this argument to every coordinate. For each i in A,

    g_i,t^2/d_i,t -> lambda_i^2 a_i^2 / (eta*c*lambda_i/2) > 0;

for each i in I the same weight tends to zero, because d_i,t -> epsilon>0. Thus the total weight converges to a positive number and all nonvanishing weights multiply a curvature converging to K/eta. This proves the active-curvature limit. The maximum and loss limits follow from coordinatewise convergence. The strict-separation criterion follows immediately from the maximum formula. QED.

## Epsilon-power regimes: unconditional obstruction and conditional conclusion

For every iterate, including during bias correction,

    0 <= eta*Cact_t <= eta*S_t <= eta*lambda_max/epsilon.

For epsilon=eta^p and fixed positive eigenvalues, this gives the following rigorous conclusions.

* If p<1, eta*S_t and eta*Cact_t tend to zero as eta->0, uniformly over every time and every initialization where the active curvature is defined. Neither observable can approach 38. This resolves the impossibility portion of target 1 for the entire p<1 range.
* If p=1 and lambda_max<38, there is a uniform positive gap from 38, again independent of initialization and time. More generally an oscillatory coordinate in the theorem must have lambda_i>38.
* If p>1, the cap is not an obstruction. Under the theorem's moment-convergence hypothesis, every oscillatory coordinate has a_i=eta/38-eta^p/lambda_i; inactive supercritical coordinates account for any limiting top/active separation. This does not show that such oscillatory coordinates arise with positive or full probability.

For a parameterized family satisfying the theorem with A nonempty for every sufficiently small eta, its active-curvature limit implies an eventual o(1/eta) band with a possibly uncontrolled eta-dependent burn-in: for any delta(eta)>0 tending to zero, choose T(eta) so that |eta*Cact_t-38|<delta(eta) for all t>=T(eta). This is a consequence of convergence for each eta, not a rate estimate or a uniform-in-initialization result.

## Unresolved requirements

1. Prove (or disprove) convergence of all second moments for a specified random initialization and parameter range; local two-cycle stability alone does not provide this.
2. Determine which coordinates are inactive and the probability of that event for m0=v0=0. In particular, certify standard-start fast-tail trajectories instead of relying on floating-point shooting.
3. Bound burn-in and its eta dependence if the intended statement requires quantitative or high-probability control.
4. Establish any asserted decrease/nonmonotonicity of the loss. The theorem gives only a limiting loss; a two-cycle itself has constant loss, and convergence to it need not imply a net decrease from every starting point.

No complete proof or refutation of the repaired broad T421 row is claimed.
