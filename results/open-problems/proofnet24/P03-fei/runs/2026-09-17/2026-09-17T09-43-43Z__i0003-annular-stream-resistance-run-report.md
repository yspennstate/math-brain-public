Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested in prompt text, but the exposed scheduler/runtime provides no model-family selector, no reasoning-effort selector, and no authenticated routing receipt; I therefore do not claim GPT-6 or maximum reasoning. **NO MOVEMENT in the active metric: `eta_stream^cert = 1/2 -> 1/2`; unchanged streak `0 -> 1`. Methods used: #11 DUALIZE, #24 FIND THE EXTREMAL OBJECT, #29 ADD THE POINTS AT INFINITY.**

# P03 / I0003 run report — annular stream resistance and the critical `sqrt(log)` endpoint

Run date: 17 September 2026 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
Track: P03 / HARD OUTSIDE.  
Canonical claim: `operations/claims/I0003.md`.  
Source: Ahmed Bou-Rabee and Yuval Peres (2026), *The randomly oriented Manhattan lattice in 2D is transient*, arXiv:2609.07621v1, Section 7, Problem 3.  
Broad source status after this run: **OPEN / PARTIAL**.

The inherited saturated metrics remain

- `periodic_scope_certified = 1`,
- `bounded_discrepancy_scope_certified = 1`.

The active quantitative metric is

\[
\eta_{\rm stream}^{\rm cert}=\frac12,
\]

meaning that for every fixed `gamma < eta`, every exact-source deterministic field with anchored stream envelope `M(R)=O((log(2+R))^gamma)` is rigorously covered by recurrence. The preceding run proved the stronger endpoint-little-o statement `M(R)=o(sqrt(log R)) => recurrence`. This run does **not** increase the power exponent, but it does remove the little-o restriction, proves the full critical endpoint `M(R)=O(sqrt(log R))`, and in fact proves a strictly larger annular-resistance class such as `M(R)=O(sqrt(log R log log R))`.

The main new claim is

`P03-I0003-ANNULAR-STREAM-RESISTANCE-236 = PROVED / PARTIAL / PUBLICATION-NOVELTY-UNVERIFIED`.

No checker was created: this is an analytic infinite-volume theorem with a complete argument below and no finite computational core.

---

## 1. Repository continuity and scope gate

I continued from the newest complete P03 report rather than restarting:

`proofnet24/P03-fei/runs/2026-09-17/2026-09-17T08-36-10Z__i0003-subsqrtlog-stream-run-report.md`, creation commit `6c1051d86072386533f09dc00ffb2b9226dc4c20`, blob `3c9b97d6bd979bfa28422e4a41f26ab2ca2052d0`.

