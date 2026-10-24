Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.** GPT-6 / maximum reasoning was requested, but this runtime exposes no authenticated applied-model / applied-effort receipt, so I do not claim otherwise.

# PROB10-02 / R17 — symmetric single-debt peeking and an exact binary run-exhaustion macro process

Repository / branch: private `yspennstate/math-open-problems` / `master`.

Target:
\[
\gamma_2=\lim_{n\to\infty}\frac{\mathbf E\,LCS(X_1^n,Y_1^n)}n
\]
for two independent iid uniform binary strings. Every stochastic transition below is generated from actual source bits. No independent Bernoulli matching array is introduced.

**Source endpoint movement in this R17 run: none. Status remains OPEN / PARTIAL.** The run gives two new dependence-preserving finite-state formulations and an exact mechanism-level lower improvement, but that lower certificate remains below the retained rigorous source lower endpoint.

## 0. Continuity, ownership, source metric, and literature

Controlling owner directive: `operations/PROB10_2026-09-20.md`.

### 0.1 Actual R17 predecessor and H0021 handoff

The newest completed R17 PROB10-02 report entering this run is

`runs/prob10_2026-09-20/PROB10-02/20260920T1200Z_r17_snell_elimination_variational_c8d4.md`

at commit `a1b2b3226fc44f4094a8b4d128a06e5419060c7d`, blob `0548abac1497cef1698a548630394dd2e537bf84`.

It proved the exact one-sided-debt Snell elimination and finite truncation
\[
0\le d^*-d^{(K)}\le 2^{-(K-\ell+1)}(\operatorname{osc}H+1),
\]
and the exact width-6 mechanism certificate
\[
\rho=\frac{6293309}{10^7},\qquad
\gamma_2\ge\frac{12586618}{16293309}\approx0.7725022584424073,
\]
still below the source lower endpoint. Its scalar cylinder upper-dual obstruction and first-match-prefix counterexample are retained, not reset.

The actual pre-refocus R17 successor remains correctly handed off. `operations/claims/H0021.md`, blob `e4b83b8fb97a3fc672a007eb59621d6dd8718039`, still records H0021 as **UNASSIGNED (released by R17 under later owner refocus)**. Navigation commit `c8891869a1335d67bada83f23f63f2ce09603565`, the R16 six-run stagnation, two consumed R16 recoveries, the R17 H0021 unchanged streak of one, zero R17 recoveries consumed, and frozen `Delta_near=2` are all preserved. No H0021 claim, artifact, failure count, or ownership field is modified here.

### 0.2 Current nonduplicating ownership

The same-source division remains:

- P02: covering/cone stationary upper route;
- P13: finite strip / boundary recursion route;
- R17: finite-lookahead / information-state route.

This run stays in the R17 information-state lane. The run-exhaustion macro process in Sections 4--6 is an ordinary-window semi-Markov policy, not P13's strip boundary chain and not P02's covering/cone dual.

### 0.3 Certified interval before and after

The newest P02 source-level dependency remains

`proofnet24/P02-progress-lcs/runs/2026-09-20/2026-09-20T10-03-15Z__matched-successor-defect-report.md`

at commit `cf4381fc95f73f7c9ed885112c738dc36c7eb6a2`, blob `2596bca4d6d8b52b27b80626df09a3b0caaa7829`.

The retained rigorous lower endpoint is
\[
L=\frac{99083249}{125000000}=0.792665992.
\]
The repository-internal exact upper candidate in that report is recovered symbolically, not guessed:
\[
p=256717,\quad q=800000,\quad d=543283,\quad t=p/q,\quad S=q^6d,
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
\]
P02 proves
\[
U_{new}<0.82627594276228262501510658153729663282346199619319002388080618331256294443029952.
\]
Therefore the source metric entering and leaving this run is
\[
\boxed{W_{before}=W_{after}=U_{new}-L.}
\]
The proved decimal separator implies the diagnostic inequality
\[
W_{after}<0.03360995076228262501510658153729663282346199619319002388080618331256294443029952,
\]
but the exact tracked endpoint is the symbolic `U_new` above. P02's candidate remains companion-track work pending the repository's review / priority standard and is not attributed to R17.

### 0.4 Bounded fresh literature/status check

A fresh bounded check on 20 September 2026 remains consistent with the exact binary coefficient being unresolved.

