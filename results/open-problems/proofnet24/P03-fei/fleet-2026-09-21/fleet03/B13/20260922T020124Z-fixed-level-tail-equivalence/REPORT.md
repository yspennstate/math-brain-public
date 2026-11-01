# fleet03/B13 — fixed Fourier-level peeling is FEI-complete

**Run:** `fleet03-B13-20260922T020124Z-gate-extremality-r11`  
**Outcome:** `AUXILIARY_ONLY` as a full-proof status, but with a proved constant-for-constant reduction and a refuted proof shortcut.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Live target and change of method

Fresh owner control revision `2026-09-22.2` sends every FEI worker to the all-gate formulation

\[
\Gamma(p_{\rm out})+H_t(G;p)
\le \sum_i {\rm It}_i(G;p)
 {\Gamma(p_i)+h(V_{p_i})\over V_{p_i}},
\tag{G}
\]

and asks either for an all-gate proof or a genuine gate needing a larger correction margin than the binary-AND/read-once candidate.

That specific AND-extremality candidate is no longer an open implication in the current source state. I consumed the explicit composition-prime ten-input falsifier from fleet04/B13,

`proofnet24/P03-fei/fleet-2026-09-21/fleet04/B13/20260922T0055Z-arity10-prime-falsifier/REPORT.md`, blob `d71f08f9a2fd0b417ac7b0cdbac19bacac85c01b`.

It gives a balanced composition-prime Boolean gate with

\[
I={257\over128},\qquad {H\over I-1}>6.4593722816378554,
\]

and hence a read-once-potential margin strictly larger than the live AND margin. Thus I do **not** repeat the already-settled falsification. The replacement obligation is to find a finite universal bound, equivalently some new finite-centre all-gate potential.

This run tests a natural next shortcut suggested by profile/coding approaches:

> pay finitely many low Fourier levels separately, then hope the remaining high-level entropy has a strictly easier universal constant.

The shortcut is false in the strongest possible constant-for-constant sense.

## 1. Peer theorem consumed

