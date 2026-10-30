# FOREST / fleet03 B01 — a universal negative deletion–contraction cross term on complete graphs

**Run:** `20260922T042943Z-fleet03-B01-forest-r11`  
**Campaign:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Outcome:** `ESSENTIAL_STEP_APPLIED` plus `CANDIDATE_REFUTED` for coefficientwise deletion–contraction induction  
**Parent status:** the team lead has an internal `FULL_PROOF_CANDIDATE`; this report does not promote the Grimmett–Winkler conjecture to an established/public theorem.  
**Context:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and peer inputs

The source target is the unit-weight uniform law on **all** unrooted forests of a finite simple graph `G`, including the empty forest, disconnected forests, isolated vertices and every possible forest size. For distinct edges `e,f`, with `Z,Z_e,Z_f,Z_ef` the exact forest counts,

`Delta_G(e,f) = Z_e Z_f - Z Z_ef >= 0`.

I used the latest complete lead version available at run start:

`proofnet24/P14-probability-correlation/collective-2026-09-22/fleet01/B01/20260922T030948Z-b01-forest-auto11/report.md`, blob `58b8b1d8ac522a4eda7479400820e590c12f22aa`, version `FOREST-KN-COCKS-RECONCILED-v3`.

That candidate proves the complete-graph unit inequality by labelled-forest/Hermite formulas and transfers it to arbitrary finite simple graphs through Cocks's fixed-graph weighted upgrade plus Semple–Welsh minor closure.

I also applied the required named partner result from fleet04/B02:

`proofnet24/P14-probability-correlation/collective-2026-09-22/fleet04/B02/20260922T030824Z-fleet04-B02-forest-exchange-v1/report.md`, blob `a52ce1445eaee4c5167118baed2d089fde5b6f68`.

For disjoint marked edges of `K_5`, that report gives the exact base-forest cells

`(n00,n10,n01,n11,q)=(49,21,21,43,14)`

and proves that a `q`-only defect routing fails: `49*29=1421 > 14*(134-49)=1190`, while the ordinary switch channel `21^2=441` restores the total Rayleigh slack `210`. I use the **same K_5 disjoint-edge instance** below and expose an independent, orthogonal obstruction in a one-edge deletion–contraction interpolation.

## 2. One-edge interpolation of the Rayleigh gap

Fix `K_n`, disjoint marked edges

`e={1,2}`, `f={3,4}`,

and the bridge edge

`g={1,3}`.

Give `g` weight `t>0` and every other edge weight `1`. Because the forest generating polynomial is multiaffine in `g`, write

`Z(t)=A0+t B0`,
`Z_e(t)=Ae+t Be`,
`Z_f(t)=Af+t Bf`,
`Z_ef(t)=Aef+t Bef`.

Here `A*` counts the relevant forests avoiding `g`, while `B*` is the coefficient of `t`, equivalently the count of relevant forests containing `g` after removing its weight factor. Therefore

`Delta_n(t)=Delta_A + C_n t + Delta_B t^2`,

where

`Delta_A = Ae Af - A0 Aef`,
`Delta_B = Be Bf - B0 Bef`,

and the mixed deletion–contraction coefficient is

`C_n = Ae Bf + Be Af - Aef B0 - Bef A0`.                 (2.1)

A coefficientwise deletion–contraction proof would require, at minimum, `C_n>=0`. The rest of this report proves the opposite for **every `n>=5`**.

## 3. Reduction to five complete-graph orbit counts

Let

- `Z` = number of all forests of `K_n`;
- `E` = number containing one fixed edge;
- `J_a` = number containing two fixed adjacent edges;
- `J_d` = number containing two fixed disjoint edges;
- `K` = number containing the fixed three-edge path `e-g-f`.

By symmetry and inclusion/exclusion with respect to `g`,

`A0=Z-E`, `B0=E`,

`Ae=Af=E-J_a`, `Be=Bf=J_a`,

`Aef=J_d-K`, `Bef=K`.

Thus (2.1) becomes

`C_n = 2(E-J_a)J_a - (J_d-K)E - K(Z-E)`

`    = 2E J_a - 2J_a^2 - E J_d + 2EK - KZ`.             (3.1)

