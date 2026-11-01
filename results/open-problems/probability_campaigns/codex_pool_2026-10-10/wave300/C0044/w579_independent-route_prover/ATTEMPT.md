# C0044 independent route — pre-proof commitment

Recorded 2026-10-10 before reading any current core-lane proposed proof.

The candidate route is to view the quenched probability of directional escape as a bounded harmonic function of the environment seen from the particle. Use martingale quadratic variation and invariant-measure energy to identify what would force this harmonic function to be constant. Track exactly where absolute continuity, spatial ergodicity, or uniform integrability of occupation densities is needed; an invariant measure obtained by compactness need not preserve the original environment law.

I will first derive the harmonic-energy identities and an explicit sufficient condition on the occupation densities. If prior work already uses this route, retain only a disjoint quantitative lemma after claiming its boundary. I have not read the current core-lane proposed proof.

Hardest anticipated gap: an arbitrary elliptic iid environment need not have an available invariant law absolutely continuous with respect to the original environment law. No such existence is assumed proved.

## Exact target and prior-attempt digest

The target and the separation between strict and uniform ellipticity are in STATEMENT.md. Intake problems.jsonl line 44 cites Drewitz–Ramirez, Selected Topics in Random Walk in Random Environment, Open Question 3.2, p. 42, with (E) and (IID). The author's university PDF search result displays the same question; fetching the full PDF timed out. Zerner's primary introduction at arXiv:0706.0745v1 independently supplies the precise model and directional event.

C0044-A001 (attempts.jsonl line 35) uses planar intersection of oppositely directed walks and speculates about fresh-environment averaging. C0044-A002 (line 121) corrects its empty assertion about disjoint events. The actual planar theorem concerns P_0(A_ell), while Kalikow's theorem concerns P_0(A_ell union A_-ell). The recorded obstruction is the lack of forced intersection in higher dimensions and lack of finite-region measurability of the quenched escape probability. Exact source/store rows are saved in C0044_PRIOR_EXTRACT.json. The two queried canonical-store cards are dated intake material, not owner proof certificates.

Targeted C0044 searches found no additional matching proof in the named H/I attempt directories; the Lean annotated ranking still says attempted_un. Team O's board has no C0044 assignment. The newer probability300 board groups w576–w587 on C0044. No current core-lane proof has been read. I claim only the finite-time reverse-density formulas and quantitative concentration obstruction below, and have requested method boundaries from peers.

Scars used: prob1000_ranking_hour_555_problems_and_the_unread_inbox_corrections_2026_09_07; gist_evidence_ladder_for_untrusted_work_2026_07_15; perceptron_proof_open_gaps_fleet_2026_07_12; proof_steps_need_derived_joint_structure_2026_09_09. The third top recall hit concerned forbidden trading material and was not opened. Source/hash checks are provenance, not mathematical proof.

## Setup for the independent lemmas

The following derivation works in every d >= 1. P is stationary and ergodic under the full Z^d translation group, supported on strictly elliptic nearest-neighbor environments. IID is a sufficient condition for this ergodicity, but is not used otherwise. Write omega(x,e) for the probability of displacement e at x, and (T_x omega)(y,e) = omega(x+y,e). Put eta_n = T_{X_n} omega, mu_n = Law_{P_0}(eta_n), and

    R phi(omega) = sum_e omega(0,e) phi(T_e omega).

Fix nonzero ell and put h(omega) = P_{0,omega}(A_ell), p = E_P h, and u = h(1-h). The canonical product environment space is standard Borel. Finite-dimensional path kernels are measurable, hence the path law and the probability of the Borel event A_ell are measurable. No local measurability of h is assumed.

All equalities of environment functions are taken on a single P-full set on which they hold for every integer translate; countability of Z^d allows this choice.

## L1. Exact reverse-density formula

For every n >= 0, mu_n is absolutely continuous with respect to P, with density

    f_n(omega) = sum_{x in Z^d} P_{-x,omega}(X_n = 0).

