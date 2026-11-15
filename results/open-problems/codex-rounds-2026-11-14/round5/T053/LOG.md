# T053 round 5 work log

Task: “Diffusion in the random Lorentz gas at fixed density”.
Session orientation: 2026-11-15T07:46:02.605671+04:00.

## 1. Scope, startup, and literature

All writes are confined to this folder. No git, subagents, external publication, shared-brain/checklist/mesh mutations, or background jobs. The folder-only instruction supersedes earlier shared-state obligations. Read the startup MEMORY.md and compute_state.json. Compute state was warn / owner_away_open (CPU saturation); only tiny single-thread standard-library audits are planned, under OMP_NUM_THREADS=1 and nice -n 15. The nice wrapper warns about inherited priority; verify actual priority in the audit.

Read the earliest REPORT.md, LOG.md and SOLVED_ELSEWHERE.md. That folder has no PROOF.md or scripts. Read the round 3 and round 4 file inventories; their proof and audit files are being read in full in bounded sections.

Literature searches (web tool, within five minutes):
- "random Lorentz gas" "fixed" diffusion 2026
- "Lorentz gas" "Palm" collision Poisson
- "Lorentz gas" "central limit theorem" "2026"
- "Lorentz" "fixed density" "2026" diffusion proof
- "Poisson" "Lorentz gas" "2026" invariance principle
- "random Lorentz gas" recurrence fixed density proof

Opened arXiv abstract pages:
- https://arxiv.org/abs/2506.18539, Karsten Matthies and Raphael Winter. The abstract concerns a joint small-radius/long-time limit; latest listed revision 8 July 2025.
- https://arxiv.org/abs/2501.00519, Bálint Tóth. Almost-sure statements along extractor sequences in a joint limit; latest listed revision 26 February 2025.
- https://arxiv.org/abs/2609.11690, Yingxin Mu and Artem Sapozhnikov. Maximum visibility, not a dynamical CLT.

No fixed-density solution was found in this bounded search. No SOLVED_ELSEWHERE.md is warranted. Search results alone are not cited as papers. The new high-dimensional void-percolation search hit is checked separately before closing this literature step.

## 2. Planned independent audit and extension

First independently re-derive the previous stationarity conclusion with a bounded spatial test function and a boundary-shell estimate, and re-run the previous audit without writing to its folder. Check its local collision-flux/global-existence argument for circularity and overlapping-sphere singularities.

Chosen extension (before doing it): derive the stationary collision Palm law on exposed sphere patches bordering unbounded vacancy. Compute its total rate and the normalized incoming cosine law, without assuming dynamical ergodicity. This directly continues round 4 and supplies the properly conditioned collision ensemble needed for later correlation work. Establishing strict positivity and normalization is part of this one piece; no mixing or CLT will be inferred.

## 3. Literature closed; earlier claims rechecked

The last opened primary page was https://arxiv.org/abs/2611.07196, Patrick Charbonneau and Marcus Michelen, *On the critical value of void percolation in high dimensions*. Its abstract concerns the large-d vacant-percolation threshold, not a billiard diffusion theorem. Literature check finished at 2026-11-15T07:47:00.545542+04:00, within five minutes of orientation.

Read in full all round 3 and round 4 REPORT.md, LOG.md, PROOF.md and audit scripts. Independently checked round 4: for any bounded spatial weight supported in C_R, Liouville change of variables compares the preimage and image cylinders; the signed integral error is bounded by the symmetric-difference shell volume. Forward and inverse speed bounds place this shell in C_(R+|t|) minus C_(R-|t|). Translating and taking Poisson expectation gives theta times the two origin expectations; the normalized shell tends to zero. The argument works for nonlocal bounded observables. No factor 2 is added when bounding the integral over the symmetric difference. The finite-branch collision-history map is injective in (y,w,s), so its flux bound does not presuppose complete trajectories; finite accumulation would make the count integral infinite on positive phase volume. Boundary singularities lie on pairwise codimension-two strata and their direct-flight tubes are phase-null. Translation/Tonelli transfers the result to the origin. The earlier stationarity and almost-everywhere existence claims hold.

