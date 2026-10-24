Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.** GPT-6 / maximum reasoning was requested, but this runtime exposes no authenticated model-selector or applied-effort receipt, so I do not claim otherwise.

**SOURCE-LEVEL MOVEMENT.** For the genuine Chvátal–Sankoff problem of two independent iid uniform binary strings, the retained lower endpoint remains

\[
L=0.792665992=\frac{99083249}{125000000}.
\]

Let `U_R` be P02's preceding exact four-band endpoint from `2026-09-20T07-11-24Z__radix-four-band-support-report.md`. This run uses successor **slack arithmetic**, not another successor-value support table, and proves a stronger finite dual rate `lambda_C < lambda_R`. Therefore

\[
\boxed{L\le \gamma_2\le U_C<U_R},
\qquad
U_C:=\frac{\log(4t^2)}{\log\lambda_C}.
\]

An exact positive-series logarithm certificate proves the strict separator

\[
\boxed{
U_C<0.82627594276228262501510658153729663282346199619319002388080618331256294443029954<U_R.
}
\]

Thus the tracked metric strictly moves from `U_R-L` to `U_C-L`. Diagnostic high precision, not used as proof, gives

\[
U_R-U_C\approx 1.56286669461208485518\times 10^{-80}.
\]

Status remains **PARTIAL / source OPEN**. The absolute improvement is tiny; the substantive mechanism improvement is that the universal two-step defect constant more than doubles, from `D_R` to `D_C` below.

# P02 / T02 — successor-slack congruence semigroup and a stronger C045 dual bound

## 1. Source, exact model, continuity, and ownership

The target is

\[
\gamma_2=\lim_{n\to\infty}\frac{\mathbf E\,LCS(X_1^n,Y_1^n)}n
\]

for two independent iid **uniform binary strings**. The same source letters recur across the LCS dynamic-programming grid, so the `n^2` match indicators are dependent. The independent Bernoulli matching model is not substituted anywhere in this report.

