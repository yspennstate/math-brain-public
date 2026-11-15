# T060 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
First recorded clock: November 15, 2026, 04:31:30 Asia/Tbilisi (00:31:30 UTC).

## 1. Orientation and bounded literature check

Read both prior folders' REPORT.md and LOG.md, round 1's SOLVED_ELSEWHERE.md, and round 3's entire PROOF.md. File discovery found no computation scripts in either prior folder and no PROOF.md in round 1. Earlier folders were read only. No git or subagents. The task-specific restriction to this folder overrides shared checklist, mesh and memory writes; those were not requested. A startup brain recall returned no useful Haldane memory; its output mentioned an attempted background index refresh, so no further brain calls will be made. Read the brain index and compute state: warn / owner_away_open, CPU saturated. No numerical workload is needed.

Shell reads were wrapped, after initial directory discovery, with OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15. The sandbox prints `nice: setpriority: Operation not permitted`; the requested lowered priority is therefore not verified. Restrict shell work to short file operations.

Web searches, within the first five minutes:

- `"Haldane" "Tasaki" "2026" Heisenberg uniqueness`
- `"2610.34330" uniqueness ground states`
- `spin 1 Heisenberg chain infinite volume uniqueness proof November 2026`

Opened primary pages: Hal Tasaki, *On the uniqueness of translation-invariant ground states of the S=1 Heisenberg and J–D antiferromagnetic chains*, https://arxiv.org/abs/2610.34330 and https://arxiv.org/html/2610.34330v2; Sirui Lu, *Bridging Gaps with Tensor Networks: From the Haldane Gap and Beyond*, https://arxiv.org/abs/2611.11049. Checked Tasaki's Theorem 2.1, gap inequality (2.12), and discussion (Section 11). They still distinguish translation-invariant uniqueness from unrestricted uniqueness. No later solution of the latter was found. The already reported periodic result is not a new stop condition. Literature phase ends here.

## 2. Independent check of the round 3 result

Re-derived the main claim using probability measures on the compact ground-state set G. For any varying rho_N in G and interval starts m_N, put mu_N=N^{-1} sum_{x=m_N}^{m_N+N-1} delta_{rho_N composed with tau^x}. A subsequential weak limit mu has barycenter omega: translating its barycenter changes each local expectation by at most 2||A||/N, so uniqueness of the invariant ground state identifies the limit. A measure with a pure-state barycenter must be delta_omega. To see this without assuming it, if a self-adjoint local A has nonconstant value under mu, split mu at a threshold strictly above or below omega(A), producing a nontrivial convex decomposition of omega with one component having a different A expectation. Extremality forbids it. A countable separating collection of local observables then shows mu is concentrated at omega. For fixed block I, f(rho)=||rho_I-omega_I||_1 is continuous and bounded by 2, so integral f dmu_N tends to zero uniformly over rho_N,m_N by the same subsequence argument. Markov's inequality gives the exceptional-density assertion. This independently verifies the earlier result. Finite-period exclusion follows by averaging a finite orbit and extremality, as in the earlier proof.

## 3. Choice of one extension, before proof

Exclude competing ground states obtained from omega by a local operation. Start with a local unitary U: testing local stability in omega_U(A)=omega(U* A U) with B=U* reverses the excitation energy omega(U*[H,U]). The gap bounds this energy below by gamma(1-|omega(U)|^2), forcing omega_U=omega. Investigate whether the same conclusion holds for an arbitrary local filter C, omega_C(A)=omega(C*AC)/omega(C*C), and for limits of such operations. This addresses an explicit class of sparse discrepancies that density alone cannot exclude. It does not assume that every competitor has such a representation.

Commands so far: `rg --files` and `find ... -maxdepth 1 -type f -print` for file discovery; `cat` on the prior reports/proof and `sed` on logs, all read only. No scripts existed to rerun. Outputs confirmed the prior file inventory and the complete round 3 argument. The analytic extension and its audit will be recorded below as completed.

## 4. Selected extension sharpened within the same scope

The local-filter question admits a representation-theoretic formulation: exclude every ground state normal in the GNS representation of omega. This includes local filtered states, their finite mixtures and their limits in the norm of functionals. A proof uses smooth negative-frequency averages of observables. Such averages annihilate the ground vector in every ground-state representation. In the representation of omega, their matrix elements against its ground vector detect every component at strictly positive energy. Normality transfers their zero expectation to each vector in a trace-class decomposition, forcing support in the one-dimensional zero-energy subspace. The local gap inequality makes that subspace one dimensional. The proof will spell out the frequency convention and both zero-energy and positive-energy cases; no assumption about the representation of an arbitrary competing state will be smuggled in.

The local-unitary calculation will serve as an independent direct check and give an explicit local-stability violation, at least gamma times the square of a block discrepancy divided by four. This remains one extension: exclusion of locally created defects and the normal states they generate. It will not prove that every Heisenberg ground state is normal in this representation.

