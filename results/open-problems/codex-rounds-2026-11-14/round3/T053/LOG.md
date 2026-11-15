# T053 work log

Task: “Diffusion in the random Lorentz gas at fixed density”. Session receipt/orientation: 2026-11-15T01:01:44.287305+04:00 (local +04:00).

All writes remain in this folder. The explicit folder-only task rule supersedes shared brain/checklist/mesh writes. No git, subagents, network shell commands, or heavy computation. Read the compute state: status warn, mode owner_away_open; inherited nice priority is 20. Every shell program is invoked through `OMP_NUM_THREADS=1 nice -n 15 python3`; the wrapper warns that increasing the inherited priority is forbidden, but actual priority 20 is lower than 15.

## 1. Earlier work read and bounded literature check

Read every substantive earlier file: REPORT.md, LOG.md, SOLVED_ELSEWHERE.md in ~/codex_op_1114/briefs/T053. PROOF.md is absent, and no scripts exist there. The earlier worker supplied a literature verification and a scale calculation, not a fixed-density lemma. Read the brain navigation index and available startup memory without invoking tools that write outside this folder.

Web queries: `"Lorentz gas" "fixed density" diffusion 2026`; `"Lorentz gas" Matthies Winter 2506.18539 Toth 2026 diffusion`. These returned the same 2025–2026 advances already recorded. Opened the arXiv full texts of 2506.18539v2 and 2501.00519v2 and the original 1812.11325 page. Additional queries: `"Poisson" "Lorentz" "2026" "invariance"`; `"Poisson" "maximal visibility" logarithmic vacant balls`. Exact findings and the chosen extension follow below.

## 2. Independent recheck of earlier main claim

Write r=exp(-s), T=exp(2s)/s^p. The old smallness parameter is s^(2-p), and the improved one is s^(1-p). The old window requires p>2 and the new one p>1; the witness p=3/2 gives sqrt(s) versus 1/sqrt(s). An independent route divides the two products: old/new=|log r|, and solves each cutoff directly: T=o(r^(-2)|log r|^(-2)) versus o(r^(-2)|log r|^(-1)). They agree. For fixed 0<r<1, the improved product is a positive constant times T and diverges. The earlier scale claim holds. The formula uses dimensionless r; r=1 is not a loophole because the theorem explicitly requires r->0.

The opened current arXiv statements agree with the earlier worker's scope: Matthies–Winter retains a joint small-radius/long-time limit; Tóth's almost-sure statement is along extractor sequences with varying environments. No fixed-density theorem was found in the bounded update search. A separate search surfaced a September 2026 maximum-visibility paper, which is being opened before selecting a geometric lemma; it is not a solution of diffusion.

## 3. Choice of one extension (before proving it)

Bounded literature check ended at 2026-11-15T01:03:06.391717+04:00, within five minutes of orientation. Opened Yingxin Mu and Artem Sapozhnikov, *On the maximum visibility in a ball through the vacant set of Poissonian obstacles*, arXiv:2609.11690v1, https://arxiv.org/abs/2609.11690 and https://arxiv.org/html/2609.11690v1. Their Theorem 1.1 includes the fixed-radius maximum-visibility constant d/(lambda*kappa_(d-1)*r^(d-1)); Remark 1.2 supplies polynomial deviation bounds. For bounded radii those bounds already imply almost-sure convergence along dyadic radii, then all radii by monotonicity. Thus neither that constant nor its almost-sure consequence will be represented as a new literature theorem. The paper does not establish Lorentz diffusion. Also opened Tóth's April 2026 ESI survey abstract, https://www.esi.ac.at/events/t3247/, which describes bare diffusive scaling as still beyond reach. No SOLVED_ELSEWHERE.md is warranted for the main problem.

Chosen piece: give a self-contained fixed-radius geometric lemma, with explicit finite-scale upper and lower probability bounds, prove the sharp almost-sure logarithmic maximum vacant segment law, and extract its uniform collision-free-flight consequence for every well-defined unit-speed billiard path. This is one geometric result and its corollary, new relative to the earlier folder but overlapping the cited visibility literature. It is a checkable preliminary lemma at fixed density: it rules out arbitrarily long straight flights from a bounded region, including along paths whose directions depend on the environment. It does not address recollisions.

