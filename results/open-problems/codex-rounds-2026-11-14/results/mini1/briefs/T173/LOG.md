# T173 work log

Task: “push this problem forward by one checkable piece.”
Started: 2026-11-14T21:20:47.957112+04:00

## Orientation and constraints

Read the workspace inventory, startup memory index and compute governor state. The folder initially held PROMPT.md, codex.log and run.pid. No git used and no subagents started. The current task prohibits writes outside this folder, so shared brain, mesh and checklist mutations are omitted. Scripts are launched with OMP_NUM_THREADS=1 and nice -n 15. The sandbox reports `nice: setpriority: Operation not permitted`; priority will be checked before substantive computation. Only tiny single-thread computations are planned.

## Literature search, first pass

Web queries: `"slotted Aloha" "stability region" exact four users 2020 2025`; `"slotted Aloha" "stability" "Szpankowski" arbitrary number users`; subsequent searches with 2025, 2026, exact four users, and Foster/Kompalli.
Opened https://arxiv.org/abs/0809.5023 (Charles Bordenave, David McDonald, Alexandre Proutiere, Asymptotic stability region of slotted-Aloha) and https://arxiv.org/html/2406.02186v1 (Yunshan Yang, Lin Dai, Achieving Stability for Aloha Networks with Multiple Receivers). The latter is a multiple-receiver/capture model, outside this problem. No complete solution found in the first pass. Search timestamps on old documents were not treated as publication dates.

## Chosen piece (before derivation)

Prove an explicit second-order light-traffic expansion for the stability threshold of one tagged user, with the other N-1 users having arrival rates epsilon times fixed positive constants. Work with a permanently transmitting-dummy tagged user to obtain an autonomous light-user environment. Prove a uniform O(epsilon^3) remainder, and connect its mean service to stability/instability on either side of the threshold. Specialize to four users with all transmission probabilities 1/2 and quantify the first error in the mean-field boundary.

Why: the original obstacle is an unknown stationary empty/nonempty probability. In this wedge, only states with at most two light packets contribute through second order, so a finite balance calculation can eliminate that obstacle without assuming independent queues. This is a local boundary result, not a solution of the whole region. Novelty is not claimed until the original paper has been checked.

## Literature check concluded; execution priority checked

Opened the original arXiv PDF https://arxiv.org/pdf/0809.5023 and searched it for light-traffic/second-order material. Its Proposition 1 treats special directions where approximation and truth coincide; the chosen one-heavy/three-light direction is being checked against those hypotheses. The search did not identify a complete solution or this coefficient. No SOLVED_ELSEWHERE.md is warranted. The literature check was under ten minutes and is now concluded.

Command: `OMP_NUM_THREADS=1 nice -n 15 python3` with `os.getpriority(os.PRIO_PROCESS,0)`. Output: `priority 20`. The wrapper warning comes from an inherited nice value of 20, which is already lower priority than requested. No expensive computation is needed.

First symbolic target (to be audited independently): for p_1=p_2=p_3=p_4=1/2, lambda_1=lambda_2=lambda_3=epsilon, a saturated fourth user has mean potential service
`mu_4(epsilon) = 1/2 - 3 epsilon - (21/2) epsilon^2 + O(epsilon^3)`.
The independent-queue approximation instead gives coefficient -6. The proposed proof will derive tail bounds before discarding higher-occupancy states.

## Derivation checkpoint

For the three-light-user environment, total light backlog W has departure probability at least delta=3/16 whenever W>0. Setting R=1/(32 epsilon), for 0<epsilon<=1/128, yields E[R^W]<=4 and hence P(W>=k)<=4(32 epsilon)^k. This will justify all discarded terms.

Pair-state flux gives P(Q_i>0,Q_j>0)=28 epsilon^2+O(epsilon^3), rather than the independence coefficient 16. Exact rate balance then gives the proposed -21/2 threshold coefficient. A coarse explicit remainder bound of 400000 epsilon^3 is being audited.

A reference trail also identified Lin Dai's 2022 framework paper; attempts to open its CityU PDF returned 403/inaccessible. It is not used as a verified theorem or as evidence that the finite fixed-probability problem is solved. The original Bordenave–McDonald–Proutiere Proposition 1 does not cover the chosen one-heavy/three-light direction: its multiple equal-rate users must be the heaviest after the indicated normalization. The comparison below will explicitly define the independent-queue approximation; it will not invoke a large-N theorem at these fixed parameters.

## Independent verification script, first run

Created verify.py. It enumerates all attempt and arrival masks on states with at most two light packets and solves stationary power-series coefficients using exact rational Gaussian elimination. Two different overflow closures (reset and hold) must agree. This check is independent of the pair-flux derivation.

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 verify.py > verification.txt 2>&1`
First output: `ValueError: current limit exceeds maximum limit` when setting RLIMIT_RSS. The inherited hard limit was lower than the requested advisory limit. Corrected the script to preserve that hard limit and take the minimum, before rerunning. No mathematical calculation had run yet.

The second RSS-setting attempt failed too. A direct read returned RSS and AS limits `(9223372036854775807, 9223372036854775807)` and nice 20. The sandbox rejects changing advisory RLIMIT_RSS, so the script now reports measured peak RSS and uses only tiny exact matrices; it retains a 60-second CPU limit. The first diagnosis of a lower inherited hard RSS limit was incorrect.

## Exact coefficient check, partial output and script correction

The four-user checks already matched: half probabilities gave `(1/2,-3,-21/2)` and pair coefficient 28; quarter probabilities gave `(1/4,-1,-29/18)` and pair coefficient 928/27; asymmetric probabilities gave `(2/7,-12/5,-6968/875)`. The two-user sanity case then exposed a script indexing error: degree-two transition matrices were absent when there was only one light queue. Added an identically zero degree-two matrix in that case. No result was inferred from the failed run.

## Exact verification passed

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 verify.py > verification.txt 2>&1`
Exit code: 0. Exact stdout/stderr:

```text
nice: setpriority: Operation not permitted
four_half mu coefficients: 1/2, -3, -21/2
  pair 1,2 quadratic coefficient: 28
  pair 1,3 quadratic coefficient: 28
  pair 2,3 quadratic coefficient: 28
four_quarter mu coefficients: 1/4, -1, -29/18
  pair 1,2 quadratic coefficient: 928/27
  pair 1,3 quadratic coefficient: 928/27
  pair 2,3 quadratic coefficient: 928/27
four_asymmetric mu coefficients: 2/7, -12/5, -6968/875
  pair 1,2 quadratic coefficient: 201/5
  pair 1,3 quadratic coefficient: 11088/125
  pair 2,3 quadratic coefficient: 756/5
two_user_sanity mu coefficients: 1/3, -1, 0
moment bound: 431244/120617 < 4
pair busy remainder constant: 803156
service remainder constant: 635135/2 < 400000
epsilon: 1/1000000
tagged arrival: 62499624999/125000000000 = 0.499996999992000
certified service interval: 4999969999891/10000000000000 4999969999899/10000000000000
unstable margin: 21/10000000000000
independent boundary light slack: 999935999946000486000729/2000000000000000000000000000000000000
independent boundary tagged slack: 1000100000134999513999271/2000000000000000000000000000000000000
ALL EXACT CHECKS PASSED
elapsed seconds: 0.112
peak RSS bytes (macOS): 15368192
```

Data are in verification.json; all rational numbers are strings, without rounding. Four cases and both finite overflow closures agreed through degree two. Every stationary coefficient equation, including the equation replaced by normalization during solution, was checked. The tail bound, pair-error constant, service-error constant and concrete instability/independence inequalities were checked with rational arithmetic.

## Proof saved

Wrote PROOF.md: general finite-N second-order expansion, stationary exponential-tail argument, positive-recurrence construction below saturated service, positive-drift escape above it, explicit four-user remainder, and a rational unstable vector passing the explicitly defined independent-queue test. The equality case lambda_0=mu is excluded from the claim.

The general gap between the independent closure and true threshold is positive at order epsilon^2 whenever at least two light users have positive rates. The all-quarter case also has a nonzero gap, so this effect is not limited to transmission probabilities summing above one.

## Adversarial audit

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 audit.py > audit.txt 2>&1`
Exit code: 0. Output:

```text
nice: setpriority: Operation not permitted
enumerated light departure probabilities: [Fraction(3, 16), Fraction(1, 4)]
pair-transition polynomials: {'(0, 0, 0)': ['0', '0', '1', '-1'], '(1, 0, 0)': ['0', '3/4', '-5/4', '1/2'], '(0, 1, 0)': ['0', '3/4', '-5/4', '1/2'], '(0, 0, 1)': ['0', '0', '1/4', '-1/4'], '(1, 1, 0)': ['3/4', '-2', '7/4', '-1/2']}
Lyapunov invariant-moment slack: 6403/262144
independent certificate recomputation: passed
ALL AUDIT CHECKS PASSED
peak RSS bytes (macOS): 14925824
```

The separate audit enumerated the light departure probabilities and the exact transitions into a pair state, recomputed the Lyapunov drift slack and explicit error bound, then rebuilt the instability certificate from its busy fractions and checked the decimal endpoints.

Potential failure cases checked in the written argument:
- simultaneous arrivals are included; they supply the empty-to-pair term and cannot be omitted;
- the tagged attempt both blocks the light environment and supplies tagged service, so its service sequence is not assumed independent of the environment;
- light queues holding two packets are included in the finite coefficient calculation and their possible contribution to pair transitions is bounded;
- a common stationary comparison vector is constructed before concluding positive recurrence from tightness;
- instability is proved by positive-probability escape while the tagged queue stays positive, rather than by applying a negative-stability theorem to an unrelated dominant system;
- the exact equality boundary is not covered; endpoints p_i=0 or 1 and changing p_i with epsilon are not covered;
- the two-user limit has zero quadratic term and agrees with its linear exact boundary;
- the original paper's special exact directions do not include three light users and one heavier user.

No contradiction was found. The literature search did not establish originality of this light-traffic coefficient; the claim is a proved local result, not priority or a complete solution.

## Report saved

Wrote REPORT.md with verdict PROVED for the local expansion and explicit instability example, not for the full problem. It lists the commands, exact output locations, literature limits, corrected script failures, assumptions and a next step. Successful computation stayed below 16 MB RSS and one second per run, at inherited nice 20. No files outside this folder were edited.
