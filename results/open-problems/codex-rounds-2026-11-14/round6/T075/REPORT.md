VERDICT: PARTIAL proved explicit parameter stability of prefix caps and delayed finite concentration at transcendental parameters; T075 remains open

The round-5 obstruction holds. Its total variation constant was
independently recovered by integrating both signs of the one-step defect.
Its script reproduced all reported checks, including the depth 25,031
certificate and margin 1/9,437,184. The bounded literature check found
no solution of T075. Samuel Kittle and Constantin Kogler's
[arXiv:2611.17277v1](https://arxiv.org/html/2611.17277v1) still assumes
absolute continuity in its higher-integrability theorem.

The new result in PROOF.md is parameter stability. For the previous
uniform-tail prefix law mu_n^lambda and its small-set cap A_n^lambda,
if 0<a<=lambda,eta<=b<1, then

    TV(mu_n^lambda,mu_n^eta),
    |A_n^lambda(delta)-A_n^eta(delta)|
        <= min(1, C_n(a,b)|lambda-eta|),

    C_n(a,b) = (1-a)/[(1-b)^2 a^n].

Every word-interval endpoint has derivative at most (1-b)^-2. Comparing
uniform distributions on the two word intervals proves the bound even
when prefix sums coincide or the endpoint ordering changes.

Consequently, given delta_0/4<theta<1, any initial horizon N, any
later lower bound M>N, any delta_1>0 and epsilon>0, there are a depth
m>=M and an open interval J in (1/2,1) such that every lambda in J has

    A_n^lambda(delta_0)<theta for 0<=n<=N,
    A_m^lambda(delta_1)>1-epsilon.

Thus J contains uncountably many transcendental examples of this finite
behavior. It can also be restricted to avoid any prescribed finite list
of integer-polynomial roots, with a positive rational lower bound for
their absolute values selected by the construction. The preceding
report's singular controls were algebraic. This extends the finite
obstruction to the transcendental class without asserting singularity
there. It rules out a uniform future cap bound across that class from
these finite initial caps and qualitative transcendence alone.

The depth m is existential. The stability radius is explicit once m is
supplied. No single transcendental parameter is shown to concentrate at
arbitrarily small lengths. A finite concentration episode is compatible
with absolute continuity, so this is not a counterexample to T075 or
to an absolute-continuity criterion restricted to transcendental inputs.

Commands, run from this folder:

~~~sh
OMP_NUM_THREADS=1 nice -n 15 python3 ~/codex_op_1114r5/briefs/T075/check_obstruction.py > earlier_recheck.txt 2>&1
OMP_NUM_THREADS=1 nice -n 15 python3 check_stability.py > computation.txt 2>&1
~~~

The successful new run checked 225 uniform-interval pairs, 81
parameter/depth TV comparisons, 4,599 word intervals, 324 cap differences,
360 independent midpoint/dual caps, and 80 polynomial exclusions.
Runtime was 0.908 seconds, peak RSS 19,185,664 bytes, one thread,
actual priority 20. All arithmetic in these checks is rational.
The example at a=3/5, b=601/1000, n=8 gives
C_n=156250000000/1044517761, independently re-derived by integer
arithmetic. LOG.md records commands, output and the failure-case audit.

What failed: the initial run stopped before computation because macOS
rejected an optional address-space limit. The platform condition was
corrected and the run passed. An example denominator was corrected
before rerunning. No infinite-subsequence upper cap estimate for a
fixed transcendental parameter, or quantitative upper bound for the
multinacci concentration time, was obtained.

Uncertainty: no novelty or optimality is claimed for the elementary
stability estimate or its continuity corollaries. No formal proof
verification was run, and the literature check was bounded.

Next worker: make the late depth effective at one multinacci control,
using a quantitative concentration estimate rather than singularity
and weak convergence alone. The stability formula would then give an
explicit parameter interval for a certified delayed concentration
episode. To approach T075 itself, establish arithmetic control at
infinitely many scales for one fixed transcendental parameter; finite
polynomial nonvanishing and finite cap checks do not supply it.

Task: “take the NEXT checkable step on this problem, building on that work.” — 2026-11-15, first exact tool clock 10:29:54 +04:00.