Notation: obstacle radius r>0 fixed, intensity lambda>0, a=lambda*kappa_(d-1)*r^(d-1), M_R=supremum of lengths of vacant straight segments with both endpoints in B(0,R). Target: M_R/log R -> d/a almost surely. Upper method: finite nets in initial point and direction, with an explicitly reduced obstacle radius. Lower method: independent empty sausages in disjoint rectangular cells. The lower law is for the entire vacant set, not the origin's unbounded component. The upper law alone transfers to any component.

Formulation fixed for future workers: use P_infinity=P_lambda(. | 0 belongs to an unbounded open vacant component), assuming this event has positive probability, and initial velocity uniform on S^(d-1), independent conditional on the environment. Annealed convergence averages these two choices; quenched convergence fixes P_infinity-almost every environment and averages only initial velocity. Uniqueness of the unbounded component is not needed for the geometric lemma.

## 4. Proof saved

Created PROOF.md with the finite-scale net upper bound (explicit sphere-net constant K_d=d*2^d*(5/4)^(d-1)), the independent-cell lower bound, and their almost-sure sharp logarithmic limit. Derived G(T)<=M_T for every regular unit-speed billiard path, hence limsup G(T)/log T <= d/a and liminf N_X(T)*log T/T >= a/d when collisions are locally finite. Conditioning on the origin's unbounded component preserves the probability-one statement. A lower bound on the whole vacant set is explicitly not a lower bound within that component or along a trajectory.

Write command: `OMP_NUM_THREADS=1 nice -n 15 python3 -` using pathlib text writes. Next: independent checks of the geometric constants, finite-scale bounds and possible conditioning/tangency errors.

## 5. Independent audit script: initial execution issue

Created audit_geometry.py using only the standard library. First command `OMP_NUM_THREADS=1 nice -n 15 python3 audit_geometry.py` failed immediately at resource.setrlimit(RLIMIT_AS, (768 MiB,768 MiB)): ValueError, current limit exceeds maximum limit. No numerical work ran. On this macOS host virtual address reservations make this unsuitable; replaced it with a data-size cap bounded by the inherited hard limit and a resident-memory check. This is an execution issue in the audit harness, not a failure of a mathematical bound. The next run and its exact output follow.

The second audit launch also failed before computation: RLIMIT_DATA setrlimit raised the same ValueError. Read-only getrlimit reported both AS and DATA as (9223372036854775807,9223372036854775807). The exact reason setrlimit is unavailable here was not established; the virtual-reservation explanation above was only a hypothesis and is withdrawn. Removed setrlimit calls. The script has fewer than 50,000 scalar integration/verification iterations, bounded small lists, and no large allocations; it checks and reports peak resident memory.

## 6. Successful independent audit

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 audit_geometry.py`

Output:

```text
nice: setpriority: Operation not permitted
priority 20
sausage volumes d=2..8, three radii: max relative discrepancy 7.83e-15
independent sausage cells: all face margins exactly r/2; adjacent supports gap r
sphere-shell bound d=2..8: largest shell / bound 0.800000
d=2 a=0.3220000000 d/a=6.2111801242 (shadow and radius-one scaling agree)
d=3 a=0.3540574921 d/a=8.4732001646 (shadow and radius-one scaling agree)
d=5 a=0.2725145819 d/a=18.3476420409 (shadow and radius-one scaling agree)
logR, log(U)/logR, log(N*p)/logR
   20  1.42206786  0.43779243
   40  0.56864031  0.57677154
   80  0.12459785  0.65477275
  160 -0.10608772  0.69806707