Controlling policy is `operations/PROGRESS20_2026-09-20.md`, blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`.

Fresh source navigation on 2026-09-20 recovered Alexander Tiskin, `arXiv:2212.01582v2`, submitted as v2 on 2024-08-13. The current arXiv page explicitly says that claims in the preprint about the stochastic process and `gamma` turned out to be incorrect and that the erroneous parts were omitted, while retaining the supported estimate. It still describes the coefficient as unresolved. Those withdrawn claims are not used here.

The rigorous public lower endpoint retained by the project is `0.792665992` from Heineman–Miller–Reichman–Salls–Sárközy–Soiffer (`arXiv:2407.10925`). Lueker's published 2009 upper endpoint remains `0.826280`; his JACM paper also proves convergence of the finite-state upper-bound methodology toward the true constant in its parameterized setting. The stronger C045/P02 endpoints below are repository-internal exact candidates pending later independent review and public-priority checking; they are not represented as published results.

Newest own substantive dependency:
`proofnet24/P02-progress-lcs/runs/2026-09-20/2026-09-20T07-11-24Z__radix-four-band-support-report.md`, blob `197be381f48ffcb8c9816cd332ab98d72ce809ce`.

Newest P13 companion recovered:
`proofnet24/P13-progress-lcs/runs/2026-09-20/2026-09-20T07-14-00Z__dc-bc-two-defect-width6-transfer.md`, blob `465178b40b3733349e62388f499b1334ba946039`. P13 remains on the true-source correlated boundary/reset route and improves finite-to-infinite transfer constants, not this covering/cone upper certificate.

Newest current-history LCS report recovered outside the LIVE20 pair:
`runs/prob10_2026-09-20/PROB10-02/20260920T0742Z_r17_reward_flux_span_3c71.md`, blob `e128692135d4c85a49d0920d8d7f580cb32e3f87`. R17 develops correlated reward-flux/coboundary transfer and reports no source-endpoint movement. P02 therefore remains nonduplicating on the finite covering/cone variational route.

The essential finite core remains R17 C045, `runs/R17/20260918_0926Z_fullcap6_c045_f7a1.md`, with exact all-row cone output blob `0a00ececfdfe58ec85f5a7e6c29bf2559fd58539`. C033–C035 remain withdrawn after the complement-gauge bug; C036 repaired the cocycle transport; C045 is the retained gauge-correct finite core.

Short handoff of P02's actual former target: Aldous–Fill Open Problem 2.34 remains closure-packaged at frozen `11/11`; publication novelty there remained explicitly unverified. It is not reopened. No T02 POSTED exclusion was found in the inherited current P02 continuity checks.

## 2. Frozen C045 primitive operator and the preceding four-band theorem

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

Define the integer one-step slack

\[
s_i=aV_i-b(BV)_i\ge0.
\tag{2.1}
\]

If `s_i=0`, then `b|V_i`, hence `V_i=b`, and `(BV)_i=a`.

The preceding P02 run proved that every such tight row has at least one non-tight accepted successor in each of the four coefficient bands

\[
\{0\},\quad\{1,2,3\},\quad\{4,5,6\},\quad\{7\}.
\tag{2.2}
\]

Using only `s_j>=1`, that yielded the two-step defect

\[
D_R=c_0+c_3+c_6+c_7
=147353456536129906925733975506591175200000.
\tag{2.3}
\]

The previous report also proved that coefficient counts plus interval-valued successor **witness values** alone are sharp at `D_R`. This run therefore changes mechanism exactly as required: it uses arithmetic of the successor **slacks** `s_j`.

## 3. New congruence for the weighted successor slack

Fix a tight row `i`. Define

\[
T_i:=\sum_j B_{ij}s_j.
\tag{3.1}
\]

Because the row is tight, `(BV)_i=a`. From (2.1),

\[
\begin{aligned}
T_i
&=\sum_jB_{ij}\bigl(aV_j-b(BV)_j\bigr)\\
&=a(BV)_i-b(B^2V)_i\\
&=a^2-b(B^2V)_i.
\end{aligned}
\]

Hence every tight row satisfies the new exact congruence

\[
\boxed{T_i\equiv a^2\pmod b}.
\tag{3.2}
\]

Exact reduction gives

\[
\boxed{a^2\bmod b=3275530027931543170.}
\tag{3.3}
\]

This congruence is independent of successor identities and is additional information not present in the preceding four-band support calculation.

## 4. Slack-semigroup compression

Group the nonzero successor slacks by coefficient type. For each `k`, let

\[
S_k:=\sum_{\substack{\ell\text{ accepted label of type }k\\s_{j(\ell)}>0}}s_{j(\ell)}.
\tag{4.1}
\]

Each `S_k` is a nonnegative integer. The four-band theorem (2.2) implies

\[
S_0\ge1,
\qquad S_7\ge1,
\qquad S_1+S_2+S_3\ge1,
\qquad S_4+S_5+S_6\ge1.
\tag{4.2}
\]

Moreover

\[
\boxed{T_i=\sum_{k=0}^7 c_kS_k.}
\tag{4.3}
\]

Thus every genuine tight C045 row maps into the following relaxed arithmetic set:

\[
\mathcal S=\left\{
\sum_{k=0}^7c_kS_k:
S_k\in\mathbf Z_{\ge0},\ (4.2),\ 
\sum c_kS_k\equiv a^2\pmod b
\right\}.
\tag{4.4}
\]

Successor coincidences, actual C045 graph geometry, and the upper size of individual slacks are deliberately forgotten. Therefore a lower bound proved for this relaxation is valid for every actual tight row.

## 5. Exact finite exclusion through 2200 additional tail units

Let

\[
H=2200,
\qquad
T_{\max}=D_R+Hc_7.
\]

With

\[
c_7=73482242694633120311956186136958404773,
\]

this is

\[
T_{\max}
=309014390464322771612037585007899665700600.
\]

The exact C++ checker exhausts **every** tuple `S_0,...,S_6` compatible with `T<=T_max` and (4.2), then solves the unique required residue class for `S_7` using the inverse of `c_7 mod b`. Since `T_max/c_7` is tiny compared with `b`, there is at most one positive representative for `S_7` inside the remaining budget. This is an exact exhaustive finite test, not floating search.

The execution visits

\[
232590292
\]

recursion nodes and performs

\[
224031469
\]

modular leaf tests. It finds **no** tuple in the relaxed semigroup satisfying (3.2) at or below `T_max`.

Therefore, since `T_i` is integer,

\[
\boxed{
T_i\ge D_C:=T_{\max}+1
=309014390464322771612037585007899665700601
}
\tag{5.1}
\]

for every genuine tight row.

This more than doubles the preceding tight-row defect:

\[
\boxed{
\frac{D_C}{D_R}
=2.0970963133705307889785432840\ldots>2.
}
\tag{5.2}
\]

The gain is not a decimal artifact: it is the exact exclusion of an entire semigroup interval using the new successor-slack congruence.

## 6. Stronger two-step Collatz theorem

The exact identity valid for every row is

\[
\boxed{
a^2V_i-b^2(B^2V)_i
=a s_i+b\sum_jB_{ij}s_j.
}
\tag{6.1}
\]

There are two cases.

If `s_i>0`, then `s_i>=1`. Exact arithmetic verifies

\[
D_CM\le a.
\tag{6.2}
\]

Hence

\[
a s_i+b\sum_jB_{ij}s_j
\ge a
\ge D_CM
\ge D_CV_i.
\]

If `s_i=0`, then `V_i=b`, and the new tight-row theorem (5.1) gives

\[
a s_i+b\sum_jB_{ij}s_j
=bT_i
\ge bD_C
=D_CV_i.
\]

Thus every row satisfies

\[
\boxed{
B^2V\le \frac{a^2-D_C}{b^2}V.
}
\tag{6.3}
\]

Consequently

\[
\rho(B)\le \sqrt{\frac{a^2-D_C}{b^2}}.
\tag{6.4}
\]

For an exact rational strict majorant define

\[
\boxed{
\beta_C=\frac ab-\frac{D_C}{2ab}.
}
\tag{6.5}
\]

Then

\[
\beta_C^2
=\frac{a^2-D_C}{b^2}
+\frac{D_C^2}{4a^2b^2}
>\frac{a^2-D_C}{b^2},
\]

so

\[
\rho(B)<\beta_C.
\tag{6.6}
\]

Rescaling gives

\[
\boxed{
\lambda_C:=\frac{t^2}{S}\beta_C,
\qquad
\rho(A)<\lambda_C<\lambda_R<1.
}
\tag{6.7}
\]

The preceding P02 rate used `D_R`; since `D_C>D_R`, the strict finite-operator improvement is immediate.

## 7. Dependence-preserving finite-to-infinite transfer

For completeness, the source transfer is restated under the exact assumptions used here.

The C045 covering operator enumerates accepted collations of **actual ordered source-string pairs**. At positive fugacities `(x,y)`, if its finite operator has spectral radius below `z<1`, finite dimensionality gives a constant `K<infinity` such that the total accepted collation weight of order `m` is at most `Kz^m`.

Every actual pair `(X_1^n,Y_1^n)` with `L_n>=m` has at least one accepted covering collation. The probability of each actual ordered length-`n` binary pair is exactly `4^{-n}`. By coefficient positivity,

\[
\Pr\{L_n\ge m\}
\le K(4xy)^{-n}z^m.
\tag{7.1}
\]

No probability is assigned independently to any match cell; all dependence remains inside the actual source-string pair enumeration.

For any

\[
c>\frac{\log(4xy)}{\log z},
\]

putting `m=floor(cn)` makes (7.1) exponentially small. Summing the upper tail of `L_n`, dividing by `n`, and sending `n->infinity` yields

\[
\boxed{
\gamma_2\le\frac{\log(4xy)}{\log z}.
}
\tag{7.2}
\]

Taking `x=y=t` and `z=lambda_C` gives

\[
\boxed{
U_C:=\frac{\log(4t^2)}{\log\lambda_C}.
}
\tag{7.3}
\]

Since `log(4t^2)<0` and `z -> log(4t^2)/log z` is strictly increasing on `(0,1)`, (6.7) implies

\[
\boxed{U_C<U_R.}
\tag{7.4}
\]

This is the original-problem source-level movement.

## 8. Exact logarithmic separator

A separate exact Python checker uses only rational arithmetic and

\[
-\log z
=2\sum_{j\ge0}\frac{u^{2j+1}}{2j+1},
\qquad
u=\frac{1-z}{1+z},
\]

truncated after 220 terms with the exact positive geometric remainder bound. It certifies

\[
U_C<Q<U_R,
\]

where

\[
Q=
\frac{82627594276228262501510658153729663282346199619319002388080618331256294443029954}{10^{80}}.
\]

Equivalently,

\[
\boxed{
U_C<0.82627594276228262501510658153729663282346199619319002388080618331256294443029954<U_R.
}
\]

Diagnostic high precision gives

\[
U_R-U_C\approx1.56286669461208485518\times10^{-80},
\]

but the displayed decimal is not the proof; the exact rational enclosure is.

## 9. Artifacts and immediate soundness checks

Exact semigroup checker:
`proofnet24/P02-progress-lcs/artifacts/2026-09-20T08-03-23Z__slack_semigroup_gap_checker.cpp`.
Creation commit `26f246deeefa786b96f3f9761caf332032de78df`; verified blob `02cb00168f3f499ee35585c2e0b45f8e5cfcf9fc`.

Executed semigroup output:
`proofnet24/P02-progress-lcs/artifacts/2026-09-20T08-03-23Z__slack_semigroup_gap_checker.out`.
Creation commit `fd41a0eed3ac1dcaed6b0f26e6db78972fa1ded2`; verified blob `1b0cfd5b26171547b426c2156d1f4f0432ed0eb1`. It records `232590292` exact enumeration nodes, `224031469` modular leaf tests, `congruent_relaxed_tuple_found=0`, and ends `NO_CONGRUENT_RELAXED_T_AT_OR_BELOW_THRESHOLD=PASS`, `D_NEW_TIMES_M_LE_A=PASS`, `TIGHT_ROW_SLACK_GAP_D_NEW=PASS`, `ALL_EXACT_CHECKS_PASS`.

Exact endpoint checker:
`proofnet24/P02-progress-lcs/artifacts/2026-09-20T08-03-23Z__slack_semigroup_endpoint_checker.py`.
Creation commit `5c9b6c43881cf619df78a25e5508c2c1a2cd4dfd`; verified blob `8046f51c3091766b68c03d0cacaf051a2a88740a`.

Executed endpoint output:
`proofnet24/P02-progress-lcs/artifacts/2026-09-20T08-03-23Z__slack_semigroup_endpoint_checker.out`.
Creation commit `6c542fe5bf0202ec6d8d348a10f549f40b39d8b0`; verified blob `5062597b7f27508e476409c2a5ebb8bda18f6bee`. It ends `D_NEW_STRICTLY_BEATS_D_R=PASS`, `TWO_STEP_SPECTRAL_MAJORANT_STRICTLY_IMPROVES=PASS`, `EXACT_LOG_SEPARATOR_PASS`, `SOURCE_INTERVAL_STRICTLY_SHRINKS_PASS`, `ALL_EXACT_CHECKS_PASS`.

No C045 11.6-million-state product or 93 MB witness was regenerated. The new finite computation is solely the successor-slack semigroup relaxation plus the exact endpoint enclosure.

## 10. What this proves, what it does not, and next attack

Original-problem before/after:

\[
\boxed{L\le\gamma_2\le U_R}
\quad\longrightarrow\quad
\boxed{L\le\gamma_2\le U_C<U_R}.
\]

Mechanism before/after:

\[
D_R=147353456536129906925733975506591175200000
\]

is replaced by

\[
\boxed{D_C=309014390464322771612037585007899665700601>2D_R}.
\]

This is still **not** a determination of `gamma_2`, and the stronger endpoint remains an internal exact candidate pending later independent review and priority checking.

The new route also identifies its next bottleneck. In the non-tight-row branch of (6.1), the present proof uses only `s_i>=1` and `V_i<=M`, giving the ceiling `D<=a/M`. The current `D_C` is already a substantial fraction of that ceiling. The next worthwhile P02 attack is therefore one of:

1. continue the exact semigroup exclusion only until it reaches the non-tight-row ceiling, then stop; or preferably
2. prove a stronger lower bound for `s_i/V_i` on non-tight rows from the exact residue relation `s_i == a V_i (mod b)`, which raises that ceiling and can be combined with the tight-row semigroup; or
3. use actual C045 successor identities to constrain the `S_k` semigroup further, rather than merely extending the same brute threshold.

The route will not revert to successor-value support tables already shown sharp in the previous run.

```yaml
ledger_delta:
  track: P02
  parent: T02
  target: "Chvatal-Sankoff gamma_2 for two independent iid uniform binary strings"
  model_actual: "GPT-5.6 Sol"
  reasoning_actual: UNVERIFIED
  metric: "certified width U-L"
  lower: "99083249/125000000 = 0.792665992"
  upper_before: "U_R = log(4t^2)/log(lambda_R)"
  upper_after: "U_C = log(4t^2)/log(lambda_C)"
  exact_separator: "U_C < 0.82627594276228262501510658153729663282346199619319002388080618331256294443029954 < U_R"
  movement: true
  status: PARTIAL
  source_status: OPEN
  new_theorem: "tight-row weighted successor slack T=sum_j B_ij s_j lies in a four-band integer semigroup and satisfies T == a^2 mod b; exact exclusion through D_R+2200*c7 forces T>=D_C"
  defect_before: "147353456536129906925733975506591175200000"
  defect_after: "309014390464322771612037585007899665700601"
  defect_ratio: "> 2.09709631337053078897"
  dependence: "actual iid source-string pairs; no independent Bernoulli matching"
  p13_scope: "correlated boundary/reset transfer; nonduplicating"
  r17_scope: "correlated reward-flux/history transfer; nonduplicating"
  prior_p02_handoff: "Aldous-Fill OP2.34 closure-packaged at 11/11; not reopened"
  review: "internal exact candidate; independent review and public-priority checking pending"
  semigroup_checker_commit: "26f246deeefa786b96f3f9761caf332032de78df"
  semigroup_output_commit: "fd41a0eed3ac1dcaed6b0f26e6db78972fa1ded2"
  endpoint_checker_commit: "5c9b6c43881cf619df78a25e5508c2c1a2cd4dfd"
  endpoint_output_commit: "6c542fe5bf0202ec6d8d348a10f549f40b39d8b0"
  next_attack: "raise the non-tight-row s_i/V_i floor using slack residues, then combine with the tight-row semigroup ceiling"
```
