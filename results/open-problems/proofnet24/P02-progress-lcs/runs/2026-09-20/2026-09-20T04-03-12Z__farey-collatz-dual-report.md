Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.** GPT-6 / maximum was requested, but this runtime exposes no authenticated model/effort selector or applied-effort receipt, so I do not claim otherwise.

**SOURCE-LEVEL MOVEMENT.** For the true iid-uniform binary-string Chvatal--Sankoff problem, the exact repository-internal interval shrinks strictly again. The before endpoint is the preceding P02 two-step certificate

\[
U_2=\frac{\log(4t^2)}{\log\lambda_2},
\qquad
L=\frac{99083249}{125000000}=0.792665992,
\]

and this run proves a new Farey--Collatz rate \(\lambda_F<\lambda_2\), hence

\[
\boxed{L\le \gamma_2\le U_F:=\frac{\log(4t^2)}{\log\lambda_F}<U_2.}
\]

Thus the tracked metric moves strictly from `U_2-L` to `U_F-L`. An exact rational/log enclosure supplies the 121-decimal separator

\[
\boxed{
U_F<
0.8262759427622826250151065815372966328234619961931900238808061833125629444302995644982136949828322096567193237968597809380
<U_2.
}
\]

This is still PARTIAL, not a determination of \(\gamma_2\). The gain is tiny in ordinary decimal terms, but it is a genuine new source-level upper bound and is more than 34 times the preceding two-step spectral-gap strictification at the finite-operator level.

# P02 / T02 — Farey-Collatz denominator compression for the binary LCS covering operator

## 1. Source, status, and continuity

The target is

\[
\gamma_2=\lim_{n\to\infty}\frac{\mathbf E\,LCS(X_1^n,Y_1^n)}n
\]

for two independent iid uniform binary strings. The same source letters generate all row/column match indicators; no independent Bernoulli matching model is substituted.

Fresh source check on 2026-09-20:

- Alexander Tiskin, `arXiv:2212.01582v2`, last revised 2024-08-13, states that the coefficient remains unresolved and records that erroneous claims from the earlier preprint were removed while retaining the supported estimate.
- Heineman--Miller--Reichman--Salls--Sarkozy--Soiffer, `arXiv:2407.10925`, prove the retained rigorous lower bound `0.792665992` for the binary/two-string case.
- Lueker's public rigorous upper bound remains `0.826280`; the stronger C045/P02 endpoint is a private-repository exact candidate pending normal independent review and priority checking.

The newest own substantive dependency recovered is

`proofnet24/P02-progress-lcs/runs/2026-09-20/2026-09-20T03-05-17Z__two-step-rational-collatz-report.md`.

It proves the componentwise two-step inequality used below. The relevant same-source companion reports are P13

`proofnet24/P13-progress-lcs/runs/2026-09-20/2026-09-20T03-03-05Z__one-defect-reset-exact-error.md`

on the correlated boundary-carry/reset route, and R17

`runs/prob10_2026-09-20/PROB10-02/20260920T0320Z_r17_disagreement_flux_dual_d7c9.md`

on history-coupled strip disagreement/coalescence. P02 therefore stays on the complementary covering/cone variational route and does not duplicate either mechanism.

The prior P02 Aldous--Fill occupation-time target remains a completed handoff and is not reopened. Root `POSTED.md` was checked for the controlling exclusions; no posting exclusion covers this T02 target.

## 2. Exact inherited C045 data

At

\[
t=\frac{256717}{800000},
\]

the retained C045 covering operator is

\[
A=\frac{t^2}{S}B,
\]

where `B` is a nonnegative integer matrix, the inherited positive integer witness `V` obeys

\[
1\le V_i\le M,
\qquad
M=5000000000000000000,
\]

and

\[
S=142418378752000000000000000000000000000000.
\]

The reduced one-step rational Collatz target is

\[
R=\frac ab,
\]

with

\[
a=1995237757733917147310102692686664915858011319606812684127301,
\qquad
b=4220452010631561279.
\]

The preceding P02 theorem proves, without irreducibility,

