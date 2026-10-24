# HARD7-04 — sharp post-giant hub stripping under only finite third moments

**Status:** analytic route theorem / PARTIAL only. This does **not** settle van der Hofstad's Section 8.3 discrete-duality question or determine the sharp second-largest-component law. It strengthens the active `VDH-8.3-DUALITY` route by determining, up to a sharp constant, the largest degree that can remain after the giant under the source's finite-third-moment hypotheses. It also gives a source-valid extremal family showing why the strongest Coulson--Perarnau barely-subcritical theorem cannot simply be applied to the post-giant degree sequence.

## 1. Inputs already proved on this track

Let the deterministic degree sequence satisfy the active source regime

\[
\nu_n=1+\varepsilon_n,\qquad \varepsilon_n\downarrow0,
\qquad \varepsilon_n n^{1/3}\to\infty,
\qquad \frac1n\sum_i d_i^3\to \mathbb E D^3<\infty,
\tag{1.1}
\]

with positive limiting mean and a nondegenerate critical limiting degree law `D`. Put

\[
X=D^*-1,
\qquad
\kappa:=\mathbb E[X(X-1)]\in(0,\infty),
\qquad
N_n:=n\varepsilon_n^3\to\infty.
\tag{1.2}
\]

The preceding HARD7-04 artifacts proved the following facts, which are the only track-specific inputs used below.

1. If `xi_n` is the excess-branching extinction probability and `t_n^*=-log xi_n`, then
   \[
   \frac{t_n^*}{\varepsilon_n}\longrightarrow\frac{2}{\kappa}.
   \tag{1.3}
   \]
2. There is a genuine completed-component stopping time `tau_n`, equal to the end of the giant excursion with probability `1-o(1)`, such that
   \[
   \tau_n=t_n^*+o_p(\varepsilon_n).
   \tag{1.4}
   \]
3. Give vertex `i` the independent clock
   \[
   E_i\sim\operatorname{Exp}(d_i).
   \tag{1.5}
   \]
   If `S_n^{post}` is the sleeping vertex set at `tau_n`, then actual sleeping vertices are contained in the auxiliary clock-survivor set:
   \[
   S_n^{post}\subseteq\{i:E_i>\tau_n\}.
   \tag{1.6}
   \]
   The only auxiliary survivors that can be absent from the actual sleeping set are vertices forced awake as C1 roots.
4. If `R_n^{root}` is the set of C1 roots selected through the giant boundary, then
   \[
   |R_n^{root}|=O_p(\varepsilon_n^{-1}).
   \tag{1.7}
   \]
5. Conditional on the exploration through `tau_n`, the sleeping half-edges are uniformly perfectly matched, so the post-giant remainder is an exact configuration model on the random degree sequence `\{d_i:i\in S_n^{post}\}`.

Define its maximum degree

\[
\Delta_n^{post}:=\max_{i\in S_n^{post}}d_i,
\tag{1.8}
\]

with value zero if the remainder is empty.

---

## 2. B4 — prove a weaker statement completely: exponential hub stripping

The source heuristic says that high-degree vertices should be absorbed into the unique giant. The following theorem makes that statement quantitative at the largest scale allowed by only third-moment information.

### Theorem 2.1 (sharp universal upper scale for residual hubs)

Under (1.1), for every fixed `a>kappa/2`,

\[
\boxed{
\mathbb P\left(
\Delta_n^{post}>\frac{a}{\varepsilon_n}\log(n\varepsilon_n^3)
\right)\longrightarrow0.
}
\tag{2.1}
\]

Equivalently,

\[
\boxed{
\frac{\varepsilon_n\Delta_n^{post}}
{\log(n\varepsilon_n^3)}
\le \frac{\kappa}{2}+o_p(1).
}
\tag{2.2}
\]

#### Proof

Fix `a>kappa/2`. Choose a constant `b` satisfying

\[
\frac1a<b<\frac2\kappa.
\tag{2.3}
\]

By (1.3)--(1.4),

\[
\mathbb P(\tau_n<b\varepsilon_n)\to0.
\tag{2.4}
\]

Set

