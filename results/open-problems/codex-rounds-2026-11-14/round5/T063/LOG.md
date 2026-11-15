# T063 work log

Task: “take the NEXT checkable step on this problem, building on that work”; received 15 November 2026, approximately 07:48 Asia/Tbilisi (03:48 UTC).

## Orientation and five-minute literature check

Read the startup brain instructions directly, the compute state, and the REPORT.md, LOG.md, PROOF.md and scripts available in all three earlier folders. The first folder has no PROOF.md or scripts. Only this folder may be written: no global recall logging, checklist, mesh registration or memory writes, since those mutate other folders. No git or subagents. Compute state at entry: status ok, owner_away_open; CPU busy. Only small standard-library single-thread checks will run, using the required nice launcher.

Literature search began at about 03:48 UTC and ended before 03:53 UTC. Queries included `six vertex Gaussian free field Pei 2611.00291 November 2026`, `six vertex height Gaussian free field 2610.07454 full disordered regime`, and `"2611.00291" uniqueness error revised`. Opened Yan Ru Pei, *Closing the identification step in the GFF limit: Uniqueness of the zero-slope six-vertex phase for -1 <= Delta < 1/2*, https://hexagonmath.org/pdf/2611.00291v1 and its record https://hexagonmath.org/2611.00291v1; and Emile Averous, Hugo Duminil-Copin, Tiancheng He, Piet Lammers, Ioan Manolescu, *Conformal invariance of the six-vertex model's height function*, https://arxiv.org/abs/2610.07454. A GitHub directory open of the September OpenAI manuscript failed with cache miss. The claims found are the same as in the earlier reports; no newer full-range proof was certified. Hexagon:2611.00291v1 is not an arXiv identifier. No SOLVED_ELSEWHERE.md is warranted.

## Independent recheck, in progress

Read the complete round 4 proof and independently checked its constructions: the vertex equation is r+b=s+t; Fx=(s,r,1-b,1-t) and Fy=(1-r,1-s,t,b) preserve both this equation and r != s. Four copies with common boundary give opposite complemented cuts. The logarithmic boundary loss is 3 log(2^(2A+2B))=3(W+H)log 2 when W=2A,H=2B. Straight inserted rows and columns carry weight one, preserve old arrows and have deletion as a left inverse. Fixed-block entropy bounds the limiting state's pressure from below, so the claimed near-balanced pressure maximality has the correct direction. A rerun and separate numerical cross-check follow before concluding that the earlier result holds.

## Choice of one extension

Audit Pei's Corollary 1.3 and its load-bearing dependencies, as requested by both preceding reports. The intended output is a checked missing lemma or a precisely demonstrated obstruction, not an assumption that uniqueness has been proved. Start at the variational corollary, trace to the zero-slope uniqueness theorem, and isolate a finite, falsifiable step if possible. The earlier minimisation proof alone establishes no uniqueness or GFF convergence.

## Earlier computation rerun

Command:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 ~/codex_op_1114r4/briefs/T063/check_two_flux.py
```

The unchanged script passed: independent edge enumerators agree on six shapes; Z(2,2;1,1)=4+2c^4; gluing images 6+18+18+306=348; 2296 insertion images and 60 coefficientwise comparisons. Peak RSS 15,171,584 bytes, reported elapsed 0.823 seconds, effective nice 20. The launcher's attempted priority change was denied because the inherited process is already nice 20. Together with the separate analytic derivation above, the earlier main result holds. No files in the previous folder were written.

## Audit scope fixed before new computation

Read Pei's Section 6 corollary proof and traced its uniqueness input through Theorems 1.4 and 1.5. Read Sections 3.1–3.4 and the folding/free-energy/Gibbs/Burton–Keane steps in Section 4. These are too many independent infinite-volume dependencies to certify by a finite test. The one piece chosen for a complete check is the finite-cluster swap, Lemmas 3.2–3.5.

Concrete extension: integrate out geometric residual energies and prove the finite swap directly with binary diagonal bridges. At level ell, a saddle diagonal has D=ell+1 on both endpoints or D=ell-1 on both endpoints, and D=ell on the perpendicular diagonal. Independently open each saddle with probability 1-c_v^(-2), where c_v is the weight at its vertex; other diagonals are closed. Prove that exchanging any union of interior graph clusters (NN edges plus open bridges), with shifts by ell, preserves the augmented Gibbs law. This formulation should include arbitrary inhomogeneous c_v>=1 and the endpoint c_v=1, where no bridges open. Then prove that the signs of the interior clusters, conditional on sum, absolute difference and bridge set, are independent fair signs. This is one finite-volume swap theorem, not a uniqueness or GFF theorem.

Planned adversarial checks: exhaust every admissible two-replica block and swap mask; compute weights independently from h-diagonal equalities; enumerate entire small domains including different fixed boundaries and bridges next to the collar; check orbit sizes and exact rational masses. An explicit saddle should show why omitting the bridges destroys the Gibbs symmetry for c>1. A direct all-edge 2x2 enumeration will separately recheck the earlier partition polynomials.

A read-only shell download of the already opened Pei PDF failed with DNS error; no PDF file was created. All literature inspection uses the web tool. The audit does not assume the inaccessible shell download succeeded.

## Exact binary-bridge computation

Created check_binary_swaps.py. Command:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 check_binary_swaps.py
```

