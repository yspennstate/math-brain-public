# The planted-count bridge

This note independently proves a quantitative version of one implication in
the claimed outside solution by mt0-svg, at commit
`d6b298c0100af57a8f46f8314eca8bf8f7eb4693`. It does not verify the certificate
or prove its linear mean bound. In particular it does not independently
settle either case of T127.

## 1. Recheck of the preceding model audit

In the saved formal model, vertices are words over an alphabet of size d.
A nonempty word has its tail as parent and d distinct children, whereas the
empty word has d children and no parent. A step variable is uniform on
Fin(d) × Fin(d+1). At the root the first component is used; every possible
child has d+1 preimages. Away from the root the second component is used;
every possible neighbor has d preimages. Dividing by d(d+1) gives the simple
random walk transition probabilities 1/d and 1/(d+1), respectively. The
coordinates indexed by distinct frogs and walk steps are independent under
the product measure. This establishes the claimed walk law independently
of the source comments. Enumeration in audit_bridge.py gives the same
fiber counts for d=3,4.

The wake recursion retains every existing activation time and activates an
unvisited vertex at time t+1 exactly when a previously active frog reaches
it on its next step. A newly activated frog starts at index zero. Induction
on time therefore identifies it with synchronous activation in T127.
There are at most 2^t active frogs at time t, by induction: each active
frog can activate at most one sleeper in the next step. Thus infinitely
many visit pairs are equivalent to infinitely many root-visit times.
Excluding the initial visit does not change finiteness.

The additional-root-frog argument in round 5 also holds. For fixed whole
paths, the activated frogs are exactly the finite directed reachability
closure of the seeds, with an edge u→v when u's path visits v. This follows
by tracing activation predecessors backwards, and conversely by induction
along any finite directed path. Reachability from two seeds is the union
of their separate closures. Each activated frog contributes its whole
path's total root visits regardless of its wake time. Consequently the
two-seed total is between the first single-seed total and the sum of the
two single-seed totals, when all share the non-root paths. Both single-seed
systems have the prescribed marginal law. Almost-sure recurrence or
transience therefore transfers to the extra-root-frog convention.

These arguments confirm the preceding model audit. They do not check the
imported theorems.

## 2. A second-moment criterion with its degree factor retained

Fix an integer d≥2. The planted tree consists of a rooted d-ary tree with
root r and an extra leaf y joined to r. Frogs perform simple random walk
until first hitting y, where they stop. Every vertex of the d-ary part has
degree d+1, including r. Assign independent whole walk paths to all its
vertices.

Let X be the total number of activated frogs whose paths hit y, with
one initial active frog at r and a sleeper at every other vertex. Each
frog is counted once. Let U_m be the number of assigned paths starting
at depths 0,...,m that hit y, whether or not their frogs are activated.
Suppose measurable nonnegative random variables Z_m satisfy

\[
Z_m\le X,\qquad Z_m\le U_m\quad\text{almost surely}.
\]

For example, take Z_m to count frogs reaching y in the model with sleepers
only through depth m. Its activated set is contained in the full model's
activated set by directed reachability, so Z_m≤X. Every frog it activates
starts at depth at most m, so Z_m≤U_m. These comparisons concern whole
paths and do not require equal activation times.

**Proposition.** If c>0 and E Z_m≥cm for an unbounded sequence of positive
integers m, then

\[
\Pr(X=\infty)\ge d^2c^2.
\]

**Proof.** Define f(y)=1 and f(v)=d^{-(i+1)} when v has depth i in the
d-ary part. At depth i≥1 its neighbor average is

\[
\frac{d^{-i}+d\,d^{-(i+2)}}{d+1}=d^{-(i+1)}.
\]

At r the average is (1+d·d^{-2})/(d+1)=1/d=f(r). Let p_t(v) be the
probability of hitting y within t steps from v. We have p_0≤f. Since y
is absorbing, the Markov transition recursion and the neighbor averages
show inductively that p_t≤f for every t. Increasing t to infinity gives

\[
p_v:=\Pr(\text{the path from }v\text{ hits }y)\le d^{-(|v|+1)}.
\]

The variables I_v indicating these hits are independent: I_v depends
only on the assigned path of frog v. The set of vertices of depth at
most m is finite, and U_m is the sum of its I_v. There are d^i vertices
at depth i. Therefore, with s_m=E U_m,

\[
s_m=\sum_{|v|\le m}p_v
 \le\sum_{i=0}^{m}d^i d^{-(i+1)}=\frac{m+1}{d}.
\]

Independence and I_v²=I_v give

