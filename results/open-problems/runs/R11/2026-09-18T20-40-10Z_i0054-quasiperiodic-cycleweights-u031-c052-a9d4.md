Model: GPT-5.6 Sol. Reasoning: UNVERIFIED runtime level; GPT-6 / maximum was requested in prompt text, but the exposed runtime/task-control surface has no binding model-family selector, reasoning-effort selector, guaranteed-duration control, or authenticated completed-run routing receipt, so GPT-6 / maximum is not verified or claimed. Metric movement: `51 -> 52`; Section-B methods actually used: **#9 RANDOMIZE, #18 SAY IT IN ANOTHER LANGUAGE, #24 FIND THE EXTREMAL OBJECT**.

# R11 / I0054 — quasiperiodic finite-Fourier cycle weights and C052

Date: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Track: R11, CLOSABLE OUTSIDE.  
Source: David J. Aldous and Svante Janson, *The Critical Beta-splitting Random Tree II: Overview and Open Problems*, arXiv:2303.02529v3, Open Problem 18.  
Status after this run: **PARTIAL at source/campaign level, not CLOSED**.  
New author-side claims: `R11-I0054-U031 = PROVED_AUTHOR_SIDE`; `R11-I0054-C052 = PROVED_AUTHOR_SIDE under the frozen equivalence convention`.

No email, Drive, public posting, purchase, permission change, workflow execution, scheduler change, shared-root edit, or peer-track edit was performed.

---

## 1. Continuity, admission, source, and topology

I continued from

`runs/R11/2026-09-18T19-53-52Z_i0054-periodic-cycleweights-u030-c051-73e4.md`

rather than restarting. That report moved the fixed metric `50 -> 51`, proved U030/C051, used B5/B16/B29, and recorded B9/B18/B24 as the next nonrepeating triple. Those are the three methods actually used here.

Before research I reread/searched the required repository surfaces: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, `operations/claims/I0054.md`, `operations/NEW_METHODS_2026-09-16.md`, the I0054 intake/attempt surfaces, the newest R11 report, current audit hits, and the neighboring P13 state. The canonical claim remains **R11 provisional exclusive owner, `PENDING_ADMISSION, not READY`**. I found no competing current owner and no posted/settled Open Problem 18 result. P13's old I0051 clade-covariance problem is distinct and is not reassigned here. R11's pre-deployment planar-SAW route remains retired with its immutable history.

I reread the actual arXiv v3 PDF. Printed page 58 says:

> Open Problem 18. Are there superficially different discrete models whose limit is the same CTCS(infinity)?

and immediately asks whether the characteristic subordinator approximation can arise in another discrete tree model. Printed page 48 says that CTCS(infinity) is formalized through Kingman's exchangeable partitions and that the finite CTCS(n) clade partition is the restriction of the infinite partition.

Therefore the frozen target remains the strong one used by R11: for every fixed `k`, the **entire partition-valued cadlag genealogy** on `[k]` must converge in Skorokhod `J_1`; then the compatible restrictions converge in the summable projective metric
\[
d_{\rm proj}(\omega,\eta)
=\sum_{k\ge1}2^{-k}\bigl(1\wedge d_{J_1,k}(\omega^{[k]},\eta^{[k]})\bigr).
\]
Matching a root split, tagged fragment, or one-time marginal is insufficient.

For a current CTCS block of size `b=i+j`, the generator rate of one specified unordered split `A|A^c`, `|A|=i`, is
\[
q_b(A\mid A^c)=B(i,j)=\frac{(i-1)!(j-1)!}{(b-1)!}.
\]

### Current literature / prior-art screen

Fresh 18 September 2026 searches again found Aldous--Janson v3 as the controlling source. The nearby 18 August 2026 paper of Chorbadzhiyska--Minchev--Savov, arXiv:2608.18320, treats beta-splitting trees through homogeneous fragmentations/subordinators and resolves a height problem, not this discrete-model universality problem. Heng Ma's 13 September 2026 arXiv:2609.14329 explicitly resolves Aldous--Janson Open Problem 4 (discrete height), again not Open Problem 18. A bounded exact-phrase/current-author search found no announced resolution of Open Problem 18. This negative search is **not** a novelty certificate.

