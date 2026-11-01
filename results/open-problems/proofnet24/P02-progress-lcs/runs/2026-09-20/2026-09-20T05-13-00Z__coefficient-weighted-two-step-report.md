Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.** GPT-6 / maximum was requested, but this runtime exposes no authenticated model/effort selector or applied-effort receipt, so I do not claim otherwise.

**SOURCE-LEVEL MOVEMENT.** For the true iid-uniform binary-string Chvátal--Sankoff problem, the exact repository-internal interval shrinks strictly again. The previous endpoint is the P02 Farey--Collatz certificate

\[
U_F=\frac{\log(4t^2)}{\log\lambda_F},
\qquad
L=\frac{99083249}{125000000}=0.792665992,
\]

and this run proves a new coefficient-weighted two-step rate \(\lambda_W<\lambda_F\), hence

\[
\boxed{L\le \gamma_2\le U_W:=\frac{\log(4t^2)}{\log\lambda_W}<U_F.}
\]

Thus the tracked metric moves strictly from `U_F-L` to `U_W-L`. An exact positive-series enclosure proves the 84-decimal separator

\[
\boxed{
U_W<
0.826275942762282625015106581537296632823461996193190023880806183312562944430299564492
<U_F.
}
\]

Diagnostic high precision gives

\[
U_W=0.826275942762282625015106581537296632823461996193190023880806183312562944430299564491109755\ldots,
\]

\[
U_F=0.826275942762282625015106581537296632823461996193190023880806183312562944430299564498213694\ldots,
\]

so the source endpoint decreases by about \(7.10394\times10^{-84}\). The decimal is diagnostic only; the proof is exact. This remains PARTIAL, not a determination of \(\gamma_2\).

# P02 / T02 — coefficient-weighted two-step slack for the binary LCS covering operator

## 1. Source, current status, and continuity

The target is

\[
\gamma_2=\lim_{n\to\infty}\frac{\mathbf E\,LCS(X_1^n,Y_1^n)}n
\]

for two independent iid uniform binary strings. The same source letters generate the dependent match array; no independent Bernoulli matching model is substituted.

Fresh source check on 2026-09-20:

- Alexander Tiskin, `arXiv:2212.01582v2`, last revised 2024-08-13, still calls the binary coefficient unresolved. Its arXiv comments explicitly say that claims in the original preprint about the stochastic process and `gamma` were incorrect and were removed, while a supported estimate was retained.
- Heineman--Miller--Reichman--Salls--Sarkozy--Soiffer, `arXiv:2407.10925`, prove the retained rigorous lower bound `0.792665992` for the binary/two-string case.
- Li--Ren--Wen, published online 2026-03-02, still present determination of the two-string binary constant as open while studying the multiple-string generalization.
- Lueker's public rigorous upper bound remains `0.826280`. The stronger C045/P02 endpoint is repository-internal, exact-certified by the project, and still pending normal independent review and public-priority checking.

