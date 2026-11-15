# T065 work log

Task received: “push this problem forward by one checkable piece.” Session opened 2026-11-14 20:49 Asia/Tbilisi (16:49 UTC); the prompt supplies no separate ask timestamp.

## 1. Orientation and constraints (16:49–16:50 UTC)

Read the startup memory index and compute state, which reported status `ok`, mode `owner_away_open`. Only the present folder will be changed. The task-specific prohibition on writes elsewhere takes precedence over global brain/checklist/mesh writes: those state-changing helpers will not run. No git and no subagents.

Commands used for orientation: `pwd`, `rg --files ...`, and `nice -n 15 env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 -B -c ...` to read startup memory and compute state. The `nice` wrapper warns `setpriority: Operation not permitted` because the process already inherits nice 20. Independent check with `os.getpriority(os.PRIO_PROCESS,0)` returned **20**: the actual priority is lower than requested. Computations will retain this inherited priority and one-thread environment.

Literature queries so far (web search):
- deterministic Hamiltonian anharmonic chain compressible Euler hydrodynamic limit 2025 2026
- hydrodynamic limit deterministic Newtonian dynamics Euler local equilibrium open problem 2024 2025
- deterministic anharmonic chain hydrodynamic Euler limit 2026 proof
- Deng Hani Ma derivation compressible Euler Newton laws 2025 hard spheres smooth potential

Opened arXiv pages 2609.18550, 2608.20252, 1009.2175. Search results identify a 2025 hard-sphere derivation and 2026 deterministic circuit models; checking their precise scope against fixed smooth interactions. These search results alone are not being treated as theorems.

## 2. Literature outcome and choice (16:51 UTC)

Opened and read:
- Mario Pulvirenti and Sergio Simonella, *Some Considerations on the Fluid-Dynamical Limit of Particle Systems*, arXiv:2609.18550 (16 September 2026), https://arxiv.org/abs/2609.18550 and https://arxiv.org/html/2609.18550v1. Its abstract still describes the fundamental Hamiltonian derivation problems as open; Section 2 identifies the unresolved deterministic local-equilibrium/ergodic step.
- Yu Deng, Zaher Hani, Xiao Ma, *Hilbert’s sixth problem: derivation of fluid equations via Boltzmann’s kinetic theory*, arXiv:2503.01800, https://arxiv.org/abs/2503.01800. Hard spheres via Boltzmann, within the separate dilute-gas line explicitly excluded from T065’s target.
- Nadine Even and Stefano Olla, *Hydrodynamic Limit for an Hamiltonian System with Boundary Conditions and Conservative Noise*, arXiv:1009.2175, https://arxiv.org/abs/1009.2175. The abstract explicitly adds random local velocity exchanges.
- Sunder Sethuraman, *Notes on Hydrodynamic Limits and Related Topics*, arXiv:2608.20252, https://arxiv.org/abs/2608.20252. Read abstract page; HTML fetch failed. No claim based on its unavailable full text.
- Sun Woo P. Kim, Friedrich Hübner, Juan P. Garrahan, Benjamin Doyon, *Circuits as a simple platform for the emergence of hydrodynamics in deterministic chaotic many-body systems*, Nature Communications 17, 8152 (2026), https://www.nature.com/articles/s41467-026-74457-3. The model is a circuit, outside Newtonian pair potentials and oscillator chains. Its introduction distinguishes the open finite-density Hamiltonian problem from dilute hard-sphere progress.

No solution or substantial advance **within the stated model class** was found. This is a bounded literature check, not an exhaustive assertion about all papers. No SOLVED_ELSEWHERE.md is warranted.

**Chosen piece, before computation:** classify additive conserved quantities whose density is an arbitrary polynomial of total degree at most 6 in the stretch and momentum at two adjacent sites, for the fixed uniformly convex potential V(r)=r²/2+r⁴/4. Compute the exact kernel of the conservation operator, including all telescoping densities. Give a finite certificate, independently rebuild the operator on a periodic ring, and justify extension to all sufficiently large rings by locality. This tests a precise possible obstruction (extra local charges) in one concrete candidate potential class. It will not prove ergodicity, full nonintegrability, or a hydrodynamic limit.