Weighted random permutations are classical. In particular Ercolani--Ueltschi (Random Structures & Algorithms 44 (2014), 109--133) and Betz--Ueltschi--Velenik (Ann. Appl. Probab. 21 (2011), 312--331) study random permutations with cycle weights; later work treats broad weight regimes. I make no novelty claim for weighted permutations, finite Fourier analysis, Abel summation, or singularity transfer. Targeted searches for quasiperiodic/irrational-rotation cycle weights did not surface the CTCS uniform-cycle compiler below. External novelty of U031/C052 remains **UNVERIFIED**.

---

## 2. Move #18 — translate an aperiodic weight sequence into finitely many boundary singularities

Let
\[
P(t)=\sum_{r=-L}^{L}c_re^{irt}
\]
be a real trigonometric polynomial such that
\[
c_0=1,\qquad c_{-r}=\overline{c_r},\qquad P(t)>0\quad(t\in\mathbb R).
\]
Fix `alpha` with `alpha/(2 pi)` irrational and define the genuinely aperiodic positive cycle weights
\[
\vartheta_m=P(m\alpha),\qquad m\ge1.
\]
Set
\[
A(z)=\sum_{m\ge1}\frac{\vartheta_m}{m}z^m,
\qquad
F(z)=e^{A(z)}=\sum_{n\ge0}f_nz^n.
\]
Fourier expansion gives the exact identity, for `|z|<1`,
\[
\boxed{
A(z)=-\sum_{r=-L}^{L}c_r\log(1-e^{ir\alpha}z),
\qquad
F(z)=\prod_{r=-L}^{L}(1-e^{ir\alpha}z)^{-c_r}.
}
\tag{2.1}
\]
The `r=0` factor is `(1-z)^(-1)`.

The strict positivity of `P` forces a spectral gap. Indeed, for every `r != 0`,
\[
|c_r|
=\left|\frac1{2\pi}\int_0^{2\pi}P(t)e^{-irt}\,dt\right|
<\frac1{2\pi}\int_0^{2\pi}P(t)\,dt=1.
\tag{2.2}
\]
The inequality is strict because equality in the triangle inequality would force `e^{-irt}` to have one constant argument on the support of `P(t)dt`, while `P(t)>0` on the whole circle. Hence
\[
\rho:=\max_{r\ne0}\Re c_r<1.
\tag{2.3}
\]
Irrationality of `alpha/(2 pi)` makes the finitely many points `z=e^{-ir alpha}` distinct. Thus `z=1` is the unique exponent-one boundary singularity and every other singularity is subcritical.

Near `z=1`,
\[
A(z)=\log\frac1{1-z}+h_0+O(1-z),
\qquad
F(z)=\frac{C}{1-z}(1+O(1-z)),
\tag{2.4}
\]
with `C>0`. At a secondary point `zeta_r=e^{-ir alpha}`, the local form is
\[
F(z)=C_r(1-z/\zeta_r)^{-c_r}(1+O(1-z/\zeta_r)).
\tag{2.5}
\]
A finite-singularity Darboux/transfer contour therefore yields
\[
\boxed{f_n=C+O(n^{\rho-1})\longrightarrow C.}
\tag{2.6}
\]
For completeness: on a contour indented around the finitely many unit-circle singularities, the `z=1` indentation contributes exactly the coefficient of `C/(1-z)`, namely `C`; the `r != 0` indentation after `z=\zeta_r(1-u/n)` is bounded by a constant times `n^{\Re c_r-1}`, and the remaining contour may be pushed to radius `1+eta` away from those finitely many cuts. Summing the finite contributions gives (2.6).

---

## 3. Exact uniform-cycle pointing and the logarithmic coefficient

Sample a permutation `sigma in S_N` with probability
\[
\Pr_N(\sigma)=\frac1{N!f_N}\prod_{C\in\operatorname{Cycles}(\sigma)}\vartheta_{|C|},
\tag{3.1}
\]
and, **after** sampling `sigma`, choose one of its `K(sigma)` cycles uniformly. Let `M_N` be the selected cycle size.

