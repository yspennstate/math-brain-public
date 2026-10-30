# fleet03/B17 — exact prime-Bellman one-core dent transport

**Classification:** `ESSENTIAL_STEP_APPLIED / PRIME_BELLMAN_DENT_TRANSPORT / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED**.

## 0. Live target and change of mechanism

The live owner convergence target is the all-gate potential inequality.  The fixed seed discussed below is the source-exact candidate

\[
C^\dagger=6.521851214,\qquad
\Gamma^\dagger(p)=\Gamma_0(p)+0.268204856\,p(1-p),
\]

where `Gamma_0` is the committed `cert_vi_h96k40.npz` read-once potential.

The previous fixed-candidate route is already refuted by the composition-prime Numaro gate.  Therefore this run does **not** add another unrelated truth-table sweep.  It consumes the prime Bellman-envelope reduction and asks the next exact question: when the envelope makes a forced downward dent at one bias, can the same source-bound prime gate transport that dent through later Bellman iterates strongly enough to threaten nonnegativity?

The answer here is a nontrivial **yes for eight exact steps**, but the same one-core mechanism then dies.  This isolates a much smaller remaining return-map problem.

## 1. Completed cross-account theorem consumed and applied

The named completed peer result is fleet04/B18,

`proofnet24/P03-fei/fleet-2026-09-21/fleet04/B18/20260922T071537Z-prime-repair-shape-barrier/PRIME_BELLMAN_ENVELOPE.md`, creation commit
`a6b9372512342993ba16a1892ccda12dddf1e7d7`.

It defines, over composition-prime gates plus the unary identity,

\[
R_G(\Gamma;q)=
\sum_i {\rm It}_i(G;q){\Gamma(q_i)+h_2(V_{q_i})\over V_{q_i}}
-\widetilde H_G(q),
\]

\[
(\mathcal T\Gamma)(p)=\inf_{G,q:\,p_{\rm out}=p}R_G(\Gamma;q),
\]

and proves that fixed points of `T` are exactly universal all-gate potentials.  It also proves monotonicity, continuity from above, and the dominated-fixed-point criterion: if all iterates `Gamma_{m+1}=T Gamma_m` from a nonnegative seed remain nonnegative, their decreasing limit is a universal potential; if a finite iterate becomes negative, that particular dominated-envelope seed is dead.

I apply this theorem to the exact Numaro source gate.  Fleet04/B14 proved the same truth table is composition-prime by the ANF rank-one criterion, rejecting every one of the `262124` proper decomposition blocks.  Hence every biased use below is a valid term in the **prime** Bellman infimum.

## 2. Exact one-core transport identity

Let `F` be the source-bound 18-variable Numaro gate, with truth-table SHA-256

`f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839`.

At uniform bias each of its nine core coordinates has singleton Walsh coefficient

\[
\alpha={57\over256}.
\]

Bias one core coordinate at `p` and keep the other 17 inputs at `1/2`.  Put

\[
t=1-2p.
\]

Pairing uniform Fourier coefficients across that core coordinate gives exactly

\[
\widehat F_p(S)=a_S-tb_S,
\qquad
\widehat F_p(S\cup\{i\})=\sqrt{1-t^2}\,b_S.
\tag{2.1}
\]

Therefore the biased spectral masses are rational whenever `p` is rational:

\[
w_S=(a_S-tb_S)^2,
\qquad
w_{S\cup\{i\}}=(1-t^2)b_S^2.
\tag{2.2}
\]

The output bias contracts centered deviation exactly:

\[
\boxed{
F_*(p)=\frac12-\alpha\left(\frac12-p\right).
}
\tag{2.3}
\]

Moreover the pivotal probability of this coordinate is independent of its own bias, so

\[
\boxed{
{{\rm It}_i(F;p)\over V_p}=\alpha={57\over256}.
}
\tag{2.4}
\]

Let

\[
\Gamma_m=\mathcal T^m\Gamma^\dagger,
\qquad
\Delta_m(p)=\Gamma^\dagger(p)-\Gamma_m(p)\ge0
\]

whenever the iterate is finite.  Write

\[
D^\dagger(p):=D_{\Gamma^\dagger}
\bigl(F;(p,1/2,\ldots,1/2)\bigr).
\]

Applying the same prime gate as one admissible term in `T`, and using `Gamma_m<=Gamma^dagger`, gives the exact dent-transfer inequality

\[
\boxed{
\Delta_{m+1}(F_*(p))
\ge
\alpha\,\Delta_m(p)-D^\dagger(p).
}
\tag{2.5}
\]

This is the new source-valid mechanism.  It is not a heuristic about nearby potentials: (2.5) is an immediate Bellman consequence of the exact biased gate inequality and the peer's prime-envelope theorem.

## 3. A stronger prime violation than the previously used first dent

The previous Bellman report used the exact prime witness at

\[
p=3/8,\qquad p_{\rm out}=967/2048,
\]

with

\[
D^\dagger=-0.0176114199558\ldots.
\]

The one-core formula exposes a substantially stronger rational point:

\[
\boxed{p={223\over456}},
\qquad
\boxed{F_*(p)={1019\over2048}}.
\]

The exact-rational mass computation together with rational atanh-series logarithm enclosures gives

\[
\boxed{
D^\dagger(223/456)
=-0.0380237343652791923\ldots<0.
}
\tag{3.1}
\]

Thus the first envelope dent is at least `0.03802373436527919`, more than twice the earlier `0.0176114` dent.

For comparison, if one insisted on repairing only by increasing the scalar quadratic coefficient in `Gamma_0+c p(1-p)`, this one witness alone requires

\[
c>0.4145936656\ldots,
\]

which would put the center above approximately `6.5584484164`.  This is **not** a lower bound on the true FEI constant; a shaped Bellman repair can do better.

## 4. Eight-step exact dent cascade

To test whether the first dent immediately dissipates, start at the exact mesh node

\[
p_0={27\over64}
\]

and iterate only the one-core prime action.  By (2.3),

\[
\boxed{
 p_r={1\over2}-{5\over64}\left({57\over256}\right)^r.
}
\tag{4.1}
\]

Starting with `Delta_0(p_0)=0`, define the certified lower bound recursively by

\[
d_{r+1}=\alpha d_r-D^\dagger(p_r).
\tag{4.2}
\]

The checker proves the following values with rational spectral masses and exact logarithm enclosures; the displayed lower/upper endpoints agree to the shown digits.

| r | p_r (decimal) | D^dagger(p_r) | forced d_{r+1} |
|---:|---:|---:|---:|
|0|0.421875000000000|-2.949721936018588e-2|2.949721936018588e-2|
|1|0.482604980468750|-3.765739768036862e-2|4.422513792853501e-2|
|2|0.496126890182495|-1.238204977982591e-2|2.222905314672628e-2|
|3|0.499137627892196|-7.952949029505733e-4|5.744732517651347e-3|
|4|0.499807987460372|+6.165310421542769e-6|1.272935289211765e-3|
|5|0.499957247207973|+5.745644379463878e-6|2.776813536090932e-4|
|6|0.499990480823650|+5.719678481178613e-6|5.610781040834604e-5|
|7|0.499997880495891|+5.718135422822338e-6|6.774619238410960e-6|
|8|0.499999528079163|+5.718046244761963e-6|-4.209634929959523e-6|

Hence

\[
\boxed{
\Delta_8(p_8)>6.774619238410960\times10^{-6}
}
\tag{4.3}
\]

at

\[
p_8=0.4999995280791632\ldots,
\qquad
\frac12-p_8=4.719208367932034\times10^{-7}.
\]

The next unchanged one-core step has a negative lower bound, so this exact mechanism has reached its natural stopping point.  I do **not** continue it by pretending a negative lower bound is information.

## 5. The remaining gap is a return map, not dent magnitude

The same source gate at the exact unbiased center has

\[
I={261\over128},
\]

and the checker encloses its seed defect by

\[
D^\dagger_{\rm center}
=5.71804089691748009\times10^{-6}\ldots .
\]

If a center dent `Delta(1/2)` is fed back through this uniform prime gate, the linear Bellman multiplier is `I-1=133/128>1`.  Therefore the self-amplification threshold is

\[
\boxed{
\tau_{\rm center}
={D^\dagger_{\rm center}\over I-1}
=5.50307695342434193\times10^{-6}\ldots .
}
\tag{5.1}
\]

The transported off-center dent from (4.3) is already larger:

\[
\boxed{
{d_8\over\tau_{\rm center}}>1.2310602406.
}
\tag{5.2}
\]

So the current obstacle is sharply localized.  We no longer need to manufacture a larger dent.  We need a **source-valid low-cost return map** from the bias `p_8` (or a nearby propagated state) to the center, preserving enough of that dent.  If such a return forces a center dent above (5.1), repeated uniform use of the same composition-prime gate would make a finite Bellman iterate negative and would rigorously kill the dominated `Gamma^dagger` envelope route.

This does not refute FEI: a different seed/potential may still have nonnegative Bellman iterates.

## 6. Refutation attempt and method change

I stress-tested the obvious closure rather than assuming it.

- Continuing the same one-core contraction is dead: row `r=8` above gives a negative next lower bound.
- Exact balancing with one auxiliary coordinate of the same Numaro gate was tested as a return-to-center mechanism.  Although the relevant core dent is positive, the gate's own seed defect dominates the transported credit in the tested late stages, so it does not return a positive certified center dent.
- Low-complexity multi-core fan-out tests show a different phenomenon: using several core inputs at the same dented bias can have total transport coefficient above one.  In particular the nine-core action near the center has first-order multiplier `9*57/256=513/256>2`.  This is a genuinely different candidate return/cycle mechanism and is the next attack; it must be certified as a finite prime-gate cascade rather than extrapolated from a local linearization.

Thus the next nonredundant obligation is a **prime-gate return/cycle theorem**: either exhibit a finite source-valid sequence of prime Numaro biasings that returns the dent to a previously visited bias (especially the center) with net gain sufficient to cross the Bellman nonnegativity threshold, or prove an invariant showing every such cycle is dissipative.

## 7. Status ledger

- **PROVED:** fleet04/B18 prime Bellman fixed-point/dominated-seed reduction.
- **PROVED:** the Numaro source gate is composition-prime (fleet04/B14).
- **PROVED HERE:** exact one-core dent transport identity (2.5).
- **PROVED HERE:** stronger rational prime violation (3.1).
- **PROVED HERE:** eight-step exact dent cascade (4.3).
- **PROVED HERE:** the off-center dent magnitude exceeds the uniform-center self-amplification threshold (5.2).
- **REFUTED:** unchanged one-core contraction as a complete closure route; its ninth forced dent lower bound is negative.
- **OPEN:** a low-cost prime return/cycle from the propagated near-center state.
- **OPEN:** nonnegativity of all prime Bellman iterates from any viable finite-cap seed.
- **OPEN / NOT PROVED:** full unrestricted uniform-cube FEI.

**Consumed peer artifact:** fleet04/B18 prime Bellman envelope fixed-point reduction, commit `a6b9372512342993ba16a1892ccda12dddf1e7d7`.

**Applied to claim:** survival/nonnegativity of the dominated prime Bellman iterates after the forced Numaro dent.

**Remaining implication:** prove a finite return/cycle that drives a Bellman iterate negative, or prove all such prime cycles dissipate while constructing a different nonnegative fixed-point seed.

**Next recipient:** `fleet04/B18` for prime-envelope integration; `fleet03/B18` can use the dent-vs-center-threshold inequality in the Gibbs/Bellman formulation.
