# T053 round 6 work log

Task: “Diffusion in the random Lorentz gas at fixed density”.
Session orientation: 15 November 2026, 10:09 +04:00 (06:09 UTC).

## 1. Scope and startup

All writes stay in this folder. The task's explicit folder-only rule supersedes the earlier requests to mutate the shared brain, checklist and mesh. Read the startup memory index, mesh protocol and compute state without running their writing commands. Compute status: warn, mode owner_away_open, CPU saturated, about 70% memory free. Only small one-thread standard-library checks will run, with OMP_NUM_THREADS=1 and nice -n 15. No subagents, git, publication, external writes or background jobs.

## 2. Bounded literature check

Web searches:
- "random Lorentz gas" "fixed" diffusion 2026 central limit theorem
- "Lorentz gas" "2506.18539" diffusion
- "Lorentz gas" Poisson recurrence fixed density open problem

Opened primary arXiv abstract pages:
- https://arxiv.org/abs/2506.18539 — Karsten Matthies and Raphael Winter, Improved geometric and recollision estimates for the invariance principle of the random Lorentz gas. Still a joint small-radius/long-time limit; listed revision 8 July 2025.
- https://arxiv.org/abs/2501.00519 — Bálint Tóth, Semi-Quenched Invariance Principle for the Random Lorentz Gas -- Beyond the Boltzmann-Grad Limit. Extractor-sequence joint limit; listed revision 26 February 2025.
- https://arxiv.org/abs/2611.07196 — Patrick Charbonneau and Marcus Michelen, On the critical value of void percolation in high dimensions. Its abstract concerns the percolation threshold, not a dynamical CLT.

No fixed-density solution found. This short check is closed within five minutes of orientation; no SOLVED_ELSEWHERE.md is warranted. These sources are not premises of the mathematical extension.

## 3. Reading and independent audit in progress

Read the earliest REPORT.md and LOG.md and its directory inventory; it has no proof or script. Read round 5 PROOF.md, LOG.md and audit_collision.py. Reading the remaining earlier files in bounded sections to avoid truncated tool output. The round-5 main claims to recheck are gamma=c_d*s_infinity/theta, the full marked Campbell identity, the cosine incoming velocity law, and nu(ell)=1/gamma. A separate analytic reconstruction and rerun of the audit will precede the new proof.

## 4. Earlier computations rerun

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 -`, reading and executing each previous audit via `exec(compile(old.read_text(), str(old), "exec"), {"__name__":"__main__"})` under stdout capture. No imports or writes in earlier folders. All three passed. Actual nice value 20; wrapper warns when attempting to raise priority.

Earlier audit: ~/codex_op_1114r3/briefs/T053/audit_geometry.py
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
peak resident bytes 15286272
PASS; elapsed 0.005 seconds
```

