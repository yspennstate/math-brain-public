Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.** GPT-6 / maximum reasoning was requested, but this runtime exposes no authenticated applied-model / applied-effort selector or receipt, so I do not claim otherwise.

# PROB10-02 / R17 — exact Snell elimination of information debt and a rigorous finite variational approximation

Repository / branch: private `yspennstate/math-open-problems` / `master`.

Target:
\[
\gamma_2=\lim_{n\to\infty}\frac{\mathbf E\,LCS(X_1^n,Y_1^n)}n
\]
for two independent iid uniform binary strings. Every transition below is driven by actual source bits. No independent Bernoulli matching array is introduced.

**R17 source-endpoint movement in this run: none. Status remains OPEN / PARTIAL.** The mathematical progress is an exact elimination of the persistent one-sided information-debt coordinates from the preceding R17 Bellman process, a proved geometric finite-to-infinite approximation bound for that eliminated process, and an improved exact width-6 mechanism certificate. The latter is still below the retained rigorous source lower endpoint and therefore is not counted as source progress.

## 0. Continuity, ownership, literature, and source metric

Controlling owner directive: `operations/PROB10_2026-09-20.md`, current blob `6f0fcee836d93371d43b84af1a55150fedc80779` as consumed in this run.

### 0.1 Actual pre-refocus R17 successor remains handed off

I reread `operations/claims/H0021.md`, current blob `e4b83b8fb97a3fc672a007eb59621d6dd8718039`. It still records

`UNASSIGNED (released by R17 under later owner refocus)`

and preserves the actual R16/R17 H0021 history. In particular:

- navigation commit `c8891869a1335d67bada83f23f63f2ce09603565` is preserved;
- frozen H0021 metric remains `Delta_near=2`;
- R16's six-run historical stagnation and two consumed recoveries remain preserved;
- R17's own H0021 unchanged streak remains one, with zero R17 H0021 recovery runs consumed;
- the substantive H0021 report `runs/R17/20260919_2216Z_h0021_portwidth_defect_barrier_c080_b42f.md` and all earlier artifacts remain untouched.

No H0021 failure count, claim, artifact, or ownership field is reset in this run.

### 0.2 R17 LCS continuity is not restarted

The newest completed R17 PROB10-02 report before this run is

`runs/prob10_2026-09-20/PROB10-02/20260920T1046Z_r17_one_sided_information_debt_f2c4.md`

at commit `47a325cf00ea3c6609661143fcb64e15418c7081`, blob `12d4a1c0ce29910970669fb802f9ce02b4dc6857`.

That report already proved:

1. a **no-free-peek theorem**: an exposed but unconsumed iid source bit cannot be forgotten and later treated as fresh if the action used its value, except in the trivial action-independent case;
2. an exact one-sided information-debt Bellman process with statuses `N,A0,A1`, preserving the true source dependence;
3. the source transfer
   \[
   F_\ell h\ge h+\rho\mathbf1
   \quad\Longrightarrow\quad
   \gamma_2\ge \frac{2\rho}{1+\rho};
   \tag{0.1}
   \]
4. exact rational certificates through `ell=6`, with the previous displayed `ell=6` transferred lower about `0.772418377682626`, still below the retained source lower endpoint;
5. the exact length-six counterexample `A=010011, B=110100` to a leading-run-only action rule.

The earlier exact recursive congruence / MTBDD route, suffix-carry relaxation, finite-strip calculations, and their obstructions remain preserved. This run does not reset any of those failed transfers or treat the problem as unattempted.

### 0.3 Current neighboring ownership

The current division is still nonduplicating:

- **P02** owns the covering/cone stationary upper route;
- **P13** owns the dependence-preserving strip/boundary recursion and, in its current `2026-09-20T11-19-06Z__bias-extremal-integer-bellman-transfer.md`, has exact width-6 boundary-chain work;
- **R17** owns the finite-lookahead / information-state route.

An initial forced-clear macro idea was persisted before code in

`artifacts/prob10_2026-09-20/PROB10-02/20260920T1120Z_r17_forced_clear_smdp_idea_7d31.md`.

Ownership screening judged that route too close to P13's finite-boundary program for this slot, so I did not spend the computational budget duplicating it. I do **not** claim here a theorem that the two constructions are identical.

### 0.4 Actual source interval before and after this R17 work

The newest P02 source-level dependency retained on current master is

