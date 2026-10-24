Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED; GPT-6 / maximum was requested, but the accessible runtime exposes no model-family selector, no reasoning-effort selector, and no authenticated applied-runtime telemetry, so GPT-6 maximum is not claimed. NO MOVEMENT on the fixed full-range numerical envelope: `r(10)=222.6104736743168493957921796888577...` remains exact and `r(11)<=523.4894710902614257202829985613411...` remains the strongest replay-certified bound; unchanged count `0 -> 1`. Methods used: #27 SWAP THE QUANTIFIERS, #14 FIND THE GROUP ACTING, #5 ADD A PARAMETER.**

# R03 run36 — basis-row encoding and the near-distinct-magnitude frontier

Repository / branch: `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL; source OPEN.** The fixed finite envelope does not move. The substantive progress is a theorem-sized asymptotic reduction that pushes the dense corank-one obstruction from the run35 square-root coefficient-complexity window to normals whose absolute coefficient magnitudes are almost all distinct. No source-closure claim is made.

All thirty Section-B moves had already appeared in the R03 history by run34. A literally unused move therefore no longer exists. I reuse #27/#14/#5 in new roles; this triple is different from run35's #3/#17/#26 and does not reset any prior failure or stagnation history.

## 1. Continuity, source match, exclusions and frozen metric

Before new work I reread the required campaign controls `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, the F0001 intake record, the newest complete own report `runs/R03/20260917T1308Z_35_sqrt_cutoff_support35.md` at creation commit `fd1dc9fb73f03fe4e089619e1506a076e22fe3f9`, and the newest neighboring R02/R04 states.

R02 has rotated to I0121 / Frankl's union-closed sets conjecture; R04 has retired repeated I0027 research after six unchanged runs. Neither is a competing Rademacher-singularity track. `POSTED.md` and `INDEX.md` still do not settle or retire F0001.

The outside source remains intake `F0001`, Van H. Vu, *Recent progress in combinatorial random matrix theory*, arXiv:2005.02797 / Probability Surveys 18 (2021), Conjecture 2.2:

\[
p_n=(2+o(1))n^2 2^{-n}
\]

for an iid uniform Rademacher `n x n` matrix. Thus the campaign target

\[
\boxed{\Pr(\det B_n=0)=(1+o(1))n(n-1)2^{1-n}}
\tag{1.1}
\]

is retained only after source matching.

Let `T_n` be the exact union of equal/opposite signed row-pair and column-pair events. Retained C225 pays their overlaps. The fixed R03 remainder is

\[
\boxed{r(n):=2^n\Pr(\det B_n=0,T_n^c),}
\tag{1.2}
\]

and source closure remains equivalent to

\[
\boxed{r(n)=o(n^2).}
\tag{1.3}
\]

Fresh primary-literature checking on 2026-09-17 still leaves (1.1) open. Jain--Sah--Sawhney, arXiv:2010.06554 / GAFA 2021, prove the sharp elementary-mechanism asymptotic for finite-support entry laws that are **not uniform on their support**; for uniform support they obtain exponential-scale full singularity precision and sharp compressible-sector control, not the Rademacher polynomial prefactor. Song--Wang, arXiv:2607.00495 (2026), determine a growing-corank Bernoulli regime; Hunter--Kwan--Sauermann--Sawhney, arXiv:2510.12933, prove exponential suppression of large corank. Neither supplies the missing corank-one prefactor. The dated source and prior-art record is `artifacts/R03/20260917T1405Z_36_source_status.md`, creation commit `0501ba8d60203e1ae464d2454bc18b0e0a7dbc40`.

Pre-run and post-run finite envelope:

\[
r(10)=222.6104736743168493957921796888577\ldots
\]

exactly, and

\[
\boxed{
r(11)\le
\frac{32615069759481592686393385491735}
{62303201039659529147657486336}
=523.4894710902614257202829985613411\ldots .
}
\tag{1.4}
\]

All retained branches for `n>=12` remain available. Nothing below weakens any part of the full `n`-range.

