# MOC4 fleet04/B07 — rank-two parity masks for the exterior-square Bogoliubov channels

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Campaign:** MOC4, complex-normal 4-by-4 Marcus–de Oliveira target  
**Worker/run:** fleet04/B07, `20260922T034036Z-fleet04-B07-moc4-r11`  
**Assignment:** representation-theoretic / exterior-algebra proof of the shared mixed-minor constraint  
**Outcome:** `ESSENTIAL_STEP_APPLIED`; full MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Source-exact target and the two peer results used

For all complex normal `4 x 4` matrices `A,B`, with spectra
`a_1,...,a_4` and `b_1,...,b_4` counted with multiplicity, the target is

\[
\det(A+B)\in\operatorname{conv}\left\{
\prod_{i=1}^4(a_i+b_{\sigma(i)}):\sigma\in S_4
\right\}.
\tag{MOC4}
\]

The current campaign source boundary explicitly includes singular matrices and repeated
spectra and does not ask for any `n>4` statement.

The newest complete campaign-lead report read was fleet03/B07
`20260922T013930Z-fleet03-B07-MOC4-r11`, report blob
`47f09f9f722aa8501330ca532a2ca261474c681c`. It refutes
`MOC4-ZERO-ENTRY-COMMON-LIFT-v1` by an exact rational zero-entry true-unitary
witness. Hence the zero-entry branch cannot be closed by a common positive
`S_4` subset-permutation lift; the support functional itself must retain the
true exterior-square compatibility.

The required named OTHER-account partner result used substantively is fleet01/B08
`20260922T024227Z-fleet01-B08-MOC4-r12`, report blob
`0705fa57b0656cb991ae383d6a86dd56e3c33db7`. It refutes
`MOC4-BOGOLIUBOV-EVEN-LIFT-v1`: a strict exact rational orthogonal `U` has a
Bogoliubov mass array outside the convex hull of the 24 even signed matching
vertices. Therefore an unconditional positive 24-state representation is false,
even away from all zero-entry and vanishing-2-minor boundaries.

This run also preserves the exact exterior-square reduction from fleet01/B07:
for `O=Lambda^2 U` in the complementary-pair basis, each real `2 x 2` block is
written as `z -> m z+n zbar` and the exact structured support objective is

\[
Q_{K,X}(O)=\sum_{\alpha,\beta}
\left[
\left(K_{\alpha\beta}+\frac12X_{\alpha\beta}\right)|m_{\alpha\beta}|^2+
\left(-K_{\alpha\beta}+\frac12X_{\alpha\beta}\right)|n_{\alpha\beta}|^2
\right].
\tag{1}
\]

Put

\[
q^+_{\alpha\beta}=|m_{\alpha\beta}|^2,\qquad
q^-_{\alpha\beta}=|n_{\alpha\beta}|^2.
\tag{2}
\]

The earlier fleet04/B07 result `MOC4-ODD-WEYL-ORIENTATION-v1` proved only a
three-cell inequality for each odd signed matching. The new result below replaces
that by sixteen nine-cell inequalities coming from a rank obstruction in odd
complex dimension.

## 2. New theorem: the anti-linear channel has rank at most two

Identify the real six-space with `C^3`. Every `O in SO(6)` acts as a real-linear
isometry

\[
T(z)=Mz+N\bar z,\qquad M,N\in M_3(\mathbb C).
\tag{3}
\]

Orthogonality gives the standard Bogoliubov identities

\[
MM^*+NN^*=I,\qquad MN^T+NM^T=0.
\tag{4}
\]

### Theorem — `MOC4-BOGOLIUBOV-RANK2-PARITY-MASK-v1`

For every `O in SO(6)` in (3),

\[
\boxed{\det N=0,\qquad \operatorname{rank}N\le2,\qquad
\|N\|_F^2\le2.}
\tag{5}
\]

More generally, for every pair of even-parity bit vectors
`r,c in {0,1}^3`, one has

