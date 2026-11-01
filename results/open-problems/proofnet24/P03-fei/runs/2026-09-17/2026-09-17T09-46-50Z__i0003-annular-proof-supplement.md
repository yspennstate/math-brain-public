Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is an immutable proof supplement to the 09:43:43Z P03/I0003 report, not a new research run or metric update.

# Proof supplement for `P03-I0003-ANNULAR-STREAM-RESISTANCE-236`

Main report:
`proofnet24/P03-fei/runs/2026-09-17/2026-09-17T09-43-43Z__i0003-annular-stream-resistance-run-report.md`

The main report proves the capacity estimate

\[
\operatorname{cap}_{L}(\{0\},\Lambda_R^c)
\le
\left(\sum_{r=1}^{R-1}A_r^{-1}\right)^{-1}
\]

and gives the four-segment strong-connectivity construction once both signs occur arbitrarily far in every positive and negative tail of both line-sign sequences. It explicitly proves that tail property from the simpler envelope condition (7.2). For completeness, this supplement records the missing one-line implication needed for the stronger annular hypothesis (7.1) itself.

## Lemma

If any one of the four one-sided sign tails (`a_y` as `y->+infinity` or `y->-infinity`, or `b_x` as `x->+infinity` or `x->-infinity`) is eventually constant, then

\[
A_r\ge c r^3
\]

for all sufficiently large `r`, with an absolute `c>0`. Consequently

\[
\sum_r A_r^{-1}<\infty.
\]

### Proof

It is enough to treat `a_y` on the positive tail. If `a_y=s in {+1,-1}` for all `y>=Y`, then, because `alpha_0=0` and every increment has absolute value one,

\[
|\alpha_r|\ge r-C
\]

for some fixed `C` and all large `r`. Also `|\beta_x|<=|x|` for every `x`.

Consider the top boundary crossing edges

\[
e_x=\{(x,r),(x,r+1)\},
\qquad |x|\le r/4.
\]

One of the two faces adjacent to `e_x` has lower-left corner `(x,r)`, hence stream

\[
\psi_{x,r}=\frac{\alpha_r-\beta_x}{4}.
\]

For all sufficiently large `r` and `|x|<=r/4`,

\[
|\alpha_r-\beta_x|
\ge |\alpha_r|-|\beta_x|
\ge r-C-r/4
\ge r/2.
\]

Thus

\[
\psi_{x,r}^2\ge \frac{r^2}{64}.
\]

There are at least `r/2` such crossing edges for large `r`, and every one contributes this nonnegative face term to `Xi_r`. Therefore

\[
\Xi_r\ge \frac{r^3}{128}
\]

for all sufficiently large `r`, so

\[
A_r=\frac{8r+4}{2}+16\Xi_r\ge \frac{r^3}{8}.
\]

Hence the tail of `sum A_r^{-1}` is bounded by `8 sum r^{-3}` and converges.

The cases `a_y` as `y->-infinity` use the bottom square boundary. The two `b_x` tails use the right or left square boundary and the symmetric bound `|alpha_y|<=|y|`. ∎

Therefore divergence

\[
\sum_r A_r^{-1}=\infty
\]

forces both signs to occur arbitrarily far in all four one-sided tails. The four-segment construction in the main report then gives strong connectivity, and the capacity-to-infinity criterion applies exactly as stated. This completes the proof of Claim 236 under its strongest annular hypothesis (7.1), with no change to any constant, status label, or metric.

No checker is required; this is a deterministic analytic lemma.

**End of proof supplement.**
