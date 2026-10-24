# MOC4 account02/B07 — odd-overlap equality lift and singular-safe Hessian trace

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Run:** `20260922T023423Z-b07-b42a363e`  
**Campaign:** MOC4, complex-normal `4 x 4` Marcus–de Oliveira target  
**Worker:** account02/B07  
**Assignment:** support-functional and second-variation estimates, including singular determinant points by justified limits  
**Outcome:** `ESSENTIAL_STEP_APPLIED`. Full MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and completed inputs consumed

The target is

\[
\det(A+B)\in\operatorname{conv}\left\{\prod_{i=1}^4(a_i+b_{\sigma(i)}):\sigma\in S_4\right\}
\]

for every complex normal `4 x 4` pair, including repeated spectra and singular determinant points.

I read and use the newest complete campaign-lead report available in the archive:

- account03/B07, `MOC4-ZERO-ENTRY-COMMON-LIFT-v1`, report commit
  `457cce618ad2542b6590807b7e516eaf8b139585`, report blob
  `47f09f9f722aa8501330ca532a2ca261474c681c`. It refutes a positive
  common permutation lift even on a zero-entry true-unitary face, while retaining
  the exact zero-face factorization and the exact support-functional route.

The named partner result read in full is:

- account03/B08, `MOC4-GIVENS-FOREST-LIFT-v1`, archive commit
  `bc960571ce90ce963eaf88cab8a8852f8dfbd06f`, report blob
  `885e95c15d6f82987a4cdc714613e3516b59898f`. It proves an honest
  nonnegative permutation lift for every one-use forest Givens word and therefore
  supplies a source-valid model for how a structured true-unitary family can be
  closed by explicit positive endpoint weights.

The decisive other-account input applied directly is:

- account04/B07, `MOC4-ODD-WEYL-ORIENTATION-v1`, archive commit
  `89fe5ebe78b671f1a7f46624ebcd385ceea91ddd`. In exterior-square
  coordinates it writes `O=Lambda^2 U in SO(6)` in `3 x 3` blocks
  `B_{alpha beta}` of size `2 x 2`. Writing each block as
  `z -> m z + n zbar`, set
  `q^+_{alpha beta}=|m|^2` and `q^-_{alpha beta}=|n|^2`. The exact support
  objective is
\[
Q_{K,X}(O)=\sum_{\alpha,\beta}
  (K_{\alpha\beta}+X_{\alpha\beta}/2)q^+_{\alpha\beta}
 +(-K_{\alpha\beta}+X_{\alpha\beta}/2)q^-_{\alpha\beta}.
\tag{1}
\]
  It proves that for every odd coloured matching `J=(rho,epsilon)`,
\[
\sum_{\alpha=1}^3\sqrt{q^{\epsilon_\alpha}_{\alpha,\rho(\alpha)}}\le2.
\tag{2}
\]
  The 24 even coloured matchings are exactly the `S_4` endpoint `q`-data;
  the 24 odd ones are forbidden orientation-reversing `O(6)` endpoints.

I also retain account01/B07's exact mixed-support reduction and its generic
structured witness (`MOC4-MIXED-ASSIGNMENT-v1` and the later exact
`MOC4-SUPPORT-GAP-RESCUE-v1` formulation). No arbitrary bistochastic array is
substituted for true-unitary data below.

## 2. New theorem: equality in an odd overlap inequality is automatically safe

### Theorem — `MOC4-ODD-OVERLAP-EQUALITY-LIFT-v1`

Let `O in SO(6)` be an actual exterior-square point, partitioned into the three
complementary-pair planes as above. Fix any odd coloured matching
`J=(rho,epsilon)` and choose the three local `O(2)` block phases exactly as in
the proof of (2), so that

\[
\operatorname{tr}(J^T O)
 =2\sum_\alpha\sqrt{q^{\epsilon_\alpha}_{\alpha,\rho(\alpha)}}.
\tag{3}
\]

If equality holds in (2), then the complete `q`-array of `O` is a convex
combination of at most nine even coloured matching arrays. Consequently, for
**every** real coefficient pair `(K,X)`, structured or not,

\[
Q_{K,X}(O)\le
\max_{\text{24 even coloured matchings}}Q_{K,X}.
\tag{4}
\]

In particular, equality in any odd-overlap inequality can never be the source
of an MOC4 support violation.

### Proof

Put `R=J^T O`. Since `J` is orientation reversing and `O in SO(6)`,
`R in O(6)` has determinant `-1`. Equality in (2) and (3) gives
`tr R=4`. An orientation-reversing `6 x 6` orthogonal matrix has trace at
most four. Equality forces exactly one eigenvalue `-1` and five eigenvalues
`+1`; hence

\[
R=I-2vv^T
\tag{5}
\]

for a real unit vector `v`.

After reordering the three pair planes according to `rho`, write
`v=(v_1,v_2,v_3)` with `v_i in R^2` and

\[
t_i=\|v_i\|^2,\qquad t_i\ge0,\qquad t_1+t_2+t_3=1.
\tag{6}
\]

