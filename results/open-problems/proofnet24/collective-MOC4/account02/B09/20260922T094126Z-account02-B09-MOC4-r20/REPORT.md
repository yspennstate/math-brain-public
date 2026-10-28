# account02/B09 MOC4 — rank-one reciprocal companion payment on a zero face

Run: `20260922T094126Z-account02-B09-MOC4-r20`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Outcome: **ESSENTIAL_STEP_APPLIED**. Full MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Target and fresh source state

The target is the `n=4` complex-normal Marcus–de Oliveira statement: for every complex normal `4 x 4` pair with spectra `a_i,b_i`, prove

\[
\det(A+B)\in \operatorname{conv}\left\{\prod_{i=0}^3(a_i+b_{\sigma(i)}):\sigma\in S_4\right\},
\]

including singular and repeated-spectrum cases.


The latest complete campaign-lead report actually consumed was account03/B07 `20260922T074824Z-account03-B07-MOC4-r13`, report blob `7724d19f793eb934c5fcc2b469bb9d0a108da4eb`. Its current generic strict-interior split is `MSQR` versus `NDI`; on `MSQR` a pair-Hessian kernel is a full-Hessian kernel and the Lyapunov–Schmidt quartic reserve acquires the exact nonnegative cross-split Schur-complement term. That remains the lead's first generic interior obstruction.

Two named OTHER-account results are used directly here.

1. account04/B09 `20260922T084040Z-b09-moc4-r38`, report blob `eff32b1a75051281bca2cf1b8b552060f4d285d8`, proves the zero-face cofactor factorization in the singleton gauge: for a genuine point on `P_ij=0`, the selected linear-channel mass has the exact product form
   \[
   q^+=p s^T,\qquad p,s\in\Delta_2,
   \]
   and an aligned Drury external extreme has
   \[
   q^+_e={1\over3}P_C
   \]
   for a `3 x 3` permutation matrix `P_C`. It also proves the sharp individual coefficient cap `lambda_e<=1/3`, but that cap alone leaves a positive residual on the exact structured stress direction below.
2. account01/B07 `20260922T070244Z-b07-moc4-r11`, report blob `711db07255ac0f3edc3562039d0b8d6f6e0e6d92`, supplies the exact complex spectral stress datum having one unique bad Drury external value. Its 24 endpoint maximum is
   \[
   M={3654300159\over10^9},
   \]
   whereas the unique bad external has
   \[
   E_0={2969983423\over 8\cdot10^8},\qquad
   \varepsilon:=E_0-M={232716479\over4\cdot10^9}>0.
   \]

The exact outer-coordinate conventions and external-functional enumeration were checked against account03/B09 `MOC4-SAXL-EXTERNAL-FACET-CLOSURE-v1`, verifier blob `4ab9e83916bd515f1e06a13589acfd157270f26f`.

## 2. Why a zero face has only 30 relevant outer atoms

Fix a genuine singleton zero face `P_ij=0`. The normalized Saxl/Drury outer hull has 24 Weyl and 48 external atoms, all with nonnegative singleton coordinates `P_ij`. Therefore any positive outer decomposition of a point with `P_ij=0` is automatically supported only on atoms whose same singleton coordinate vanishes. There are exactly 18 Weyl atoms and 12 aligned external atoms, hence 30 relevant atoms.

In the corresponding even-even singleton gauge, every genuine zero-face point has

\[
q^+=ps^T,\qquad p,s\ge0,\qquad \sum p_i=\sum s_j=1,                 \tag{2.1}
\]

while a distinguished aligned external atom `e=e_C` has

\[
q^+_e={1\over3}P_C.                                                  \tag{2.2}
\]

All these `q+` matrices are nonnegative and have total mass one. This is genuine same-unitary spinor information, not a bistochastic substitute.

## 3. New theorem: rank-one reciprocal companion payment

### `MOC4-ZERO-FACE-RANKONE-RECIPROCAL-PAYMENT-v1`

Fix one zero face and one aligned external atom `e=e_C` whose support value is

\[
H_e=M+\varepsilon,\qquad \varepsilon>0.                              \tag{3.1}
\]

Assume every other one of the 29 allowed outer atoms `v` is target-safe, `H_v<=M`. Suppose there is a nonnegative `3 x 3` cost matrix `c=(c_{ab})` such that for every safe allowed atom

\[
M-H_v\ \ge\ \langle c,q^+_v\rangle.                                 \tag{3.2}
\]

Reorder columns along the bad matching and write

\[
\widetilde c_{ab}=c_{a,C(b)}.
\]

Define the reciprocal payment

\[
\boxed{\displaystyle
\Psi_C(c)={2\over3}\sum_{0\le a<b\le2}
\sqrt{\widetilde c_{ab}\widetilde c_{ba}}.}                          \tag{3.3}
\]

Then every genuine point on this zero face satisfies

