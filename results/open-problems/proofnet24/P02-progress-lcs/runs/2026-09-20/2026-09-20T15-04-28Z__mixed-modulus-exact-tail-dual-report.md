Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.** GPT-6 / maximum reasoning was requested, but no authenticated applied-effort selector or receipt is exposed, so I do not claim otherwise.

# P02 / T02 — mixed-modulus exact-tail dual strictification

## 0. Source-level before / after

Target:
\[
\gamma_2=\lim_{n\to\infty}\frac{\mathbf E\,LCS(X_1^n,Y_1^n)}n
\]
for two independent iid uniform binary strings. The dependence among the `n^2` match indicators induced by the two source strings is retained throughout. The independent Bernoulli matching model is not substituted.

Retain the rigorous public lower endpoint
\[
L=0.792665992=\frac{99083249}{125000000}.
\]
The latest durable P02 certificate entering this run was

`proofnet24/P02-progress-lcs/runs/2026-09-20/2026-09-20T14-15-00Z__mixed-modulus-padic-dual-report.md`,

blob `9348acb6ac74acbc51f4e0aaf528c2fed8838624`. It proved, relative to the frozen gauge-correct C045 operator/witness and the already-proved actual-string covering transfer,
\[
L\le\gamma_2\le U_{mm},
\qquad
U_{mm}=\frac{\log(4t^2)}{\log\lambda_{mm}}.
\]

This run proves a stronger exact finite dual rate `lambda_tail < lambda_mm` and therefore
\[
\boxed{L\le\gamma_2\le U_{tail}<U_{mm}},
\qquad
U_{tail}=\frac{\log(4t^2)}{\log\lambda_{tail}}.
\]
An exact rational positive-series logarithm enclosure proves
\[
\boxed{
U_{tail}<
0.8262759427622826250151065815372966328234619961931900238808061833125629444302
<U_{mm}.
}
\]
Thus the repository-internal certified width under the stated frozen assumptions moves strictly from `U_mm-L` to `U_tail-L`.

Diagnostic high precision, not used as proof, gives
\[
U_{mm}-U_{tail}\approx 6.8468259712281457892\times10^{-77},
\]
and
\[
U_{tail}-L\approx
0.03360995076228262501510658153729663282346199619319002388080618331256294443016.
\]
The source-level decimal movement is minute; the finite dual mechanism-level improvement is clean and exact: the universal two-step defect is doubled.

Status: **PARTIAL / source OPEN / exact repository-internal candidate pending later independent review and public-priority checking.**

## 1. Source status, prior attempts, exclusions, coordination, and handoff