Only sites with |x|_1 <= n contribute. In particular f_0 = 1, E_P f_n = 1, and

    f_{n+1}(omega) = sum_e omega(-e,e) f_n(T_-e omega).

Proof. For bounded measurable phi, the definition of eta_n gives

    E_{P_0} phi(eta_n)
      = sum_x E_P[P_{0,omega}(X_n=x) phi(T_x omega)].

In the x term change variables zeta = T_x omega. Stationarity preserves P, and translation covariance of the fixed-environment path law turns P_{0,omega}(X_n=x) into P_{-x,zeta}(X_n=0). This proves the density formula by integration against phi. Applying the same change of variables to integral f_n R phi dP gives the displayed adjoint recurrence. No independence of visited environments is asserted. The crude bound f_n <= (2n+1)^d is finite but not uniform in n.

For N >= 1 put bar_mu_N = N^{-1} sum_{n=0}^{N-1} mu_n, with density bar_f_N = N^{-1} sum_{n=0}^{N-1} f_n.

## L2. Harmonicity and strict interior under a mixed annealed probability

Rh = h. If 0 < p < 1, then 0 < h < 1 P-almost surely, so u > 0 P-almost surely.

Proof. Directional escape is unaffected by dropping a finite path prefix or adding a finite starting displacement. Conditioning on the first step therefore gives Rh = h. If h(omega)=0, strict positivity of every omega(0,e) forces h(T_e omega)=0 for every e. Conversely, if h(T_e omega)=0, the harmonic identity there, including the positive transition of displacement -e, forces h(omega)=0. Thus {h=0} is invariant under every integer translation modulo null sets. Ergodicity makes its P-probability 0 or 1; p>0 excludes 1. Apply the same argument to the harmonic function 1-h, using p<1, to exclude h=1.

This does not show that h itself is translation invariant. Positivity propagation is weaker than constancy.

## L3. Martingale uncertainty collapse and energy identity

Let F_n contain the whole environment and X_0,...,X_n. Then

    M_n = h(eta_n) = E_{P_0}[1_{A_ell} | F_n]

and M_n tends to 1_{A_ell} almost surely and in L2. Consequently

    D_n := integral u f_n dP = E_{P_0}[M_n(1-M_n)] -> 0,
    m_N := integral u bar_f_N dP = N^{-1} sum_{n<N} D_n -> 0.

Define Gamma_h = sum_e omega(0,e)(h(T_e omega)-h(omega))^2. For every n,

    D_n = E_P u - sum_{j=0}^{n-1} integral Gamma_h f_j dP,
    sum_{j>=0} integral Gamma_h f_j dP = E_P u.

Proof. The fixed-environment Markov property gives the conditional-expectation identity at deterministic times. The increasing sigma-fields generate the full environment/path sigma-field containing A_ell. The upward martingale convergence theorem gives the indicator limit; boundedness gives L2 convergence and uncertainty collapse. Conditional on F_j, the square of the next martingale increment has expectation Gamma_h(eta_j). Orthogonality follows from the tower property applied to F_j-measurable earlier increments; it does not require independent increments. Summing E[M_{j+1}^2]-E[M_j^2] gives the finite identity. Its limit uses D_n -> 0 and nonnegative summands. The total is E_P[h(1-h)], not p(1-p): the environment is already known in F_0.

## L4. Uniform-integrability criterion — a restricted zero-one theorem

If there is a subsequence n_k -> infinity for which {f_{n_k}} is uniformly integrable in L1(P), then p is 0 or 1. The same conclusion holds if {bar_f_{N_k}} is uniformly integrable for some N_k -> infinity. A uniform L^r(P) bound for one r>1, or a uniform bound on integral f log f dP, suffices for the respective subsequence.

Proof. Suppose 0<p<1. By L2, delta_t := P(u <= t) tends to 0 as t decreases to 0. For any density g with uncertainty a=integral u g dP,

    integral_{u<=t} g dP >= 1-a/t.                    (4.1)