## 2. Retained geometric reduction

Put `d=n-1`. For a uniformly random invertible sign matrix

\[
R\in\{\pm1\}^{d\times d},
\]

write

\[
w_R=R^{-1}{\bf1},
\qquad
C(w)=\{x\in\{\pm1\}^d:\langle x,w\rangle=1\},
\qquad
M(w)=|C(w)|,
\tag{2.1}
\]

and let

\[
\kappa(w)=\#\{|w_i|:w_i\ne0\}
\tag{2.2}
\]

be the number of distinct nonzero absolute coefficient magnitudes.

Run31/C285 reduced the dense corank-one remainder, after the retained JSS structured-sector and higher-corank payments, to the basis-weighted excess `(M(w_R)-d)_+`. Run35/C292 proved that for every fixed `delta>0` and every fixed `c<1/sqrt(2)`, the dense sector

\[
|\operatorname{supp}w_R|\ge\delta d,
\qquad
\kappa(w_R)\le c\sqrt d
\]

has expectation at most `exp(-(1-o(1)) d log log d)` and hence is negligible far below the source scale.

The run35 bottleneck was the entropy cost of enumerating all possible affine section patterns before counting sign bases. The present run reverses that order.

## 3. Method #27 — SWAP THE QUANTIFIERS: let actual basis rows determine the magnitudes

Fix `k>=1`. An **unlabeled signed magnitude assignment** for a vector with exactly `k` distinct nonzero absolute values consists of:

1. its nonzero support `S`;
2. a partition of `S` into `k` nonempty blocks, coordinates in one block having the same absolute value;
3. the sign of every nonzero coordinate.

If `S(s,k)` is a Stirling number of the second kind, the number of such assignments is

\[
A_{d,k}
=
\sum_{s=k}^d {d\choose s}2^s S(s,k).
\tag{3.1}
\]

Using `S(s,k)<=k^s/k!`,

\[
\boxed{
A_{d,k}
\le
\frac{(1+2k)^d}{k!}.
}
\tag{3.2}
\]

Fix one assignment. Canonically label its `k` blocks, for example by the least coordinate in each block. Write the corresponding positive distinct magnitudes as

\[
a=(a_1,\ldots,a_k).
\]

For a sign row `r in {+-1}^d`, define its block-sum vector

\[
z(r)_j
=
\sum_{i\in B_j}\sigma_i r_i,
\tag{3.3}
\]

where `sigma_i` is the fixed sign of `w_i` in the assignment. Then

\[
\langle r,w\rangle=1
\quad\Longleftrightarrow\quad
z(r)\cdot a=1.
\tag{3.4}
\]

### R03-C294a — the block-sum rows span all magnitude parameters

**STATUS: PROVED.** If `R` is invertible and `Rw=1` with the fixed assignment above, then the `d` vectors

\[
z(r_1),\ldots,z(r_d)\in\mathbb R^k
\]

span `R^k`.

**Proof.** Suppose `h in R^k` is orthogonal to every `z(r_l)`. Define `u in R^d` by

\[
u_i=\sigma_i h_j\quad(i\in B_j),
\qquad
u_i=0\quad(i\notin\operatorname{supp}w).
\]

Then for every row `r_l` of `R`,

\[
(Ru)_l=z(r_l)\cdot h=0.
\]

Thus `Ru=0`. Since `R` is invertible, `u=0`; every block is nonempty, so `h=0`. Hence the block-sum rows span `R^k`. QED.

Therefore **some `k` actual rows of the invertible basis determine all `k` magnitudes**. Choose an index set `I subset [d]`, `|I|=k`, for which the matrix

\[
Z_I=(z(r_i))_{i\in I}
\]

is nonsingular. Then

\[
\boxed{a=Z_I^{-1}{\bf1}.}
\tag{3.5}
\]

This is the key quantifier swap. Run35 counted possible sections first and then asked how many bases lie in them. Here one first chooses `k` rows of the basis; they uniquely determine the numerical magnitudes, so only the **remaining `d-k` rows** have to be paid by a Littlewood--Offord concentration factor.