\[
E U_m^2=s_m^2+\sum_{|v|\le m}p_v(1-p_v)
 \le s_m^2+s_m
 \le B_m:=\frac{(m+1)^2}{d^2}+\frac{m+1}{d}.
\]

In particular Z_m is square integrable. Fix a finite K≥0. On {X≤K},
Z_m≤K. On {X>K}, Z_m≤U_m. Cauchy–Schwarz now gives

\[
cm\le E Z_m
 \le K+E[U_m\mathbf1_{\{X>K\}}]
 \le K+\sqrt{B_m\Pr(X>K)}
\]

for every m in the specified sequence. For sufficiently large such m,
cm>K, so

\[
\Pr(X>K)\ge\frac{(cm-K)^2}{B_m}.
\]

Along that sequence, B_m/m²→1/d² and K/m→0. Hence
Pr(X>K)≥d²c² for every finite K. The events {X>K} decrease to
{X=∞} as integer K→∞. Continuity from above of a probability measure
proves the proposition. No monotonicity or independence of the Z_m is
required. ∎

An independent threshold derivation gives the same constant. For any
nonnegative square-integrable Z with mean a>0 and 0<θ<1,

\[
a\le\theta a+\sqrt{E Z^2\Pr(Z>\theta a)},
\quad
\Pr(Z>\theta a)\ge(1-\theta)^2a^2/E Z^2.
\]

The first inequality splits the expectation on {Z≤θa} and its complement
and applies Cauchy–Schwarz. Apply it to Z_m. Since a=E Z_m≥cm and
Z_m≤X, it yields

\[
\Pr(X>\theta cm)\ge(1-\theta)^2c^2m^2/B_m.
\]

Take an increasing sequence of the admissible m. Its left-hand events
decrease to {X=∞}. Let m→∞ and then θ↓0 to recover d²c².

The source's Awake.lean first obtains the same hitting bound and then
drops its factor 1/d, giving E U_m²≤(m+1)+(m+1)². Retaining that factor
and taking the asymptotic limit gives the quantitative bound above.
This is a refinement of that estimate; no priority claim is made.

## 3. Exact arithmetic at the d=3 interface

The imported d=3 argument asserts, with m1=1778279,

\[
E G_n(1)\ge(n+2)/5\quad(n>m1-30),
\qquad
E Z_{n+1}\ge(1+E G_n(1))/4.
\]

Treat these inequalities as hypotheses. For m=n+1 they imply

\[
E Z_m\ge\frac{1+(m+1)/5}{4}
 =\frac{m+6}{20}\ge\frac m{20}
 \qquad(m\ge1778251).
\]

Indeed m1-30=1778249, so the first allowable integer n is 1778250.
The excess over m/20 is exactly 3/10. The proposition with d=3 and
c=1/20 gives the conditional conclusion

\[
\boxed{\Pr(X=\infty)\ge9/400.}
\]

The paper's second-moment paragraph gives c²/24, which at c=1/20 is
1/9600; 9/400 is 216 times that bound. This comparison is only about
the lower bound on the planted event. The classification would still
require the source's independent implication from positive probability
of this event to almost-sure recurrence in the original model.

The terminal certificate arithmetic also agrees exactly. Its declared
deficit ratio is δ=7045771/88917100 and its all-awake mean at (m1,62) is

\[
\mu=(m1+1+62)/3=1778342/3.
\]

Consequently

\[
(1-\delta)\mu=27290443/50=b1.
\]

Solving this equation for δ gives 1-b1/μ=7045771/88917100, a second
check independent of the forward multiplication. A valid terminal
state with deficit at most δμ would therefore supply the required mean
b1. Its existence and validity have not been established here.

## 4. Source boundary and limits

The top-level recurrence term uses Assembly.recurrent_three_of_m1 and
Chain.m1run_certS_proof. The latter refers to M1K.storedRun_holds and
CertData.certS1_stored, and supplies LaneD.step_sound, seedCheck_sound,
extCheck_sound and topMass_eq_massPk. The step-soundness statement
requires all part checks and a coverage check, parameter bounds and an
input-state shape condition. Its conclusion gives the output shape as
well as an upper bound on the step map. The certificate interface also
requires a complete chain, a terminal postfixed inequality and both
deficit conditions. These are substantive requirements beyond matching
the target's model definitions.

CertData and M1Data are generated from release inputs. Source-text scans
and matching input digests do not evaluate these inputs or prove the
soundness of their checkers. The second-moment proposition above is
proved independently; its application with c=1/20 remains conditional.
Neither the complete imported argument nor the d=4 argument is certified
by this note.
