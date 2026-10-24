# B14 — a non-read-once near-record for the existential restriction ratio

**Status:** PARTIAL / exact construction plus finite search. **Full uniform-cube FEI remains OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; no authenticated brain retrieval or receiver-context use occurred.  
**Live role:** FEI erasure and selector proof.  
**Current sprint subassignment:** account02/B14, search new non-read-once Boolean constructions maximizing the existential restriction ratio.  
**Fresh mathematical source before this search:** `master` at `6af28cd57436c16a5bb4d13219a5352118111c81`.  
**Publication priority:** UNVERIFIED; no novelty claim is made.

This run followed FLEET_RULES creative moves **#2 (attack the negation / hunt a counterexample), #15 (break symmetry on purpose), and #16 (compute a finite structured family exactly enough to expose the next obstruction)**. It does not rerun the settled read-once certificate and does not substitute a large value at one coordinate for the required existential minimum.

## 1. Quantity and baseline

For a nonconstant Boolean function `f`, define the potential-free existential restriction ratio

\[
\rho_0(f):=\min_{i:\operatorname{Inf}_i(f)>0}
\frac{\Delta_i H(f)}{\operatorname{Inf}_i(f)},
\qquad
\Delta_iH:=H(f)-\frac{H(f_{i,+})+H(f_{i,-})}{2}.
\]

A uniform upper bound on `rho_0` would imply FEI by physical-restriction induction. The current structured benchmark in this route is width-two tribes with eight disjoint tribes on 16 variables. Its exact-Walsh/high-precision value in the verifier delivered here is

\[
\rho_0=6.00374605655908825141422865358\ldots,
\]

with every coordinate equivalent and

\[
\operatorname{Inf}_i=\frac{2187}{32768}.
\]

This number is a tested-family benchmark, not a proved universal supremum.

## 2. Exact non-read-once construction

Group the 16 input bits into eight ordered pairs. Let

\[
f_0(x)=
\begin{cases}
+1,&\text{if no pair equals }11,\\
-1,&\text{otherwise.}
\end{cases}
\]

Thus `f_0` is width-two tribes up to the output convention. Define `f_*` by changing exactly one truth-table value:

\[
f_*(x)=f_0(x)\quad(x\ne 1^{16}),
\qquad
f_*(1^{16})=+1.
\tag{1}
\]

The positive set therefore has `3^8+1=6562` inputs.

### Proposition 2.1 — `f_*` is not read-once AND/OR/NOT

Every read-once formula over AND, OR, NOT is unate: after fixing one polarity for each input, it is monotone in every coordinate. Function (1) is not unate.

Fix a coordinate `x_1` and let `x_2` be its mate.

* If `x_2=1` and every other pair is `00`, changing `x_1:0->1` changes `f_*:+1->-1`.
* If `x_2=1` and all other fourteen bits are `1`, changing `x_1:0->1` changes `f_*:-1->+1`, because the endpoint is precisely the flipped all-ones input.

Thus the same coordinate has derivatives of both signs. No literal polarity can make it monotone. Hence `f_*` is not unate and therefore is not a read-once AND/OR/NOT formula. QED.

This is a genuine non-read-once construction, not a relabelled disjoint formula.

## 3. Exact Walsh data and the restriction ratio

The delivered verifier constructs the 65,536 Boolean values, computes the integer Walsh transform

\[
A_S=\sum_x f_*(x)(-1)^{S\cdot x},\qquad
\widehat f_*(S)=A_S/2^{16},
\]

and checks Parseval exactly:

\[
\sum_S A_S^2=2^{32}.
\]

All 16 coordinate fibre multisets are exactly identical. Every coordinate has the exact dyadic influence

\[
\boxed{\operatorname{Inf}_i(f_*)=\frac{547}{8192}=0.0667724609375.}
\tag{2}
\]

There are only 14 nonzero squared-Walsh fibre types for a representative coordinate; the full exact integer table and multiplicities are in `verification.json`.

Using the exact integer masses and evaluating only the logarithmic/square-root entropy expressions at 80 and 110 Decimal digits, with agreement through the printed precision, gives

\[
\frac{B_i}{\operatorname{Inf}_i}
=3.60511665813110646622505586666\ldots,
\]

\[
\frac{JS_i}{\operatorname{Inf}_i}
=2.39664657029542465902738231197\ldots,
\]

and therefore

\[
\boxed{
\rho_0(f_*)
=6.00176322842653112525243817864\ldots .
}
\tag{3}
\]

The global FEI ratio is separately

\[
\frac{H(f_*)}{I(f_*)}
=4.32872278023717051354145850631\ldots,
\qquad
I(f_*)=1.068359375.
\tag{4}
\]

These are high-precision transcendental evaluations, **not directed-rounding enclosures**. No strict numerical improvement is claimed, so the sprint's strict-improvement enclosure requirement is not invoked. The dyadic Walsh/influence claims and the equality of all coordinate fibre multisets are exact integer statements.

The new witness misses the width-two-tribes benchmark by only

\[
6.00374605655908825141422865358\ldots
-
6.00176322842653112525243817864\ldots
=
0.00198282813255712616179047494\ldots .
\tag{5}
\]