\[
\boxed{h-M\le \lambda_e\bigl(\varepsilon-\Psi_C(c)\bigr),}          \tag{3.4}
\]

where `lambda_e` is the coefficient of `e` in any outer decomposition of that point. In particular,

\[
\boxed{\Psi_C(c)\ge\varepsilon\quad\Longrightarrow\quad h\le M}    \tag{3.5}
\]

for the entire genuine zero face.

### Proof

Take any outer decomposition

\[
x=\lambda e+\sum_{v\ne e}\lambda_v v,
\qquad \lambda,\lambda_v\ge0,
\qquad \lambda+\sum_{v\ne e}\lambda_v=1.
\]

Because all `q+` entries are nonnegative, `(2.1)` and `(2.2)` imply on each bad-matching cell

\[
p_a s_{C(a)}\ge {\lambda\over3}.                                    \tag{3.6}
\]

Put `t_b=s_{C(b)}` and

\[
m=\min_a p_at_a.
\]

Then `m>=lambda/3`. The safe support deficit in the decomposition is

\[
D:=\sum_{v\ne e}\lambda_v(M-H_v).
\]

Using `(3.2)` and linearity of `q+`,

\[
D\ge \langle c,ps^T\rangle
      -\lambda\left\langle c,{P_C\over3}\right\rangle.              \tag{3.7}
\]

Now expand the first term after the column reordering:

\[
\langle c,ps^T\rangle
=\sum_a\widetilde c_{aa}p_at_a
 +\sum_{a<b}\left(
 \widetilde c_{ab}p_at_b+\widetilde c_{ba}p_bt_a\right).             \tag{3.8}
\]

The diagonal terms are at least `m sum_a c~_aa`. For every unordered pair, AM–GM and the rank-one identity give

\[
\begin{aligned}
\widetilde c_{ab}p_at_b+\widetilde c_{ba}p_bt_a
&\ge2\sqrt{\widetilde c_{ab}\widetilde c_{ba}
             (p_at_b)(p_bt_a)}\\
&=2\sqrt{\widetilde c_{ab}\widetilde c_{ba}
             (p_at_a)(p_bt_b)}\\
&\ge2m\sqrt{\widetilde c_{ab}\widetilde c_{ba}}.
\end{aligned}                                                        \tag{3.9}
\]

Therefore

\[
\langle c,ps^T\rangle
\ge m\left(\sum_a\widetilde c_{aa}
+2\sum_{a<b}\sqrt{\widetilde c_{ab}\widetilde c_{ba}}\right).
                                                                        \tag{3.10}
\]

Since `m>=lambda/3` and

\[
\left\langle c,{P_C\over3}\right\rangle
={1\over3}\sum_a\widetilde c_{aa},                                  \tag{3.11}
\]

substitution in `(3.7)` cancels the matching-diagonal charge and yields

\[
D\ge\lambda\Psi_C(c).                                                 \tag{3.12}
\]

Finally

\[
h-M=\lambda\varepsilon-D
\le\lambda(\varepsilon-\Psi_C(c)),
\]

which proves `(3.4)` and `(3.5)`. QED.

### Companion-mass interpretation

The previous one-third coefficient cap is the zeroth-order shadow of the same rank-one geometry. From `(3.6)`, putting `z_a=\sqrt{p_at_a}` gives `z_a>=\sqrt{\lambda/3}` and Cauchy gives `sum z_a<=1`. Hence the total `q+` mass off the bad matching is at least

\[
\Omega(\lambda)=4\sqrt{\lambda/3}-2\lambda.                           \tag{3.13}
\]

Because all remaining outer mass is at most `1-lambda`, `(3.13)` implies `lambda<=1/3`. The new theorem is stronger because it prices the **reciprocal off-matching pairs** by their actual support deficits instead of charging all companion mass at one worst scalar rate.

## 4. Exact closure of the known structured bad-external stress datum on every zero face

Use the account01/B07 exact spectra

\[
a={1\over100}(-174+93i,\ 95+23i,\ 44-179i,\ 59+38i),
\]

\[
b={1\over100}(-149+118i,\ -44-104i,\ 101+83i,\ -78+63i),
\]

with support functional

\[
L(z)=\operatorname{Im}z-{1\over40}\operatorname{Re}z.
\]

Exact enumeration reproduces the unique endpoint maximum

\[
M={3654300159\over10^9}
\]

and the unique bad external

\[
\tau=(3,2,1,0),\qquad \rho'=(2,0,1),\qquad
\varepsilon={232716479\over4\cdot10^9}.                              \tag{4.1}
\]

If a zero singleton `(i,j)` is not one of the four graph positions `j=tau(i)`, this unique bad external is absent from the 30-atom zero-face outer hull, so that zero face is already safe.

It remains to check the four aligned singletons

\[
(0,3),\ (1,2),\ (2,1),\ (3,0).                                      \tag{4.2}
\]

In every corresponding singleton gauge the bad external has the same matching support