This identity is exact and uses no asymptotics or probability approximation.

## 4. Labelled-forest formulas

Use the lead's standard labelled-tree/forest series

`R=z exp(R)`, `T=R-R^2/2`, `F=exp(T)`, `A=exp(R)`.

If a fixed connected tree on `r` prescribed vertices is required to be present, deleting its `r-1` prescribed edges splits its host tree uniquely into `r` rooted trees, one at each prescribed vertex, while all other components remain an arbitrary forest. Hence

`#(forests containing the prescribed tree) = (n-r)! [z^(n-r)] F A^r`.

Therefore

`E   = (n-2)! [z^(n-2)] F A^2`,
`J_a = (n-3)! [z^(n-3)] F A^3`,
`K   = (n-4)! [z^(n-4)] F A^4`.

For two disjoint prescribed edges, the lead's exact same-tree/separate-tree decomposition gives

`J_d = (n-4)! [z^(n-4)] F A^4 (1 + 4/(1-R))`.           (4.1)

These preserve the unit unrooted law and all forest sizes.

## 5. Cauchy–Hermite reduction of the mixed coefficient

Let `H_j(x)=He_j(x)` be the probabilists' Hermite polynomial, defined by

`exp(xu-u^2/2)=sum_{j>=0} H_j(x) u^j/j!`.

Under the exact substitution `z=u exp(-u)`, `R=u` and `dz=exp(-u)(1-u)du`. Hence, whenever `x=m+p+1`,

`m! [z^m] F A^p = H_m(x) - m H_(m-1)(x)`,               (5.1)

while the extra factor `1/(1-R)` cancels the Jacobian factor `(1-u)` and gives

`m! [z^m] F A^p/(1-R) = H_m(x)`.                         (5.2)

Now put

`m=n-4`, `x=n+1=m+5`, `h_j=H_j(x)`,

and, for `m>=1`,

`s = m h_(m-1)/h_m`.

Using the Hermite recurrence `h_(j+1)=x h_j-j h_(j-1)`, equations (4.1), (5.1), (5.2) simplify to

`K/h_m   = 1-s`,
`J_d/h_m = 5-s`,
`J_a/h_m = 4-s`,
`E/h_m   = 2m+14-3s`,
`Z/h_m   = m^2+11m+38-(m+8)s`.                            (5.3)

Substitute (5.3) into (3.1). Direct simplification gives

`C_n/h_m^2 = -(m+1) [m-(m+5)s+s^2]`.                     (5.4)

But `x=m+5`, `s=m h_(m-1)/h_m`, and `h_(m+1)/h_m=x-s`, so

`m-(m+5)s+s^2`
` = m - s(x-s)`
` = m (h_m^2-h_(m-1)h_(m+1))/h_m^2`.

Therefore

**`C_n = -m(m+1) D_m(x)`**,                              (5.5)

where

`D_m(x)=H_m(x)^2-H_(m-1)(x)H_(m+1)(x)`.

## 6. Strict sign by an elementary Hermite Turán identity

No external inequality is needed. From the Hermite recurrence,

`D_m = H_(m-1)^2 + (m-1) D_(m-1)`,

with `D_1=1`. Iteration yields the exact identity

`D_m(x) = (m-1)! sum_{j=0}^{m-1} H_j(x)^2/j!`.            (6.1)

The right side is strictly positive for every real `x` and every `m>=1`. Combining (5.5) and (6.1),

**Theorem.** For every `n>=5`, for disjoint `e,f` in `K_n` and any bridge edge `g` joining one endpoint of `e` to one endpoint of `f`, the coefficient of `t` in the one-edge weighted Rayleigh gap `Delta_n(t)` is strictly negative:

`C_n = -(n-4)(n-3)(n-5)!`
`      * sum_{j=0}^{n-5} He_j(n+1)^2/j!  < 0`.            (6.2)

(The factorial form is just (5.5)–(6.1) with `m=n-4`.)

Thus **coefficientwise deletion–contraction positivity is impossible on every complete graph `K_n`, `n>=5`, even in this maximally symmetric orbit**.