Define
\[
B_A(z):=\int_0^1e^{tA(z)}dt
=\frac{F(z)-1}{A(z)}
=\sum_{n\ge0}b_nz^n.
\tag{3.2}
\]
Using `1/K=\int_0^1 t^{K-1}dt` and marking the selected cycle in the labelled assembly gives the exact finite identity
\[
\boxed{
\Pr(M_N=m)=\frac{\vartheta_m}{m}\frac{b_{N-m}}{f_N}.
}
\tag{3.3}
\]
All `b_n` are nonnegative because of the integral representation.

At `z=1`, (2.4) implies
\[
B_A(z)=
\frac{C+o(1)}
{(1-z)\{\log(1/(1-z))+h_0+o(1)\}}.
\tag{3.4}
\]
I record the local logarithmic transfer explicitly. On a Hankel indentation at `z=1`, put `z=1-u/n`. Then
\[
z^{-n-1}=e^{u}(1+o(1)),
\]
and the denominator in (3.4) becomes
\[
\frac{u}{n}\{\log n-\log u+h_0+o(1)\}.
\]
After multiplying the coefficient integral by `log n`, dominated convergence on a truncated Hankel contour gives the standard simple-pole Hankel integral
\[
\frac1{2\pi i}\int_{\mathcal H}\frac{e^u}{u}\,du=1.
\]
The tails are uniformly integrable after the usual keyhole truncation, and expanding
`1/(log n-log u+h_0)` gives an `O(1/log^2 n)` local error. At a secondary singularity, division by `A(z)` adds at least one logarithmic denominator, so its coefficient is
\[
O\!\left(\frac{n^{\Re c_r-1}}{\log n}\right)
+O\!\left(\frac1{n(\log n)^2}\right)
=o(1/\log n)
\]
by (2.3). Hence
\[
\boxed{b_n\sim\frac{C}{\log n}.}
\tag{3.5}
\]
The same finite-contour estimates, enlarged over finitely many small `n`, give a global bound
\[
0\le b_n\le\frac{C_1}{\log(n+2)}.
\tag{3.6}
\]
Combining (2.6), (3.3), and (3.5), uniformly for every fixed `epsilon>0` and
`epsilon N <= m <= (1-epsilon)N`,
\[
\boxed{
\Pr(M_N=m)=\frac{\vartheta_m}{m\log N}(1+o(1)).
}
\tag{3.7}
\]

---

## 4. Move #24 — the extremal boundary cannot occur in the positive finite-Fourier class

The dangerous failure mode suggested after U030 was a secondary boundary singularity with exponent one, capable of competing with `z=1`. Equation (2.2) shows that this is impossible throughout the present class: positivity and mean one imply
\[
\boxed{\max_{r\ne0}|c_r|<1.}
\tag{4.1}
\]
Thus every nonconstant finite Fourier mode is automatically subcritical. In this class, the true extremal exponent `1` lives only on the boundary where the positive mass would have to collapse onto a set on which a nontrivial character has constant phase. A strictly positive trigonometric polynomial cannot do that.

This turns the proposed counterexample search into a universality theorem: **finite Fourier quasiperiodicity is not strong enough to destroy the CTCS tangent.** To find failure one must leave this class, for example through infinitely many frequencies with no uniform spectral gap or through a genuinely singular boundary measure.

---

## 5. U031 — quasiperiodic finite-Fourier cycle weights have the CTCS binary tangent

Conditional on `M_N=m`, exchangeability makes the selected cycle support a uniform `m`-subset of `[N]`. For one specified visible unordered split with side sizes `i,j`,
\[
s_{N,m}(i,j)
=
\frac{(m)_{\underline i}(N-m)_{\underline j}
+(m)_{\underline j}(N-m)_{\underline i}}
{(N)_{\underline{i+j}}}.
\tag{5.1}
\]
Set
\[
P_N(i,j)=\sum_{m=1}^N\Pr(M_N=m)s_{N,m}(i,j).
\tag{5.2}
\]