For the reflection (5), the diagonal block is
`I_2-2v_i v_i^T`, while the off-diagonal block is `-2v_i v_j^T`.
Using
`q^\pm=(r\pm d)/2`,
`r=(1/2)||B||_F^2`, and `d=det B`, one gets exactly

\[
q^+_{ii}=(1-t_i)^2,\qquad
q^-_{ii}=t_i^2,
\tag{7}
\]
and, for `i != j`,
\[
q^+_{ij}=q^-_{ij}=t_i t_j.
\tag{8}
\]

Now define nine orientation-reversing block-monomial coloured matchings
`E_{ij}`.

- `E_{ii}` is the identity block permutation, with the `i`th selected block
  coloured minus and the other two plus.
- For `i != j`, `E_{ij}` uses the transposition `(ij)`; the edge
  `i -> j` is plus, the edge `j -> i` is minus, and the fixed edge is plus.

Every `E_{ij}` has odd minus parity. Give it weight `t_i t_j`. These nine
weights are nonnegative and sum to one. Their channel marginals reproduce
(7)-(8) exactly:

- diagonal minus channel `i` receives only `t_i^2`;
- diagonal plus channel `i` receives
  `sum_{r,s != i}t_r t_s=(1-t_i)^2`;
- each off-diagonal channel `i -> j` receives `t_i t_j` once in each colour.

Therefore

\[
q(R)=\sum_{i,j=1}^3 t_i t_j\,q(E_{ij}).
\tag{9}
\]

Left multiplication by the fixed block-monomial `J` only permutes block
locations and, on orientation-reversing row blocks, swaps the `+/-` channels.
Thus it acts linearly as a permutation on `q`-arrays. Hence

\[
q(O)=\sum_{i,j}t_i t_j\,q(JE_{ij}).
\tag{10}
\]

Both `J` and `E_{ij}` have determinant `-1`, so `JE_{ij}` has determinant
`+1`. Its `q`-array is therefore one of the 24 even coloured matching arrays,
which are exactly the `S_4` endpoint `q`-data. Equation (4) follows by
linearity of (1). QED.

This is an explicit positive endpoint lift on a true-unitary boundary locus,
in the same spirit as the named partner's `MOC4-GIVENS-FOREST-LIFT-v1`, but it
covers a different family: the complete equality locus of every odd-Weyl
overlap constraint, independent of whether the original unitary admits a
forest-Givens factorization.

## 3. Quantitative collar away from every forbidden odd endpoint

The equality theorem has an exact stability strengthening.

For a fixed odd matching with the phase-optimized `J`, define

\[
\delta_J
 =2-\sum_\alpha\sqrt{q^{\epsilon_\alpha}_{\alpha,\rho(\alpha)}}\ge0.
\tag{11}
\]

Again put `R=J^T O`. Equation (3) gives
`tr R=4-2 delta_J`. Since `det R=-1`, choose a unit `-1` eigenvector `u`
and let the reflection `H=I-2uu^T`. Then

\[
\begin{aligned}
\|R-H\|_F^2
 &=12-2\operatorname{tr}(R^T H)\\
 &=12-2(\operatorname{tr}R+2)
 =4\delta_J.
\end{aligned}
\tag{12}
\]

Thus the equality point `O_J=JH` satisfies

\[
\|O-O_J\|_F=2\sqrt{\delta_J}.
\tag{13}
\]

Let

\[
W=\max_{\alpha,\beta}
 \max\{|K_{\alpha\beta}+X_{\alpha\beta}/2|,
       |-K_{\alpha\beta}+X_{\alpha\beta}/2|\}.
\tag{14}
\]

Because (1) is one half of a blockwise quadratic form whose operator norm is
`W`, and every orthogonal `6 x 6` matrix has Frobenius norm `sqrt(6)`,

\[
|Q_{K,X}(O)-Q_{K,X}(O_J)|
 \le 2W\sqrt{6\delta_J}.
\tag{15}
\]

The equality theorem gives `Q(O_J)<=M_even`, so

\[
\boxed{Q_{K,X}(O)\le M_{\rm even}+2W\sqrt{6\delta_J}.}
\tag{16}
\]

Therefore if an actual unitary had a positive support violation
`gamma=Q(O)-M_even>0`, then for **every** odd matching

\[
\boxed{\delta_J\ge\frac{\gamma^2}{24W^2}}
\tag{17}
\]

when `W>0`. A target-level violator is thus uniformly separated from all 24
forbidden odd-Weyl faces. This removes the tight-orientation boundary from the
counterexample search; only a genuinely strict interior can remain.

## 4. New singular-safe second-variation class identity

The previous B07 run proved, by an adjugate formula with no inverse, that at a
local support maximizer every true `U(2)` row/column pair orbit is a top
Rayleigh point even when the determinant base matrix is singular. The six
pair Hessians have a useful exact central sum.

Write the nonconstant support as