\[
\boxed{
\sum_{\alpha,\beta:\ r_\alpha\oplus c_\beta=0}q^-_{\alpha\beta}
+
\sum_{\alpha,\beta:\ r_\alpha\oplus c_\beta=1}q^+_{\alpha\beta}
\le2.}
\tag{PM}_{r,c}
\]

There are `4 x 4=16` such inequalities.

### Proof of the rank statement

First suppose `M` is invertible and write `Z=M^{-1}N`. The second identity in
(4) becomes

\[
M(Z^T+Z)M^T=0,
\]

so `Z^T=-Z`. A `3 x 3` skew-symmetric matrix has determinant zero because

\[
\det Z=\det Z^T=\det(-Z)=-\det Z.
\]

Hence `det N=det M det Z=0`.

The set on which `det M != 0` is dense in `SO(6)`: `det M` is a real-analytic
function on the connected real-analytic manifold `SO(6)` and is nonzero at the
identity. If it vanished on a nonempty open set, real-analytic continuation would
force it to vanish identically, contradicting its value at the identity. Since
`det N` is continuous, the identity `det N=0` extends from this dense set to all
of `SO(6)`.

Thus `rank N<=2`. From the first identity in (4),

\[
NN^*\preceq I,
\]

so every singular value of `N` is at most one. At most two are nonzero, hence

\[
\|N\|_F^2=\operatorname{tr}(NN^*)\le2.
\]

This proves (5).

### Proof of all sixteen parity masks

For `r in {0,1}^3`, let `C_r` conjugate exactly those complex coordinates with
`r_alpha=1`. As a real orthogonal map its determinant is `(-1)^{|r|}`.
Therefore even `r` gives `C_r in SO(6)`, and similarly for an even input mask
`c`.

Apply (5) to

\[
T_{r,c}=C_r\,T\,C_c\in SO(6).
\]

Conjugating exactly one side of a scalar real-linear block `z -> mz+n zbar`
interchanges the complex-linear and anti-linear channels (up to conjugation and
irrelevant phases); conjugating both or neither leaves their roles unchanged.
Consequently the anti-linear coefficient of `T_{r,c}` has squared Frobenius norm

\[
\|N_{r,c}\|_F^2=
\sum_{r_\alpha\oplus c_\beta=0}q^-_{\alpha\beta}
+\sum_{r_\alpha\oplus c_\beta=1}q^+_{\alpha\beta}.
\]

Equation (5) gives `(PM)_{r,c}`.

This is a true common-unitary constraint. It is not a positivity assumption and
does not introduce arbitrary bistochastic or independently chosen compound-minor
arrays.

## 3. Relation to the earlier odd-Weyl inequality

An odd signed matching has an odd number of minus channels and therefore an even
number of plus channels. Fix the matching permutation `rho`. Take `r=(0,0,0)`
and let `c_beta=1` exactly for those matched columns on which the selected channel
is plus. Since the number of plus choices is even, `c` has even parity.

The three selected matching masses are then a subset of the nine nonnegative
terms on the left of `(PM)_{r,c}`. Hence

\[
\sum_\alpha q^{\epsilon_\alpha}_{\alpha,\rho(\alpha)}\le2.
\tag{6}
\]

Thus the new parity-mask theorem strictly strengthens the linear consequence of
`MOC4-ODD-WEYL-ORIENTATION-v1`: it charges all nine cells selected by an
orientation gauge, not merely the three cells of one odd matching.

The earlier square-root overlap inequality remains additional nonlinear
information; no claim is made that `(PM)` characterizes the exterior-square
image.

## 4. Direct application to the assigned partner's counterexample

The partner fleet01/B08 r12 gives the exact rational orthogonal matrix

\[
U=\begin{pmatrix}
636/1105&-423/1105&-12/65&-772/1105\\
3576/5525&332/5525&-144/325&3411/5525\\
164/425&348/425&9/25&-96/425\\
27/85&-36/85&4/5&24/85
\end{pmatrix}.
\tag{7}
\]

The accompanying verifier in this run reconstructs `O=Lambda^2 U` in the same
oriented basis `(12,34 | 13,-24 | 14,23)`, computes `M,N` exactly, and obtains

