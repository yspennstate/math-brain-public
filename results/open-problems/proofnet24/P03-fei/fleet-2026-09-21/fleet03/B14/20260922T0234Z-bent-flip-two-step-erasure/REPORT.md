# B14 — a two-step physical block neutralizes the canonical bent-plus-one-point-flip erasure obstruction

**Outcome:** `AUXILIARY_ONLY / HARD_CASE_BLOCK_REFUND_PROVED`.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. Repository/control sources were consumed directly; no authenticated cognitive-brain retrieval/context entered the mathematics.

## 1. Exact candidate version and peer result consumed

The current B14 restriction target asks for a realizable physical policy that keeps the exact restriction-entropy/Poincare payment and survives the known failure of every-coordinate erasure bounds.

The named compatible peer result consumed and applied is

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B14/20260922T0145Z-js-poincare-currency/REPORT.md`
(observed at repository commit `9d01f69d5376d92a4a121c66ee63b32b74b9b1be`).

It proves the sharp universal one-step estimate

\[
JS_i\le16Q_i,
\qquad
P(f)=I(f)/4-q_f(1-q_f),
\]

and consequently reduces the remaining global restriction problem to a pure adaptive erasure problem. In its notation, if one can make cumulative physical erasure finite in Poincare currency, then full FEI follows up to the sharp coherent-recombination surcharge. The peer report explicitly preserves the bent-plus-one-point-flip family as a counterexample to prescribed-coordinate erasure payment.

The prior missing implication attacked here is therefore very specific:

> Does that canonical unbounded one-coordinate erasure family remain an obstruction after allowing a **real two-coordinate physical block**, with every coordinate reveal charged through the exact Poincare drop?

The answer is **no**. A fixed two-step policy has uniformly bounded erasure price, and the complete two-step entropy price is below four.

## 2. The hard family

Let `m>=2` be even, `N=2^m`, and

\[
h_m(x)=(-1)^{x_1x_2+x_3x_4+\cdots+x_{m-1}x_m}
\]

be the standard nondegenerate quadratic bent function on `m` bits. Add a physical bit `z` and define `f_m(x,z)` to equal `h_m(x)` everywhere except at the single point

\[
(x,z)=(0^m,1),
\]

where the sign is flipped.

This is the standard geometry behind the known prescribed-coordinate obstruction: the appended coordinate has

\[
\operatorname{Inf}_z(f_m)=\frac1N,
\]

while its erasure ratio grows linearly in `m`. That failure remains valid and is not weakened here.

The new policy is simply:

> **PAIR-BENT:** first reveal `z`, then reveal one genuine bent coordinate, say `x_1`.

No affine change of variables, selector bit, packet label, or uncharged auxiliary coordinate is introduced.

## 3. Exact Poincare currency of the pair

The source identity for a physical block `A` is

\[
4Q_A
=\sum_{i\in A}\operatorname{Inf}_i(f)
-4\operatorname{Var}_a(q_{A=a}),
\tag{3.1}
\]

with `q` the output `-1` probability. Equivalently, if `mu_a=E[f\mid A=a]`, then the last term is `Var_a(mu_a)`.

For `A={z,x_1}` one has

\[
\operatorname{Inf}_z=\frac1N,
\qquad
\operatorname{Inf}_{x_1}=\frac12+\frac1N.
\tag{3.2}
\]

Put `s=sqrt(N)`. Up to ordering, the four conditional output means are

\[
\frac2s,\quad0,\quad\frac2s-\frac4N,\quad0.
\tag{3.3}
\]

Hence

\[
\operatorname{Var}(\mu_A)
=\frac1N-\frac2{N^{3/2}}+\frac3{N^2}.
\tag{3.4}
\]

Substitution into (3.1) gives the exact block currency

\[
\boxed{
4Q_A
=\frac12+\frac1N+\frac2{N^{3/2}}-\frac3{N^2}.
}
\tag{3.5}
\]

In particular `4Q_A>1/2` for every `N>=4`.

## 4. Exact entropy recursion for the same physical block

Write `H_m=H(f_m)`. Let

\[
t=N^{-1/2}=2^{-m/2}.
\]

Every Walsh coefficient of `h_m` has magnitude `t`. If its sign is `sigma_T`, flipping `(0^m,1)` changes the coefficient without `z` from `sigma_T t` to `sigma_T t-t^2`, and creates every coefficient containing `z` with magnitude `t^2`.

Walsh inversion at zero gives

\[
\#\{\sigma=+1\}=\frac{t^{-2}+t^{-1}}2,
\qquad
\#\{\sigma=-1\}=\frac{t^{-2}-t^{-1}}2.
\]

A direct entropy simplification therefore gives

\[
H_m=m+e(t),
\tag{4.1}
\]
where, with natural logarithms,

\[
e(t)
=\frac{-2t^2\ln t-(1-t^2)F(t)}{\ln2},
\qquad
F(t)=(1-t)\ln(1-t)+(1+t)\ln(1+t).
\tag{4.2}
\]

Now restrict `z` and `x_1`. Three of the four children are restrictions of the bent function and have spectral entropy exactly `m-2`. The fourth child is, after relabeling the partner of `x_1` as the appended coordinate, exactly `f_{m-2}`. (For `m=2`, define `f_0` to be the resulting one-bit character, with entropy zero.) Thus the total two-step entropy decrement is

\[
L_A
=H_m-\frac{3(m-2)+H_{m-2}}4
=2+e(t)-\frac14e(2t).
\tag{4.3}
\]

### Lemma 4.1 — the defect correction costs at most `2/N`

For `0<t<=1/2`,

\[
\boxed{e(t)-\frac14e(2t)\le2t^2.}
\tag{4.4}
\]

**Proof.** The even expansion

\[
F(t)=\sum_{n\ge1}a_nt^{2n},
\qquad
a_n=\frac1{n(2n-1)}
\tag{4.5}
\]

converges also at the endpoint needed here. Algebra from (4.2) gives

\[
e(t)-\frac14e(2t)
=2t^2-\frac{A(t)}{4\ln2},
\tag{4.6}
\]
with

\[
A(t)=4(1-t^2)F(t)-(1-4t^2)F(2t).
\]

Collecting the coefficient of `t^{2n}` yields

\[
\boxed{
A(t)
=4\sum_{n\ge2}(4^{n-1}-1)(a_{n-1}-a_n)t^{2n}\ge0,
}
\tag{4.7}
\]

because `a_n` is strictly decreasing. This proves (4.4). `square`

Consequently

\[
\boxed{L_A\le2+\frac2N.}
\tag{4.8}
\]

Combining (4.8) with (3.5),

\[
16Q_A-\left(2+\frac2N\right)
=\frac2N+\frac8{N^{3/2}}-\frac{12}{N^2}
=\frac2N\left(1+\frac4{\sqrt N}-\frac6N\right)>0.
\]

Therefore the **entire physical two-step entropy price** obeys

\[
\boxed{
\frac{L_A}{4Q_A}<4
\qquad(m\ge2\text{ even}).
}
\tag{4.9}
\]

So this family cannot be a counterexample to a finite-block Poincare selector merely because its appended coordinate is individually disastrous.

## 5. Stronger statement for the pure erasure remainder

Let `E_A` be the cumulative **erasure only** along the realizable order `z` then `x_1`.
At the first step,

\[
B_z\le H(1_{z\in S})=h_2(\operatorname{Inf}_z)=h_2(1/N).
\tag{5.1}
\]

At the second step each child contributes at most one bit of erasure, so

\[
\boxed{E_A\le1+h_2(1/N).}
\tag{5.2}
\]

This already gives a uniform source-exact bound in the currency (3.5). In fact

\[
\boxed{
\frac{E_A}{4Q_A}<\frac73
\qquad(m\ge2\text{ even}).
}
\tag{5.3}
\]

Here is a fully elementary proof of the displayed constant.

* `m=2` (`N=4`): after the `z=1` branch the one-point-flipped two-bit bent child is a character, so the average second-step erasure is at most `1/2`; hence `E_A<=3/2`. Since `4Q_A=13/16`, the ratio is at most `24/13<7/3`.
* `m=4` (`N=16`):
  \[
  h_2(1/16)=\frac14+\frac{15}{16}\log_2(16/15)<\frac{11}{32},
  \]
  because `ln(16/15)<1/15` and `ln 2>2/3`. Thus `E_A<43/32`, while `4Q_A=149/256`; hence `E_A/(4Q_A)<7/3`.
* `m>=6`: use the standard binary-entropy bound
  \[
  h_2(1/N)\le\frac{\log_2(eN)}N<\frac{m+3/2}{N}
  \]
  and `4Q_A>=1/2+1/N`. The desired inequality follows from
  \[
  2^m=N>6m-5,
  \]
  true at `m=6` and preserved when `m` increases by two.

Thus the exact canonical fixed-coordinate erasure obstruction has a two-step physical policy whose **pure erasure** cost is uniformly below `7/3` in Poincare-currency units.

## 6. Attempted refutation and numerical stress check

A separate checker directly constructs the Boolean functions, computes Walsh spectra, physically restricts the two coordinates, and evaluates both the full block price and the sequential erasure price. It is regression evidence only; Sections 3--5 are the proof.

| `m` | full `L_A/(4Q_A)` | sequential erasure `E_A/(4Q_A)` |
|---:|---:|---:|
| 2 | 2.728513460540 | 1.437688918146 |
| 4 | 3.625809539973 | 1.994022647046 |
| 6 | 3.913580584858 | 2.064888843144 |
| 8 | 3.980890834898 | 2.033549306796 |
| 10 | 3.995630516121 | 2.012549025884 |
| 12 | 3.998963924169 | 2.004146511411 |
| 14 | 3.999748323716 | 2.001284806054 |

The full price tends to `4` from below, so the proof's constant `4` is asymptotically sharp for **this particular two-coordinate policy**. The erasure-only price tends to `2`; no universal sharpness claim is made for `7/3`.

## 7. Exact status, dead route, and replacement obligation

**PROVED:** for the complete even-dimensional bent-plus-one-point-flip family, the actual two-step physical policy `z -> x_1` has full entropy price `<4` and pure-erasure price `<7/3` in exact Poincare currency.

**PRESERVED REFUTATION:** the prescribed-coordinate statement `B_i<=K Inf_i` remains false; the appended coordinate's normalized one-step erasure grows with `m`. The new result does not erase that counterexample; it shows why it is not a finite-block obstruction.

**NOT PROVED:** there is no universal theorem here that every Boolean function has a two-coordinate block with bounded price. The shared-core family already demonstrates that a larger physical block can be the natural selector. No all-arity/all-bias gate potential is proved.

**Replacement obligation:** the next genuine obstruction to the fleet02/B14 adaptive-erasure reduction must be stronger than every known bad single coordinate. One must either prove a dimension-independent finite-block selector in exact `Q` currency, or construct a Boolean family for which **every admissible physical block policy** has unbounded cumulative erasure price. A family with only one bad prescribed coordinate is no longer sufficient.

`consumed_peer_artifact = fleet02/B14/20260922T0145Z-js-poincare-currency/REPORT.md`  
`applied_to_claim = pure adaptive erasure / K_tree obstruction test on bent-plus-one-point-flip`  
`remaining_implication = universal finite physical-block selector, or a genuine all-block obstruction`  
`next_recipient = fleet02/B14`  
`implication_to_full_FEI = auxiliary hard-case closure only; full FEI remains OPEN`.

No novelty or publication-priority claim is made.