\[
C=\{(0,2),(1,0),(2,1)\}.                                             \tag{4.3}
\]

For each zero face, the verifier constructs a nonnegative cell-cost certificate `c` by assigning to each selected-gauge unit cell the smallest target deficit among the safe Weyl atoms carrying that cell. It then checks **all 29 safe allowed outer atoms exactly** and verifies `(3.2)`. Thus no unsupported interpolation or numerical fit enters the certificate.

For the four zero faces, the three reciprocal products

\[
\widetilde c_{ab}\widetilde c_{ba},\qquad a<b,
\]

have respective minima

\[
\begin{array}{c|c}
(0,3)&7722066359586285189/8000000000000000000\\
(1,2)&59883458322870963/2000000000000000000\\
(2,1)&458752717014079761/250000000000000000\\
(3,0)&59883458322870963/2000000000000000000.
\end{array}                                                          \tag{4.4}
\]

A stronger-than-needed exact check avoids any floating square-root comparison: in every row of `(4.4)`,

\[
4\min_{a<b}(\widetilde c_{ab}\widetilde c_{ba})-9\varepsilon^2>0.    \tag{4.5}
\]

The smallest of the four exact margins in `(4.5)` is already

\[
{1428858029948453847\over16000000000000000000}>0.                   \tag{4.6}
\]

Thus even the **smallest single** reciprocal pair contributes

\[
{2\over3}\sqrt{\widetilde c_{ab}\widetilde c_{ba}}>\varepsilon,
\]

so certainly `Psi_C(c)>epsilon` on all four aligned zero faces. By `(3.5)`,

\[
\boxed{h(U)\le M\quad\text{for every true unitary }U\text{ with at least one zero entry}}
\]

for this exact complex structured stress support direction. The bad external direction therefore cannot realize a target violation on the zero-entry branch.

This is strictly stronger on this datum than account04/B09's sharp individual `lambda_e<=1/3` result: that result alone leaves at most one third of the positive external excess; the reciprocal companion payment removes the residual completely on every zero face.

## 5. Relation to the campaign lead and compact conditional route

A target counterexample gives a positive-gap true-unitary global support maximizer. The current lead architecture separates boundary escape from the generic strict interior and, after genericization, splits the latter into:

- `MSQR`: at least one genuine pair Hessian is mixed-Schur singular, with the lead's full-Hessian kernel and cross-split reserve;
- `NDI`: all six pair blocks are negative definite.

This run supplies a different geometric mechanism on the zero-face side. Whenever an external-deficient direction has one active aligned bad external on a given zero face and admits a cost certificate `(3.2)` with `Psi_C(c)>=epsilon`, that entire zero face is closed. The account01/B07 stress direction now satisfies this criterion for all possible zero singletons.

Thus an end-to-end proof would follow from two remaining families of implications:

1. **zero-face external payment:** extend `(3.2)`-`(3.5)` to every structured external-deficient direction, including faces carrying several simultaneously bad aligned externals;
2. **strict interior:** close the lead's `MSQR` and `NDI` branches using its full-Hessian cross-split equations, same-unitary compatibility, and existing subgroup/pair roofs.

The first essential missing implication exposed by the present mechanism is

**`MOC4-ZERO-FACE-MULTI-EXTERNAL-RECIPROCAL-PAYMENT-v1`**:

> On a genuine singleton zero face with several aligned external atoms above `M`, assign nonnegative cell costs (or a coupled family of costs) so that every safe outer atom pays its exact support deficit and the rank-one reciprocal products of `q+=ps^T` pay the **sum** of active external excesses. If such a simultaneous allocation fails, the failure must be exhibited by actual structured spectra/support data and the exact zero-face outer coordinates, not by an arbitrary probability matrix.

A q+-only linear supporting hyperplane cannot be enough in general: the convex hull of product probability matrices contains the entire nine-cell probability simplex. The useful information here is the **nonlinear rank-one reciprocal identity** `(p_at_b)(p_bt_a)=(p_at_a)(p_bt_b)`, exactly the information used in `(3.9)`.

## 6. Verification and claim limits

`verify_rankone_reciprocal_payment.py` uses only standard-library exact `Fraction` arithmetic. It reconstructs all 24 endpoint supports, all 48 Drury external values, the selected-gauge `q+` arrays, each 30-atom zero-face hull, all four cost matrices, every safe-atom inequality `(3.2)`, and the rational square tests `(4.5)`. The captured output is saved beside this report.

The analytic theorem itself uses no spectral division, inverse determinant, simple-spectrum assumption, or limiting argument. Its zero-face statement is therefore compatible with singular/repeated spectral data whenever the stated finite support-cost hypothesis is verified. The exact stress application is one support direction, not a proof of full MOC4.

No arbitrary bistochastic surrogate, benchmark material, credentials, unrelated private data, email/Drive content, paid model/API/Codex call, remote workflow, permission change, or public release was used. Full MOC4 remains open.
