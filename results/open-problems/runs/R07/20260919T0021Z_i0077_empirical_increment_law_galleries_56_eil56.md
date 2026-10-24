Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: `55 -> 56` genuinely distinct nonparabolic shape families; Section-B moves actually used: #3 PROVE SOMETHING STRONGER, #18 SAY IT IN ANOTHER LANGUAGE, #19 MAKE IT AN ALGORITHM.**

# R07 CLOSABLE OUTSIDE — run 56: empirical increment-law portal galleries

Run date: 2026-09-19 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Target: Burdzy--Scheutzow, *Forward Brownian Motion*, arXiv:1302.6958v4 / PTRF 160 (2014), Problem 7.8 / intake I0077.  
Delivery: private GitHub only. No email, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

Overall source status remains **PARTIAL**. New claims T77/T78 below are **SELF_CHECK_ONLY** pending the required two independent OTHER-track audits. Publication novelty remains **UNVERIFIED**.

## 1. Continuity, admission, ownership, and recovered state

I continued from the newest complete R07 report rather than restarting:

`runs/R07/20260918T2322Z_i0077_quartic_signature_portal_galleries_55_qs55.md`.

Before new mathematics I re-read/recovered the current repository state from:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md` and the controlling owner directive;
- canonical reservation `operations/claims/I0077.md`;
- the searchable R07/I0077 attempt chain, including the immutable KPZ handoff and all recoverable shape reports;
- newest neighboring R15 work, which preserves Burdzy--Scheutzow Problem 7.2 / I0076 as a distinct retired-handoff target and is now on successor work;
- targeted intake/attempt searches for `I0077`, `1302.6958`, `Problem 7.8`, the exact source wording, and empirical/dyadic-increment keywords.

`INDEX.md` / `RANKING.md` settle Burdzy--Scheutzow Problem 7.5, not 7.8. `POSTED.md` contains no exact Problem-7.8 closure. The canonical claim still says `PENDING_ADMISSION, not READY` while reserving I0077 exclusively to R07. I preserve that shared operational label and do not edit shared roots. The old R07 KPZ route remains preserved by immutable handoff and is not reopened or deleted.

The fixed metric is unchanged:

> number of genuinely distinct nonparabolic space-time shape families for which R07 has a complete source-appropriate theorem, modulo the frozen convention that Brownian rescaling/reflection/translation and mere parameter changes inside one structural family do not create new families.

Entering metric: **55**.  
Entering unchanged count: **0**.

Run 53 separated traces whose total quadratic variation is non-Brownian. Run 54 separated traces whose total quadratic variation is Brownian but whose local quadratic clock is non-Brownian. Run 55 crossed that boundary by matching the full local quadratic clock but separating the normalized fourth microscopic moment (`7/3` instead of Brownian `3`). Its explicit next frontier was to stop adding moments and inspect the whole empirical law of normalized microscopic increments. This run does exactly that.

## 2. Primary source benchmark rechecked

The primary Burdzy--Scheutzow PDF was re-read, including Definition 2.1, Theorem 4.3, and the open-problem page.

Definition 2.1 gives random witness times `S_j -> -infinity` for an FBM `X` such that, for each fixed witness index,

\[
B^{(j)}_t=X_{S_j+t}-X_{S_j},\qquad t\ge0,
\tag{2.1}
\]

is an unconditional standard Brownian motion.

Theorem 4.3 is the exact three-clause parabolic theorem governed by the killed Ornstein--Uhlenbeck exponent `lambda_0(c_1,c_2)`: escape for `lambda_0>=1`, existence of a decomposable FBM satisfying the asymptotic parabolic bounds for `lambda_0<=1`, and exact all-negative-time confinement when `c_1<=0<=c_2` and `lambda_0<1`.

Problem 7.8 is exactly:

> Can one generalize Theorem 4.3 from parabolas to other space-time shapes?

The following forward-Levy sentence is Problem 7.9 and is not part of I0077.

## 3. Fresh current-literature / prior-art pass

Fresh bounded searches on 2026-09-19 used the exact source title, arXiv id, exact Problem-7.8 wording, later-author/citation queries, and combinations of `dyadic increments`, `empirical distribution`, `Takagi`, `Bernoulli convolution`, `Faber-Schauder`, and Brownian high-frequency increments.

Relevant prior art recovered:

1. X. Han, A. Schied, Z. Zhang, *A limit theorem for Bernoulli convolutions and the Phi-variation of functions in the Takagi class*, arXiv:2102.02745. Their proof technology explicitly turns dyadic Takagi increments into Bernoulli-convolution limits. This is the nearest conceptual precedent for the deterministic empirical-increment side of the present construction.
2. D. Kim, *Pathwise integration beyond Young via Faber--Schauder energy spaces*, arXiv:2606.13331 (2026), and recent related Faber--Schauder variation work. These reinforce that dyadic coefficient/increment signatures are a natural pathwise language beyond Hölder and ordinary variation.
3. The classical empirical-distribution / bounded-test-function law of large numbers for iid Gaussian increments supplies the Brownian benchmark. The new point needed for FBM is not that fixed-phase fact but the simultaneous-in-phase upgrade proved below.

The bounded current searches did **not** surface an accessible later paper explicitly resolving exact Burdzy--Scheutzow Problem 7.8 or stating T77/T78 below. That is negative bounded evidence only; it is **not** a worldwide novelty certificate.

## 4. Counterexample-first screen: matching finitely many Brownian moments is not enough

Run 55 suggested a possible stopping principle:

> perhaps once a deterministic trace has Brownian local quadratic variation and Brownian local quarticity, the dyadic roughness signature has become indistinguishable from Brownian motion for the purposes of a gate obstruction.

This is false. One can match the second and fourth normalized microscopic moments **exactly in the limit on every fixed dyadic subinterval**, while forcing the entire empirical normalized-increment law to converge to a compactly supported non-Gaussian distribution.

This falsifies a proposed stronger extension mechanism. It does **not** refute the source's open-ended Problem 7.8.

## 5. Move #18 — say it in another language: from moments to empirical measures

For `Q in C([0,1])`, define its level-`N` empirical normalized-increment measure

\[
\nu_N^Q
=2^{-N}\sum_{k=0}^{2^N-1}
\delta_{\,2^{N/2}[Q((k+1)2^{-N})-Q(k2^{-N})]}.
\tag{5.1}
\]

Quadratic variation tests only the second moment of `nu_N^Q`; realized quarticity tests only the fourth. Brownian motion has a much stronger microscopic signature: for a fixed phase, these normalized increments are iid `N(0,1)`, so every bounded continuous test function sees the standard Gaussian law.

For the FBM application the phase is random. The correct invariant is therefore not just weak convergence at phase zero, but a Brownian empirical-law theorem that holds simultaneously at every starting phase before the witness is selected.

## 6. Move #3 — a stronger Brownian theorem than any fixed moment

Let `phi:R->R` be bounded and Lipschitz. For standard Brownian motion `B`, put, with `n=2^N`,

\[
A_N(\theta;\phi)
=\frac1n\sum_{k=0}^{n-1}
\phi\!\left(\sqrt n\,[B_{\theta+(k+1)/n}-B_{\theta+k/n}]\right).
\tag{6.1}
\]

### Lemma 6.1 — uniform empirical test-function law over all phases

For every bounded Lipschitz `phi` and every finite `A`, almost surely,

\[
\boxed{
\sup_{0\le\theta\le A}
\left|A_N(\theta;\phi)-\mathbb E\phi(Z)\right|
\longrightarrow0,
\qquad Z\sim N(0,1).
}
\tag{6.2}
\]

One probability-one event can be chosen so that (6.2) holds for every integer `A>=1` simultaneously.

### Proof

Fix `A`, let `n=2^N`, and use the phase mesh

\[
D_N=\{j\delta_N:0\le j\delta_N\le A+\delta_N\},
\qquad \delta_N=n^{-6}.
\tag{6.3}
\]

For fixed `theta`, the `n` standardized increments in (6.1) are iid `N(0,1)`. If `|phi|<=M`, Hoeffding's inequality gives, for every `epsilon>0`,

\[
\Pr\{|A_N(\theta;\phi)-\mathbb E\phi(Z)|>\epsilon\}
\le 2\exp(-c_{M,\epsilon}n).
\tag{6.4}
\]

The mesh has `O_A(n^6)` points, so the union bound is summable in `N`. Borel--Cantelli yields uniform convergence on `D_N`.

For arbitrary `theta in [0,A]`, choose `theta' in D_N` with `|theta-theta'|<=delta_N`. Brownian modulus of continuity on `[0,A+2]` gives eventually

\[
\omega_B(r)\le C\sqrt{r\log(1/r)}.
\tag{6.5}
\]

For every `k`, the two standardized increments differ by at most

\[
2\sqrt n\,\omega_B(\delta_N)
=O\!\left(n^{-5/2}\sqrt{\log n}\right).
\tag{6.6}
\]

If `L_phi` is the Lipschitz constant, then

\[
|A_N(\theta;\phi)-A_N(\theta';\phi)|
\le 2L_\phi\sqrt n\,\omega_B(\delta_N)
\longrightarrow0.
\tag{6.7}
\]

This extends the mesh result to all phases. Intersect the resulting probability-one events over integer `A`. QED.

The important quantifier order is explicit: (6.2) is proved pathwise for **every phase** before any random FBM witness time is introduced.

## 7. T77 — empirical-increment-law gate obstruction

### Theorem T77

Let `Q in C([0,1])`. Assume that there is a bounded Lipschitz function `phi` and a number `ell` such that

\[
\frac1{2^N}\sum_{k=0}^{2^N-1}
\phi\!\left(
2^{N/2}[Q((k+1)2^{-N})-Q(k2^{-N})]
\right)
\longrightarrow \ell,
\tag{7.1}
\]

with

\[
\ell\ne\mathbb E\phi(Z),\qquad Z\sim N(0,1).
\tag{7.2}
\]

Suppose a deterministic space-time shape has arbitrarily far unit gate blocks: there are `a_m -> infinity` and constants `c_m` such that

\[
K(a_m+s)\subset\{c_m+Q(s)\},
\qquad 0\le s\le1,
\tag{7.3}
\]

while the fibers between those blocks are arbitrary. Then every forward Brownian motion `X` satisfies

\[
\boxed{
\Pr\!\left(
\exists R<\infty:\ X_{-u}\in K(u)\ \forall u\ge R
\right)=0.
}
\tag{T77}
\]

### Proof

Work on the countable intersection, over FBM witness indices `j`, of the probability-one events from Lemma 6.1 applied to the unconditional standard Brownian futures `B^{(j)}` in (2.1). This is still a probability-one event.

Assume eventual confinement occurs. Choose a gate block `[a_m,a_m+1]` lying beyond the eventual-confinement age. Because `S_j -> -infinity`, choose a witness index `j` with

\[
S_j\le -a_m-1.
\tag{7.4}
\]

In the Brownian future from `S_j`, the chronological gate interval `[-a_m-1,-a_m]` begins at the (random) phase

\[
\theta=-a_m-1-S_j\ge0.
\tag{7.5}
\]

Along that interval, age runs backward through the gate, so (7.3) forces, up to an additive constant, the time-reversed trace

\[
\widetilde Q(r)=Q(1-r),\qquad 0\le r\le1.
\tag{7.6}
\]

Its normalized dyadic increments are the negatives of those of `Q`, in reverse order. Thus if `check phi(x)=phi(-x)`, confinement implies

\[
A_N(\theta;\check\phi)
\longrightarrow \ell.
\tag{7.7}
\]

But Lemma 6.1, valid at this random phase because it is simultaneous over all phases, gives

\[
A_N(\theta;\check\phi)
\longrightarrow \mathbb E\check\phi(Z)
=\mathbb E\phi(Z),
\tag{7.8}
\]

using symmetry of the standard Gaussian. This contradicts (7.2). QED.

### Empirical-measure corollary

If `nu_N^Q => mu` weakly and `mu != N(0,1)`, then bounded-Lipschitz functions separate probability measures, so some `phi` satisfies (7.1)--(7.2). Hence T77 applies. This is the promised replacement of a hierarchy of moment tests by the entire one-step microscopic increment law.

## 8. Move #19 — make the moment-matched non-Gaussian trace algorithmic

I now construct a deterministic continuous trace whose local quadratic clock and local quarticity are both Brownian, but whose empirical normalized increments have a compact non-Gaussian limiting law.

Let `q_*` be the unique root in

\[
\left(\frac{12}{25},\frac{49}{100}\right)
\tag{8.1}
\]

of

\[
\boxed{
E(q)=18q^3-(74+2\sqrt2)q^2+(45-6\sqrt2)q+3\sqrt2-6=0.
}
\tag{8.2}
\]

Numerically,

\[
q_*\approx0.4823713078159667502.
\tag{8.3}
\]

Set

\[
\delta=\sqrt{2-4q_*},\qquad
 a=\frac{\sqrt2-\delta}{2},\qquad
 b=\frac{\sqrt2+\delta}{2},\qquad
 c=\sqrt{q_*}.
\tag{8.4}
\]

Then

\[
a+b=\sqrt2,\qquad ab=q_*,\qquad 0<a<b<1,
\tag{8.5}
\]

with approximate values

\[
a\approx0.574333696,
\quad b\approx0.839879867,
\quad c\approx0.694529559.
\tag{8.6}
\]

Define a binary normalized-increment tree by

\[
x_{0,0}=0,
\tag{8.7}
\]

and, recursively,

\[
\boxed{
\begin{aligned}
x_{N+1,2k}&=a x_{N,k}+c,\\
x_{N+1,2k+1}&=b x_{N,k}-c.
\end{aligned}}
\tag{8.8}
\]

Because the two children satisfy

\[
2^{-(N+1)/2}(x_{N+1,2k}+x_{N+1,2k+1})
=2^{-N/2}x_{N,k},
\tag{8.9}
\]

the prescription

\[
Q_0((k+1)2^{-N})-Q_0(k2^{-N})
=2^{-N/2}x_{N,k},
\tag{8.10}
\]

is exactly consistent across all dyadic refinements. Since `b<1`,

\[
|x_{N,k}|\le \frac{c}{1-b}<5
\tag{8.11}
\]

uniformly. Therefore the dyadic values extend uniquely to a continuous `Q_0` on `[0,1]`, with `Q_0(0)=Q_0(1)=0`.

Under uniform choice of a leaf at depth `N`, `x_{N,k}` has the same law as the affine recursion

\[
X_{n+1}=A_{n+1}X_n+C_{n+1},
\tag{8.12}
\]

where independently at each step

\[
(A,C)=
\begin{cases}
(a,c),&1/2,\\
(b,-c),&1/2.
\end{cases}
\tag{8.13}
\]

Both affine maps are strict contractions. Hence the leaf empirical measures converge to the unique compactly supported stationary law `mu` of (8.12).

## 9. Why the root equation matches Brownian second and fourth moments

Write `m_r=E_mu[X^r]`. Symmetry of the signs in `C` and `a+b=sqrt(2)` give `m_1=0`. Moreover

\[
\mathbb E A^2=1-q_*,\qquad c^2=q_*,
\tag{9.1}
\]

so the stationary variance recursion gives

\[
m_2=(1-q_*)m_2+q_*,
\qquad\boxed{m_2=1.}
\tag{9.2}
\]

For the third moment, with

\[
D=1-\sqrt2\left(1-\frac32q_*\right),
\tag{9.3}
\]

one obtains

\[
m_3=-\frac{3c\delta}{\sqrt2\,D}.
\tag{9.4}
\]

Also

\[
\mathbb E A^4=2-4q_*+q_*^2,
\qquad
1-\mathbb E A^4=-1+4q_*-q_*^2.
\tag{9.5}
\]

Expanding the fourth stationary moment equation and imposing `m_4=3` reduces **exactly** to (8.2). Hence the chosen root gives

\[
\boxed{m_2=1,\qquad m_4=3.}
\tag{9.6}
\]

The exact checker independently verifies the algebraic reduction from the stationary fourth-moment recursion to `E(q)=0`, proves by exact signs that `E` has a unique root in (8.1), and verifies the contraction/denominator conditions.

For every fixed dyadic interval `I`, descendants of its root obey the same contractive affine recursion, only from a different initial state. Consequently their empirical law still converges to `mu`, and therefore

\[
\boxed{
V_N(Q_0;I)\longrightarrow |I|,
\qquad
\mathcal K_N(Q_0;I)\longrightarrow 3|I|.
}
\tag{9.7}
\]

Thus `Q_0` has the complete Brownian local quadratic clock and the complete Brownian local quarticity along the dyadic filtration.

Yet `mu` is not Gaussian: by (8.11) its support lies in a compact interval. In fact the exact root bracket gives `c<7/10`, `b<17/20`, so

\[
\operatorname{supp}\mu\subset[-14/3,14/3]\subset[-5,5].
\tag{9.8}
\]

## 10. Roughify without changing the empirical law or either matched moment

The bounded normalized increments make `Q_0` `1/2`-Hölder, so using it directly could overlap an earlier critical-Hölder gate family. As in run 55, add a finite-variation perturbation at Brownian logarithmic modulus scale, but preserve both endpoints:

\[
S(0)=0,
\qquad
S(t)=\sqrt{t\log(e/t)}-t,
\quad 0<t\le1.
\tag{10.1}
\]

Then `S(0)=S(1)=0`, `S` has finite total variation, and

\[
\frac{S(t)}{\sqrt t}\to\infty
\quad(t\downarrow0),
\tag{10.2}
\]

so

\[
Q=Q_0+S
\tag{10.3}
\]

is not `1/2`-Hölder.

For every bounded 1-Lipschitz `phi`, on the level-`N` dyadic mesh,

\[
\begin{aligned}
&\left|
\frac1{2^N}\sum_k \phi(2^{N/2}\Delta_kQ)
-
\frac1{2^N}\sum_k \phi(2^{N/2}\Delta_kQ_0)
\right|\\
&\qquad\le
2^{-N/2}\sum_k|\Delta_kS|
\le 2^{-N/2}\,TV(S)\to0.
\end{aligned}
\tag{10.4}
\]

Hence `Q` has the same limiting empirical normalized-increment law `mu`.

The BV perturbation also leaves (9.7) unchanged. For quadratic variation this follows from `sum (Delta S)^2 -> 0` and Cauchy--Schwarz. For quarticity, use `|Delta Q_0|<=5*2^{-N/2}`, the bound

\[
\max_k|\Delta_kS|
=O\!\left(\sqrt{2^{-N}N}\right),
\tag{10.5}
\]

and expand `(Delta Q_0+Delta S)^4`; every term containing `Delta S` tends to zero after the `2^N` quarticity normalization. The same argument works on each fixed dyadic subinterval. Therefore

\[
\boxed{
V_N(Q;I)\to|I|,
\qquad
\mathcal K_N(Q;I)\to3|I|
\quad\text{for every dyadic }I.
}
\tag{10.6}
\]

So runs 53, 54, and 55 are all silent on this trace.

To remove even the simplest odd-moment separator, symmetrize the entire rough trace. Define

\[
H(t)=
\begin{cases}
2^{-1/2}Q(2t),&0\le t\le1/2,\\
-2^{-1/2}Q(2t-1),&1/2\le t\le1.
\end{cases}
\tag{10.7}
\]

Because `Q(0)=Q(1)=0`, this is continuous and satisfies `H(0)=H(1)=0`. At every dyadic level `N>=1`, the normalized increments of `H` are exactly one copy of the level-`N-1` normalized increments of `Q` and one reflected copy. Thus their empirical law converges to

\[
\mu_{\rm sym}=\tfrac12(\mu+\check\mu).
\tag{10.8}
\]

The limit is compactly supported and non-Gaussian, but now it is symmetric. Hence its first five Gaussian moments are matched through the information used here:

\[
\boxed{m_1=0,\quad m_2=1,\quad m_3=0,\quad m_4=3,\quad m_5=0.}
\tag{10.9}
\]

Moreover the scaling in (10.7) preserves the Brownian local quadratic clock and local quarticity on every dyadic interval: intervals below level one map to dyadic intervals for `Q`, while the whole interval is the equal mixture of the two halves. The logarithmic singularity at zero also persists, so `H` is still not `1/2`-Hölder. The final gate trace below is `H`, not `Q`.

## 11. An explicit bounded Lipschitz separator

Define

\[
\phi_*(x)=\min\{1,(|x|-5)_+\}.
\tag{11.1}
\]

This is bounded and 1-Lipschitz. The limiting empirical law of `H` is supported in `[-5,5]`; equivalently, using (10.4) and the exact symmetrization,

\[
\frac1{2^N}\sum_k\phi_*(2^{N/2}\Delta_kH)\longrightarrow0.
\tag{11.2}
\]

But for `Z~N(0,1)`,

\[
\mathbb E\phi_*(Z)>0
\tag{11.3}
\]

because `P(|Z|>6)>0`. Thus T77 applies with `ell=0` without needing any unquantified measure-separation step. In particular, the separator survives even after matching the Gaussian mean, variance, skewness, and fourth moment.

## 12. T78 — moment-matched empirical-law portal gallery

Take superexponentially sparse gate starts

\[
a_m=2^{2^m},\qquad m\ge1.
\tag{12.1}
\]

On each gate block impose the singleton trace

\[
K(a_m+s)=\{H(s)\},
\qquad0\le s\le1.
\tag{12.2}
\]

Since `H(0)=H(1)=0`, connect successive gate blocks through gaps whose fibers widen continuously from `{0}` to all of `R`, contain a full-space middle-third portal slab, and then narrow continuously back to `{0}`. Concretely, in the gap

\[
G_m=(a_m+1,a_{m+1}),\qquad L_m=a_{m+1}-a_m-1,
\tag{12.3}
\]

write `x=(u-a_m-1)/L_m` and set the extended radius

\[
R_m(x)=
\begin{cases}
\dfrac{x}{1/3-x},&0\le x<1/3,\\
+\infty,&1/3\le x\le2/3,\\
\dfrac{1-x}{x-2/3},&2/3<x\le1.
\end{cases}
\tag{12.4}
\]

For finite `R_m`, let `K(u)=[-R_m(x),R_m(x)]`; for `R_m=+infinity`, let `K(u)=R`. Before the first gate set `K(u)={0}`. The resulting space-time set

\[
\mathcal E_*=
\{(-u,y):u\ge0,\ y\in K(u)\}
\tag{12.5}
\]

is closed: finite-radius boundary functions are continuous; at the portal interfaces the radius tends to infinity; at gate endpoints it tends to zero and matches `H(0)=H(1)=0`.

Every gap contains a literal full-space slab of length

\[
\frac{L_m}{3}\longrightarrow\infty.
\tag{12.6}
\]

Nevertheless T77 and (11.2)--(11.3) give

\[
\boxed{
\Pr\!\left(
\exists R:\ (-u,X_{-u})\in\mathcal E_*
\ \forall u\ge R
\right)=0
}
\tag{T78}
\]

for every FBM `X`.

This is the metric-point-56 family: **moment-matched self-affine empirical-law portal galleries**.

## 13. Why this is a genuinely new family under the frozen equivalence rule

This is not counted again by changing `q`, a scale, or a portal width. The whole construction with the unique moment-matching root `q_*` is one family.

The structural separator from recent R07 families is microscopic and invariant under the frozen Brownian scaling/reflection/translation operations:

1. **Run 53:** total quadratic variation is non-Brownian. Here total QV is Brownian.
2. **Run 54:** local quadratic clock is non-Brownian. Here for every fixed dyadic `I`, `V_N(H;I)->|I|`.
3. **Run 55:** quarticity differs (`7/3` versus `3`). Here for every fixed dyadic `I`, local quarticity is exactly Brownian in the limit: `K_N(H;I)->3|I|`.
4. **Earlier critical-Hölder gate families:** the present trace is not `1/2`-Hölder because the singularity in (10.2) survives (10.7).
5. **BV gate families:** `H` has positive Brownian quadratic variation and hence is not BV.
6. **Present obstruction:** the first surviving separator is the **full one-step empirical normalized-increment law**, witnessed explicitly by `phi_*`.

Thus no constant Brownian rescaling, reflection, translation, time reversal, or mere parameter change converts the point-56 microscopic signature into the point-55 signature.

## 14. Exact self-check

Artifacts:

- `artifacts/R07/20260919T0021Z_empirical_increment_law_check.py`
- `artifacts/R07/20260919T0021Z_empirical_increment_law_check.out`

The checker uses only Python's standard library and exact arithmetic in `Q(sqrt(2))`. It verifies:

- `E(12/25)>0` and `E(49/100)<0` exactly;
- strict decrease of `E` on the bracket, hence the unique root `q_*`;
- the exact reduction of the stationary fourth-moment condition `m_4=3` to `E(q)=0`;
- the stationary variance identity `m_2=1`;
- positivity of the stationary-moment denominators on the bracket;
- contraction of both affine branches.

The archived output ends

`ALL_EXACT_CHECKS_PASS`.

This is a **self-check**, not an external audit. The Brownian theorem and the all-scale deterministic arguments are proved on the page rather than delegated to the script.

## 15. Honest status and remaining closure obligations

- T77: **SELF_CHECK_ONLY / unaudited theorem-sized claim**.
- T78: **SELF_CHECK_ONLY / unaudited explicit family**.
- Independent OTHER-track audits: **0/2**.
- Source Problem 7.8: **PARTIAL**, not closed.
- Publication novelty: **UNVERIFIED**.
- Canonical claim operational state: still `PENDING_ADMISSION, not READY`.
- No shared root was edited.

The fresh literature pass positively found nearby Takagi/Bernoulli-convolution and Faber--Schauder pathwise machinery, which must be cited as prior art for the deterministic dyadic side. It did not positively find this FBM gate theorem. A negative bounded search is not a novelty certificate.

## 16. Next frontier

The one-step empirical law is now exhausted as an invariant. The next genuinely harder boundary is a deterministic trace whose **one-step normalized increment empirical law is exactly Gaussian**, while adjacent or longer increment blocks have the wrong dependence structure. Brownian motion has not only Gaussian one-step marginals but iid microscopic blocks. A next route should therefore test, for bounded Lipschitz `Phi:R^r->R`, the empirical block law

\[
\frac1n\sum_k
\Phi(\sqrt n\,\Delta_kQ,\ldots,\sqrt n\,\Delta_{k+r-1}Q)
\tag{16.1}
\]

against the iid Gaussian `r`-block law, uniformly in Brownian phase. This would strictly subsume the present one-step theorem rather than merely adding sixth and eighth moments.

No theorem is claimed for that frontier in this run.

## 17. Model / scheduler control report

The exposed task-control surface still does not provide a binding model-family selector, reasoning-effort selector, guaranteed-duration field, or authenticated applied-model receipt. Therefore GPT-6/maximum remains prompt-only, and this report truthfully records GPT-5.6 Sol / reasoning UNVERIFIED rather than claiming otherwise.

No scheduler change was attempted: the current owner instruction explicitly prohibits scheduler changes from this worker. The historical `You cannot modify this task` response for P26 is recorded as an authorization-context issue; a later authorized context succeeded. For any task that still rejects edits, the legitimate workaround is the owning/authorized account or workspace, an authorized ownership/admin correction, or platform support. Do not bypass permissions or create a duplicate schedule.

## 18. Structured ledger delta

```yaml
ledger_delta:
  track: R07
  run_id: 20260919T0021Z_i0077_empirical_increment_law_galleries_56_eil56
  source: "Burdzy--Scheutzow, Forward Brownian Motion, Problem 7.8 / I0077"
  target: "generalize Theorem 4.3 from parabolic regions to genuinely distinct nonparabolic space-time shape families"
  fixed_metric: "number of genuinely distinct nonparabolic shape families with a complete source-appropriate theorem under the frozen equivalence convention"
  metric_before: 55
  metric_after: 56
  movement: +1
  unchanged_streak_after: 0
  section_B_moves: [3, 18, 19]
  new_claims:
    - id: T77
      label: "empirical-increment-law gate obstruction"
      status: SELF_CHECK_ONLY
    - id: T78
      label: "moment-matched self-affine empirical-law portal gallery"
      status: SELF_CHECK_ONLY
  exact_artifacts:
    - artifacts/R07/20260919T0021Z_empirical_increment_law_check.py
    - artifacts/R07/20260919T0021Z_empirical_increment_law_check.out
  independent_other_track_audits: "0/2"
  source_status: PARTIAL
  publication_novelty: UNVERIFIED
  admission_state: "PENDING_ADMISSION, not READY"
  next_frontier: "joint/block empirical normalized-increment law after matching the one-step Gaussian law"
```
