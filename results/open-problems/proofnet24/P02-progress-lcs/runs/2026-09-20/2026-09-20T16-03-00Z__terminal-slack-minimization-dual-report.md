Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.** GPT-6 / maximum reasoning was requested, but this runtime exposes no authenticated model-selector or applied-effort receipt.

# P02 / T02 — terminal-slack minimization dual strictification

## 0. Original problem and source-level before / after

Target:
\[
\gamma_2=\lim_{n\to\infty}\frac{\mathbf E\,LCS(X_1^n,Y_1^n)}n
\]
for two independent iid uniform binary strings. All transfers below retain the dependence induced by the two source strings; the independent Bernoulli matching model is not substituted.

Fresh source navigation on 20 September 2026 rechecked Alexander Tiskin, `arXiv:2212.01582v2`. The arXiv record says the binary coefficient remains unresolved; v2 is dated 2024-08-13; and its comments explicitly say that claims in the preprint concerning the process and `gamma` turned out to be incorrect and were omitted from v2. None of those withdrawn claims is used here.

The rigorous published lower endpoint retained by the project is
\[
L=0.792665992=\frac{99083249}{125000000},
\]
from Heineman--Miller--Reichman--Salls--Sarkozy--Soiffer, `arXiv:2407.10925`; their abstract records the conventional rigorous upper endpoint `0.826280`.

The latest durable P02 certificate entering this run was

`proofnet24/P02-progress-lcs/runs/2026-09-20/2026-09-20T15-04-28Z__mixed-modulus-exact-tail-dual-report.md`,

blob `94d093c0949a9ddbe9f043896ff9582f83b00c03`. Under the frozen gauge-correct C045 operator/witness and the already-proved actual-string covering transfer it proved
\[
L\le\gamma_2\le U_{tail},
\qquad
U_{tail}=\frac{\log(4t^2)}{\log\lambda_{tail}}.
\]

This run proves a stronger exact finite dual rate `lambda_ts < lambda_tail`, hence
\[
\boxed{L\le\gamma_2\le U_{ts}<U_{tail}},
\qquad
U_{ts}=\frac{\log(4t^2)}{\log\lambda_{ts}}.
\]
An exact rational logarithm enclosure proves
\[
\boxed{
U_{ts}<
0.8262759427622826250151065815372966328234619961931900238808061833125629444301
<U_{tail}.
}
\]
Therefore the certified repository-internal width strictly decreases from `U_tail-L` to `U_ts-L`.

Diagnostic high precision, not used as proof, gives
\[
U_{tail}-U_{ts}\approx1.02702389568422\times10^{-76},
\]
and
\[
U_{ts}-L\approx0.03360995076228262501510658153729663282346199619319002388080618331256294443006.
\]

Status: **PARTIAL / source OPEN / exact repository-internal candidate pending later independent review and public-priority checking.**

## 1. Scope continuity, handoff, exclusions, coordination