limiting rates -0.35410197 0.75000000
earlier witness s=4 old=2 new=0.5
earlier witness s=16 old=4 new=0.25
earlier witness s=64 old=8 new=0.125
peak resident bytes 14712832
PASS; elapsed 0.006 seconds
```

The numerical checks are supporting audits, not the proof. Sausage volumes were computed by axial cross-section integration with an independent recurrence for unit-ball volumes, versus the cylinder-plus-ball formula with Gamma volumes. The sharp coefficient was also re-derived by rescaling to radius one, and specialized independently to 1/(lambda*r) in d=2 and 3/(lambda*pi*r^2) in d=3. Exact fractions verify every cell margin and independence gap. The logarithmic rate signs agree with the proof. At smaller logR the upper bound U exceeds 1 and is uninformative; formula (2) already takes min(1,U), and the theorem is asymptotic. No claim of useful small-scale constants is made.

## 7. Adversarial proof audit

- Counting endpoints independently in the full ball would produce a false 2d leading constant. The upper proof counts a starting point and direction only, with direction mesh eta/(2L). Its spatial entropy is R^d times a power of L; balancing exp(-aL) gives d/a. The independent-cell lower count R^d/L gives the same leading constant by a separate construction.
- A Poisson void formula cannot be applied directly to a trajectory chosen from the environment. The proof first discretizes all possible segments into deterministic candidates and then uses a union bound. No independence between overlapping candidate tubes is assumed.
- A fixed mesh without reducing the obstacle radius would miss near-tangent segments. Equations (6) and the use of r-eta handle this explicitly; eta is fixed after choosing c>d/a, then sent to zero through a countable sequence of c.
- The independent lower tubes include both spherical caps. Their volume has the end correction lambda*kappa_d*r^d, and the cells have length L+3r, leaving a gap r between neighboring closed sausages. There is no overlap hidden at cell faces.
- Conditioning on H destroys independence of void events. All constructions and probability bounds are proved under the unconditioned Poisson law first. Probability-one statements then transfer by absolute continuity; finite-scale probabilities may be divided by theta=P(H). No conditional independence is used.
- The lower law does not assert existence of long segments in the origin's infinite component. Finite vacant cavities remain possible. Only the uniform upper bound is used for billiard flights.
- Collision endpoints lie on obstacles, whereas M_R uses the open vacant set. Trim both endpoints of each flight, apply M_R, and pass to the supremum. This yields the same full flight length as a supremum without incorrectly placing collision points in V.
- The collision-count corollary assumes a global regular path with finitely many collisions in bounded time. Singular multiple contacts and collision accumulation are not disposed of by this lemma.
- The dyadic Borel--Cantelli argument requires no independence across radii. Monotonic interpolation costs (n+1)/n, which tends to one; interpolating radii themselves would unnecessarily lose a factor two.
- Logarithmic straight-flight control says nothing about cancellation or correlation of velocities, repeated collisions, positive diffusivity, or recurrence. It holds even above the percolation threshold. It cannot by itself resolve T053.

Audit completed at 2026-11-15T01:07:18.571939+04:00.

## 8. Report written

Created REPORT.md with verdict PARTIAL, the precise geometric result, its overlap with Mu–Sapozhnikov, the regular-path assumptions, validation output, failed resource-limit launches, and the unresolved fixed-density CLT/recurrence. The next proposed lemma is invariance of the environment-and-velocity law conditioned on the unbounded vacant component; no ergodicity assumption is to be smuggled into it. All writes were standard-library operations in this folder.

Final file audit first attempt: all files were present and syntax compilation passed, but an assertion searched PROOF.md for the literal phrase `not the origin`. The proof instead states `need not belong to the component containing the origin`; the sentinel was wrong. Corrected the audit to check the actual caveat. This was a text-audit error, not a mathematical change.

## 9. Final file audit passed

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 -` reading all four deliverables, compiling audit_geometry.py in memory, checking the exact report verdict, the novelty and component caveats, and absence of SOLVED_ELSEWHERE.md.

Output: all four files present and nonempty; script syntax valid; priority 20; final file audit PASS at 2026-11-15T01:08:33.772438+04:00. The earlier folder was only read. No git, subagents, outside writes, or external publication.