- Chvátal--Sankoff, *Longest common subsequences of two random sequences*, J. Appl. Probab. 12 (1975), 306--315, is the original source of the limiting constant and bounds.
- Tiskin, `https://arxiv.org/abs/2212.01582v2`, last revised 13 August 2024, says the binary coefficient is still unresolved. Its v2 comments explicitly state that earlier claims about the stochastic process and `gamma` were incorrect and were omitted. **No withdrawn v1 claim is used here.**
- Heineman--Miller--Reichman--Salls--Sárközy--Soiffer, `https://arxiv.org/abs/2407.10925`, give the rigorous lower `0.792665992`.
- Lueker, JACM 56 (2009), gives the conventional published upper `0.826280`.
- Li--Ren--Wen, published online by Cambridge University Press on 2 March 2026, still describe determining the two-string binary constant as open and summarize the established public range.

This is a bounded current check, not an exhaustive worldwide novelty claim.

## 1. Ideas fixed before code and three materially different attacks

Before any checker for this run, I persisted

`artifacts/prob10_2026-09-20/PROB10-02/20260920T1216Z_r17_symmetric_single_debt_idea_71e4.md`

at commit `34f25374d42360c0f2aa942571c12b3124842465`.

Three attacks were then executed:

1. **symmetric single-debt peeking:** enlarge the one-sided information process to debt on either source and allow debt-orientation switching while preserving every exposed bit;
2. **binary run-exhaustion macro process:** use an exact structural recurrence specific to binary mismatched leading runs, producing a separate semi-Markov average-cost variational lower bound;
3. **aggressive run/head quotient:** test whether the macro value can be lumped only by head symbols and leading-run lengths; preserve an exact counterexample when it fails.

The first attack improves the R17 mechanism certificate. The second changes method within the same problem after repeated source-level stagnation. The third supplies an exact obstruction rather than silently scaling a false compression.

## 2. Attack A — symmetric single-debt information process

Fix `ell>=1`, windows
\[
a=a_1\cdots a_\ell,\qquad b=b_1\cdots b_\ell,
\]
and shifts
\[
\sigma_u a=a_2\cdots a_\ell u.
\]
The information status is
\[
N,\ A_0,A_1,\ B_0,B_1.
\]
`N` means no exposed source bit beyond the two visible windows. `A_u` means the next X-bit beyond the visible X-window has already been exposed as `u` and remains unconsumed. `B_v` is the Y analogue. At the end of every decision there is at most one such outstanding bit.

Let `h(a,b,s)` be a bounded potential. Define the Bellman operator `F^sym_ell` as follows.

### 2.1 No-debt state, matching heads

If `a_1=b_1`, greedily match them:
\[
(F^{sym}_\ell h)(a,b,N)
=1+\frac14\sum_{u,v}h(\sigma_u a,\sigma_v b,N).
\tag{2.1}
\]

### 2.2 No-debt state, mismatching heads

The ordinary one-step skips are
\[
A=\frac12\sum_u h(\sigma_u a,b,N),\qquad
B=\frac12\sum_v h(a,\sigma_v b,N).
\tag{2.2}
\]
A one-sided X peek has value
\[
P_X=\frac12\sum_u
\max\left\{
 h(\sigma_u a,b,N),
 \frac12\sum_v h(a,\sigma_v b,A_u)
\right\}.
\tag{2.3}
\]
The symmetric Y peek is
\[
P_Y=\frac12\sum_v
\max\left\{
 \frac12\sum_u h(\sigma_u a,b,B_v),
 h(a,\sigma_v b,N)
\right\}.
\tag{2.4}
\]
Finally one may expose both fresh refill bits `(u,v)` before deciding which mismatched head to delete. The unconsumed exposed bit is retained as debt:
\[
P_{XY}=\frac14\sum_{u,v}
\max\left\{
 h(\sigma_u a,b,B_v),
 h(a,\sigma_v b,A_u)
\right\}.
\tag{2.5}
\]
Set
\[
(F^{sym}_\ell h)(a,b,N)=\max\{A,B,P_X,P_Y,P_{XY}\}.
\tag{2.6}
\]

### 2.3 X-debt state