\[
h_n:=\left\lceil\frac{a}{\varepsilon_n}\log N_n\right\rceil.
\tag{2.5}
\]

On the event `tau_n>=b epsilon_n`, (1.6) implies

\[
\{\Delta_n^{post}\ge h_n\}
\subseteq
\bigcup_{i:d_i\ge h_n}\{E_i>b\varepsilon_n\}.
\tag{2.6}
\]

No independence between `tau_n` and the clocks is needed here; after replacing the random time by the deterministic lower bound `b epsilon_n`, this is a deterministic set inclusion. Hence

\[
\begin{aligned}
\mathbb P(\Delta_n^{post}\ge h_n)
&\le o(1)+\sum_{i:d_i\ge h_n}e^{-b\varepsilon_n d_i}\\
&\le o(1)+e^{-b\varepsilon_n h_n}\,\#\{i:d_i\ge h_n\}.
\end{aligned}
\tag{2.7}
\]

Third-moment convergence gives a deterministic constant `C<infty` with `sum_i d_i^3<=Cn` for all large `n`. Therefore

\[
\#\{i:d_i\ge h_n\}
\le\frac{Cn}{h_n^3}
\le \frac{C'}{a^3}\frac{n\varepsilon_n^3}{(\log N_n)^3}
=\frac{C'}{a^3}\frac{N_n}{(\log N_n)^3}.
\tag{2.8}
\]

Also

\[
e^{-b\varepsilon_n h_n}\le N_n^{-ab}.
\tag{2.9}
\]

Since `ab>1`, (2.7)--(2.9) give

\[
\mathbb P(\Delta_n^{post}\ge h_n)
\le o(1)+O\left(
\frac{N_n^{1-ab}}{(\log N_n)^3}
\right)=o(1).
\tag{2.10}
\]

This proves (2.1), and letting `a downarrow kappa/2` through a countable sequence gives (2.2). `square`

### Corollary 2.2 (all fixed higher residual moments acquire an exponential cutoff)

For every fixed real `r>=3`,

\[
\boxed{
\frac1n\sum_{i\in S_n^{post}}d_i^r
=O_p(\varepsilon_n^{3-r}).
}
\tag{2.11}
\]

In particular,

\[
\frac1n\sum_{i\in S_n^{post}}d_i^4=O_p(\varepsilon_n^{-1}).
\tag{2.12}
\]

#### Proof

Fix any `b<2/kappa`. On `tau_n>=b epsilon_n`, (1.6) gives

\[
\sum_{i\in S_n^{post}}d_i^r
\le\sum_i d_i^r\mathbf1_{\{E_i>b\varepsilon_n\}}.
\tag{2.13}
\]

The expectation of the right side is

\[
\begin{aligned}
\sum_i d_i^r e^{-b\varepsilon_n d_i}
&=\varepsilon_n^{3-r}
\sum_i d_i^3(\varepsilon_n d_i)^{r-3}e^{-b\varepsilon_n d_i}\\
&\le C_{r,b}\varepsilon_n^{3-r}\sum_i d_i^3
=O(n\varepsilon_n^{3-r}),
\end{aligned}
\tag{2.14}
\]

because `sup_{y>=0} y^{r-3}e^{-by}<infty`. Markov's inequality and (2.4) prove (2.11). `square`

### The constant is naturally the subcritical variance parameter

Coulson--Perarnau use

\[
R_n=\frac{\sum_i d_i(d_i-2)^2}{\sum_i d_i}.
\tag{2.15}
\]

For the critical limiting degree law,

\[
R_*:=\frac{\mathbb E[D(D-2)^2]}{\mathbb E D}.
\tag{2.16}
\]

At criticality `E[D(D-2)]=0`, and therefore

\[
\begin{aligned}
R_*-\kappa
&=\frac{\mathbb E\{D(D-2)^2-D(D-1)(D-2)\}}{\mathbb E D}\\
&=-\frac{\mathbb E[D(D-2)]}{\mathbb E D}=0.
\end{aligned}
\tag{2.17}
\]

Thus the upper constant in (2.2) is exactly `R_*/2`.

---

## 3. B21 — ask who else has this shape: what the best subcritical theorem actually needs

A fresh 19 September 2026 literature check was made against the current active source and the sharpest directly relevant subcritical theorem I found.

### 3.1 Source status

The active primary source remains Remco van der Hofstad, *Stochastic processes on random graphs*, preliminary monograph dated 4 August 2026, Notes on Section 8.3, printed p. 245 / PDF p. 255. After discussing the finite-third-moment subcritical crossover and the supercritical second-largest component, it asks: **“Does the discrete duality principle still hold?”**

The source URL is

`https://rhofstad.win.tue.nl/Saint_Flour_SPoRG_Grundlehre.pdf`.

Repository searches also reconfirmed that the old intake candidate `I0049` is not this target: the uniformly-grown-graph critical-window question is already recorded as KNOWN / resolved in its queued scope after Jorritsma--Maillard--Mörters, arXiv:2512.18937. No ownership collision was found for `operations/claims/VDH-8.3-DUALITY.md`.

### 3.2 Coulson--Perarnau does not automatically close the post-giant problem

Matthew Coulson and Guillem Perarnau, *Largest component of subcritical random graphs with given degree sequence*, Electronic Journal of Probability 28 (2023), DOI `10.1214/23-EJP921`, arXiv `2111.11780`, define

\[
Q_n=\frac1m\sum_i d_i(d_i-2),\qquad
R_n=\frac1m\sum_i d_i(d_i-2)^2.
\tag{3.1}
\]

Their Theorem 1.3 assumes, in addition to their Assumption 1.1,

\[
\Delta_n|Q_n|=o(R_n),
\qquad
Q_n\le-\omega(n)n^{-1/3}R_n^{2/3},
\tag{3.2}
\]

and obtains

\[
L_1\le(1+\delta)\frac{2R_n}{Q_n^2}
\log\left(\frac{|Q_n|^3n}{R_n^2}\right)
\quad\text{with high probability}.
\tag{3.3}
\]

Their Assumption 1.1(v) is the additional fourth-moment restriction

\[
\mathbb E[D_n^4]\le\Delta_n^{1/2},
\tag{3.4}
\]

which they themselves call the most restrictive assumption and explicitly ask how far it is needed. Their Theorem 1.5 replaces (3.2) by a Cramér-transform formulation but still assumes Assumption 1.1 and `Delta_n<=n^{1/6}`.

The post-giant theorem from the previous HARD7-04 run gives

\[
Q_n^{post}=-\varepsilon_n+o_p(\varepsilon_n),
\qquad
R_n^{post}\xrightarrow{p}R_*=\kappa>0.
\tag{3.5}
\]

The new Theorem 2.1 gives only

\[
\Delta_n^{post}|Q_n^{post}|
\le\left(\frac{R_*}{2}+o_p(1)\right)\log N_n,
\tag{3.6}
\]

not `o_p(R_*)`. Corollary 2.2 similarly gives an `O_p(epsilon_n^{-1})` fourth moment, not (3.4). Therefore the source's finite-third-moment assumptions do **not** feed directly into the hypotheses of the presently sharp Coulson--Perarnau theorem.

This is now an exact hypothesis mismatch rather than the vague statement “a subcritical theorem is missing.”

Fresh dated searches included `barely subcritical configuration model largest component finite third moment`, `second largest barely supercritical configuration model discrete duality`, and later papers citing the 2023 Coulson--Perarnau result. I found model-specific later work, including recent preferential-attachment/inhomogeneous results, but no later source closing this deterministic-degree finite-third-moment configuration-model gap. This is bounded negative evidence, not a novelty certificate.

---

## 4. B24 — find the extremal object: the `R_*/2` residual-hub constant is sharp

The upper scale in Theorem 2.1 is not just an artifact of a union bound. Under the source's own finite-third-moment assumptions one can asymptotically saturate it, even for a fixed benign critical limiting law.

### Theorem 4.1 (source-valid extremal family)

Let the critical limiting degree law be

\[
\mathbb P(D=1)=\frac34,
\qquad
\mathbb P(D=3)=\frac14.
\tag{4.1}
\]

Then

\[
\mathbb E D=\frac32,
\qquad
\mathbb E[D(D-2)]=0,
\qquad
\kappa=R_*=1.
\tag{4.2}
\]

For every fixed `c<1/2`, there exists a deterministic barely-supercritical degree-sequence family satisfying all hypotheses in (1.1), converging with third moments to (4.1), for which

\[
\boxed{
\mathbb P\left(
\frac{\varepsilon_n\Delta_n^{post}}
{\log(n\varepsilon_n^3)}\ge c-o(1)
\right)\longrightarrow1.
}
\tag{4.3}
\]

Consequently, the universal constant `kappa/2=1/2` in Theorem 2.1 is sharp for this limiting law. In particular, the stronger property

\[
\varepsilon_n\Delta_n^{post}=o_p(1)
\tag{4.4}
\]

is false under the source hypotheses alone; hence the Coulson--Perarnau condition `Delta|Q|=o(R)` cannot be recovered merely by proving that all “very high” original degrees enter the giant.

#### Construction and proof

Fix `0<c<1/2`. Choose `alpha>0` so small that

\[
r:=\frac{\alpha}{1-3\alpha}<1-2c.
\tag{4.5}
\]

Choose `beta` with

\[
r+2c<\beta<1.
\tag{4.6}
\]

Finally choose a constant `C>2` sufficiently close to `2` that

\[
r+Cc<\beta.
\tag{4.7}
\]

Work along an even integer subsequence `n` and set the design scale

\[
\bar\varepsilon_n=n^{-\alpha},
\qquad
\bar N_n=n\bar\varepsilon_n^3=n^{1-3\alpha},
\qquad
M_n=\lfloor\bar N_n^\beta\rfloor.
\tag{4.8}
\]

Choose an odd integer

\[
h_n=\frac{c+o(1)}{\bar\varepsilon_n}\log\bar N_n.
\tag{4.9}
\]

Give `M_n` vertices degree `h_n`. Among the remaining `n-M_n` vertices, use only degrees `1` and `3`, with degree-3 proportion

\[
\frac14+\frac38\bar\varepsilon_n+o(\bar\varepsilon_n),
\tag{4.10}
\]

where the `o(bar epsilon_n)` term absorbs integer rounding. All degrees may be kept odd, so on even `n` the total degree is even; bounded changes to the bulk would also repair parity without affecting any estimate.

##### Step 1: the hubs are invisible to the limiting third moment

Because `n=bar N_n/bar epsilon_n^3`,

\[
\frac{M_nh_n^3}{n}
=(c^3+o(1))\bar N_n^{\beta-1}(\log\bar N_n)^3\longrightarrow0.
\tag{4.11}
\]

Thus the empirical law and its third moment converge to (4.1). In particular the critical limiting law is nondegenerate and has `kappa=1`.

The hub contribution to the numerator defining `Q=nu-1` is smaller still:

\[
\frac{M_nh_n(h_n-2)}{n}
=O\left(
\bar\varepsilon_n\bar N_n^{\beta-1}(\log\bar N_n)^2
\right)
=o(\bar\varepsilon_n).
\tag{4.12}
\]

For the `{1,3}` bulk with degree-3 excess `s_n=3bar epsilon_n/8+o(bar epsilon_n)`, the numerator `E[D(D-2)]` is `4s_n`, while the mean degree is `3/2+2s_n`. Hence its criticality excess equals

\[
\frac{4s_n}{3/2+2s_n}
=\bar\varepsilon_n(1+o(1)).
\tag{4.13}
\]

Equations (4.12)--(4.13) show that the actual source parameter

\[
\varepsilon_n:=\nu_n-1
=\bar\varepsilon_n(1+o(1)).
\tag{4.14}
\]

Therefore `epsilon_n n^{1/3}->infty`, and `n epsilon_n^3=bar N_n(1+o(1))`.

##### Step 2: polynomially many hubs survive the extinction clock

For this family `kappa=1`, so (1.3)--(1.4) and (4.14) imply

\[
\mathbb P(\tau_n\le C\bar\varepsilon_n)\to1.
\tag{4.15}
\]

Let `Z_n` be the number of hub vertices whose independent clock exceeds `C bar epsilon_n`. Since all hubs have degree `h_n`,

\[
Z_n\sim\operatorname{Bin}\left(
M_n,e^{-C\bar\varepsilon_n h_n}
\right),
\tag{4.16}
\]

and

\[
\mathbb E Z_n
=\bar N_n^{\beta-Cc+o(1)}.
\tag{4.17}
\]

By (4.7), this expectation tends to infinity. More importantly,

\[
\bar\varepsilon_n^{-1}
=\bar N_n^{r},
\tag{4.18}
\]

and therefore

\[
\frac{\mathbb E Z_n}{\bar\varepsilon_n^{-1}}
=\bar N_n^{\beta-Cc-r+o(1)}\longrightarrow\infty.
\tag{4.19}
\]

A Chernoff bound gives `Z_n=(1+o_p(1))E Z_n`.

##### Step 3: forced roots cannot remove all surviving hubs

On the event in (4.15), every hub counted by `Z_n` is still an auxiliary clock survivor at `tau_n`. The only way such a vertex can fail to be sleeping in the exact post-giant remainder is to have been selected as a C1 root. By (1.7) and (4.14),

\[
|R_n^{root}|=O_p(\bar\varepsilon_n^{-1})=o_p(Z_n)
\tag{4.20}
\]

using (4.19). Hence with probability tending to one at least one degree-`h_n` hub remains in `S_n^{post}`. Thus

\[
\Delta_n^{post}\ge h_n
\tag{4.21}
\]

with high probability. Equations (4.9), (4.14), and `n epsilon_n^3=bar N_n(1+o(1))` imply (4.3). `square`

### Interpretation: a factor-four gap appears

For the limiting law (4.1), and more generally at a nondegenerate critical limit, `R_*=kappa`. The canonical Coulson--Perarnau barely-subcritical bulk scale is

\[
\frac{2R_*}{\varepsilon_n^2}\log(n\varepsilon_n^3),
\tag{4.22}
\]

whereas Theorem 2.1 says the largest surviving hub has degree at most

\[
\left(\frac{R_*}{2}+o_p(1)\right)
\frac{\log(n\varepsilon_n^3)}{\varepsilon_n}.
\tag{4.23}
\]

A naive subcritical drift calculation would multiply a root degree by `1/epsilon_n` to estimate the size of the tree it feeds, putting the hub contribution at coefficient `R_*/2`, versus coefficient `2R_*` in (4.22): a factor of four. This last comparison is **route guidance, not a proved component-size theorem**, because an exploration from a high-degree root in a finite configuration model is not an independent Galton--Watson tree. It nevertheless identifies a concrete next task: prove that the exponentially thinned hub layer cannot create components at the `2R_*` bulk-extreme scale, then truncate it away and apply a sharp bounded-tail exploration theorem to the bulk.

---

## 5. What moved and what remains open

The frozen admission metric

\[
\Delta_{dual,n}=\left|\frac{1-\nu_n^{dual}}{\varepsilon_n}-1\right|
\tag{5.1}
\]

already had asymptotic value zero, so it cannot move below zero in this run. The source-level progress is structural:

1. the exact post-giant remainder has maximum degree at most `(R_*/2+o_p(1)) epsilon_n^{-1} log(n epsilon_n^3)`;
2. this scale is sharp under the source's own finite-third-moment assumptions;
3. therefore the most tempting black-box use of Coulson--Perarnau Theorem 1.3 is genuinely unavailable in full generality, rather than merely not yet checked;
4. the sharp residual hubs still sit a factor four below the canonical bulk largest-component coefficient after the heuristic `1/epsilon_n` subcritical progeny amplification, revealing a new truncation route instead of a dead end.

The source remains **PARTIAL / OPEN**. The next proof obligation is now sharper:

\[
\boxed{
\text{Control components rooted in the post-giant hub layer up to }(2R_*-\delta)
\varepsilon_n^{-2}\log N_n,
\text{ then prove the sharp bulk extreme law after truncation.}
}
\tag{5.2}
\]

No finite exhaustive claim was introduced here, so no exact checker was manufactured. Every theorem-sized claim above has its proof on the page; Theorem 4.1 explicitly distinguishes a source-valid asymptotic construction from finite numerical evidence.