### Bulk weighted Riemann sum

Let
\[
g_{i,j}(x)=x^{i-1}(1-x)^j+x^{j-1}(1-x)^i.
\]
Because `theta_m=P(m alpha)=sum_r c_r e^{ir alpha m}`, for every `C^1` function `g`,
\[
\frac1N\sum_{m=1}^N\vartheta_m g(m/N)
\longrightarrow\int_0^1g(x)dx.
\tag{5.3}
\]
Indeed the `r=0` term is the ordinary Riemann sum. For `r != 0`, the partial sums of `e^{ir alpha m}` are uniformly bounded by `2/|1-e^{ir alpha}|`; Abel summation against `g(m/N)` therefore makes the normalized contribution `O_g(1/N)`.

Using (3.7), (5.1), and (5.3) on `epsilon <= m/N <= 1-epsilon` gives the bulk limit
\[
(\log N)P_N(i,j)\to
\int_0^1g_{i,j}(x)dx
\]
after `N -> infinity` then `epsilon -> 0`, provided the two endpoints vanish. They do, as follows.

### Endpoint bounds

Let `a=min(i,j)>=1`. For `m<=epsilon N`, (3.6), (2.6), boundedness of `theta_m`, and (5.1) give
\[
\Pr(M_N=m)\le\frac{C}{m\log N},
\qquad
s_{N,m}(i,j)\le C_{i,j}(m/N)^a,
\]
for all sufficiently large `N`; hence
\[
(\log N)\sum_{m\le\epsilon N}\Pr(M_N=m)s_{N,m}(i,j)
\le C_{i,j}\epsilon^a.
\tag{5.4}
\]
For the upper endpoint write `m=N-r`. Since a nontrivial split must place at least `a` specified visible labels in the complement,
\[
s_{N,N-r}(i,j)\le C_{i,j}(r/N)^a.
\]
Also (3.3), (2.6), and (3.6) give
\[
\Pr(M_N=N-r)\le\frac{C}{N\log(r+2)}.
\]
For `r<=sqrt(N)`, the total after multiplication by `log N` is
`O(log N * N^{-(a+1)/2})=o(1)`. For `sqrt(N)<r<=epsilon N`, use `log r >= (1/2)log N` to obtain
\[
(\log N)\sum_{\sqrt N<r\le\epsilon N}
\Pr(M_N=N-r)s_{N,N-r}(i,j)
\le C_{i,j}\epsilon^{a+1}.
\tag{5.5}
\]
Equations (5.4)--(5.5) prove the endpoint negligibility.

Therefore
\[
\begin{aligned}
(\log N)P_N(i,j)
&\longrightarrow
\int_0^1\bigl[x^{i-1}(1-x)^j+x^{j-1}(1-x)^i\bigr]dx\\
&=B(i,j+1)+B(j,i+1)\\
&=\boxed{B(i,j)}.
\end{aligned}
\tag{5.6}
\]
In particular `P_N(1,1)~1/log N`. With
\[
\lambda_N=P_N(1,1)^{-1},
\]
we obtain the normalized tangent
\[
\boxed{\lambda_NP_N(i,j)\longrightarrow B(i,j)}
\tag{5.7}
\]
for every fixed `i,j>=1`.

This is `R11-I0054-U031`.

---

## 6. Move #9 — random phase does not break the theorem

As a robustness/counterexample test, replace the deterministic weights by
\[
\vartheta_m(\beta)=P(m\alpha+\beta).
\]
The Fourier coefficients become `c_r e^{ir beta}`. Their magnitudes are unchanged, so the uniform spectral gap
\[
\max_{r\ne0}|c_r|<1
\]
holds for every `beta`; the dominant `r=0` singularity is unchanged; and the Abel-summation estimate is uniform in `beta`. Therefore U031 is uniform over phase. A phase drawn independently at each proposal, or drawn once and held fixed, has the same normalized beta tangent after averaging/conditioning.

I do **not** count this randomized phase variant as another metric class. Its role this run is methodological: the randomization attack failed to destroy the limit and instead exposed the stronger phase-uniform theorem.

