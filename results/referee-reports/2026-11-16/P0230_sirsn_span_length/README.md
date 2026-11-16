# P0230: length of the SIRSN span of k points (working record, 16 November 2026)

The problem is Open Problem 35 of D. Aldous, *Scale-invariant random spatial networks*, Electron. J. Probab. 19
(2014), arXiv:1204.0817: place k uniform points in a square of area k and let L_k be the total length of the union
of the network routes between them. Is E L_k / k convergent to the length per unit area of the network?

This folder is the record of one night's work on the question for the planar Poisson-line SIRSN: the attempt with
its running audit log, and three referee reports written by model instances that did not write the attempt. The
outcome is an audited candidate, not a refereed result. A manuscript is being prepared separately and is not
included here.

| file | what it is |
|---|---|
| `01_attempt_and_audit_log.md` | The attempt (agent A): reduction of the upper bound to an exit tail, the addenda after reading Kahn, the summary of six upper-bound passes, the lower-bound section and the prior-art search. |
| `02_referee_D_first_reading.txt` | A logic-level referee (agent D) who did not read Kahn's text: passes the upper bound, raises the doubt about the lower bound that the later sections answer. |
| `03_audit2_referee_B.md` | The second audit (agent B): the upper bound rebuilt, the lower bound by monotone convergence, and Kahn's three results checked against the arXiv text. |
| `04_lower_bound_reading_referee_C.md` | An independent reading of the lower bound with the truncation repair (agent C): passes. |

Agent letters stand for separate model sessions; the same letter means the same session across files.

## What existed before and what is new

The network is W. S. Kendall's Poisson-line construction (*From random lines to metric spaces*, Ann. Probab. 45
(2017), arXiv:1403.1156); the SIRSN axioms and the question are Aldous's. Every analytic input to the upper bound
is due to J. Kahn (*Improper Poisson line process as SIRSN in any dimension*, Ann. Probab. 44 (2016) 2694-2725,
arXiv:1503.03976): the exponential moment of long-distance route length in a ball (Theorem 6.1) and, through its
proof rather than its statement, the tail bound for routes leaving a large ball (the argument of Theorem 5.1). The
monotone-convergence lower bound uses only the SIRSN axioms. Work on the same metric by G. Blanc
(arXiv:2207.03349) and by G. Blanc, N. Curien and J. Kahn (arXiv:2407.07887) was read and contains no statement
on k-point spans.

What the record adds is the assembly: Poissonization at rate 1 + eps, a split of the far region into annuli handled
by Hölder's inequality with Kahn's moment bound, the observation that the summability condition is exactly
gamma > 2, and a lower bound by truncated local lengths that needs no moment of L_N.

## What the referees changed

Agent D asked whether routes from bulk points to points outside the square could spoil the lower bound; agent B's
addendum answers it. Agent A's first lower-bound argument assumed a moment of the span length that is not
available; the truncation at level M removes the need, and agent C checked the repaired chain. The exit tail is
not Kahn's Theorem 5.1 as stated (a mean for a fixed pair) but a lemma proved by the same argument; the write-up
states it as its own lemma.
