# B13 FEI sprint — phase-aware block payment and a killed mixing shortcut

**Status:** full uniform-cube Fourier entropy-influence remains **OPEN / NOT PROVED**. This report proves one universal auxiliary inequality, proves its constant is sharp within Boolean functions, and refutes one natural stronger mixing lemma by an explicit Boolean pair.

**Execution label:** **WITHOUT_VERIFIED_BRAIN**. No authenticated mathematical/cognitive brain retrieval or receiver-context use occurred in this run.

**Route:** current account03/B13 cancellation/block-derivative assignment, compatible with APPROACHES 2, 13 and 14. This continues the preceding block-spectral-channel report rather than auditing the settled read-once certificate or repeating a finite sweep.

**No novelty claim:** all statements below are new-to-this-run deductions for the fleet. No publication-priority claim is made.

## 1. Exact universal statement attempted

Let the coordinates split as `X disjoint-union Y`, and let

`f : {-1,1}^{X union Y} -> {-1,1}`.

For each `A subseteq X`, write

`p_A = fhat(A)^2`,

`q_A = sum_{R subseteq Y} fhat(A union R)^2`.

Equivalently, if `c_A(y)=widehat{f_y}(A)` for the restriction to the `X` block, then

`p_A = (E_y c_A(y))^2`,

`q_A = E_y c_A(y)^2`.

Define the **coherent-to-incoherent phase loss**

`Phi_{X|Y}(f) = sum_{A subseteq X, p_A>0} p_A log2(q_A/p_A)`.

Also define the block spectral disturbance mass

`J_Y(f) = P_{S~fhat^2}[S intersects Y] = sum_{A subseteq X}(q_A-p_A)`.

The attempted universal statement was

`Phi_{X|Y}(f) <= c J_Y(f)`

with a dimension-independent best constant.

### Theorem (PROVED, sharp)

For every real function with Parseval-normalized Fourier-square law, hence in particular every Boolean `f`,

`Phi_{X|Y}(f) <= J_Y(f)/ln 2 <= I_Y(f)/ln 2`,

where `I_Y(f)=sum_{i in Y} Inf_i(f)=E|S intersect Y|`.

The constant `1/ln 2 = 1.4426950408889634...` is optimal even within Boolean functions.

This is a phase/cancellation payment that uses a true block quantity `J_Y`, not the sum of one-coordinate Palm relaxations.

## 2. Proof

For positive `x` and `y>=0`,

`x log2((x+y)/x) = x log2(1+y/x) <= y/ln 2`

by `ln(1+t)<=t`.

Apply this coordinatewise with `x=p_A` and `y=q_A-p_A>=0` (the latter is a sum of Fourier-square masses having a nonempty `Y` part):

`p_A log2(q_A/p_A) <= (q_A-p_A)/ln 2`.

Summing over `A subseteq X` gives

`Phi_{X|Y}(f) <= (1/ln2) sum_A(q_A-p_A)`
`               = J_Y(f)/ln2`.

Finally, `1[S intersects Y] <= |S intersects Y|`, so

`J_Y(f) <= E|S intersects Y| = I_Y(f)`.

No FEI assumption, monotonicity, read-once structure or induction hypothesis is used.

## 3. Exact block/correlation interpretation

Because rerandomizing all coordinates in `Y` kills every Fourier character intersecting `Y`,

`E[f(x) f(x^{(Y-rerand)})] = P[S avoids Y] = 1-J_Y(f)`.

Thus the sharp phase payment can be written directly from the block correlation profile:

`Phi_{X|Y}(f) <= [1 - Corr_Y(f)]/ln2`.

With the block-influence convention in which `Corr_Y=1-2 Inf_Y^{rerand}`, this is

`Phi_{X|Y}(f) <= 2 Inf_Y^{rerand}(f)/ln2`.

This identifies a genuine use of APPROACHES 2/13: the signed cancellation between the coherent coefficient `E c_A` and its local second moment `E c_A^2` is already paid by a single block correlation deficit.

