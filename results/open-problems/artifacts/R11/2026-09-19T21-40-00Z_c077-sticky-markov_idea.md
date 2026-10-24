# R11 / I0054 research idea before code — sticky-Markov harmonic-grid fragmentation

Model requested by owner: GPT-6 maximum. Actual runtime: GPT-5.6 Sol; reasoning level UNVERIFIED, so GPT-6 / maximum is not claimed.

Source target: Aldous--Janson, arXiv:2303.02529v3, Open Problem 18 / I0054. Frozen metric baseline from the newest R11 report: 76 author-side model classes with complete fixed-restriction / projective CTCS(infinity) convergence proofs under the frozen equivalence convention.

Methods selected from the preceding handoff: **#1 CHANGE THE CATEGORY, #13 FIND WHAT ONLY INCREASES/DECREASES, #27 SWAP THE QUANTIFIERS.**

This note records the mathematical route before any new checker is written.

## New category

Previous C001 uses independent Bernoulli paintbox colors. Replace each paintbox mark by a **fresh stationary two-state Markov field along the ambient label line**. Dependence is therefore spatial and finite-N nonexchangeability is real, but it is made asymptotically invisible by a vanishing persistence parameter.

For N >= 2, let

    x_j = j/N,  1 <= j <= N-1,
    eps_N = 1/N,
    lambda_{N,j} = N/[2 j (N-j)].

For every current nonsingleton block B subset [N], give each j an independent Poisson clock of rate lambda_{N,j}. At a ring, independently sample a stationary chain Y_1,...,Y_N in {0,1} with stationary law

    pi_x(1)=x, pi_x(0)=1-x

and transition kernel

    K_{x,eps}(a,b) = (1-eps) pi_x(b) + eps 1{a=b}.

Split B into the two Y-color classes if both are nonempty; otherwise the mark is invisible. Different rings and blocks use fresh fields.

The raw proposal intensity per block is still exactly

    sum_j lambda_{N,j} = H_{N-1}.

## Method #13: correlation contracts exactly with ambient distance

Write Pi for the rank-one kernel whose every row is pi_x. Since Pi^2=Pi and I Pi=Pi I,

    K = eps I + (1-eps) Pi

has the exact d-step form

    K^d = eps^d I + (1-eps^d) Pi.

Thus the memory coefficient is exactly eps^d and decreases with the distance d between labels.

For fixed visible labels r_1<...<r_m, couple the restricted Markov field to iid Bernoulli(x) colors sequentially. Across gap d_q=r_{q+1}-r_q, refresh from pi_x with probability 1-eps^{d_q}, and retain the previous state with probability eps^{d_q}. Therefore

    || Law(Y_{r_1},...,Y_{r_m}) - pi_x^{\otimes m} ||_TV
       <= sum_{q=1}^{m-1} eps^{d_q}
       <= (m-1) eps.

This is uniform in x and in the actual visible labels.

Consequently, for any specified unordered nontrivial visible split A|A^c of a visible block V, |V|=m,

    | q_N^Markov(V,A) - q_N^iid(m,|A|) |
      <= (m-1) eps_N sum_j lambda_{N,j}
      = (m-1) H_{N-1}/N -> 0.

The iid comparator is exactly C001's harmonic-grid paintbox rate

    q_N^iid(m,i)
      = (1/N) sum_{j=1}^{N-1}
          (j/N)^{i-1}(1-j/N)^{m-i-1}
      -> B(i,m-i).

Hence every specified visible split rate tends to the CTCS rate B(i,m-i).

## Method #27: one schedule must work for every fixed restriction

The quantifiers are handled by choosing a single persistence schedule eps_N=1/N before choosing k. Then for every fixed k, simultaneously for every state and transition of the finite partition chain on [k], the rate error caused by Markov dependence is O_k(H_N/N)=o(1). No k-dependent tuning is used.

Hidden labels lump out exactly: a hidden-only split leaves the visible carrier in one daughter, which receives fresh clocks and fresh ambient Markov fields with the same global-N law. Therefore the [k]-restriction is itself a finite-state time-homogeneous CTMC (not exchangeable at finite N), and entrywise generator convergence to the CTCS[k] generator follows. Common-clock uniformization should then give path total-variation convergence on every compact interval, hence J_1 convergence and the frozen projective CTCS(infinity) limit.

## Finite non-equivalence target

At N=4, eps=1/4. The source finite CTCS(4) is exchangeable, while this model should have different specified rates for end labels and middle labels, and different balanced split rates depending on adjacency. A rational exact checker will compute this array only after this idea note is committed. Any nonconstant same-size split-rate multiset is invariant evidence against equivalence by leaf relabeling plus positive global time rescaling; normalized root topology supplies an additional witness.

## Prior-art posture before checking

Stationary two-state Markov chains and paintbox fragmentation mechanisms are classical. A bounded search this run found Crane's consistent Markov partition processes generated from paintboxes and general spatially dependent fragmentation literature, but no checked source using this sticky Markov-coloring perturbation to answer Aldous--Janson Open Problem 18. No generic Markov-chain or paintbox ingredient is claimed novel. Candidate novelty is only the CTCS-specific vanishing-persistence compiler and this concrete finite discrete hierarchy.

If the exact finite witness fails, this route is not counted. If it passes and the full generator/path argument survives exact checking, call the new class C077 author-side proved but keep the source/campaign status PARTIAL pending the canonical admission gate and two independent OTHER-track audits.