Controlling policy recovered: `operations/PROGRESS20_2026-09-20.md`, blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`.

Newest own substantive report recovered:

`proofnet24/P02-progress-lcs/runs/2026-09-20/2026-09-20T04-03-12Z__farey-collatz-dual-report.md`, blob `7f75484503fa5534cf357738df36fac84ace033f`.

Newest companion report recovered:

`proofnet24/P13-progress-lcs/runs/2026-09-20/2026-09-20T04-17-26Z__width2-complete-reset-language-transfer.md`, blob `c75f518881bea4c4ccda98802c3abd2d99055d6c`.

P13 remains on the correlated boundary-carry/reset route. Its new width-two coupling constant is a useful finite-to-infinite lower-transfer improvement, but P13 explicitly records that widths `w<=5` cannot beat the retained source lower endpoint. P02 therefore stays on the complementary covering/cone variational route.

Essential historical C045 dependency recovered:

`runs/R17/20260918_0926Z_fullcap6_c045_f7a1.md`.

That report records the complete six-factor local-deficiency language, the gauge-correct 11,614,187-state reachable product, the frozen positive integer witness, and the exact all-row cone certificate. Its exact cone output is

`artifacts/R17/20260918_0926Z_fullcap6_c045_f7a1_exact_cone_checker.out`, blob `0a00ececfdfe58ec85f5a7e6c29bf2559fd58539`.

The prior P02 Aldous--Fill occupation-time target remains a completed handoff and is not reopened. Root `POSTED.md` was checked; no posting exclusion covers T02.

## 2. Prior LCS attempts that constrain this run

The repository history relevant to this argument is:

1. R17 C033--C035 were withdrawn after the complement-gauge bug. C036 repaired the cocycle transport, and C045 is built on the repaired gauge.
2. C045 completed the full local-deficiency language through six factors for the existing `h=8` representation and certified
   \[
   \gamma_2\le 0.826275942762282626
   \]
   internally via a positive cone witness.
3. P02 then proved, in successive runs, an algebraic-integer strictification, primitive-content normalization, a rational two-step Collatz gap, and the bounded-denominator Farey refinement. The current exact source endpoint before this run is `U_F` from the latest report.
4. The latest P13 mechanism is a true-source dependent strip recursion, not independent matching; it improves finite-to-infinite error but does not currently raise the source lower bound.

The previous P02 report identified the highest-value next move as graph/operator-specific slack rather than another decimal or generic arithmetic strictification. This run executes that move.

## 3. Exact inherited primitive operator

At

\[
t=\frac{256717}{800000}=\frac pq,
\]

write the retained C045 operator as

\[
A=t^2H,\qquad B=SH,
\]

with

\[
S=q^6(q-p)=142418378752000000000000000000000000000000.
\]

The primitive positive label coefficients of the integer matrix `B` are

\[
q^{6-k}(q-p)p^k\quad(0\le k\le6),
\qquad p^7
\]

for the two geometric-tail labels. Therefore every positive matrix entry of `B` is a sum of one or more of these coefficients and is at least

\[
\boxed{m_0=p^7=73482242694633120311956186136958404773.}
\tag{3.1}
\]

The inherited positive integer witness `V` satisfies

\[
1\le V_i\le M,
\qquad
M=5000000000000000000,
\tag{3.2}
\]

and

\[
BV\le R V,
\qquad R=\frac ab,
\tag{3.3}
\]

where

\[
a=1995237757733917147310102692686664915858011319606812684127301,
\]

\[
b=4220452010631561279.
\]

The exact inherited constants obey

\[
\gcd(a,b)=1,\qquad b\le M<2b,
\tag{3.4}
\]

and the new checker verifies

\[
\boxed{a\ge m_0M.}
\tag{3.5}
\]

## 4. New theorem: minimum-positive-weight two-step Collatz defect

### Theorem P02-T02-E

Let `B` be a nonnegative integer matrix and `V` a positive integer vector. Assume

\[
BV\le \frac ab V,
\qquad \gcd(a,b)=1,
\qquad 1\le V_i\le M,
\]

with

\[
b\le M<2b.
\]

Assume every positive entry of `B` is at least `m_0`, and

\[
a\ge m_0M.
\]

Then

\[
\boxed{
B^2V\le \frac{a^2-m_0}{b^2}V.
}
\tag{4.1}
\]

Consequently

\[
\boxed{
\rho(B)\le \sqrt{\frac{a^2-m_0}{b^2}}
<\frac ab-\frac{m_0}{2ab}.
}
\tag{4.2}
\]

### Proof

Define the integer one-step slack

\[
s_i:=aV_i-b(BV)_i\in\mathbf Z_{\ge0}.
\tag{4.3}
\]

A direct substitution gives the exact two-step defect identity

\[
\boxed{
a^2V_i-b^2(B^2V)_i
=a s_i+b\sum_j B_{ij}s_j.
}
\tag{4.4}
\]

There are two cases.

**Case 1: `s_i>0`.** Then `s_i>=1`, so by (3.5)

\[
a s_i+b\sum_jB_{ij}s_j\ge a\ge m_0M\ge m_0V_i.
\tag{4.5}
\]

**Case 2: `s_i=0`.** Tightness gives

\[
b(BV)_i=aV_i.
\]

Since `gcd(a,b)=1`, this forces `b|V_i`; because `b<=V_i<=M<2b`, necessarily

\[
V_i=b.
\tag{4.6}
\]

Suppose for contradiction that every positive successor `j` of row `i` were also tight, so `s_j=0` whenever `B_ij>0`. The same divisibility argument then gives `V_j=b` for every such successor. Hence

\[
(BV)_i=\sum_jB_{ij}V_j=b\sum_jB_{ij},
\]

which is divisible by `b`. But tightness at `i`, together with `V_i=b`, gives `(BV)_i=a`, contradicting `gcd(a,b)=1` and `b>1`. Therefore some positive successor has `s_j>=1`. Every positive `B_ij>=m_0`, so

\[
a s_i+b\sum_jB_{ij}s_j
=b\sum_jB_{ij}s_j
\ge bm_0=m_0V_i.
\tag{4.7}
\]

Combining the two cases with (4.4) yields

\[
a^2V_i-b^2(B^2V)_i\ge m_0V_i
\]

for every `i`, proving (4.1). Collatz gives the first inequality in (4.2). For the strict rational majorant, put `R=a/b` and `d=m_0/b^2`. Since `d>0`,

\[
\left(R-\frac{d}{2R}\right)^2
=R^2-d+\frac{d^2}{4R^2}
>R^2-d.
\]

Thus

\[
\sqrt{R^2-d}<R-\frac{d}{2R}
=\frac ab-\frac{m_0}{2ab}.
\]

QED.

### Why this is a different mechanism

The preceding two-step theorem used only that some successor slack was a positive integer and therefore at least `1`. The new theorem uses a feature of the actual C045 operator that had not entered the previous certificates: a positive transition carries at least the primitive matrix weight `m_0=p^7`. The one unit of successor slack is therefore multiplied by an exact edge weight of at least `m_0`, not by `1`.

This is graph/operator-specific progress, not another characteristic-polynomial or Farey rounding step.

## 5. New finite spectral rate

Define

\[
\boxed{
\beta_W:=R-\frac{m_0}{2ab}
}
\tag{5.1}
\]

and

\[
\boxed{
\lambda_W:=\frac{t^2}{S}\beta_W.
}
\tag{5.2}
\]

Theorem P02-T02-E gives

\[
\boxed{\rho(A)<\lambda_W.}
\tag{5.3}
\]

The exact checker reconstructs the previous Farey rate `beta_F` from the inherited `R` and witness cap `M`, and proves

\[
\boxed{\lambda_W<\lambda_F<1.}
\tag{5.4}
\]

The improvement in the finite-operator correction is not merely qualitative. Exactly,

\[
\boxed{
\frac{R-\beta_W}{R-\beta_F}
=
\frac{362978618003680528349338421255245764907630477682840899534}
{168660543882229665139}
>10^{36}.
}
\tag{5.5}
\]

So the new structural slack strengthens the current Farey correction by more than thirty-six orders of magnitude at the `B`-rate level. The resulting source endpoint movement is still tiny because the C045 scale itself is extremely large, but it is now around the 84th decimal rather than the 120th.

## 6. Dependence-preserving finite-to-infinite transfer

The C027/C045 covering transfer is retained with its actual dependence structure.

The accepted-list operator enumerates actual ordered pairs of binary strings. For positive fugacities `(x,y)`, if the finite accepted-list operator has spectral radius strictly below `z<1`, finite dimensionality gives a constant `K<infinity` for which the total accepted-list weight at collation order `m` is at most `K z^m`. Coefficient positivity then counts actual source pairs and yields

\[
\Pr\{L_n\ge m\}\le K(4xy)^{-n}z^m.
\tag{6.1}
\]

No independence is assigned to the `n^2` match indicators. Dependence is preserved because the counted objects are the underlying pairs `(X_1^n,Y_1^n)`, each with exact probability `4^{-n}`.

For every

\[
c>\frac{\log(4xy)}{\log z},
\]

(6.1) decays exponentially at `m=floor(cn)`. Summing the tail and dividing by `n` gives

\[
\gamma_2\le\frac{\log(4xy)}{\log z}.
\tag{6.2}
\]

At the C045 symmetric point `x=y=t`, take `z=lambda_W`. Equation (5.3) supplies the strict spectral domination required by the finite-dimensional exponential estimate, so

\[
\boxed{
\gamma_2\le U_W:=\frac{\log(4t^2)}{\log\lambda_W}.
}
\tag{6.3}
\]

Since `0<4t^2<1` and `z -> log(4t^2)/log z` is strictly increasing on `(0,1)`, (5.4) yields

\[
\boxed{U_W<U_F.}
\tag{6.4}
\]

Thus the improvement is on the original dependent binary-string problem, not merely on an auxiliary finite operator.

## 7. Exact endpoint separator

The executed checker encloses `-log z` using the positive atanh expansion

\[
-\log z=2\sum_{k\ge0}\frac{u^{2k+1}}{2k+1},
\qquad
u=\frac{1-z}{1+z},
\]

with 160 exact rational terms and the tail bound

\[
0<\mathrm{tail}\le
\frac{2u^{2K+1}}{(2K+1)(1-u^2)}.
\]

It proves

\[
U_W<Q<U_F
\]

for the exact decimal rational

\[
\boxed{
Q=0.826275942762282625015106581537296632823461996193190023880806183312562944430299564492.
}
\]

Therefore, with

\[
L=0.792665992,
\]

the source metric moves strictly from

\[
W_{\rm before}=U_F-L
\]

to

\[
\boxed{W_{\rm after}=U_W-L<W_{\rm before}.}
\]

Diagnostic values are

\[
W_{\rm after}=0.033609950762282625015106581537296632823461996193190023880806183312562944430299564491109755\ldots,
\]

\[
W_{\rm before}=0.033609950762282625015106581537296632823461996193190023880806183312562944430299564498213694\ldots.
\]

## 8. Essential soundness artifact

Executed exact checker:

`proofnet24/P02-progress-lcs/artifacts/2026-09-20T05-13-00Z__coefficient_weighted_two_step_checker.py`

Creation commit: `e0f7e94198290f88b02afc29285cacee7d045521`.

Archived output:

`proofnet24/P02-progress-lcs/artifacts/2026-09-20T05-13-00Z__coefficient_weighted_two_step_checker.out`

Creation commit: `52dd18894267338106aa39562627de1ee4d97dd0`.

The output verifies the primitive coefficient list, `m_0=p^7`, `a>=m_0M`, the exact rational `beta_W`, exact improvement over the current Farey rate, and the exact logarithmic source separator. It ends

`EXACT_MIN_POSITIVE_COEFFICIENT_PASS`,
`EXACT_WEIGHTED_TWO_STEP_CONSTANTS_PASS`,
`EXACT_RATE_BEATS_CURRENT_FAREY_PASS`,
`EXACT_LOG_SEPARATOR_PASS`,
`SOURCE_INTERVAL_STRICTLY_SHRINKS_PASS`, and
`ALL_EXACT_CHECKS_PASS`.

The finite theorem proof above is independent of the checker; the checker certifies only the large exact arithmetic and endpoint comparison.

## 9. What remains and next attack

This still does not determine `gamma_2`. The public rigorous interval remains much wider, and the C045/P02 upper endpoint remains an internal candidate pending independent review and priority checking.

The new theorem shows that the actual size of positive transition weights matters. The remaining obvious leverage is more local and should not be replaced by another generic arithmetic polish:

1. recover or regenerate only the **tight-row successor profile** of the frozen C045 witness and prove a lower bound on
   \[
   \sum_j B_{ij}s_j
   \]
   stronger than one minimum edge weight for every tight row; or
2. prove that every tight row has at least `r>=2` positive slack successors, or that its least slack-carrying label cannot be a tail label, which would replace `m_0=p^7` by a larger exact coefficient sum; or
3. construct a local multiplicative correction to `V` supported on the finite tight/near-tight neighborhood, lowering the maximum one-step row ratio itself.

Any of these would use actual C045 graph structure and could move the endpoint many more digits. If the tight-row profile cannot be recovered from reproducible intermediates without rebuilding the full product, the next route should switch to a different variational witness family rather than spend a run on decimal compilation.

## 10. Ledger delta for P26/shared reconciliation

```yaml
ledger_delta:
  track: P02
  parent: T02
  source: "Chvatal--Sankoff binary LCS constant for two independent iid uniform binary strings"
  target: "strictly shrink a certified interval for gamma_2 with a dependence-preserving variational/dual bound"
  metric: "certified width U-L"
  lower: "99083249/125000000 = 0.792665992"
  upper_before: "U_F = log(4t^2)/log(lambda_F)"
  upper_after: "U_W = log(4t^2)/log(lambda_W)"
  exact_separator: "U_W < 0.826275942762282625015106581537296632823461996193190023880806183312562944430299564492 < U_F"
  width_before: "U_F - 0.792665992"
  width_after: "U_W - 0.792665992"
  movement: true
  source_level_movement: true
  mechanism: "coefficient-weighted two-step Collatz defect using minimum positive primitive C045 transition weight m0=p^7"
  dependence_preserved: true
  independent_bernoulli_matching_used: false
  status: PARTIAL
  source_status: OPEN
  public_priority: UNVERIFIED
  review_status: "candidate exact internal bound; independent review pending"
  companion_scope: "P13 remains on correlated boundary recursion/reset transfer; no duplication"
  prior_target_handoff: "Aldous--Fill OP2.34 remains completed/handed off; not reopened"
```

P02 status after this run: **PARTIAL, SOURCE-LEVEL MOVEMENT.**
