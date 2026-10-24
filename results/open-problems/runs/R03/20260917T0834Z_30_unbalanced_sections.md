Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED; GPT-6 / maximum was requested, but the exposed task interface still has no model-family selector, no reasoning-effort selector, and no authenticated applied-runtime telemetry, so GPT-6 maximum is not claimed. METRIC MOVED: `r(10)=222.610473674316849...` remains exact and `r(11)<=523.907004072269228... -> r(11)<=523.902278711313543...`; consecutive unchanged count `1 -> 0`. Section-B methods actually used: **#15 BREAK THE SYMMETRY ON PURPOSE; #18 SAY IT IN ANOTHER LANGUAGE; #5 ADD A PARAMETER.**

# R03 run30 — unbalanced relation slices and the basis-weighted section problem

Run ID: `20260917T0834Z_30_unbalanced_sections`  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity, source gate, and frozen metric

I continued from the newest own report

`runs/R03/20260917T0708Z_29_dense_schur_hadamard.md`

and did not restart the problem, reset any killed route, or replace the frozen metric.

Before new mathematics I recovered `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, the canonical `F0001` Rademacher-singularity lineage, newest own run29, and the newest neighboring R04 retirement/handoff report. The large intake JSONL corpus is connector-truncated, so the intake check is a targeted canonical-source/ownership recovery rather than a claim that every roughly 780-row ledger was rendered byte-for-byte. No posted exclusion or competing ownership claim was found for R03.

The dated source/current-status record is

`artifacts/R03/20260917T0834Z_30_source_status.md`.

Jain--Sah--Sawhney, arXiv:2010.06554 / GAFA 31 (2021), remains the primary modern source. For iid uniform signs their Conjecture 1.1 specializes exactly to

\[
\boxed{
\Pr(\det B_n=0)=(1+o(1))\,n(n-1)2^{1-n}.
}
\tag{1.1}
\]

Their sharp full theorem still excludes laws uniform on their support; the uniform-support result remains exponential-scale. A fresh bounded 2026-09-17 search also recovered Song--Wang's growing-corank theorem but no later primary proof of the sharp iid nonsymmetric prefactor. This is a bounded-search statement, not a novelty certificate.

Let `T_n` be the exact union of equal/opposite signed row-pair and column-pair events. Retained C225 pays their overlaps. The fixed metric is

\[
\boxed{r(n):=2^n\Pr(\det B_n=0,T_n^c),}
\tag{1.2}
\]

and source closure is equivalent to

\[
\boxed{r(n)=o(n^2).}
\tag{1.3}
\]

Run28 made

\[
\boxed{r(10)=222.6104736743168493957921796888577\ldots}
\tag{1.4}
\]

exact from the primary order-nine binary computation. The strongest retained `n=11` bound entering this run is

\[
\boxed{
r(11)\le
\frac{4080135425100039167106240490725}
{7787900129957441143457185792}
=523.907004072269227999\ldots .
}
\tag{1.5}
\]

Run29's source-equivalent dense Schur target C280 is also retained:

\[
r(n)=o(n^2)
\quad\Longleftrightarrow\quad
q_n^{UU}=o(n^2 2^{-n}),
\tag{1.6}
\]

where `q_n^{UU}` is the collision-deleted Schur small-ball average with both null directions outside the JSS structured set.

## 2. Method #15 — BREAK THE SYMMETRY: stop insisting that sparse relations be balanced

The finite modular machinery in runs20/26 used **maximally balanced** sign relations on disjoint supports. That is natural because it maximizes one Boolean slice, but it unnecessarily throws away a large number of exact-corank-two planes. This run removes that symmetry assumption.

Work at the finite point relevant for `r(11)`:

\[
m=10,\qquad p=11.
\]

For integers

\[
3\le s\le7,
\qquad
1\le k\le\lfloor s/2\rfloor,
\]

call `(s,k)` a relation type. On a fixed support `S` of size `s`, choose a projective sign relation whose coefficients contain `k` signs of the minority sign and `s-k` of the majority sign. Modulo global sign, the number of such projective lines is

\[
\boxed{
L_{s,k}=
\begin{cases}
\binom{s}{k},&2k<s,\\[1mm]
\frac12\binom{s}{k},&2k=s.
\end{cases}}
\tag{2.1}
\]

Because `p=11>s`, the modular equation is the same as the integer equation on Boolean vectors. Its Boolean slice

\[
K_{s,k}:=\{x\in\{0,1\}^s:v\cdot x=0\pmod{11}\}
\]

has exact size

\[
\boxed{H_{s,k}=|K_{s,k}|=\binom{s}{k}}
\tag{2.2}
\]

by Vandermonde.

### Local affine-fiber caps

Let `q_{s,k}` be the largest fiber of a nonzero linear functional on the `(s-1)`-dimensional relation space `v^perp`, restricted to `K_{s,k}`. The exact projective-functional checker gives

\[
\begin{array}{c|c|c|c}
s&k&H_{s,k}&q_{s,k}\\ \hline
3&1&3&2\\
4&1&4&3\\
4&2&6&4\\
5&1&5&4\\
5&2&10&6\\
6&1&6&5\\
6&2&15&10\\
6&3&20&12\\
7&1&7&6\\
7&2&21&15\\
7&3&35&20
\end{array}
\tag{2.3}
\]

Every entry is finite exact arithmetic in the executed artifact; none is inferred numerically.

Now take two projective sign relations `v,w` of types

\[
a=(s,k),\qquad b=(t,\ell)
\]

on disjoint coordinate supports, with `s+t<=10`, and put

\[
V=\operatorname{span}_{\mathbb F_{11}}\{v,w\}.
\]

Every mixed projective line in `V` has support exactly `s+t`; the only two projective lines below full support are `[v]` and `[w]`. Therefore the plane intrinsically remembers its two sparse relation lines (up to interchange).

Let

\[
b_0=10-s-t.
\]

The common Boolean slice factors exactly as

\[
C_V:=V^\perp\cap\{0,1\}^{10}
\cong K_{s,k}\times K_{t,\ell}\times\{0,1\}^{b_0},
\]

so

\[
\boxed{h=|C_V|=H_{s,k}H_{t,\ell}2^{b_0}.}
\tag{2.4}
\]

A proper hyperplane of `V^perp` has a nonzero functional component on at least one of these direct factors. Conditioning on the other factors gives the rigorous cap

\[
\boxed{
Q=\max\left\{
q_{s,k}H_{t,\ell}2^{b_0},
q_{t,\ell}H_{s,k}2^{b_0},
\mathbf1_{\{b_0>0\}}\frac h2
\right\}.
}
\tag{2.5}
\]

The last term uses the elementary fact that a nonzero functional on a Boolean free block has any one fiber on at most half the cube.

A `j`-dimensional linear span contains at most `2^j` Boolean points, while every proper span inside the eight-dimensional space `V^perp` also contains at most `Q` points of `C_V`. Hence the greedy ordered-basis count is

\[
\boxed{
B(a,b)=\prod_{j=0}^{7}
\left(h-\min\{2^j,Q\}\right).
}
\tag{2.6}
\]

After those eight basis columns are chosen, there are

\[
(h-9)(h-10)
\tag{2.7}
\]

ordered choices of two further distinct nonzero unused columns. The ten columns then span exactly `V^perp`, so the left modular nullspace is **exactly** `V`, not merely a space containing `V`. Since `s,t>=3`, `V` has no support-one or support-two projective line; thus these matrices have no zero/equal rows. The columns were selected nonzero and pairwise distinct by construction.

The number of planes for two type labels is

\[
N_{10}(a,b)
=\binom{10}{s}\binom{10-s}{t}L_{s,k}L_{t,\ell},
\tag{2.8}
\]

with a factor `1/2` exactly when `a=b`.

### R03-C281 — unbalanced disjoint-slice exact-corank-two packing

**STATUS: PROVED WITH EXECUTED EXACT CHECKER.**

Retain only pairs for which at least one local type is **not** maximally balanced:

\[
k\ne\lfloor s/2\rfloor
\quad\text{or}\quad
\ell\ne\lfloor t/2\rfloor.
\tag{2.9}
\]

These planes are new relative to the previously credited families:

- run18's plane atlas is generated by two lines from its `L_m`, consisting only of support-three balanced and support-four balanced relations;
- run20/run26's disjoint-support families use maximally balanced local relations on both supports;
- run21/run27's overlap-one planes have mixed lines whose supports drop below `s+t`, unlike the invariant support spectrum here;
- the exact-corank-three families are disjoint by nullity.

Because `[v],[w]` are the only sub-full-support lines of a disjoint-support plane, a plane with at least one unbalanced generator cannot secretly be one of the old balanced-disjoint planes.

Exactly **18** type pairs have positive basis lower bound at `m=10,p=11`. They contain

\[
\boxed{363720}
\]

new projective null planes and certify at least

\[
\boxed{
E_{10}^{\mathrm{unbal}}
=265896069414475904006400
}
\tag{C281}
\]

collision-free binary `10 x 10` matrices of exact modular corank two.

The two largest contributions already show why breaking balance matters:

\[
(3,1)\times(4,1):
107201627740899901440000,
\]

\[
(4,1)\times(4,2):
80401220805674926080000.
\]

The full 18-row table is in the archived exact output.

### R03-C282 — the `n=11` fixed metric moves

**STATUS: PROVED.** The current retained C253/M2 envelope had never credited these new planes. For an exact-nullity-two matrix on one of them, the first projective incidence contributes

\[
{2\brack1}_{11}=12.
\]

Its unique null 2-plane is not in any previously credited M2 plane family, and the matrix is not in any previous exact-corank-two correction family because its exact nullspace is different. Thus its pointwise contribution to the retained upper certificate is still all `12`, while the true singular indicator is `1`. We may therefore subtract the **full slack 11** for every matrix in C281; using only the older `11-c` slack would be unnecessarily conservative.

The normalized correction is

\[
\boxed{
\Delta_{11}
=2^{11-100}\cdot 11\,E_{10}^{\mathrm{unbal}}
=
\frac{11425221732653261500275}
{2417851639229258349412352}
=0.0047253609556851445206465\ldots .
}
\tag{2.10}
\]

Subtracting this from (1.5) gives

\[
\boxed{
r(11)\le
\frac{2040049312230419145475474052475}
{3893950064978720571728592896}
=523.9022787113135428552389980\ldots .
}
\tag{C282}
\]

The exact checker recomputes every local projective fiber, all 18 plane multiplicities, every basis product, C281's total, the full slack, and C282's rational arithmetic; the archived output ends `SELF-CHECK PASS`.

The full `n`-range is preserved. Exact values through `n=10` are retained, C282 replaces the previous `n=11` entry, and every earlier complete-domain branch remains available for `n>=12`. No restricted case is substituted for the frozen metric.

This is real movement, but it is still only finite movement. Fixed support-type catalogs remain exponentially negligible in the source asymptotic and are not promoted as an asymptotic solution.

## 3. Method #18 — SAY IT IN ANOTHER LANGUAGE: a basis-weighted hypercube-section identity

Run29 showed that worst-case pointwise Schur anticoncentration is false, even after bilateral structured-vector deletion. The right question is therefore how much **basis weight** the high-concentration sections carry.

Put

\[
d=n-1.
\]

For `w in R^d`, define the two-level sign-cube section

\[
S(w):=\{a\in\{\pm1\}^d:a\cdot w\in\{-1,+1\}\},
\qquad
N(w):=|S(w)|.
\tag{3.1}
\]

Let `B(w)` be the number of ordered real bases of `R^d` whose vectors all belong to `S(w)`.

There is an exact bijection:

- given an invertible sign matrix `A` and a sign vector `b`, put `w=A^{-1}b`; every row `a_i` of `A` then satisfies `a_i dot w=b_i in {+-1}`, so its rows form an ordered basis inside `S(w)`;
- conversely, an ordered sign basis `A` inside `S(w)` determines the sign vector `b=Aw`.

Hence

\[
\boxed{
\#\{(A,b):A\in\{\pm1\}^{d\times d}\text{ invertible},\ b\in\{\pm1\}^d,\ A^{-1}b=w\}
=B(w).
}
\tag{3.2}
\]

The right collision deletion is especially clean in these variables:

\[
b=\pm A e_j
\quad\Longleftrightarrow\quad
w=\pm e_j.
\tag{3.3}
\]

The right bordered null vector is `(-w,1)`, so its JSS structured/unstructured status also depends only on `w`.

Let `W_RU` denote the `w` which survive the right collision deletion and whose right bordered null vector is JSS-unstructured. For an ordered basis `A` inside `S(w)`, define

\[
L_A^U(w)
:=\#\{c\in S(w):
 c\notin\pm\operatorname{Row}(A),
 (-A^{-T}c,1)\text{ is JSS-unstructured}\}.
\tag{3.4}
\]

### R03-C283 — exact basis-weighted section representation

**STATUS: PROVED.** The dense Schur average from C280 is exactly

\[
\boxed{
q_n^{UU}
=2^{-(d^2+2d)}
\sum_{w\in W_{RU}}
\sum_{A\in\mathcal B(w)}L_A^U(w),
}
\tag{C283.1}
\]

where `mathcal B(w)` is the set of ordered sign bases contained in `S(w)`. In particular,

\[
\boxed{
q_n^{UU}
\le
2^{-(d^2+2d)}
\sum_{w\in W_{RU}}B(w)N(w).
}
\tag{C283.2}
\]

The sum is finite: only `w=A^{-1}b` for some invertible sign `A` and sign `b` can have `B(w)>0`.

If `I_d` is the number of invertible `d x d` sign matrices, then uniqueness of `w=A^{-1}b` also gives

\[
\sum_wB(w)=I_d2^d.
\tag{3.5}
\]

Define the **basis-weighted section law**

\[
\mu_d(w):=\frac{B(w)}{I_d2^d},
\qquad
\rho(w):=\frac{N(w)}{2^d}.
\tag{3.6}
\]

Then

\[
\boxed{
q_n^{UU}
\le
\Pr(A_d\text{ invertible})\,
\mathbb E_{\mu_d}\big[\rho(w)\mathbf1_{W_{RU}}\big].
}
\tag{C283.3}
\]

This is a genuine category change: the remaining random-inverse problem becomes a weighted enumeration problem for two-level sections of the sign cube. Aichholzer--Aurenhammer's cube-spanned-hyperplane classification and Ferber--Jain--Luh--Samotij's counting inverse Littlewood--Offord framework are directly relevant prior art, but I found no source that makes C283 by itself a novelty claim.

## 4. Method #5 — ADD A PARAMETER: concentration threshold and a sharp support cap

C283 suggests parameterizing by section concentration rather than by the coefficient vector directly.

For `tau in [0,1]`,

\[
\mathbb E_{\mu_d}[\rho\mathbf1_{W_{RU}}]
\le
\tau
+
\mu_d\{w\in W_{RU}:\rho(w)>\tau\}.
\tag{4.1}
\]

So the missing asymptotic theorem can be attacked as a **tail estimate under the basis-weighted law**, not as a false worst-case anticoncentration statement.

There is also a sharp classical pointwise support bound. Suppose `w` has exactly `s` nonzero coordinates. Absorb coefficient signs into the Rademacher variables and write their positive magnitudes as `alpha_i>0`. A sign choice is equivalent to a subset `J subset [s]`. The event

\[
\sum_i\varepsilon_i\alpha_i\in\{-1,+1\}
\]

places the positive subset sum at one of two fixed levels. Along a strict chain of subsets, the positive weighted sum strictly increases, so the corresponding family contains no chain of length three. Erdős's 1945 extension of Sperner's theorem therefore gives

\[
\boxed{
\rho(w)
\le
2^{-s}\big(M_1(s)+M_2(s)\big),
}
\tag{4.2}
\]

where `M_1(s),M_2(s)` are the two largest binomial coefficients of order `s`. For odd `s`, equal coefficients with the target levels `+-1` attain the two central layers, so the `Theta(s^{-1/2})` scale is sharp.

In particular, the UU condition from C280 forces `s>=delta n-1`, hence only

\[
\rho(w)=O_\delta(n^{-1/2})
\tag{4.3}
\]

pointwise. Run29's Hadamard family shows that this polynomial worst-case scale is real. Thus no refinement of a **uniform** Littlewood--Offord inequality can reach the exponentially small target in C280.

### R03-C284 — the remaining source obligation as a basis-weight tail

Combining C280, C283 and (4.1), it is enough to prove that for some threshold sequence `tau_n`,

\[
\tau_n=o(n^2 2^{-n})
\tag{4.4}
\]

and

\[
\boxed{
\mu_{n-1}\{w\in W_{RU}:\rho(w)>\tau_n\}
=o(n^2 2^{-n}).
}
\tag{C284}
\]

Equivalently: the highly concentrated two-level sections may exist (Hadamard cores prove that they do), but the total number of **sign bases they carry** must be exponentially negligible at the source scale.

The closest established machinery found this run is the counting inverse Littlewood--Offord framework: high concentration forces additive structure, and the counting theorem is designed to pay for how many coefficient profiles have that structure. The new difficulty is that R03 needs the count weighted by `B(w)`, the number of sign bases contained in the section, and needs the final precision `o(n^2 2^{-n})`, not merely an exponential-rate singularity bound.

This is the next asymptotic route. The finite C281/C282 improvement is useful, but I will not mistake continued fixed-support enumeration for the source proof.

## 5. Current failures and what they rule out

The killed-route ledger is preserved.

- A fixed-prime modular singularity estimate still overcounts accidental determinant divisibility.
- A universal large modular-rank floor is impossible; run23's Haemers--Peeters barrier gives collision-free matrices of logarithmic real/modular rank.
- Bounded sparse-plane catalogs move small `n` but are exponentially negligible asymptotically.
- Worst-case pointwise Schur anticoncentration is false by C279, including a bilaterally unstructured Walsh/Hadamard finite obstruction.
- The classical support-only cap (4.2) is sharp only at polynomial scale and is therefore insufficient by itself.
- Exact order-ten binary singular enumeration remains unresolved in the current finite literature, so the run28 order-nine shortcut does not yet extend to make `r(11)` exact.

What a source-level proof now needs that these routes lack is an **entropy/counting theorem for the basis-weighted high-concentration section tail** in C284.

## 6. Neighboring track / audit obligation

The newest recovered R04 state remains

`runs/R04/20260917T0310Z_i0027_retirement_handoff.md`.

It is a retirement/handoff report and introduces no new theorem claim or finite checker. Earlier R03 audits of its source-closing chain are preserved; I did not manufacture a duplicate audit this run.

R03 itself remains far from closure: the full source conjecture is OPEN, C281/C282 are finite improvements, and C283/C284 are reductions. The retained narrow audit `R02-AUDIT-R03-C253-04=PASS` does not constitute a full current-package audit. No P26 end-to-end current R03 audit and no second distinct full-package current R03 audit are recorded.

## 7. Runtime/model control status

The model-setting limitation is still present. The exposed task controls offer prompt/title, schedule/timing and enabled state, but no model-family field, reasoning-effort field, or authenticated applied-runtime telemetry. Therefore `GPT-6 / maximum` remains a prompt request only from this worker. Historical `You cannot modify this task` results are consistent with authorization/workspace boundaries; the repository records that P26 later updated from a different authorized context. Enforcing a native model selection requires an owning/admin-authorized product surface that exposes those controls, or platform support. No scheduler or permission state was changed here.

## 8. Exact artifacts and ledger delta

Executed exact checker:

`artifacts/R03/20260917T0834Z_30_unbalanced_slices_exact.py`

Archived output:

`artifacts/R03/20260917T0834Z_30_unbalanced_slices_exact.out`

The output terminates `SELF-CHECK PASS`.

```yaml
ledger_delta:
  track: R03
  target: sharp iid Rademacher matrix singularity asymptotic
  source_status: OPEN
  status: PARTIAL
  fixed_metric: r(n)=2^n P(det(B_n)=0, T_n^c), complete n-domain upper envelope
  before:
    r10: exact 222.6104736743168493957921796888577...
    r11_upper: 523.907004072269227999...
    consecutive_unchanged: 1
  after:
    r10: exact 222.6104736743168493957921796888577...
    r11_upper: 523.9022787113135428552389980480274...
    consecutive_unchanged: 0
  movement: YES
  methods: [15, 18, 5]
  new_claims:
    - R03-C281: 363720 new symmetry-broken disjoint null planes certify E=265896069414475904006400 collision-free exact-modular-corank-2 matrices at m=10,p=11
    - R03-C282: full new-plane slack lowers r(11) by 0.0047253609556851445206...
    - R03-C283: exact basis-weighted two-level sign-cube section representation of q_n^UU
    - R03-C284: source obligation reduced to a basis-weighted high-concentration section tail at o(n^2 2^-n) scale
  next_obligation: prove a counting/inverse-LO estimate for mu_d{rho(w)>tau_n} at source scale; do not return to bounded-support catalogs as the main route
  retained_audit: R02-AUDIT-R03-C253-04=PASS (claim-scoped only)
  closure: false
```

No shared root ledger, peer file, email, Drive file, public post, purchase, permission, workflow, or scheduler state was changed.
