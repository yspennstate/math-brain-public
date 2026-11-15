# T222 work log

Task received: 2026-11-15 approximately 01:40 Asia/Tbilisi (2026-11-14
21:40 UTC). Request: "take the NEXT checkable step on this problem,
building on that work."

## Orientation and bounded literature check

Read the previous REPORT.md, LOG.md, PROOF.md (all 452 lines, in two
reads), and AUDIT.md in ~/codex_op_1114/briefs/T222.
`rg --files` found no mathematical scripts there; only those documents
and launcher/transcript files. Read the brain navigation and startup index,
the mesh protocol, and the compute state. Task-specific confinement of all
writes to this directory supersedes shared mesh/checklist/brain writes;
none of those stores was mutated. No git or subagents.

Shell reads used `env OMP_NUM_THREADS=1 nice -n 15 /bin/sh -c '...'`.
The sandbox reports `nice: setpriority: Operation not permitted`, then
executes the short read. No successful priority adjustment is claimed.
Governor: `warn`, `owner_away_open`, CPU saturated. No simulation planned.

Web-tool queries, completed within five minutes of starting:

- `"Euclidean traveling salesman" "variance" "2026"`
- `"Steele" "variance" "traveling" convergence`
- `"1706.04290" variance TSP limit`
- `"traveling salesman" "variance convergence" 2026`
- `"Euclidean" "TSP" "variance limit"`

Opened Sourav Chatterjee, *A general method for lower bounds on
fluctuations of random variables*, arXiv:1706.04290v3,
https://arxiv.org/html/1706.04290v3, including its TSP discussion and
Section 3. No closing theorem found. Search hits on first-order constants,
algorithms and unrelated TSP models do not close this question; no claim
of an exhaustive review is made. No SOLVED_ELSEWHERE.md is warranted.

## Independent re-derivation of the earlier result

For S containing n-1 points let d(x,S)=T(S union {x})-T(S).
Shortcutting gives d >= 0; the closed detour through a nearest neighbor
gives d <= 2R. Orthogonal Hoeffding expansion gives exactly

    E_n := sum_j j V[n,j] = n E[Var_X(d(X,S) | S)].

This follows by integrating out each coordinate, squaring its orthogonal
residual, and counting a component supported on A exactly |A| times.
It checks the earlier replacement identity without its factor 1/2.
Choosing zero as a competitor for the conditional mean gives
E_n <= 4n E R^2. The homothetic-square area bound r^2/2 gives
E R^2 <= 2/n, hence E_n <= 8. At almost every fixed x, the scaled
nearest-distance tail tends to exp(-pi t); the uniform bound exp(-t/4)
allows integration over x and t, yielding n E R^2 -> 1/pi.
Thus the earlier bound limsup E_n <= 4/pi holds. Its variance-tail and
covariance consequences follow from nonnegative V[n,j]. No error found.

## Choice recorded before proof

Choose ONE extension: sharpen the explicit asymptotic interaction-energy
constant, and consequently the errors in the earlier reduction.
For c >= 0 center at T(S)+c/sqrt(n), rather than T(S). Convexity of
the squared error and 0 <= d <= 2R imply the finite-n bound

    E_n <= E[max(c^2, (2 sqrt(n) R-c)^2)].

The Rayleigh nearest-distance limit should turn the right side into

    F(c) = c^2 + (4/pi) exp(-pi c^2) - 2c erfc(sqrt(pi)c).

Prove the limit, optimize F, and independently audit all coefficients.
Why this choice: it strengthens an already verified geometric estimate
without asserting localization of optimal tours or an unproved limit of
add-one costs. This is a sharper constant within the previous reduction;
no claim that it improves the best published variance bound is intended.

## Proof saved

Saved PROOF.md with the complete finite-n centered insertion inequality,
the boundary-safe limit passage, and the strict analytic bound

    limsup E_n <= kappa = min_(c>=0) F(c) < 2/pi.

This improves the previous 4/pi in the same interaction-energy estimate.
The unique minimizer satisfies

    c = 2c exp(-pi c^2) + erfc(sqrt(pi)c).

No decimal approximations or numerical run are needed. The strict
comparison uses c=1/sqrt(pi), integration by parts giving
erfc(1)>2/(3e sqrt(pi)), and e>8/3. Both are proved in PROOF.md.
The improved variance-tail and noise-covariance errors are
kappa/(m+1) and kappa(1-rho), respectively.

The proof also identifies the precise limit of this method's information:
among scalar Y with 0<=Y<=2Z and P(Z>z)=exp(-pi z^2), the supremum
of Var(Y) is kappa. It is attained by Y=2Z 1_{Z>c_*}. This is an
envelope test, not a proposed law of TSP insertion costs.

Source follow-up: used the already opened Chatterjee HTML's Section 3,
lines 728-732, to verify the exact conjecture; no further search round.

## Audit plan

Recompute F from truncated exponential moments, rather than the tail
integral in PROOF.md. Recompute the resampling energy with independent
replacement pairs. Test the conditional-centering inequality at n=2 and
at the two possible endpoints of every insertion interval. Check the
possible failure of uniform integrability, boundary control, and the
temptation to infer variance convergence. Record the results in AUDIT.md.

