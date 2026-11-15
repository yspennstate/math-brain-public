# T076 work log, round 6

Task: “take the NEXT checkable step on this problem, building on that work.”
Received 15 November 2026, approximately 10:32 Asia/Tbilisi (06:32 UTC).

## Orientation and bounded literature check, 10:32–10:34

Read the startup MEMORY.md and compute_state.json, all four earlier
REPORT.md and LOG.md files, the three available PROOF.md files, and the
first session's SOLVED_ELSEWHERE.md. Directory listings show no scripts in
any earlier folder and no PROOF.md in the first session. Prior folders are
read-only. The task-specific restriction to writes only in this folder
overrides the earlier shared mesh/checklist/brain-write instructions;
none of those external stores is being changed. No git or subagents.

The compute state is `ok`, `owner_away_open`. A priority probe,
`OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1
nice -n 15 /usr/bin/true`, reports
`nice: setpriority: Operation not permitted`. No numerical program will
run without the required priority. The intended work is analytic.

Web search queries:

- `random band matrices two dimensional localization lengths Lai Yang 2609.24426`
- `random band matrices dimension three fixed bandwidth delocalization 2026`

Opened primary pages https://arxiv.org/abs/2609.24426,
https://arxiv.org/html/2609.24426v4, and
https://arxiv.org/abs/2507.20274. The first remains v4 of 8 November 2026,
by Xujie Lai and Fan Yang, *Localization Lengths for Two-Dimensional Random
Band Matrices: Exponential Lower Bounds*. Its already-recorded threshold is
W >= (log N)^(1+epsilon). The d>=3 paper is by Sofiia Dubova, Fan Yang,
Horng-Tzer Yau and Jun Yin; its abstract still assumes W>=N^c. No later
solution was found in this search, which finished within five minutes.
Further opening of the v4 paper is source inspection for the proposed
lemma, not an extended literature survey.

Commands for document inspection were `ls -la`, `cat`, `sed`, `tail`,
and `rg --files`. No computational scripts exist in the earlier folders.

## Independent verification of round 5, before the extension

The earlier result holds. In the eigenbasis of A, write a=1-b>0 and
g_u=1-ub. The exact conjugation gives

    J_t = delta^2/W^2 C_t [integral_0^t u^2 E(u) A B G_u^2 E(u) du] C_t,
    C_t=A^(1/2)G_t Q.

A separate route is to set Y_u=(I-uB)D(u)(I-uB) and then substitute
Y_u=delta*u/W^2 A^(1/2)E(u)A^(1/2) into
W^2 G_t Y_u B G_u^2 Y_u G_t. Both give the same factor W^-2.
For the positive primitive F_v, its eigenvalue is bounded by

    a|b| integral_0^v u^2/g_u^2 du
      <= a v^2 [u/(1-ub)]_0^v
      = a v^3/g_v <= v^2.

Step-path summation by parts then yields ||integral E dF E|| <=
t^2(1+2V), since replacing one contraction by another costs at most
2||F|| times the norm of the replacement. This independently verifies
the BV estimate, including negative b and its endpoint factor.

For the two-logarithm lower bound, each round-5 swapped pair sends the
coefficient at j into output k, by multiplying the 2 by 2 swap matrix
on both sides of diag(f_k,f_j). The plateau coefficient is at least
28/(8*138^2*s), exceeding 1/(10000*s); the plateau length s/2 gives
1/20000. Independently grouping the low modes by rows rather than
square shells gives sum_(1<=k1,k2<=n) 1/a_k >=
M^2/16 sum_(l=1)^n 1/l. Thus the origin coefficient is at least
(1/20000)*(4/9)*(2/16)=1/360000 times sum_r log(8^r+1).
Summing r reproduces log(8)*R(R+1)/720000. All modes used have b>0.
The disjoint time windows make repeated modes across scales harmless.
No earlier error found. This is analytic verification, not a numerical run.

## Choice recorded before extending the result

Prove one replacement for temporal bounded variation: a sharp bound in
terms of the number of dyadic diffusion scales that E(u) can couple.
Let Pi_j project onto dyadic bands of A on Q. Assume, at each time,
Pi_i E(u) Pi_j=0 when |i-j|>h, with no temporal regularity. The target
is K_t=integral_0^t u^2 E(u) A|B|G_u^2 E(u) du <=
C(2h+1)t^2 Q, and consequently one return-kernel logarithm when h is
fixed. Also check whether the linear cost in h is necessary.

Reason: round 5 identifies successive transfers between widely separated
diffusion scales as the obstruction. Controlling those transfers is a
different input from controlling temporal variation, and remains meaningful
for a random path with infinite variation. It is not yet known for the
actual random normalized error. Full positivity and Ward constraints are
not resolved by this choice; a precise conditional alternative to the
square-function target is the scope of this session.

## Bound derived and sharpness refinement

Use Pi_j=1_(2^-j,2^(1-j)](A)Q for j>=0. On that band, with lambda=2^-j,

    u^2 a|1-a|/(1-u+ua)^2 <= 2u^2 lambda/(1-u+u lambda)^2 = q_j(u),
    integral_0^t q_j(u)du <= 2 lambda*t^3/(1-t+t lambda) <= 2t^2.

For v in Q, the scale restriction makes Pi_i E(u)v depend only on
R_i v=sum_(|i-j|<=h) Pi_j v. Contractivity bounds its squared norm by
||R_i v||^2. Integration band by band, then counting how often each input
band occurs, proves the explicit constant

    K_t <= 2(2h+1)t^2 Q,
    -2(2h+1)delta^2*t/W^2 G_t Q <= J_t <=
       2(2h+1)delta^2*t/W^2 G_t Q.

