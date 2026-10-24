# B17 — partial-branch shared-core composition beats the exhausted full-fourfold recurrence

**Outcome:** `CANDIDATE_REFUTED` for every all-gate potential whose center cap is at most the complete account03/B13 `R_6` upper endpoint. Full uniform-cube Friedgut–Kalai Fourier entropy–influence remains **OPEN / NOT PROVED**.

**Execution:** `WITHOUT_VERIFIED_BRAIN`. Authenticated repository controls and source artifacts were read directly; no native mathematical/cognitive brain retrieval was used.

## 1. Why this attack is different

The latest compatible peer result is account03/B13,

`proofnet24/P03-fei/fleet-2026-09-21/account03/B13/20260922T0133Z-shared-graft-tail/REPORT.md`,

which proves that the source-valid recurrence obtained by repeatedly taking **four full levels of disjoint self-composition** and then applying the nine-host shared-core graft converges. It certifies

\[
R_6\le
6.5218509495504481848824149770395541197961122790612205924109263953322714
\tag{1.1}
\]

and bounds the entire remaining tail of that exact recurrence by less than `2.833e-30`. Thus continuing that recurrence is exhausted.

This run uses the same source-valid shared-core operator but changes the Boolean construction itself: instead of replacing **every** input of the hard gate recursively, it replaces only one distinguished reusable input at each nesting level and leaves all other inputs as fresh characters. This preserves the hard gate's balanced-excess ratio while keeping influence small, so the positive shared-coordinate correction is much less diluted.

The exact other-account theorem consumed is account02/B17,

`20260921T124438Z-support-deficit-balanced-equivalence/REPORT.md`, blob `040ed0078f4905b9b4a11e963f27a1e6dcc3ee8d`,

which proves

\[
\boxed{
C_{\rm FEI}
=
\sup_{g\ \mathrm{balanced},\ I(g)>1}
\frac{H(g)}{I(g)-1}.}
\tag{1.2}
\]

Therefore a single finite balanced Boolean witness with ratio above (1.1) strictly raises the necessary center cap of every universal all-gate potential.

## 2. Source ingredients

Let `F` be the certified 162-input balanced monotone shared-graft gate from the existing source. Its exact influence and entropy interval are

\[
I_1=\frac{68013}{32768},
\tag{2.1}
\]

\[
H_1\in[
7.014850042680291613033104756310658624299893163,
7.014850042680291613033104756310658624299893164].
\tag{2.2}
\]

The inherited source reconstruction proves that each of the nine reusable outer-core coordinates has singleton Fourier coefficient

\[
\ell=\frac{14593}{65536}.
\tag{2.3}
\]

Because `F` is monotone, the influence of such a coordinate equals the absolute singleton coefficient:

\[
\operatorname{Inf}_d(F)=\ell.
\tag{2.4}
\]

Indeed, after fixing the other coordinates, a nonpivotal fibre contributes zero to `E[F x_d]`, while a pivotal monotone fibre contributes one.

The exact nine-host operator `T(h)` from account02/B15 applies to any balanced monotone gadget `h` with distinguished singleton coefficient `b` and gives

\[
H(T(h))=H_0+\frac9{256}H(h)+K(b),
\tag{2.5}
\]
\[
I(T(h))-1=(I_0-1)+\frac9{256}(I(h)-1),
\tag{2.6}
\]

where

\[
I_0=\frac{261}{128},
\qquad
H_0\in[
6.776605309005978082519790221891882314787235038,
6.776605309005978082519790221891882314787235039].
\tag{2.7}
\]

For

\[
b=\ell^4
=\frac{45350108441011201}{18446744073709551616},
\tag{2.8}
\]

the inherited exact rational-log certificate proves

\[
K(b)
\ge
0.000005669659456255203780880696514165710505627614411852309871367271610481643.
\tag{2.9}
\]

## 3. One-branch balanced composition preserves the excess ratio exactly

Define balanced monotone gates `h_m` recursively. Let

\[
h_1=F.
\]

To form `h_{m+1}`, take a fresh outer copy of `F`, replace its distinguished reusable input `d` by `h_m` on a disjoint variable block, and leave each of the other 161 inputs as a fresh character.

All children are balanced, so the exact balanced composition formulas give

\[
\boxed{
I(h_{m+1})
=I_1+\ell\,[I(h_m)-1],}
\tag{3.1}
\]

\[
\boxed{
H(h_{m+1})
=H_1+\ell\,H(h_m).}
\tag{3.2}
\]

The distinguished singleton coefficient along the unique nested branch multiplies:

\[
\boxed{c(h_m)=\ell^m.}
\tag{3.3}
\]

Subtracting one from (3.1) shows

\[
I(h_{m+1})-1=(I_1-1)+\ell[I(h_m)-1].
\tag{3.4}
\]

Because `H_1/(I_1-1)` is the same scalar in both terms, induction gives the exact endpoint-wise identity