\[
s(U)=k+x,\qquad
k=\langle D,K\rangle,\quad
x=\tfrac12\langle R,X\rangle,\quad
c=\tfrac16\langle {\bf 1}_{3\times3},X\rangle.
\tag{18}
\]

Let the six transpositions of `S_4` act on the `b` labels. In the
three-dimensional standard signed representation,
the transposition class sum is `2I_3`. In the three complementary-pair
permutation representation it is `2J_3`. Since `R` is doubly stochastic,

\[
\sum_{\tau\ {\rm transposition}}s(UP_\tau)=2k+6c.
\tag{19}
\]

At a pair-stationary point the two real tangent directions for a given pair
have equal Rayleigh curvature; their sum is
`4(s(UP_tau)-s(U))`. Summing all six pair planes gives the exact column-pair
Hessian trace

\[
\boxed{\operatorname{Tr}H_{\rm pair}
 =-16k-24(x-c)
 =-8\{2k+3(x-c)\}.}
\tag{20}
\]

The same identity holds for the six row-pair planes. Thus every local support
maximizer, including a singular determinant point, necessarily obeys

\[
\boxed{2k+3(x-c)\ge0.}
\tag{21}
\]

For a global maximizer, averaging over the three double transpositions also
gives `k>=0`. These are necessary support-functional constraints on an actual
unitary maximizer, not a convex relaxation.

## 5. Compact conditional end-to-end chain and first remaining implication

Assume MOC4 fails. Strict separation gives spectra, a support direction and a
global true-unitary maximizer with positive gap `gamma`. The inherited
adjugate pair formula is valid without an inverse; if needed, repeated spectra
and singular determinant values can be reached by perturbing the spectra (or
`A` by a scalar parameter) while preserving a strict support gap, and then
passing to a limit.

At such a maximizer:

1. all twelve genuine row/column two-plane Rayleigh conditions hold;
2. the Hessian constraint (21) holds and, globally, `k>=0`;
3. by (17), every odd-Weyl overlap inequality is quantitatively strict;
4. if a pair orbit is flat, the inherited pair-flat boundary reduction moves
   the same support value to a zero-entry representative, where the lead's
   `MOC4-ZERO-FACE-SUPPORT-v1` remains the separate boundary obligation.

Consequently the first essential interior implication can now be stated
without the already-refuted positive-lift, parity-roof, or orientation-forgetting
relaxations:

> **`MOC4-STRICT-ORIENTATION-BIRAYLEIGH-v1`.**  
> For every structured support pair `(K,X)` arising from complex spectra and a
> support direction, prove that an actual `O=Lambda^2 U in SO(6)` which comes
> from a row-and-column bi-Rayleigh local maximizer, satisfies
> `k>=0`, `2k+3(x-c)>=0`, and is strict in all odd-overlap inequalities, must
> obey `Q_{K,X}(O)<=M_even`.

A proof of this interior statement together with the lead's zero-face support
lemma closes the generic support problem; the existing strict-separation and
continuity argument then returns the repeated-spectrum and singular cases.
The present run proves the complete odd-overlap equality branch and its
quantitative exclusion from any violator, but does not prove the strict
interior implication.

## 6. Exact verification

`verify_odd_overlap_equality.py` uses only `fractions.Fraction`. It verifies
symbolically, coefficient by coefficient, the nine-atom decomposition (9) for
all 18 coloured channels; checks a rational sample
`t=(2/11,3/11,6/11)` with weight sum one; verifies an arbitrary rational
support objective agrees with the nine-atom mixture; and independently checks
the exact stability identity (12) on a rational orthogonal example.

Verifier blob: `1680833c27950ac9536f1cbd152a7ff1c6479de3`.  
Verification-output blob: `4e49e85c5185e811fce2ed362e6a488ef8978b90`.

Exact output:

```text
PASS MOC4-ODD-OVERLAP-EQUALITY-LIFT-v1 exact certificate
odd_atoms = 9
sample_t = ['2/11', '3/11', '6/11']
sample_weight_sum = 1
sample_support_objective = 1150/693
sample_mixture_objective = 1150/693
stability_trace = 16/5
stability_delta = 2/5
stability_distance_squared = 8/5
stability_4delta = 8/5
```

## 7. Failure accounting and non-claims

- `MOC4-ODD-OVERLAP-EQUALITY-LIFT-v1`: **PROVED** as a support theorem on
  the equality locus of every odd overlap inequality.
- `MOC4-ODD-OVERLAP-COLLAR-v1`: **PROVED** in the quantitative form (16)-(17).
- `MOC4-PAIR-HESSIAN-TRACE-v1`: **PROVED** from the inherited singular-safe
  pair-Rayleigh formula and exact `S_4` class sums.
- `MOC4-STRICT-ORIENTATION-BIRAYLEIGH-v1`: **OPEN**.
- Parent MOC4: **OPEN**.
- No arbitrary bistochastic surrogate, Hermitian-only reduction, lost complex
  phase, benchmark material, credential, scheduler-internal identifier, machine
  path, email/Drive data, paid model/API, Codex, remote workflow, or public
  release is used.