`proofnet24/P02-progress-lcs/runs/2026-09-20/2026-09-20T10-03-15Z__matched-successor-defect-report.md`,

blob `2596bca4d6d8b52b27b80626df09a3b0caaa7829`.

It retains the rigorous public lower endpoint
\[
L=\frac{99083249}{125000000}=0.792665992.
\tag{0.2}
\]
It defines its repository-internal exact upper candidate by
\[
p=256717,\quad q=800000,\quad d=q-p=543283,\quad t=p/q,\quad S=q^6d,
\]
\[
a=1995237757733917147310102692686664915858011319606812684127301,
\quad b=4220452010631561279,
\]
\[
D_{new}=515110016194946010524505039025520073185829,
\]
\[
\beta_{new}=\frac ab-\frac{D_{new}}{2ab},\qquad
\lambda_{new}=\frac{t^2}{S}\beta_{new},\qquad
U_{new}=\frac{\log(4t^2)}{\log\lambda_{new}}.
\tag{0.3}
\]
That report proves the separator
\[
U_{new}<0.82627594276228262501510658153729663282346199619319002388080618331256294443029952.
\tag{0.4}
\]
Thus the source metric entering this R17 work is the exact symbolic width
\[
W_{before}=U_{new}-L.
\tag{0.5}
\]
Nothing below beats either endpoint, so
\[
\boxed{W_{after}=W_{before}=U_{new}-L.}
\tag{0.6}
\]
P02's internal upper candidate is companion-track work pending the repository's review/priority standard and is not attributed to R17.

### 0.5 Bounded fresh literature/status check

A bounded current check on 20 September 2026 remains consistent with the exact binary coefficient being unresolved.

- V. Chvátal and D. Sankoff, *Longest Common Subsequences of Two Random Sequences*, J. Appl. Probab. 12 (1975), is the original source of the limiting constant.
- Alexander Tiskin, `https://arxiv.org/abs/2212.01582v2`, last revised 13 August 2024, explicitly says the binary coefficient is as yet unresolved. Its v2 comments explicitly state that earlier preprint claims about the stochastic process and `gamma` turned out to be incorrect and were omitted. **None of those withdrawn claims is used here.**
- Heineman--Miller--Reichman--Salls--Sarkozy--Soiffer, `https://arxiv.org/abs/2407.10925`, give the rigorous lower bound `0.792665992` for the two-string binary case.
- Li--Ren--Wen, *Expected Length of the Longest Common Subsequence of Multiple Strings*, published online by Cambridge on 2 March 2026, still presents the two-string binary constant through the established bound history rather than an exact determination.
- Lueker's 2009 JACM upper `0.826280` remains the conventional published upper endpoint; the smaller `U_new` above is repository-internal.

This is a bounded status check, not a claim of exhaustive worldwide priority.

## 1. Ideas fixed before code and three attacks

Three idea notes were persisted before the exact checker:

1. `20260920T1120Z_r17_forced_clear_smdp_idea_7d31.md` — forced-clear finite options; screened out for ownership proximity to P13 before implementation;
2. `20260920T1132Z_r17_cylinder_cocycle_idea_e5a2.md` — a pathwise stationary cylinder upper dual;
3. `20260920T1148Z_r17_debt_snell_elimination_idea_19ac.md` — exact elimination of persistent one-sided debt by an optimal-stopping / Snell envelope.

The executed mathematical attacks are:

- **Attack A:** falsify the bounded scalar cylinder upper dual by an exact periodic-environment obstruction;
- **Attack B:** prove exact Snell elimination, uniqueness, and a quantitative finite-horizon approximation theorem;
- **Attack C:** test an aggressive first-match-prefix quotient of the Snell problem and preserve an exact counterexample when it fails.

Attack B then yields a finite exact certificate stronger than the previous R17 `ell=6` mechanism value.

## 2. Attack A — exact obstruction to the bounded scalar cylinder upper dual

The 11:32 idea considered a two-sided iid environment `omega=(X,Y)` with shifts `T_X,T_Y`, match reward
\[
m(\omega)={\bf1}_{\{X_1=Y_1\}},
\]
a bounded cylinder potential `phi`, and constants `c_X,c_Y` satisfying pointwise
\[
c_X+\phi(T_X\omega)-\phi(\omega)\ge0,
\tag{2.1}
\]
\[
c_Y+\phi(T_Y\omega)-\phi(\omega)\ge0,
\tag{2.2}
\]
\[
c_X+c_Y+\phi(T_XT_Y\omega)-\phi(\omega)\ge m(\omega).
\tag{2.3}
\]
These inequalities would telescope along every monotone alignment path and imply `gamma_2<=c_X+c_Y`.

