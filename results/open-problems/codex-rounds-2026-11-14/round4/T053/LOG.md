# T053 work log

Task: “Diffusion in the random Lorentz gas at fixed density” — 15 November 2026, 04:25 +04:00 (session orientation).

Scope: only this folder is writable for the task. No git or subagents. Shared brain, checklist and mesh mutations are superseded by the explicit folder-only instruction. Read the brain navigation index and compute state without invoking logging commands outside this folder. Compute state: status warn, mode owner_away_open, about 54% memory free. All subsequent shell programs use OMP_NUM_THREADS=1 and nice -n 15; inherited nice 20 produces a harmless setpriority warning. No heavy computation is planned.

## 1. Prior folders and bounded literature update

Read REPORT.md, LOG.md and SOLVED_ELSEWHERE.md in ~/codex_op_1114/briefs/T053. That folder has no PROOF.md and no scripts. Read REPORT.md, PROOF.md, LOG.md and audit_geometry.py in ~/codex_op_1114r3/briefs/T053. Neither earlier folder was edited.

Web search queries: `random Lorentz gas fixed density central limit theorem 2026 Poisson`; `Lorentz gas fixed scatterer density quenched invariance principle 2026`; `"Lorentz gas" "2026" "fixed density" CLT`; `"Poisson" "Lorentz gas" "2026" recurrence stationarity`.

Opened primary pages: Karsten Matthies and Raphael Winter, arXiv:2506.18539, https://arxiv.org/abs/2506.18539 and https://arxiv.org/html/2506.18539v2; Bálint Tóth, arXiv:2501.00519, https://arxiv.org/abs/2501.00519; Yingxin Mu and Artem Sapozhnikov, arXiv:2609.11690, https://arxiv.org/abs/2609.11690 and https://arxiv.org/html/2609.11690v1. Also opened https://www.esi.ac.at/events/t3247/ (13 April 2026 survey abstract). The papers retain the joint-limit or visibility scope already recorded. The survey explicitly says bare diffusive scaling remains open. No fixed-density solution surfaced. The search is bounded evidence, not proof of absence. No SOLVED_ELSEWHERE.md is warranted.

Local read commands used standard-library Python via `OMP_NUM_THREADS=1 nice -n 15 python3 -`; the first discovery commands were pwd, rg, ls and cat. The later commands adopt the requested nice/thread wrapper uniformly.

Literature update ended 2026-11-15T04:27:09.905542+04:00 (within five minutes of orientation).

## 2. Independent recheck of the earlier result

Re-derived the exponential rate directly by Cavalieri slicing of a segment's r-neighborhood: the interior cross-section contributes kappa_(d-1) r^(d-1) L and the two end sections together contribute kappa_d r^d. The leading void exponent is therefore a L, with a=lambda kappa_(d-1) r^(d-1). Independent cells of length L+3r and width 3r give N asymptotic to C R^d/L; their expected successes have logarithm (d-ac) log R - log log R + O(1) when L=c log R. The net upper bound has logarithm (d-bc) log R + (d-1) log log R + O(1), b=lambda kappa_(d-1)(r-eta)^(d-1). These opposite signs give the same threshold c=d/a. Dyadic summability and monotonic interpolation work on both sides. The sphere-shell constant, net approximation error eta/2+L*(eta/(2L))=eta, disjoint sausage margins r/2, and trimming of billiard flights all check out. The earlier claim holds, with its stated restriction to regular trajectories and its component caveat.

The earliest logarithmic witness also checks algebraically: r=exp(-s), T=exp(2s)s^(-3/2) gives old product sqrt(s) and new product 1/sqrt(s), while fixed r cannot satisfy the theorem's limiting regime.