\[
\det N=0,\qquad
\det M=\frac{404496}{1221025}.
\tag{8}
\]

All sixteen parity-mask inequalities hold. Their largest left side is

\[
\frac{60830802}{30525625}
=1.9927782641633054\ldots,
\tag{9}
\]

attained at `r=c=(0,1,1)`, with exact slack

\[
2-\frac{60830802}{30525625}
=\frac{220448}{30525625}>0.
\tag{10}
\]

The same datum nevertheless violates a facet of the 24-even-state polytope, as
proved by the partner. Therefore `(PM)` does **not** smuggle the refuted universal
positive lift back into the argument: the parity-mask relaxation is genuinely
larger than the 24-state convex hull while still containing this exact actual-unitary
point.

## 5. Exact structured payoff: the masks close the previous 48-state obstruction

The previous fleet04/B07 r13 report used the source-valid structured coefficient
pair

\[
K=\begin{pmatrix}
245983/5120000&5030591/5120000&-39077/1024000\\
-5113569/5120000&56671/5120000&19643/1024000\\
-8539/1024000&-35819/1024000&5009153/5120000
\end{pmatrix},
\tag{11}
\]

\[
X=\begin{pmatrix}
-3609633/1280000&111173/51200&2385071/1280000\\
-917133/1280000&1431961/1280000&525623/256000\\
-1352967/1280000&1061147/1280000&948017/1280000
\end{pmatrix}.
\tag{12}
\]

For the weights

\[
w^+_{\alpha\beta}=K_{\alpha\beta}+X_{\alpha\beta}/2,\qquad
w^-_{\alpha\beta}=-K_{\alpha\beta}+X_{\alpha\beta}/2,
\tag{13}
\]

row/column conservation alone permitted an odd signed matching with score

\[
20773731/5120000,
\]

while the true 24 even endpoints have maximum

\[
M_{\rm even}=13195057/5120000.
\tag{14}
\]

That was the exact obstruction which forced retention of orientation information.

Now maximize the same structured objective over the **larger outer relaxation**
defined only by:

1. `q^+,q^- >= 0`;
2. every row total and every column total of `q^++q^-` equals one;
3. all sixteen parity-mask inequalities `(PM)`.

Every true exterior-square point belongs to this relaxation. The following exact
dual certificate proves that its maximum is already exactly `(14)`.

Use arbitrary equality multipliers, in row-then-column order,

\[
y=\left(
\frac{254881}{1024000},
\frac{1268991}{5120000},
-\frac{871389}{5120000},
-\frac{720783}{640000},
\frac{670179}{2560000},
0
\right).
\tag{15}
\]

All parity-mask multipliers are zero except

\[
\lambda_{000,011}=\frac{2042727}{2560000},\qquad
\lambda_{011,011}=\frac{98951}{2560000},\qquad
\lambda_{110,101}=\frac{1845561}{2560000}.
\tag{16}
\]

These three multipliers are nonnegative. For each of the 18 variables
`q^+_{alpha beta},q^-_{alpha beta}`, the dual coefficient is at least the
corresponding structured weight in (13). In cell-by-cell `(+,-)` order the exact
coefficient slacks are

\[
\begin{split}
(&155089/320000,\ 2736967/1280000,\ 0,\ 130419/320000,\\
&245751/1280000,\ 0,\ 165529/320000,\ 0,\\
&1866333/1280000,\ 0,\ 0,\ 0,\ 0,\ 347/16000,\\
&326403/640000,\ 514151/1280000,\ 0,\ 152477/320000).
\end{split}
\tag{17}
\]

Thus every slack is nonnegative. The dual objective is

\[
\sum_i y_i+2\sum_{r,c}\lambda_{r,c}
=\boxed{\frac{13195057}{5120000}}
=M_{\rm even}.
\tag{18}
\]

The even endpoint attaining `(14)` is feasible for the relaxation, so primal and
dual values agree exactly. Therefore