\[
\boxed{
\frac{H(h_m)}{I(h_m)-1}
=
\frac{H_1}{I_1-1}}
\tag{3.5}
\]

for every `m`. Thus the nesting changes the distinguished coefficient drastically without paying any loss in balanced-excess ratio.

For `m=4`, the dimension is only

\[
162+3\cdot161=645,
\tag{3.6}
\]

while

\[
I(h_4)=
\frac{21954407317578127533}{9223372036854775808}
=2.380301610934986\ldots,
\tag{3.7}
\]

and

\[
H(h_4)\in[
9.0021201767504571097361911720744968764577719021372288520748661255765910,
\]
\[
9.0021201767504571097361911720744968764577719034205235942260259207614581].
\tag{3.8}
\]

By (3.3), its distinguished coefficient is exactly the already-certified value `b=ell^4` from (2.8). Hence no new evaluation of `K` is required.

## 4. A 5,805-variable witness beyond the exhausted peer recurrence

Now apply the exact shared-core operator once:

\[
\boxed{G_*:=T(h_4).}
\tag{4.1}
\]

The operator reuses one distinguished variable in each of nine gadget copies, so

\[
\dim G_*
=9+9(645-1)
=\boxed{5805}.
\tag{4.2}
\]

The function is finite, Boolean, balanced and monotone by the source theorem and the construction above. Its influence is exactly

\[
\boxed{
I(G_*)=
\frac{4929179520764703137301}{2361183241434822606848}.}
\tag{4.3}
\]

Using (2.5), (2.7), (2.9), and the lower endpoint of (3.8),

\[
H(G_*)
>
7.0930917661293175954877340734816405113107092090489238041406283794989125.
\tag{4.4}
\]

Therefore

\[
\boxed{
\frac{H(G_*)}{I(G_*)-1}
>
6.5218511190811741401649047123074662558509151627606049713533024073225119.}
\tag{4.5}
\]

This is strictly above the complete peer upper endpoint (1.1). The certified gap is

\[
\boxed{
6.5218511190811741401649\ldots
-
6.5218509495504481848824\ldots
>
1.6953072595528248973526791213605480288369938437894\times10^{-7}.}
\tag{4.6}
\]

Thus the improvement is much larger than the entire `<2.833e-30` future tail of the previously exhausted full-fourfold recurrence; it is not another round of that recurrence.

Finally, applying the consumed balanced equivalence (1.2) gives the new source-bound FEI lower bound

\[
\boxed{
C_{\rm FEI}
>
6.5218511190811741401649047123074662558509151627606049713533024.}
\tag{4.7}
\]

This is a **lower bound only**. It neither proves a finite dimension-independent upper bound nor proves the full FEI conjecture.

## 5. Why the mechanism works, and the next exact attack

For a balanced gadget `h`, the shared-core ratio is

\[
\frac{H_0+\frac9{256}H(h)+K(b)}
{(I_0-1)+\frac9{256}(I(h)-1)}.
\tag{5.1}
\]

If `h` has fixed balanced-excess ratio `r`, then replacing it by a higher-influence disjoint self-composition leaves `r` unchanged but makes the fixed positive correction `K(b)` comparatively negligible. The one-branch chain (3.1)–(3.5) reaches the same target coefficient `b=ell^4` with far smaller `I(h)-1`; this is why it beats the full-fourfold construction.

This identifies the next nontrivial adversarial problem exactly: among balanced monotone gadgets obtainable by **partial heterogeneous substitution**, maximize the pair

\[
\left(
\frac{H(h)}{I(h)-1},\; b=\widehat h(\{d\})
\right)
\tag{5.2}
\]

against the exact shared-core objective (5.1). A universal all-gate potential must survive that optimization. Merely iterating the old full-fourfold recurrence is no longer relevant after the peer tail theorem.

### Exact old/new implications

- **Old owner candidate:** read-once `Gamma` / decomposable-AND extremality. Already `CANDIDATE_REFUTED` by the balanced Numaro witness.
- **Latest peer candidate boundary:** freeze the all-gate center after exhausting the source-valid full-fourfold shared-graft recurrence, whose `R_6` upper endpoint is (1.1).
- **New result:** the different partial-branch Boolean construction `G_*` rigorously exceeds that entire endpoint by (4.6). Therefore every potential with `Gamma(1/2)` at or below (1.1) is `CANDIDATE_REFUTED`.
- **Remaining universal implication:** prove one finite upper envelope for all balanced Boolean gates, equivalently one finite-cap all-gate potential satisfying (1.1) of the campaign statement, or continue falsification with a genuinely stronger Boolean composition mechanism.

Verifier SHA-256: `9b0bf579e194fd217db5bec0598ae9ce43ffdb5320625e1f92e688721aec7fcf`.

Captured output SHA-256: `d5adfa04c554e4bdce738d4e28833c489664e722d1da5c1dd7d94dcdc3a62b21`.

No novelty or publication-priority claim is made.