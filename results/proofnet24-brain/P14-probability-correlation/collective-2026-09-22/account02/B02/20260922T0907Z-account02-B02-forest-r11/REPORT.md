# FOREST B02 — cubic-vertex q-Rayleigh deformation

Run: `20260922T0907Z-account02-B02-forest-r11`  
Account/slot: `account02/B02`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Role: FOREST — derive source-valid polynomial/probabilistic comparisons and justify exact-source log-concavity/Rayleigh inputs  
Outcome: **ESSENTIAL_STEP_APPLIED**  
Parent target: OPEN as a public theorem; the campaign's pre-existing internal `FULL_PROOF_CANDIDATE` is preserved but not promoted here  
Context: `WITHOUT_VERIFIED_BRAIN`

## Control and continuity

Fresh control was read from main, including AGENTS.md, scheduled_tasks/README.md with OWNER MESSAGE, fleet.json, roles.json and PROTOCOL.md. The later OWNER CONTROL remains revision `2026-09-22.2`, with the collective-open-problems programme superseding the stale installation text still present in AGENTS.md. No later B02/account02 stop was observed. Protected Git blobs at the last pre-write control read were:

- AGENTS.md `94387098453b9f4a9b10179183f6f6ec780fd987`
- scheduled_tasks/README.md `3d4a9372c87802ab734141a3374d04c8823372e3`
- fleet.json `e647d5d2479749f80ce7bb4862bee0f28513c7d9`
- roles.json `ed17ecc94f76720c0345b3e32249b791b20ec611`
- PROTOCOL.md `83a9268bf5287ca203e4be69a79e25382397bca7`

Whole-file README and isolated OWNER MESSAGE SHA-256 are not reported because this connector surface does not expose an exact byte-preserving hash pipeline; no cached digest is substituted.

The latest complete lead artifact actually consumed is account01/B01 `FOREST-KN-COCKS-RECONCILED-v3`, commit `0509904b9b699563a2b6fe60b6226948886a6b86`. Its conditional end-to-end chain is:

`unit theorem on every K_n -> Cocks fixed-graph positive-weight upgrade for M(K_n) -> Semple--Welsh weighted minor closure -> delete nonedges from K_n -> unit all-forest law on arbitrary finite simple G`.

That handoff records two independent internal end-to-end reviews. I do not convert those internal reviews into a public solved-problem claim.

The named OTHER-account result consumed and extended is account03/B03 run `20260922T055815Z-account03-B03-forest-r12`, report blob `b0640c214b6bb7ae849b3ef46dd6feba888e79c0`. Its exact q=0 cubic-star factorization is

`Delta(e1,e2)=4 B12 T + (B13+C)(B23+C) >= 0`.

## Before / after

**Before this run.** The exact source law was known to be the graphic-matroid independent-set law at unit weights, so complete log-concavity applies, but spectral log-concavity alone does not force the entrywise Rayleigh sign. The partner had an exact unit-forest theorem for two edges incident to a cubic vertex.

**After this run.** The partner's cubic theorem is embedded into an exact one-parameter random-cluster/Tutte deformation from forests to product measure. The pairwise Rayleigh gap factors manifestly nonnegatively for the entire interval `0<=q<=1` at unit third-star activity, and more generally for third-star activity `0<g<=1/(1-q)`. Outer-edge weights and the two marked star weights may be arbitrary positive values. This supplies a source-valid local segment of the broader q<1 negative-correlation problem without assuming the still-open global conjecture.

## 1. Source-valid deformation

For any finite graph/matroid define

`W_q(w) = sum_{S subset E} q^{nu(S)} prod_{e in S} w_e`,

where `nu(S)=|S|-r(S)` is nullity/cyclomatic number. For a graph on n vertices, `r(S)=n-k(S)`, so

`W_q(w) = q^{-n} Z_RC(q, {q w_e})`

for `q>0`, where `Z_RC(Q,v)=sum_S Q^{k(S)} prod_{e in S} v_e` is the random-cluster partition function. Therefore:

- `q=0`: only nullity-zero subsets survive, so `W_0` is exactly the generating polynomial of all forests, including the empty forest, disconnected forests and every size;
- `q=1`: `W_1=prod_e(1+w_e)`, the independent-edge product measure.

