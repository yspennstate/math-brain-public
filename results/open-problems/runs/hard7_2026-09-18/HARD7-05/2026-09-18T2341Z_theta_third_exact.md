Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. HARD7-05 frozen metric no movement: `W_{1/4}=0 -> 0`; methods B1 / B4 / B13. Substantive source movement: exact second special point `theta_{2,1/3}=1/6`.**

# HARD7-05 run 4 — exact second special point `theta_{2,1/3}=1/6`

Status: **PARTIAL for the full Molchan source problem.** The source asks for the entire function `H -> theta_{2,H}` on `0<H<1`, `H != 1/2`; this run proves one additional exact value, `H=1/3`. The already frozen admission metric `W_{1/4}` was saturated in run 3 and therefore honestly remains `0 -> 0`; I do not replace it with an easier metric or relabel this theorem as movement of that metric.

## 1. Continuity, source, ownership, repository read

I resumed the exclusive canonical claim

`operations/claims/MOLCHAN-2025-THETA2H.md`

owned by `HARD7-05`, and the latest checkpoint

`runs/hard7_2026-09-18/HARD7-05/2026-09-18T2237Z_theta_quarter_exact.md`.

Before new mathematics I re-read the governing HARD7 control, the 16 September new-methods policy and owner directive, `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the current claim, the newest neighboring HARD7-04 and HARD7-06 reports, and targeted repository/intake search results for integrated-fBM persistence. The large `probability_1000_intake_*/problems.jsonl` ledgers cannot be rendered literally in full through the connector without truncation, so the intake reread is honestly targeted rather than a claimed byte-for-byte full scan. The current claim search still returns this exact source family as HARD7-05-owned; no release, duplicate owner, posted equivalent, or canonical collision was found.

The primary source remains G. Molchan, *Persistence probabilities for fractionally integrated fractional Brownian noise*, arXiv:2509.10265. Run 3 verified the current source as v11, revised 4 July 2026, and read the current PDF statement that the `alpha=2`, `H != 1/2` exponent values remain unsolved. In this run I refreshed the live arXiv record and bounded current-literature searches dated 19 September 2026 for

- `theta_{2,1/3} integrated fractional Brownian persistence`,
- `integrated fractional Brownian H=1/3 persistence exponent`,
- the exact Molchan title/identifier,
- and the covariance comparison family used below.

The searches recovered Molchan's paper, Aurzada--Kilian (2022), Molchan's earlier persistence bounds, and numerical/adjacent persistence literature, but no exact determination of `theta_{2,1/3}`. This is a bounded negative search, **not** proof of worldwide novelty.

The scheduler capability statement remains unchanged: GPT-6/maximum is prompt-requested only; the exposed scheduler interface has no model selector, no reasoning-effort selector and no guaranteed duration. Historical `You cannot modify this task` failures are scheduler-ownership/platform issues; the authorized workaround is account/workspace ownership resolution or platform support, not a duplicate schedule or permission bypass. No scheduler was modified in this run.

## 2. Frozen metric and source-relevant auxiliary progress

The fixed admission metric is still

`W_{1/4} = U_{1/4}-L_{1/4}`.

Run 3 proved `theta_{2,1/4}=1/8`, so

\[
W_{1/4}=0\longrightarrow0.
\]

There is therefore **no movement in the frozen metric**. However, the source problem is a function of `H`, and this run proves a second exact point:

\[
\boxed{\theta_{2,1/3}=\frac16}.
\]

This is real source progress but does not close the source problem.

## 3. Starting point: exact source covariance at `H=1/3`

From run 1, for `p=2H`, the variance-one Lamperti transform of integrated fBM has correlation

\[
R_H(t)=
\frac{p+2}{2(p+1)}T^{-(p+2)/2}
\left[
T^{p+1}+T-
\frac{T^{p+2}+1-(T-1)^{p+2}}{p+2}
\right],\qquad T=e^t.
\tag{3.1}
\]

Set `H=1/3`, hence `p=2/3`, and put

\[
x=e^{-t/9}\in(0,1].
\]

Then `T=x^{-9}` and exact simplification gives

\[
\boxed{
R_{1/3}(t)=
\frac{3(1-x^9)^{8/3}+8x^9+8x^{15}-3-3x^{24}}
{10x^{12}}.
}
\tag{3.2}
\]

Molchan's current lower bound gives

\[
\theta_{2,H}\ge \frac12(H\wedge(1-H)),
\]

so at `H=1/3`,

\[
\boxed{\theta_{2,1/3}\ge\frac16}.\tag{3.3}
\]

The goal is therefore an exact Slepian upper comparison at exponent `1/6`.

## 4. B13 — find what only increases: the fixed-exponent comparison ray

Molchan's exactly solvable stationary family from current Statement 1.4 has covariance

\[
K_m(s)=\frac{\cosh((1-2m)s/2)}{\cosh(s/2)},
\qquad 0<m\le\frac12,
\tag{4.1}
\]

and persistence exponent

\[
\theta(K_m)=\frac38m.
\tag{4.2}
\]

After time-rescaling by `c`, the exponent becomes `(3/8)cm`. To match the lower endpoint `1/6`, keep

\[
q:=cm=\frac49.
\tag{4.3}
\]

The resulting fixed-exponent family is

\[
K_m^{(q)}(t)
=
\frac{\cosh((1-2m)qt/(2m))}{\cosh(qt/(2m))}.
\tag{4.4}
\]

This family has a simple monovariance that was not used in run 3. Write `s=qt>0` and `u=e^{-s/m}`. Then

\[
K_m^{(q)}(t)
=e^{-s}\frac{1+e^{2s}u}{1+u}.
\tag{4.5}
\]

For fixed `s>0`, the right-hand side is strictly increasing in `u`, because

\[
\frac{d}{du}\left(e^{-s}\frac{1+e^{2s}u}{1+u}\right)
=
 e^{-s}\frac{e^{2s}-1}{(1+u)^2}>0.
\tag{4.6}
\]

Also `u=e^{-s/m}` is strictly increasing in `m`. Hence

\[
\boxed{m\mapsto K_m^{(q)}(t)\text{ is strictly increasing for every }t>0.}
\tag{4.7}
\]

Thus once a comparison `K_m^{(q)}<=R_{1/3}` is proved at one endpoint `m=m_*`, it automatically holds for every smaller `m` on the same fixed-exponent ray. This is the B13 monovariant.

The local quadratic condition selects a natural admissible range. Run 1 gives

\[
R_{1/3}(t)=1-\frac{1-(1/3)^2}{2}t^2+o(t^2)
=1-\frac49t^2+o(t^2).
\]

For (4.4), the quadratic coefficient is `q^2(1-m)/(2m)`. Local domination `R>=K` therefore requires

\[
\frac{q^2(1-m)}m\ge 1-H^2,
\]

which at `H=1/3`, `q=4/9`, becomes

\[
 m\le\frac2{11}.
\tag{4.8}
\]

The rational endpoint

\[
 m=\frac16,
\qquad c=\frac q m=\frac83
\tag{4.9}
\]

lies safely inside (4.8), is algebraically simple, and by (4.7) is the hardest point of the entire subray `0<m<=1/6`.

Its covariance is

\[
\boxed{
K(t)=K_{1/6}\!\left(\frac83t\right)
=
\frac{\cosh(8t/9)}{\cosh(4t/3)}.
}
\tag{4.10}
\]

Its exact persistence exponent is

\[
\boxed{
\theta(K)=\frac83\cdot\frac38\cdot\frac16=\frac16.
}
\tag{4.11}
\]

## 5. B4 — prove a weaker statement completely: all-lag domination at `H=1/3`

### Theorem 1
For every `t>=0`,

\[
\boxed{
R_{1/3}(t)\ge
\frac{\cosh(8t/9)}{\cosh(4t/3)}.
}
\tag{5.1}
\]

The inequality is strict for every finite `t>0`.

### Proof
With `x=e^{-t/9}`, (4.10) becomes

\[
K(t)=x^4\frac{1+x^{16}}{1+x^{24}}.
\tag{5.2}
\]

All denominators are positive on `0<x<=1`. Using (3.2), inequality (5.1) is equivalent to

\[
F(x):=3(1+x^{24})(1-x^9)^{8/3}+P(x)\ge0,
\tag{5.3}
\]

where

\[
P(x)=
(1+x^{24})(8x^9+8x^{15}-3-3x^{24})
-10x^{16}(1+x^{16}).
\tag{5.4}
\]

If `P(x)>=0`, (5.3) is immediate. Suppose `P(x)<0`. Define the cubic defect

\[
D(x):=
27(1+x^{24})^3(1-x^9)^8+P(x)^3.
\tag{5.5}
\]

Because `P<0`, positivity of `D` is exactly

\[
[3(1+x^{24})(1-x^9)^{8/3}]^3 > (-P)^3,
\]

and strict monotonicity of the cube root then gives

\[
3(1+x^{24})(1-x^9)^{8/3}>-P,
\]

which is (5.3). It remains only to prove `D(x)>0` for `0<x<1`.

The exact algebraic factorization is

\[
D(x)=x^{15}(1-x)^6Q(x),
\tag{5.6}
\]

where `Q` is a reciprocal integer polynomial of degree `108`:

\[
Q(x)=x^{108}Q(1/x).
\tag{5.7}
\]

The positivity problem therefore should not be treated as a generic degree-108 root-isolation problem. B1 below changes category and makes its sign transparent. QED modulo the exact positivity statement established in the next section.

## 6. B1 — change category: reciprocal polynomial to a positive cone

Because `Q` is reciprocal of even degree `108`, there is a unique integer polynomial `q` of degree `54` such that

\[
Q(x)=x^{54}q\left(x+x^{-1}\right).
\tag{6.1}
\]

For `x>0`, define

\[
y=x+x^{-1}\ge2,
\qquad
z=y-2=\frac{(1-x)^2}{x}\ge0.
\tag{6.2}
\]

The exact checker constructs `q` through the recurrence

\[
S_0(y)=2,\quad S_1(y)=y,\quad S_k(y)=yS_{k-1}(y)-S_{k-2}(y),
\]

for `S_k(x+x^{-1})=x^k+x^{-k}`, verifies the reconstruction identity (6.1), and then expands

\[
q(z+2)=\sum_{j=0}^{54} a_j z^j.
\tag{6.3}
\]

The exact integer certificate gives

\[
\boxed{a_j>0\quad\text{for all }0\le j\le54},
\tag{6.4}
\]

with

\[
\min_j a_j=216,\qquad a_0=512000,\qquad a_{54}=216.
\tag{6.5}
\]

Therefore `q(y)>0` for every `y>=2`, hence by (6.1)

\[
Q(x)>0\qquad(x>0).
\tag{6.6}
\]

Combining (5.6) and (6.6),

\[
D(x)>0\qquad(0<x<1).
\]

The proof of Theorem 1 is complete. This category change is materially stronger than a numerical grid or black-box root count: the degree-108 obstruction lies inside the positive-coefficient cone after the exact reciprocal substitution `z=(1-x)^2/x`.

## 7. Exact persistence consequence

The source process and comparison process are centered, stationary and variance one. Theorem 1 gives the Slepian covariance order

\[
K(t)\le R_{1/3}(t)\qquad\forall t.
\]

In the same direction used in run 3 and in Molchan's comparison arguments, this yields

\[
\theta_{2,1/3}\le \theta(K)=\frac16.
\tag{7.1}
\]

Together with the source lower bound (3.3),

\[
\theta_{2,1/3}\ge\frac16,
\tag{7.2}
\]

we obtain

\[
\boxed{\theta_{2,1/3}=\frac16}.\tag{7.3}
\]

No discretely sampled path, finite-size persistence fit, or unproved interpolation step is used.

A useful byproduct of B13 is that every reference on the fixed-exponent ray with `0<m<=1/6` also satisfies

\[
K_m^{(4/9)}(t)\le K_{1/6}^{(4/9)}(t)\le R_{1/3}(t),
\]

so the comparison is not an isolated tuned point: it sits at the endpoint of an exact monotone family.

## 8. Exact finite certificate

Checker:

`artifacts/hard7_2026-09-18/HARD7-05/2026-09-18T2341Z_theta_third_exact_check.py`

creation commit:

`ff733db59d7682a4f1e6e0f9bc4564fd6283499f`

Executed output:

`artifacts/hard7_2026-09-18/HARD7-05/2026-09-18T2341Z_theta_third_exact_check.out`

creation commit:

`8493c799c663097eb1fa8da93ad33afafe748207`

The script was executed before archival with exact SymPy integer/symbolic arithmetic and exact Python `Fraction` arithmetic. It verifies the factorization, reciprocal symmetry, degree-54 reconstruction, all 55 strict coefficient inequalities in (6.4), and the reference exponent `1/6`. Archived output ends

`ALL_EXACT_CHECKS_PASS`.

This is a self-check of the finite algebraic core, not an independent audit.

## 9. What this run tried and what happened

- **B13 (find what only increases): succeeded.** At fixed reference exponent `q=cm`, the comparison covariance is pointwise strictly increasing in `m`. This turns one exact endpoint comparison into a whole valid reference subray.
- **B4 (prove something weaker, completely): succeeded.** Instead of trying to solve all `H`, the run solved the next rational special point `H=1/3` exactly.
- **B1 (change category): succeeded.** The apparently high-degree sign problem becomes positivity of a degree-54 polynomial in `z=(1-x)^2/x` with all coefficients strictly positive.

The three methods are genuinely different from the previous run's B3/B15/B24 triple.

## 10. Honest status and next routes

The full source remains **OPEN / PARTIAL**. This track now has exact source values at

\[
H=\frac14:\quad \theta_{2,H}=\frac18,
\qquad
H=\frac13:\quad \theta_{2,H}=\frac16,
\]

in addition to the classical `H=1/2` value `1/4`, but no theorem for all `H` is claimed.

Because the frozen metric `W_{1/4}` is saturated, it cannot move again. This is only the first no-movement run after its saturation and does **not** trigger section I. A next run should keep the same source/claim and use a new triple, not repeat B1/B4/B13. Suggested directions are **B5 / B21 / B30**:

- B5: vary `H` and derive when the fixed-exponent comparison ray admits a rational endpoint whose algebraic defect is reciprocal-positive;
- B21: compare this positivity mechanism with total positivity / hyperbolic-cosine ratio inequalities elsewhere in Gaussian comparison theory;
- B30: solve one rational denominator at a time and identify the first denominator/Hurst value where the positive-cone mechanism fails.

The key next question is whether the two exact points are isolated arithmetic coincidences or the first members of an interval/family theorem.

## 11. ledger_delta

```yaml
ledger_delta:
  track: HARD7-05
  source_id: MOLCHAN-2025-THETA2H
  status: PARTIAL
  source_full_problem: OPEN
  metric: W_{1/4}
  before: 0
  after: 0
  movement: "no movement in frozen metric"
  methods: [B1, B4, B13]
  substantive_auxiliary_movement: "proved theta_{2,1/3}=1/6"
  new_exact_point: "H=1/3"
  comparison_reference:
    m: "1/6"
    c: "8/3"
    covariance: "cosh(8t/9)/cosh(4t/3)"
    exponent: "1/6"
  exact_checker_commit: ff733db59d7682a4f1e6e0f9bc4564fd6283499f
  exact_output_commit: 8493c799c663097eb1fa8da93ad33afafe748207
  exact_output_tail: ALL_EXACT_CHECKS_PASS
  independent_audits: 0
  closure: false
  next_methods: [B5, B21, B30]
```
