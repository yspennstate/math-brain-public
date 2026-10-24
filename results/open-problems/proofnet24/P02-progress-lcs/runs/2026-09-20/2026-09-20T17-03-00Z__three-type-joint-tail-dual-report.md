Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.** GPT-6 / maximum reasoning was requested, but this runtime exposes no authenticated model/effort selector or applied-effort receipt.

# P02 / T02 — exact three-type joint-tail dual and strict source-interval shrink

## 0. Original problem, source status, and before / after

Target:
\[
\gamma_2=\lim_{n\to\infty}\frac{\mathbf E\,LCS(X_1^n,Y_1^n)}n
\]
for two independent iid uniform binary strings. All transfers below retain the dependence induced by the two source strings; the independent Bernoulli matching model is not substituted.

Fresh source checking on 20 September 2026 rechecked Alexander Tiskin, `arXiv:2212.01582v2`. The arXiv record says the binary coefficient remains unresolved; v2 is dated 2024-08-13; and its comments explicitly say that claims in the preprint concerning the stochastic process and `gamma` turned out to be incorrect and were omitted from v2. None of those withdrawn claims is used here.

The rigorous public lower endpoint retained by the project is
\[
L=0.792665992=\frac{99083249}{125000000},
\]
from Heineman--Miller--Reichman--Salls--Sarkozy--Soiffer, `arXiv:2407.10925`. Their abstract records the conventional rigorous public upper endpoint `0.826280`. Li--Ren--Wen, published online by Cambridge on 2026-03-02, still describe determination of the two-string binary constant as open and summarize the public range as roughly `0.792665 <= gamma <= 0.826280`.

The latest durable P02 certificate entering this run was

`proofnet24/P02-progress-lcs/runs/2026-09-20/2026-09-20T16-03-00Z__terminal-slack-minimization-dual-report.md`,

blob `d4e06dbb448580078c0840dcae12ebc6b4284f0b`. Under the frozen gauge-correct C045 operator/witness and the already-proved actual-string covering transfer it proved
\[
L\le\gamma_2\le U_{ts},
\qquad
U_{ts}=\frac{\log(4t^2)}{\log\lambda_{ts}}.
\]

This run proves a stronger exact finite dual rate `lambda_jt < lambda_ts`, hence
\[
\boxed{L\le\gamma_2\le U_{jt}<U_{ts}},
\qquad
U_{jt}=\frac{\log(4t^2)}{\log\lambda_{jt}}.
\]
An exact rational logarithm enclosure proves
\[
\boxed{
U_{jt}<
0.82627594276228262501510658153729663282346199619319002388080618331256294443
<U_{ts}.
}
\]
Therefore the certified repository-internal width strictly decreases from `U_ts-L` to `U_jt-L`.

Diagnostic high precision, not used as proof, gives
\[
U_{jt}=0.8262759427622826250151065815372966328234619961931900238808061833125629444296833501608\ldots,
\]
\[
U_{ts}-U_{jt}\approx3.76575428417548\times10^{-76},
\]
and
\[
U_{jt}-L\approx0.03360995076228262501510658153729663282346199619319002388080618331256294442968.
\]

Status: **PARTIAL / source OPEN / exact repository-internal candidate pending later independent review and public-priority checking.**

## 1. Scope continuity, handoff, exclusions, and nonduplication