\[
\boxed{
B^2V\le xV,
\qquad
x:=\frac{a^2-1}{b^2}.
}
\tag{2.1}
\]

It then used the rational square-root majorant

\[
\beta_2=R-\frac1{2ab},
\qquad
\lambda_2=\frac{t^2}{S}\beta_2.
\tag{2.2}
\]

The new observation is that every actual row ratio in (2.1) has a denominator at most `M`, while the reduced denominator of `x` is vastly larger. That arithmetic discreteness can be exploited exactly by a Farey predecessor rather than by the generic real bound `x` itself.

## 3. New theorem: bounded-denominator Farey-Collatz refinement

### Theorem P02-T02-D

Let `C` be a nonnegative integer matrix and let `V` be a positive integer vector with

\[
1\le V_i\le M.
\]

Suppose

\[
CV\le \xi V,
\qquad
\xi=\frac pq
\]

with `p/q` reduced and `q>M`.

Assume reduced fractions `r/s` and `u/v` satisfy

\[
\frac rs<\frac pq<\frac uv,
\qquad
us-rv=1,
\qquad
s+v>M.
\tag{3.1}
\]

Then

\[
\boxed{CV\le \frac rs V}
\tag{3.2}
\]

componentwise, and consequently

\[
\boxed{\rho(C)\le \frac rs.}
\tag{3.3}
\]

### Proof

For each row put

\[
y_i:=\frac{(CV)_i}{V_i}.
\]

Because `C` and `V` are integer, `y_i` is rational; after reduction its denominator is at most `V_i`, hence at most `M`. Equation (3.1) and `q>M` imply `y_i` cannot equal `p/q`, since equality would force the reduced denominator `q` to divide a denominator no larger than `M`. Thus

\[
y_i<\frac pq<\frac uv.
\]

If `y_i>r/s`, then `y_i` lies strictly between the Farey neighbours `r/s` and `u/v`. The determinant-one condition `us-rv=1` implies the standard denominator lemma: every reduced rational strictly between these neighbours has denominator at least `s+v`. By (3.1), `s+v>M`, contradicting the denominator bound on `y_i`. Hence `y_i<=r/s` for every row, proving (3.2). Collatz applied to `C` gives (3.3). QED.

This theorem is independent of irreducibility, diagonalizability, SCC structure, or an eigenvalue computation. It extracts a stronger spectral certificate solely from an integer witness plus a denominator cap.

## 4. Exact Farey certificate for the C045 two-step operator

Reduce

\[
x=\frac{a^2-1}{b^2}.
\]

Its exact reduced denominator is

\[
\boxed{
q_x=5937405058014662746395437076377371947>M.
}
\]

The exact continued-fraction/Farey computation gives

\[
\ell:=\frac rs
=\frac{
1104002398435165599900932137085809831236281338089355842106336119228260681469295517974362268385980447059
}{4939678005094299958}
\]

and

\[
h:=\frac uv
=\frac{
20898414422832779420540013969214281279099828582862451521166721044267584845854583875738805843619718695
}{93506534235917251}.
\]

The exact checker verifies

\[
\ell<x<h,
\qquad
us-rv=1,
\]

and

\[
\boxed{s+v=5033184539330217209>M.}
\]

Therefore Theorem P02-T02-D applied to `C=B^2` and (2.1) yields

\[
\boxed{B^2V\le \ell V,\qquad \rho(B)^2\le\ell.}
\tag{4.1}
\]

The exact Farey gain over the raw two-step square-rate is

\[
x-\ell=
\frac{54573621959045121727}
{29328869172410675583462203818912063653993954701752478226}.
\tag{4.2}
\]

## 5. Rational spectral rate strictly better than the previous P02 rate

Set

\[
\Delta:=R^2-\ell>0
\]

and define

\[
\boxed{
\beta_F:=R-\frac{\Delta}{2R}.
}
\tag{5.1}
\]

This is rational. Moreover

\[
\beta_F^2
=R^2-\Delta+\frac{\Delta^2}{4R^2}
=\ell+\frac{\Delta^2}{4R^2}
>\ell.
\]