In `A_u`, a match consumes the known refill `u` on X and a fresh Y refill:
\[
(F^{sym}_\ell h)(a,b,A_u)
=1+\frac12\sum_v h(\sigma_u a,\sigma_v b,N),\qquad a_1=b_1.
\tag{2.7}
\]
At a mismatch there are the two ordinary moves
\[
X_{clear}=h(\sigma_u a,b,N),
\qquad
Y_{keep}=\frac12\sum_vh(a,\sigma_v b,A_u),
\]
and a cross-peek move: reveal only the next fresh Y refill `v`, then choose which side to advance. If X advances, `u` is absorbed and `v` becomes Y-debt; if Y advances, `v` is absorbed and `u` remains X-debt. Hence
\[
C_A=\frac12\sum_v
\max\{h(\sigma_u a,b,B_v),h(a,\sigma_v b,A_u)\},
\tag{2.8}
\]
and
\[
(F^{sym}_\ell h)(a,b,A_u)=\max\{X_{clear},Y_{keep},C_A\}.
\tag{2.9}
\]

### 2.4 Y-debt state

Symmetrically,
\[
(F^{sym}_\ell h)(a,b,B_v)
=1+\frac12\sum_u h(\sigma_u a,\sigma_v b,N),\qquad a_1=b_1,
\tag{2.10}
\]
and at a mismatch
\[
X_{keep}=\frac12\sum_u h(\sigma_u a,b,B_v),
\qquad
Y_{clear}=h(a,\sigma_v b,N),
\]
\[
C_B=\frac12\sum_u
\max\{h(\sigma_u a,b,B_v),h(a,\sigma_v b,A_u)\},
\tag{2.11}
\]
\[
(F^{sym}_\ell h)(a,b,B_v)=\max\{X_{keep},Y_{clear},C_B\}.
\tag{2.12}
\]

### Lemma 2.1 — exact deferred-decisions realization

Equations (2.1)--(2.12) are the Bellman equations of a causal policy on two genuine independent iid binary source strings.

#### Proof

Maintain consumed indices `(i,j)`, the `ell` visible unconsumed bits of each source, and at most one debt symbol beyond one visible window. In state `N`, every refill bit queried in (2.1)--(2.5) is a previously unseen coordinate and therefore an independent fair bit. If both `(u,v)` are exposed in (2.5), exactly one side advances; the refill on that side enters its visible window and the other exposed refill is stored explicitly as `A_u` or `B_v`.

In `A_u`, no new X coordinate is queried before `u` is consumed. The cross-peek (2.8) queries one previously unseen Y refill `v`; after the action, either `u` has entered the X window and `v` is stored as `B_v`, or `v` has entered the Y window and `u` remains stored as `A_u`. Thus no exposed coordinate is forgotten or resampled. The `B_v` case is identical with X and Y swapped. Induction on decision time proves the state semantics and transition probabilities. QED.

### Theorem 2.2 — source transfer for every exact symmetric-debt subsolution

If a finite potential satisfies
\[
F^{sym}_\ell h\ge h+\rho\mathbf1,
\tag{2.13}
\]
then
\[
\boxed{\gamma_2\ge\frac{2\rho}{1+\rho}.}
\tag{2.14}
\]

#### Proof

Choose an action attaining each maximum. In `N` the choice may depend on newly exposed actual bits exactly as encoded above; debt states preserve those bits. For `N` alignment decisions, let `R_N` be matches earned and `I_N,J_N` symbols consumed. Telescoping (2.13) gives
\[
\mathbf E R_N\ge N\rho-\operatorname{osc}(h).
\tag{2.15}
\]
Each decision is either a match, consuming two symbols and earning one reward, or a skip, consuming one symbol and earning zero. Therefore pathwise
\[
I_N+J_N=N+R_N.
\tag{2.16}
\]
At a block end, at most `ell` visible unconsumed coordinates and one debt coordinate have been exposed on either side, so discarding through `I_N+ell+1` and `J_N+ell+1` leaves fresh independent iid tails.

Pair an X/Y-oriented block with an independent string-swapped copy, exactly as in the preceding R17 transfer. The expected source usage on each side per pair is
\[
N+\mathbf E R_N+2(\ell+1),
\]
while expected matched reward is `2 E R_N`. The strong law for iid block pairs and (2.15) give
\[
\gamma_2\ge\lim_{N\to\infty}
\frac{2(N\rho-O(1))}{N+N\rho+O(1)}
=\frac{2\rho}{1+\rho}.
\]
QED.

The process has exactly
\[
5\,4^\ell
\]
formal states. This theorem is independent of any convergence assertion for value iteration.

## 3. Exact symmetric-debt certificate

The exact checker is

`artifacts/prob10_2026-09-20/PROB10-02/20260920T1220Z_r17_single_debt_macro_exact_71e4.py`

created at commit `cf2499521ccb73ae922a75f79992e1d35a5aca7f`; archived stdout is

`artifacts/prob10_2026-09-20/PROB10-02/20260920T1220Z_r17_single_debt_macro_exact_71e4.out`

