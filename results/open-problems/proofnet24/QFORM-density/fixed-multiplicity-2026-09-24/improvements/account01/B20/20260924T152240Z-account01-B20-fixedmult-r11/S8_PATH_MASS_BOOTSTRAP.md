# `s_8` endpoint bootstrap: favorable-seed amplification forces large `V_2`

Run: `20260924T152240Z-account01-B20-fixedmult-r11`
Parent source blob: `19fb119877426b640b2c0dae19ec2f78a399fe11`.
Status: **proved structural strengthening; it does not by itself prove the eight-eigenvalue density theorem**.

This note combines the volume-sampled interpolation error with the two-hub determinant-amplification lemma from the companion B20 note.

Work in the normalized no-pivot `s_8(A)>=1` endpoint and put
\[
d=\frac3{40},\qquad \kappa=\frac4{625},\qquad
x:=V_2(A),\qquad v:=V_3(A).
\]
The existing `k=2` spectral-to-volume theorem gives
\[
x\ge\kappa^2. \tag{1}
\]
If `v>=kappa^3`, the existing order-three receiver already pays. Hence assume
\[
v<\kappa^3. \tag{2}
\]

## 1. A mass-amplification inequality

For an invertible ordered disjoint two-seed `(S,T)`, let
\[
e(S,T):=\|E^{S,T}\|_F
\]
be the interpolation off-diagonal error from the manuscript's completion lemma, and set
\[
w(S,T):=\det(A_{S,T})^2.
\]
The volume-sampling identity/inequality gives
\[
\frac1x\sum_{S\cap T=\varnothing}w(S,T)e(S,T)^2
\le \frac{9v}{x}. \tag{3}
\]
(The zero-determinant seeds have zero weight.)

Fix `epsilon>0` with
\[
\epsilon<\frac12\left(1-d-\frac1{11}\right). \tag{4}
\]
Define the favorable seed set
\[
\mathcal F_\epsilon=\{(S,T):e(S,T)<\epsilon\}.
\]
By weighted Markov,
\[
\sum_{\mathcal F_\epsilon}w(S,T)
\ge x\left(1-\frac{9v}{\epsilon^2x}\right), \tag{5}
\]
whenever the parenthesis is positive.

For every favorable seed, the global completion rank is at most six. Therefore
\[
s_2(D)>1-\epsilon.
\]
Choose deterministically two exterior coordinates `H={h_1,h_2}` on which
`|D_{hh}|>1-epsilon`. Exactly as in the two-hub lemma,
\[
|P_{hh}|>1-d-\epsilon,
\qquad
|P_{h_1h_2}|,|P_{h_2h_1}|<\frac1{11}+\epsilon.
\]
Hence
\[
|\det P_{H,H}|>q(\epsilon), \tag{6}
\]
where the **exact affine function after difference of squares** is
\[
q(\epsilon)
:= (1-d-\epsilon)^2-\left(\frac1{11}+\epsilon\right)^2
=\left(1-d-\frac1{11}-2\epsilon\right)
 \left(1-d+\frac1{11}\right)>0. \tag{7}
\]
Writing
\[
U=A_{S,H},\qquad C=A_{H,T},\qquad B=A_{S,T},
\]
gives
\[
w(S,H)w(H,T)
=|\det U\det C|^2
>q(\epsilon)^2w(S,T). \tag{8}
\]

Now sum over favorable seeds. The deterministic choice of `H` makes the map
`(S,T) -> (S,H,T)` injective. Therefore its image is a subset of all ordered pairwise-disjoint two-set paths. Since `A` is symmetric, `w(S,H)=w(H,S)`, and
\[
\begin{aligned}
 x^2
 &=\left(\sum_{S\cap H=\varnothing}w(S,H)\right)^2\\
 &\ge \sum_H\left(\sum_{S:S\cap H=\varnothing}w(S,H)\right)^2\\
 &\ge \sum_{S,H,T\ \mathrm{pairwise\ disjoint}}w(S,H)w(H,T)\\
 &\ge q(\epsilon)^2\sum_{\mathcal F_\epsilon}w(S,T).
\end{aligned} \tag{9}
\]
Combining (5) and (9), and cancelling `x>0`, proves the bootstrap inequality
\[
\boxed{
 x\ge q(\epsilon)^2
 \left(1-\frac{9v}{\epsilon^2x}\right)
}\tag{10}
\]
for every `epsilon` satisfying (4) and making the parenthesis positive.

This is dimension-free. It is stronger than the existence of one favorable seed because it uses the **whole volume-sampled seed mass** and the injective two-arm path it creates.

## 2. Explicit bootstrap under the unpaid `V_3<kappa^3` endpoint

Starting only from (1)–(2), iterate (10) using rational `epsilon` values. All arithmetic below is exact before the displayed decimals.

### First step: `epsilon_1=7/20`

Here
\[
q(7/20)=\frac{26373}{193600},
\qquad
1-\frac{9\kappa^3}{(7/20)^2\kappa^2}=\frac{649}{1225}.
\]
Thus
\[
x>
\frac{41036572611}{4174016000000}
=0.00983143634595555\ldots . \tag{11}
\]

### Second step: `epsilon_2=1/20`

Insert (11) into the denominator on the right side of (10). Since
\[
q(1/20)=\frac{144381}{193600},
\]
one obtains
\[
x>0.5027854219139453. \tag{12}
\]
(The exact favorable-mass factor at this step is
`2576213674299/2849761986875`.)

### Third step: `epsilon_3=1/80`

Using (12),
\[
q(1/80)=\frac{39783}{48400},
\]
and (10) gives
\[
x>0.6553327666246669. \tag{13}
\]

### Fourth step: `epsilon_4=1/87`

Using (13),
\[
q(1/87)=\frac{4626301}{5614400},
\]
and the exact rational evaluation of (10) gives
\[
\boxed{V_2(A)=x>0.6604843294068005.} \tag{14}
\]
For reference, the exact fourth-step lower bound is
\[
\frac{579102903724039065459170645936649737111}
{876785228567266153745909086040000000000}.
\]

Hence the unpaid `s_8`, no-pivot, small-`V_3` chamber cannot have merely the tiny baseline `V_2>=kappa^2=0.00004096`: its disjoint order-two volume is forced above `0.66048`.

## 3. Consequences and the remaining analytic obstruction

The overlap theorem immediately sharpens to
\[
W^{\times}_{2,1}
\ge 2V_2-9V_3
>1.32096-9\kappa^3
>1.32095. \tag{15}
\]
So any still-unpaid `s_8` state has simultaneously:

1. tiny disjoint order-three volume `V_3<kappa^3`;
2. very large disjoint order-two volume `V_2>0.66048`;
3. very large overlap-one bordered-minor mass `W^{\times}_{2,1}>1.32095`;
4. for a large fraction of its `V_2`-weighted seeds, two determinant-amplifying physical arms.

This sharply identifies the endpoint as an **alignment/shared-coordinate analytic problem**, rather than a lack of algebraic volume. It also explains why a single maximum-determinant seed is the wrong object: the useful information is a weighted mass-transfer inequality over all seeds.

Equation (14) does **not** by itself yield a density bound. The current source has a marginal-free receiver for disjoint `V_3`, but no corresponding product-preserving receiver that consumes the overlap mass in (15), where one original coordinate belongs to both the row and column side of a bordered minor. Producing such a receiver, or converting a positive fraction of (15) into genuinely disjoint third-order volume without losing the arbitrary product-law scope, remains the first closure obligation for `s_8`.

Eight eigenvalues therefore remain **OPEN** in this note; nine remains the complete candidate threshold.