The main completed other-account theorem used here is fleet02/B17,

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B17/20260921T124438Z-support-deficit-balanced-equivalence/REPORT.md`, blob `040ed0078f4905b9b4a11e963f27a1e6dcc3ee8d`.

For every finite `C`, it proves the exact equivalence

\[
H(h)\le C I(h)\quad\text{for every Boolean }h
\tag{1.1}
\]

if and only if

\[
H(f)\le C\,[I(f)-1]
\quad\text{for every balanced Boolean }f.
\tag{1.2}
\]

It also proves the balanced self-composition recurrence. If `f` is balanced with
\(a=I(f)\), \(b=H(f)\), and `F_d` is its depth-`d` disjoint self-composition, then for \(a>1\)

\[
I(F_d)=a^d,\qquad
H(F_d)=b\,{a^d-1\over a-1}.
\tag{1.3}
\]

Fleet01/B15 independently applies exactly this recurrence to a fixed composition-prime ten-input gate; its complete report is

`proofnet24/P03-fei/fleet-2026-09-21/fleet01/B15/20260922T011010Z-prime-gate-recursive-amplifier/REPORT.md`, blob `962bd574f875a97302ba37edb889151f76f88a16`.

## 2. The exact universal statement attempted

For a balanced Boolean function `f`, write

\[
p_S=\widehat f(S)^2,
\qquad
H_{>r}(f)=\sum_{|S|>r}p_S\log_2{1\over p_S}.
\tag{2.1}
\]

Here `r` is any fixed nonnegative integer.

### Theorem 2.1 — fixed-level tail FEI is exactly full FEI

For every fixed integer \(r\ge0\) and every finite constant \(C\), the following are equivalent:

1. every Boolean `h` satisfies \(H(h)\le C I(h)\);
2. every balanced Boolean `f` satisfies
   \[
   H_{>r}(f)\le C\,[I(f)-1].
   \tag{2.2}
   \]

Equivalently, if

\[
C_{>r}:=\sup_{f\ \mathrm{balanced},\ I(f)>1}
 {H_{>r}(f)\over I(f)-1},
\tag{2.3}
\]

then, allowing the value `+infinity`,

\[
\boxed{C_{>r}=C_{\rm FEI}}
\qquad\text{for every fixed }r.
\tag{2.4}
\]

Thus deleting any fixed finite number of Fourier levels does **not** lower the sharp universal constant at all.

### Proof

`(1) => (2)` follows from fleet02/B17: full FEI at constant `C` gives the balanced support-deficit inequality \(H(f)\le C(I(f)-1)\), and \(H_{>r}(f)\le H(f)\).

For the converse, assume (2.2). Fix a balanced Boolean `f` with

\[
a=I(f),\qquad b=H(f).
\]

If \(a=1\), Parseval and balance imply all spectral mass is on level one. Hence `f` is a degree-one Boolean function. Writing \(f=\sum_i c_i x_i\), the nonzero degree-two Fourier coefficients of \(f^2\) are \(2c_i c_j\); since \(f^2\equiv1\), at most one `c_i` is nonzero. Parseval then makes it \(\pm1\), so `f` is a character and \(b=0\). Thus (1.2) holds.

Assume now \(a>1\), and form the depth-`d` self-composition `F_d`. By (1.3),

\[
{H(F_d)\over I(F_d)-1}={b\over a-1}
\tag{2.5}
\]

for every `d`.

`F_d` lives on \(N_d=n^d\) coordinates when `f` has arity `n`. There are at most

\[
M_d=\sum_{k=0}^{r}{N_d\choose k}
\tag{2.6}
\]

Fourier atoms of size at most `r`. Let

\[
H_{\le r}(F_d)=H(F_d)-H_{>r}(F_d).
\]

Take the subprobability vector consisting of those at most `M_d` atom masses, and add its missing mass as one extra category. The entropy of that `(M_d+1)`-point probability vector is at most \(\log_2(M_d+1)\), while it is at least \(H_{\le r}(F_d)\). Therefore

\[
H_{\le r}(F_d)\le \log_2(M_d+1).
\tag{2.7}
\]

For fixed `r`, the right side is `O(d)`: for example,

\[
M_d\le (r+1)N_d^r=(r+1)n^{rd}.
\tag{2.8}
\]

Apply the assumed tail inequality (2.2) to `F_d`:

\[
H(F_d)
\le C(a^d-1)+\log_2(M_d+1).
\tag{2.9}
\]

Divide by \(a^d-1\) and use (2.5):

\[
{b\over a-1}
\le C+{\log_2(M_d+1)\over a^d-1}.
\tag{2.10}
\]

Because \(a>1\), the last term tends to zero exponentially. Hence

\[
b\le C(a-1).
\]

This is (1.2) for the original arbitrary balanced `f`; fleet02/B17 then gives full FEI at the same constant `C`. QED.

## 3. Stronger quantitative form

The same proof does not require `r` to be literally fixed. For a depth-`d` self-composition on \(N_d=n^d\) coordinates, any cutoff sequence `r_d` satisfying

\[
\log_2\!\left(1+\sum_{k=0}^{r_d}{N_d\choose k}\right)=o(a^d)
\tag{3.1}
\]

has

\[
{H_{\le r_d}(F_d)\over I(F_d)-1}\to0.
\tag{3.2}
\]

A sufficient elementary condition is \(r_d d=o(a^d)\). Thus the invariant balanced obstruction can be pushed above cutoffs growing almost linearly in its mean spectral size (up to logarithmic losses). A proof that only pays bounded or slowly growing low levels cannot lower the target constant.

This is an asymptotic statement about explicit finite Boolean self-compositions at every depth, not a non-Boolean relaxation.

## 4. Concrete source-valid prime-gate calculation

For the fleet04/B13 ten-input monotone prime gate, monotonicity makes the magnitudes of its singleton Fourier coefficients equal its individual influences. The exact list from the peer certificate is

- eight singleton coefficients of magnitude \(29/128\);
- one of magnitude \(49/256\);
- one of magnitude \(1/256\).

Therefore its exact singleton spectral mass is

\[
W_1={14657\over32768}=0.447296142578125,
\tag{4.1}
\]

and its singleton entropy is

\[
H_1=1.9342375831117603809586524544148078\ldots.
\tag{4.2}
\]

If this gate is self-composed to depth `d`, a final singleton spectral atom occurs only through a singleton outer atom at every level. Consequently, exactly,

\[
W_1(F_d)=W_1^d,
\qquad
H_1(F_d)=dW_1^{d-1}H_1.
\tag{4.3}
\]

Using \(a=257/128\) and the certified lower bound
\(R=H/(I-1)>6.4593722816378554\), the following lower bounds result for the entropy carried by levels at least two:

| depth `d` | `H_1(F_d)/(I(F_d)-1)` | `H_{>=2}(F_d)/(I(F_d)-1)` lower bound |
|---:|---:|---:|
| 1 | 1.919243493320196 | 4.540128788317659 |
| 2 | 0.570826945649231 | 5.888545335988624 |
| 4 | 0.045398719227256 | 6.413973562410599 |
| 6 | 0.003220905495045 | 6.456151376142810 |
| 8 | 0.000210682340572 | 6.459161599297283 |
| 12 | 0.000000775641604 | 6.459371505996251 |

This is a concrete counterexample sequence to the hope that the gate obstruction is substantially a low-degree/singleton phenomenon.

## 5. Apply the newest other-account lower floor

A second completed peer result was consumed:

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B12/20260922T013941Z-shared-graft-tail/REPORT.md`, blob `1ff8ad8dc43e0aaa70a215dd172f19151c32a002`.

It proves a genuine finite balanced Boolean shared-graft round with

\[
{H(F_5)\over I(F_5)-1}>6.5218509495457.
\tag{5.1}
\]

Apply Theorem 2.1 to that finite gate and its ordinary balanced self-compositions. For **every fixed** Fourier cutoff `r`,

\[
\boxed{C_{>r}>6.5218509495457.}
\tag{5.2}
\]

So even after throwing away every Fourier coefficient on levels `0,1,...,r`, the remaining tail by itself already has a universal constant floor above `6.5218509495457`.

## 6. Exact failed claim and replacement obligation

### Refuted shortcut

`REFUTED:` there is a fixed finite Fourier cutoff after which the entropy-influence problem has a strictly smaller sharp constant and the low levels can be treated as the only source of the current obstruction.

Theorem 2.1 rules this out constant-for-constant. The self-composition mechanism can bury the same balanced support-deficit obstruction above every fixed cutoff.

### What remains open

This does **not** refute FEI and does not provide a finite universal upper bound. It says that a successful replacement for the dead read-once all-gate potential must control genuine high-level entropy; paying finitely many low levels, singleton labels, or a bounded Fourier prefix cannot by itself reduce the universal constant.

The remaining implication is still the owner-selected one after the current candidate's falsification: construct some finite-centre symmetric nonnegative potential satisfying (G) for every gate/bias, or prove an equivalent finite universal bound. The present theorem narrows the search by showing that any fixed-level decomposition must retain a tail estimate already FEI-complete.

**Next recipient:** `fleet03/B18` (FEI proof integration) and `fleet02/B12` (spectral compression). The useful formula to consume is Theorem 2.1, especially the constant-for-constant direction `(tail at C) => full FEI at C` via balanced self-composition.

No novelty or publication-priority claim is made. Full FEI remains **OPEN / NOT PROVED**.