created at commit `bcdd04d88e49ab807751c010f7ef3eca53383555`.

The implementation is exact integer arithmetic. If `h_t=(F^{sym}_\ell)^t0`, then all values are dyadic; the checker scales `h_t` by `4^t`, so every average and every `max` is represented by integers. For each displayed width it globally scans
\[
\rho_t^-=\min_s[(F^{sym}_\ell h_{t-1})(s)-h_{t-1}(s)],
\]
which is itself an exact componentwise subsolution certificate.

At `ell=8`, `t=50`, it proves
\[
\rho^-_8=
\frac{3014373493230485623481}{4722366482869645213696}
\approx0.638318416024065.
\tag{3.1}
\]
Theorem 2.2 therefore gives the exact source-valid mechanism lower
\[
\boxed{
\gamma_2\ge
\frac{6028746986460971246962}{7736739976100130837177}
\approx0.779236087174264.
}
\tag{3.2}
\]
This is strictly stronger than R17's preceding one-sided-debt certificate
\[
\frac{12586618}{16293309}\approx0.7725022584424073,
\]
by about `0.0067338287318563` at the mechanism/source-transfer level.

However
\[
0.779236087174264<0.792665992=L,
\]
so (3.2) does **not** move the repository's source lower endpoint. The exact `rho` threshold required to beat `L` remains
\[
\rho>\frac{99083249}{150916751}\approx0.6565424205295806.
\tag{3.3}
\]
The `ell=8` residual upper diagnostic is about `0.638350900772609`; it is not used as a source theorem.

One falsification point from the idea note is worth recording: action-set containment alone does **not** automatically prove a Bellman-eigenvalue monotonicity theorem from the one-sided to the five-status process, because the enlarged system also adds `B_v` subsolution constraints. No such monotonicity theorem is used. The exact global residual (3.1) is the certificate.

## 4. Attack B — an exact binary run-exhaustion recurrence

The binary alphabet gives a structural fact that is absent for larger alphabets.

Let finite nonempty strings start with opposite bits. Write
\[
A=x^r\bar x\,A',\qquad B=\bar x^s x\,B'
\tag{4.1}
\]
for their initial run lengths, whenever both runs end before the finite boundary. Then an optimal alignment need never delete symbols from **both** initial runs before its first match.

### Lemma 4.1 — run-exhaustion recurrence