This path is not a change of the source problem: the source law is exactly the endpoint `q=0,w_e=1`.

### Why the log-concavity input is legitimate

Branden--Huh, *Hodge-Riemann relations for Potts model partition functions*, arXiv:1811.01696, prove that for `0<q<=1` the homogeneous multivariate Tutte polynomial of every matroid has the one-positive-eigenvalue property on the positive orthant, and hence its logarithm is concave. Their random-cluster specialization is stable under the positive diagonal rescaling `v_e=q w_e`, so it applies to `W_q` for every positive q on this ray.

At `q=0`, Anari--Liu--Oveis Gharan--Vinzant, *Log-Concave Polynomials III: Mason's Ultra-Log-Concavity Conjecture for Independent Sets of Matroids*, arXiv:1811.01600, prove complete log-concavity of the homogenization of the independent-set generating polynomial of every matroid. Graphic-matroid independent sets are exactly acyclic edge subsets, so specializing the homogenizing variable to one gives the actual all-unrooted-forest polynomial.

This is only a spectral/log-concavity input. It is not silently upgraded to entrywise negative correlation. Tang--Zhang, *Negative correlation for the random-cluster model below one on high-degree regular graphs*, arXiv:2609.11578 (2026-09-10), explicitly state that for `0<Q<1` even pairwise negative correlation is still open on arbitrary finite graphs. The theorem below is therefore proved directly by terminal partition algebra.

## 2. Exact cubic-terminal polynomial

Let v be a cubic vertex with distinct neighbours `u1,u2,u3`, star edges `e1,e2,e3`, and `H=G-v`. Give every edge of H an arbitrary positive weight. For a subset `S subset E(H)`, partition the three terminals according to their connected components in `(V(H),S)`. Let

- `A`: q-weighted mass of partition `1|2|3`;
- `B12`: mass of `12|3`;
- `B13`: mass of `13|2`;
- `B23`: mass of `23|1`;
- `C`: mass of `123`.

These are all nonnegative and already include the factor `q^{nu(S)}` and the outer-edge weights.

For one terminal block `B`, adding a nonempty set `J` of star edges into that same H-component adds the first edge without increasing nullity and each further edge with one extra unit of nullity. Hence the exact block factor is

`Psi_B(x) = 1 + sum_{nonempty J subset B} q^(|J|-1) prod_{j in J} x_j`.

Thus

`Psi_i=1+x_i`,

`Psi_ij=1+x_i+x_j+q x_i x_j`,

`Psi_123=1+x+y+z+q(xy+xz+yz)+q^2 xyz`,

and the full local polynomial is exactly

`Phi_q(x,y,z)`
` = A Psi_1 Psi_2 Psi_3`
` + B12 Psi_12 Psi_3`
` + B13 Psi_13 Psi_2`
` + B23 Psi_23 Psi_1`
` + C Psi_123`.

No rooting, fixed-size conditioning or connectedness conditioning has been introduced.

## 3. New Rayleigh factorization

Mark `e1,e2`. Since `Phi_q` is multiaffine in x,y, the Rayleigh difference

`Delta_q = (partial_x Phi_q)(partial_y Phi_q) - Phi_q partial_xy Phi_q`

is independent of the positive marked activities x,y. Give the third star edge activity `g>0`. Direct expansion and collection gives

`Delta_q(e1,e2) = (1-q) R_{q,g}`,

where

`R_{q,g}`
` = (g+1)^2 B12(A+B12+B13+B23)`
` + (g+1)(qg+2) B12 C`
` + (g+1)(1-(1-q)g) A C`
` + (1-q)g^2 B13 B23`
` + (1+qg) C(B13+B23+C)`.

Every coefficient is nonnegative whenever `0<=q<1` and

`0 < g <= 1/(1-q)`.

Therefore

**Cubic q-Rayleigh theorem.** For every finite graph with a cubic vertex v, arbitrary positive weights on edges outside the three-edge star, arbitrary positive activities on the two marked incident star edges, cluster/nullity parameter `0<=q<1`, and third-star activity `0<g<=1/(1-q)`, the two marked incident edges have nonpositive covariance under the law proportional to `q^{nu(S)} prod_{e in S} w_e`. At `q=1` the measure is product and the covariance is zero for every positive g.

Indeed, for a multiaffine partition polynomial P,

