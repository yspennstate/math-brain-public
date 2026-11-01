# B13 FEI creative run: exact random-chain information payment and a robust Boolean phase constraint

**Status:** PARTIAL. Full uniform-cube Fourier entropy-influence (FEI) remains **OPEN / NOT PROVED**.

**Run label:** `WITHOUT_VERIFIED_BRAIN`.

**Route:** current B13 sprint assignment (cancellation/random-chain payment), tied back to APPROACHES 2/13 (Boolean block/profile constraints). This run did not audit or rerun the settled read-once certificate.

## 1. Fresh dependencies and correction adopted

The fleet01/B12 cancellation handoff defined, for the spectral sample `S`,

`p_A = P(S=A)`, `u_A = sum_{B superset A} p_B`, and

`B_can = sum_A p_A log2(u_A/p_A)`.

It proved the granular upward-mass inequality and the exact reduction `H <= 2I + 2 B_can`. The later fleet03/B12 correction showed that the sharp scalar target `B_can <= (beta/2-1) I` is false (odd majority already crosses it), and replaced it by the uniform-prefix shadow process. I use that corrected process, not the refuted scalar closure.

For `a=|A|`, define

`v_A = sum_{B superset A} p_B / C(|B|,a)`.

Equivalently: sample `S`, uniformly order its elements, and ask for the unordered set of the first `a` elements. Then `v_A` is exactly the probability that this prefix is `A`.

The previous handoff proved

`B_sh := sum_A p_A log2(v_A/p_A) <= (log2 e) I`,

and the exact prefix identity

`H(S) = J + Br - E log2(K!)`, `K=|S|`,

where

`J = sum_A v_A h2(p_A/v_A)`

and

`Br = sum_A (v_A-p_A) H(r_A)`,

with

`r_A(i)=v_{A union {i}} / ((a+1)(v_A-p_A))` for `i notin A`.

## 2. PROVED: the factorial rebate is exactly a sum of local mutual informations

This is the main new random-chain identity.

Condition on the event that the unordered prefix is `A` and that the chain continues. Let `T_A` denote the final spectral set and `N_A` the next coordinate in the uniformly random ordering. Define

`MI_A = I(N_A ; T_A | prefix=A, continue)`.

Then

`Br - E log2(K!) = sum_A (v_A-p_A) MI_A`.                         (1)

### Proof

Given `prefix=A`, `continue`, and final set `B supersetneq A`, the next element is uniform on `B\A`; hence

`H(N_A | T_A=B, prefix=A, continue) = log2(|B|-a)`.

The probability mass of a particular final `B` at prefix `A` before conditioning on continuation is

`p_B / C(|B|,a)`.

Therefore

`(v_A-p_A) MI_A`
` = (v_A-p_A) H(r_A)`
`   - sum_{B supersetneq A} [p_B/C(|B|,a)] log2(|B|-a)`.

Sum over all `A`. For fixed `B`, `b=|B|`, and fixed prefix size `a<b`, there are `C(b,a)` subsets `A subset B`, so the second term contributes exactly

`p_B log2(b-a)`.

Summing `a=0,...,b-1` gives `p_B log2(b!)`. Summing `B` gives `E log2(K!)`, proving (1).

Thus the factorial rebate is not a mysterious global correction: it subtracts exactly the entropy of choosing the next coordinate that remains even after the final set is revealed. The residual branching term is pure information that the next coordinate carries about the unrevealed final spectral set.

## 3. PROVED: exact three-term entropy decomposition

Let

`C_cont := sum_A (v_A-p_A) log2(v_A/(v_A-p_A))`,

with zero terms omitted, and

`C_br := sum_A (v_A-p_A) MI_A`.

Since, for `s_A=p_A/v_A`,

`v_A h2(s_A) - p_A log2(1/s_A)`
` = (v_A-p_A) log2(v_A/(v_A-p_A))`,

we have `J-B_sh=C_cont`. Combining with (1) gives the exact identity

`H(S) = B_sh + C_cont + C_br`.                                  (2)

All three terms are nonnegative. The first is terminal surprisal, the second is continuation surprisal, and the third is branch/final-set mutual information.

This decomposition holds for **every** random subset law. Booleanity enters in paying the latter two terms by influence.

## 4. PROVED: for a Boolean spectral sample, continuation surprisal costs at most `2 I`

Let `p_0=p_empty=hat f(empty)^2` and `V=1-p_0=P(S nonempty)`.

For every nonempty `A`, writing `s=p_A/v_A`, the elementary inequality

`-(1-s) ln(1-s) <= s`

gives

`(v_A-p_A) log2(v_A/(v_A-p_A)) <= (log2 e) p_A`.

Hence all non-root prefixes contribute at most `(log2 e) V`.

At the root `A=empty`, `v_empty=1`, so the contribution is exactly

`V log2(1/V)`.

Therefore

`C_cont <= V [ log2(1/V) + log2 e ].`                            (3)

Now use Booleanity. Put

`theta = min(P[f=1],P[f=-1]) <= 1/2`.

Then

`V = Var(f) = 4 theta(1-theta)`.

The cube edge-isoperimetric inequality gives

`I(f) >= 2 theta log2(1/theta)`.                                 (4)

For `0<theta<=1/2`,

`V [ln(1/V)+1] <= 4 theta ln(1/theta)`.                           (5)

A short verification of (5): after dividing by `4 theta`, the difference between right and left is