Earlier audit: ~/codex_op_1114r4/briefs/T053/audit_stationarity.py
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
peak resident bytes 16121856
PASS; elapsed 0.004 seconds
```

Earlier audit: ~/codex_op_1114r5/briefs/T053/audit_collision.py
```text
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
peak resident bytes 16859136
PASS; elapsed 0.028 seconds
```
## 5. Independent analytic recheck: earlier result holds

The marked count identity can be reconstructed from the inverse map (boundary hit y, incoming direction v, elapsed time s) -> initial phase point. Insert a rational time between the preceding hit and the recorded hit: the earlier regular branch preserves phase volume, and the final straight tube has determinant (-v dot n). Time reversal gives injectivity. Nonnegative summation covers all finite histories; positive-length incoming tubes transfer the volume-null exceptional set to boundary flux. Averaging initial positions over C_R squeezes the expected marked count between T*|C_(R-T)|*b_g and T*|C_(R+T)|*b_g. Dividing by theta*|C_R| gives the exact rate gamma=c_d*s_infinity/theta. This independently checks that no bounded-observable shell estimate was applied to unbounded counts.

The one-hemisphere flux is kappa_(d-1)/(d*kappa_d) by projection. Inserting a Poisson center under the unconditioned law gives s_infinity <= lambda*d*kappa_d*r^(d-1)*p0; inserting under Q would be invalid. The sausage bound P_mu(no hit before T) <= (p0/theta)*exp(-aT), followed by E N=gamma*T, gives the recorded positive lower bound with T=(1+log(p0/theta))/a. All constants have the correct length/time scaling.

For the reciprocal-rate claim, partition the real time axis into successive complete flight intervals. The unique interval straddling zero gives 1=gamma*integral_0^infinity nu(ell>u)du. A collision-free stationary component is excluded by the first-flight bound and stationarity at every integer time; reverse velocity treats the past. Hence nu(ell)=1/gamma holds without ergodicity. Round-4 existence and stationarity inputs also withstand the local finite-history flux and inner/outer cylinder checks. Round-3 net and disjoint-cell exponents both give d/a; the earliest logarithmic witness agrees on direct substitution.

Read all requested reports, logs, proofs and scripts. The earliest folder has no PROOF.md or scripts. Some large combined tool displays truncated; the mathematical proof/script files and the missing portion of the round-4 log were subsequently read in bounded sections. No earlier mathematical error found.

## 6. Choice of ONE extension, before doing it

Prove the full collision-map/suspension representation suggested by round 5: invariance of the incoming boundary-mark law under the next-collision map, then recovery of stationary time observations by integrating over the variable flight lengths. Use this representation to give an exact velocity-correlation formula, including its convergent positive-Laplace-parameter collision series. These are parts of a single passage between the collision and time descriptions. They retain the full environment and all successive flight times; no Markov-flight or ergodicity assumption is introduced. The representation is new relative to these folders, with no literature-priority claim.

Why this piece: it makes explicit which collision correlations would need control to reach the fixed-density diffusion problem. Event-shift invariance can be proved by a bounded endpoint cancellation, and the suspension by the already justified marked Campbell formula. The main audit hazards are length bias at a typical time, incoming/outgoing velocity indexing, nonergodic mixture weights, and exchanging an infinite signed collision sum. Those will be checked independently in exact finite periodic examples and by a pointwise telescoping bound for the Laplace series.
## 7. Proof saved; validation design

Created PROOF.md. The next-collision map preserves nu because the difference between the sum of g at successor marks and at present marks over (0,T] is at most two endpoint values. The marked Campbell identity then makes the difference of expectations T*gamma*(nu(g composed S)-nu(g)); divide by T and let T grow.

The stationary time law is gamma*nu(dM)*ds on 0<=s<ell(M). Its current-flight mark marginal is gamma*ell(M)*nu(dM), with uniform age conditional on the mark. Partitioning ages by the flight occupied at time t gives the exact correlation overlap series. Integrating those overlaps against exp(-z*t) yields equation (14). Its absolute majorant telescopes pointwise to ell(M)/z, whose expectation is 1/(gamma*z), so no second-moment or signed-series interchange is assumed. The finite-index tail bound is also explicit.

Validation will compare exact rational phase integration of periodic unit-velocity paths against the overlap series, including unequal gaps and nonergodic mixtures. A separate direct Laplace integral will integrate the piecewise-linear periodic correlation over one time period, then sum periods geometrically; it will be compared with the collision series and its rigorous truncation bound. These are checks of the representation, not simulations of random Lorentz diffusion.
## 8. Independent validation passed

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 audit_suspension.py`.

```text
nice: setpriority: Operation not permitted
nice 20
exact time-phase correlation vs collision overlaps: 24 cases PASS
event-shift, roof normalization, age moments, residual waiting law: PASS
mixture volume weights=(Fraction(2, 5), Fraction(3, 5)), intensity=1, event weights=(Fraction(1, 5), Fraction(4, 5))
mixture volume weights=(Fraction(1, 2), Fraction(1, 2)), intensity=11/12, event weights=(Fraction(3, 11), Fraction(8, 11))
exact nonergodic mixture correlations: 16 cases PASS
negative control, using volume weights at events: discrepancy 23/48 (caught)
finite-window endpoint cancellation: PASS
Laplace series vs direct periodic piecewise-linear integral: max error 1.78e-15
constant-velocity Laplace 1/z: max error 1.78e-15; largest tail bound 2.68e-19
negative control, including first roof in intervening exponent: caught
peak resident bytes 15286272
PASS; elapsed 0.035 seconds
```

The correlation checks use exact fractions; the Laplace checks compare a direct piecewise-linear time integral with the collision-index series. The two mixture rates follow independently from event counts divided by periods: 2/4 and 4/3. For volume weights (1/2,1/2), their mean intensity is 11/12, giving event component weights (3/11,8/11); (2/5,3/5) gives intensity 1 and event weights (1/5,4/5). The constant-velocity case independently enforces the 1/z normalization. The negative controls deliberately use incorrect sampling or indexing and are rejected; no intended identity failed.