Thus the high potential-free restriction ratio is not confined to the read-once class: a one-point non-unate defect retains it to within two thousandths.

## 4. Symmetry-orbit attack around the record

To test whether a sparse defect can actually beat the disjoint-tribes benchmark, classify inputs by

\[
(a,b,c)=(\#00\text{ pairs},\#\text{single-1 pairs},\#11\text{ pairs}),
\qquad a+b+c=8.
\]

There are exactly 45 such orbits under pair permutations and within-pair swaps. Toggling any union of these orbits preserves transitivity on the 16 physical coordinates, so `rho_0` is the ratio at one coordinate.

The delivered search computes every orbit's Walsh perturbation with exact `int64` arithmetic and evaluates all choices of up to three distinct whole orbits. The entropy ranking in this search is float64 exploratory arithmetic; selected witness (1) is independently re-evaluated by the high-precision verifier.

Results:

| toggled orbits | cases checked | best `rho_0` | best orbit(s) |
|---|---:|---:|---|
| none | 1 | `6.0037460565590886` | baseline |
| one | 45 | `6.001763228426529` | `(0,0,8)` = all-ones point |
| two | 990 | `5.9934041329589824` | `(0,0,8)` and `(8,0,0)` |
| three | 14,190 | `5.97879332288853` | `(0,0,8)`, `(7,0,1)`, `(8,0,0)` |

So this entire symmetry-preserving Hamming neighbourhood, through three orbit toggles, fails to improve the known structured benchmark. This is a finite negative result only; it does not prove an upper bound for `rho_0`.

## 5. Scientific implication toward the universal target

The result changes the shape of the selector problem in two useful ways.

First, an attempted proof that a ratio near `6.00` forces an exact read-once/disjoint-tribes representation is too rigid: (1) is genuinely non-read-once but almost preserves the ratio. Any structural argument must be **quantitatively stable under sparse Boolean defects**, not merely classify exact equality cases.

Second, the most obvious symmetric sparse-defect route does not generate a larger existential obstruction. Single-, double-, and triple-orbit perturbations all move the minimum downward. The next construction search should therefore break the pair-orbit symmetry while keeping **all** coordinate ratios high, or use a shared-variable composition whose selector/control coordinates do not become the bottleneck.

This is compatible with the recovered exact scalar-frontier work: the relevant universal question is an existential coordinate, not an every-coordinate upper payment. It also preserves the known width-two-tribes counterexample to the older stronger fixed erasure target; no false every-coordinate payment is reintroduced here.

## 6. Failed routes preserved

During the same construction attack I also tested overlapping cyclic tribes, MUX/shared-residual combinations, repeated small gadgets, and linear mixing of the disjoint tribes. None produced a reproducible value above the disjoint width-two-tribes benchmark; selector/control coordinates or cross-pair mixing became the bottleneck. Those exploratory families are not used as the finite theorem in Section 4. The exact reproducible negative search delivered here is the 45-orbit search.

The current primary-literature check found González--MacManus--Pereyra (arXiv:2606.00246, 29 May 2026), whose stopping-tree framework directly emphasizes suitable restriction-decrement coordinates; Potapov (arXiv:2609.21563, 18 September 2026), proving FEI for plateaued functions with sharp class constant 4 and for partially bent functions with sharp 2; and Li--Han (arXiv:2512.03117), giving a strengthened influence-profile entropy bound but not full FEI. I found no source establishing that the top-flip construction above is extremal or novel. **Priority remains UNVERIFIED.**

## 7. Before / after / remaining obligation

**Before:** the strongest local obstruction in this concrete search was the read-once width-two-tribes value `6.003746056559088...`; it was unclear how robust that value is outside the read-once class.

**After:** the exact non-unate top-flip witness (1) has `rho_0=6.001763228426531...`, only `0.001982828132557...` lower, while an exhaustive symmetry-orbit toggle search through three orbits finds no improvement over the baseline.

**Universal obligation remaining:** prove a dimension-independent upper bound on `rho_0`, or produce a Boolean family with unbounded `rho_0`. More locally, decide whether a genuinely shared-variable/non-read-once construction can exceed `6.003746...` while keeping every relevant coordinate above that threshold. Full FEI remains OPEN.

## 8. Reproducibility

Delivered beside this report:

* `verify_top_flip_witness.py` — exact integer Walsh/influence/fibre verification plus 80/110-digit Decimal entropy stability; SHA-256 `125b616ac97c6b228b68f0e576514cc07324cef67d9efbb3743d9769091ae78a`.
* `verification.json` — actual verifier output; SHA-256 `c09e7293fc1c0bd77187fb7cfd06f06f4dd4d98ee5e1cf673e74c41abb371ebf`.
* `scan_symmetric_orbit_toggles.py` — exact-Walsh / exploratory-float64 45-orbit scan through triples; SHA-256 `79661b5a8273b6bb591c9d002c0b1b137cf1e21a102b284aa5f422661395302d`.
* `orbit_scan.json` — actual orbit-scan output; SHA-256 `8a863e5209698793b63f13105894685a6d1d8a7c618dc22fe751f73d93a38967`.

No finite computation in this report is promoted to a universal FEI theorem.