### Proposition 2.1 — scalar cylinder obstruction

Every certificate of the form (2.1)--(2.3) satisfies
\[
\boxed{c_X+c_Y\ge1.}
\tag{2.4}
\]

#### Proof

Take the deterministic bi-infinite all-zero environment `omega_0`. Then
\[
T_X\omega_0=T_Y\omega_0=T_XT_Y\omega_0=\omega_0,
\qquad m(\omega_0)=1.
\]
Substituting into (2.3) cancels the potential exactly and leaves
\[
c_X+c_Y\ge1.
\]
QED.

Since the retained upper endpoint is already below `0.827`, the bounded scalar cylinder-gradient dual cannot improve it. This is an exact obstruction, not a numerical failure. The richer non-exact edge-cocycle possibility from the idea note is **not** claimed resolved here.

## 3. Attack B — exact Snell elimination of one-sided information debt

Fix a lookahead length `ell>=1`. Let
\[
a=a_1\cdots a_\ell,\qquad b=b_1\cdots b_\ell,
\]
and define
\[
\sigma_u(a)=a_2\cdots a_\ell u.
\]
Let `H(a,b)` be an arbitrary bounded ordinary-state potential and fix a candidate Bellman increment
\[
\rho\ge0.
\]

For a debt orientation `(a,u)`, the already exposed but not yet consumed first-string bit is `u`. Put
\[
a^u=\sigma_u(a),\qquad x=a_1.
\]
While the debt persists, `a` and `u` remain frozen and only the `b` window shifts using genuine fresh iid `Y` bits. This converts the debt coordinate into a one-dimensional optimal-stopping problem on the binary de Bruijn shift of `b`.

### 3.1 Debt Bellman operator

For a bounded function `d` on binary `ell`-windows define `B=B_{H,\rho}^{a,u}` by
\[
(Bd)(b)=
\begin{cases}
1+\frac12\sum_{v\in\{0,1\}}H(a^u,\sigma_v b)-\rho,
& b_1=x,\\[1.2ex]
\max\left\{H(a^u,b)-\rho,
\frac12\sum_{v\in\{0,1\}}d(\sigma_v b)-\rho\right\},
& b_1\ne x.
\end{cases}
\tag{3.1}
\]

At a mismatch, the first term means consume the first-string head now and clear the debt. The second means advance the second string by one actual fresh source bit and keep the exposed first-string bit. At a matching head, taking the match clears the debt and earns one reward.

Define the forced-clear horizon-zero function
\[
d^{(0)}(b)=
\begin{cases}
1+\frac12\sum_vH(a^u,\sigma_vb)-\rho,&b_1=x,\\
H(a^u,b)-\rho,&b_1\ne x,
\end{cases}
\tag{3.2}
\]
and recursively
\[
d^{(K+1)}=B d^{(K)}.
\tag{3.3}
\]
Thus `d^(K)` permits at most `K` successive waits before a forced first-string clear, unless a matching head arrives earlier.

### 3.2 Finite-block contraction and unique infinite envelope

### Lemma 3.1

For any bounded `d,e` and every integer `r>=0`,
\[
\boxed{
\|B^{\ell+r}d-B^{\ell+r}e\|_\infty
\le 2^{-r}\|d-e\|_\infty.
}
\tag{3.4}
\]
In particular `B^(ell+1)` is a contraction with factor at most `1/2`. Hence `B` has a unique bounded fixed point, denoted
\[
d^*=B d^*.
\tag{3.5}
\]
Moreover `d^(K)` increases pointwise to `d^*`.

#### Proof

At a matching-head state the right side of (3.1) is independent of the input function, so a perturbation is killed immediately. At a mismatch, the map
\[
d\mapsto\max\{\text{fixed stop value},\,\tfrac12(d(\sigma_0b)+d(\sigma_1b))-\rho\}
\]
is monotone and nonexpansive, and a terminal perturbation can propagate through one application only along the wait branch.

