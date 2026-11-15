# T060 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
First retained explicit clock reading: November 15, 2026, 07:48:50 Asia/Tbilisi (03:48:50 UTC). Orientation and the bounded literature check preceded this reading by approximately eight minutes; the literature search itself ended within five minutes of its start.

## 1. Read-only orientation and literature check

Read the REPORT.md and LOG.md of rounds 1, 3 and 4, and both existing PROOF.md files. Round 1 has no PROOF.md; file discovery found no computation scripts in the three earlier folders. All earlier folders remained read only. Read the startup MEMORY.md index, BRAIN_INDEX.md and compute governor state. Task-specific restrictions prohibit writes outside this folder, so shared brain, checklist and mesh commands were not run. No git, subagents, external messages, GPU or numerical workload.

Initial directory discovery used `pwd` and `rg --files` before the priority wrapper. Subsequent shell reads used `OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 /bin/sh -c '...'`. The sandbox prints `nice: setpriority: Operation not permitted`; lowered priority is therefore unverified. Only brief reads and artifact operations are planned.

The bounded literature check used the web tool, immediately after orientation:

- `"2610.34330" Haldane uniqueness`
- `"spin-1 Heisenberg" "uniqueness" "2026" Tasaki`
- `Haldane Heisenberg unrestricted ground state uniqueness November 2026 proof`
- `Tasaki Heisenberg ground state uniqueness after October 27 2026`

Opened Hal Tasaki, *On the uniqueness of translation-invariant ground states of the S=1 Heisenberg and J–D antiferromagnetic chains*, arXiv:2610.34330v2, https://arxiv.org/abs/2610.34330 and https://arxiv.org/html/2610.34330v2 . Checked Theorem 2.1, equation (2.12), and Section 11. The theorem supplies purity and a local gap inequality, conditional here on its numerical premises. Its unrestricted uniqueness limitation remains explicit. No later solution of that remaining question was found. The already reported periodic-gap result does not trigger a new stop branch. No new finite numerical premise is claimed to have been verified.

## 2. Independent re-check of round 4

The main normal-sector exclusion holds. Re-derived it using a purification instead of diagonalizing the density operator. If T represents a normal competing ground state in the known GNS space H, take a purification Psi in H tensor an auxiliary separable Hilbert space. For any negative-frequency average A_f, ground-state spectral positivity gives rho(A_f* A_f)=0, hence (pi(A_f) tensor 1)Psi=0. Pair the first tensor factor with the vacuum Omega. With F(s)=integral f(t)exp(its)dt, covariance gives ((<Omega|pi(A)F(-K)) tensor 1)Psi=0. Cyclicity implies (F(-K) tensor 1)Psi=0. Smooth F supported on negative frequencies exhaust the strictly positive spectrum of K. Therefore Psi lies in ker K tensor the auxiliary space. The local gap inequality makes ker K=span{Omega}, so rho=omega. No purity assumption is needed for this re-check. Zero-energy multiplicity is essential.

Independent sign check: K=diag(0,E), A=|0><1| has alpha_t(A)=exp(-itE)A, so A_f=F(-E)A. This annihilates the vacuum and detects the excited vector, agreeing with F(-K). There is no earlier computation to rerun.

## 3. One extension selected before proof

Prove that a competing ground state whose discrepancy vanishes in norm on the algebra outside growing finite intervals must equal omega. This gives a condition directly on observable expectations rather than on trace-class preparations or finite-rank tightness. Investigate the stronger exact statement that deleting any finite interval leaves the norm distance between a ground state and omega unchanged. The key additional published premise is purity of omega. A finite interval is a full matrix tensor factor; its removal should preserve the weight of the normal sector of an arbitrary state. Prove that sector weight is a ground-state component, then apply the independently checked round-4 exclusion. Fixed-block density convergence cannot substitute for a norm estimate on the whole complement.

No claim to literature priority is intended for this general operator-algebraic deduction. No Hamiltonian-specific tail estimate is assumed.

## 4. Extension derived; exact statement

For every competing ground state rho there is a number p in [0,1] and, if p<1, a ground state sigma disjoint from the representation of omega, such that rho=p omega+(1-p)sigma. For every finite interval I,

`||(rho-omega)|A_(I^c)|| = ||rho-omega|| = 2(1-p)`.

Here the complement algebra contains arbitrary finite joint observables on both sides of I. Purity of omega identifies its normal representation sector with a single irreducible factor. Covariance makes the central projection onto that sector invariant under time evolution. Cutting a ground vector by this projection preserves nonnegative energy, so each sector component is a ground state. Round 4 identifies the normal component as omega. Finally A=M_d tensor A_(I^c), and its normal-sector central projection is 1 tensor the corresponding tail projection. Thus deleting I preserves p. Evaluation on this central projection and norm additivity prove the displayed formula.