## 7. Minimal explicit witness: disjoint edges of K5

For `n=5`, exact counts are

`Z=291`, `E=93`, `J_a=23`, `J_d=29`, `K=5`.

The last two small connected counts can also be seen directly: a fixed 3-edge path on four vertices can either leave the fifth vertex isolated or attach it to one of the four path vertices, giving `K=5`; the other counts agree with the lead's exact EGF formulas.

Consequently

`Z(t)=198+93t`,
`Z_e(t)=Z_f(t)=70+23t`,
`Z_ef(t)=24+5t`,

so

**`Delta_5(t)=148 - 2t + 64t^2`.**                        (7.1)

The middle coefficient is negative. At unit weight,

`Delta_5(1)=148-2+64=210`,

exactly the same `210` slack found independently in the fleet04/B02 component-reservoir calculation.

This is a source-valid counterexample to the candidate mechanism

`FOREST-COEFFICIENTWISE-DELETION-CONTRACTION-v1`,

**not** a counterexample to the Grimmett–Winkler inequality. Indeed (7.1) remains positive for every real `t` because its discriminant is negative.

## 8. What a viable deletion–contraction induction must prove instead

For a general graph/matroid and a third edge `g`, the one-coordinate gap has the exact form

`Delta(t)=Delta_del + C_g t + Delta_con t^2`.

Even if deletion and contraction already satisfy the desired inequality, this run proves one cannot demand `C_g>=0`. When `C_g<0`, positivity for all `t>0` instead requires the sharp quadratic compatibility condition

`C_g >= -2 sqrt(Delta_del Delta_con)`.                     (8.1)

Thus (8.1), or a stronger structural statement implying it, is the genuine missing implication for a deletion–contraction induction. The complete-graph family (6.2) shows that any proof of (8.1) must permit cancellation between the deletion and contraction sectors.

This is consistent with the named partner's independent K5 obstruction: their `q`-only reservoir is too small and must be supplemented by the ordinary switch channel. Here the same K5 unit slack `210` is likewise assembled from two positive endpoint gaps `148` and `64` **minus** a mixed contribution `2`. Both coordinate systems rule out a purely local/nonnegative routing proof.

## 9. Public-source consistency check

Semple and Welsh define a matroid to be **strongly independence correlated** when every coefficient of its multivariate independence Rayleigh difference is nonnegative. Their final paper states that `M(K4)` is not strongly independence correlated and proves that a binary matroid is strongly independence correlated iff it has no `K4` minor (Theorem 4.2). Thus negative coefficient phenomena are already known to be unavoidable in complete-graph graphic matroids. The explicit family (6.2) is a more specialized one-variable deletion–contraction obstruction tailored to the present FOREST route.

Source: C. Semple and D. Welsh, *Negative Correlation in Graphs and Matroids*, Combinatorics, Probability and Computing 17 (2008), 423–435, DOI `10.1017/S0963548307008978`, especially Proposition 3.5, Theorem 4.2, and the Section 5 note recording Cocks's fixed-graph implication. The final author PDF explicitly states that if Conjecture 1.1 holds for a graph `G`, then `M(G)` is independence correlated.

## 10. Status and handoff

**Outcome:** `ESSENTIAL_STEP_APPLIED` with `CANDIDATE_REFUTED` for coefficientwise deletion–contraction induction.

The team's current end-to-end candidate remains intact: this report found no contradiction in the lead's complete-graph/Hermite theorem or the Cocks/Semple–Welsh transfer. Instead it proves a new no-go theorem for an appealing direct recursive mechanism and isolates the exact replacement inequality (8.1).

**Next recipient:** lead `fleet01/B01` and named partner `fleet04/B02`.

**Useful handoff:** equations (2.1), (3.1), (5.5), (6.2), and the minimal polynomial `Delta_5(t)=148-2t+64t^2`. A productive next direct route is to seek a structural proof of (8.1), potentially by pairing the partner's ordinary-switch and overlap-reservoir channels across deletion/contraction slices rather than preserving either slice separately.

No brain installation/benchmark work, scheduler mutation, email/Drive/public posting, workflow dispatch, paid compute, cross-account native action, or unrelated private material was used.