Output (all arithmetic exact except runtime):

```text
nice: setpriority: Operation not permitted
OMP_NUM_THREADS=1; effective_nice=20
prior independent all-edge recheck: doubly balanced={0: 4, 4: 2}; singly balanced={0: 8, 4: 2} PASS
local psi audit: 324 block pairs; 5184 mask admissibility checks PASS
local diagonal changes={-2: 32, 0: 2360, 2: 32}; 1244 graph/involution checks; 4976 rational mass checks PASS
unbridged saddle counterexample at c=2: pair weight 4 -> 1; closed factor 1/4 repairs PASS
domain 2x2 boundary=same c=1: fillings=7x7 states=49 groups=26 max_clusters=2 swaps=107 PASS
domain 2x2 boundary=same c=3/2: fillings=7x7 states=53 groups=28 max_clusters=2 swaps=115 PASS
domain 2x2 boundary=same c=2: fillings=7x7 states=53 groups=28 max_clusters=2 swaps=115 PASS
domain 2x2 boundary=same c=inhomogeneous: fillings=7x7 states=49 groups=26 max_clusters=2 swaps=107 PASS
domain 2x2 boundary=shifted c=1: fillings=7x7 states=49 groups=49 max_clusters=0 swaps=49 PASS
domain 2x2 boundary=shifted c=3/2: fillings=7x7 states=51 groups=51 max_clusters=0 swaps=51 PASS
domain 2x2 boundary=shifted c=2: fillings=7x7 states=51 groups=51 max_clusters=0 swaps=51 PASS
domain 2x2 boundary=shifted c=inhomogeneous: fillings=7x7 states=49 groups=49 max_clusters=0 swaps=49 PASS
domain 2x2 boundary=reflected c=1: fillings=7x7 states=49 groups=42 max_clusters=2 swaps=69 PASS
domain 2x2 boundary=reflected c=3/2: fillings=7x7 states=1056 groups=968 max_clusters=2 swaps=1256 PASS
domain 2x2 boundary=reflected c=2: fillings=7x7 states=1056 groups=968 max_clusters=2 swaps=1256 PASS
domain 2x2 boundary=reflected c=inhomogeneous: fillings=7x7 states=299 groups=278 max_clusters=2 swaps=347 PASS
domain 3x2 boundary=same c=1: fillings=17x17 states=289 groups=120 max_clusters=3 swaps=873 PASS
domain 3x2 boundary=same c=3/2: fillings=17x17 states=341 groups=142 max_clusters=3 swaps=1009 PASS
domain 3x2 boundary=same c=2: fillings=17x17 states=341 groups=142 max_clusters=3 swaps=1009 PASS
domain 3x2 boundary=same c=inhomogeneous: fillings=17x17 states=341 groups=142 max_clusters=3 swaps=1009 PASS
domain 3x2 boundary=shifted c=1: fillings=17x17 states=289 groups=289 max_clusters=0 swaps=289 PASS
domain 3x2 boundary=shifted c=3/2: fillings=17x17 states=315 groups=315 max_clusters=0 swaps=315 PASS
domain 3x2 boundary=shifted c=2: fillings=17x17 states=315 groups=315 max_clusters=0 swaps=315 PASS
domain 3x2 boundary=shifted c=inhomogeneous: fillings=17x17 states=315 groups=315 max_clusters=0 swaps=315 PASS
domain 3x2 boundary=reflected c=1: fillings=17x17 states=289 groups=234 max_clusters=3 swaps=477 PASS
domain 3x2 boundary=reflected c=3/2: fillings=17x17 states=12468 groups=10980 max_clusters=3 swaps=16212 PASS
domain 3x2 boundary=reflected c=2: fillings=17x17 states=12468 groups=10980 max_clusters=3 swaps=16212 PASS
domain 3x2 boundary=reflected c=inhomogeneous: fillings=17x17 states=3238 groups=2752 max_clusters=3 swaps=4522 PASS
domain totals: states=33873 groups=29290 swap images=46129 PASS
peak_RSS_bytes=48316416; elapsed_seconds=2.106
```

The 24 domain cases use 2x2 and 3x2 interior faces, a fixed one-face collar, three pairs of boundary conditions, and four weight assignments. Inhomogeneous weights cycle through 1, 3/2, 2, 3 at successive vertices. All bridge configurations of positive weight are enumerated, including bridges with endpoints on the fixed collar. Every union of interior clusters is swapped, and its actual image is located in the independently enumerated state set. Graph equality, involution, rational mass equality, complete sign orbits and conditional mass 2^(-k) all passed. Reflected boundary conditions produce many collar saddles, so these are not just checks of interior bonds with identical boundaries. Peak RSS was below 49 MB, runtime below three seconds. The script has a 120-second alarm and asserts both one-thread settings and inherited niceness.