Controlling policy is `operations/PROGRESS20_2026-09-20.md`, blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`. Root `POSTED.md` was checked; no posting exclusion covers T02.

Fresh source navigation on 20 September 2026 rechecked Alexander Tiskin, `arXiv:2212.01582v2`. The arXiv abstract still states that the binary coefficient is unresolved. The submission history gives v2 on 2024-08-13, and the arXiv comments explicitly say that claims in the preprint concerning the process and `gamma` turned out to be incorrect and that the erroneous parts were omitted while a supported partial estimate was retained. None of the withdrawn claims is used here.

Heineman--Miller--Reichman--Salls--Sarkozy--Soiffer, `arXiv:2407.10925`, prove the rigorous binary two-string lower endpoint `0.792665992`; their abstract records the conventional rigorous upper endpoint `0.826280`. Li--Ren--Wen, *Bulletin of the Australian Mathematical Society* 114 (2026), published online 2026-03-02, still describe exact determination of the two-string binary constant as open and summarize the public interval as approximately `0.792665 <= gamma <= 0.826280`.

Prior attempts relevant to this lane remain: Chvatal--Sankoff's existence and first bounds; Deken; Dancik--Paterson finite-state/covering bounds; Lueker's 2009 rigorous interval; simulation/estimate work including Boutet de Monvel, Bundschuh, and Bukh--Cox; the 2024 computational lower-bound improvement to `0.792665992`; and Tiskin's corrected stochastic-process estimate. P02 stays on the finite-state covering/cone stationary upper-dual route, but the new step below is an arithmetic exact-row closure on the frozen C045 witness rather than another finite-LCS expectation computation.

Newest companion P13 report recovered:

`proofnet24/P13-progress-lcs/runs/2026-09-20/2026-09-20T14-13-00Z__residual-transport-width6-exact-transfer.md`, blob `9975402d777916fa5eccc31218f546baf281644c`.

P13 works the genuine-source strip/Bellman/boundary-recursion lane. Its new theorem transports Bellman residuals by `P^k`, proves an every-horizon finite-to-infinite transfer, and shrinks its width-six mechanism interval by a large factor, but it does not claim the present covering/cone arithmetic.

Newest same-source R17 report recovered:

`runs/prob10_2026-09-20/PROB10-02/20260920T1458Z_r17_equivariant_lookahead_atom_5d8e.md`, blob `2a97a4ebd2ec6efdde34155b38bbafb14a8fd300`.

R17 uses an equivariant finite-lookahead common-subsequence policy plus a policy-independent synchronizing atom to obtain a rigorous lower mechanism bound `0.78128135`; it explicitly reports no source endpoint movement because this is below `0.792665992`. It is nonduplicating with P02.

Brief handoff of P02's actual earlier target: Aldous--Fill Open Problem 2.34 remains closure-packaged at frozen `11/11`; it is not reopened.

No historical or peer file was overwritten. No email, Drive, public posting, paid compute, access, workflow, or schedule change was performed.

## 2. Frozen C045 data and the preceding mixed-modulus defect

Put
\[
t=\frac pq=\frac{256717}{800000},\qquad d=q-p=543283,
\]
\[
S=q^6d,\qquad A=t^2H,\qquad B=SH.
\]
The primitive C045 label coefficients are
\[
c_k=q^{6-k}dp^k\quad(0\le k\le6),
\qquad c_7=p^7,
\]
with multiplicities
\[
(m_0,m_1,\ldots,m_7)=(2,4,4,4,4,4,4,4).
\]
Since `gcd(p,q)=gcd(p,d)=1`, `v_p(c_k)=k` exactly for `0<=k<=7`.

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
\qquad \gcd(a,b)=1,
\qquad b\le M<2b.
\]
Define row slack
\[
\boxed{s_i=aV_i-b(BV)_i\ge0.}
\tag{2.1}
\]
Let
\[
\alpha=a\bmod b=1884560463669269501,
\qquad
h=707440146652911839,
\]
so `alpha*h == 1 (mod b)`. Hence every state obeys
\[
\boxed{V_i\equiv h s_i\pmod b.}
\tag{2.2}
\]
For every row set
\[
T_i=(Bs)_i.
\]
Then
\[
\boxed{a^2V_i-b^2(B^2V)_i=a s_i+bT_i.}
\tag{2.3}
\]

The preceding report proved the exact normalized defect
\[
D_{mm}=
\frac{655209040831815247751186134103526570372190622578374697627001555}
{925139970226099634}
\tag{2.4}
\]
and therefore
\[
B^2V\le\frac{a^2-D_{mm}}{b^2}V.
\tag{2.5}
\]
Its mixed-modulus aggregate lemma is retained: for coefficient type `k`, let `R_k` be the sum of successor slacks and `W_k` the sum of successor witness values over accepted labels of that type, rejected labels contributing zero. Then
\[
\boxed{W_k\equiv hR_k\pmod b},
\qquad 0\le W_k\le m_kM.
\tag{2.6}
\]
The p-adic row equation
\[
\boxed{u:=\frac{aV-s}{b}=\sum_{k=0}^7c_kW_k}
\tag{2.7}
\]
forces one residue `W_k mod p` at each type after the preceding types have been fixed. Because `m_kM<8b<pb`, the pair of congruences `W_k == hR_k (mod b)` and `W_k == z_k (mod p)` has at most one `W_k` in the permitted aggregate witness range for each `R_k`.

This is a safe relaxation: actual successor decompositions map into it, but the relaxation does not require actual successor identities, multiplicity decomposability, or repeated-successor consistency.

## 3. New idea: stop one p-adic digit early and use exact row equality

The preceding proof chose a target small enough that the relaxed tree died already at type 2. A natural continuation is to increase the target and filter deeper. A naive continuation through type 7, however, wastes information: after types `0,...,6` have been fixed, the exact row equation (2.7) determines the type-7 aggregate witness sum itself.

Specifically, any surviving prefix has fixed values `W_0,...,W_6`. Therefore an actual row must satisfy
\[
\boxed{
W_7^*=\frac{u-\sum_{k=0}^6c_kW_k}{c_7}.
}
\tag{3.1}
\]
Since `c_7=p^7`, the seven preceding p-adic digit conditions guarantee integrality for a surviving prefix, but an actual type-7 aggregate must also obey the hard range
\[
\boxed{0\le W_7^*\le4M.}
\tag{3.2}
\]
Thus exact equality at the final coefficient type is strictly stronger than testing only the next residue modulo `p`.

This is the new mechanism of the run: **mixed-modulus prefix filtering plus exact terminal row equality**.

## 4. New target defect

Define
\[
\boxed{D_{tail}:=2D_{mm}.}
\tag{4.1}
\]
In reduced form,
\[
\boxed{
D_{tail}=
\frac{655209040831815247751186134103526570372190622578374697627001555}
{462569985113049817}.
}
\tag{4.2}
\]
This is an exact factor-two mechanism improvement over the preceding durable defect.

Suppose for contradiction that an actual C045 row violates
\[
\frac{a s_i+bT_i}{V_i}\ge D_{tail}.
\tag{4.3}
\]
We show that no such row exists.

### 4.1 Parent reduction

For a row of slack `s`,
\[
\frac{as}{V}\ge\frac{as}{M}.
\]
The exact cutoff is
\[
C=\left\lceil\frac{D_{tail}M}{a}\right\rceil=3550,
\tag{4.4}
\]
with
\[
\frac{3550a}{M}\ge D_{tail},
\qquad
\frac{3549a}{M}<D_{tail}.
\]
Hence only `0<=s<3550` can violate (4.3).

By (2.2) and `M<2b`, a fixed positive slack has at most two witness values in `[1,M]`: the least positive residue `(hs mod b)` and, if still at most `M`, that residue plus `b`; for `s=0`, positivity and `M<2b` force `V=b`. The exact scan therefore contains exactly
\[
\boxed{4207}
\]
parent pairs `(s,V)`.

### 4.2 Exact mixed-modulus prefix filtration

For a target `D`, after fixing earlier aggregate slacks `R_0,...,R_{k-1}`, violation of (4.3) gives the exact integer budget
\[
R_k\le
\left\lceil
\frac{DV-a s-b\sum_{j<k}c_jR_j}{bc_k}
\right\rceil-1.
\tag{4.5}
\]
For each integer `R_k` in this budget, the inherited mixed-modulus lemma computes the unique possible aggregate witness `W_k`, if one exists, and the p-adic digit condition determines its residue modulo `p`.

At `D=D_tail`, the exact executed filtration gives the following complete branch counts:
\[
\boxed{
4207\to75\to18\to4\to2\to7\to61\to1163
}
\tag{4.6}
\]
where the successive numbers after 4207 are the surviving aggregate prefixes after types `0,1,...,6`.

The corresponding maximum aggregate-slack budgets are
\[
11683,\ 29870,\ 58533,\ 134553,\ 377503,\ 861374,\ 2517577.
\tag{4.7}
\]
All arithmetic in this filtration is integer or `Fraction` arithmetic.

### 4.3 Exact type-7 closure kills all 1163 prefixes

For each of the 1163 type-6 prefixes, compute the forced terminal value (3.1). The checker verifies that all 1163 are integers, as expected from the p-adic construction, but
\[
\boxed{
\#\{\text{prefixes with }0\le W_7^*\le4M\}=0.
}
\tag{4.8}
\]
Therefore not a single surviving relaxed prefix can satisfy the exact row equality with a legal type-7 aggregate witness sum.

Every actual C045 row violating (4.3) would map to one of these relaxed prefixes and then would necessarily provide a legal `W_7^*`. Equation (4.8) rules this out. Hence
\[
\boxed{
\frac{a s_i+bT_i}{V_i}\ge D_{tail}
\quad\text{for every C045 row }i.
}
\tag{4.9}
\]
Combining (4.9) with (2.3) proves the new finite dual theorem
\[
\boxed{
B^2V\le\frac{a^2-D_{tail}}{b^2}V.
}
\tag{4.10}
\]

This is the substantive advance of the run. It uses exact final-row equality to double the preceding mixed-modulus defect, not merely a tighter decimal evaluation of the old rate.

## 5. Spectral improvement

By Collatz monotonicity on positive `V`,
\[
\rho(B)^2\le\frac{a^2-D_{tail}}{b^2}.
\tag{5.1}
\]
Define the rational strict majorant
\[
\boxed{
\beta_{tail}:=\frac ab-\frac{D_{tail}}{2ab}.
}
\tag{5.2}
\]
Then
\[
\beta_{tail}^2
=\frac{a^2-D_{tail}}{b^2}
+\frac{D_{tail}^2}{4a^2b^2}
>\frac{a^2-D_{tail}}{b^2},
\]
so
\[
\rho(B)<\beta_{tail}.
\tag{5.3}
\]
Because `D_tail=2D_mm>D_mm`,
\[
\beta_{tail}<\beta_{mm}.
\]
Rescale from `B=SH` and `A=t^2H` by setting
\[
\boxed{
\lambda_{tail}=\frac{t^2}{S}\beta_{tail}.
}
\tag{5.4}
\]
Then
\[
\boxed{
\rho(A)<\lambda_{tail}<\lambda_{mm}<1.
}
\tag{5.5}
\]

## 6. Dependence-preserving finite-to-infinite transfer

This is the original two-source-string LCS problem, not an independent Bernoulli matching array.

The retained C045 covering machine enumerates accepted collations of actual ordered binary source-string pairs. At fugacities `(x,y)`, if the finite operator `A(x,y)` has spectral radius below `z<1`, finite dimensionality gives a constant `K_z<infinity` such that accepted weight at collation length `m` is at most `K_z z^m`. Coefficient positivity and the covering property then give, for actual iid uniform binary strings of common length `n`,
\[
\boxed{
\Pr\{L_n\ge m\}\le K_z(4xy)^{-n}z^m.
}
\tag{6.1}
\]
Here `4^{-n}` is the probability of an actual ordered source pair. No independent probabilities are assigned to the `n^2` match indicators.

For
\[
c>\frac{\log(4xy)}{\log z},
\]
both logarithms are negative in the retained parameter regime and (6.1) gives an exponentially decaying tail at `m=floor(cn)`. Summing the LCS tail, using `0<=L_n<=n`, and passing to the limit gives
\[
\boxed{
\gamma_2\le\frac{\log(4xy)}{\log z}.
}
\tag{6.2}
\]
Take
\[
x=y=t=\frac{256717}{800000},
\qquad z=\lambda_{tail}.
\]
Equations (5.5) and (6.2) give
\[
\boxed{
\gamma_2\le U_{tail}:=\frac{\log(4t^2)}{\log\lambda_{tail}}
<U_{mm}.
}
\tag{6.3}
\]
Thus the new finite theorem strictly shrinks the interval for the original dependent binary-string problem.

## 7. Exact endpoint separation

The endpoint checker encloses negative logarithms using
\[
-\log z=2\sum_{j\ge0}\frac{u^{2j+1}}{2j+1},
\qquad
u=\frac{1-z}{1+z},
\]
with 220 exact rational terms and the positive geometric tail bound
\[
0<\mathrm{tail}\le
\frac{2u^{2K+1}}{(2K+1)(1-u^2)}.
\]
It independently encloses `-log(4t^2)`, `-log(lambda_tail)`, and `-log(lambda_mm)`. Exact rational interval division proves the endpoint intervals are disjoint and produces the separator
\[
\boxed{
U_{tail}<
0.8262759427622826250151065815372966328234619961931900238808061833125629444302
<U_{mm}.
}
\tag{7.1}
\]
The retained lower endpoint `L` is also exactly below the lower enclosure for `U_tail`.

Diagnostic decimals only:
\[
U_{tail}=0.8262759427622826250151065815372966328234619961931900238808061833125629444301626279787891\ldots,
\]
\[
U_{mm}=0.8262759427622826250151065815372966328234619961931900238808061833125629444302310962385014\ldots .
\]

## 8. Essential soundness checks and artifacts

The theorem-critical scan uses Python integers and `fractions.Fraction`; no floating arithmetic enters branch exclusion, defect comparison, or exact-tail closure.

Core checker:

`proofnet24/P02-progress-lcs/artifacts/2026-09-20T15-04-28Z__exact_tail_mixed_modulus_dual_checker.py`

- creation commit `28475c41a2dc208128643fd4984c30ee3d5080a6`
- verified blob `ef637d9879ac1b8ae18d4e8fb09bd58093bda554`

Core executed output:

`proofnet24/P02-progress-lcs/artifacts/2026-09-20T15-04-28Z__exact_tail_mixed_modulus_dual_checker.out`

- creation commit `271f66e263e8f6180047b37f364b7a49176ab937`
- verified blob `2514dfbf6798d87aaeef96e15464e0340d3862de`
- records the complete stage counts `4207 -> 75 -> 18 -> 4 -> 2 -> 7 -> 61 -> 1163`, then `exact_tail_integer_candidates=1163`, `exact_tail_in_range_candidates=0`, and ends `EXACT_TYPE7_ROW_EQUALITY_CLOSURE=PASS`, `GLOBAL_TWO_STEP_DEFECT_D_TAIL=PASS`, `ALL_EXACT_CHECKS_PASS`.

Endpoint checker:

`proofnet24/P02-progress-lcs/artifacts/2026-09-20T15-04-28Z__exact_tail_endpoint_checker.py`

- creation commit `94a40ec6ca032bc2542552092dab3009d989914e`
- verified blob `3f1946da158e4888c091d5f9c490677ac342f463`

Endpoint executed output:

`proofnet24/P02-progress-lcs/artifacts/2026-09-20T15-04-28Z__exact_tail_endpoint_checker.out`

- creation commit `d2422711a0149044ea32d2b9cd0f84eb6e90ff14`
- verified blob `258c43ec72e28a35efce622047c91f5b3d95c1f5`
- ends `EXACT_LOG_INTERVALS_DISJOINT=PASS`, `SOURCE_INTERVAL_STRICTLY_SHRINKS=PASS`, `LOWER_ENDPOINT_RETAINED=PASS`, `ALL_EXACT_CHECKS_PASS`.

Full candidate status remains pending later independent review. This run does not independently reconstruct the entire 11,614,187-state C045 covering machine; it uses the retained exact gauge-correct operator/witness and the already-proved actual-string covering transfer as explicit dependencies. The new exact-tail theorem is self-contained relative to those frozen data.

## 9. Failed / bounded exploratory route and residual obstruction

Before finding the exact-tail closure, a direct continuation of the relaxed mixed-modulus scan was tested at larger multiples of `D_mm`. At `1.5 D_mm`, relaxed branches survive all eight p-adic residue filters; at `2 D_mm`, the raw type-7 scan becomes unnecessarily large. This is not a counterexample because those residue-only branches need not satisfy the exact row equation. Replacing the last residue filter by exact equality is the decisive change and proves `2D_mm`.

An exploratory attempt to push the same raw recurrence toward `2.5D_mm` became computationally expensive around the type-6 layer and was abandoned without a claim. No result from that incomplete scout is used in the proof.

The next useful P02 attack should exploit the same exact-tail idea earlier: after a prefix of types, bound the remaining exact row mass and solve the two-type or three-type tail by lattice/CRT arithmetic rather than scanning every aggregate slack. Alternatively, recover actual C045 successor identities for the small surviving prefixes. Either could raise `D_tail` materially without a large raw scan.

## 10. ledger_delta

```text
ledger_delta:
  target: T02_binary_Chvatal_Sankoff
  owner_lane: P02_stationary_variational_covering_dual
  prior_target_handoff: Aldous_Fill_OP2.34_frozen_11_of_11_unchanged
  public_lower: 0.792665992
  public_conventional_upper: 0.826280
  source_before: L <= gamma_2 <= U_mm
  source_after:  L <= gamma_2 <= U_tail < U_mm
  source_metric: certified_U_minus_L_strictly_shrunk_under_frozen_C045_assumptions
  exact_separator: U_tail < 0.8262759427622826250151065815372966328234619961931900238808061833125629444302 < U_mm
  prior_defect: D_mm = 655209040831815247751186134103526570372190622578374697627001555/925139970226099634
  new_defect: D_tail = 655209040831815247751186134103526570372190622578374697627001555/462569985113049817
  mechanism_gain: D_tail = 2*D_mm
  new_claim: P02-T02-MIXED-MODULUS-EXACT-TAIL-DUAL-01
  assumptions: frozen_gauge_correct_C045_operator_and_positive_integer_witness; actual_string_pair_covering_transfer
  dependence_model: actual_two_binary_source_strings; NOT_independent_Bernoulli_matching
  exact_core: 4207_parents -> 75 -> 18 -> 4 -> 2 -> 7 -> 61 -> 1163_type6_prefixes -> 0_legal_exact_type7_aggregates
  p13_nonduplication: genuine_source_strip_Bellman_residual_transport_boundary_recursion
  r17_nonduplication: equivariant_finite_lookahead_policy_plus_synchronizing_atom
  status: PARTIAL_INTERNAL_EXACT_CANDIDATE_PENDING_INDEPENDENT_REVIEW_AND_PRIORITY_CHECK
  artifacts:
    - 2026-09-20T15-04-28Z__exact_tail_mixed_modulus_dual_checker.py
    - 2026-09-20T15-04-28Z__exact_tail_mixed_modulus_dual_checker.out
    - 2026-09-20T15-04-28Z__exact_tail_endpoint_checker.py
    - 2026-09-20T15-04-28Z__exact_tail_endpoint_checker.out
```
