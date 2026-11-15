VERDICT: PARTIAL classified all cylinder subsequential limits of the earlier critical tree

For the explicit degree-three tree in the earlier report, the set of all
subsequential limits under radius conditioning is exactly

    { λ Q_A + (1−λ) Q_B : 0≤λ≤1 }.

Under Q_A the attachment edge to branch A is forced open, a uniformly chosen
infinite ray in A is forced open, and every remaining edge has its ordinary
independent Bernoulli(1/2) state. Q_B exchanges A and B. Every mixture has
exactly one infinite open cluster, containing the root, and exactly one
infinite simple ray from the root. The conditional opening probabilities
of the A attachment edge have subsequential-limit set [1/2,1].

This extends the supplied earlier report, which proved only two distinct
single-edge subsequential limits. It also proves a ratio criterion: for
these branches the full conditioned law converges if and only if
q_A(n)/(q_A(n)+q_B(n)) converges. Each branch individually has a unique
conditioned limit, with finite-prefix density Z_m/E Z_m. Their relative
survival probabilities are the entire obstruction after joining them.
An interrupted run in this folder had already drafted this extension;
that work was resumed, audited and completed here.

The proof is in PROOF.md. Beyond the prefix-density calculation, the needed
step is control between the earlier selected radii. For
N_(k−1)≤n≤N_k, k≥2, the proof gives

    q_s(n)/M_s(n) ≤ 2^(−k²+4k−9),
    |w_(n+1)−w_n| ≤ 2^(−k²+4k−11),

where M_s(n)=E Z_s(n) and w_n=q_A(n)/(q_A(n)+q_B(n)). These follow from
the previous binary plateau and a reciprocal-recursion Lipschitz bound.
The adjacent increments vanish, so the earlier alternating endpoint
weights force every intermediate mixture weight to occur.

The earlier result was independently rechecked and holds: the binomial
second moment, binary-plateau estimate, alternating suppression counts,
p_c=1/2, critical extinction at every vertex, and the root-edge probability
including its radius offset all agree. The new audit uses forward
generating-function polynomials rather than the earlier worker's
distribution-transition implementation, and explicit finite configurations
provide an additional check.

Reproduction command, run in this folder:

```sh
nice -n 15 env OMP_NUM_THREADS=1 python3 audit.py > audit_output.txt 2>&1
```

The fresh run passed 186 exact moment/survival checks, 320 prefix-density
and total-variation checks, 254 adjacent-horizon checks, explicit enumeration
of 18,010 configurations on 14 finite trees including their forced-ray
laws, 16 union-mixture identities, 459 mixture-weight increment checks,
and 40 suppression-stage certificates. Runtime was 0.261 seconds and peak
RSS 16,678,912 bytes. The process was single-threaded at inherited nice 20;
the redundant nice request warned but retained priority 20. Exact output
and the command are saved in LOG.md and audit_output.txt. stage_bounds.csv
contains exact rational analytic bounds, not simulated survival values.

The adversarial audit checked the mixture identity on every finite atom,
the size-biased prefix law by both expansion and explicit path forcing,
the plateau constant by two independent estimates, stage boundaries,
unary-only prefixes, m=0 and m=n, and the countable off-ray extinction
argument. One display defect was corrected: binary float underflow had
printed the positive k=40 increment bound as zero. Decimal rendering now
prints 1.605005e−437; the exact CSV and proof were unaffected.

The brief literature check found no verified solution of T160. Opened
sources were:

- Deepan Basu and Artem Sapozhnikov, *Kesten's incipient infinite cluster
  and quasi-multiplicativity of crossing probabilities*,
  [arXiv:1603.06884](https://arxiv.org/abs/1603.06884). Their general
  construction assumes uniqueness and quasi-multiplicativity.
- Shirshendu Chatterjee, Pranav Chinmay, Jack Hanson, and Philippe Sosoe,
  *Robust construction of the incipient infinite cluster in high dimensional
  critical percolation*, [arXiv:2502.10882](https://arxiv.org/abs/2502.10882).
  Its input is high-dimensional two-point asymptotics.
- Malo Hillairet, *Short, Quantitative Construction of the IIC in Planar
  Percolation*, [arXiv:2509.18852](https://arxiv.org/abs/2509.18852).
  This concerns planar percolation.
- Jian Ding and Zhenhao Cai, *Quasi-multiplicativity and Regularity for
  Metric Graph Gaussian Free Fields*,
  [published paper](https://doi.org/10.1007/s00220-026-05772-5).
  Remark 1.2 explicitly assumes the Bernoulli quasi-multiplicativity
  hypothesis when discussing the Bernoulli IIC; its unconditional results
  concern a different model.

What failed or remains uncertain: no Z³ ratio estimate, transitive
counterexample, or proof of the stated IIC limit was obtained. The tree
lacks transitivity and supercritical uniqueness. Even uniqueness of the
infinite cluster under every limiting law does not select a limit in this
example. No literature novelty is asserted for this classification.

Next worker: formulate an exact finite-box analogue of the branch density
calculation for Z³. Expose a fixed finite box and express the conditional
law through the exterior probabilities that its root-connected boundary
set reaches ∂B_n. Identify a sufficient ratio-convergence criterion for
these finitely many boundary states, taking account of exterior paths that
join distinct interior components. The scalar tree calculation is a test
case; it supplies no contraction or convergence of those lattice ratios.
Do not simulate the exponentially large tree: its entire limiting-law set
is now classified analytically.

Task: “take the NEXT checkable step on this problem, building on that work.”
Received 15 Nov 2026, approximately 01:38 Asia/Tbilisi; resumed approximately
03:29 Asia/Tbilisi.