---

## 7. C052 — an explicit genuinely aperiodic weighted-permutation hierarchy

Choose `alpha` by
\[
\cos\alpha=\frac14,
\qquad
P(t)=1+\frac12\cos t,
\qquad
\vartheta_m=1+\frac12\cos(m\alpha).
\tag{7.1}
\]
Then `1/2 <= theta_m <= 3/2`. Moreover
\[
e^{i\alpha}=\frac{1+i\sqrt{15}}4
\]
has irreducible rational minimal polynomial
\[
2x^2-x+2.
\]
Its discriminant is `-15`, and the primitive minimal polynomial is not monic, so `e^{i alpha}` is not an algebraic integer. Every root of unity is an algebraic integer; hence `e^{i alpha}` is not a root of unity and `alpha/(2 pi)` is irrational. Thus the cycle weights are genuinely aperiodic.

Here
\[
A(z)=-\log(1-z)-\frac14\log(1-e^{i\alpha}z)-\frac14\log(1-e^{-i\alpha}z),
\]
\[
F(z)=\frac1{1-z}(1-e^{i\alpha}z)^{-1/4}(1-e^{-i\alpha}z)^{-1/4}.
\tag{7.2}
\]
The only secondary exponents are `1/4`, well below the dominant exponent `1`. U031 applies.

For each global size `N`, define one discrete hierarchy as follows. At each raw generation, every current nonsingleton block `B` attempts independently with probability
\[
a_N=\delta_N\lambda_N,
\qquad
\delta_N=\min\{N^{-2},P_N(1,1)/2\}.
\tag{7.3}
\]
On an attempt:

1. sample a fresh `theta`-weighted permutation of the ambient `[N]` using (3.1);
2. choose one of its cycles uniformly;
3. let `S` be that cycle support and replace `B` by the nonempty members of `B cap S` and `B setminus S`.

Take one raw generation to have physical duration `delta_N`.

### Exact hidden-label lumping

For a restriction to `[k]`, every visible current block `A` lies in a unique full block `B`. The attempt probability is the same for every nonsingleton full block and does not depend on `|B|`. A fresh ambient selected support `S` is exchangeable and independent of the hidden content of `B`. If an attempt changes only hidden labels and leaves `A` intact, exactly one descendant full block still contains `A`, and at the next raw generation that descendant again has the same attempt probability and the same fresh support law. Therefore the `[k]` process is itself Markov, with no hidden-state correction: its one-block specified split probabilities are exactly `P_N(i,j)`.

### Finite-restriction generator and J1 convergence

For fixed `k`, the partition state space of `[k]` is finite. By (5.7), every allowed single-block transition rate converges to the corresponding CTCS rate. In one raw step, the probability that two distinct visible blocks both make visible jumps is `O_k(a_N^2)`. Over a bounded physical interval there are `O(1/delta_N)` raw generations, so the accumulated simultaneous-jump error is
\[
O_k(\delta_N\lambda_N^2).
\]
Since `lambda_N~log N` and eventually `delta_N=N^{-2}`,
\[
\boxed{
\delta_N\lambda_N^2
=O((\log N)^2/N^2)\to0.
}
\tag{7.4}
\]
Thus the restricted one-step matrices have the uniform finite-state Euler expansion
\[
P_{N,k}=I+\delta_NQ_{\rm CTCS}^{[k]}+o_k(\delta_N).
\tag{7.5}
\]
Iterating over `floor(t/delta_N)` steps gives uniform convergence of the finite-state semigroups on compact time intervals. Coupling the exponential holding times and jump kernels (or, equivalently, applying finite-state uniformization) then yields convergence of the complete cadlag paths:
\[
\boxed{
\Pi_{N,052}^{[k]}\Longrightarrow\Pi_{\rm CTCS}^{[k]}
\quad\text{in Skorokhod }J_1
}
\tag{7.6}
\]
for every fixed `k`.