After `ell+r` consecutive propagated waits, the heads seen at times `0,...,ell-1` exhaust the original deterministic `b` window. If any of them matches `x`, the perturbation has already been killed. In the worst case all `ell` original heads mismatch. Propagation through the remaining `r` steps then requires `r` independent fresh fair refill bits all to be `1-x`, an event of probability `2^{-r}`. Averaging the terminal perturbation over these fresh bits gives (3.4).

Taking `r=1`, `B^(ell+1)` is a strict contraction on the finite-dimensional sup-norm space. It has a unique fixed point. If `q` is that fixed point, then `Bq` is also fixed by `B^(ell+1)`, so uniqueness gives `Bq=q`; hence `B` itself has the same unique fixed point `d^*`.

From (3.2), at every mismatch
\[
d^{(0)}(b)\le(Bd^{(0)})(b),
\]
while equality holds at a match. By monotonicity,
\[
d^{(0)}\le d^{(1)}\le d^{(2)}\le\cdots.
\]
The contraction implies convergence to the unique fixed point `d^*`. QED.

### 3.3 Optimal-stopping representation

Let `b_t` be the second-string window after `t` successive waits, driven by genuine fresh iid fair refill bits, and let
\[
T=\inf\{t\ge0:(b_t)_1=x\}.
\tag{3.6}
\]
At any mismatch time `t<T`, stopping yields
\[
H(a^u,b_t)-(t+1)\rho.
\tag{3.7}
\]
Waiting until the first match yields
\[
1+H(a^u,b_{T+1})-(T+1)\rho.
\tag{3.8}
\]
Standard finite-horizon backward induction applied to (3.1) shows that `d^(K)` is exactly the value over causal stopping policies with at most `K` waits. Lemma 3.1 and monotone convergence show that `d^*` is the unrestricted Snell envelope. This representation uses the same previously exposed bit `u` until it is consumed; it never resamples or forgets it.

### 3.4 Proved finite-to-infinite truncation error

### Theorem 3.2 — geometric Snell truncation

Let
\[
S=\operatorname{osc}(H)=\max H-\min H.
\]
For every `K>=ell`, every orientation `(a,u)`, and every starting `b`,
\[
\boxed{
0\le d^*(b)-d^{(K)}(b)
\le 2^{-(K-\ell+1)}(S+1).
}
\tag{3.9}
\]

#### Proof

The lower inequality follows because the finite-horizon policy class is contained in the infinite-horizon class.

Couple a full optimal policy and its version forced to clear the first-string debt at the `K`-th wait. They differ only if no matching head has appeared through state `b_K` and the full policy has not stopped earlier. For `K>=ell`, the first `ell` possible heads can be adversarially fixed, but the remaining
\[
K+1-\ell
\]
heads are fresh independent fair bits. Therefore
\[
\Pr(T>K)\le2^{-(K-\ell+1)}.
\tag{3.10}
\]
On this event the forced policy stops at time `K` with payoff
\[
H(a^u,b_K)-(K+1)\rho.
\]
If the full policy stops later at a mismatch, its advantage is at most `S`, because `rho>=0`. If instead it reaches a later matching head, its advantage is at most `S+1`, the extra `1` being the match reward; all additional `rho` costs only decrease that advantage. Hence the conditional advantage is at most `S+1`. Multiplying by (3.10) gives (3.9). QED.

This is the requested explicit finite-to-infinite error: the persistent debt state can be approximated exponentially accurately without replacing the genuine source by independent match indicators.

## 4. Exact reduced stationary variational operator

For each `(a,u)`, let `d^*_{a,u}` be the fixed point from Section 3. Define an ordinary-state operator `G^*_{ell,rho}`.

If `a_1=b_1`, set
\[
(G^*H)(a,b)=1+\frac14\sum_{u,v}H(\sigma_u a,\sigma_v b).
\tag{4.1}
\]
If `a_1\ne b_1`, define the two ordinary no-peek values
\[
A=\frac12\sum_u H(\sigma_u a,b),
\qquad
B=\frac12\sum_v H(a,\sigma_v b),
\tag{4.2}
\]
and the one-sided-peek value
\[
P^*=\frac12\sum_u
\max\left\{
H(\sigma_u a,b),
\frac12\sum_v d^*_{a,u}(\sigma_v b)
\right\}.
\tag{4.3}
\]
Then
\[
(G^*H)(a,b)=\max\{A,B,P^*\}.
\tag{4.4}
\]
Let `G_K` be the same operator with `d^(K)` in place of `d^*`.