Controlling policy: `operations/PROGRESS20_2026-09-20.md`, blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`. Root `POSTED.md` was checked; no posting exclusion covers T02.

Brief handoff of P02's actual pre-T02 target: the former Aldous--Fill occupation-time target remains closure-packaged at frozen `11/11`; it is not reopened.

Essential C045 dependency recovered:

`runs/R17/20260918_0926Z_fullcap6_c045_f7a1.md`, blob `1a3b57364d1cc744acd2c3d9397abaeed5a86aab`.

That report proves the gauge-correct full six-factor covering language, the forward-reachable product with `11,614,187` states, an exact all-row positive cone certificate, and the dependence-preserving bivariate covering/diagonal transfer
\[
\gamma_2\le \frac{\log(4xy)}{\log\lambda}
\]
whenever the reachable covering operator at `(x,y)` has spectral radius at most `lambda<1`. C033--C035 remain withdrawn because of the complement-gauge bug; C045 retains the C036 cocycle repair.

Newest same-source companion P13 report recovered:

`proofnet24/P13-progress-lcs/runs/2026-09-20/2026-09-20T16-15-00Z__shield-bisimulation-terminal-event-k63.md`, blob `519c053c69042a1cf38efe622200aa8b1da3006c`.

P13 works the genuine-source strip/boundary lane. It proves a leading-one shield bisimulation and a strict `k=63` contraction for its width-six terminal event, but explicitly reports no source endpoint movement. This does not duplicate the covering/cone arithmetic below.

A current complementary R17 report is

`runs/prob10_2026-09-20/PROB10-02/20260920T1458Z_r17_equivariant_lookahead_atom_5d8e.md`, blob `2a97a4ebd2ec6efdde34155b38bbafb14a8fd300`.

R17 develops a constructive finite-lookahead lower mechanism with a proved synchronizing atom and obtains `gamma_2 >= 0.78128135`, below the retained public lower endpoint `0.792665992`; hence no source movement there. P05's renewal/finite-state route is likewise lower-side and remains below the retained public lower endpoint. P02 stays on the complementary finite covering/cone upper-dual lane.

No historical or peer file is overwritten. No email, Drive, public posting, paid compute, workflow, permission, access, or schedule change is performed.

## 2. Prior LCS attempts relevant to this run

The public rigorous progression recovered from the current sources includes Chvatal--Sankoff (1975), Deken (1979), Dancik/Paterson (1990s), Lueker (2009), and the 2024 lower-bound improvement. Lueker's rigorous binary interval was `0.788071 <= gamma_2 <= 0.826280`; the 2024 work raises the rigorous lower endpoint to `0.792665992`. Tiskin's stochastic-process approach supplies an estimate but v2 explicitly removes earlier incorrect claims. Recent literature in 2026 still treats the exact constant as open.

Repository-internally, the useful upper-side chain is the gauge-correct C045 covering certificate followed by P02's exact Collatz/dual strictifications. The immediately preceding durable P02 theorem used a terminal-slack minimization defect
\[
D_{ts}=\frac72D_{mm}.
\]
This run changes the terminal mechanism: instead of enumerating type 6 and then minimizing type-7 slack, it solves types `5,6,7` jointly from exact row mass and congruence constraints.

## 3. Frozen C045 arithmetic and inherited two-step identity

Put
\[
t=\frac pq=\frac{256717}{800000},\qquad d=q-p=543283,
\]
\[
S=q^6d,\qquad A=t^2H,\qquad B=SH.
\]
The primitive label coefficients are
\[
c_k=q^{6-k}dp^k\quad(0\le k\le6),
\qquad c_7=p^7,
\]
with multiplicities
\[
(m_0,\ldots,m_7)=(2,4,4,4,4,4,4,4).
\]
Because `gcd(p,q)=gcd(p,d)=1`, each `c_k` has exact `p`-adic valuation `k` for `0<=k<=6`.

The inherited positive integer cone witness satisfies
\[
1\le V_i\le M=5\cdot10^{18},
\qquad
BV\le\frac abV,
\]
where
\[
a=1995237757733917147310102692686664915858011319606812684127301,
\]
\[
b=4220452010631561279,
\qquad b\le M<2b.
\]
Define
\[
s_i=aV_i-b(BV)_i\ge0,
\qquad T_i=(Bs)_i.
\]
Then rowwise
\[
\boxed{a^2V_i-b^2(B^2V)_i=a s_i+bT_i.}\tag{3.1}
\]
Let
\[
\alpha=a\bmod b=1884560463669269501,
\qquad h=707440146652911839,
\]
so `alpha*h == 1 (mod b)`. Hence every successor coordinate obeys
\[
\boxed{V_j\equiv hs_j\pmod b.}\tag{3.2}
\]

For a coefficient type `k`, let `R_k` be the sum of successor slacks and `W_k` the sum of successor witness values over accepted labels of that type, rejected labels contributing zero. Then
\[
\boxed{W_k\equiv hR_k\pmod b},
\qquad0\le W_k\le m_kM.\tag{3.3}
\]
The exact row equation is
\[
\boxed{u:=\frac{aV-s}{b}=\sum_{k=0}^7c_kW_k.}\tag{3.4}
\]

The preceding mixed-modulus theorem defined
\[
D_{mm}=
\frac{655209040831815247751186134103526570372190622578374697627001555}
{925139970226099634}.
\]
This run proves the much larger universal defect
\[
\boxed{D_{jt}=9D_{mm}}
=
\frac{5896881367486337229760675206931739133349715603205372278643013995}
{925139970226099634}.\tag{3.5}
\]
Since `D_ts=(7/2)D_mm`,
\[
\boxed{\frac{D_{jt}}{D_{ts}}=\frac{18}{7}>2.57.}\tag{3.6}
\]
Thus the finite dual defect improves by more than a factor `2.57` over the previous durable theorem.

## 4. Prefix mixed-modulus reduction through type 4

Suppose an actual row violates
\[
\frac{a s_i+bT_i}{V_i}\ge D_{jt}.\tag{4.1}
\]
Since `V_i<=M`, the parent term alone excludes every
\[
s\ge C:=\left\lceil\frac{D_{jt}M}{a}\right\rceil=15974.
\]
Thus only `0<=s<15974` matters. Relation (3.2) and `M<2b` leave exactly `18,926` residue/range-compatible parent pairs `(s,V)`.

For each type `k`, after types `<k` are fixed, exact `p`-adic valuation forces one residue
\[
W_k\equiv z_k\pmod p.\tag{4.2}
\]
The inherited exact aggregate-lift parameterization
\[
W_k=hR_k-nb
\]
combines (3.3), (4.2), the witness range and the strict defect budget without enumerating impossible raw slack values.

Applying this exact relaxation through types `0,...,4` gives the complete state chain
\[
\boxed{18926\to1533\to1182\to2256\to11286\to148080}.\tag{4.3}
\]
The corresponding exact `n`-scan counts are
\[
28041558,\ 10574353,\ 20489512,\ 102171516,\ 1345424982,
\]
and the maximum type budgets are
\[
52727,\ 150782,\ 423248,\ 1165159,\ 3515813.
\]
These are theorem-critical counts, checked exactly by the archived C++ program.

## 5. New theorem: exact three-type joint-tail closure

This is the substantive new mechanism.

Fix a surviving prefix through type 4. Put
\[
E=\frac{u-\sum_{k=0}^4c_kW_k}{p^5}.
\]
For an actual row with nonnegative residual mass, exact row equality becomes
\[
\boxed{
E=qd\,W_5+pd\,W_6+p^2W_7.
}\tag{5.1}
\]
Define the correspondingly weighted tail slack
\[
\boxed{
Q=qd\,R_5+pd\,R_6+p^2R_7.
}\tag{5.2}
\]
By (3.3),
\[
E\equiv hQ\pmod b,
\]
so
\[
\boxed{Q\equiv\alpha E\pmod b.}\tag{5.3}
\]
The strict violation budget gives an exact upper bound `Q<=Qmax`; with rational `D_jt=N/D`, the checker uses
\[
Q_{max}=
\left\lfloor
\frac{NV-D\,\mathrm{used}_{0:4}-1}
{D\,b\,p^5}
\right\rfloor.\tag{5.4}
\]
Therefore every violating row must have
\[
Q=r+jb,\qquad r=(\alpha E)\bmod b,
\qquad 0\le Q\le Q_{max}.\tag{5.5}
\]
This immediately eliminates `104,175` of the `131,080` positive-residual prefixes.

For every remaining value of `Q`, solve the tail slack equation exactly. Since
\[
Q=qdR_5+p(dR_6+pR_7),\tag{5.6}
\]
and `qd` is invertible modulo `p`,
\[
\boxed{R_5\equiv(qd)^{-1}Q\pmod p.}\tag{5.7}
\]
For each nonnegative `R_5` in range, put
\[
Q_2=\frac{Q-qdR_5}{p}.
\]
Then
\[
Q_2=dR_6+pR_7,
\]
and `d` is invertible modulo `p`, so
\[
\boxed{R_6\equiv d^{-1}Q_2\pmod p,}\tag{5.8}
\]
with `R_7` then forced. Equations (5.7)--(5.8) enumerate **all** nonnegative tail slack triples. Across the complete prefix set they produce exactly
\[
\boxed{3,529,814}
\]
relaxed slack triples.

It remains to impose exact witness mass, not merely slack congruence. For a fixed `R_5`, (3.3) says
\[
W_5=(hR_5\bmod b)+\ell_5b,
\]
and because `0<=W_5<=4M<5b`, only finitely many `ell_5` (`0,...,4`) are possible. For each such lift, (5.1) becomes
\[
\frac{E-qdW_5}{p}=dW_6+pW_7.\tag{5.9}
\]
Likewise
\[
W_6=(hR_6\bmod b)+\ell_6b,
\qquad0\le\ell_6\le4,
\]
and then (5.9) forces `W_7` exactly. The checker requires
\[
0\le W_7\le4M,
\qquad W_7\equiv hR_7\pmod b.
\tag{5.10}
\]

**No** one of the `3,529,814` relaxed slack triples admits even a relaxed witness lift satisfying (5.9)--(5.10):
\[
\boxed{\texttt{witness_lifts}=0.}\tag{5.11}
\]
This relaxation ignores actual successor identities, coincidences and decomposability of the aggregate sums, so every genuine C045 row maps into the searched relaxed set. Zero relaxed survivors therefore proves that no actual row violates (4.1).

Hence every actual row satisfies
\[
\boxed{
\frac{a s_i+bT_i}{V_i}\ge D_{jt}.
}\tag{5.12}
\]
Combining with (3.1),
\[
\boxed{
B^2V\le\frac{a^2-D_{jt}}{b^2}V.
}\tag{5.13}
\]

The executed exact checker ends

`PREFIX_MIXED_MODULUS_ENUMERATION=PASS`,
`EXACT_THREE_TYPE_JOINT_TAIL_CLOSURE=PASS`,
`GLOBAL_TWO_STEP_DEFECT_9_DMM=PASS`, and
`ALL_EXACT_CHECKS_PASS`.

## 6. Spectral strictification

Define
\[
R=\frac ab,
\qquad
\beta_{jt}=R-\frac{D_{jt}}{2ab}.
\tag{6.1}
\]
Then
\[
\beta_{jt}^2
=
\frac{a^2-D_{jt}}{b^2}
+
\frac{D_{jt}^2}{4a^2b^2}
>
\frac{a^2-D_{jt}}{b^2}.
\]
By Collatz monotonicity on the positive witness,
\[
\rho(B)^2\le\frac{a^2-D_{jt}}{b^2},
\]
so
\[
\boxed{\rho(B)<\beta_{jt}.}\tag{6.2}
\]
Since `D_jt>D_ts`,
\[
\beta_{jt}<\beta_{ts}.
\]
Rescaling to the actual finite covering operator,
\[
\lambda_{jt}=\frac{t^2}{S}\beta_{jt},
\]
therefore gives
\[
\boxed{\rho(A)<\lambda_{jt}<\lambda_{ts}<1.}\tag{6.3}
\]

## 7. Dependence-preserving finite-to-infinite transfer

The C045 covering operator enumerates accepted collations of **actual ordered binary source-string pairs**. It does not assign independent probabilities to the `n^2` match indicators.

The already-proved C027/C045 covering transfer says that if the finite reachable covering operator at fugacities `(x,y)` has spectral radius below `z<1`, finite dimensionality and positivity give an accepted-weight bound of the form `K_z z^m`. Every actual pair of independent uniform binary strings of length `n` has probability exactly `4^{-n}`. Because every physical pair with `LCS>=m` has at least one accepted covering collation,
\[
\Pr\{L_n\ge m\}\le K_z(4xy)^{-n}z^m.
\tag{7.1}
\]
No cellwise Bernoulli-independence assumption appears.

Taking `m` proportional to `n`, summing the exponentially small upper tail and passing to `n->infinity` yields
\[
\boxed{\gamma_2\le\frac{\log(4xy)}{\log z}.}\tag{7.2}
\]
At
\[
x=y=t=256717/800000,
\qquad z=\lambda_{jt},
\]
this is `U_jt`. Since `lambda_jt<lambda_ts<1`, monotonicity of `log(4t^2)/log z` on `(0,1)` gives `U_jt<U_ts`.

The endpoint checker encloses each negative logarithm using 300 terms of the positive `atanh` series plus an exact rational geometric remainder and certifies the strict decimal separator in Section 0. It ends

`D_NEW_EQ_18_OVER_7_D_PREV=PASS`,
`EXACT_TWO_STEP_SPECTRAL_MAJORANT=PASS`,
`EXACT_LOG_INTERVALS_DISJOINT=PASS`,
`SOURCE_INTERVAL_STRICTLY_SHRINKS=PASS`,
`LOWER_ENDPOINT_RETAINED=PASS`, and
`ALL_EXACT_CHECKS_PASS`.

## 8. Essential soundness checks, failed scout, and residual obstruction

Immediate exact checks performed in the finite program include:

- `alpha*h == 1 (mod b)`;
- exact `p`-adic valuation `v_p(c_k)=k` for `0<=k<=6`;
- exact parent count and every prefix state/scan/budget count;
- exact divisibility of the residual row mass by `p^5`;
- complete enumeration of every congruent `Q=r+jb` below the violation budget;
- complete nonnegative Diophantine enumeration of `(R_5,R_6,R_7)` by (5.7)--(5.8);
- all allowed aggregate witness lifts under `W_k<=4M`;
- exact row equality and terminal congruence.

The preceding `3.5D_mm` checker was separately reproduced during development; the new joint-tail closure also gives zero violating terminal triples there, consistent with the older terminal-slack theorem.

A `19/2 D_mm` (`9.5D_mm`) exploratory run did not finish inside the bounded local execution window, so **no claim above `9D_mm` is made**. This is not evidence of failure of the theorem at `9.5`; it is only an execution-limit obstruction in the current prefix enumerator.

The next useful mechanism is now clear. The three-type joint-tail theorem removes the former type-6 explosion, but the type-4 prefix stage already performs about `1.345e9` exact lift scans at `9D_mm`. A materially stronger next run should move the same joint-tail congruence one type earlier: after types `0,...,3`, divide the exact residual equation by `p^4`, form the four-type weighted slack total for `k=4,5,6,7`, use its single modulo-`b` class plus successive modulo-`p` elimination to solve the final four slack coordinates by a low-dimensional CRT/lattice parameterization, and only then lift aggregate witnesses. Repeating a larger raw type-4 scan would be the wrong mechanism.

## 9. Artifact manifest

Exact finite checker:

`proofnet24/P02-progress-lcs/artifacts/2026-09-20T17-03-00Z__three_type_joint_tail_checker.cpp`

- creation commit `9a767b8c0d2026edcec55002ef66d3f468be5434`
- verified blob `cb68fe8d1a0d7d880fb195b630a2c4fd5944e9f6`.

Executed output:

`proofnet24/P02-progress-lcs/artifacts/2026-09-20T17-03-00Z__three_type_joint_tail_checker.out`

- creation commit `faa315915887f71c9fe03014fd7e0e9ccce37d06`
- verified blob `b93050a640c27276eb75d3c21c38098396ef97da`.

Exact endpoint checker:

`proofnet24/P02-progress-lcs/artifacts/2026-09-20T17-03-00Z__three_type_joint_tail_endpoint_checker.py`

- creation commit `1d95591241afc9550c301aff1fa96fee6251eb8c`
- verified blob `3bf19a5e97306a239580598a93ada3bee5e6ba00`.

Executed endpoint output:

`proofnet24/P02-progress-lcs/artifacts/2026-09-20T17-03-00Z__three_type_joint_tail_endpoint_checker.out`

- creation commit `313a4dc6b698b69532b09a86c30741fa4195a81a`
- verified blob `210181c7fa07fe9826176de178cd166084bde0e3`.

## 10. ledger_delta

```yaml
ledger_delta:
  track: P02
  parent: T02
  source: "Chvatal--Sankoff binary LCS constant for two independent iid uniform binary strings"
  status: PARTIAL
  source_status: OPEN
  model_runtime: "GPT-5.6 Sol; reasoning level UNVERIFIED; not GPT-6 maximum"
  lower_before: "99083249/125000000"
  lower_after: "99083249/125000000"
  upper_before: "U_ts = log(4 t^2)/log(lambda_ts), D_ts=(7/2)D_mm"
  upper_after: "U_jt = log(4 t^2)/log(lambda_jt), D_jt=9D_mm"
  exact_strict_separator: "U_jt < 0.82627594276228262501510658153729663282346199619319002388080618331256294443 < U_ts"
  metric_before: "U_ts - 0.792665992"
  metric_after: "U_jt - 0.792665992"
  source_movement: "strictly smaller certified repository-internal interval"
  mechanism_advance: "exact three-type joint-tail CRT/Diophantine closure for coefficient types 5,6,7"
  finite_defect_before: "D_ts=(7/2)D_mm"
  finite_defect_after: "D_jt=9D_mm"
  finite_defect_ratio: "18/7"
  dependency_model: "actual binary source-pair covering operator; no independent Bernoulli match array"
  finite_to_infinite_transfer: "retained C027/C045 covering/diagonal transfer, explicitly dependence-preserving"
  exact_parent_pairs: 18926
  prefix_chain: "18926 -> 1533 -> 1182 -> 2256 -> 11286 -> 148080"
  exact_tail_slack_triples: 3529814
  exact_tail_witness_lifts: 0
  failed_scout: "19/2 D_mm timed out locally; no claim above 9D_mm"
  residual_obstruction: "type-4 prefix lift enumeration dominates; next attack is four-type joint tail after k=3"
  companion_scope: "P13 strip/boundary shield-bisimulation lane; R17 constructive lookahead lower lane; P05 renewal lower lane"
  immutable_report: "proofnet24/P02-progress-lcs/runs/2026-09-20/2026-09-20T17-03-00Z__three-type-joint-tail-dual-report.md"
```
