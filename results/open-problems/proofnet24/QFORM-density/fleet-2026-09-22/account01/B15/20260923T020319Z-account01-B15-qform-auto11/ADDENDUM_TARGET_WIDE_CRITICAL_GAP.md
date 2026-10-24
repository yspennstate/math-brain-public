# account01/B15 addendum — target-wide critical-gap normal form

Status: `TARGET_LEVEL_REGULARITY_LEMMA / EXACT_CRITICAL_GAP_NORMAL_FORM`; full QFORM remains **OPEN / NOT PROVED**.

This addendum records a target-wide strengthening noticed during final verification of the run. It uses the completed `account02/B15` fixed-instance regularity theorem (`yspennstate/math-open-problems@9b8bb7e84811978a2c46c7bb5ec50f2570dbc056`): every fixed target matrix of rank at least three and every cap-one product input have a bounded density with a representative in `C_0(R)`. No universal height is imported from that theorem.

## 1. Sharp owner constant and spectral normalization

Let `T` be the full owner target class: independent scalar densities `<=1` and real symmetric `A` with

`s=s_3(A)>=1`,

where `s_3(A)` is the third-largest eigenvalue modulus. Let

`C_* = sup_T ||p_Q||_infinity`, `Q=X^T A X`,

possibly `+infinity`.

Then

`boxed: C_* = sup_T s ||p_Q||_infinity.`

Indeed, the right side is at least `C_*` because `s>=1`. Conversely, for any target `A`, put `B=A/s`. Then `s_3(B)=1`, `Q_B=Q_A/s`, and

`p_{Q_B}(t)=s p_{Q_A}(s t)`.

Hence `||p_{Q_B}||_infinity=s||p_{Q_A}||_infinity`, and `B` is again in the owner target class. Taking suprema proves equality.

## 2. The unique critical output value can be excluded exactly

For every fixed `R>0`, define

`G_R = sup_{T, |t|>=R} s p_Q(t)`

using the canonical `C_0` representative furnished by the partner theorem. Then

`boxed: G_R=C_* for every R>0.`

The upper bound follows from Section 1. For the reverse direction, continuity gives

`||p_Q||_infinity = sup_{t!=0} p_Q(t)`

for each target instance: even if the maximum is attained at the critical value `t=0`, it is approached by nonzero `t`.

Fix such a nonzero `t` and scale `A` by any `a>=R/|t|`. Then `A_a=aA` remains in the owner target class,

`s_a=a s`, `Q_a=aQ`, `p_{Q_a}(u)=a^{-1}p_Q(u/a)`,

and `|at|>=R`. Therefore

`s_a p_{Q_a}(at)=s p_Q(t)<=G_R`.

Taking the supremum over nonzero `t` and all target instances, then using Section 1, gives `C_*<=G_R`.

Thus the sharp universal-height problem may, with zero loss, be restricted to output points an **arbitrarily prescribed positive distance from the sole critical value zero**. This is a scale normalization across matrices; it does not say that a maximizer of a fixed normalized matrix is separated from zero.

## 3. Exact fixed-window normal form outside an arbitrary critical gap

Fix any `R>1` and define

`W_R = sup_{T, |y|>=R} (s/2) P(|Q-y|<=1)`.

Then

`boxed: W_R=C_* for every R>1.`

### Upper bound

For every target instance and center,

`P(|Q-y|<=1)<=2||p_Q||_infinity`.

Hence

`(s/2)P(|Q-y|<=1)<=s||p_Q||_infinity<=C_*`

by Section 1.

### Reverse bound

Fix a target instance and any `t!=0`. For `a->infinity`, eventually `|at|>=R`. Since `A_a=aA` is a target instance,

`W_R >= (a s/2) P(|aQ-at|<=1)`
`     = (a s/2) int_{t-1/a}^{t+1/a} p_Q(u)du`.

The completed partner theorem gives continuity at `t`, so the right side tends to `s p_Q(t)`. Taking suprema and invoking Sections 1–2 gives `W_R>=C_*`.

Because `R>1`, every unit window `[y-1,y+1]` in this normal form stays at distance at least `R-1` from the critical value zero. In particular one may take `R=2` and work only with windows wholly contained in `(-infinity,-1] union [1,infinity)`.

## 4. Exact fixed-tent normal form outside the same gap

Let `T_1(u)=(1-|u|)_+`, `int T_1=1`, and define

`K_R = sup_{T, |y|>=R} s E T_1(Q-y)`.

For every `R>1`,

`boxed: K_R=C_*.`

The upper bound is

`s E T_1(Q-y)<=s||p_Q||_infinity int T_1<=C_*`.

For the reverse bound, with the same scaled instance and center `at`,

`a s E T_1(aQ-at)`
`=s int_{-1}^1 T_1(v) p_Q(t+v/a)dv`
`->s p_Q(t)`

by continuity and dominated convergence. Take suprema.

## 5. Consequence for the full owner target

The full conjecture is therefore exactly equivalent to **any one** of the following target-wide statements, with the same sharp constant `C_*`:

1. `sup_T s||p_Q||_infinity<infinity`;
2. for any fixed `R>0`, `sup_{T,|t|>=R} s p_Q(t)<infinity`;
3. for any fixed `R>1`, `sup_{T,|y|>=R} (s/2)P(|Q-y|<=1)<infinity`;
4. for any fixed `R>1`, `sup_{T,|y|>=R} s E(1-|Q-y|)_+<infinity`.

This is stronger than merely replacing a shrinking window by one fixed scale: **the fixed window may also be required to avoid an arbitrarily large neighborhood of the critical value zero**.

The theorem separates regularity from height exactly as required by the B15 assignment. The only role of continuity is to make the canonical pointwise sharp constant and approximate-identity limit exact for each fixed instance. The universal estimate is still completely unpaid.

## 6. What this does and does not remove

This normalization shows that cone-vertex singularity at output `0` is not, by itself, the essential source of a universal-height obstruction. Any hypothetical large target density can be transferred, in the scaled sharp functional, to a noncritical output level as far from zero as desired.

It does **not** make projection-only or arbitrary-joint arguments valid. In particular `QFORM-TWOSHEET-XRAY-ONLY-FALSE` already builds an arbitrary 3D density with bounded X-ray norm and arbitrarily concentrated indefinite quadratic output near the noncritical level `-1`. Product provenance remains essential.

Nor does the result assert a uniform modulus of continuity for raw target densities; such a modulus is already known to fail. It only uses instancewise `C_0` regularity from the completed partner theorem.

## 7. First unpaid target-wide implication after this addendum

It is enough to prove, for one convenient fixed number such as `R=2`,

`boxed: sup_{T, |y|>=2} [s_3(A)/2] P(|X^T A X-y|<=1) < infinity.`

This is a full-dimensional positive small-ball statement in the original product coordinates, at one fixed output scale and with the observation window uniformly separated from the only critical output value. If proved, it gives the full unrestricted QFORM density theorem with the same universal constant after the exact normalizations above.