## 4. Sharpness inside Boolean functions

Take even `k`, `N=2^k`, and the quadratic bent Boolean function

`h(x)=(-1)^{x1 x2 xor x3 x4 xor ... xor x_{k-1} x_k}`.

Let `h'` be obtained by flipping `h` at one input, and set

`f(x,y)=h(x)` for `y=0`, `f(x,y)=h'(x)` for `y=1`.

Here `Y={y}`. Writing the global Fourier decomposition as

`a_A=(hhat(A)+h'hat(A))/2`,

`b_A=(hhat(A)-h'hat(A))/2`,

we have

`p_A=a_A^2`, `q_A=a_A^2+b_A^2`, and

`J_Y=sum_A b_A^2=Inf_y(f)=1/N`.

Bentness gives `|hhat(A)|=N^{-1/2}`, while a one-point flip gives `|b_A|=N^{-1}` for every `A`. Hence `b_A^2/a_A^2=1/N+O(N^{-3/2})` uniformly away from the two asymptotic sign classes, and summing the Taylor expansion of `log(1+t)` yields

`Phi_{X|Y}(f) = 1/(N ln2) + O(N^{-3/2})`.

Therefore

`Phi_{X|Y}(f)/J_Y(f) -> 1/ln2`.

The attached reproducer gives:

| k | Phi/J |
|---:|---:|
| 2 | 1.092006960251363 |
| 4 | 1.385487979063102 |
| 6 | 1.430660838669879 |
| 8 | 1.439829575225781 |
| 10 | 1.441987618813369 |
| 12 | 1.442518744338173 |

The limit is `1/ln2 = 1.4426950408889634...`.

So even the stronger coefficient-1 claim `Phi<=J_Y` is **REFUTED** by a finite Boolean family.

## 5. Combination with the previous B13 magnitude-channel theorem

The preceding account03/B13 report proved, for the same block split and the local squared-spectrum channel `Y -> Z subseteq X`,

`I(Y;Z) <= (2/ln2) I_Y(f)`,

and showed `2/ln2` is sharp using the same bent one-point-flip family.

The new phase theorem controls the piece that that magnitude-channel theorem explicitly left unpaid. Consequently

`Phi_{X|Y}(f) + I(Y;Z) <= (3/ln2) I_Y(f)`.

The same Boolean family has the numerical ratios

| k | I(Y;Z)/J | Phi/J | joint/J |
|---:|---:|---:|---:|
| 2 | 2.195179762781594 | 1.092006960251363 | 3.287186723032956 |
| 4 | 2.805655914813947 | 1.385487979063102 | 4.191143893877049 |
| 6 | 2.869211287837629 | 1.430660838669879 | 4.299872126507508 |
| 8 | 2.881562254420487 | 1.439829575225781 | 4.321391829646267 |
| 10 | 2.884446418751395 | 1.441987618813369 | 4.326434037564765 |
| 12 | 2.885154992865864 | 1.442518744338173 | 4.327673737204037 |

For this one-bit block `J=I_Y`, and the joint ratio tends to

`3/ln2 = 4.328085122666891...`.

Thus the sum of the two proven block payments also has the sharp constant `3/ln2` for this decomposition.

This still does **not** prove FEI: the remaining difficulty is the upper-zeta mixing inside the projected spectral law.

## 6. Exact decomposition exposing the remaining obstruction

Let

`v_A = sum_{B subseteq X: B superset A} q_B`.

Because `q_B` already sums over every `Y` component,

`v_A = sum_{T superset A} p_T = u_A`

for every `A subseteq X`, where `u_A` is the global upward spectral mass.

For the part of cancellation entropy coming from atoms entirely inside `X`,

`T_X(f) = sum_{A subseteq X} p_A log2(u_A/p_A)`,

we therefore have the exact split

`T_X = Phi_{X|Y} + sum_A p_A log2(v_A/q_A)`.

Since `p_A<=q_A` and `v_A>=q_A`,

