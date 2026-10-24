# B14 — the arity-10 gate obstruction is balance-primitive under physical coordinate restriction

**Outcome:** `ESSENTIAL_STEP_APPLIED / STRUCTURAL_SHARPENING_OF_THE_FALSIFIER`.  Full uniform-cube FEI remains **OPEN / NOT PROVED**.

**Execution:** `WITHOUT_VERIFIED_BRAIN`.  The native runtime had Python, but no importable `math_brain` and no `lean`, `lake`, or `elan`; no brain-assisted or formal-kernel claim is made.

## 1. Live target and source change

Current brain control revision `2026-09-22.2` supersedes this slot's older posterior-crossing wording.  The later OWNER MESSAGE directs every FEI worker to converge on the all-gate reformulation and do one of two things: prove decomposable/AND extremality for the current read-once potential, or falsify it with a gate whose correction margin is larger.

That falsification has now occurred in the shared scientific state.  I therefore did not spend this invocation extending the superseded posterior-crossing branch.

The gate reformulation uses

\[
 c_G(p)=\frac{-D_G(p)}{I(G;p)/4-p_{out}(1-p_{out})}.
\]

At uniform input biases, for a balanced gate and `C0=Gamma(1/2)=6.4548`, the exact identity from account01/B14 is

\[
\boxed{c_G(1/2,\ldots,1/2)
=4\left(\frac{H(G)}{I(G)-1}-C_0\right).}
\tag{1}
\]

Account03/B12 then produced an explicit genuine balanced monotone **10-input** restriction of the Numaro seed with

\[
I(G)=\frac{257}{128},\qquad
6.509836127588151479<H(G)<6.509836127588151480,
\]

hence

\[
\frac{H(G)}{I(G)-1}>6.459372281637855731,
\qquad
c_G>0.018289126551422926.
\tag{2}
\]

The same read-once certificate verifies the complete AND family with quadratic margin `c=0.01`, so (2) is already a rigorous genuine-gate refutation of AND/decomposable extremality.  The witness truth-table SHA-256 is

`3168d8fb8ac9f5d6d7dca1d79146392aecb5eb55cc76ccb028395a9e6a62bfb4`.

The remaining useful question on this exact falsifier is whether it is merely a padded version of a smaller balanced obstruction obtainable by ordinary physical restriction.  This run answers that question exactly.

## 2. New finite theorem

### Theorem — balanced physical restrictions of the 10-input witness

Let `G` be the explicit 10-input gate above.  Consider every proper coordinate subcube restriction of `G`; equivalently, independently mark each of its ten coordinates as free, fixed to zero, or fixed to one, excluding the all-free state.

There are `3^10-1 = 59048` such restrictions.  Exactly `9514` are balanced.  Their counts by the number of still-free coordinates are

\[
\begin{array}{c|rrrrrrr}
d&1&2&3&4&5&6&7\\\hline
\#&1028&2882&3112&1788&512&152&40.
\end{array}
\tag{3}
\]

There are **no balanced restrictions with 8 or 9 free coordinates**.  Thus the arity-10 witness cannot be made into a balanced arity-9 or arity-8 gate by fixing only one or two physical coordinates.

Among the `9514` balanced restrictions, exactly `460` have total influence `I>1`.  Every one of these has effective arity only **4 or 6** after deleting zero-influence free coordinates.  More precisely, `(free arity,effective arity)` occurs with counts

\[
(4,4):184,\quad (5,4):120,\quad (6,4):16,
\quad (6,6):100,\quad (7,6):40.
\tag{4}
\]

The other balanced restrictions have `I=1`; for a balanced monotone Boolean function equality in the cube edge-isoperimetric/Poincare bound is the character case, so they are harmless terminal dictators with possible dummies.

For all `460` non-character cases, the exact pair `(I, |W|\text{-histogram})` belongs to only seven types.  The largest amplified ratio is

\[
\boxed{
\max_{\substack{G'\text{ proper balanced}\\\text{restriction of }G\\I(G')>1}}
\frac{H(G')}{I(G')-1}
=
\frac{46}{5}-\frac95\log_2 3
=6.347067498701918873\ldots .}
\tag{5}
\]

It occurs on an effective six-variable gate with

\[
I=\frac{13}{8},\qquad
|W|:\quad 4^{\times32},8^{\times4},16^{\times4},24^{\times4},
\]

up to the trivial Walsh scaling caused by one dummy free coordinate.

In particular, the exact integer inequality

\[
3^9>2^{14}
\]

implies `log_2 3>14/9`, hence the right side of (5) is strictly below `6.4`.  Therefore every proper balanced restriction with `I>1` obeys

\[
\boxed{c_{G'}<4(6.4-6.4548)=-0.2192.}
\tag{6}
\]

So the original arity-10 witness has positive margin `>0.0182891`, while **every proper balanced physical restriction has strictly negative margin**, with a gap exceeding `0.2374` in the margin units that decide the gate programme.

This is stronger than merely saying no one-coordinate restriction works: balance itself disappears after one or two fixes, and whenever balance eventually returns the obstruction has collapsed to an effective 4- or 6-variable gate far inside the safe region.

## 3. Exact certificate

`check_b14_gate10_restrictions.py` reconstructs the source-exact 18-variable seed, reconstructs the 10-variable witness and verifies its inherited SHA-256, then exhausts all `59048` proper ternary coordinate states.

No floating-point inequality is needed for the theorem.  The seven exact Walsh/influence types reduce to three entropy forms:

* `I=3/2, H=3`, giving ratio `6`;
* `I=13/8, H=23/4-(9/8)log_2 3`, giving (5);
* `I=13/8, H=11/2-(27/64)log_2 3-(25/64)log_2 5`.

The checker certifies the second nontrivial entropy is below `4` by the integer comparison

\[
3^{27}5^{25}>2^{96},
\]

and certifies that (5) is the larger of the two by

\[
2^{16}5^{25}>3^{45}.
\]

Executed checker SHA-256:

`23b5a94ebe16cf486281cb64b66db83d17e6560d5d273c245c19428c0f09f2d7`

Captured output SHA-256:

`ca4dd0de21c9993dd2c567512db825ac690ad252ad783bbdf60acfd69e69a1`

## 4. Source-to-next-arrow use

The source gate programme's first proposed universal implication — AND/decomposable extremality for the current read-once potential — is **refuted**, not merely unproved.  Equation (1) shows why: on the balanced-uniform slice, the margin already contains the amplified full-FEI quantity `H/(I-1)`.  The explicit arity-10 gate in (2) is the smallest currently source-certified genuine obstruction I consumed in this run.

The new theorem rules out the most obvious repair: one cannot physically restrict that gate to a smaller balanced witness while retaining the positive margin.  Its positive gate defect is genuinely collective across all ten active coordinates in the sense of ordinary coordinate restriction.

Thus the next bounded-arity falsifier question is not "which coordinate of the known witness should be fixed?".  A smaller witness, if one exists, must be a different gate or must use a genuinely nonuniform bias vector rather than a balanced coordinate descendant of this gate.  Conversely, any replacement universal potential must survive the balanced-uniform identity (1), so changing only the off-centre shape of the old read-once potential cannot repair this particular balanced obstruction.

This does **not** prove FEI, does not give a new FEI constant, and does not weaken the known addressing/per-coordinate-erasure obstructions.  No prescribed-coordinate payment is asserted.