For any fixed `K`, the first `K` projective coordinates are all determined by the `[K]` path, so (7.6) gives their joint convergence. The tail of the projective metric is bounded deterministically by `sum_{k>K}2^{-k}`. Letting `K -> infinity` gives
\[
\boxed{
\Pi_{N,052}\Longrightarrow\Pi_{\operatorname{CTCS}(\infty)}
}
\tag{7.7}
\]
in the frozen summable projective finite-restriction `J_1` topology.

This is the complete required-limit proof for C052, not a marginal limit.

---

## 8. Exact finite witness and frozen non-equivalence

The cosine recurrence
\[
\cos(n\alpha)=\frac12\cos((n-1)\alpha)-\cos((n-2)\alpha)
\]
is rational because `2 cos alpha=1/2`. The first four weights are
\[
\vartheta_1=\frac98,\quad
\vartheta_2=\frac9{16},\quad
\vartheta_3=\frac{21}{32},\quad
\vartheta_4=\frac{81}{64}.
\]
Exact enumeration of all weighted permutations of `[4]`, followed by uniform cycle selection, gives
\[
\Pr(M_4=1)=\frac{1123}{3083},\quad
\Pr(M_4=2)=\frac{360}{3083},\quad
\Pr(M_4=3)=\frac{448}{3083},\quad
\Pr(M_4=4)=\frac{1152}{3083}.
\]
For specified visible splits,
\[
P_4(1,1)=\frac{2051}{6166},\qquad
P_4(2,2)=\frac{120}{3083},\qquad
P_4(1,3)=\frac{1571}{12332}.
\]
Hence the global-time-rescaling invariant root-rate pair is
\[
\boxed{
\left(
\frac{P_4(2,2)}{P_4(1,1)},
\frac{P_4(1,3)}{P_4(1,1)}
\right)
=
\left(\frac{240}{2051},\frac{1571}{4102}\right).
}
\tag{8.1}
\]
Nearby retained classes have different witnesses:
\[
C051:\left(\frac{80}{217},\frac{57}{434}\right),\quad
C050:\left(\frac12,0\right),\quad
C049:\left(\frac4{41},\frac{33}{82}\right),\quad
C048:\left(\frac5{61},\frac{51}{122}\right).
\]
A targeted repository search for the exact witness `240/2051` found no previous I0054 occurrence, and a search for `I0054 aperiodic cycle weights` recovered only C051's recorded *future target*, not a prior construction. The aperiodic irrational-rotation cycle-weight law is also structurally different from C051's periodic law. Leaf relabeling cannot alter these exchangeable root-rate ratios, and positive global time rescaling cancels from them. Under the frozen convention C052 is therefore counted as a new class.

---

## 9. Exact self-check, written after the mathematical route

After the proof route was established I executed an exact `Fraction` checker and archived both source and stdout:

`artifacts/R11/2026-09-18T20-40-10Z_c052_quasiperiodic_cycleweights_check.py`  
creation commit: `a0111d4572ce363f7d2cd857fde00c0236651347`  
SHA-256 of executed local source: `be1f22692a080c0964ad18044c95313a2176bd02620bcaaa6b32306c5758ed92`.

`artifacts/R11/2026-09-18T20-40-10Z_c052_quasiperiodic_cycleweights_check.out`  
creation commit: `3e77f3bfd3105bb292e7bea2e2266fc3bc3d6b6b`  
SHA-256 of archived stdout: `1416b6902d3c4c4546fa124ed3b30546f0807bba82e70785ce452d8d10f36d82`.

The checker performs **177,853 exact assertions**. It enumerates all weighted permutations through `N=8`; verifies the partition-function recurrence and the exact uniform-cycle pointing identity; verifies conditional support exchangeability and the hypergeometric visible-split formula; checks the rational cosine recurrence and finite positivity diagnostics; checks the complete `N=4` witness; compares the nearest archived witnesses; verifies the beta telescoping identity through `i,j<=40`; and verifies the CTCS total exit-rate identity through block size 30. Its last line is

`ALL_EXACT_CHECKS_PASS`.

This is a **self-check of finite claims**, not an independent audit and not a replacement for the written asymptotic/J1 proof above.