## 4. Method #14 — FIND THE GROUP ACTING: quotient permutations of magnitude labels

The factor `1/k!` in (3.2) is not cosmetic. The names of the magnitude classes have no mathematical meaning; the symmetric group on the `k` classes acts by relabeling. Counting set partitions rather than labeled colorings quotients this action before any analytic estimate is applied.

Without this quotient one would pay roughly `(2k+1)^d`; with it one pays `(2k+1)^d/k!`. In the near-distinct regime `k=d-s`, `log k!` removes almost `d log d` units of entropy and is exactly what makes the following bound useful.

Let `I_d` denote the number of invertible `d x d` sign matrices. Tikhomirov's singularity theorem gives

\[
I_d=(1-o(1))2^{d^2},
\]

so for all sufficiently large `d`,

\[
I_d\ge2^{d^2-1}.
\tag{4.1}
\]

For `k` distinct nonzero absolute coefficients, select one coordinate from each magnitude class and condition on all other signs. After absorbing the fixed coefficient signs, the selected coefficients have distinct positive magnitudes. The classical Sárközy--Szemerédi theorem gives the atom bound

\[
\sup_t\Pr\!\left(\sum_{j=1}^k\varepsilon_j a_j=t\right)
\le Ck^{-3/2}
\tag{4.2}
\]

for an absolute `C`. Consequently every such affine cube section obeys

\[
\boxed{
M(w)\le C\,2^d k^{-3/2}.
}
\tag{4.3}
\]

Now count the contribution for exact coefficient complexity `k`. For each magnitude assignment:

- choose the determining row set `I`: at most `binom(d,k)` choices;
- choose its `k` sign rows: at most `2^{dk}` choices;
- if `Z_I` is invertible, (3.5) fixes the magnitudes uniquely;
- choose the remaining `d-k` rows from `C(w)`;
- bound the excess weight `(M(w)-d)_+` by `M(w)`.

Thus, writing

\[
E_{d,k}:=
\mathbb E_R\big[(M(w_R)-d)_+\mathbf1_{\{\kappa(w_R)=k\}}\big],
\]

we obtain

\[
I_dE_{d,k}
\le
A_{d,k}{d\choose k}2^{dk}
\left(C2^dk^{-3/2}\right)^{d-k+1}.
\tag{4.4}
\]

Combining (3.2), (4.1) and (4.4),

\[
\boxed{
E_{d,k}
\le
2\frac{(1+2k)^d}{k!}{d\choose k}
C^{d-k+1}2^d
k^{-\frac32(d-k+1)}.
}
\tag{4.5}
\]

Using `log(k!)>=k log k-k` and `log binom(d,k)<=d H(k/d)`, where `H` is binary entropy in natural logarithms, (4.5) gives the uniform logarithmic estimate

\[
\boxed{
\log E_{d,k}
\le
-\frac12(d-k)\log k
+dH(k/d)
+O(d).
}
\tag{4.6}
\]

The `O(d)` constant is absolute.

This is the main new quantitative inequality of the run.

## 5. Method #5 — ADD A PARAMETER: the defect `s=d-k`

The natural parameter in (4.6) is no longer `k` itself but the **magnitude-collision defect**

\[
s=d-k.
\tag{5.1}
\]

Run35 said that any surviving dense contribution must have `k` at least order `sqrt(d)`. Equation (4.6) shows much more: except in a thin endpoint window, the actual basis supplies enough equations to kill the section entropy.

### R03-C294 — near-distinct-magnitude localization

**STATUS: PROVED.** Fix `delta>0`. Let `s_d` be any positive sequence satisfying

\[
\frac{s_d\log d}{d}\longrightarrow\infty.
\tag{5.2}
\]

Then, for `R` uniform over invertible `d x d` sign matrices,