Since `beta_F>0`, (4.1) gives

\[
\boxed{\rho(B)<\beta_F.}
\tag{5.2}
\]

Because

\[
\ell<x=R^2-\frac1{b^2},
\]

we have

\[
\Delta>\frac1{b^2},
\]

and therefore

\[
\beta_F
<R-\frac{1/b^2}{2R}
=R-\frac1{2ab}
=\beta_2.
\tag{5.3}
\]

Thus define

\[
\boxed{
\lambda_F:=\frac{t^2}{S}\beta_F.
}
\tag{5.4}
\]

Then

\[
\boxed{
\rho(A)<\lambda_F<\lambda_2<1.
}
\tag{5.5}
\]

The exact improvement factor in the finite-operator rate gap is particularly clean:

\[
\boxed{
\frac{R-\beta_F}{R-\beta_2}
=
\frac{168660543882229665139}{4939678005094299958}
>34.
}
\tag{5.6}
\]

So this is not merely another digit extraction from the same rational rate: bounded-denominator arithmetic strengthens the preceding two-step strictification by more than a factor of 34.

## 6. Dependence-preserving finite-to-infinite transfer

The inherited C027 transfer remains the bridge from the finite covering operator to the original source problem. Its relevant logic is recorded here.

The covering machine enumerates actual ordered pairs of finite binary strings. At positive fugacities `(x,y)`, if its accepted-list operator has spectral radius below `z<1`, finite dimensionality gives a finite constant `K` with exponential accepted-list weight bounded by `K z^m`. Coefficient positivity then counts actual string pairs and yields

\[
\Pr\{L_n\ge m\}\le K(4xy)^{-n}z^m.
\tag{6.1}
\]

No independence is assigned to the `n^2` match indicators; all dependence remains encoded by the underlying pair `(X_1^n,Y_1^n)`, each such pair having exact probability `4^{-n}`.

For any

\[
c>\frac{\log(4xy)}{\log z},
\]

the right side of (6.1) decays exponentially at `m=floor(cn)`. Summing the tail and dividing by `n` gives

\[
\gamma_2\le\frac{\log(4xy)}{\log z}.
\tag{6.2}
\]

For the C045 symmetric point `x=y=t`, take `z=lambda_F`; (5.5) supplies the required strict spectral domination. Hence

\[
\boxed{
\gamma_2\le U_F:=\frac{\log(4t^2)}{\log\lambda_F}.
}
\tag{6.3}
\]

Because `0<4t^2<1` and the function

\[
z\mapsto\frac{\log(4t^2)}{\log z}
\]

is strictly increasing on `(0,1)`, (5.5) proves

\[
\boxed{U_F<U_2.}
\tag{6.4}
\]

Thus the source-level interval width strictly decreases.

## 7. Exact endpoint separator

The checker also certifies the strict source-level movement without floating-point assumptions. For `0<z<1` it encloses

\[
-\log z
=2\sum_{m\ge0}\frac{u^{2m+1}}{2m+1},
\qquad
u=\frac{1-z}{1+z},
\]

using 300 positive terms and the exact rational geometric tail bound

\[
0<\text{tail}\le
\frac{2u^{2K+1}}{(2K+1)(1-u^2)}.
\]

Applied to `4t^2`, `lambda_F`, and `lambda_2`, these rational intervals prove

\[
U_F<Q<U_2
\]

for the exact decimal rational

\[
\boxed{
Q=0.8262759427622826250151065815372966328234619961931900238808061833125629444302995644982136949828322096567193237968597809380.
}
\]

Diagnostic long division gives

\[
U_F=0.826275942762282625015106581537296632823461996193190023880806183312562944430299564498213694982832209656719323796859780937959385\ldots
\]

and

\[
U_2=0.826275942762282625015106581537296632823461996193190023880806183312562944430299564498213694982832209656719323796859780941163604\ldots.
\]

The displayed decimals are diagnostics; the theorem uses only the exact rational inequalities in the checker. The decrease is approximately `3.2042e-120` at the source endpoint.