### Theorem 4.1 — exact debt elimination, lower and upper Bellman sides

Fix `H` and `rho>=0`. There exist debt potentials `D_0,D_1` making the full one-sided information-debt Bellman inequalities satisfy
\[
F_\ell(H,D)\ge(H,D)+\rho\mathbf1
\tag{4.5}
\]
if and only if
\[
\boxed{G^*_{\ell,\rho}H\ge H+\rho\mathbf1.}
\tag{4.6}
\]
Likewise there exist debt potentials with
\[
F_\ell(H,D)\le(H,D)+\rho\mathbf1
\tag{4.7}
\]
if and only if
\[
\boxed{G^*_{\ell,\rho}H\le H+\rho\mathbf1.}
\tag{4.8}
\]
Thus the `2*4^ell` debt potential coordinates need not be independent optimization variables: for a fixed ordinary potential and rate they are exactly the family of one-dimensional Snell envelopes `d^*_{a,u}`.

#### Proof

For the lower inequalities, the debt-state part of (4.5) is exactly
\[
D_{a,u}\le B_{H,\rho}^{a,u}D_{a,u}.
\tag{4.9}
\]
Iterating (4.9) and using monotonicity gives
\[
D_{a,u}\le B D_{a,u}\le B^2D_{a,u}\le\cdots\to d^*_{a,u},
\]
where convergence follows from Lemma 3.1. The ordinary `N`-state Bellman expression is monotone in every debt value. Hence replacing any feasible debt family by the larger fixed-point family `d^*` preserves the lower ordinary inequalities. With that replacement, the ordinary component is exactly (4.1)--(4.4), proving necessity of (4.6). Conversely, if (4.6) holds, choose `D_{a,u}=d^*_{a,u}`. The debt inequalities hold with equality and the ordinary inequalities are (4.6), proving sufficiency.

For the upper inequalities, the debt part is
\[
D_{a,u}\ge B_{H,\rho}^{a,u}D_{a,u}.
\tag{4.10}
\]
Iteration gives `D_{a,u}>=d^*_{a,u}`. Replacing by the smaller fixed point can only decrease the monotone ordinary Bellman expression, so any full supersolution implies (4.8). Conversely choose the fixed points. QED.

This is an exact stationary variational reduction of R17's dependence-preserving information-state process. It is **not** claimed to be an exact finite-`ell` characterization of the full Chvátal--Sankoff constant; its source role remains the proved lower transfer (0.1).

### Corollary 4.2 — rigorous finite approximation of the reduced operator

For `K>=ell`,
\[
\boxed{
G_KH\le G^*H\le G_KH+\varepsilon_K\mathbf1,
\qquad
\varepsilon_K=2^{-(K-\ell+1)}(\operatorname{osc}(H)+1).
}
\tag{4.11}
\]

#### Proof

Theorem 3.2 gives `0<=d^*-d^(K)<=epsilon_K` uniformly for every orientation. Averages and maxima in (4.3)--(4.4) are monotone and 1-Lipschitz in the sup norm, while the match branch and the no-peek branches do not use `d`. This gives (4.11). QED.

Two useful certified consequences are immediate:

1. if an **exact finite** calculation proves
   \[
   G_KH\ge H+\rho\mathbf1,
   \tag{4.12}
   \]
   then `G^*H>=H+rho`, so Theorem 4.1 produces a genuine full-debt subsolution with **no truncation loss in rho**; by the previously proved source transfer (0.1),
   \[
   \gamma_2\ge\frac{2\rho}{1+\rho};
   \tag{4.13}
   \]
2. if an exact calculation proves
   \[
   G_KH+\varepsilon_K\mathbf1\le H+\rho\mathbf1,
   \tag{4.14}
   \]
   then it certifies a full-debt supersolution. This bounds the finite information-debt mechanism; it is **not** by itself an upper bound on the unrestricted `gamma_2`.

This is the main new finite-to-infinite bridge of the run.

## 5. Attack C — first-match-prefix quotient fails exactly

A natural compression after Snell elimination is to classify `b` only by the deterministic prefix up to the first in-window head matching `x=a_1`. That is not sufficient for arbitrary ordinary potentials.

