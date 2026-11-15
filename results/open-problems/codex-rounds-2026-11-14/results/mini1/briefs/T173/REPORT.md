VERDICT: PROVED a second-order light-traffic stability-threshold expansion and a certified four-user instability example

The full fixed-N stability region is still unresolved here. This result describes
the boundary near a coordinate axis, where one user has substantial traffic and
the other users have rates proportional to a small parameter.

For four users with transmission probabilities all equal to 1/2, let the first
three arrival rates be epsilon. If mu(epsilon) is the mean potential service of
the fourth user when it always attempts according to its usual coin, including
dummy attempts when empty, then

```
mu(epsilon) = 1/2 - 3 epsilon - (21/2) epsilon^2 + remainder,
|remainder| <= 400000 epsilon^3,  0 < epsilon <= 1/128.
```

The original queue process is positive recurrent for lambda_4 < mu(epsilon)
and transient for lambda_4 > mu(epsilon), with positive arrival rates. The
equality case is excluded. PROOF.md also proves the corresponding explicit
second-order formula for arbitrary fixed N and arbitrary transmission
probabilities strictly between zero and one.

The mechanism is a pair correction: two light queues are simultaneously busy
with probability 28 epsilon^2 + O(epsilon^3), whereas multiplying their leading
marginal probabilities gives 16 epsilon^2. Ignoring this dependence predicts a
tagged threshold 1/2 - 3 epsilon - 6 epsilon^2 + O(epsilon^3).

A concrete consequence, with epsilon = 1/1000000, is that

```
p      = (1/2, 1/2, 1/2, 1/2)
lambda = (0.000001, 0.000001, 0.000001, 0.499996999992)
```

is transient. The certified tagged-service interval is

```
[0.4999969999891, 0.4999969999899].
```

Nevertheless this arrival vector is strictly inside the explicitly defined
downward independent-queue region. A rational busy-fraction witness and every
inequality appear in PROOF.md and verification.json. Thus that approximation
cannot be used as a universal inner bound for fixed transmission probabilities.

The literature search stayed below ten minutes and found no verified complete
solution. The opened [Charles Bordenave, David McDonald, Alexandre Proutiere,
Asymptotic stability region of slotted-Aloha, arXiv:0809.5023](https://arxiv.org/abs/0809.5023)
provides large-N asymptotics and certain exact directions; the direction used
here is outside those exact cases. The opened [Yunshan Yang, Lin Dai, Achieving
Stability for Aloha Networks with Multiple Receivers,
arXiv:2406.02186](https://arxiv.org/html/2406.02186v1) studies a different receiver
model. No SOLVED_ELSEWHERE.md was created. Originality of the expansion has not
been established by this short search.

Verification commands, run in this folder:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 verify.py > verification.txt 2>&1
OMP_NUM_THREADS=1 nice -n 15 python3 audit.py > audit.txt 2>&1
```

Both completed successfully. The main calculation enumerates attempt and
arrival masks and solves exact rational stationary coefficient equations on
states of total light backlog at most two. Two different overflow rules agree
through degree two. It checks the half-probability case, a quarter-probability
case, an asymmetric four-user case and the known two-user linear boundary.
The separate audit re-enumerates service probabilities and pair transitions,
checks the Lyapunov bound and rebuilds the rational certificate. Peak measured
RSS was below 16 MB; runtime was below one second per successful run. The
inherited process nice value was 20, despite the wrapper's priority warning.
No simulation is used as evidence of stability.

Initial verification runs failed while trying to set the sandbox's advisory
RSS limit, and then on a missing zero polynomial coefficient in the two-user
sanity case. Both issues are recorded in LOG.md; the successful outputs are
saved there in full. No failed run is treated as validation.

The result does not classify the equality boundary, probabilities at 0 or 1,
or arrival vectors away from the light-traffic wedge. The explicit error
constant is deliberately coarse. A next worker could tighten that bound to
obtain useful numerical intervals at larger light loads, or compute degree
three with the same finite-state method and then prove a fourth-order tail
remainder. Before claiming novelty, search the light-traffic perturbation
literature more thoroughly.

Task: T173, “push this problem forward by one checkable piece” — recorded
14 Nov 2026, 21:20, Asia/Tbilisi.