## 5. Proof and adversarial checks

Wrote PROOF.md with the normal-sector exclusion, local-filter interpretation and a direct quantitative unitary check. No computation script is needed: the result uses no new finite certificate or estimated constant. The ground-state dynamical characterization is derived from local stability: first stationarity using 1+zB, then an analytic-commutator bound and the analytic-vector core theorem, then positivity of the implementing Hamiltonian. The normal-sector proof does not require irreducibility, purity of finite-block marginals or translation invariance of the competitor.

Independent checks of the load-bearing signs and constants:

- Frequency convention: F(s)=integral f(t) exp(its) dt. On a two-level system K=diag(0,Delta), A=|0><1| evolves as exp(-it Delta) A, so A_f=F(-Delta) A. It annihilates the vacuum and detects the excited vector. This agrees with both F(K_theta) in equation (10) and F(-K) in equation (13). Reversing the sign in (13) would make the proof fail; the direct two-level check excludes that error.
- The ground-state test for a local unitary is exactly -E_U. Independently, in the same two-level system with U exchanging the levels, E_U=Delta and the inverse test in the excited state is -Delta. Thus the sign is an energy-lowering violation, not another nonnegative energy.
- The trace norm coefficient two was checked by a second calculation. With q=|omega(U)| and b=sqrt(1-q^2), the projection difference in the basis Omega,eta is [[-b^2,q*b],[q*b,b^2]]. Squaring gives b^2 times the 2 by 2 identity. Its trace norm is therefore 2*b, in agreement with the two eigenvalues used in PROOF.md. Squaring d_I<=2*b yields b^2>=d_I^2/4, with the direction required in (17). In the orthogonal two-level example q=0,d_I=2,E_U=Delta,gamma=Delta, the bound is equality, so the factor 1/4 cannot be improved under these general premises.
- The analytic bound counts ell+2k+1 overlapping bonds, each commutator costing at most 2J. Since ell+2k+1<=2(k+ell+1), its product is bounded by (4J)^n (n+ell)!/ell!. Dividing by n! leaves a polynomial of degree ell times (4J|t|)^n, confirming the convergence radius used for stationarity and the core argument.
- Zero excitation energy is treated separately: the gap inequality makes ker K precisely the line spanned by Omega. The frequency proof only removes strictly positive spectral components. With a degenerate zero-energy subspace the conclusion is false (a finite system with H=0 supplies an immediate check), which is why this step cannot be omitted.
- A nonunitary local filter C is not treated as invertible or unitary. Its vector pi(C)Omega/sqrt(omega(C*C)) gives a positive rank-one trace-class representative directly. The denominator is required to be positive; zero-probability filters are excluded.
- Attempted stronger inference: weak-* limits of local filters need not be normal. The explicit growing flipped-interval example in PROOF.md proves this by projections converging strongly to zero but having expectation one in the limiting product state. Thus the normal-folium proof cannot be promoted to all competitors using the earlier density result.

What remains unproved: normality of an arbitrary competing Heisenberg ground state, a discrepancy-amplification lemma, any quantitative density rate, higher-spin gaps, or the finite trace inputs of the published spin-1 theorem. No unrestricted uniqueness claim is made.

## 6. Final readback and artifacts

Read the entire PROOF.md back with:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 /bin/sh -c 'wc -l -c LOG.md PROOF.md; sed -n "1,280p" PROOF.md'
```

Output at that point: LOG.md 50 lines / 9129 bytes; PROOF.md 175 lines / 13455 bytes. Corrected the opening notation to define the dynamics by its derivative rather than suggest an infinite-volume Hamiltonian belongs to the quasi-local algebra. Wrote REPORT.md with the conditional verdict, exact new scope, commands, failed stronger inference, and a concrete next target: trace-class tightness of local preparations of a hypothetical competitor.

Ran:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 /bin/sh -c 'head -n 1 REPORT.md; wc -l -c REPORT.md PROOF.md LOG.md; test -s REPORT.md && test -s PROOF.md && test -s LOG.md'
```

Exit status 0. REPORT.md: 24 lines / 3763 bytes; PROOF.md: 176 lines / 13449 bytes; LOG.md: 50 lines / 9129 bytes before this append. First line exactly: `VERDICT: PARTIAL exclusion of normal competing ground states, conditional on the published local gap inequality`. The priority warning recurred. At 00:39:30 UTC the three artifacts were present and nonempty. No new computation or literature claim depends on the readback commands.

Final mathematical audit: checked that the negative-frequency annihilation is used only after the ground-state implementer has been proved nonnegative; that cyclicity, not an unproved irreducibility assumption, supplies the dense testing vectors; that zero-energy components are handled by the local gap; and that the normal-folium closure uses norm convergence, never weak-* convergence. The remaining normality/tightness target is explicitly an unproved target, not an inference from density.
