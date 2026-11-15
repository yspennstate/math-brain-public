VERDICT: PROVED a depth-uniform zero-temperature reformulation of the regular hierarchical upper bound

The round 5 cascade-invariance claim survives independent checking.
The bounded literature search found no later solution of the regular
hierarchical equality. The fixed-degree graph problem remains open
in this work.

New beyond round 5: [PROOF.md](PROOF.md) proves that its optimized
finite-hierarchy bound J_d(beta), for integer d>=3, has a
zero-temperature limit. It equals the infimum K_d^infinity over finite
hierarchies of bounded energetic fields x in [-1,1], with local costs

\[
 S(x_1,\ldots,x_d)=\frac{\sum_j|x_j|-|\sum_jx_j|}{2},\qquad
 E(x,y)=\frac{|x|+|y|-|x-y|}{2}.
\]

The functional is d/2-L_y(S)+(d/2)L_y(E), where L_y is the iterated
conditional logarithmic mean defined in PROOF.md, equation (5).
Let K_d^{<beta} restrict its scaled parameters to
0<y_0<...<y_(r-1)<beta. Then

\[
 K_d^{<\beta}-\frac{2d\log2}{\beta}
 \leq\frac{J_d(\beta)}\beta
 \leq K_d^{<\beta}+\frac{(2d+1)\log2}{\beta},
 \qquad
 \lim_{\beta\to\infty}\frac{J_d(\beta)}\beta=K_d^\infty.
\]

The error is uniform over every finite depth, all parameters and all
measurable messages, including deterministic-spin endpoints. Thus
varying or diverging nearly minimizing depths cause no gap in this
temperature passage. The proof uses both trial-conversion directions,
uniform finite-spin sum estimates, and a recursion that does not
increase a uniform additive error. Increasing the parameter cutoff
then exhausts the energetic domain.

Combining this with the earlier graph upper bound gives

\[
 c_d\leq K_d^\infty,\qquad
 \lim_{\beta\to\infty}\frac{J_d(\beta)-p_d(\beta)}\beta
                                  =K_d^\infty-c_d\geq0.
\]

This does not prove that the gap vanishes. It supplies a precise
temperature-free target for the reverse comparison. No new numerical
bound or claim of priority over the zero-temperature RSB literature
is made. Harangi's [RSB bounds on the maximum cut, arXiv:2506.21296v1](https://arxiv.org/html/2506.21296v1)
already develops zero-temperature trial families; the addition here
is the uniform passage for the entire infimum defined by round 5.
In particular the local costs S and E already appear in its Section 4.

Checks: independently counted the two-spin and star configurations to
reproduce both error constants; checked depth one and two, zero and
constant fractional fields, endpoint messages, changing depth and
parameters, and an exactly evaluated nonconstant d=3 test.
The latter equals 3-(5/2)log(2)/log(3) at the stated trial, with its
probabilities independently checked by counting sign configurations.
Details and commands are in [LOG.md](LOG.md).

Commands: read-only pwd, rg --files, ls -la, cat and sed -n; primary
papers opened with the web tool; local files written with apply_patch.
Targeted reads used `nice -n 15 env OMP_NUM_THREADS=1`; priority changes
were denied. No research computation or script was run. No git,
subagents, external writes, or edits to earlier folders.

What failed or remains uncertain: no reverse inequality K_d^infinity<=c_d
was obtained. There is no rate for K_d^{<beta}-K_d^infinity; the
O(1/beta) estimate is only relative to the truncated domain. The
external graph theorem remains an unaudited dependency for the graph
comparison, but not for the analytic limit theorem for J_d. Initial
overbroad read output was truncated and replaced by targeted reads.

Next worker: seek energetic trials with K_d(r,y,x)<=c_d+epsilon,
or a reverse comparison from the invariant-law variational minimum.
All fields in [-1,1], not merely their signs, must be retained unless
a further reduction is proved. The temperature passage for this trial
space is now settled; proving its value equals the graph optimum is not.

Task: “take the NEXT checkable step on this problem, building on that work”
— T122, received 2026-11-15 approximately 11:00 +04 (Asia/Tbilisi).