`Cov(1_e,1_f) = - w_e w_f Delta_{ef}/P^2`,

so `Delta>=0` is exactly pairwise negative correlation.

At the source point `q=0,g=1`, the formula becomes

`R_{0,1}=4 B12(A+B12+B13+B23+C)+(B13+C)(B23+C)`,

which is exactly the account03/B03 cubic-vertex theorem. Thus the peer result is not merely cited; it is recovered as the endpoint of the new deformation.

For unit third-star activity at general q, one may equivalently write

`R_{q,1}`
` = 4 B12 T + 2q C(A+B12)`
` + (1-q) B13 B23`
` + (1+q) C(B13+B23+C)`,

which is manifestly nonnegative for the entire `0<=q<=1` interpolation.

## 4. Exact regression

A standard-library exact-arithmetic checker was executed locally before archival. It enumerates every one of the 64 simple H on four labelled vertices, attaches the cubic vertex, assigns deterministic positive integer outer weights and marked star weights 2 and 3, and compares the direct subset-enumeration derivative Rayleigh gap with the closed factorization for rational

`q in {0,1/5,1/2,3/4,1}`

and threshold/boundary g values. It also separately checks the q=0,g=1 reduction to the partner formula.

Result:

- 64 graphs;
- 640 exact rational cases;
- 384 strictly positive cases;
- 128 q=1 zero-gap product cases;
- 64 explicit partner-reduction checks;
- 0 failures;
- final line `STATUS=ALL_EXACT_CHECKS_PASS`.

Checker native SHA-256: `d2cea4d268eaad67a4e1da20810fdaecb443b9c3f8f0b53288c31aeaad5a61ed`; Git blob `4fdf2d5d1cf930675a9c0cb2b8b43dbffd55390a`.

Output native SHA-256: `b36ba11b01f0220d3d76c8f934337e34ff7355b9bf3f9f7eaaf1d4eb73f68405`; Git blob `0fa17d991be9a6d81d535fb4c8da72812ad8c449`.

The finite computation is a regression for the symbolic identity, not the proof of the theorem.

## 5. Conditional end-to-end argument and first remaining implication

The shortest campaign-level conditional proof remains the lead chain:

`all complete graphs at unit weights`
` -> fixed-graph positive-weight independence correlation (Cocks)`
` -> weighted minor closure (Semple--Welsh)`
` -> arbitrary finite simple G by deletion`
` -> unit all-unrooted-forest law`.

The current lead handoff says that chain has already passed the campaign's two internal reviews; this run neither weakens nor independently republishes that conclusion.

For the independent log-concavity/q-deformation route, the first essential missing implication is now sharp: **propagate a local nonnegative terminal factorization such as the cubic theorem to an arbitrary marked pair without assuming the general q<1 Rayleigh conjecture.** The Branden--Huh/ALOV spectral theorem supplies log-concavity on the exact deformation, but Tang--Zhang's current-status statement rules out treating spectral concavity itself as that propagation theorem. A promising concrete subproblem is to combine the team's 3-connectivity/minimal-counterexample reduction with this local formula and show that a putative bad pair must avoid every reducible cubic/separator neighbourhood; failure would yield a source-valid obstruction rather than a renamed spectral condition.

## 6. Inventory / operational record

The current account's exposed managed inventory was inspected once. All twenty B01--B20 managed registrations were enabled, hourly-valid, unique and role-aligned; B20 was enabled; quiet delivery was preserved. No deficit or role drift requiring a B20 repair handoff was observed. B02 performed zero scheduler mutations and created no task.

Actual-hour login and a unique start record were created before substantive work. The scoped privacy review found no credentials, scheduler identifiers, machine paths, raw transcripts, benchmark gold or unrelated private data in the artifacts. No email, Drive, public posting, paid model/API/Codex execution, remote workflow or permission change was used.

Model self-report: `GPT-5.6 Sol`. Requested effort: maximum actually supported by the current interface. Configured/known reasoning effort: `UNKNOWN_NOT_EXPOSED`. Exposed provider reasoning/token usage: `null / NOT_EXPOSED`. Context: `WITHOUT_VERIFIED_BRAIN`.

Measured wall execution at report serialization: approximately 1142 seconds, including tool/network/runtime time and not pure thinking. The matching finish record carries the later final wall interval.