Round 3 also checks: cylinder-plus-caps has exponent aL; independent cells count R^d/L while the net count is R^d L^(d-1). The common leading threshold is d/a. No component lower bound follows.

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 -`, reading each earlier script, `exec(compile(old.read_text(), str(old), "exec"), {"__name__":"__main__"})` under stdout capture. No writes or pycache in prior folders. Output:

`~/codex_op_1114r4/briefs/T053/audit_stationarity.py`

```text
nice 20
c_d: projection vs angular integration d=2..9 max absolute error 4.63e-14
c_2=1/pi; c_3=1/4
tube determinant and reflection flux max absolute error 8.88e-16
shell: powers vs binomial max absolute error 1.78e-15; slab bound PASS
normalized shell / (|t|/R) -> 2d
correlation identity: full square vs triangle vs closed form max relative error 2.5e-07
C=1 gives E|X_t|^2=t^2; per-coordinate factor is 1/d
earlier d/a coefficient: shadow and radius-one rescaling agree d=2..7
peak resident bytes 15728640
PASS; elapsed 0.004 seconds
```

`~/codex_op_1114r3/briefs/T053/audit_geometry.py`

```text
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
peak resident bytes 16498688
PASS; elapsed 0.011 seconds
```

## 4. Extension derivation in progress

Define the boundary measure using exposed patches whose local vacant side belongs to an unbounded component. Retain its entire centered configuration as a mark. Its specific area s_infinity is at most lambda*d*kappa_d*r^(d-1)*exp(-lambda*kappa_d*r^d), by the Poisson insertion formula after forgetting the component restriction. Anticipated collision rate is gamma=c_d*s_infinity/theta, where c_d=kappa_(d-1)/(d*kappa_d). The necessary equality will be proved by spatially averaging the exact collision-history change of variables and squeezing between inner/outer cubes, rather than by assuming ergodicity or exchanging an unbounded collision count with a limiting approximation.

## 5. Proof saved

Created PROOF.md. Derived the exact marked-count identity by the inverse collision-history map and inner/outer cube squeeze. The boundary flux exceptional set is removed by positive-length incoming tubes and the volume-null bad set; this avoids assuming regularity at surface-typical points without proof. The expected specific area is expressed by an unconditioned Poisson insertion identity and bounded by the total exposed area. Positivity follows independently from the first-flight sausage void bound, giving gamma >= (1-exp(-1))*a/[1+log(p0/theta)]. Normalizing the count identity gives the incoming cosine law. A direct Palm consequence, proved by covering time 0 by its unique intercollision interval, is mean flight time 1/gamma without ergodicity. No frequency law or mixing is inferred. Next: audit constants by angular/projection calculations and the all-vacancy special case, and challenge the boundary history and stationary point-process steps.

## 6. Independent validation

Created audit_collision.py with bounded standard-library loops. Command:

~~~sh
OMP_NUM_THREADS=1 nice -n 15 python3 audit_collision.py
~~~

Output:

~~~text
nice: setpriority: Operation not permitted
nice 20
single-hemisphere flux d=2..12: projection vs angular max error 4.86e-15
cosine-law E[mu^2]=2/(d+1): impact-ball vs angular max error 1.42e-14
d=2 flux 1/pi; d=3 flux 1/4; whole-sphere absolute flux is twice these
all-vacancy rate: exposed area vs shadow max relative error 4.44e-16
independent first-flight derivative max relative error 5e-08
positive lower-bound substitution and upper/lower consistency PASS
exact rational marked Campbell tests: two periodic laws, 3 windows, 3 marks PASS
nonergodic mixture: rate=1; Palm mean flight=1; product=1
different samplings: volume-weighted event mean=5/4; forward waiting mean=4/5
inner/outer spatial count squeeze: face-slab checks PASS
peak resident bytes 15269888
PASS; elapsed 0.027 seconds
~~~

The hemisphere constant is checked by projection volume and independent angular integration with Gamma sphere areas. The conditional squared normal velocity is checked by uniform impact-ball radius and an angular third/first moment ratio. The exposed-area / vacant-volume rate for all vacancy is checked against the cylinder shadow coefficient, and the exact first-flight survival derivative supplies a separate check. Its 5e-8 relative error is the expected first-order finite-difference error, below the 6e-8 tolerance. The positivity bound is checked by direct substitution into the survival inequality, over four values of p0/theta. Inner/outer cube factors are bounded independently by face slabs.

The exact rational point-process calculation integrates over a uniform time phase for two deterministic periodic gap sequences, using all breakpoints where the window count changes. It checks the marked count formula for three windows and three marks. Their mixture is nonergodic: the volume weights 2/5 and 3/5 become event weights 1/5 and 4/5. Its rate is 1, Palm mean flight is 1, volume-weighted mean of within-component event means is 5/4, and forward residual mean is 4/5. This checks the reciprocal-rate identity under the correct event sampling and explicitly breaks two tempting incorrect substitutes. It is not a Lorentz simulation or evidence for mixing.

## 7. Adversarial proof audit

Checked sphere overlaps, fixed-origin conditioning, all unbounded components versus a presumed unique component, arbitrary nonlocal environment marks, and incoming versus outgoing velocity conventions. The insertion identity is applied under P, never under Q; retaining the full exposed area as an equality for the unbounded boundary would be wrong. The collision surface ensemble has a tangent ball at the origin and is not Q. Integrating the absolute normal velocity over the full sphere would double the rate; only the incoming hemisphere is counted.

Checked surface exceptions: the earlier volume-a.e. theorem alone does not permit evaluation at a surface point. Positive-length regular incoming tubes transfer it to flux-a.e. boundary states. Corrected an intermediate overstatement about reverse states at a fixed elapsed time: only product flux-time nullity is needed and proved by countability of collision times and Tonelli. Expanded the collision-history Jacobian with a rational intermediate time q and direct tube coordinates s-q. This justifies equality in the new collision formula, not merely an upper bound on finite histories.

Checked unbounded counts: all spatial inequalities are nonnegative, bounded mark expectations have finite boundary mass, and no unbounded count is passed through a shell-error limit. The count identity is obtained by an inner/outer squeeze; unbounded marks follow afterward by truncation. The positivity argument is not circular: the count identity and finite area are established first, then a Poisson first-flight bound forces positive rate. Its upper and lower bounds have units of inverse time and scale as lambda*r^(d-1).

Checked Palm inversion: a collision-free stationary subensemble would invalidate 1=gamma*E_Palm(ell); it is excluded by the exponential first-flight bound, stationarity at each integer time, and velocity reversal. Local finiteness gives a unique interval straddling zero. The mark includes the full configuration, so its next gap is a measurable function of that mark; no Markov or independent-flight assumption enters. Finite intensity and the marked time-count identity also justify equating the first-hit derivative and intensity in the all-vacancy check: multiple-hit excess is o(h), as shown in PROOF.md.

No mathematical or numerical check failed. A draft had mixed inline-math escapes from the shell command string; the file was normalized to dollar delimiters and checked for balanced delimiters. One tool orchestration call failed at JavaScript parsing before running; it was corrected without any file changes from the failed call. The nice wrapper warning reflects inherited actual nice value 20. No heavy jobs, outside writes, or repeated simulation were used.

## 8. Report saved

REPORT.md records the exact allowed verdict PROVED for the stationary collision Palm law and its rate/mean-flight consequences. The original fixed-density diffusion and planar recurrence problems are explicitly unresolved. It records the prior recheck, commands, successful audit results, corrections, internal-audit limitation, primary pages actually opened, and the next collision-map/suspension step. Only LOG.md, PROOF.md, audit_collision.py and REPORT.md were created or edited. Report saved at 2026-11-15T07:56:08.801937+04:00.

## 9. Final file audit

Command: OMP_NUM_THREADS=1 nice -n 15 python3 - (standard-library read/AST checks and this local log append). All four deliverables are nonempty; audit script parses; 19 proof equation labels are sequential; display and inline math delimiters balance; the product flux-time qualification, rational-time Jacobian, theta normalization, positive rate bounds, Palm mean-flight identity, and no-priority statement are present. Report has the exact allowed first-line verdict and explicit unresolved main problem and next step. No SOLVED_ELSEWHERE.md exists. PASS at 2026-11-15T07:56:44.329846+04:00. This is a file/consistency audit, not a repeated numerical run.