Planned dynamics: r_i=q_i-q_{i-1}, dot r_i=p_i-p_{i-1}, dot p_i=V′(r_{i+1})-V′(r_i). Stretch variables range freely; hence the statement covers charges valid on every total-stretch sector, not charges existing only after fixing one sector.

## 3. Implementation (16:53 UTC)

Created `conserved_charges.py` (standard library only). It builds an integer conservation matrix by differentiating a density on the infinite chain and grouping translated monomials. Audits: exact rational column elimination, row elimination modulo two independently trial-division-checked primes, explicit nonzero minors, independent full periodic polynomial differentiation at N=7 and N=8, and a harmonic control with a known extra current.

First run command:
`nice -n 15 env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 -B conserved_charges.py > computation.out 2>&1`

Run returned exit 1 immediately; diagnostic output is being inspected before any result is claimed.

Timestamp correction: earlier manually entered section labels 16:54 and 16:55 were ahead of the clock; corrected them to the actual 16:50 and 16:51 intervals. Wall-clock tool currently reports 16:53 UTC.

First-run failure: `resource.setrlimit(RLIMIT_RSS, (512 MiB,512 MiB))` raised `ValueError: current limit exceeds maximum limit`. The shell inherits a stricter hard RSS limit. Fixed the resource setup to take the minimum of the requested cap and inherited hard limit, never attempting to raise either limit. No algebra had run.

Literature check ended at 16:53 UTC, under four minutes from its start. The Nature page’s direct open failed on its authentication redirect; subsequently opened the paper’s arXiv page, https://arxiv.org/abs/2503.08788, confirming the same four authors and circuit scope. The primary Nature search extract was available, but no argument depends on its full text being fetched.

Second run, same command, also returned exit 1 at RSS-limit setup. Diagnosis disproved the first explanation: `getrlimit(RLIMIT_RSS)` and `getrlimit(RLIMIT_CPU)` both return `(9223372036854775807,9223372036854775807)`, effectively unlimited. The RSS-lowering call itself is rejected on this macOS/sandbox combination. Removed that optional call; retained the CPU cap, small explicit data structures, and measured peak-RSS assertion below 1 GiB. No mathematical step had run on either failed launch.

## 4. Exact computation completed (16:54 UTC)

Third run used the same command as above and returned exit 0. Exact saved output:

```text
nice: setpriority: Operation not permitted
degree=6; density_variables=4; columns=210; rows=631
rational_rank=179; nullity=31; exact_kernel_vectors=31; kernel_rank=31
prime=1000003; rank=179; certified_minor_determinant=310877
prime=1000033; rank=179; certified_minor_determinant=810340
periodic_ring_N=7: all 210 independently constructed columns match
periodic_ring_N=8: all 210 independently constructed columns match
harmonic_control: rank=177; density_nullity=33; nonzero_additive_charges=6
harmonic_current: conserved for harmonic force, NOT conserved for quartic force; residual_terms=2
effective_nice=20; elapsed_seconds=0.407; peak_rss_MiB=20.328
PASS: exact classification and independent audits; data=charge_data.json
```

Data saved in `charge_data.json`: column exponents, row monomials, sparse integer matrix, all kernel vectors, and two nonsingular-minor certificates. No trajectory simulation was used.

## 5. Audit refinement (16:55 UTC)

The support bound can be sharpened: each derivative term extends the two-site density by at most one site on **one** side, so its occupied-site diameter is at most 2, not merely 3. This gives a locality extension to every N>=5 (unique large cyclic gap), improving the originally planned N>=7. Added explicit independent periodic checks at N=5 and N=6, and a separate `verify_certificate.py` which imports no producer code. The verifier expands every saved matrix column into a full ten-variable polynomial on the N=5 ring and compares it to direct differentiation. It also checks the 31 exact kernel vectors, their independent Gram determinant, and both certified minors. These new checks justify rerunning after the code refinement.