---

## 10. Status, closure gate, and runtime-control status

The stable author-side state is
\[
\boxed{\texttt{R11-I0054-U031 = PROVED\_AUTHOR\_SIDE}},
\qquad
\boxed{\texttt{R11-I0054-C052 = PROVED\_AUTHOR\_SIDE}},
\qquad
\boxed{51\to52}.
\]

I am **not calling Aldous--Janson Open Problem 18 closed**. The canonical reservation remains `PENDING_ADMISSION, not READY`, and the current repository audit search still does not supply the required present-package `P26-AUDIT-R11-I0054` end-to-end PASS plus a second independent OTHER-track end-to-end PASS. External novelty is also unverified. The honest source/campaign label remains **PARTIAL**.

The model-control limitation is unchanged. Current repository policy records that the exposed scheduling/control surface has prompt/title, schedule, enablement and timing controls but no binding model-family selector, reasoning-effort selector, guaranteed hour-long runtime, or authenticated completed-run model receipt. Therefore GPT-6/maximum remains a prompt request only. A native edit that returns `You cannot modify this task` must be handled from its authorized owning context or through platform support; it must not be cloned or bypassed. I made no scheduler change in this run.

---

## 11. Next nonrepeating route

Next methods: **#10 DERANDOMIZE, #20 FIND WHY THE ALGORITHM FAILS, #30 DO ONE SCALE/FREQUENCY AT A TIME**.

The strongest next target is to leave the finite-Fourier safe class. Start with bounded positive mean-one weights
\[
\vartheta_m=1+\varepsilon a_m
\]
where `(a_m)` has zero Cesaro mean but infinitely many frequencies (Thue--Morse, Rudin--Shapiro, or a deliberately sparse block spectrum). U031 shows that finitely many subcritical boundary singularities cannot break CTCS. The next run should identify the exact failure mechanism for infinitely many boundary frequencies: either prove a discrepancy/spectral condition implying
\[
f_N\to C,\qquad b_N\sim C/\log N,
\]
or construct a bounded mean-one sequence whose bulk weighted Riemann sums still converge to Lebesgue measure while the boundary coefficient `b_N` fails the `1/log N` law. That would locate a genuine universality threshold rather than merely add class 53.

---

## ledger_delta

```yaml
track: R11
lane: CLOSABLE_OUTSIDE
intake: I0054
source: "Aldous--Janson, arXiv:2303.02529v3, Open Problem 18"
metric_name: "number of distinct nontrivial discrete model classes with complete required-limit proofs under frozen equivalence"
before: 51
after: 52
movement: true
source_status: PARTIAL
canonical_claim_status: PENDING_ADMISSION
methods_used: [9, 18, 24]
new_claims:
  - id: R11-I0054-U031
    status: PROVED_AUTHOR_SIDE
    statement: "positive mean-one finite-Fourier irrational-rotation cycle weights, followed by uniform cycle selection and pair normalization, have the CTCS beta binary tangent"
  - id: R11-I0054-C052
    status: PROVED_AUTHOR_SIDE
    statement: "the explicit cos(alpha)=1/4 quasiperiodic weighted-permutation / uniform-cycle hierarchy converges to CTCS(infinity) in projective finite-restriction Skorokhod J1"
checker:
  source: artifacts/R11/2026-09-18T20-40-10Z_c052_quasiperiodic_cycleweights_check.py
  source_creation_commit: a0111d4572ce363f7d2cd857fde00c0236651347
  output: artifacts/R11/2026-09-18T20-40-10Z_c052_quasiperiodic_cycleweights_check.out
  output_creation_commit: 3e77f3bfd3105bb292e7bea2e2266fc3bc3d6b6b
  assertions: 177853
  result: ALL_EXACT_CHECKS_PASS
closure_missing:
  - current-package P26 end-to-end PASS
  - second independent OTHER-track end-to-end PASS
  - external novelty verification
next_methods: [10, 20, 30]
next_target: "infinite-frequency bounded mean-one cycle weights: sharp spectral/discrepancy condition or explicit boundary-law obstruction"
```