Indeed a >= t integral_{u>t} g dP. Along either subsequence a tends to 0 by L3. Uniform integrability implies uniform absolute continuity: choose K so all integral_{g>K} g are small, then integral_B g <= K P(B) + integral_{g>K} g. Taking B={u<=t} sufficiently small contradicts (4.1), whose right side tends to 1 at fixed t. The L^r condition implies uniform integrability by Holder's inequality; the entropy condition follows from the superlinear positive tail of x log x (its negative part is bounded).

This is a sufficient condition, not an equivalence and not a claim that IID guarantees it.

## L5. Quantitative density and entropy obstruction

Under 0<p<1, write g for f_n or bar_f_N, a for its uncertainty D_n or m_N, and b=(1-a/t)_+. For every t>0 with 0<delta_t=P(u<=t)<1 and every r>1,

    ||g||_r >= b delta_t^{-(1-1/r)},
    integral g log g dP >= b log(1/delta_t) - log 2.  (5.1)

Therefore ||f_n||_r and ||bar_f_N||_r tend to +infinity for each r>1. Both relative entropies also tend to +infinity. Each finite-time density is finite and absolutely continuous; the obstruction is loss of uniform control over time.

Proof. Set B={u<=t} and alpha=integral_B g dP >= b by (4.1). Holder gives alpha <= ||g||_r delta_t^{1-1/r}. Jensen applied separately on B and its complement gives

    integral g log g dP
      >= alpha log(alpha/delta_t)
         + (1-alpha) log((1-alpha)/(1-delta_t))
      >= alpha log(1/delta_t) - log 2
      >= b log(1/delta_t) - log 2.

Use 0 log 0 = 0. For sufficiently large times a<t/2, so b>=1/2. Under the mixed hypothesis delta_t>0 for every t>0: otherwise u>t P-almost surely, whence every mu_n has D_n>=t, contradicting L3. Choose t first to make delta_t arbitrarily small, and then choose the time. This proves divergence, not merely unboundedness. The arguments use no unproved product of conditional probabilities.

## L6. A concrete sufficient subclass

If, in addition, sum_e omega(-e,e)=1 P-almost surely, then P is invariant for R: integration and stationarity give integral R phi dP = integral phi sum_e omega(-e,e) dP = integral phi dP. Thus f_n=1 for every n, L4 applies, and the directional zero-one law holds.

This doubly stochastic, stationary ergodic subclass is a genuine extra hypothesis. It is not supplied by IID row sampling. In an IID environment, the incoming probabilities at distinct neighboring sites are independent; imposing their sum to be deterministically one forces each incoming component to have zero variance, so within the IID class this sufficient subclass reduces to deterministic transition rows. Its purpose is a checked endpoint and a control, not a resolution of C0044.

## Single hardest gap and outcome

GAP-G1: establish any condition excluding the concentration in L5 under arbitrary strictly elliptic IID rows, without silently assuming an absolutely continuous invariant probability, finite regeneration mean, a deterministic drift, or local measurability of h. A UI subsequence would suffice, but is stronger than the desired directional law and is not justified by this attempt. Compactness of occupation measures alone cannot supply uniform absolute continuity.

No full C0044 proof is obtained. L1–L6 are complete author derivations offered for independent checking, with L4 and L6 restricted results. The public claimed solution has not been audited at its implementation theorem. This packet makes no novelty claim and no parent-problem solved claim.

Peer boundary accepted: w580 reports independent energy-framework overlap and retains the disjoint IID one-step bias/covariance identity. I retain occupation-density/UI and uncertainty concentration. The local one-step control was changed to a periodic stationary environment so it does not repeat w580's exact IID computation. His source-implementation check remains his lane.

NEXT: Referee w581 checks L2's null-set propagation and L3's filtration, then L5's quantitative bounds; a further proof attempt should attack GAP-G1 rather than repeat an openness search.