The linear dependence can be checked sharply with one modification of
the round-5 simultaneous swaps. Fix 1<=q<=R and retain only output
frequencies with max(k1,k2)>m_r=8^max(r-q,0) in the square
1<=k1,k2<=n_r=8^r. Pair each with (k1+3n_r,k2) as before. Their A-eigenvalue
ratio is less than 64^(q+1), so E couples at most h=6q+6 dyadic bands.
The retained harmonic sum is at least (log 8)/2 * min(r,q), in place of
log(n_r+1). This gives

    J_(1-M^-4),00 >= delta^2/W^2 * (log 8)/1440000 * q R,
    M=8^(R+2).

Thus the upper order (h+1)log M/W^2 is attained, for h proportional to q,
throughout this range, rather than only when h is of order log M.
The fixed mode k=(2,1) survives the first q swaps, separately proving
<e_k,K_t e_k> >= q/20000 and a relative-drift loss at least q/30000.
Detailed proof and independent audits will be written next.

## Proof saved

Saved PROOF.md with the complete dyadic square-function bound, its exact
two-coordinate Duhamel consequence, and the truncated-swap lower family.
Also proved the same criterion with decaying couplings in place of exact
zeros: if ||Pi_i E(u) Pi_j||<=c_(i-j) and S=sum_m c_m<infinity uniformly,
then K_t<=2S^2*t^2 Q. Weighted Cauchy–Schwarz gives the coefficient S^2;
the sharper 2h+1 coefficient for exact range h uses contractivity directly.
No temporal differentiability, bounded variation, or time independence is
used. This is a conditional deterministic result, not a stochastic estimate.

Source inspection: opened Lai–Yang v4 HTML near (2.19), (2.31)–(2.38),
and (3.21)–(3.22). The quadratic error is indeed W^2 D B D and the
propagator acts in both coordinates. The Ward identities give resolvent
row and column sums. No derivation from those identities to the spectral
transfer assumption is known here; the proof states this limitation.

## Adversarial audit

The preliminary triangle-inequality approach to an exact bandwidth h
would have given a quadratic cost (2h+1)^2. It is unnecessarily large:
contractivity gives ||Pi_i E R_i v||<=||R_i v|| before integration, leaving
only one overlap count. A second count using residues modulo 2h+1 gives
the same linear factor, including bands truncated at index zero.

The integral coefficient 2 was rederived by the substitution
z=u/(1-u+u*lambda), for which dz=du/(1-u+u*lambda)^2. This gives
integral q_i<=2lambda*t^3/(1-t+t*lambda)<=2t^2 independently of
evaluating an antiderivative with a factor 1/(1-lambda).

For sharpness, rechecked the exact spectral ratio:
136/(16/5)=85/2<64 and n_r/m_r<=8^q. Hence the input/output eigenvalue
ratio is strictly below 2^(6q+6). Dyadic intervals at index distance d
have ratio strictly greater than 2^(d-1), so d<=6q+6; no off-by-one
at a dyadic endpoint. For q=1, m_r=8^(r-1) except m_1=1, so each
retained annulus is nonempty; for q=R all m_r=1. Both extremes work.

The harmonic annulus bound was checked twice: square shells with 2l-1
points, and disjoint rows k2=l with 1<=k1<=l. Both yield M^2/16 times
sum_(m_r<l<=n_r)1/l. Removing the small square costs at most log 2
relative to log(n_r/m_r); since log 8=3log 2 and min(r,q)>=1, retaining
half the latter is valid. The exact layer count
sum_r min(r,q)=sum_(s=1)^q(R-s+1)=qR-q(q-1)/2>=qR/2
independently checks the last factor two.

Rechecked all numerical factors: the plateau bound has denominator
8*138^2=152352<280000; its length is s_r/2. The cosine value squared
is 2/M^2, the final-mass comparison is 4/(9a_k), and the annulus sum
has factor M^2/32. Their product is 1/720000 per min(r,q), then
1/1440000 per qR. The fixed output (2,1) belongs to every first-q
annulus, so K_t has coefficient at least q/20000 there; a_k/g_t(k)>=2/3
gives the independent relative-drift coefficient q/30000.

For each active scale all used b_k are positive. E ABG_u^2 E is diagonal
in one fixed real eigenbasis, by the 2 by 2 swap identity, so no negative
mode or cross-term cancellation can invalidate either lower bound. The
general upper bound instead uses |B| and includes negative and zero b.
The time windows lie below t=1-M^-4, the constant mode is removed, and
all cosine frequencies lie strictly below a half-period. The positive
mass avoids a singular t=1 argument. The result includes M=3 for the
upper bound; the lower examples use the stated larger M.

## Final readback, 10:39–10:40 Asia/Tbilisi

Read PROOF.md and LOG.md in full and then REPORT.md, using
`OMP_NUM_THREADS=1 nice -n 15 /bin/cat ...`; document reads completed with
the same priority warning. Re-read the first-session and round-4 logs
separately so that truncated earlier multi-file output could not hide a
caveat. No prior result needed correction.

Used `rg -n '^VERDICT:|^##|\\tag\{|\\\[|\\\]' REPORT.md PROOF.md LOG.md`
to inspect the verdict and equation/display structure. PROOF.md contains
35 consecutively numbered equations. Clarified that repeated frequencies
refer to the same vector, and that the finite sum over R_i may include
indices within h of a nonzero spectral band. These are clarifications,
not changes to a bound. The report states the new result, its exact
conditional scope, failed rough bound, analytic checks, commands, numerical
priority limitation and a concrete next-worker target.

Completed deliverables: REPORT.md, PROOF.md, LOG.md. No numerical script
was needed or executed. No other folder, shared state, git repository or
external system was changed. T076 remains open.
