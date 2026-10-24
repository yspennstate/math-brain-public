Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.** GPT-6 / maximum reasoning was requested, but this runtime exposes no authenticated applied-model / applied-effort receipt, so I do not claim otherwise.

**SOURCE-LEVEL MOVEMENT.** For the genuine Chvátal–Sankoff problem of two independent iid uniform binary strings, retain

\[
L=0.792665992=\frac{99083249}{125000000}.
\]

Let `U_C` be P02's preceding exact successor-slack-semigroup endpoint from
`proofnet24/P02-progress-lcs/runs/2026-09-20/2026-09-20T08-03-23Z__successor-slack-semigroup-report.md`.
This run proves a stronger finite dual rate `lambda_* < lambda_C` and therefore

\[
\boxed{L\le \gamma_2\le U_*<U_C},
\qquad
U_*:=\frac{\log(4t^2)}{\log\lambda_*}.
\]

An exact positive-series logarithm certificate proves the strict separator

\[
\boxed{
U_*<
0.82627594276228262501510658153729663282346199619319002388080618331256294443029953
<U_C.
}
\]

Thus the tracked metric strictly moves from `U_C-L` to `U_*-L`. Diagnostic high precision, not used as proof, gives

\[
U_C-U_*\approx 9.2685079251686472\times10^{-81}.
\]

Status remains **PARTIAL / source OPEN**. The absolute endpoint movement is tiny; the substantive mechanism movement is a 31% increase in the universal two-step defect, from the preceding integer `D_C` to the exact rational `D_*=a/v_*`, and a proof that the tight-row branch stays above that new non-tight optimum.

# P02 / T02 — residue-optimal non-tight slack and a matched tight-row exclusion

## 1. Source, exact model, current status, and continuity

The target is

\[
\gamma_2=\lim_{n\to\infty}\frac{\mathbf E\,LCS(X_1^n,Y_1^n)}n
\]

for two independent iid **uniform binary strings**. The same source symbols recur along rows and columns of the dynamic-programming grid, so the `n^2` match indicators are dependent. The independent Bernoulli matching model is not substituted anywhere in this report.