Before the attack I reread/recovered the current repository controls and source state needed for this problem: root `README.md`; `proofnet24/HOURLY_PROTOCOL_2026-09-15.md`; `FLEET_RULES.md`; `operations/FLEET_2026-09-16.md`; campaign `INDEX.md` and `RANKING.md`; root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`; `operations/claims/I0003.md`; the separate `operations/claims/I0004.md` ownership reservation; the current P03/I0003 report history; the newest same-source neighboring I0002 report; and the newest P04/I0101 report needed for the directed audit. Large intake/search surfaces are connector-bounded when rendered wholesale; I recovered exact relevant claim/intake/history rows and do **not** describe that as a literal byte-for-byte reread of every unrelated intake row.

Ownership remains exclusive to P03 for I0003. I0004, the partially oriented irrational-rotation subquestion, remains separately owned and was not touched.

The source was checked again on 17 September 2026. Bou-Rabee--Peres still state Problem 3 exactly as:

> Which orientation fields give a recurrent walk, and which give a transient one?

The source itself gives almost-sure transience for iid fair full Manhattan orientations and recurrence for the alternating deterministic environment; it separately states the partially oriented irrational-rotation question. No model substitution is made here.

I use the rate-one embedded normalization from the preceding P03 reports:

\[
(Pf)(x,y)=\frac12 f(x+a_y,y)+\frac12 f(x,y+b_x),
\qquad a_y,b_x\in\{-1,1\},
\]

and `L=P-I`. The source's displayed continuous-time generator is exactly twice this generator, so recurrence/transience is unchanged and capacities are changed only by a harmless factor of two. Counting measure is invariant, and the symmetric part is planar simple random walk, exactly as the source records.

---

## 2. Idea before code; refutation-first target

The assigned first target was to try to build a deterministic transient field at the apparent barrier

\[
M(R)=O(\sqrt{\log R}).
\]

The preceding proof used a local sector constant bounded by the **maximum** stream on the whole box and then squared that constant. That left open whether `sqrt(log R)` was a real transition or merely a worst-case loss.

The first move was therefore to dualize the nonreversible capacity formula and keep the stream weight **face by face** rather than taking a box supremum. This kills the proposed critical-scale transient construction: every field with `M(R)=O(sqrt(log R))` is recurrent. More strongly, recurrence follows from a divergent annular resistance series depending on the actual squared stream values on successive square boundaries.

Thus the counterexample search failed for a mathematical reason, not because no candidate was found.

---

## 3. Exact setup: face stream and energies

Choose anchored one-dimensional primitives

\[
\alpha_0=\beta_0=0,
\qquad
\alpha_y-\alpha_{y-1}=a_y,
\qquad
\beta_x-\beta_{x-1}=b_x,
\]

and define the face stream on the unit face with lower-left corner `(x,y)` by

\[
\psi_{x,y}=\frac{\alpha_y-\beta_x}{4}.
\]

Let

\[
M(R)=\sup_{|x|,|y|\le R}|\alpha_y-\beta_x|.
\]

For a finitely supported function `f`, let

\[
G(f)=\sum_{\{u,v\}\text{ n.n.}}(f(u)-f(v))^2,
\qquad
D(f)=\langle f,-Sf\rangle=\frac14G(f),
\]

where `S=(L+L^*)/2`.

For a face `q`, with cyclic vertex values

\[
f_{00},f_{10},f_{11},f_{01},
\]

define its perimeter energy

\[
E_q(f)
=(f_{00}-f_{10})^2+(f_{10}-f_{11})^2
 +(f_{11}-f_{01})^2+(f_{01}-f_{00})^2.
\]

The exact curl identity inherited from the previous stream-function derivation is

\[
B(f,g)=\sum_q \psi_q C_q(f,g),
\tag{3.1}
\]

for the skew part of the bilinear form, where

\[
C_q(f,g)
=(f_{00}-f_{11})(g_{10}-g_{01})
 +(f_{10}-f_{01})(g_{11}-g_{00}).
\tag{3.2}
\]

The crucial improvement is to estimate (3.2) locally before taking any supremum over `q`.

---

## 4. Weighted face-sector lemma

### Lemma 4.1

For every face `q`,

\[
|C_q(f,g)|\le \sqrt{E_q(f)E_q(g)}.
\tag{4.1}
\]

#### Proof

For four numbers `a,b,c,d`,

\[
\begin{aligned}
&(a-b)^2+(b-d)^2+(d-c)^2+(c-a)^2\\
&\qquad -\big[(a-d)^2+(b-c)^2\big]
=(a-b-c+d)^2\ge0.
\end{aligned}
\tag{4.2}
\]

Hence the squared Euclidean norm of the two diagonal differences is at most the perimeter energy. Apply Cauchy--Schwarz to the two-vector of diagonal differences in (3.2). ∎

Define the weighted stream energy

\[
W_\psi(f)=\sum_q \psi_q^2 E_q(f).
\tag{4.3}
\]

Every undirected nearest-neighbor edge belongs to exactly two unit faces, so

\[
\sum_q E_q(g)=2G(g)=8D(g).
\tag{4.4}
\]

Combining (3.1), Lemma 4.1 and Cauchy--Schwarz gives the weighted skew bound

\[
\boxed{
|B(f,g)|
\le \sqrt{8W_\psi(f)D(g)}.
}
\tag{4.5}
\]

For the symmetric bilinear part,

\[
|D(f,g)|\le\sqrt{D(f)D(g)}.
\tag{4.6}
\]

Therefore the full form satisfies

\[
\boxed{
|\mathcal E(f,g)|
\le
\big(\sqrt{D(f)}+\sqrt{8W_\psi(f)}\big)\sqrt{D(g)}.
}
\tag{4.7}
\]

This is the step that the previous box-supremum sector estimate discarded.

---

## 5. Dualized finite-volume capacity bound

Let

\[
\Lambda_R=[-R,R]^2\cap\mathbb Z^2,
\qquad B_R=\Lambda_R^c.
\]

Gaudilliere--Landim's nonreversible Dirichlet principle, after collapsing `B_R`, gives

\[
\operatorname{cap}_{L}(\{0\},B_R)
=
\inf_F\sup_H
\left\{2\langle L^*F,H\rangle-D(H)\right\},
\tag{5.1}
\]

where `F(0)=1`, `F=0` on `B_R`, and by their constant-shift remark the supremum may be represented with `H=0` on `B_R` and `H` constant on `{0}`. Thus zero extension puts both test functions in the finite-support setting of (4.7); there is no missing exterior boundary-current term.

For any fixed admissible `F`, (4.7) yields

\[
2\langle L^*F,H\rangle-D(H)
\le
2a(F)\sqrt{D(H)}-D(H)
\le a(F)^2,
\tag{5.2}
\]

with

\[
a(F)=\sqrt{D(F)}+\sqrt{8W_\psi(F)}.
\]

Consequently

\[
\operatorname{cap}_{L}(\{0\},B_R)
\le
\big(\sqrt{D(F)}+\sqrt{8W_\psi(F)}\big)^2
\le 2D(F)+16W_\psi(F).
\tag{5.3}
\]

Equation (5.3) is the successful form of method #11: dualization converts the nonreversible supremum into a weighted primal energy without replacing `psi` by its maximum.

---

## 6. The extremal annular potential

For `r>=1`, let `E_r^\partial` be the set of undirected nearest-neighbor edges with one endpoint in `Lambda_r` and the other in `Lambda_{r+1}\setminus\Lambda_r`. Its exact cardinality is

\[
N_r=|E_r^\partial|=8r+4.
\tag{6.1}
\]

For `e in E_r^\partial`, write `q_1(e),q_2(e)` for its two adjacent unit faces and define the annular squared-stream mass

\[
\Xi_r
=
\sum_{e\in E_r^\partial}
\big(\psi_{q_1(e)}^2+\psi_{q_2(e)}^2\big),
\tag{6.2}
\]

and

\[
A_r=\frac{N_r}{2}+16\Xi_r.
\tag{6.3}
\]

Take a square-radial trial function

\[
F(z)=u_{\|z\|_\infty},
\]

with `u_0=u_1=1`, `u_R=0`, and write

\[
\delta_r=u_r-u_{r+1},\qquad r=1,\ldots,R-1,
\qquad \sum_{r=1}^{R-1}\delta_r=1.
\tag{6.4}
\]

Only edges in `E_r^\partial` contribute. Hence

\[
D(F)=\frac14\sum_{r=1}^{R-1}N_r\delta_r^2,
\tag{6.5}
\]

and, after regrouping the face sum in (4.3) by its boundary edges,

\[
W_\psi(F)
=
\sum_{r=1}^{R-1}\Xi_r\delta_r^2.
\tag{6.6}
\]

Therefore (5.3) gives

\[
\operatorname{cap}_{L}(\{0\},B_R)
\le
\sum_{r=1}^{R-1}A_r\delta_r^2.
\tag{6.7}
\]

Now method #24 identifies the exact extremal trial potential. By Cauchy--Schwarz,

\[
1=\left(\sum_r\delta_r\right)^2
\le
\left(\sum_r A_r\delta_r^2\right)
\left(\sum_r A_r^{-1}\right),
\]

and equality is attained by

\[
\delta_r=
\frac{A_r^{-1}}{\sum_{j=1}^{R-1}A_j^{-1}}.
\tag{6.8}
\]

Thus

\[
\boxed{
\operatorname{cap}_{L}(\{0\},B_R)
\le
\left(
\sum_{r=1}^{R-1}\frac1{A_r}
\right)^{-1}.
}
\tag{6.9}
\]

This is an effective annular-resistance inequality at infinity.

---

## 7. The new recurrence theorem

### Theorem `P03-I0003-ANNULAR-STREAM-RESISTANCE-236`

For an exact fully line-oriented Manhattan field, form the anchored stream `psi` and annular coefficients `A_r` from (6.2)--(6.3). If

\[
\boxed{
\sum_{r=1}^{\infty}\frac1{A_r}=\infty,
}
\tag{7.1}
\]

then the walk is recurrent.

A simpler sufficient envelope condition is

\[
\boxed{
\sum_{r=1}^{\infty}
\frac1{r\,[1+M(r+1)^2]}
=\infty.
}
\tag{7.2}
\]

In particular,

\[
\boxed{
M(R)=O(\sqrt{\log R})
\quad\Longrightarrow\quad
\text{recurrence}.
}
\tag{7.3}
\]

More strongly,

\[
M(R)=O\!\left(\sqrt{\log R\,\log\log R}\right)
\tag{7.4}
\]

also implies recurrence (for large `R`, with the usual harmless regularization of small logarithms). Finite products of further iterated logarithms give further examples by the standard generalized harmonic-series test.

#### Proof

For every crossing edge in `E_r^\partial`, both adjacent faces lie inside `Lambda_{r+1}`, hence

\[
|\psi_q|\le \frac{M(r+1)}4.
\]

Therefore

\[
\Xi_r
\le
N_r\frac{M(r+1)^2}{8},
\]

so

\[
A_r
\le
(8r+4)\left(\frac12+2M(r+1)^2\right)
\le
24r\,[1+M(r+1)^2]
\tag{7.5}
\]

for `r>=1`. Equations (6.9) and (7.5) imply

\[
\boxed{
\operatorname{cap}_{L}(\{0\},B_R)
\le
\frac{24}{
\displaystyle\sum_{r=1}^{R-1}
\frac1{r[1+M(r+1)^2]}}
}
\tag{7.6}
\]

and of course (6.9) is stronger when the stream is angularly inhomogeneous.

If (7.1) or (7.2) holds, the capacities to the complements of increasing boxes tend to zero.

It remains to check irreducibility under the displayed hypotheses rather than hide it. Divergence of (7.2) forces each sign to occur arbitrarily far in each positive and negative tail of each line-sign sequence. Indeed, if for example `a_y` were eventually constant on the positive tail, then `|alpha_y|>=y-C`, whence `M(y)>=y-C` and the tail of (7.2) would be bounded by a constant multiple of `sum y^{-3}`, a contradiction. The other three tails are identical.

Given `u=(x,y)` and `v=(x',y')`, put `s=a_y` and `t=b_{x'}`. Choose a row `d` very far below both `y,y'` if `t=+1`, or very far above both if `t=-1`, with `a_d=-s`; such a row exists by the preceding tail property. Let `eta=sign(d-y)=-t`. Along the horizontal ray from `x` in direction `s`, choose a column `c` beyond `x'` in that direction with `b_c=eta`; again this exists arbitrarily far in that tail. Then the four directed segments

\[
(x,y)\to(c,y)\to(c,d)\to(x',d)\to(x',y')
\]

all follow legal line orientations. Thus the directed graph is strongly connected.

For an irreducible chain with invariant counting measure, vanishing capacity from one point to the complement of an exhaustion is the standard recurrence criterion; it is the same capacity framework used by Gaudilliere--Landim. Hence the walk is recurrent.

Finally, (7.3) makes the denominator in (7.6) dominate a constant multiple of `sum 1/(r log r)`, and (7.4) makes it dominate `sum 1/(r log r log log r)`. Both diverge. ∎

---

## 8. What happened to the proposed transient critical example

The run began by trying to realize the user's requested refutation route: a deterministic transient full Manhattan field with

\[
M(R)=O(\sqrt{\log R}).
\]

Claim 236 rules out that entire class. The `sqrt(log)` barrier in the previous **single-box supremum** estimate was partly an artifact: the correct object is cumulative annular resistance, not one worst sector constant at the terminal scale.

The theorem does **not** say that (7.1) or (7.2) is necessary. When the series converges, the present method is silent. In particular, no transient field at the first supercritical slowly varying scale is constructed here.

The current active exponent metric therefore honestly remains

\[
\eta_{\rm stream}^{\rm cert}=\frac12.
\]

The endpoint and iterated-log gains are real source-scope coverage but do not certify any fixed exponent `gamma>1/2`.

---

## 9. Section-B methods: exact outcomes

### #11 DUALIZE

I started from the nonreversible Thomson/flow side because a finite-energy escape object would prove transience. The useful reversal was to dualize the capacity min-max back onto a weighted primal test while retaining facewise stream weights. The supremum over the dual potential is solved exactly after (4.7), producing (5.3). This rules out the targeted critical transient family instead of constructing it.

### #24 FIND THE EXTREMAL OBJECT

Within square-radial test functions, the exact extremizer is not the ordinary logarithmic profile. Its shell drops are

\[
\delta_r\propto A_r^{-1},
\]

where `A_r` is the annular stream-energy cost. This is the discrete resistance profile and yields the exact bound (6.9).

### #29 ADD THE POINTS AT INFINITY

Passing the finite exhaustion to infinity identifies the real sufficient invariant:

\[
\mathcal R_\infty(\psi)
:=\sum_{r\ge1}A_r^{-1}.
\]

Infinite annular resistance forces zero escape capacity and recurrence. This is stronger than looking at a single terminal-scale `M(R)`.

---

## 10. Prior-art and source-status check — 17 September 2026

Fresh bounded queries included combinations of:

- `"randomly oriented Manhattan lattice" recurrence orientation fields deterministic stream function 2026`;
- `"stream function" recurrence Z^2 nonreversible random walk sector condition`;
- `"sqrt(log" recurrence nonreversible random walk stream function`;
- `"weighted sector condition" recurrence Markov chain capacity nonreversible`;
- `"cycle random walks" recurrence winding second moment Gaudilliere Landim`;
- `bounded cycle representation random environment Deuschel Kosters`;
- `Transient random walks on 2D-oriented lattices Guillotin-Plantard Le Ny`.

Primary/relevant literature recovered:

1. **Bou-Rabee--Peres (2026), arXiv:2609.07621v1.** Problem 3 remains explicitly stated. The source records counting-measure invariance, the simple-random-walk symmetric part, iid full-orientation transience, and alternating-environment recurrence.
2. **Gaudilliere--Landim (2014 / arXiv:1111.2445).** Their Theorem 2.4 gives the nonreversible capacity variational formula; Remark 3.3 permits the collapsed exterior normalization for the dual test; Lemma 2.6 is the global strong-sector capacity comparison. They also prove recurrence theorems for two-dimensional cycle random walks under a winding second-moment condition.
3. **Deuschel--Kosters (2008), AIHP 44, 574--591.** Their bounded-cycle representation gives a quenched invariance principle for a different nonreversible random-environment class. It does not state the deterministic annular stream criterion proved here.
4. **Guillotin-Plantard--Le Ny (2008).** Their model is partially oriented (vertical edges remain bidirectional) and supplies transience criteria generated by dynamical systems; it is not the exact fully oriented source model treated by Claim 236.

The bounded dated searches did not locate an explicit published theorem matching the exact criterion (7.1), the envelope criterion (7.2), or the deterministic full-Manhattan endpoint (7.3). This is **not** proof of publication novelty. The correct label remains `PUBLICATION-NOVELTY-UNVERIFIED`.

No later source-matching resolution of the full Bou-Rabee--Peres Problem 3 surfaced in the bounded dated search. That is negative search evidence only, not an openness certificate beyond the source and located literature.

---

## 11. Directed second audit: P04 / I0101

The newest P04 report is a thinking-only stuck recovery and creates no new mathematical claim. I therefore audited a concrete earlier P04 claim not previously audited by P03:

`P04-I0101-REGULAR-S3-BLOCK-BERNOULLI-13` from

`proofnet24/P04-closure-local-paley/runs/2026-09-17/2026-09-17T03-14-36Z__run-report.md`,

creation commit `8b86baea1dcc5c52ee850c176c6f25906ad9acbf`, blob `08fa7baa1f5c9eb8f6046a21f6bc6449fabedc46`.

The claim is: for `p == 5 (mod 24)`, a fixed free anharmonic orbit `Gy`, and every prescribed six-bit sign pattern `epsilon`, the number `N_y(epsilon)` of source vertices satisfying the two localization signs and those six target-orbit Legendre signs obeys

\[
\left|N_y(\varepsilon)-\frac{p}{256}\right|
\le \frac{769}{256}\sqrt p+8,
\tag{11.1}
\]

and hence orbit-block degrees have the `Binomial(6,1/2)` row law up to `O(sqrt p)` discrepancy.

### Independent derivation

For `p == 5 (mod 24)`, the anharmonic `S_3` action is free on the two-localized vertex set. Independently: nontrivial order-two fixed points are conjugate to `1/2`, which is excluded because `chi(2)=-1` for `p == 5 (mod 8)`; order-three fixed points satisfy `x^2-x+1=0`, whose discriminant `-3` is nonsquare for `p == 5 (mod 12)`. Thus the six points `g y` are distinct and, because they lie in the localized vertex set, are also distinct from `0,1`.

Away from these eight roots, the exact indicator of a prescribed sign pattern is

\[
2^{-8}(1+\chi(x))(1+\chi(x-1))
\prod_{g\in S_3}(1+\varepsilon_g\chi(x-g y)).
\tag{11.2}
\]

Expanding (11.2) gives one empty term `p`; every one-factor character sum vanishes; and every `r>=2` term is the quadratic character sum of a squarefree degree-`r` polynomial, hence has absolute value at most `(r-1)sqrt(p)` by the standard Weil bound. Therefore the total nonempty error is at most

\[
2^{-8}\sum_{r=2}^{8}\binom8r(r-1)\sqrt p
=\frac{769}{256}\sqrt p.
\tag{11.3}
\]

At the eight roots, (11.2) is not a literal sign indicator because `chi(0)=0`; removing those points changes the count by at most eight, which proves (11.1).

Summing (11.1) over the `binom(6,k)` patterns with exactly `k` positive target signs and dividing by the six vertices in each free source orbit gives

\[
\#\{i\ne j:k_{ij}=k\}
=
\frac{\binom6k}{64}\,q+O(\sqrt p),
\qquad q=\frac{p-5}{24},
\]

because simultaneous anharmonic action only permutes the six target coordinates. This is exactly P04's (6.2), including the harmless `O(1)` difference between `p/24` and `q`.

Verdict:

`P03-AUDIT-P04-I0101-REGULAR-S3-BLOCK-BERNOULLI-237 = PASS (CLAIM-SCOPED)`.

This audit certifies only the local six-bit counting theorem. It does **not** certify P04's global Lovasz-theta conjecture, its finite-prime dual certificates, or the missing global trivial-sector cancellation.

---

## 12. Exact remaining obligation and next attack

Claim 236 shows that terminal-scale `sqrt(log)` was not a transience threshold. The remaining source-level problem is still enormous: characterize recurrence/transience for arbitrary line-orientation fields.

For the stream route, the precise next obstruction is:

\[
\boxed{
\sum_r A_r^{-1}<\infty
\quad\text{does not currently imply either recurrence or transience.}
}
\]

The present theorem is only sufficient. Its use of a square-radial potential can also be wasteful when large stream values occupy a sparse angular set. A stronger route should either:

1. optimize over genuinely two-dimensional potentials and replace annular total squared-stream mass by a narrower bottleneck functional; or
2. construct a deterministic transient field with the smallest possible growth of that bottleneck, thereby establishing a real sharpness datum.

The next Section-B triple is:

- **#3 PROVE SOMETHING STRONGER:** replace the square-radial sufficient criterion by a network/metric criterion allowing the potential to route around high-stream faces;
- **#13 FIND WHAT ONLY INCREASES:** identify a monotone effective resistance/capacity functional under adding oriented-line defects or enlarging the stream obstruction;
- **#28 REPLACE FOR ALL WITH TYPICAL:** first control fields where only a vanishing angular fraction of each annulus has large `|psi|`, rather than paying the full worst or total annular cost.

Do not return to the already-settled periodic, bounded-stream, or sub-sqrt-log proofs, and do not enter I0004.

---

## 13. Cumulative I0003 claim ledger

- `P03-I0003-PERIODIC-CLASSIFICATION` — **KNOWN / VERIFIED TRANSFER**: doubly periodic field recurrent iff both period means vanish; otherwise ballistic/transient.
- `P03-I0003-BOUNDED-DISCREPANCY-SECTOR-232` — **KNOWN / VERIFIED TRANSFER**: bounded two-sided line discrepancies imply bounded face stream, global strong-sector comparison, recurrence.
- `P03-I0003-SUBSQRTLOG-STREAM-234` — **PROVED / PARTIAL / PUBLICATION-NOVELTY-UNVERIFIED**: `M(R)=o(sqrt(log R))` implies recurrence via localized sector capacity.
- `P03-I0003-ANNULAR-STREAM-RESISTANCE-236` — **PROVED / PARTIAL / PUBLICATION-NOVELTY-UNVERIFIED**: divergent annular resistance `sum A_r^{-1}=infinity` implies recurrence; in particular the full endpoint `M(R)=O(sqrt(log R))`, and larger iterated-log envelopes such as `O(sqrt(log R log log R))`, are recurrent.
- Broad Bou-Rabee--Peres Problem 3 — **OPEN / PARTIAL**.

The active metric remains `eta_stream^cert=1/2`; the new theorem is endpoint/slowly-varying coverage rather than a fixed-power exponent increase.

---

## 14. `ledger_delta` for P26 only

```text
P03 | Bou-Rabee--Peres 2026 arXiv:2609.07621v1 §7 Problem 3 / I0003 | active metric eta_stream^cert 1/2 -> 1/2 NO MOVEMENT, unchanged streak 0 -> 1; periodic_scope_certified=1 and bounded_discrepancy_scope_certified=1 retained | PARTIAL / broad source OPEN | B11/B24/B29 | new theorem P03-I0003-ANNULAR-STREAM-RESISTANCE-236=PROVED/PARTIAL/PUBLICATION-NOVELTY-UNVERIFIED: for face stream psi, annular coefficients A_r=(8r+4)/2+16 Xi_r with Xi_r=sum over square-boundary crossing edges of the squared streams of the two adjacent faces, divergence sum_r 1/A_r implies recurrence; exact finite-volume cap bound cap_L({0},Lambda_R^c) <= [sum_{r<R}1/A_r]^{-1}; envelope corollary cap <= 24/[sum_{r<R}1/(r(1+M(r+1)^2))], hence M(R)=O(sqrt(log R)) and even O(sqrt(log R loglog R)) imply recurrence; targeted critical-scale transient route ruled out; no checker (analytic theorem) | directed audit P03-AUDIT-P04-I0101-REGULAR-S3-BLOCK-BERNOULLI-237=PASS claim-scoped | next B3/B13/B28
```

P03 did not edit any shared root ledger or peer file.

---

## 15. Runtime / delivery limitations

The requested GPT-6 / maximum setting remains prompt-only in the exposed scheduler; no model selector, reasoning selector, authenticated runtime-routing receipt, or guaranteed thinking-duration control is exposed. Actual model/effort is therefore reported exactly as in the first line.

No email, Gmail, Drive, public posting, paid compute, permission changes, or extra schedules were used. No external script was executed. The only computation used internally was a trivial symbolic sanity check of the four-vertex identity in (4.2); the theorem does not depend on a computational certificate.

**End of complete run report.**