## 8. Original-problem metric and interpretation

Retain

\[
L=\frac{99083249}{125000000}.
\]

Before this run:

\[
W_{\rm before}=U_2-L.
\]

After this run:

\[
\boxed{W_{\rm after}=U_F-L<W_{\rm before}.}
\]

The public literature interval remains much wider (`0.792665992` to Lueker's `0.826280`). The C045/P02 endpoint is repository-internal and pending independent review; no public-priority claim is made.

Mechanism-level advance: the previous two-step theorem forced one unit of integer slack after a tight row. The new theorem notices that the resulting two-step row ratios live in the much smaller arithmetic set of rationals with denominator at most the witness cap `M`. The exact Farey predecessor skips an interval with no admissible row ratio at all. This is a reusable dual refinement for integer cone certificates.

## 9. Essential soundness artifact

Executed exact checker:

`proofnet24/P02-progress-lcs/artifacts/2026-09-20T04-03-12Z__farey_collatz_checker.py`

Creation commit `e44463e508ab00b9a0d3ec708d3b24485aef14fe`; verified blob `a0b9a10fef5e6fef715714db976b93618e63ff71`.

Archived output:

`proofnet24/P02-progress-lcs/artifacts/2026-09-20T04-03-12Z__farey_collatz_checker.out`

Creation commit `d2a98dcd11156f35b22f9c92730f592503c2aed1`; verified blob `860439c94c1a65e368bf5c0fe39387fb57d1add3`.

The output ends

`EXACT_FAREY_PREDECESSOR_CERTIFICATE_PASS`,
`EXACT_SPECTRAL_STRICTIFICATION_PASS`,
`EXACT_LOG_SEPARATOR_PASS`,
`SOURCE_INTERVAL_STRICTLY_SHRINKS_PASS`, and
`ALL_EXACT_CHECKS_PASS`.

No large C045 product table or witness was regenerated; this run uses only the previously certified componentwise inequality and witness-coordinate cap, then performs exact small arithmetic on the resulting rational data.

## 10. Residual obstruction and next attack

The source problem remains open. This run improves the upper endpoint but the gain is still at the `1e-120` scale because the two-step certificate itself only forces a very small absolute spectral slack.

The highest-value next P02 route is now genuinely structural rather than another rational strictification: recover enough of the C045 tight-row successor structure to prove a larger **minimum two-step deficit on every tight row**, or construct a local multiplicative correction `V_i exp(phi_i)` that lowers the maximum exact row ratio. Either would replace the arithmetic Farey gap by graph-specific slack and could move visible decimal digits. Repeating continued-fraction polishing of the same two-step inequality would be low value and should not be the next run.

```yaml
ledger_delta:
  track: P02
  parent: T02
  source: "Chvatal--Sankoff binary LCS constant for two independent iid fair binary strings"
  target: "determine gamma_2; complementary covering/cone stationary-variational route"
  metric: "certified interval width U-L"
  lower: "99083249/125000000 = 0.792665992"
  upper_before: "U_2 = log(4 t^2)/log(lambda_2)"
  upper_after: "U_F = log(4 t^2)/log(lambda_F)"
  strict_relation: "U_F < Q < U_2, with exact 121-decimal rational Q recorded in section 7"
  width_before: "U_2 - 99083249/125000000"
  width_after: "U_F - 99083249/125000000"
  movement: true
  status: PARTIAL
  source_status: OPEN
  model: "GPT-5.6 Sol"
  reasoning: "UNVERIFIED"
  mechanism: "Farey predecessor / bounded-denominator Collatz refinement of the inherited two-step integer cone certificate"
  exact_finite_core: "rho(B)^2 <= ell, where ell is the certified Farey predecessor of (a^2-1)/b^2 among rationals of denominator <= M"
  dependence_preserved: true
  bernoulli_matching_used: false
  independent_review: pending
  next_attack: "graph-specific tight-row minimum deficit or local multiplicative witness correction; do not repeat endpoint/Farey polishing"
```