Controlling policy is `operations/PROGRESS20_2026-09-20.md`, blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`.

Fresh source navigation on 2026-09-20 recovered Alexander Tiskin, `arXiv:2212.01582v2`, last revised 2024-08-13. The current arXiv record still describes the coefficient as unresolved and explicitly says that claims in the earlier preprint concerning the stochastic process and `gamma` turned out to be incorrect and were omitted from v2 while a supported estimate was retained. None of the removed claims is used here.

The rigorous public lower endpoint remains `0.792665992` from Heineman–Miller–Reichman–Salls–Sárközy–Soiffer (`arXiv:2407.10925`). The conventional published upper endpoint remains Lueker's `0.826280`. Li–Ren–Wen, published online by Cambridge on 2026-03-02, still describe determination of the two-string binary constant as open and summarize the public rigorous range at roughly `0.792665 <= gamma <= 0.826280`. The stronger C045/P02 endpoint in this report is a repository-internal exact candidate pending later independent review and public-priority checking; it is not represented as a published result.

Newest own substantive dependency:
`proofnet24/P02-progress-lcs/runs/2026-09-20/2026-09-20T08-03-23Z__successor-slack-semigroup-report.md`, blob `a2c532b3ab018a09fbddee273dcd0a39a63a75d6` in that report's readback.

Newest P13 companion recovered:
`proofnet24/P13-progress-lcs/runs/2026-09-20/2026-09-20T08-17-18Z__strong-pathwise-span-linear-transfer.md`, blob `beccae1f81c74b1404861a99b72eed8ab9b9c1e9`. P13 proves the sharp all-width pathwise strip reward-span bound `m` and the resulting finite-to-stationary error `m/N`; it does not change a source endpoint and is on the true-source boundary-recursion side.

Newest current-history LCS report recovered outside the LIVE20 pair:
`runs/prob10_2026-09-20/PROB10-02/20260920T0837Z_r17_sharp_centered_path_span_a4d2.md`, blob `5ed147f73654da435da33832ec33c2a8633e19ec`. R17 independently reaches the same sharp centered-path span theorem and likewise reports no source endpoint movement. P02 therefore stays nonduplicating on the finite covering/cone variational route.

The essential finite core remains R17 C045,
`runs/R17/20260918_0926Z_fullcap6_c045_f7a1.md`, with exact all-row cone output
`artifacts/R17/20260918_0926Z_fullcap6_c045_f7a1_exact_cone_checker.out`, blob `0a00ececfdfe58ec85f5a7e6c29bf2559fd58539`. C033–C035 remain withdrawn after the complement-gauge bug; C036 repaired the cocycle transport; C045 is the retained gauge-correct 11,614,187-state finite core.

Short handoff of P02's actual former target: Aldous–Fill Open Problem 2.34 remains closure-packaged at frozen `11/11`; publication novelty there remained explicitly unverified. It is not reopened. Root `POSTED.md` was checked; no posting exclusion covers T02.

## 2. Frozen C045 primitive operator and the preceding defect

Put

\[
t=\frac pq=\frac{256717}{800000},\qquad d=q-p=543283,
\]

and write the C045 operator as

\[
A=t^2H,\qquad B=SH,\qquad S=q^6d.
\]

The eight primitive coefficient types are

\[
c_k=q^{6-k}dp^k\quad(0\le k\le6),\qquad c_7=p^7,
\]

with multiplicities `(2,4,4,4,4,4,4,4)`. The inherited positive integer witness satisfies

\[
1\le V_i\le M=5\cdot10^{18},
\qquad
BV\le \frac abV,
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

Define integer one-step slacks

\[
s_i=aV_i-b(BV)_i\ge0.
\tag{2.1}
\]

The preceding P02 run proved, for tight rows `s_i=0`, the weighted successor-slack congruence

\[
T_i:=\sum_jB_{ij}s_j\equiv a^2\pmod b
\tag{2.2}
\]

and combined it with the inherited four-band theorem to exclude every relaxed tight-row slack tuple through

\[
D_C=309014390464322771612037585007899665700601.
\tag{2.3}
\]

That gave

\[
B^2V\le\frac{a^2-D_C}{b^2}V.
\]

Its explicit residual obstruction was the non-tight-row branch: it still used only `s_i>=1` and `V_i<=M`. This run attacks exactly that obstruction.

## 3. New residue-optimal lower bound for every non-tight row

Let

\[
\alpha:=a\bmod b=1884560463669269501.
\]

Exact arithmetic gives the inverse

\[
\boxed{h=707440146652911839},
\qquad
\alpha h\equiv1\pmod b.
\tag{3.1}
\]

Set

\[
\boxed{v_*:=h+b=4927892157284473118}.
\tag{3.2}
\]

The witness range satisfies

\[
v_*\le M<2b.
\tag{3.3}
\]

Now take any non-tight row, so `s_i>0`. From (2.1),

\[
s_i\equiv aV_i\equiv\alpha V_i\pmod b,
\]

hence

\[
V_i\equiv h s_i\pmod b.
\tag{3.4}
\]

Let `r_i` be the least nonnegative residue of `h s_i` modulo `b`. Since `1<=V_i<2b`, either `V_i=r_i` or `V_i=r_i+b` (with the evident `V_i=b` possibility when `r_i=0`). Since `r_i<=h s_i`, in every case

\[
V_i\le r_i+b\le h s_i+b\le s_i(h+b)=s_i v_*.
\]

Therefore every non-tight row obeys the exact ratio bound

\[
\boxed{\frac{s_i}{V_i}\ge\frac1{v_*}.}
\tag{3.5}
\]

This is sharp for the **range-plus-congruence relaxation** itself: `s=1`, `V=v_*=h+b` satisfies the residue relation and lies inside the permitted witness interval. Thus any further improvement beyond (3.5) must use actual C045 row structure, not only `1<=V_i<=M` and the one-step congruence.

Define the exact rational defect

\[
\boxed{D_*:=\frac a{v_*}}
\tag{3.6}
\]

so that

\[
D_*=\frac{1995237757733917147310102692686664915858011319606812684127301}
{4927892157284473118}.
\]

It is nonintegral because

\[
a\bmod v_*=2634769678087876597.
\tag{3.7}
\]

Exact comparison gives

\[
\boxed{D_*>D_C},
\qquad
\frac{D_*}{D_C}=1.3102517702965761\ldots .
\tag{3.8}
\]

For every non-tight row, the first term in the two-step defect already gives

\[
a s_i\ge D_*V_i.
\tag{3.9}
\]

Thus non-tight rows can support the stronger theorem if and only if the tight-row branch can be pushed above `D_*` as well.

## 4. Tight-row semigroup exclusion all the way to the new non-tight optimum

If `s_i=0`, coprimality in (2.1) gives `b|V_i`; since `1<=V_i<=M<2b`,

\[
V_i=b,
\qquad
(BV)_i=a.
\tag{4.1}
\]

The previous four-band theorem says every such tight row has non-tight accepted support in all four bands

\[
\{0\},\qquad\{1,2,3\},\qquad\{4,5,6\},\qquad\{7\}.
\tag{4.2}
\]

Grouping positive successor slacks by coefficient type therefore puts

\[
T_i=\sum_{k=0}^7c_kS_k
\tag{4.3}
\]

inside the relaxed semigroup

\[
S_0\ge1,
\qquad S_7\ge1,
\qquad S_1+S_2+S_3\ge1,
\qquad S_4+S_5+S_6\ge1,
\tag{4.4}
\]

with, from (2.2),

\[
T_i\equiv a^2\pmod b,
\qquad
a^2\bmod b=3275530027931543170.
\tag{4.5}
\]

The new target threshold is

\[
\boxed{
D_{\rm floor}:=\left\lfloor\frac a{v_*}\right\rfloor
=404886652152996330056570759820082466026328.
}
\tag{4.6}
\]

I replaced the preceding billion-scale naive recursion by an exact meet-in-the-middle enumeration that loses no tuples. It precomputes every `(S_6,S_7)` pair that can occur under the largest possible residual budget, keyed by its exact residue modulo `b`; a separate table enforces `S_6>=1` when `S_4=S_5=0`. It then exhausts all prefixes `(S_0,...,S_5)` satisfying the first three band conditions and performs one exact residue lookup.

Coverage details from the executed exact checker are:

- `2,908,113` feasible `(S_6,S_7)` pairs in the global residual budget;
- `2,908,113` distinct residues in the unrestricted pair table;
- `2,904,606` distinct residues in the `S_6>0` table;
- `8,237,900` exact prefix states and residue lookups;
- **zero** relaxed tuples satisfying (4.4)–(4.5) with `T<=D_floor`.

Therefore every genuine tight row satisfies

\[
T_i>D_{\rm floor}.
\tag{4.7}
\]

Because `D_*` is nonintegral, (4.7) strengthens to

\[
\boxed{T_i>D_*.}
\tag{4.8}
\]

This is the key matching step: the tight branch is now proved to lie strictly above the exact optimum forced by the non-tight residue argument.

## 5. Stronger universal two-step dual theorem

The exact identity valid for every row is

\[
\boxed{
a^2V_i-b^2(B^2V)_i
=a s_i+b\sum_jB_{ij}s_j.
}
\tag{5.1}
\]

If `s_i>0`, (3.9) gives

\[
a^2V_i-b^2(B^2V)_i\ge a s_i\ge D_*V_i.
\]

If `s_i=0`, then `V_i=b`, and (4.8) gives

\[
a^2V_i-b^2(B^2V)_i
=bT_i>D_*b=D_*V_i.
\]

Hence every row satisfies

\[
\boxed{
B^2V\le\frac{a^2-D_*}{b^2}V.
}
\tag{5.2}
\]

Consequently

\[
\rho(B)\le\sqrt{\frac{a^2-D_*}{b^2}}.
\tag{5.3}
\]

Because `D_*=a/v_*`, the convenient exact rational strict majorant simplifies to

\[
\boxed{
\beta_*:=\frac ab-\frac{1}{2bv_*}.
}
\tag{5.4}
\]

Indeed,

\[
\beta_*^2
=\frac{a^2-D_*}{b^2}+\frac1{4b^2v_*^2}
>\frac{a^2-D_*}{b^2}.
\]

Thus

\[
\rho(B)<\beta_*.
\tag{5.5}
\]

Rescaling to the original C045 operator gives

\[
\boxed{
\lambda_*:=\frac{t^2}{S}\beta_*,
\qquad
\rho(A)<\lambda_*<\lambda_C<1.
}
\tag{5.6}
\]

The strict comparison with the preceding rate follows directly from `D_*>D_C`.

## 6. Dependence-preserving finite-to-infinite transfer

The previously proved C045 covering transfer is restated under the exact assumptions used here.

The finite covering operator enumerates accepted collations of **actual ordered binary source-string pairs**. At positive fugacities `(x,y)`, if its spectral radius is below `z<1`, finite dimensionality gives a constant `K<infinity` such that the accepted collation weight of order `m` is at most `Kz^m`.

Every actual pair `(X_1^n,Y_1^n)` with `L_n>=m` has at least one accepted covering collation. Every actual ordered length-`n` binary pair has probability exactly `4^{-n}`. By coefficient positivity,

\[
\Pr\{L_n\ge m\}\le K(4xy)^{-n}z^m.
\tag{6.1}
\]

No independent probabilities are assigned to match cells; all dependence remains in the underlying source strings.

For every

\[
c>\frac{\log(4xy)}{\log z},
\]

taking `m=floor(cn)` makes (6.1) exponentially small. Summing the upper tail of `L_n`, dividing by `n`, and letting `n->infinity` gives

\[
\boxed{
\gamma_2\le\frac{\log(4xy)}{\log z}.
}
\tag{6.2}
\]

Taking `x=y=t` and `z=lambda_*` gives

\[
\boxed{
U_*:=\frac{\log(4t^2)}{\log\lambda_*}.
}
\tag{6.3}
\]

Since `log(4t^2)<0`, the map `z -> log(4t^2)/log z` is strictly increasing on `(0,1)`. Therefore (5.6) gives

\[
\boxed{U_*<U_C.}
\tag{6.4}
\]

This is the original-problem source-level movement. No finite expected-LCS number is promoted without a transfer.

## 7. Exact endpoint separator

The endpoint checker uses only rational arithmetic and the positive expansion

\[
-\log z
=2\sum_{k\ge0}\frac{u^{2k+1}}{2k+1},
\qquad
u=\frac{1-z}{1+z},
\]

with the tail bounded by

\[
0<2\sum_{k\ge K}\frac{u^{2k+1}}{2k+1}
\le
\frac{2u^{2K+1}}{(2K+1)(1-u^2)}.
\]

Using `K=260` for `4t^2`, `lambda_*`, and `lambda_C`, it proves

\[
U_*<Q<U_C,
\]

where

\[
\boxed{
Q=
\frac{82627594276228262501510658153729663282346199619319002388080618331256294443029953}
{10^{80}}.
}
\tag{7.1}
\]

Therefore the strongest **repository-internal exact candidate interval currently supported by P02's finite core and transfer** is

\[
\boxed{
0.792665992\le\gamma_2\le U_*<Q.
}
\tag{7.2}
\]

This is stronger than the public literature interval but remains pending independent review and priority checking.

## 8. What genuinely changed, and what did not

Original-problem metric:

\[
\boxed{
W_{\rm before}=U_C-L,
\qquad
W_{\rm after}=U_*-L<W_{\rm before}.
}
\]

Mechanism-level change:

\[
D_C=309014390464322771612037585007899665700601
\]

is replaced by the exact rational

\[
D_*=a/v_*=4.0488665215299633\ldots\times10^{41},
\]

a factor `1.3102517702965761...` stronger. Unlike the preceding finite scan, this run identifies the non-tight residue obstruction exactly and then proves the tight-row semigroup stays above it.

What did **not** change: the source is not solved; `L` is unchanged; no independent audit is claimed; the internal C045 upper certificate is not represented as public literature; no Bernoulli matching model is used; no historical or peer file is edited.

## 9. Residual obstruction and next attack

The abstract non-tight residue/range bound is now exhausted. The relaxation admits

\[
s=1,\qquad V=v_*=4927892157284473118,
\]

so `s/V=1/v_*` cannot be improved from congruence and `1<=V<=M` alone. The next useful P02 attack must use **actual C045 row geometry** to show that no reachable row with witness coordinate `v_*` can have one-step slack `1`, or more generally to prove a larger minimum of `s_i/V_i` on the actual non-tight rows. The most direct route is a graph-specific row-classification or local successor identity around the near-maximal Collatz rows; another scalar modular table without row structure is no longer sufficient.

This is complementary to P13/R17's strip/reward geometry and does not duplicate their finite-to-stationary lower-side work.

## 10. Exact artifacts and readback data

Executed exact finite core:

- `proofnet24/P02-progress-lcs/artifacts/2026-09-20T09-05-20Z__residue_floor_semigroup_checker.cpp`
  - creation commit `e6dac82abe8ef6f3c4762d8fc472467a23b527aa`
  - verified blob `a18016c2411a345ecf553ee9ebdee78aba92da38`;
- `proofnet24/P02-progress-lcs/artifacts/2026-09-20T09-05-20Z__residue_floor_semigroup_checker.out`
  - creation commit `80ae234aa51c09bcaff1d8c13ebb8f93e23c5be3`
  - verified blob `c3872437526d0f57d8a95599ba978f530b3ed41f`
  - ends `NO_TIGHT_ROW_RELAXED_SEMIGROUP_POINT_AT_OR_BELOW_FLOOR_D_STAR=PASS` and `ALL_EXACT_CHECKS_PASS`.

Exact endpoint compiler:

- `proofnet24/P02-progress-lcs/artifacts/2026-09-20T09-05-20Z__residue_defect_endpoint_checker.py`
  - creation commit `bd0f31a9d502aca499029040d37fc50d39b77777`
  - verified blob `88dd62ace38ac3958dad9bb748394790326f1c14`;
- `proofnet24/P02-progress-lcs/artifacts/2026-09-20T09-05-20Z__residue_defect_endpoint_checker.out`
  - creation commit `c49f93d45a30528327fdadea9fa58f6cf92a2ea2`
  - verified blob `d3862efacfc57e230ebbdcaaeb71b51c822db00a`
  - ends `D_STAR_STRICTLY_BEATS_D_C=PASS`, `EXACT_LOG_SEPARATOR_PASS`, `SOURCE_INTERVAL_STRICTLY_SHRINKS_PASS`, and `ALL_EXACT_CHECKS_PASS`.

No persistence failure occurred in this run.

```yaml
ledger_delta:
  track: P02
  parent: T02
  source: "Chvatal-Sankoff binary LCS constant for two independent iid uniform binary strings"
  status: PARTIAL
  source_status: OPEN
  metric: "certified interval width U-L with exact assumptions"
  lower: "0.792665992"
  upper_before: "U_C = log(4t^2)/log(lambda_C)"
  upper_after: "U_* = log(4t^2)/log(lambda_*), with U_* < 0.82627594276228262501510658153729663282346199619319002388080618331256294443029953 < U_C"
  movement: "strict"
  mechanism_before: "two-step defect D_C=309014390464322771612037585007899665700601"
  mechanism_after: "exact rational two-step defect D_*=a/(h+b), h=(a mod b)^(-1) mod b, D_*/D_C>1.31025"
  dependence_preserved: true
  bernoulli_matching_used: false
  finite_to_infinite_transfer: "actual-string-pair covering bound; unchanged and restated"
  independent_review: PENDING
  public_priority: UNVERIFIED
  next_obstruction: "actual C045 non-tight rows; congruence/range relaxation is sharp at s=1,V=h+b"
```