Controlling policy: `operations/PROGRESS20_2026-09-20.md`, blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`. Root `POSTED.md` was checked; no posting exclusion covers T02.

Brief handoff of P02's actual pre-T02 target: the former Aldous--Fill occupation-time target remains closure-packaged at frozen `11/11`; it is not reopened.

Newest same-source companion P13 report recovered:

`proofnet24/P13-progress-lcs/runs/2026-09-20/2026-09-20T15-47-00Z__terminal-gradient-coboundary-transfer.md`, blob `2d5c79ab75a947f2deb72b13dd22825fc46ac56f`.

P13 works the genuine-source strip/Bellman/boundary lane and proves an all-width terminal-gradient coboundary transfer. It explicitly carries P02's source upper endpoint rather than duplicating this covering/cone arithmetic.

A current complementary LCS owner, P05, has

`probability_campaigns/progress_first_2026-09-20/P05/renewal/2026-09-20T15-38-00Z__report.md`, blob `18ff5d361b6b9504de7cfcd1d21c5d66d69fba80`.

P05 develops an exact renewal/finite-state lower route. Its reported source-valid renewal lower certificate remains below the retained published `0.792665992`, so it does not duplicate P02's upper-dual movement.

No historical or peer file is overwritten. No email, Drive, public posting, paid compute, permission, workflow, access, or schedule change is performed.

## 2. Frozen C045 data and inherited two-step identity

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
Because `gcd(p,q)=gcd(p,d)=1`, each `c_k` has exact `p`-adic valuation `k`.

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
\boxed{a^2V_i-b^2(B^2V)_i=a s_i+bT_i.}\tag{2.1}
\]
Let
\[
\alpha=a\bmod b=1884560463669269501,
\qquad h=707440146652911839,
\]
so `alpha*h == 1 (mod b)`. Hence
\[
\boxed{V_i\equiv hs_i\pmod b.}\tag{2.2}
\]

The preceding mixed-modulus report proved
\[
D_{mm}=
\frac{655209040831815247751186134103526570372190622578374697627001555}
{925139970226099634},
\]
and the immediately preceding exact-tail run improved the universal defect to
\[
D_{tail}=2D_{mm}.
\]

This run proves
\[
\boxed{D_{ts}=\frac72D_{mm}}
=
\frac{4586463285822706734258302938724685992605334358048622883389010885}
{1850279940452199268}.
\tag{2.3}
\]
Thus
\[
\boxed{D_{ts}=\frac74D_{tail}},
\]
a 75% finite-defect improvement over the previous durable theorem.

## 3. Exact aggregate-lift compression lemma

For coefficient type `k`, let `R_k` be the total successor slack and `W_k` the total successor witness value over accepted labels of that type, rejected labels contributing zero. The inherited relation is
\[
\boxed{W_k\equiv hR_k\pmod b},
\qquad0\le W_k\le m_kM.
\tag{3.1}
\]
The row equation is
\[
\boxed{u:=\frac{aV-s}{b}=\sum_{k=0}^7c_kW_k.}\tag{3.2}
\]
After types `<k` are fixed, exact `p`-adic valuation gives a forced residue
\[
W_k\equiv z_k\pmod p.
\tag{3.3}
\]

The preceding checker enumerated every integer `R_k` in its defect budget. The new observation reparameterizes the two congruences exactly and reduces the search dimension.

From (3.1), for some integer `n`,
\[
\boxed{W_k=hR_k-nb.}\tag{3.4}
\]
Conversely, any integers `(n,R_k)` satisfying (3.4), `0<=W_k<=m_kM`, recover (3.1). Combining (3.3) and (3.4), since `gcd(h,p)=1`,
\[
\boxed{R_k\equiv h^{-1}(z_k+nb)\pmod p.}\tag{3.5}
\]
For fixed `n`, the witness-range condition gives the exact interval
\[
\boxed{
\left\lceil\frac{nb}{h}\right\rceil
\le R_k\le
\left\lfloor\frac{nb+m_kM}{h}\right\rfloor,
}
\tag{3.6}
\]
intersected with `0<=R_k<=Rmax_k`. Its length is at most `m_kM/h<29<p`, so (3.5) permits at most one `R_k` for each `n`.

The complete `n` range is finite:
\[
\left\lceil-\frac{m_kM}{b}\right\rceil
\le n\le
\left\lfloor\frac{hRmax_k}{b}\right\rfloor.
\tag{3.7}
\]
Equations (3.5)--(3.7) therefore enumerate **exactly the same relaxed aggregate pairs `(R_k,W_k)`** as the old integer-`R_k` scan, but without checking the overwhelmingly many impossible `R_k` values. This is a proof-level reparameterization, not a heuristic pruning rule.

## 4. New terminal-slack minimization lemma

The preceding exact-tail theorem stopped after types `0,...,6` and used exact row equality to force
\[
W_7^*=\frac{u-\sum_{k=0}^6c_kW_k}{c_7}.
\tag{4.1}
\]
At `D_tail`, every surviving prefix already had `W_7^*` outside `[0,4M]`.

At the larger target `D_ts`, legal terminal witness sums do occur, so witness-range closure alone is no longer sufficient. The new step uses the terminal slack congruence itself.

For any legal forced `W_7`, (3.1) gives
\[
W_7\equiv hR_7\pmod b.
\]
Multiplying by `alpha=h^{-1} mod b`,
\[
\boxed{R_7\equiv\alpha W_7\pmod b.}\tag{4.2}
\]
Hence the least possible nonnegative terminal aggregate slack is
\[
\boxed{r_7=(\alpha W_7)\bmod b.}\tag{4.3}
\]
Every actual terminal aggregate slack has the form `r_7+jb`, `j>=0`. Because `b c_7 R_7` enters the defect with a positive coefficient, `r_7` is the **best possible** value for a hypothetical violating row. Therefore, if the violation inequality already fails at `R_7=r_7`, it fails for every actual terminal aggregate slack.

This is the substantive new dual lemma of the run: **exact row equality plus least-residue terminal slack closes branches that witness-range equality alone cannot close.**

## 5. Exact finite exclusion at `D_ts=(7/2)D_mm`

Suppose an actual C045 row violated
\[
\frac{a s_i+bT_i}{V_i}\ge D_{ts}.
\tag{5.1}
\]
Since `V_i<=M`, any `s` with `as/M>=D_ts` is immediately safe. Exact arithmetic gives cutoff
\[
C=\left\lceil\frac{D_{ts}M}{a}\right\rceil=6212.
\tag{5.2}
\]
Thus a violator has `0<=s<6212`.

By (2.2) and `M<2b`, each positive slack has at most two compatible parent witness values; for `s=0`, positivity forces `V=b`. The exact parent list contains
\[
\boxed{7361}
\]
cases.

For a fixed prefix through type `k-1`, the strict violation budget gives
\[
R_k\le
\left\lceil
\frac{D_{ts}V-a s-b\sum_{j<k}c_jR_j}{bc_k}
\right\rceil-1.
\tag{5.3}
\]
Applying the exact aggregate-lift lemma through types `0,...,5` produces the complete branch chain
\[
\boxed{7361\to228\to79\to67\to119\to505\to5686.}\tag{5.4}
\]
The corresponding maximum type budgets are
\[
20478,\ 55780,\ 132888,\ 336702,\ 1007453,\ 2824469.
\]

At type 6, the exact lift enumerator scans the mathematically equivalent `n` parameter rather than every raw slack. It produces exactly
\[
\boxed{176125}
\]
aggregate `(R_6,W_6)` pairs under the complete type-6 budgets. Exact row equality then yields a legal terminal witness sum `0<=W_7<=4M` in exactly
\[
\boxed{167}
\]
cases.

For each of these 167 cases the checker sets `R_7` to the least congruent value (4.3) and evaluates the full exact defect
\[
a s+b\sum_{k=0}^7c_kR_k.
\]
Not one case remains below `D_ts V`:
\[
\boxed{\#\{\text{relaxed violations after terminal slack minimization}\}=0.}\tag{5.5}
\]
Since every actual row maps into this relaxed aggregate search, (5.5) proves for every actual C045 row
\[
\boxed{
\frac{a s_i+bT_i}{V_i}\ge D_{ts}.
}\tag{5.6}
\]
Together with (2.1),
\[
\boxed{
B^2V\le\frac{a^2-D_{ts}}{b^2}V.
}\tag{5.7}
\]

The executed checker ends

`FAST_MIXED_MODULUS_LIFT_ENUMERATION=PASS`,
`EXACT_TYPE7_MINIMAL_SLACK_CLOSURE=PASS`,
`GLOBAL_TWO_STEP_DEFECT_7_OVER_2_DMM=PASS`,
`ALL_EXACT_CHECKS_PASS`.

## 6. Spectral strictification

Define
\[
R=\frac ab,
\qquad
\beta_{ts}=R-\frac{D_{ts}}{2ab}.
\tag{6.1}
\]
Then
\[
\beta_{ts}^2
=
\frac{a^2-D_{ts}}{b^2}
+
\frac{D_{ts}^2}{4a^2b^2}
>
\frac{a^2-D_{ts}}{b^2}.
\]
By Collatz monotonicity on the positive witness,
\[
\rho(B)^2\le\frac{a^2-D_{ts}}{b^2},
\]
so
\[
\boxed{\rho(B)<\beta_{ts}.}\tag{6.2}
\]
Because `D_ts=(7/4)D_tail`,
\[
\beta_{ts}<\beta_{tail}.
\]
Rescaling to the actual finite covering operator,
\[
\lambda_{ts}=\frac{t^2}{S}\beta_{ts},
\]
therefore gives
\[
\boxed{\rho(A)<\lambda_{ts}<\lambda_{tail}<1.}\tag{6.3}
\]

## 7. Dependence-preserving finite-to-infinite transfer

The C045 covering operator enumerates accepted collations of **actual ordered binary source-string pairs**. It does not assign independent probabilities to the `n^2` match indicators.

At positive fugacities `(x,y)`, if the finite operator has spectral radius below `z<1`, finite dimensionality gives a constant `K_z<infinity` such that accepted collation weight of order `m` is at most `K_z z^m`. Every actual length-`n` source pair with `L_n>=m` has at least one accepted covering collation, and every actual pair of independent uniform binary strings has probability exactly `4^{-n}`. Positivity therefore gives
\[
\boxed{
\Pr\{L_n\ge m\}\le K_z(4xy)^{-n}z^m.
}\tag{7.1}
\]
No independent Bernoulli matching array is introduced.

Taking `m=floor(cn)`, choosing `c>log(4xy)/log z`, and summing the exponentially decaying upper tail yields
\[
\limsup_{n\to\infty}\frac{\mathbf E L_n}{n}\le c.
\]
Letting `c` decrease to the threshold gives
\[
\boxed{
\gamma_2\le\frac{\log(4xy)}{\log z}.
}\tag{7.2}
\]
At
\[
x=y=t=256717/800000,
\qquad z=\lambda_{ts},
\]
this is `U_ts`. Since `lambda_ts<lambda_tail<1`, monotonicity of `log(4t^2)/log z` on `(0,1)` gives `U_ts<U_tail`.

The endpoint checker encloses each negative logarithm using 240 positive atanh-series terms plus an exact rational geometric remainder and certifies
\[
U_{ts}<
0.8262759427622826250151065815372966328234619961931900238808061833125629444301
<U_{tail}.
\]
It ends `EXACT_LOG_INTERVALS_DISJOINT=PASS`, `SOURCE_INTERVAL_STRICTLY_SHRINKS=PASS`, and `ALL_EXACT_CHECKS_PASS`.

## 8. Soundness notes and failed scouts

The theorem-critical enumeration uses exact integer arithmetic (`boost::multiprecision::cpp_int`, unsigned 128-bit arithmetic only where the proved ranges fit) and exact congruence/range formulas. The endpoint proof uses Python `Fraction`; decimal values are diagnostic only.

The relaxation remains one-sided in the safe direction: it forgets actual C045 successor identities, repeated-successor consistency, and decomposability of aggregate `(R_k,W_k)` into individual labels. Therefore absence of a relaxed violator implies absence of an actual row violator.

Exploratory larger targets `3.6 D_mm`, `3.75 D_mm`, and `4 D_mm` were attempted locally but did not finish within the bounded execution windows used in this run. **No claim is made above `3.5 D_mm`.** This is not counted as source progress.

The remaining obstruction is computational/structural rather than conceptual at the terminal step: at `3.5D_mm` there are already 167 legal exact terminal witness sums, all killed only by the least-residue terminal slack. To move materially farther, the best next mechanism is to derive a two-type (`k=5,6,7`) lattice/CRT closure that solves the final mass and terminal slack jointly without enumerating billions of lift parameters, or to inject actual C045 successor identities into the surviving aggregate prefixes.

## 9. Artifact manifest

Exact finite checker:

`proofnet24/P02-progress-lcs/artifacts/2026-09-20T16-03-00Z__terminal_slack_minimization_checker.cpp`

- creation commit `7769be542d7ce1e641527aecf1a9ef50bc31b360`
- verified blob `c3160f289dfbe15142b7f368ee5d0d02a22740cc`.

Executed output:

`proofnet24/P02-progress-lcs/artifacts/2026-09-20T16-03-00Z__terminal_slack_minimization_checker.out`

- creation commit `9205169bf371bcf2f66257f022d3282387309824`
- verified blob `ecffa14e71b9f048908bbf9040066ef96fdcf38b`.

Exact endpoint checker:

`proofnet24/P02-progress-lcs/artifacts/2026-09-20T16-03-00Z__terminal_slack_endpoint_checker.py`

- creation commit `fc6be7679af647a40ba8a663ceefe48ac903960f`
- verified blob `0b8474f7cc443a5ee32a37bf43f0b13baefe5490`.

Executed endpoint output:

`proofnet24/P02-progress-lcs/artifacts/2026-09-20T16-03-00Z__terminal_slack_endpoint_checker.out`

- creation commit `921364a1a8c26750ee8fb6495be4bdf07d4f396d`
- verified blob `3f596908f4f82b3305865989df361a7676819c30`.

## 10. ledger_delta

- `target`: T02 binary Chvatal--Sankoff constant, original two-source dependent model.
- `public_before`: `[0.792665992, 0.826280]` retained; public status remains OPEN.
- `internal_before`: `[0.792665992, U_tail]` under frozen C045 assumptions.
- `internal_after`: `[0.792665992, U_ts]` with exact `U_ts<U_tail` separator at 76 decimal places.
- `mechanism_before`: universal two-step defect `D_tail=2D_mm`.
- `mechanism_after`: universal two-step defect `D_ts=(7/2)D_mm=(7/4)D_tail`.
- `new_theorem`: exact aggregate-lift reparameterization plus exact terminal least-slack closure proves `B^2V <= ((a^2-D_ts)/b^2)V`.
- `dependence_transfer`: retained actual-string C045 covering transfer; no independent Bernoulli match model.
- `coordination`: complementary to P13 terminal-gradient strip/Bellman route and P05 renewal lower route.
- `failed_scouts`: targets `3.6D_mm`, `3.75D_mm`, `4D_mm` unfinished in bounded local runs; no claims.
- `status`: PARTIAL / source OPEN / exact internal candidate pending independent review and priority checking.
- `next_attack`: solve final two/three coefficient types by CRT/lattice exact mass equations, then use actual successor identities if a relaxed terminal branch survives.
