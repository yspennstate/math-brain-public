# B12 FEI creative attempt: Palm obstruction and Boolean cancellation entropy

**Status:** full uniform-cube Fourier entropy-influence (FEI) remains **OPEN / NOT PROVED**.

**Run label:** `WITHOUT_VERIFIED_BRAIN`.

**Route:** APPROACHES #1, spectral-sample compression / sequential prediction. This run continues the fleet03/B12 ordered-set/Palm work rather than repeating its hard-family calculations or the settled read-once certificate.

Let `S` be the spectral sample of a Boolean `f:{-1,1}^n->{-1,1}`,

`p_A = P(S=A) = fhat(A)^2`, `K=|S|`, and `I=E K`.

The previous compression report proved

`H(S) <= U := H(K) + I H(q) - E log2(K!)`, where `q_i=P(i in S)/I`,

and the one-coordinate Palm inequalities

`E[t^(K-1) | i in S] <= Inf_i(f)^((1-t)/(1+t))` for `0<=t<=1`.

It proposed maximizing `U/I` subject to those Palm constraints. The first result below shows that relaxation is too weak. The second result replaces it with a genuinely Boolean quantity whose dimension-free control would imply FEI.

## 1. REFUTED route: the Palm-only variational relaxation is unbounded

Take an **abstract** random subset `S` uniformly distributed over all `m`-subsets of `[n]`, with `m>=2`. Then

`K=m`, `p_i=P(i in S)=m/n`, `I=m`, and `q_i=1/n`.

Conditioned on `i in S`, still `K=m`, so every one-coordinate Palm constraint becomes

`t^(m-1) <= (m/n)^((1-t)/(1+t)).`                                         (1)

For `0<t<1`, (1) is equivalent to

`ln(n/m) <= (m-1)(-ln t)(1+t)/(1-t).`                                    (2)

The elementary inequality

`-ln t >= 2(1-t)/(1+t)`

shows that all Palm constraints hold whenever

`ln(n/m) <= 2(m-1)`.                                                       (3)

For this shell law the Palm consistency identity is also exact: `nu_i=delta_m`, `W_m=1`, so `sum_i p_i nu_i(m)=m=m W_m`.

But the ordered coding functional is

`U/I = log2 n - (1/m) log2(m!).`                                           (4)

Choose `n_m=floor(m exp(2(m-1)))`. Then (3) holds for every `m`, while Stirling gives

`U/I = (2m-1) log2(e) + o(1) -> infinity.`

Thus the full family of one-coordinate Palm inequalities plus the proposed consistency relation does **not** prove CFC(beta), and in fact does not imply any dimension-free bound on `U/I`.

This obstruction already beats the sharp FEI candidate at `m=3`: taking `n=163` gives

`ln(n/m)=3.9951379121 < 4`,

so all Palm constraints hold, but

`U/I = 6.4870739873 > beta(1/2)=6.4547837...`.

For `m=4,n=1613`, the same feasible relaxation has `U/I=9.509290098`; the values then diverge linearly in `m`.

This is **not** a Boolean FEI counterexample. It identifies the missing ingredient: one-coordinate hypercontractive clustering does not exclude an enormous nearly uniform spectral shell, whereas Booleanity does.

## 2. PROVED Boolean structural lemma: upward mass versus a Fourier atom

For `A subseteq [n]`, define the upward spectral mass

`u_A := sum_{B superset A} p_B`.

Equivalently, with normalized iterated derivative `D_A`,

`u_A = ||D_A f||_2^2`.

### Lemma (granular upward-mass inequality)

For every nonempty `A` of size `k`,

`u_A >= 2^(1-k) |fhat(A)| = 2^(1-k) sqrt(p_A)`.                           (5)

Equivalently,

`p_A <= 4^(k-1) u_A^2`.                                                    (6)

### Proof

Fix the outside coordinates `y in {-1,1}^{A^c}` and restrict `f` to the `k` coordinates of `A`. Let

`C_A(y) = widehat{f_y}(A)`

be the top Fourier coefficient of that restricted Boolean function. Fourier expansion in the outside variables gives

`E_y C_A(y) = fhat(A)`,                                                     (7)

`E_y C_A(y)^2 = sum_{B superset A} fhat(B)^2 = u_A`.                       (8)

Because `f_y` is `+-1` on `2^k` inputs, its top coefficient is `2^-k` times a sum of `2^k` signs. That sum is even for `k>=1`; hence

`C_A(y) in 2^(1-k) Z`.                                                      (9)

Therefore pointwise `C_A(y)^2 >= 2^(1-k)|C_A(y)|`. Average, then use the triangle inequality and (7)-(8):

`u_A >= 2^(1-k) E|C_A| >= 2^(1-k)|E C_A| = 2^(1-k)|fhat(A)|`.

This proves (5).

For `k=1`, (6) is exactly the singleton endpoint `P(S={i}) <= Inf_i(f)^2` from the Palm lemma. The new point is that it holds at **every spectral atom**, with the containing-upset mass replacing the first-order influence.

## 3. A new exact FEI reduction: cancellation entropy

Define

`B_can(f) := sum_A p_A log2(u_A/p_A)`, with zero terms omitted and `u_empty=1`.

Since

`H(f) = sum_A p_A log2(1/u_A) + B_can(f)`,                                (10)

