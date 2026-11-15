# T076 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Received 15 November 2026, approximately 08:02 Asia/Tbilisi (04:02 UTC).

## Orientation and literature check

Read the REPORT.md and LOG.md in all three earlier folders, round-3 and
round-4 PROOF.md, and the first session's SOLVED_ELSEWHERE.md. Directory
inspection confirms no computational scripts and no first-session PROOF.md.
Read the startup memory, brain index, and compute governor state. The latter
reports warn / owner_away_open / cpu_saturated. This task's restriction to
writes only here overrides external mesh, checklist, recall-log and memory
mutations. No git, external registration or subagents.

Document commands used `OMP_NUM_THREADS=1 nice -n 15 /bin/cat ...`,
`rg --files ...`, and `OMP_NUM_THREADS=1 nice -n 15 /usr/bin/find ...`.
The sandbox again reports `nice: setpriority: Operation not permitted`.
Only document inspection was performed; no numerical experiment will run
without verified priority. The work below is analytic.

Literature search began at 04:02 UTC and completed within five minutes.
Queries:

- `"random band matrices" "2026" "Lai" "Yang"`
- `"random band matrices" "bounded" "three" delocalization 2026`

Opened https://arxiv.org/abs/2609.24426,
https://arxiv.org/html/2609.24426v4, and
https://arxiv.org/abs/2507.20274. The first remains v4 (8 November 2026),
Xujie Lai and Fan Yang, *Localization Lengths for Two-Dimensional Random
Band Matrices: Exponential Lower Bounds*. The second paper is Sofiia Dubova,
Fan Yang, Horng-Tzer Yau and Jun Yin, *Delocalization of Non-Mean-Field
Random Matrices in Dimensions d >= 3*; its abstract still requires W >= N^c.
No later solution found in this bounded search. The v4 improvement was
already recorded by the earlier workers and is not a new stopping event.

## Independent recheck before choosing the extension

The round-4 main estimate holds. A different scalar bound makes the time
cancellation explicit. For a=1-b>0, g_u=1-ub and |b|<=1,

    a * integral_0^t u^2 |b|/g_u^2 du
      <= a*t^2 * integral_0^t 1/g_u^2 du
      = a*t^3/g_t <= t^2.

For the commuting saturating envelope, the drift eigenvalue is at most
delta^2/W^2 * (a/g_t^2)*t^2 <= delta^2*t/(W^2*g_t).
This uses no division by b, includes b=0 and negative b, and gives exactly
the round-4 Loewner bound. The weaker-envelope calculation independently
follows by setting Y_u=(I-uB)D(u)(I-uB): its integrand becomes
G_t Y_u [B G_u^2] Y_u G_t. For D=delta*u*W^-2*G_u Q this simplifies to
delta^2*u^2/W^2 * B G_t^2 Q, whose integral has factor t^3/3.
At M=3 the eigenvalue check gives (4/9)(10/9-5/36)=35/81,
and hence 35 delta^2/(243 W^2). No earlier error found.

## Choice, recorded before the extension

One piece: extend the quadratic-drift estimate to noncommuting errors.
Use the same pointwise Loewner envelope, parametrized by self-adjoint
contractions E(u) through

    D(u)=delta*u/W^2 * A^(1/2) G_u E(u) G_u A^(1/2), on Q.

Test whether a dimension-independent bound survives if E has bounded
variation in operator norm. Also test whether any time restriction can
be omitted: errors can transfer successive diffusion scales into one
fixed output mode. This is the missing noncommuting issue identified
in round 4, restricted to the single quadratic term; no assertion about
the stochastic resolvent error is assumed.

The proposed argument uses the positive matrix primitive
F_t=integral_0^t u^2 A |B| G_u^2 du <= t^2 Q.
A time-independent E can be pulled outside this integral. Integration
by parts should replace that step for bounded variation E, with a cost
controlled by its total variation. A separate sequence of Fourier-mode
swaps will test the necessity of temporal control.

## Noncommuting calculation and stronger adversarial test

Writing C_t=A^(1/2)G_t on Q gives exactly

    J_t = delta^2/W^2 * C_t [integral_0^t
               u^2 E(u) A B G_u^2 E(u) du] C_t.

The positive primitive F_v=integral_0^v u^2 A|B|G_u^2 du satisfies
0<=F_v<=v^2 Q. For a contraction path with operator-norm total
variation V, Stieltjes integration by parts yields

    -delta^2*t*(1+2V)/W^2 * G_t Q
        <= J_t <= delta^2*t*(1+2V)/W^2 * G_t Q.

The entry bound therefore still has only the return-kernel logarithm
when V is uniformly bounded. A second derivation will use telescoping
step paths, to check the coefficient 1+2V without formal Stieltjes rules.