Take
\[
\ell=3,\qquad a=000,\qquad u=0,\qquad \rho=\frac35,
\]
and ordinary potential
\[
H(a',b')=\text{last bit of }b'.
\tag{5.1}
\]
Compare
\[
b=100,\qquad b'=101.
\]
Both have the same first-match prefix `10` and the same first in-window matching time `T=1` relative to `x=0`.

For `b=100`, immediate stop is `-3/5`. Waiting once moves to `000` or `001`, both matching-head states. At either matching-head state the terminal value is
\[
1+\frac{0+1}{2}-\frac35=\frac9{10},
\]
so the wait value at `100` is
\[
\frac9{10}-\frac35=\frac3{10}.
\]
Hence
\[
d^*(100)=\frac3{10}.
\tag{5.2}
\]

For `b'=101`, immediate stop already has value
\[
1-\frac35=\frac25.
\]
The one-wait value is again `3/10`, so
\[
d^*(101)=\frac25.
\tag{5.3}
\]
Therefore
\[
\boxed{d^*(100)\ne d^*(101)}
\]
despite identical first-match prefix/time. Any exact quotient preserving only that information loses necessary terminal-potential data. The checker verifies (5.2)--(5.3) exactly. This obstruction prevents another false compression from being scaled up.

## 6. Exact width-6 reduced certificate

The checker is

`artifacts/prob10_2026-09-20/PROB10-02/20260920T1200Z_r17_snell_elimination_exact_c8d4.py`

created at commit

`9158c0064fd55da686590b97eb84afbc1a25a086`.

Executed output is

`artifacts/prob10_2026-09-20/PROB10-02/20260920T1200Z_r17_snell_elimination_exact_c8d4.out`

created at commit

`4927c5929815f535d5c81708d8a08d733b95932d`.

The computation uses Python `Fraction` throughout. Candidate construction is not itself trusted as a proof: it runs `100` exact iterations of the full one-sided-debt Bellman operator at `ell=6`, extracts the ordinary `N`-component `H`, and then performs a fresh exact scan of the reduced finite operator `G_20` at the rational target
\[
\boxed{\rho_{cert}=\frac{6293309}{10000000}=0.6293309.}
\tag{6.1}
\]
The exact minimum residual is
\[
\min_{a,b}\bigl(G_{20}H-H\bigr)(a,b)
=
\frac{61724634372071852361413350307618400173932180058336199120280129}
{98079714615416886934934209737619787751599303819750539264000000},
\tag{6.2}
\]
which is approximately `0.6293313007088371`. More importantly, the exact positive margin over (6.1) is
\[
\boxed{
\frac{196507041945157264813263266876452046068730395772348908357}
{490398573077084434674671048688098938757996519098752696320000000}>0.
}
\tag{6.3}
\]
Thus (4.12) is proved by an exact finite scan. Since `G_20<=G^*`, Theorem 4.1 gives an exact full information-debt subsolution at `rho_cert`, and the inherited source-transfer theorem gives
\[
\boxed{
\gamma_2\ge
\frac{2\rho_{cert}}{1+\rho_{cert}}
=
\frac{12586618}{16293309}
\approx0.7725022584424073.
}
\tag{6.4}
\]

This is a strict mechanism-level improvement over the preceding R17 `ell=6` 35-step certificate, whose exact Bellman lower increment is
\[
\rho_{old}=\frac{44277390789435}{70368744177664}
\approx0.6292195676768841,
\tag{6.5}
\]
with transferred source lower about `0.7724183776826261`. The increment improvement is
\[
\rho_{cert}-\rho_{old}
=
\frac{612055919066017}{5497558138880000000}>0,
\tag{6.6}
\]
and the transferred-lower improvement is about
\[
8.38807598\times10^{-5}.
\]

However,
\[
\frac{12586618}{16293309}<\frac{99083249}{125000000},
\tag{6.7}
\]
so **the source lower endpoint does not move**. The source-improvement threshold inherited from the preceding report remains
\[
\rho>\frac{99083249}{150916751}
\approx0.6565424205295806.
\tag{6.8}
\]

For the specific extracted `H`,
\[
\operatorname{osc}(H)
=
\frac{82108478431651500895600854764180379951886888936095031}
{11972621413014756705924586149611790497021399392059392}
\approx6.85802011098.
\]
Therefore Theorem 3.2 gives, at `ell=6,K=20`, the explicit uniform debt-envelope error
\[
\varepsilon_{20}
=
\frac{\operatorname{osc}(H)+1}{2^{15}}
\approx2.39807742645\times10^{-4}.
\tag{6.9}
\]
The lower certificate (6.4) does not pay this error because `G_20<=G^*`; (6.9) is nevertheless the certified two-sided approximation error for evaluating the infinite Snell envelope from the finite truncation.