`sum_A p_A log2(v_A/q_A) <= sum_A q_A log2(v_A/q_A) = B_can(q)`,

where `B_can(q)` is the same upper-zeta functional applied to the projected law `q` on subsets of `X`.

Hence the proved block reduction is

`T_X(f) <= J_Y(f)/ln2 + B_can(q)`.

So the signed phase cancellation itself is no longer the obstacle for this partial block. The obstruction is now the nonlinear upper-zeta cancellation of the **projected mixture law** `q`.

## 7. Decisive dead route: JS does not pay the B_can mixing gap, even for Boolean spectra

A tempting next lemma would be

`B_can((P0+P1)/2) - [B_can(P0)+B_can(P1)]/2 <= JS(P0,P1)`

for spectra `P0,P1` of Boolean restrictions. If true, the previous `2/ln2` block information payment could absorb the projected-law mixing gap.

This statement is **REFUTED** by an explicit pair of 3-bit Boolean functions with truth tables, in lexicographic binary order,

`h0 = [1,-1,-1,-1, 1,1,1,-1]`,

`h1 = [1,-1,-1, 1,-1,1,1,-1]`.

Their spectral laws are exactly

`P0 = (1/4)(delta_{1}+delta_{2}+delta_{4}+delta_{7})`,

`P1 = delta_{7}`.

Thus

`B_can(P0)=3/4`, `B_can(P1)=0`,

while their midpoint law has masses `1/8` on `1,2,4` and `5/8` on `7`, so

`B_can((P0+P1)/2) = (3/8) log2 6 = 0.9693609377704335...`.

Therefore the B_can Jensen gap is exactly

`(3/8) log2 3 = 0.5943609377704335...`.

On the other hand

`JS(P0,P1) = 2 - (5/8) log2 5 = 0.5487949406953985...`.

The gap exceeds JS by

`0.04556599707503506... > 0`.

So the most direct attempt to pay projected B_can concavity by the already-controlled magnitude mutual information is dead, and it is dead on a genuine Boolean pair rather than an abstract random-set law.

## 8. What this run changes

- **PROVED:** sharp block phase payment `Phi_{X|Y} <= J_Y/ln2 <= I_Y/ln2`.
- **PROVED:** exact block-correlation form `Phi <= (1-Corr_Y)/ln2`.
- **PROVED:** partial cancellation reduction `T_X <= J_Y/ln2 + B_can(q)`.
- **PROVED / inherited plus new:** phase plus magnitude block losses are bounded by `(3/ln2) I_Y`; the bent one-point-flip family asymptotically saturates the sum for a one-bit outside block.
- **REFUTED:** coefficient `1` in `Phi<=J_Y`.
- **REFUTED:** `B_can` mixture Jensen gap `<= JS` even when both endpoints are genuine Boolean spectral laws.
- **OPEN:** a dimension-independent upper bound on full `B_can/I`.
- **OPEN:** full uniform-cube FEI.

## 9. Next attack

The next account03/B13 attack should target the exact residual `B_can(q)` for a projected mixture of Boolean spectra. The dead JS shortcut shows that ordinary channel mutual information is too small. Two concrete replacements are now natural:

1. seek a **zeta-weighted information divergence** whose Jensen gap is exactly or provably above the `B_can` mixing gap and whose one-coordinate/block increment can still be paid by Boolean disagreement; or
2. use a random upper-chain on the projected law `q`, but weight each merge by the block phase budget `q_A-p_A` so that a descendant Fourier atom is not charged once for every ancestor.

Any next candidate should first be tested against the explicit 3-bit pair above and the Numaro balanced-composition obstruction `B_can/(I-1)>=2.323994990262646786...`.

## 10. Reproduction

Run `reproduce_phase_block.py` in this directory with standard Python. It reproduces the bent-flip convergence table and the exact-support Boolean mixing counterexample. Floating point is used only to display logarithmic values; the support probabilities in the 3-bit counterexample are exact dyadic rationals and the analytic inequalities above are exact.
