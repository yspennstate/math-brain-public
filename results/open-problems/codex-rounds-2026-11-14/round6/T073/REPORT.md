VERDICT: PARTIAL improved high-noise uniqueness by allowing every common-diagonal broadcast pattern

The round 5 result holds. Independently reconstructed its exact local
identity, stationary last-ring argument, four event coefficients, expanded
polynomial, exact root bounds and endpoint value. The check uses no
predecessor imports and is saved in [verify_previous.py](verify_previous.py),
with output in [previous_output.json](previous_output.json).

The new sufficient uniqueness threshold for the continuous-time
four-neighbor process with fairly resampled ties is approximately

\[
e_4=0.24807552621222013612253301,
\]

down from 0.24807560804638594994778149, a decrease of about
8.18341658138252485·10⁻⁸. In particular, every e∈[0.24807553,1/2]
has exactly one stationary probability measure. The low-noise coexistence
problem remains unresolved by this work.

Put a=1/2−e and define

\[
\begin{aligned}
P(e)&=\frac{17}{1260}e^4+\frac7{270}e^5
                  +\frac{767}{45360}e^6+\frac{23}{6160}e^7,\\
R(e)&=\frac{68}{2835}e^5+\frac7{150}e^6
                  +\frac{767}{24948}e^7+\frac{23}{3360}e^8.
\end{aligned}
\]

The criterion is

\[
C_4(e)=4a(1-e^3/2)-\frac4{15}e^5a^3-\frac{16}{81}e^6a^3
                    -2a^4(P(e)+R(e))<1.
\]

Its unique root below 1/4 is e₄. The exact signs bracket it by

\[
\frac{38387828333112147431787763}{154742504910672534362390528}
<e_4<
\frac{9596957083278036857946941}{38685626227668133590597632}.
\]

At e=0.24807553, C₄ is
0.999999984612015744454758680159985502…, while the preceding C₃ is
1.000000317065932486634429222017556278…. Thus the extension is strict.

The new ingredient is a larger family of disjoint forcing events. Hold
a source disagreement at the center and force the four diagonal helpers
to any of their sixteen common-spin assignments. Whenever the two
diagonal inputs of a receiver are equal to b, force its outer axial
input to common 1−b before that receiver's last ring. Its transmission
probability is then a. When the diagonal inputs differ, the previous
uniform a bound still applies for every ordered axial input. Reveal
the selected receiver marks chronologically to handle dependence.

The resulting single-triple bounds are a³P(e)d for at least three
disagreements and a³R(e)d for exactly three, with d the stationary
disagreement density. The previous bounds were their leading terms.
Different diagonal assignments require disjoint intervals at the same
four last-ring marks, which justifies adding them despite the different
extra clock requirements. The full proof is in [PROOF.md](PROOF.md).

Reproduce from this folder:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 -I -B verify_previous.py > previous_output.json
OMP_NUM_THREADS=1 nice -n 15 python3 -I -B audit.py > audit_stdout.json
```

Both commands exited 0 in under one second. The second also saves
[audit_output.json](audit_output.json). Every clock coefficient is checked
by an order-ideal count and an independent integral conditional on receiver
times. The audit reconstructs all 64 rotated forcing patterns and 384
receiver/input cases, explicitly checks the extra free clock and source
counts, and compares two polynomial constructions and two exact root
enclosures. The independent integer polynomial enclosure is
(0.248075526212220136,0.248075526212220137). Peak RAM was about 16.3 MB;
one thread, actual nice 20, 30-second CPU limit. The nice prefix's
`setpriority: Operation not permitted` diagnostic is due to inherited
nice 20; both scripts verify actual nice≥15.

The literature check ended within five minutes and found no later
solution changing the picture. Opened the arXiv pages and full texts of
Jian Ding and Fenglin Huang, *Non-ergodicity for the noisy majority vote
process on trees*, [arXiv:2501.16202](https://arxiv.org/abs/2501.16202),
and Damiano De Gaspari, *Fredrickson–Andersen Model and Noisy Majority
Vote Process on Nonamenable Graphs*,
[arXiv:2508.06935](https://arxiv.org/abs/2508.06935). Their pages still
list the original 2025 versions; their expansion results do not cover
this square-lattice process. Also opened Tânia Tomé, Mário J de Oliveira
and Maria Augusta Santos, *Non-equilibrium Ising model with competing
Glauber dynamics*, [primary PDF](https://fge.if.usp.br/~oliveira/JPA_24_3677_1991.pdf).
Section 6 discusses the fair-tie rule, the elementary uniqueness bound
1/4 and a possible low-noise argument attributed to Gray (1985), without
proving that coexistence statement there. This bounded search cannot
establish absence of a solution or stronger published uniqueness criteria.
No literature priority or optimality is claimed.

What failed or remains uncertain: no computational assertion failed.
The written audit caught and corrected an endpoint explanation: the
blocking estimate does not contain a, so at e=1/2 it is justified by
d=0 from the stationary generator identity. All coefficients and numerical
claims were unaffected. The finite checks do not formally verify the
infinite-volume or conditional-probability proof. No conclusion is obtained
at e=e₄, for retained ties, or for positive-noise coexistence.

Next: apply the same nonalternating-helper construction to the adjacent
and opposite pair events E_A, whose bounds were kept unchanged here.
Add an opposite common axial input at each receiver with equal diagonal
helpers; retain the two equal common omitted neighbors and recount all
clock constraints. This is a concrete continuation with disjoint diagonal
mark events. The suggested axial-disagreement enhancement from round 5
still needs a separate dependence argument. Low-noise coexistence requires
control of large error clusters beyond these local constructions.

Task: “take the NEXT checkable step on this problem, building on that work”
— 2026-11-15, approximately 10:25 +04 (Asia/Tbilisi).