\[
\boxed{
Q_{K,X}(O)\le \frac{13195057}{5120000}
}
\tag{19}
\]

for every actual `O in SO(6)` for this exact structured spectral support datum.

This is a genuine repair of the prior orientation-forgetting failure: the former
odd excess `3789337/2560000` is completely paid by three rank-two parity masks,
with an exact rational certificate and no tolerance.

It is **not** a proof of MOC4 for arbitrary spectra. The certificate is for one
source-valid structured coefficient pair that had previously defeated the
48-state relaxation.

## 6. Compact conditional end-to-end argument and first missing implication

The surviving representation-theoretic route is now:

1. Exact exterior-power expansion reduces every MOC4 support direction to the
   structured Bogoliubov objective (1) on one `SO(6)` exterior-square point.
2. The lead's zero-entry common lift and the partner's universal 24-even-state
   Bogoliubov lift are both false, so no unconditional positive representation is
   assumed.
3. `MOC4-BOGOLIUBOV-RANK2-PARITY-MASK-v1` supplies sixteen exact linear
   common-unitary inequalities for **every** actual exterior-square point.
4. On the exact structured datum which previously had a forbidden odd-Weyl
   advantage `1.480209765625`, those inequalities already recover the exact
   true-even endpoint maximum by the dual certificate (15)-(18).
5. To finish the representation route, it would suffice to prove the following
   universal structured-normal statement.

> **`MOC4-STRUCTURED-MASK-NORMAL-v1` — first essential missing implication.**  
> For every coefficient pair `(K,X)` arising from spectra `a,b` and a support
> direction `eta`, the maximum of (1) over the nonnegative row/column-conserving
> parity-mask relaxation is attained at one of the 24 even signed matching
> endpoints.

This implication is deliberately weaker than the refuted 24-state positive-lift
claim: it asks only that the **structured objective normal** have an even endpoint
maximizer. The partner's facet-violating actual unitary can lie outside the
24-state hull and still satisfy all masks; only the structured support maximum
matters.

If `MOC4-STRUCTURED-MASK-NORMAL-v1` is false, the next admissible mechanism is
maximizer-local rather than another positive lift: combine the parity masks with
the exact row/column pair-stationarity or Cartan-Hessian payment conditions to
exclude the fractional face exposed by the offending structured normal.

## 7. Boundary cases and non-claims

- Full MOC4 remains open. No target counterexample was found.
- Singular determinant points are not divided out anywhere in the rank-two theorem.
- Repeated spectra and proper common reducing-block faces remain governed by the
  team's existing boundary results; this run does not re-prove or weaken them.
- The theorem (5) is representation-theoretic and applies before any genericity
  assumption on spectra.
- The finite dual certificate establishes only the exact coefficient datum
  (11)-(12); it is not counted as universal closure.
- No benchmark gold, answer-bearing benchmark metadata, credentials, scheduler
  identifiers, machine paths, unrelated private material, email/Drive data, paid
  model/API/Codex call, remote workflow, permission bypass, or public posting was
  used.

## 8. Exact verification output

`verify_rank2_parity_masks.py` uses only Python standard-library exact rational
arithmetic. Its output is:

```text
detN = (Fraction(0, 1), Fraction(0, 1))
detM = (Fraction(404496, 1221025), Fraction(0, 1))
partner_max_parity_mask_sum = 60830802/30525625 1.9927782641633054 r= (0, 1, 1) c= (0, 1, 1)
partner_mask_slack_to_2 = 220448/30525625 0.007221735836694581
dual_bound = 13195057/5120000 2.5771595703125
even_endpoint_max = 13195057/5120000 2.5771595703125
dual_equals_even_max = True
min_dual_coefficient_slack = 0
PASS: rank-2 parity-mask theorem witness and exact structured dual certificate
```

The verifier checks exact orthogonality of the partner matrix, reconstructs the
exterior-square blocks, checks `det N=0`, evaluates all sixteen parity masks, enumerates
the 24 even endpoint scores, and verifies every coefficient inequality and the
objective equality in the dual certificate.
