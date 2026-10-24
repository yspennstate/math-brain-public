# account01/B14 improvement — exact constant sharpening and quantitative terminal good-seed mass

Run: `20260924T121442Z-account01-B14-fixedmult-auto11`  
Pinned manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

Status: **proved improvements/obstructions; multiplicity remains 17.** No 16-direction theorem and no full three-eigenvalue theorem is claimed.

## 1. Same-proof constant improvement

Let

`L0 = 4 + 4 log 16`.

In the nine-direction remainder proposition, the scalar-pivot truncated half-potential is actually

\[
H(Q)\le 10(8+3L_0)=200+120\log 16.
\]

The other branches are smaller:

\[
12\sqrt{80e}<177
\]

in the no-pivot branch,

\[
40\pi<126
\]

for a definite pair, and

\[
10(32+4\log16)+4/e<433
\]

for an indefinite pair. Hence the full nine-direction negative half potential is bounded by

\[
\boxed{
M_9:=201+120\log16=533.7106466687\ldots .
}
\]

At the main scalar pivot, `|a_ii|>=eta=1/100`, so

\[
\|p_Q\|_\infty\le 10M_9
=2010+1200\log16
=5337.1064666877\ldots .
\]

All other main branches are smaller (`800e`, `10pi`, and the manuscript's `<251` indefinite-pair bound). Therefore the manuscript proof itself yields the sharper replacement theorem

\[
\boxed{
\|p_{X^TAX+b^TX+c}\|_\infty
\le (2010+1200\log16)\frac{K^2}{s}
<5340\frac{K^2}{s}
}
\]

whenever `s_17(A)>=s>0`. No additional assumption is introduced.

## 2. Where multiplicity 17 is actually spent

The pivot branches are not the threshold bottleneck:

- a main scalar pivot needs only nine surviving Schur directions, so `s_10>=1` would already suffice for that branch;
- an indefinite physical pair needs one surviving Schur direction, so `s_3>=1` suffices for that branch;
- a definite physical pair needs no surviving spectrum.

The fixed multiplicity 17 is spent entirely in the **no-pivot order-five crossing-volume branch**. The current spectral-to-volume proposition at order `k=5` uses `4k-3=17`. The analytic determinant receiver has tail exponent `k/4`, so order four gives only the endpoint `|t|^{-1}`, not an absolutely integrable characteristic function. Thus a valid `17 -> 16` improvement must already improve the terminal `r=4` structural count at order five (or replace the analytic endpoint mechanism entirely).

## 3. Quantitative terminal `s_16` good-seed mass lemma

This strengthens the terminal information available from the existing sampled-interpolation argument.

Assume the no-pivot order-five setup, `s_16(A)>=1`, and

\[
R:=V_5(A)/V_4(A)<\kappa=1/80^2=1/6400.
\]

For each nonsingular order-four seed `(S,T)` let `F_{S,T}` be the off-diagonal residual from the manuscript's interpolation lemma and set

\[
\epsilon_{S,T}:=\|F_{S,T}\|_F.
\]

Under the volume-sampling law

\[
\Pr(S,T)=\det(A_{S,T})^2/V_4(A),
\]

the sampling proof gives

\[
\mathbb E\epsilon_{S,T}^2\le25R<25\kappa=1/256.
\tag{1}
\]

Hence, for every `t>0`, Markov gives

\[
\Pr\{\epsilon_{S,T}\le t\}
>1-\frac{1}{256t^2}.
\tag{2}
\]

Now take

\[
\frac1{16}<t<\frac{193}{2800}=0.06892857\ldots .
\tag{3}
\]

For every seed with `epsilon<=t`, the completion satisfies

\[
s_{16}(D+R)\ge1-t,
\qquad \operatorname{rank}R\le12.
\]

Thus `D` has at least four diagonal entries of modulus `>=1-t`. Five such entries would contradict `rank R[L,L]<=4` by the same diagonal-dominance argument because

\[
1-t-1/100>4(1/7+t)
\]
throughout (3). Therefore the terminal chamber has exactly four large entries; call their index set `H`.

On `H`, using `D_ii=A_ii-P_ii`, the no-pivot entry bound and `|E_ij|<=epsilon<=t`,

\[
|P_{ii}|\ge1-t-1/100,
\qquad
|P_{ij}|<1/7+t\quad(i\ne j).
\]

The row/column diagonal-dominance margin is therefore

\[
\delta(t):=1-\frac1{100}-\frac37-4t
=\frac{393}{700}-4t.
\tag{4}
\]

Condition (3) is exactly strong enough to imply

\[
\delta(t)>2/7.
\]

Consequently `P[H,H]` is invertible and

\[
|\det P[H,H]|\ge\delta(t)^4.
\tag{5}
\]

Write

\[
b=|\det A[S,T]|,
\quad c=|\det A[H,T]|,
\quad e=|\det A[S,H]|.
\]

The factorization `P[H,H]=A[H,T]A[S,T]^{-1}A[S,H]` gives

\[
ce/b=|\det P[H,H]|.
\tag{6}
\]

Every entry of the disjoint cross minors is off-diagonal and hence `<1/7`; Hadamard gives

\[
c,e\le(2/7)^4.
\tag{7}
\]

Combining (5)--(7) yields separately

\[
\boxed{
 c\ge\alpha(t)b,\qquad e\ge\alpha(t)b,\qquad
 \alpha(t):=\left(\frac{\delta(t)}{2/7}\right)^4>1.
}
\tag{8}
\]

Thus a **positive volume-weight proportion** of terminal seeds are not merely good: each such seed forces two strictly heavier neighboring disjoint order-four minors.

### Explicit clean choice

Take

\[
t=17/256.
\]

Then from (2)

\[
\Pr\{\epsilon\le17/256\}
>1-\frac{256}{289}
=\frac{33}{289}
=0.11418685\ldots .
\]

Moreover

\[
\delta=\frac{3313}{11200},
\qquad
\frac{\delta}{2/7}=\frac{3313}{3200},
\]

so every seed in this `>11.4%` volume-weight set has two neighbors with

\[
\boxed{
 c,e\ge\left(\frac{3313}{3200}\right)^4 b
=1.1489095257\ldots\, b.
}
\]

In determinant-square volume weight, each such neighbor is at least

\[
1.3199930984\ldots
\]

times heavier than the source seed.

This is stronger than the mere existence of one baseline `epsilon<=1/16` seed: it produces a quantitatively positive mass of ascent-capable seeds while retaining strict ascent.

## 4. Why this still does not prove `s_16`

The neighboring heavier seeds in (8) are not known to satisfy the same residual-ratio bound. The directed ascent relation can have unbounded indegree as dimension grows, so strict weight ascent plus a positive mass of good seeds alone does not give a dimension-free contradiction. I found no legitimate way to charge all good-seed weight to bad terminal seeds without an additional exchange/Pluecker estimate or a transfer theorem for the residual ratio.

A second route, replacing the order-five receiver by order four, also does not close: the audited determinant theorem gives only `|phi(t)|=O(|t|^{-1})` from `Z_4`, which is not `L1`, and cap-one rough laws admit no uniform scalar Fourier `L^p` estimate below `p=2` that would permit the naive lower-power BL repair.

Therefore the lowest multiplicity rigorously proved in this run remains

\[
\boxed{17}.
\]

Any theorem stated with 16 or fewer directions remains **GAP** until either (i) the terminal good-seed/heavier-neighbor relation is transferred to another good seed with controlled multiplicity, (ii) the exact terminal saturation is ruled out by a new structural identity, or (iii) a genuinely new order-four endpoint receiver is proved.