## Second derivations and attempts to break the theorem

Wrote the complete finite-volume proof in PROOF.md. Its load-bearing factor q_v=c_v^(-2) was derived twice: directly from the pair-weight ratio at a cut saddle, and by summing the geometric residual distribution. The direct example h1=(0,1,1,0), h2=(2,1,1,2) gives weight c^2 before a one-endpoint swap and one afterwards. The required closed factor is therefore exactly c^(-2), with no square-root ambiguity. The geometric computation separately gives sum_{n>=1}(1-q)q^n=q and n -> n-1. At c=1 the geometric law is not normalisable; the binary proof treats this endpoint directly, with all bridges closed.

The proof checks every possible changed diagonal: if a swap separates its nonzero endpoints, the perpendicular endpoints must lie at level ell by the NN graph constraint. The nonzero values are ell±1. The unit height steps then force equality in both copies for equal signs and inequality in both for opposite signs. Thus the equality-count change is precisely -2 or +2; all other diagonals have change zero. This derivation does not rely on the finite enumeration window.

To test the factor of two between psi and h levels, extended the script with 10,368 nonzero-level covariance checks and two full-domain cases at ell=-2 and ell=3. Also added an independent full-assignment, nonrecursive height count giving 7 and 17 fillings, in agreement with the recursive domain generator. The geometric projection was checked with exact finite prefixes plus exact tails and 21 individual residual mass identities.

Reran the same command after these additions. The first 24 domain cases reproduced the preceding counts. Additional and final output:

```text
nonzero-level covariance checks=10368 PASS
independent full-assignment height count 2x2=7 PASS
independent full-assignment height count 3x2=17 PASS
independent geometric projection: closed probability q; 21 saddle mass checks PASS
domain 3x2 boundary=same c=3/2 ell=-2: fillings=17x17 states=341 groups=142 max_clusters=3 swaps=1009 PASS
domain 3x2 boundary=reflected c=inhomogeneous ell=3: fillings=17x17 states=3238 groups=2752 max_clusters=3 swaps=4522 PASS
domain totals: states=37452 groups=32184 swap images=51660 PASS
peak_RSS_bytes=49987584; elapsed_seconds=2.573
```

Independent count audit: 6^2*9=324 local block pairs; 324*16=5184 masks; 2*5184=10368 level checks; 4*1244=4976 rational mass checks. Final domain totals are 33873+341+3238=37452 states, 29290+142+2752=32184 conditioning fibers, and 46129+1009+4522=51660 swap images. The proof of the conditional sign law gives exactly 2^K equally weighted states in each fiber; the script checks every sign vector and its normalised rational probability separately.

Boundary and scope audit: components meeting the fixed collar are never swapped. The graph is determined by absolute difference and bridge bits, so component labels survive every swap. Distinct boundary heights do not spoil invariance because the map preserves each boundary separately. The two replicas must have the same vertex-weight assignment. The construction is for one fixed level; it does not replace the all-level folding argument without additional work. For c_v<1 the stated bridge probability would be negative, so that range is excluded. No finite test failed. No error in Pei's stated finite augmented swap was found; the counterexample concerns only the unaugmented NN swap.

The new result is a finite binary-bridge formulation, a complete check of one dependency of the November uniqueness claim, and its inhomogeneous/weight-one extension. It does not certify Corollary 1.3. In particular, the infinite-volume reconstruction, equilibrium-to-Gibbs lift and roughness arguments remain separate dependencies. The preceding torus equilibrium theorem continues to hold, while its uniqueness premise remains conditional.

## Final audit and deliverables

Saved REPORT.md with the required first-line PROVED verdict, limited to the finite binary-bridge theorem. A small read-only standard-library check, run with the same OMP/thread/nice environment, asserted the required files, exact numerical cross-references, explicit lack of a full uniqueness audit, the c<1 exclusion, and the direct treatment of the nonnormalisable q=1 geometric endpoint. Output: `PASS: deliverables, verdict, numerical cross-references and finite-volume scope`; effective nice 20. There is no SOLVED_ELSEWHERE.md. The deliverables are REPORT.md, PROOF.md, LOG.md and check_binary_swaps.py. All are inside this folder; earlier folders were read only.

The final proof was reviewed against unequal boundaries, arbitrary integer levels, zero-probability open bridges at weight one, and simultaneous changes at all diagonals meeting a swapped set. The local cancellation is pointwise and does not rely on translation invariance or an aspect ratio. The sign law is conditional; no assertion of unconditional independent signs is made. The next checkable target is Pei's fold reconstruction, Lemma 4.4, and its entropy bound, Lemma 4.5, with the all-level residual coupling retained.