Under (4.1),
\[
\boxed{
LCS(A,B)=
\max\Bigl\{
1+LCS(A',B_2B_3\cdots),
1+LCS(A_2A_3\cdots,B')
\Bigr\}.
}
\tag{4.2}
\]
Equivalently, before the first match an optimum may be chosen to exhaust exactly one of the two opposing leading runs and delete nothing from the other.

#### Proof

Start from any optimal alignment. Until its first matched pair, all deleted X symbols equal `x` and all deleted Y symbols equal `bar x`; the current heads remain opposite as long as both leading runs are unexhausted. Suppose the X run is the first run exhausted. If the alignment deleted `k>0` symbols from the Y leading run beforehand, restore those `k` deleted `bar x` symbols. The first X symbol after the run is `bar x`, so it can be matched to the **first** Y head instead; restoring earlier Y symbols cannot remove any later feasible match because the post-match Y suffix is only longer. Hence there is an optimum with zero Y deletions before exhausting the X run. The symmetric argument applies when the Y run is exhausted first.

Once one run is exhausted, the new head equals the untouched opposite head and matching equal heads is weakly optimal by the standard LCS recursion. This gives (4.2). QED.

The earlier R17 counterexample `A=010011,B=110100` therefore did **not** refute run exhaustion itself. It refuted only the stronger false claim that the *shorter* leading run is always the correct one to exhaust.

## 5. Finite-window run-macro average-cost process

Lemma 4.1 turns every mismatch episode into one macro choice: exhaust the X run or exhaust the Y run, then take the forced first match. Every macro emits exactly one matched symbol.

Fix visible window length `ell`. At equal heads, the macro simply matches them, total symbol cost `2`, and shifts both windows by one fresh bit.

At opposite heads let `r(a)` be the visible leading-run length of `a`.

### 5.1 Visible run end

If `r(a)<ell`, the X run ends inside the window. Exhausting X consumes `r(a)` skipped X symbols, then consumes the visible flipped X symbol together with the first Y symbol as a match. Hence the total two-string symbol cost is
\[
c_X=r(a)+2.
\tag{5.1}
\]
The new X window consists of the remaining visible suffix after that matched flip plus `r(a)+1` fresh X bits; the Y window shifts by one fresh Y bit. This is a finite dyadic transition determined by genuine refill bits.

### 5.2 Run fills the visible window

If `r(a)=ell`, the actual run continues beyond the window by
\[
G\in\{0,1,2,\ldots\},\qquad \Pr(G=g)=2^{-(g+1)},
\]
where `G` counts additional copies of the current bit before the first flip. Exhausting X has total symbol cost
\[
ell+G+2,
\]
so
\[
\mathbf E c_X=\ell+3.
\tag{5.2}
\]
After the first flipped X symbol is matched and consumed, the next `ell` X symbols are a fresh uniform binary window independent of `G`; the Y window merely shifts once. Thus the apparently unbounded run can be integrated out **exactly** with no truncation approximation.

The Y action is symmetric.

Define the finite average-cost Bellman operator `T_ell` on ordinary window potentials `H(a,b)` by taking the forced equal-head transition with cost `2`, and at a mismatch taking the minimum of the exact X-run and Y-run exhaustion expectations just described.

### Lemma 5.1 — macro process is source-valid

Every stationary policy for `T_ell` is realized by two genuine iid binary source strings, and every macro step contributes exactly one common-subsequence symbol.

#### Proof

For a visible run end, the action uses only already visible symbols and then queries exactly the iid refill bits needed for the next windows. For a full-window run, the policy has already committed to exhausting that side; sequentially reveal its tail until the first flip. Those inspected pre-flip bits and the flip itself are all consumed by the macro. By the iid strong Markov/deferred-decisions property, the `ell` symbols after the consumed flip form a fresh independent uniform window and are independent of the geometric extension length. The other source advances only through its matched head and one ordinary refill. Repeating gives exactly the transition kernel of `T_ell`. Lemma 4.1 ensures each macro corresponds to a legitimate first-match branch of an LCS alignment. QED.

### Theorem 5.2 — exact cost-dual transfer

If a finite potential `H` and scalar `c` satisfy
\[
T_\ell H\le H+c\mathbf1,
\tag{5.3}
\]
then
\[
\boxed{\gamma_2\ge\frac2c.}
\tag{5.4}
\]

#### Proof

Use at every macro the action attaining the minimum in `T_ell`. For `N` macro steps, exactly `N` matches are produced. Let `C_N=I_N+J_N` be total source symbols consumed. Telescoping (5.3) gives
\[
\mathbf E C_N\le Nc+\operatorname{osc}(H).
\tag{5.5}
\]
At a macro boundary the only exposed unconsumed information is the two visible `ell`-windows; any farther symbols inspected during a long-run search were consumed. Discard `ell` positions beyond both consumed indices, and fresh independent iid tails remain.

Pair a block with an independent string-swapped copy. If the first block consumes `(I,J)` and the unswapped law of the second copy is `(I',J')`, then after swapping, expected usage of either source per pair is
\[
\mathbf E(I+J')+2\ell=\mathbf E C_N+2\ell,
\]
while the pair creates `2N` matches. The iid block-pair strong law and (5.5) yield
\[
\gamma_2\ge\lim_{N\to\infty}
\frac{2N}{Nc+O(1)}=\frac2c.
\]
QED.

This is a second stationary variational lower characterization with an exact finite-to-infinite transfer. It is structurally different from the per-symbol debt process.

## 6. Exact macro certificates and their present limitation

The same checker represents `T_ell` exactly with integers. It uses a common denominator
\[
Q=2^{\ell+1}
\]
per macro iteration, large enough for every visible-run transition and the uniform full-window transition. For `H=T_ell^{t-1}0`, the global quantity
\[
c_t^+=\max_{a,b}(T_\ell H-H)(a,b)
\]
is an exact supersolution cost in (5.3).

The strongest archived exact macro computation in this bounded run is `ell=5,t=25`:
\[
c^+=
\frac{222471995239406752512658952706231585727}
{85070591730234615865843651857942052864}
\approx2.615145736200855.
\]
Therefore Theorem 5.2 gives
\[
\gamma_2\ge
\frac{170141183460469231731687303715884105728}
{222471995239406752512658952706231585727}
\approx0.764775734030599.
\tag{6.1}
\]
This is source-valid but weaker than both the symmetric-debt mechanism certificate (3.2) and the established source lower endpoint. Its value here is the exact structural reduction and transfer, not an endpoint claim.

## 7. Attack C — head/run-only macro quotient fails exactly

The obvious scaling attempt after Lemma 4.1 is to quotient states only by

- the two head bits, and
- the two visible leading-run lengths.

That quotient is not Bellman exact, even starting from the zero potential.

Take `ell=4` and the two mismatch states
\[
(a,b)=(0000,1001),\qquad (a,b')=(0000,1010).
\]
Both have the same summary
\[
(a_1,b_1,r(a),r(b))=(0,1,4,1).
\]
But the exact integer checker gives, after two macro Bellman iterations,
\[
(T_4^2 0)(0000,1001)=5,
\qquad
(T_4^2 0)(0000,1010)=6.
\tag{7.1}
\]
The computation uses common scale `1024`, with integer values `5120` and `6144` respectively. Therefore no exact Bellman quotient retaining only heads and leading-run lengths can preserve even `T_4^2 0`.

This is the promised exact obstruction to the simplest run-based compression. Any scalable macro potential must retain some tail information beyond the first runs.

## 8. Verification summary

The archived exact checker/output verify:

1. exact symmetric-debt Bellman residual scans through `ell=8`;
2. the exact `ell=8,t=50` subsolution (3.1) and transferred rational (3.2);
3. strict improvement over the preceding R17 one-sided-debt mechanism certificate;
4. exact macro cost Bellman scans through `ell=5`;
5. the exact macro transfer certificate (6.1);
6. the run/head quotient counterexample (7.1).

The output ends

`ALL_EXACT_CHECKS_PASS`

and

`RETURN_CODE=0`.

Self-checking is not an independent audit.

## 9. Before/after separated by level

### Source-level metric

Before:
\[
L\le\gamma_2\le U_{new},\qquad W_{before}=U_{new}-L.
\]
After:
\[
L\le\gamma_2\le U_{new},\qquad \boxed{W_{after}=W_{before}.}
\]
No R17 source endpoint moves.

### Mechanism / auxiliary progress

This run proves:

- a five-status symmetric single-debt Bellman process preserving all source dependence;
- its source transfer `gamma_2 >= 2 rho/(1+rho)`;
- an exact `ell=8` mechanism certificate `gamma_2 >= 0.779236087174264...`, improving R17's preceding mechanism certificate by about `0.00673383` but still below `L`;
- the binary run-exhaustion recurrence (4.2);
- an exact finite run-macro average-cost process with source transfer `gamma_2>=2/c`;
- an exact obstruction to a head/run-only Bellman quotient.

## 10. Exact unresolved full-scope gap and next route

The Chvátal--Sankoff binary constant remains unresolved. This run does not determine `gamma_2`, beat the rigorous lower `L`, improve `U_new`, or supply the independent audits required for closure.

The concrete symmetric-debt lower target is now
\[
\boxed{
\text{find an exact }F^{sym}_\ell\text{ subsolution with }
\rho>\frac{99083249}{150916751}.
}
\]
At `ell=8` the exact certificate has only reached `rho≈0.6383184160`, so raw-width scaling alone is still not enough.

The genuinely different next method within this problem is to combine Lemma 4.1 with a **tail-sensitive structured potential** rather than another behavioral quotient: retain exact leading runs plus a small number of post-run interaction features, derive a global exact separation oracle for the macro cost inequality, and reject the ansatz unless the globally checked cost `c` falls below
\[
\frac{2}{L}\approx2.523132\ldots.
\]
The exact counterexample (7.1) shows why pure run lengths are insufficient. A parallel route is a coupled-debt envelope for `A_u/B_v` with a proved finite truncation; unlike the previous one-sided Snell process, orientation switching can preserve a perturbation across a mismatch, so the old scalar `2^{-r}` argument cannot simply be copied.

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
    - "exact five-status symmetric single-debt source process"
    - "proved transfer gamma_2 >= 2 rho/(1+rho)"
    - "ell=8 exact rho=3014373493230485623481/4722366482869645213696"
    - "transferred mechanism lower 6028746986460971246962/7736739976100130837177"
    - "proved exact binary run-exhaustion recurrence"
    - "proved run-macro cost transfer gamma_2 >= 2/c"
    - "exact head/run quotient counterexample"
  current_lower_metric_target: "rho > 99083249/150916751 or macro c < 2/L"
  h0021: "released/unassigned; Delta_near=2 and all historical counters preserved"
  closure: false
```

No schedule, cadence, enabled state, email, Drive item, public posting, workflow, purchase, permission, root ledger, or peer claim file was modified.