Re-ran the unmodified earlier audit by reading, compiling and executing it in memory (no imports from, writes to, or pycache in the earlier folder). Command: `OMP_NUM_THREADS=1 nice -n 15 python3 -`, with `exec(compile(old.read_text(), str(old), 'exec'), {'__name__':'__main__'})` inside stdout capture. Output:

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
peak resident bytes 15810560
PASS; elapsed 0.005 seconds
```

## 3. Choice of one extension, before proof

Prove invariance of the environment seen from the particle under Q=P(. | 0 in V_infinity) times uniform spherical velocity, exactly the next step named in the round-3 report. Use finite-speed spatial averaging of the infinite Liouville measure, not an assumed ergodic theorem. The necessary preliminary is almost-everywhere existence of the billiard flow even when Poisson balls overlap: expose smooth boundary patches, discard multiple-boundary and grazing hits as null, and bound the integrated collision count by local boundary flux to exclude finite-time accumulation almost everywhere. This is a single stationarity result with its well-posedness justification. Stationary correlation identities can then be stated as direct consequences; no decay estimate or CLT will be claimed. This is new relative to the supplied folders, not asserted new to the billiard literature.

Potential failure cases to audit: origin is fixed whereas the flow theorem initially holds only for Lebesgue-a.e. starting point; conditioning must be on all unbounded components without assuming uniqueness; boundary overlaps create nonsmooth strata; velocity may correlate with the shifted environment; spatial averaging must handle nonlocal observables and must not smuggle in ergodicity. These will be addressed explicitly.

Choice recorded 2026-11-15T04:27:42.092241+04:00.

## 4. Proof written

Created PROOF.md. Deterministic local flux bound: integral over initial positions A and all velocities of N_T is at most T*c_d*H^(d-1)(Gamma intersect (A+B_T)), with c_d=kappa_(d-1)/(d*kappa_d). It counts only finite regular collision histories and hence does not assume away an accumulation. Its finiteness excludes infinitely many collisions by finite time for almost every initial phase point. Singular finite encounters are null by explicit lower-dimensional parameterizations. The full billiard preserves infinite Liouville measure, also after restriction to the union of unbounded vacant components.

The stationarity proof compares a spatial cylinder with its flow image. Both lie between cylinders over cubes of radii R-|t| and R+|t|. Error <= ||f||_infinity [(2(R+|t|))^d-(2(R-|t|))^d], before division by theta*(2R)^d. Stationarity of the Poisson law turns both expected spatial averages into the desired origin expectations. No uniqueness of the infinite component, locality of f, or ergodicity is used. A separate Tonelli calculation transfers the deterministic a.e.-position flow theorem to the origin under Q tensor sigma.

Direct consequences written: stationary finite-dimensional distributions; zero mean displacement and isotropic covariance; exact finite-time velocity-correlation formula. Its infinite-time version is explicitly conditional on absolute correlation integrability, which remains unproved.

Next: independent constant checks and adversarial audit of the change-of-variables argument and boundary shell estimate.

## 5. First adversarial proof audit

Checked the collision-flux argument for circularity: no complete flow is used in (6), only finite regular branches. Reversing a recorded (collision point, incoming velocity, elapsed time) uniquely recovers its finite history, so branch images cannot acquire multiplicity when summed over collision indices. Markov's inequality supplies a second formulation: phase measure of {N_T>=k} <= T*c_d*S(K)/k, tending to zero; finite-time accumulation is in every one of those events.

Checked corners and tangencies: pairwise Poisson sphere tangencies occur with probability zero, and all multiple-boundary points lie in smooth pairwise intersection sets of dimension d-2. A finite singular encounter is parameterized by at most 2d-2 variables, below phase dimension 2d-1. The rational-time argument pulls the direct null set back through finite regular flow branches. No claim that all exceptional trajectories are regular is made.

Checked component restriction: a trajectory touching a unique sphere patch can be detoured within its locally connected vacant side, so it cannot change open vacant components. The proof uses the union of all unbounded components and does not invoke uniqueness. Added an explicit rational-polygon test for measurability of that union.

Created audit_stationarity.py for independent flux, tube Jacobian, spatial-shell, correlation-factor, and earlier scaling checks. It uses bounded standard-library loops and no simulation of diffusion. Numerical identities test constants, not stationarity itself.

## 6. Independent numerical validation

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 audit_stationarity.py`

Output:

```text
nice: setpriority: Operation not permitted
nice 20
c_d: projection vs angular integration d=2..9 max absolute error 4.63e-14
c_2=1/pi; c_3=1/4
tube determinant and reflection flux max absolute error 8.88e-16
shell: powers vs binomial max absolute error 1.78e-15; slab bound PASS
normalized shell / (|t|/R) -> 2d
correlation identity: full square vs triangle vs closed form max relative error 2.5e-07
C=1 gives E|X_t|^2=t^2; per-coordinate factor is 1/d
earlier d/a coefficient: shadow and radius-one rescaling agree d=2..7
peak resident bytes 12795904
PASS; elapsed 0.004 seconds
```

Every load-bearing constant has a second route: hemisphere projection versus angular integration for c_d (including d=2); coordinate determinant versus normal flux for the collision tube; binomial shell volume versus face-strip cover for the spatial averaging error; full time-square integral versus triangular integral and an exponential test kernel's closed form for both factors in the covariance formula; direct transverse shadow versus radius-one rescaling for the earlier geometric coefficient. The finite-grid discrepancy in the square integral is expected quadrature error and is below its stated tolerance. This computation supplies no evidence for actual Lorentz correlation decay.

## 7. Final adversarial audit

Expanded the local Liouville justification to an explicit one-collision fixed-time map (y,w,s) -> (y,R_y w,t-s); its time derivative is -1 and the absolute flux factors agree. Finite collisions can be separated by rational intermediate times. Thus the flow and flux arguments do not rely on an unproved global billiard theorem.

Fixed-origin concern: equation (8) averages the bad-phase indicator over a spatial box, then invokes translation invariance and Tonelli, rather than evaluating an arbitrary spatial null set at the origin. Conditioning contributes precisely 1/theta.

Shell concern: the inverse flow gives the inner inclusion in (9); the forward speed bound alone would give only the outer inclusion. The image and original cylinder differ in a shell with normalized volume [(1+h/R)^d-(1-h/R)^d]. Its leading coefficient is 2d*h/R, with no missing factor of two. Signed observables are covered by the absolute bound on the symmetric difference. There is no requirement that f be local. Expectations, rather than a sample spatial ergodic theorem, suffice.

Exceptional configurations: coincident or pairwise tangent spheres are Poisson-null. Multiple sphere intersections are covered by pairwise strata, so higher-order transversality is unnecessary. Infinite clusters of overlapping obstacles cause no local area problem because the configuration is locally finite. The proof does not continue paths through corners, tangencies, or accumulation points; it proves those cases have zero initial-law measure. It does not claim existence for every direction.

Covariance concern: the velocity law at each fixed time is uniform and independent of the centered environment under the annealed law. This is not a quenched independence statement. Full orthogonal symmetry, including coordinate reflections, removes off-diagonal cross-time terms even in d=2. The C=1 test recovers ballistic second moment t^2 and catches the factor 2 and the per-coordinate factor 1/d. No Birkhoff conclusion, ergodicity, summable correlations, positive diffusivity, CLT, or recurrence is inferred.

No mathematical check failed. The only command warning was nice attempting to raise an already inherited value 20 to 15; actual scheduling stayed at the lower priority 20. No additional simulations or repeated validation are needed.

Audit completed 2026-11-15T04:32:20.904922+04:00.

## 8. Report saved

REPORT.md records VERDICT: PROVED for the invariant-law lemma, with the main diffusion and recurrence problems explicitly remaining open. It distinguishes the almost-everywhere flow statement from existence at every exceptional phase point and the annealed invariant law from a quenched limit. The proposed next step is the stationary collision Palm law and its finite intensity, not an unsupported correlation claim. Files written in this session: LOG.md, PROOF.md, audit_stationarity.py, REPORT.md. No earlier files or shared state were edited.

Final file audit: nonempty deliverables, exact allowed verdict line, explicit open-problem limitations, collision-index and fixed-origin checks present, script AST parses, and no misleading SOLVED_ELSEWHERE.md. PASS at 2026-11-15T04:33:15.014280+04:00. This was a file/consistency audit, not a repeat numerical run.