\[
\boxed{
\mathbb E_R\!\left[
(M(w_R)-d)_+
\mathbf1_{\{|\operatorname{supp}w_R|\ge\delta d\}}
\mathbf1_{\{\kappa(w_R)\le d-s_d\}}
\right]
=o(1).
}
\tag{C294}
\]

In fact the newly treated range contributes `exp(-omega(d))`; the only separate input is retained C292 for the already-paid small-`k` sector.

**Proof.** Fix `c_0=1/2`, which lies below `1/sqrt(2)`. Retained C292 pays

\[
\kappa(w_R)\le c_0\sqrt d,
\qquad |\operatorname{supp}w_R|\ge\delta d,
\]

by `exp(-(1-o(1))d log log d)`.

It remains to sum (4.6) over

\[
c_0\sqrt d<k\le d-s_d.
\]

If `k<=d/2`, then `d-k>=d/2` and `log k>=\frac12\log d+O(1)`, while `H(k/d)<=log 2`. Hence

\[
\log E_{d,k}
\le
-\frac18d\log d+O(d),
\tag{5.3}
\]

uniformly in this range.

Now let `d/2<k<=d-s_d` and put `s=d-k`. Since `H(k/d)=H(s/d)` and

\[
dH(s/d)\le s\log\frac{ed}{s},
\]

(4.6) gives

\[
\log E_{d,d-s}
\le
-\frac12s\log(d/2)
+s\log\frac{ed}{s}
+O(d).
\tag{5.4}
\]

For `s>=s_d`, condition (5.2) implies `s>>d/log d`, so

\[
\log\frac{s}{\sqrt d}
=\frac12\log d-o(\log d)
\]

uniformly at the smallest allowed `s`. Rewriting the first two terms of (5.4) as

\[
-s\log\frac{s}{\sqrt d}+O(s),
\]

we obtain

\[
\log E_{d,d-s}=-\omega(d)
\tag{5.5}
\]

uniformly for `s>=s_d` in this range. There are at most `d` values of `k`; summing (5.3), (5.5), and the retained C292 contribution proves C294. QED.

Because the `O(d)` in (5.4) has an absolute constant, the same proof also gives the fixed-window corollary: there exists a finite absolute `C_*` such that, for every fixed `delta>0`,

\[
\mathbb E_R\!\left[
(M(w_R)-d)_+
\mathbf1_{\{|\operatorname{supp}w_R|\ge\delta d\}}
\mathbf1_{\{\kappa(w_R)\le d-C_*d/\log d\}}
\right]
=o(1).
\tag{5.6}
\]

No numerical value of `C_*` is claimed because the classical Littlewood--Offord constant was not optimized here.

### What C294 changes

Run35/C292 localized any source-relevant dense normal to

\[
\kappa(w_R)\ge(1/\sqrt2-o(1))\sqrt d.
\]

C294 moves the frontier from square-root complexity to **near-injective absolute magnitudes**. After discarding an `o(1)` contribution, the unresolved dense sector may be restricted to

\[
\boxed{
d-\kappa(w_R)=O(d/\log d)
}
\tag{5.7}
\]

in the precise sense of (5.6), or more robustly: for every `L_d->infinity`, the sector

\[
d-\kappa(w_R)\ge L_d d/\log d
\]

contributes `o(1)`.

This is far below the source target `o(d^2)` and therefore completely pays every dense coefficient-complexity regime except a thin almost-all-distinct endpoint window.

## 6. Concrete obstruction: why this algorithm stops at the endpoint

The new route has a sharp, visible failure mode rather than a renamed coupling obstruction.

When `k=d`, C294a needs **all `d` basis rows** to determine the `d` magnitudes. There are no unexposed basis rows left, so the crucial factor

\[
\rho(w)^{d-k}
\]

that drives (4.5) becomes `1`. At the same time the Sárközy--Szemerédi bound `O(d^{-3/2})` for distinct coefficients is sharp up to constants in general. Thus a uniform pointwise improvement of (4.3) is not available as a way out.