Final producer command (exit 0):
`nice -n 15 env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 -B conserved_charges.py > computation.out 2>&1`

```text
nice: setpriority: Operation not permitted
degree=6; density_variables=4; columns=210; rows=631
rational_rank=179; nullity=31; exact_kernel_vectors=31; kernel_rank=31
prime=1000003; rank=179; certified_minor_determinant=310877
prime=1000033; rank=179; certified_minor_determinant=810340
periodic_ring_N=5: all 210 independently constructed columns match
periodic_ring_N=6: all 210 independently constructed columns match
periodic_ring_N=7: all 210 independently constructed columns match
periodic_ring_N=8: all 210 independently constructed columns match
harmonic_control: rank=177; density_nullity=33; nonzero_additive_charges=6
harmonic_current: conserved for harmonic force, NOT conserved for quartic force; residual_terms=2
effective_nice=20; elapsed_seconds=0.453; peak_rss_MiB=19.391
PASS: exact classification and independent audits; data=charge_data.json
```

Standalone verifier command:
`nice -n 15 env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 -B verify_certificate.py > verification.out 2>&1`

```text
nice: setpriority: Operation not permitted
full N=5 polynomial derivatives: 210/210 columns verified
31 exact kernel vectors; independent Gram determinant mod 1000003 = 994494
179x179 minor mod 1000003: determinant = 310877
179x179 minor mod 1000033: determinant = 810340
rank over Q and R = 179; kernel dimension = 31; quotient by 27 telescopes = 4
PASS; elapsed_seconds=0.298; peak_rss_MiB=17.406
```

## 6. Proof, report, and final audit (16:59 UTC)

Wrote `PROOF.md` with the precise all-stretch-sector theorem, every reduction step, the locality proof for N>=5, the explicit matrix construction, both minor certificates, and the analytic 31-vector independence proof. Wrote `REPORT.md` with verdict and limitations. An invertible scaling extends the same theorem to V(r)=ar²/2+br⁴/4+cr+d, a,b>0; the affine terms only add stretch and constant charges.

Additional independent audit command: `nice -n 15 env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 -B -` with the inline final-audit code in the session transcript. It imports the producer without its main routine, checks the harmonic rank with modular row elimination (independent of the saved rational column rank), and directly evaluates the original ODE and derivative of the proposed harmonic current at r=(1,2,0,0,0), p=(3,-1,4,2,-2). Output:

```text
Independent modular harmonic check: rank=177, nullity=33
Direct quartic-current derivative at r=(1,2,0,0,0): +6
Scaling identity: b*s^2/a = 1 exactly for s^2=a/b
Artifact consistency: PASS
```

The current residual was first derived by the exact polynomial operator and then by direct differentiation in PROOF.md; its sign and magnitude were checked at the explicit phase point. Density dimension 210 and telescoping dimension 27 were checked by both monomial enumeration and stars-and-bars counts. Rank 179 has exact rational, modular, and explicit minor checks. The all-N extension uses the unique largest cyclic gap, rather than extrapolating from N=5..8. The possible omitted case of conservation only on a single fixed stretch sector is explicitly outside the theorem.

No local-equilibrium estimate, ergodicity theorem, proof of full nonintegrability, or Euler hydrodynamic limit was obtained. Larger support, higher degree and nonpolynomial or nonlocal charges remain untested. No files outside this folder were written by the work; no git, subagents, external posting, or heavy computation was used.

Saved the supplementary inline audit as `audit_result.py` so it is reproducible without the transcript. Command (exit 0):

`nice -n 15 env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 -B audit_result.py > audit.out 2>&1`

```text
nice: setpriority: Operation not permitted
Independent modular harmonic check: rank=177, nullity=33
Direct quartic-current derivative at r=(1,2,0,0,0): +6
Scaling identity: b*s^2/a = 1 exactly for s^2=a/b
Artifact consistency: PASS
```

Completed 2026-11-14 about 21:00 Asia/Tbilisi. Task: “push this problem forward by one checkable piece” — session opened 20:49 Asia/Tbilisi. All three scientific scripts and their outputs are saved here.