Removed one accidental zero-width BOM from a display delimiter in PROOF.md before this audit. The nice wrapper warning is inherited priority 20, verified in the script. No high-priority or heavy process was run.
## 9. Adversarial audit and stronger finite-tail checks

Checked the following potential failures against PROOF.md:

- Incoming/outgoing indexing: a mark stores incoming v; its first flight velocity is R_n v; the next mark stores that first-flight velocity as its incoming coordinate. Formula (5) reflects exactly once before advancing.
- Full environment: the successor, preceding state and every roof are measurable functions of the full mark. Removing the configuration or replacing the sequence by independent directions would not justify the identities.
- Surface-null exceptions: goodness of every actual collision mark transfers to nu through the earlier marked count identity. It is not inferred by evaluating a volume-almost-everywhere assertion directly on a boundary.
- Nonergodic law: the endpoint cancellation is bounded pathwise, independently of the number of collisions; dividing its expectation by T needs neither ergodicity nor a sample collision frequency. Both nonergodic audit mixtures agree exactly with time-phase sampling.
- Suspension bias: nu itself describes an event; the current-flight mark at time zero is gamma*ell*nu. The inverse map follows the interior state backwards to its latest contact and reflects its outgoing velocity to recover the incoming mark, so it is unique modulo boundary null sets.
- Overlap indexing: L_0=0, L_n sums ell_0 through ell_(n-1); overlap intervals are [L_n-t,L_(n+1)-t). At n=0 this gives (ell_0-t)_+ and C(0)=gamma*nu(ell)=1.
- Signed series: the age-overlap weights sum to ell_0 pointwise. The Laplace weights telescope to b_0; together with the diagonal majorant they sum to ell_0/z. Every exchange is controlled by the finite first roof moment, without an unproved second moment.
- Intervening roofs: the n=1 Laplace coefficient has no exponential intervening factor. Including ell_0 there is a detected error. The tail after N uses ell_1 through ell_N, as checked at finite N.
- Positive z only: the bound 1/z deteriorates at zero. Nothing licenses an interchange of the zero-parameter limit with the collision series, absolute time integrability, positive diffusivity, CLT or recurrence.

Strengthened audit_suspension.py to check the direct periodic correlation is linear between its physical time breakpoints at three exact rational interior samples, and to test the finite-index tail inequality at N=1,2,7. This addresses unresolved concerns about the independent integral and tail, and justifies one further run after the changes.

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 audit_suspension.py`.

```text
nice: setpriority: Operation not permitted
nice 20
exact time-phase correlation vs collision overlaps: 24 cases PASS
event-shift, roof normalization, age moments, residual waiting law: PASS
mixture volume weights=(Fraction(2, 5), Fraction(3, 5)), intensity=1, event weights=(Fraction(1, 5), Fraction(4, 5))
mixture volume weights=(Fraction(1, 2), Fraction(1, 2)), intensity=11/12, event weights=(Fraction(3, 11), Fraction(8, 11))
exact nonergodic mixture correlations: 16 cases PASS
negative control, using volume weights at events: discrepancy 23/48 (caught)
finite-window endpoint cancellation: PASS
finite-index Laplace tail bounds at N=1,2,7: 27 checks PASS
Laplace series vs direct periodic piecewise-linear integral: max error 1.78e-15
constant-velocity Laplace 1/z: max error 1.78e-15; largest tail bound 2.68e-19
negative control, including first roof in intervening exponent: caught
peak resident bytes 15990784
PASS; elapsed 0.056 seconds
```

No mathematical check failed. The deliberate negative controls fail as intended. The only file correction was removal of the accidental BOM; the scheduling wrapper warning reflects actual nice 20. The proof remains internally audited rather than externally reviewed.

## 10. Report and final file audit

REPORT.md saved with the exact allowed PROVED verdict for the collision-map/suspension representation, while leaving the fixed-density CLT and planar recurrence unresolved. It records all commands, validation, corrections, limitations and next steps. Only LOG.md, PROOF.md, audit_suspension.py and REPORT.md were created or edited. No previous folder or shared state was edited.

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 -`, checking nonempty deliverables, AST parsing the audit script, balancing display/inline math delimiters, checking equation labels 1 through 16, and checking report scope and absence of SOLVED_ELSEWHERE.md. Output: file/consistency audit PASS at 2026-11-15T10:17:54.848980+04:00. This was not a repeated numerical run.