Equivalently: in the almost-injective regime, the problem is no longer that one section is too large; it is whether **too many invertible sign bases complete into the rare large sections**. This is a basis-completion/circuit-counting question, not another ordinary Littlewood--Offord small-ball question.

This also explains why the run35 Sidon-subset experiment could not finish the source problem. Distinctness itself is no longer enough: the remaining endpoint already has essentially maximal distinctness.

## 7. Next source-level obligation

After the retained JSS structured-sector payment, the higher-corank suppression, C292, and C294, the remaining asymptotic task can be written as

\[
\boxed{
\mathbb E_R\!\left[
(M(w_R)-d)_+
\mathbf1_{\mathrm{nontrivial}}
\mathbf1_{\mathrm{JSS\text{-}unstructured}}
\mathbf1_{\{d-\kappa(w_R)\le C_*d/\log d\}}
\right]
=o(d^2).
}
\tag{7.1}
\]

The next genuinely different route should therefore use a **two-sided or circuit-level basis-completion count** in the almost-distinct regime. A promising formulation is to count `(R,x)` pairs with `x` an extra cube vertex and expose simultaneously enough rows and columns to determine both right and left corank-one normals; the current one-sided encoding loses all leverage exactly when `k=d`. That route is not claimed proved here.

The closest prior art checked this run includes Ferber--Jain--Luh--Samotij's counting inverse Littlewood--Offord framework and the classical Sárközy--Szemerédi theorem. A bounded search did not locate the exact basis-row parameter-determination inequality (4.5), but that is **not a novelty certificate**.

## 8. Finite metric, checker policy and status

The frozen numerical metric did **not** move. I therefore did not manufacture a new finite checker or receipt. C294 is a theorem-sized symbolic argument proved on the page; it has no finite computational core requiring an exact-arithmetic certificate.

The retained finite envelope remains:

- exact values through `n=10`, including `r(10)=222.6104736743168493957921796888577...`;
- `r(11)<=523.4894710902614257202829985613411...` from run35/C293;
- every previously certified branch retained for `n>=12`.

Honest status: **PARTIAL / source OPEN / no finite-metric movement / unchanged count 1.** This is not yet a Section-I stuck episode.

## 9. Model and task-control escalation status

The limitation is still present in the interface available to this worker: task controls expose prompt/title, schedule/timing and enabled-state fields, but no model-family selector, no reasoning-effort selector and no authenticated applied-runtime telemetry. GPT-6/maximum therefore remains a prompt request rather than an enforceable setting here.

The historical P26 `You cannot modify this task` event was authorization-context dependent; repository reconciliation records that P26 later updated successfully from a different authorized context. The legitimate product-level fix is an owning/admin-authorized task surface that also exposes model/reasoning controls, or a platform-side change/support intervention. This run made **no scheduler or permission modification**, as required by the deployment instruction.

## 10. Structured ledger delta

```yaml
ledger_delta:
  track: R03
  source_id: F0001
  source_status: OPEN
  mathematical_status: PARTIAL
  fixed_metric: smallest replay-certified full-range upper envelope for r(n)=2^n P(det B_n=0,T_n^c)
  before:
    r10: "222.6104736743168493957921796888577... exact"
    r11_upper: "523.4894710902614257202829985613411..."
    unchanged_count: 0
  after:
    r10: "222.6104736743168493957921796888577... exact"
    r11_upper: "523.4894710902614257202829985613411..."
    unchanged_count: 1
  movement: no
  new_claim:
    id: R03-C294
    scope: "dense corank-one affine cube sections"
    result: "for every s_d with s_d log d / d -> infinity, the basis-weighted excess from kappa(w_R)<=d-s_d is o(1); in particular some absolute C_* pays kappa<=d-C_* d/log d"
  remaining_obligation: "almost-all-distinct coefficient magnitudes; weighted two-sided/circuit basis-completion count at o(d^2) scale"
  checker: "none; no new finite claim"
  next_methods: [25, 11, 30]
```

No shared root ledger, peer file, email, Drive file, public post, purchase, permission, workflow or scheduler state was changed.