The archived checker also performs a separate exact geometric-tail regression on a nontrivial rational test potential for `K=3,...,9`, verifies the first-match-prefix counterexample, and ends

`ALL_EXACT_CHECKS_PASS`

and

`RETURN_CODE=0`.

Self-checking is not an independent audit.

## 7. Before/after separated by level

### Source-level metric

Before:
\[
L\le\gamma_2\le U_{new},\qquad W_{before}=U_{new}-L.
\]
After:
\[
L\le\gamma_2\le U_{new},\qquad
\boxed{W_{after}=W_{before}.}
\]
No R17 source endpoint moves.

### Mechanism-level progress

This run proves, for the genuine dependent source model:

1. bounded scalar cylinder-gradient upper certificates are exactly obstructed at value `1` by the all-zero periodic environment;
2. the persistent one-sided debt coordinate is an exact one-dimensional Snell envelope with a unique fixed point;
3. its `K`-wait truncation has the explicit uniform error (3.9);
4. the full `3*4^ell` lower/supersolution existence problem reduces exactly to the ordinary-state operator `G^*` plus the solved Snell envelopes;
5. finite `G_K` lower certificates transfer without truncation loss to the full debt process and then, by the previous source theorem, to the original iid binary LCS;
6. a first-match-prefix-only quotient is false, with the exact `(100,101)` counterexample;
7. at `ell=6`, the exact reduced certificate improves the R17 mechanism lower to (6.4), while honestly remaining below the source endpoint.

## 8. Exact unresolved full-scope gap

The full Chvátal--Sankoff constant remains unresolved. This run does not determine `gamma_2`, beat `L`, improve `U_new`, or provide the independent audits required for closure.

The concrete R17 lower-side target is now sharper:

\[
\boxed{
\text{find a finite exact }G_K\text{ subsolution at some larger }\ell
\text{ with }\rho>rac{99083249}{150916751}.
}
\tag{8.1}
\]
The Snell theorem removes the persistent debt variables and supplies a rigorous finite truncation. The remaining bottleneck is the `4^ell` ordinary potential itself. The failed first-match quotient shows that any successful compression must retain enough tail information to evaluate terminal `H` values; simply keeping the time to the first matching head is insufficient.

A genuinely different next attack within this problem would be an **inequality-only structured potential** for `H` (for example a low-order local interaction / tensor representation) with an exact separation oracle for `G_K`, rather than another exact behavioral quotient or another finite strip. Any such candidate must be rationalized and globally scanned before it can move (8.1).

Status remains **OPEN / PARTIAL**.

```yaml
ledger_delta:
  track: R17
  target: "PROB10-02 full binary Chvatal-Sankoff constant"
  model_requested: "GPT-6 maximum"
  model_actual: "GPT-5.6 Sol"
  reasoning_actual: "UNVERIFIED"
  source_status: OPEN
  status: PARTIAL
  lower_before: "99083249/125000000"
  lower_after: "99083249/125000000"
  upper_before: "U_new from P02 2026-09-20T10-03-15Z matched-successor-defect report"
  upper_after: "same U_new"
  metric_before: "U_new-L"
  metric_after: "U_new-L"
  source_movement: none
  mechanism_progress:
    - "exact scalar-cylinder periodic obstruction c_X+c_Y>=1"
    - "exact one-sided debt Snell elimination"
    - "proved finite-block contraction and unique debt envelope"
    - "proved uniform truncation error 2^{-(K-ell+1)}(osc(H)+1)"
    - "exact reduced lower/supersolution equivalence"
    - "first-match-prefix quotient counterexample"
    - "ell=6 exact reduced certificate rho=6293309/10000000"
    - "transferred mechanism lower 12586618/16293309, still below source L"
  current_lower_metric_target: "rho > 99083249/150916751"
  h0021: "released/unassigned; Delta_near=2 and all historical counters preserved"
  closure: false
```

No schedule, cadence, enabled state, email, Drive item, public posting, workflow, purchase, permission, root ledger, or peer claim file was modified.