## Resumed read-back, 2026-11-15 03:31–03:33 Asia/Tbilisi

Found the proof and completed analytic audit already saved in this folder,
but no REPORT.md. Preserved those artifacts and checked them against the
original worker's files; the continuation is the same chosen extension,
not a new research direction. Read the original REPORT.md, LOG.md,
PROOF.md and AUDIT.md. A script search found no .py or .sh mathematical
scripts in the original folder (rg exit 1 means no matches).

Read the startup memory ~/.claude/brain_startup.md and
the brain navigation index. The present task forbids writes outside this
folder, so no logging recall command, shared checklist, mesh registration,
or shared memory update was run. Governor: warn, owner_away_open, CPU
saturated. All shell reads used OMP_NUM_THREADS=1 and nice -n 15; the
sandbox continued to print its setpriority denial. There was no numerical
run or heavy computation, and priority was not verified.

A fresh bounded web check used these four queries:

- `"Euclidean traveling salesman" "variance" convergence Steele 2026`
- `"travelling salesman" "variance limit" Steele`
- `"Steele" "variance" "traveling" "2026"`
- `"Euclidean traveling salesman" "Hoeffding" first order variance`

Opened https://arxiv.org/html/1706.04290v3, by Sourav Chatterjee,
and used find for Steele and converges. The exact conjecture is still
printed at Section 3, problem (2), line 732 of the tool's rendering.
No later closing theorem was found. Search hits alone are not cited as
papers read. This check took less than five minutes; no further status
search is planned and no SOLVED_ELSEWHERE.md is justified.

Independent re-derivation of the original energy claim: orthogonality
gives E_n = sum_i E Var(L_n | X_{-i}); the deleted tour is constant
under that conditioning. Hence E_n <= n E d^2 <= 4n E R^2.
The homothetic square has area r^2/2, so E R^2 <= 2/n and E_n<=8.
For fixed interior x the scaled survival function is eventually
(1-pi r^2/n)^(n-1); its limit is exp(-pi r^2). The bound
exp(-r^2/4), uniformly in x, controls the second moments. Integrating
2r exp(-pi r^2) gives 1/pi. Thus the original 4/pi claim holds.

Rechecked the new constant without the main proof's tail integration:
W=pi Z^2 is exponential, with truncated first moment
(a^2+1)exp(-a^2), a=sqrt(pi)c. The truncated square-root moment is
a exp(-a^2)+(sqrt(pi)/2)erfc(a). Substitution into
c^2+4 E[Z(Z-c)1_{Z>c}] recovers F(c) exactly. Differentiating instead
through the two endpoint integrals gives F'=2c-4 E[Z1_{Z>c}]
and F''=2+8pi c^2 exp(-pi c^2)>0. The unique stationary point is
the mean of Y_*=2Z1_{Z>c_*}, proving scalar-envelope sharpness as well
as checking all coefficients. These are exact calculations, not a
numerical evaluation of c_* or kappa.

The strict estimate at c=1/sqrt(pi) was checked from
1/e=2I+J with J<I, hence I>1/(3e). It gives
pi F(c)<1+8/(3e)<2. Endpoint tests, the singleton base, corners,
nonunique tours, uniform integrability, and the fixed choice of c_* all
pass the checks in AUDIT.md. No mathematical error was found. The
oscillating order-one example confirms that the improved energy bound
still does not imply variance convergence.

Representative read commands (all through the environment/nice prefix):

```sh
cat ~/codex_op_1114/briefs/T222/REPORT.md
cat ~/codex_op_1114/briefs/T222/LOG.md
sed -n '1,240p' ~/codex_op_1114/briefs/T222/PROOF.md
sed -n '241,480p' ~/codex_op_1114/briefs/T222/PROOF.md
cat ~/codex_op_1114/briefs/T222/AUDIT.md
rg --files ~/codex_op_1114/briefs/T222 -g '*.py' -g '*.sh'
cat LOG.md PROOF.md AUDIT.md
cat ~/.claude/compute/compute_state.json
```

No earlier-worker file was edited. The only writes are artifacts in this
folder, made with apply_patch. No git, subagents, accounts or messages.

## Final artifact audit, 2026-11-15 03:33:32 Asia/Tbilisi

Ran:

```sh
env OMP_NUM_THREADS=1 nice -n 15 /bin/sh -c '
head -n 1 REPORT.md
wc -l LOG.md PROOF.md AUDIT.md REPORT.md
sed -n "115,255p" PROOF.md
sed -n "265,313p" PROOF.md
sed -n "1,115p" AUDIT.md
cat REPORT.md
date "+%Y-%m-%d %H:%M:%S %Z"
'
```

Exit 0; the priority denial persisted. REPORT.md has the required first
line. Counts before this append were LOG.md 184, PROOF.md 313,
AUDIT.md 174, REPORT.md 98. Rechecked the strict inequality, endpoint
threshold, minimizer equation, scalar extremizer, and stated limitations.
No correction to the mathematics was needed. The chosen extension is
complete; the variance convergence assertion is not proved.