(5) bounds the first term. Let

`p0=p_empty=fhat(empty)^2`, `V=1-p0=P(S nonempty)`.

For every nonempty `A`, (5) implies

`log2(1/u_A) <= (1/2)log2(1/p_A) + |A|-1`.                                (11)

Multiplying by `p_A`, summing, and using `sum_A |A|p_A=I` gives

`sum_A p_A log2(1/u_A)`
` <= (1/2)[H(f)-p0 log2(1/p0)] + I - V`.                                  (12)

Combining (10)-(12) and rearranging proves the exact reduction

`H(f) <= 2 I(f) - 2V - p0 log2(1/p0) + 2 B_can(f)`                         (13)

and hence, more simply,

`H(f) <= 2 I(f) + 2 B_can(f)`.                                             (14)

Therefore a universal bound

`B_can(f) <= c I(f)`                                                       (15)

would prove FEI with constant `C=2+2c`. In particular, the sharp candidate `beta(1/2)=6.4547837...` would follow from

`c <= beta/2 - 1 = 2.22739185...`.                                         (16)

This is the concrete residual obligation produced by this route.

## 4. Why `B_can` is the right missing Boolean quantity

Let `T` be an independent spectral sample. Then

`u_A=P(T superset A)` and `p_A=P(T=A)`, so

`p_A/u_A = P(T=A | T superset A)`.

Thus

`B_can = E_{S}[ -log2 P(T=S | T superset S) ]`.                            (17)

It is an **upper-set termination surprisal**: after learning that an independent spectral sample contains the currently named set, how expensive is it to certify that there are no further spectral coordinates?

There is also a restriction/cancellation interpretation. From (7)-(8),

`u_A/p_A = E C_A(y)^2 / (E C_A(y))^2`.                                    (18)

So `B_can` measures, atom by atom, how much the signed top coefficient of a random restriction cancels relative to its second moment. The abstract uniform-shell obstruction has no Boolean mechanism enforcing these restriction identities. A proof of (15) can therefore focus directly on paying sign cancellation by additional spectral degree/influence.

## 5. Immediate structured consequence

Suppose the nonzero Fourier spectrum of a Boolean function is supported on one positive level `k` (so `K=k` almost surely). For every support atom `A`, no strict spectral superset exists, hence `u_A=p_A` and `B_can=0`. Also `p0=0`, `V=1`, `I=k`. Equation (13) gives

`H(f) <= 2k-2 = 2I(f)-2`.                                                  (19)

Thus the exact shell law that makes the Palm relaxation unbounded cannot be a Boolean spectrum with arbitrary shell size: Booleanity forces at most `2^(2k-2)=4^(k-1)` nonzero equal-size Fourier atoms at that level by (5).

This is only a structured-class consequence, not a universal FEI proof.

## 6. Decisive finite sanity check

The attached standard-library checker enumerates every Boolean function through `n=4` after fixing global sign. It verifies (5) for every nonempty Fourier atom and verifies (13) for every function. It also computes `B_can/I`.

Maximum `B_can/I` among the enumerated nonconstant functions:

- `n=2`: `1.0000000000`,
- `n=3`: `1.3725562489`,
- `n=4`: `1.4649755512`.

In each of `n=2,3,4`, the maximizer in this enumeration is the one-point defect. These numbers are well below the sufficient sharp-target threshold `2.22739185`, but finite checks are only evidence.

Every enumerated pure-level Boolean function had `B_can=0`, as predicted.

## 7. Dead route and next attack

**Dead route, proved dead:** the Palm-only variational program proposed in the prior spectral-compression report is unbounded; its `m=3,n=163` feasible shell already crosses beta.

**Alive route:** prove or refute the Boolean cancellation-entropy inequality (15). The next useful attack is not another small-`n` sweep. It is to derive a recursive/payment inequality for

`p_A log2(E C_A^2/(E C_A)^2)`

that charges cancellation of the signed restricted coefficient `C_A` to Fourier mass on strict supersets `B supersetneq A`, with a charge that sums to `O(sum_B |B|p_B)=O(I)` rather than counting all subsets of `B`. A random-chain or stopping-time allocation over the Boolean lattice is a natural way to avoid the exponential ancestor multiplicity.

A secondary target is to compute `B_can/I` exactly along finite stages of Hod's extremal read-once construction. If it tends to `beta/2-1`, (13) may be asymptotically sharp; if it stays strictly lower, the granularity step rather than the cancellation payment is where the sharp constant is lost.

## 8. Classification

- **PROVED:** Palm-only compression relaxation is unbounded, with an explicit feasible shell crossing beta already at `m=3,n=163`.
- **PROVED:** granular upward-mass inequality (5)-(6) for every Boolean spectral atom.
- **PROVED:** exact reduction (13)-(14) of full FEI to cancellation entropy `B_can`.
- **PROVED:** pure-level Boolean spectra satisfy `H<=2I-2`.
- **COMPUTATIONAL EVIDENCE ONLY:** `max B_can/I=1.4649755512` through `n=4` modulo global sign.
- **OPEN:** a universal dimension-free bound `B_can<=cI`, hence full FEI.
- **NOT CLAIMED:** novelty or publication priority. Fourier granularity is an established theme; the contribution here is the particular upward-mass/cancellation-entropy reduction assembled for this FEI route.
