# T060 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
First clock: 2026-11-15 10:17:39 Asia/Tbilisi (06:17:39 UTC).

## 1. Orientation and bounded literature check

Read the earlier folders' REPORT.md, LOG.md and available PROOF.md files. The original folder has no PROOF.md. Directory listings show no computation scripts in any earlier folder. Some batched read output was truncated; remaining sections will be read separately. All earlier folders remain read only. Read the startup MEMORY.md, BRAIN_INDEX.md and compute governor. Governor: warn, owner_away_open, CPU saturation and swap activity. No numerical workload is planned.

The task-specific prohibition on outside writes supersedes the general brain, mesh and checklist write instructions. No outside write, git, subagent or external message is used. Shell reads after initial discovery use `OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 /bin/sh -c '...'`. The sandbox prints `nice: setpriority: Operation not permitted`; priority adjustment is not verified, so no substantive computation will run.

Web search, completed within five minutes: `"2610.34330" Heisenberg uniqueness ground states`; `spin 1 Heisenberg chain Haldane conjecture proof November 2026 uniqueness`; `"Heisenberg" "uniqueness" "November" "2026" ground states`; `"2610.34330" uniqueness new proof`. Opened Hal Tasaki, *On the uniqueness of translation-invariant ground states of the S=1 Heisenberg and J–D antiferromagnetic chains*, https://arxiv.org/abs/2610.34330v2 and https://arxiv.org/html/2610.34330v2 . Equation (2.12) gives the local gap inequality; the paragraph immediately following explicitly restricts uniqueness to translation-invariant states. No later resolution of unrestricted uniqueness was found. The previously reported periodic result does not trigger a new solved-elsewhere branch.

## 2. Independent re-check of round 5

The main claim holds. Independent route: a representation of `M_d tensor B` is `id tensor eta`, by matrix units. Thus its central support in the bidual is `1 tensor z_eta`. Cutting a ground state by the invariant normal-sector projection preserves the ground-state condition: the cut vector lies in the zero eigenspace of its positive implementing Hamiltonian. Round 4's negative-frequency test shows that the normal component must be p omega. The disjoint remainder has mass 1-p and remains disjoint on B, since the same central projection factors as above. Therefore the difference has orthogonal positive and negative masses 1-p on both the full algebra and B; both norms are 2(1-p). This independently obtains the claimed constant from the Jordan decomposition, without assuming pure finite-block marginals. Invariance of the central projection and finite dimensionality of the removed factor are essential.

## 3. Choice of one extension, before proof

Try to replace the two-sided exterior witness for a distinct pure ground state by a witness in one half-chain. Add the split property of the reference state, which is expected from its pure, gapped, one-dimensional ground-state representation. The precise target: a distinct pure ground state must be disjoint from the reference on at least one half-chain at each cut; hence one fixed direction remains at norm distance two beyond every finite cutoff. Prove the operator-algebra gluing step explicitly, and check the published gap-to-split theorem before using it. This would narrow the required Heisenberg estimate from joint observables on two exterior intervals to connected intervals on each side. It does not itself supply such an estimate.

## 4. Split premise checked; extension derived

Opened Taku Matsui, *Boundedness of Entanglement Entropy, and Split Property of Quantum Spin Chains*, https://arxiv.org/abs/1109.5778 and https://arxiv.org/pdf/1109.5778 . Read Definitions 1.1–1.3, Corollary 1.6 and Section 2's discussion of split inclusions. The corollary assumes a bounded finite-range interaction and exactly the GNS gap inequality used here, including a nondegenerate zero eigenvalue. It does not require unique finite-volume ground states. In a pure split representation the half-chain von Neumann algebras are spatial type I factors. The nearest-neighbor spin-1 interaction satisfies the boundedness/range hypotheses. This is a further published theorem, not a numerical input independently checked here.

Derived the target. In a pure competitor's representation, the center of either half-chain algebra commutes with both halves and hence is scalar. Factor representations are either quasi-equivalent or disjoint, as their central supports in the bidual are minimal central projections. If neither half is disjoint from the reference, both half representations are normal representations of the reference type I factors. Successive matrix-unit decompositions then give the whole competitor representation as an amplification of the reference representation. The normal-sector lemma forces equality. Consequently a distinct pure ground state is disjoint on at least one half-chain. Disjointness survives deletion of any finite matrix tensor factor, so the same direction works beyond every finite cutoff.

Adversarial checks selected before final writing: verify the matrix-unit gluing without assuming the competitor has a gap or split property; check finite-factor deletion on restricted states rather than just on an ambient representation; use an actual Ising kink ground state to test whether both directions can be required; mix that kink with the vacuum to test the purity restriction and the factor two. No numerical run is needed.

## 5. Proof written and adversarial checks