`F(theta) = -theta ln theta + (1-theta) ln(1-theta) + (1-theta)(ln 4 - 1)`.

Its derivative is

`F'(theta) = -ln(4 theta(1-theta)) - 1`.

Since `4 theta(1-theta)` increases on `(0,1/2]`, `F'` crosses zero at most once, so the minimum of `F` is at an endpoint. The endpoint values are

`lim_{theta->0} F = ln 4 - 1 > 0`,

`F(1/2) = ln 2 - 1/2 > 0`.

Thus (5) holds. Combining (3)-(5), in bits,

`boxed:  C_cont <= 2 I(f).`                                      (6)

The constant `2` is asymptotically sharp already for a one-point defect. There `theta=2^{-n}`, `I=2 n theta`, and the **root term alone** satisfies

`V log2(1/V) / I -> 2`.

So this part of the chain cannot be improved below `2` by a universal scalar estimate.

## 5. New reduced full-FEI target: only branch/final-set information remains

The universal prefix-shadow bound and (6) inserted into (2) give

`boxed:  H(f) <= (2 + log2 e) I(f) + C_br(f).`                    (7)

Numerically, `2+log2 e = 3.442695040888963...`.

Therefore the sharp Hod/read-once candidate `beta(1/2)=6.4547837...` would follow from the single universal inequality

`C_br(f) <= (beta(1/2)-2-log2 e) I(f)`

`          = 3.0120886591... I(f).`                              (8)

I do **not** prove (8) here. Equation (7) is a rigorous dimension-free payment of every part of the prefix code except the information that a next spectral coordinate carries about the still-unrevealed final set. This isolates the remaining Booleanity obligation more cleanly than the refuted scalar `B_can` target.

For a level-symmetric law, `v_A=tau_a/C(n,a)` and the chain has an especially transparent form:

`C_br = H(S)-H(K) = E log2 C(n,K)`.

Using exact integer Fourier level masses for odd majority and floating logs only at the final evaluation gives:

- majority `n=13`: `C_br/I = 1.709528260912`;
- majority `n=151`: `C_br/I = 2.507259272418`;
- majority `n=251`: `C_br/I = 2.589784491191`.

These are stress tests only, not a proof of (8).

## 6. PROVED: a robust two-sided Boolean phase-balance constraint on the spectral profile

The prior B13 run proved exact product rigidity by a divisibility argument. Here is a different, robust necessary condition that survives perturbation and uses only Booleanity of `f`.

For every nonempty `U subseteq [n]`, Booleanity `f^2=1` gives the Fourier convolution identity

`0 = widehat{f^2}(U) = sum_A hat f(A) hat f(A triangle U)`.        (9)

Partition the involution `A -> A triangle U` into unordered pairs `P={A,A triangle U}` and set

`w_P = sqrt(p_A p_{A triangle U})`.

Equation (9) is a signed zero-sum of the pair weights. Consequently no one pair can outweigh all the rest:

`boxed:  2 max_P w_P <= sum_P w_P.`                              (10)

Equivalently, with the oriented Hellinger overlap

`Z_U = sum_A sqrt(p_A p_{A triangle U}) = 2 sum_P w_P`,

we have

`sqrt(p_A p_{A triangle U}) <= Z_U/4` for every `A`.              (11)

Thus whenever `Z_U>0`, the normalized overlap weights on the unordered `U`-pairs have maximum atom at most `1/2` and hence at least one bit of entropy. This is a genuine two-sided Booleanity constraint on the spectral profile, independent of dimension.

### Decisive limitation of this constraint

It is **not enough** for FEI by itself. Consider the abstract homogeneous product law with independent inclusion probability `q=1/n`, so `E|S|=1` but

`H(S)/E|S| = n h2(1/n) -> infinity`.

For a block `U` of size `k`, its largest normalized unordered-pair weight is

`2^{-(k-1)} (1-1/n)^{n-k}`.

For `n>=3`, this is `<1/2` for `k=1`, and is automatically `<=1/2` for every `k>=2`. Hence this high-entropy product law passes **every individual phase-polygon constraint (10)** even though the exact law cannot be a Boolean spectrum (by the previous exact product-rigidity theorem).

So the missing Boolean information is **joint consistency of the signs across different shifts `U`**, not the triangle condition for each autocorrelation equation separately. This precisely identifies what a successful APPROACH 2/13 inequality has to use.

## 7. What changed and next step

New proved statements this run:

1. `Br-E log2 K!` is exactly a sum of local mutual informations `C_br`, equation (1).
2. `H = B_sh + C_cont + C_br`, equation (2).
3. Boolean edge isoperimetry pays the whole continuation term sharply: `C_cont<=2I`, equation (6).
4. The only unpaid term in the resulting dimension-free chain proof is `C_br`, equation (7).
5. Every Boolean spectral profile obeys the robust phase-balance inequality (10), but the explicit `q=1/n` product calculation proves that imposing those inequalities shift-by-shift is insufficient.

The next nonduplicative attack should combine **joint** convolution identities for several shifts with `C_br`: condition on a prefix `A`, and use the simultaneous zero-autocorrelation system of the derivative/amplitude vector to bound `I(N_A;T_A)` rather than bounding `H(r_A)` alone. The target is a weighted inequality whose sum is at most about `3.0121 I`; any argument using only one shift at a time is now known to be too weak.

No novelty or publication-priority claim is made. Full FEI remains OPEN.