Consequences: norm convergence to omega outside expanding intervals forces equality; any distinct pure ground state has distance two from omega on the complement of every finite interval. A tail distance strictly below two suffices for a pure competitor, but not for an arbitrary mixed one. The full proof and adversarial checks are being written in PROOF.md. Governor at 07:48:37 reported `ok / owner_away_open`. No heavy run is needed.

## 5. Audit sharpened the premises; examples checked independently

The exact formula does not actually need purity of omega. Finite matrix-unit decomposition works in any nondegenerate representation, and its central normal-sector projection still factors as 1 tensor the complement projection. Removed the unnecessary purity assumption from the final theorem. The selected extension remains the same norm criterion; its proof now uses only the round-4 gap premise. The local gap itself is only used through the normal-sector lemma.

Wrote the equivalent finite-matrix statement: for each fixed n, trace distances on the two-interval regions `[-m,-n-1] union [n+1,m]` increase as m grows and converge to the full state norm distance. This follows from density of the increasing finite algebras in the complement algebra, and finite-dimensional trace-norm duality. No assertion about support-size bounds follows.

Re-derived every coefficient independently: the norm is 2(1-p) both by evaluating 2z-1 and by adding the positive/negative masses in the Jordan decomposition. A two-sector diagonal matrix gives eigenvalues plus/minus (1-p). A separate actual-chain check uses h=(1-Z_x Z_(x+1))/2: the all-zero GNS basis consists of finite flipped sets F, the energy is the number of boundary bonds of F, and every nonempty finite F has energy at least 2. Thus gamma=2 is exact. Mixtures of the two constant ground states attain tail norm 2(1-p), witnessed by a single-site Z outside any removed interval. This checks the mixed-state caveat under the actual gap premise, rather than only in an abstract matrix model.

Tried to replace complement norm by the earlier fixed-block density condition. The product configuration with defects at 2^n has zero upper Banach defect density, but distance two on every complement. Independent density count: after discarding the first R sites, remaining defects are separated by at least 2^R; an interval of N sites contains at most R+1+N/2^R defects. Fixed-block translates inherit the factor given by block length. Let N tend to infinity first, then R tend to infinity. This state is not a ground state of the Ising test Hamiltonian: an isolated flip has local stability value -2. The example does not purport to construct a Heisenberg competitor.

Two patch attempts failed because a context line did not match; apply_patch made no edit on those attempts. Applied the intended changes with narrower matching contexts. No computation was run.

## 6. Readback and final artifacts

Read the entire PROOF.md with:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 /bin/sh -c 'wc -l -c LOG.md PROOF.md; cat PROOF.md; date "+%Y-%m-%d %H:%M:%S %Z"'
```

Output at that point: LOG.md 53 lines / 8280 bytes; PROOF.md 210 lines / 18438 bytes. Readback ended at 07:54:01 Asia/Tbilisi; exit status 0, with the priority warning. Subsequent edits expanded the stationarity/core justification, made the nearest-neighbor scope explicit rather than leave a finite-range bound implicit, supplied the bounded-commutator domain argument used in sector cutting, and ordered the example equation tags. Wrote REPORT.md with the conditional verdict, new result, failed stronger inference, commands and remaining target. Only these three new mathematical artifacts were created here.

Final mathematical audit: sector cutting uses an invariant central projection, not an arbitrary convex decomposition. The complement is the full joint algebra on both sides. The equality of sector weights follows from the explicit matrix-unit decomposition and the entrywise kernel calculation. No purity of a finite marginal, irreducibility, half-chain factorization or Hamiltonian-specific normality claim is used. The distinction between a pure competitor and a mixed one is retained. All constants were checked analytically by the independent examples above. No heavy computation, numerical certificate, external write or unrestricted uniqueness proof is claimed.

Ran the final validation:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 /bin/sh -c 'head -n 1 REPORT.md; wc -l -c REPORT.md PROOF.md LOG.md; test -s REPORT.md && test -s PROOF.md && test -s LOG.md; rg -n "tag|purity|irreducib|finite-range" PROOF.md; date "+%Y-%m-%d %H:%M:%S %Z"'
```

Exit status 0 at 07:56:14 Asia/Tbilisi, with the previously noted priority warning. REPORT.md: 28 lines / 4330 bytes; PROOF.md: 214 lines / 19231 bytes; LOG.md: 65 lines / 9766 bytes before this final append. The first report line begins exactly `VERDICT: PARTIAL`. All three files are nonempty. The final grep confirmed equation order and the explicit absence of a purity or irreducibility requirement. The Ising example is finite range and specifically nearest neighbor; no broader interaction-range argument is required.