Wrote PROOF.md with the half-chain disjointness theorem, persistence in one fixed direction, and connected-interval trace-distance formulation. The normal-sector lemma is included with its sign convention and analytic-core justification. The finite-factor proof explicitly checks that a marginal's GNS representation has the same central support as the reduced ambient representation; this avoids confusing a vector's support with its central support.

The Ising kink with zeros on x<=0 and ones on x>=1 is a pure ground state: on every finite affected interval, the fixed exterior endpoints require zero or one wall, and the kink attains that minimum. Thus the full quantum local-stability test is nonnegative for every B, including non-diagonal B. The reference all-zero state has exact GNS gap 2, because each nonempty finite flipped set has twice its number of connected components as energy. The kink agrees exactly with the reference sufficiently far left and has norm distance 2 on every right half-chain. This disproves the stronger two-direction conclusion under the stated premises.

Mixing the kink with the vacuum gives a distinct ground state with left norm zero and right norm 2(1-p)<2. This independently tests the necessity of purity in the strict-distance criterion. Checked the factor two in two ways: the single-site Z expectation difference and the eigenvalues +(1-p), -(1-p) of the diagonal density-matrix difference. Disjoint-state distance 2 was likewise obtained both by a central projection contraction and by the masses of the Jordan parts.

A potential false shortcut was rejected: norm distance 2 alone does not survive finite deletion. Kink versus vacuum on the left half ending at site 1 has distance 2, but the restrictions coincide after deleting site 1. The theorem proves disjointness first, which does survive finite deletion. No converse from distance 2 to disjointness is used.

Second independent derivations added to PROOF.md. For finite deletion, full-algebra intertwiners between `id_Md tensor eta_j` are exactly `1 tensor T`, whereas complement intertwiners are matrices of intertwiners T. Nonzero intertwiners therefore exist in one setting exactly when they exist in the other. This independently verifies the finite-erasure step in round 5's main claim, without factoring a bidual central projection. Together with the verified ground-state sector decomposition and the positive/negative masses, it re-obtains its exact norm identity.

For the new gluing step, replace the second spatial matrix-unit decomposition by finite-rank projections P_n,Q_n on the reference half spaces. Their commuting images have product r_n increasing strongly to one. The vector functionals of r_n Omega are supported on finite matrix corners in the reference representation and converge in functional norm to rho, with error at most 2||Omega-r_n Omega||. The normal predual is norm closed (its restriction is isometric by Kaplansky density), proving normality a second way. Neither proof assumes split property or a gap for rho.

## 6. Readback, final audit and commands

Completed the separately bounded reads of earlier reports/logs/proofs whose initial batched output had been truncated. `rg --files` with globs `*.py`, `*.sh`, `*.jl`, `*.sage` found no computation scripts in the four earlier folders. Their original directory listings likewise contained none. There is no earlier numerical run to repeat.

Wrote REPORT.md with the required verdict and explicit limits. Read the complete new proof in two nontruncated parts:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 /bin/sh -c 'sed -n "1,125p" PROOF.md'
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 /bin/sh -c 'sed -n "126,300p" PROOF.md'
```

Both exited 0, with the priority warning. Final audit: purity is used to make each competitor half representation a factor, not to make either marginal state pure. Factor central supports are minimal central projections, so non-disjointness yields the required normal isomorphism. Type I matrix units apply to the reference factors; no unjustified tensor decomposition is assumed for the competitor. Finite-factor deletion preserves disjointness of the actual marginal GNS representations by full central support of the restricted cyclic functional. This is stronger than mere norm orthogonality, which the kink example shows would be insufficient. The one direction is fixed before moving any cutoff. Finite-block trace distances increase in length for a fixed cutoff and reach two in the limit; no bounded-length witness is inferred.

The remaining uncertainty is Hamiltonian-specific: no strict upper bound below two has been established for the half-chain distances of any hypothetical Heisenberg competitor. The published numerical gap premises remain external. No unrestricted uniqueness proof, mixed-state extension of criterion (4), finite numerical certificate, or higher-integer-spin theorem is claimed.

Final validation command:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 /bin/sh -c 'head -n 1 REPORT.md; wc -l -c REPORT.md PROOF.md LOG.md; test -s REPORT.md && test -s PROOF.md && test -s LOG.md; rg -n "tag\{|\*\*Theorem|Corollary 1.6|disjoint|mixed" PROOF.md; date "+%Y-%m-%d %H:%M:%S %Z"'
```

Exit 0 at 2026-11-15 10:27:47 Asia/Tbilisi. REPORT.md: 31 lines, 4081 bytes; PROOF.md: 222 lines, 21836 bytes; LOG.md before this append: 57 lines, 10731 bytes. All required artifacts were nonempty; first report line begins exactly `VERDICT: PARTIAL`. Equation tags run from 1 through 19, and the source, purity, disjointness and mixed-state caveats were present. Priority warning persisted. No computation or outside mutation was performed.