The first adversarial idea (one fixed output mode) only breaks the
operator comparison and need not break a single-log entry bound. It is
insufficient for that stronger conclusion. Replaced it by simultaneous
swaps of n^2 low cosine modes with n^2 modes at frequency of order n,
at successive scales n=8^r. Each scale contributes at least c log n
to the origin diagonal; summing r yields c (log M)^2. Thus the same
pointwise envelope can fail even the previous entry bound without
commutation or temporal control. The proof will specify all modes,
time intervals and constants, and use t=1-M^-4 <1.

## Proof saved and first audit, 04:09 UTC

Saved PROOF.md with the exact noncommuting factorization, two derivations
of the bounded-variation estimate, a universal two-log upper bound, and
an explicit continuous family attaining that order. No computation ran.

Construction: M=8^(R+2), n_r=8^r, s_r=n_r^2/M^2. Swap the n_r^2
real cosine modes k in {1,...,n_r}^2 with j=(k_1+3n_r,k_2), using
disjoint time windows 1-u in [s_r,2s_r]. A piecewise linear scalar
cutoff is one on the middle half. Normalized cosine values at the
origin have square 2/M^2. The input eigenvalues satisfy
28s_r<=a_j<=136s_r<1/16. The time integral on the plateau is at least
1/20000; at t=1-M^-4, a_k/g_t(k)^2>=4/(9a_k). Finally
sum_{k in {1,...,n}^2} 1/a_k >= M^2 log(n+1)/16. Together these give

    J_t,00 >= delta^2/W^2 * (log 8)/720000 * R(R+1).

The constant is checked as (1/20000)*(4/9)*(2/16)=1/360000,
then sum_{r=1}^R r=R(R+1)/2. The scalar plateau bound is checked by
28*10000 > 8*138^2 = 152352. All modes used have positive b_k, so
the drift diagonal has no negative-mode cancellation.

Added a small-entry corollary. Under the pointwise envelope,
sup_u max_xy |D_xy(u)| <= C delta*(1+log M)/W^2, since the comparison
matrix AG_u^2Q has diagonal at most 4r_M(1) at late times. Choosing
W=ceil(R^(3/4)) makes these error entries O(delta R^-1/2), while the
quadratic diagonal is at least c delta^2 R^1/2. Thus uniformly small
entries do not rescue even the stronger noncommuting envelope.

One attempted multi-file patch had an invalid LOG.md context and was
rejected atomically; a read confirmed no partial proof change. The
corrected patch above succeeded. All writes remain in this folder.

## Adversarial audit and report

Rechecked the source directly at Lai–Yang (2.31)–(2.39): the quadratic
term is W^2 D B D and its propagator acts in both coordinates exactly
as used here. This was a source verification, not another literature
search. Re-read the round-3 log separately to ensure the initial batched
output had not hidden any earlier caveat.

Independent checks saved in PROOF.md:

- The Y_u=(I-uB)D(u)(I-uB) factorization reproduces the direct
  cancellation and the W^-2 normalization.
- A two-by-two swap interchanges diagonal coefficients, verifying
  that input scale a_j, rather than output scale a_k, occurs inside
  the time integral.
- Square shells and disjoint rows each give the harmonic lower bound
  sum 1/|k|^2 >= (1/2) sum_{l<=n} 1/l.
- Both the differential product rule and step-path telescoping give
  the bounded-variation constant 1+2V.
- Positive mass mu=M^-4 is smaller than every time window and at most
  half every nonconstant a_k. This checks the 4/(9a_k) factor and
  avoids relying on a t=1 singular limit.
- All paired frequencies lie below M/2, are nonconstant and have
  positive b_k. Repeated modes across scales are harmless because the
  time supports are disjoint. Real cosine normalization contributes
  2/M^2, not 1/M^2. The cutoff plateau length is s_r/2, not s_r.
- The universal upper bound is O(delta^2*(1+log M)^2/W^2), matching
  the constructed lower order. Negative b_k are handled with |B|.

REPORT.md saved with the required PARTIAL first line, exact scope,
counterexample, failed inference and next-worker target. The new
counterexample does not refute any random-matrix theorem: no realization
or full positivity/Ward constraints have been proved. The bounded
variation input has likewise not been established for a random error.

## Final readback, 04:11–04:12 UTC

Read REPORT.md in full with `OMP_NUM_THREADS=1 nice -n 15 /bin/cat
REPORT.md`; the same priority warning appeared. PROOF.md and LOG.md
were also read back after saving. Added the explicit definition of total
variation and restricted the strict upper symbol bound to nonzero
frequencies. No mathematical constant changed. Rechecked the required
verdict line, all local links, task wording and receipt time, and the
absence of a claim to solve T076. The deliverables are REPORT.md,
PROOF.md and LOG.md. There is no computation script because the result
is wholly analytic. No earlier folder or external state was edited.
