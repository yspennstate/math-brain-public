# B17 FEI creative run — a dimension-free disjoint-branch MUX closure theorem

**Run:** `B17-20260921T124026Z-r30`  
**Status:** PARTIAL. Full Friedgut--Kalai Fourier entropy--influence conjecture remains **OPEN / NOT PROVED**.  
**Research label:** `WITHOUT_VERIFIED_BRAIN`.  
**Route:** APPROACH 7, with APPROACH 14 coding/entropy bookkeeping.  
**Fresh source state used:** `yspennstate/math-open-problems` master was refreshed during the run through `c4968a03f04b3f6674d6945e0bc30fe93e165562`.  
**No audit:** this run does not rerun the read-once certificate or the settled small-n sweeps.

## 1. Why this is a different mechanism

The previous fleet01/B17 sequence killed the raw sensitivity-set entropy route and the scalar Palm-size relaxation, then proved an antichain/high-floor spectral theorem. The current sprint asks fleet01/B17 for a coding/compression mechanism with Booleanity and specifically lists a larger composition/read-twice class as an acceptable primary route.

The operation studied here is a disjoint-branch multiplexer. Let `x` be a fresh selector bit, let `g:{-1,1}^A -> {-1,1}` and `h:{-1,1}^B -> {-1,1}`, with `A,B` disjoint, and define

\[
F(x,a,b)=
\begin{cases}
g(a),&x=+1,\\
h(b),&x=-1.
\end{cases}
\]

Equivalently,
\[
F=\frac{g+h}{2}+x\,\frac{g-h}{2}. \tag{1}
\]

In the AND/OR/NOT basis this is the usual MUX expression `(x AND g) OR ((NOT x) AND h)`, so the selector occurs twice. The three-bit example `MUX(x,y,z)` is not unate in `x`, hence it is not an AND/OR/NOT read-once function. Thus a closure theorem for (1) genuinely enlarges the certified AND/OR/NOT read-once class.

## 2. Exact Fourier bookkeeping

Write
\[
a=\widehat g(\varnothing)=\mathbb E g,\qquad
b=\widehat h(\varnothing)=\mathbb E h,
\]
and let
\[
\phi(t)=t\log_2(1/t),\quad \phi(0)=0.
\]

From (1), the Fourier coefficients of `F` are:

- at `emptyset`: `(a+b)/2`;
- at `{x}`: `(a-b)/2`;
- for every nonempty `S subseteq A`, two copies `ghat(S)/2`, on `S` and `S union {x}`;
- for every nonempty `T subseteq B`, two copies `hhat(T)/2`, on `T` and `T union {x}` (the second may carry a minus sign, irrelevant after squaring).

Therefore, with
\[
q_+=\frac{(a+b)^2}{4},\qquad q_-=\frac{(a-b)^2}{4},
\]
one gets the **exact identities**
\[
\boxed{
I(F)=\frac12 I(g)+\frac12 I(h)+j(a,b),
\qquad
j(a,b)=\frac{1-ab}{2},
} \tag{2}
\]
and
\[
\boxed{
H(F)=\frac12 H(g)+\frac12 H(h)+M(a,b),
} \tag{3}
\]
where
\[
M(a,b)
=(1-a^2)+(1-b^2)
+\phi(q_+)+\phi(q_-)
-\frac12\phi(a^2)-\frac12\phi(b^2). \tag{4}
\]

The selector charge `j(a,b)` has a direct Boolean meaning: if `G,H` are independent signs with means `a,b`, then
\[
j(a,b)=\Pr(G\ne H).
\]
So (3) asks whether the extra spectral description length created by the MUX can be paid by the probability that the two branches disagree.

## 3. PROVED: a universal scalar MUX charge

Define
\[
K_{\rm mux}
=
4+\frac{\gamma+2/e}{\ln2}
=
6.284948333490136\ldots,\qquad
\gamma=\frac{109+73\sqrt{73}}{864}. \tag{5}
\]

### Theorem 3.1

For every `a,b in [-1,1]`,
\[
\boxed{M(a,b)\le K_{\rm mux}\,j(a,b).} \tag{6}
\]

### Proof

Put
\[
D=1-ab=2j(a,b)
\]
and split
\[
M=(2-a^2-b^2)+N,
\]
with
\[
N=\phi(q_+)+\phi(q_-)-\frac12\phi(a^2)-\frac12\phi(b^2). \tag{7}
\]

First,
\[
2-a^2-b^2\le2(1-ab)=2D, \tag{8}
\]
because `(a-b)^2>=0`.

It remains to prove
\[
N\le \frac12\frac{\gamma+2/e}{\ln2}\,D. \tag{9}
\]

The numerator `N` depends only on `|a|,|b|`: changing the sign of one variable merely swaps `q_+` and `q_-`. The denominator `1-ab` is smallest when `a,b` have the same sign. Hence the worst ratio `N/D` occurs for `a,b>=0`.

Let
\[
x=a^2,\quad y=b^2,\quad
m=\frac{x+y}{2},\quad
\theta=\frac{x}{x+y},
\quad
r=2\sqrt{\theta(1-\theta)}.
\]
For `x+y>0`, the entropy grouping identity
\[
\phi(u)+\phi(v)=\phi(u+v)+(u+v)h_2\!\left(\frac{u}{u+v}\right)
\]
gives
\[
N=m\left[
1-h_2(\theta)
+h_2\!\left(\frac{1+r}{2}\right)
\right]
=:m\,A(\theta), \tag{10}
\]
while
\[
D=1-mr. \tag{11}
\]
Here `A(theta)>=0`. For fixed `theta`,
\[
\frac{N}{D}=\frac{mA(\theta)}{1-mr}
\]
is increasing in `m`. Subject to `a,b<=1`, its maximum is therefore attained when one of `a,b` equals `1`.

Take `b=1`, `a=1-2u`, `0<=u<=1/2`. Then `D=2u` and
\[
N=L(u)
=\phi((1-u)^2)+\phi(u^2)
-\frac12\phi((1-2u)^2). \tag{12}
\]

Write
\[
L=A_0+B_0,
\]
where
\[
A_0=\phi((1-u)^2)-\frac12\phi((1-2u)^2),
\qquad
B_0=\phi(u^2).
\]

For `0<=z<1`,
\[
-\ln(1-z)
\le z+\frac{z^2}{2(1-z)},
\qquad
-\ln(1-z)\ge z+\frac{z^2}{2}. \tag{13}
\]
Using the upper bound at `z=u` and the lower bound at `z=2u`,
\[
(\ln2)A_0
\le
u^2(3+u-8u^2)
=
u\,q(u),\qquad q(u)=u(3+u-8u^2). \tag{14}
\]
On `0<=u<=1/2`, the unique interior maximizer of `q` is
\[
u_*=\frac{1+\sqrt{73}}{24},
\]
and
\[
q(u_*)=\frac{109+73\sqrt{73}}{864}=: \gamma
=0.848046612740948\ldots.
\]
Hence
\[
A_0\le \frac{\gamma}{\ln2}\,u.
\]

Also
\[
B_0
=\frac{2u^2\ln(1/u)}{\ln2}
\le
\frac{2}{e\ln2}u, \tag{15}
\]
because `u ln(1/u)<=1/e`.

Thus
\[
L(u)\le
\frac{\gamma+2/e}{\ln2}\,u,
\]
and since `D=2u`, (9) follows. Combining (8) and (9),
\[
M
\le
\left(2+\frac12\frac{\gamma+2/e}{\ln2}\right)D
=
K_{\rm mux}\,j.
\]
QED.

## 4. Consequence: a strictly larger FEI-good class

### Corollary 4.1 — closure at any `C >= K_mux`

Suppose
\[
H(g)\le C I(g),\qquad H(h)\le C I(h)
\]
and `C>=K_mux`. Then their disjoint-branch MUX satisfies
\[
H(F)\le C I(F). \tag{16}
\]

Indeed, combine (2), (3), and (6):
\[
H(F)
\le
\frac C2(I(g)+I(h))+K_{\rm mux}j
\le
C\left[\frac12(I(g)+I(h))+j\right]
=CI(F).
\]

Therefore the class obtained by starting with any FEI-`K_mux` base class and repeatedly applying fresh-selector, variable-disjoint MUX gates is again FEI-`K_mux`.

In particular the already certified AND/OR/NOT read-once class satisfies `H<=6.4573 I`, hence it can be used as the base. Since `6.4573 > K_mux`, the MUX closure introduces **no loss at all** in the certified read-once constant. Thus it gives a strictly larger, generally non-unate class with
\[
\boxed{H(f)\le 6.4573\,I(f).} \tag{17}
\]

The current sprint also contains a rigorously certified shared-core lower-bound construction with
\[
C_{\rm FEI}>6.521850083658.
\]
Thus the certified constant in (17) is *below* the current universal lower bound. Consequently any current extremal witness above `6.521850083658` must use structure outside this branch-disjoint MUX closure of the certified read-once class.

This does **not** prove full FEI. It does, however, eliminate a nontrivial shared-selector/read-twice mechanism as the place where the current global obstruction lives.

## 5. Exact finite stress tests

The accompanying checker performs exact rational Walsh transforms for every pair of two-bit Boolean branch functions (`16 x 16 = 256` MUXes). It verifies the exact coefficient bookkeeping behind (2)--(4) and numerically checks (6).

Observed output:

- analytic MUX charge threshold: `6.284948333490136`;
- all `256` branch pairs: exact entropy/influence identity error `0`;
- largest overhead ratio among those branch pairs: `4.867668746754797`;
- dense `1001 x 1001` scalar grid: maximum `4.872318912079024`, near one branch constant and the other mean about `0.542`;
- the three-bit MUX has `H=2`, `I=3/2`, `H/I=4/3`.

The dense grid is only a stress test. The universal bound (6) is analytic.

## 6. What would kill or improve this route

The theorem is useful precisely because its charge is **summable under recursive disjoint-branch MUX composition**. It does not address shared variables between the two branches. The next test should therefore allow a controlled overlap set `R=A intersect B` and derive the exact correction to (2)--(3). A successful extension needs to charge the resulting Fourier-collision/Jensen--Shannon term by influence on the overlap without paying it once per branch.

A decisive obstruction would be an exact Boolean family with one shared branch variable for which the best overlap correction divided by the shared influence diverges. If that happens, pivot back to the global signed-autocorrelation/coding constraints from the preceding B17 runs rather than weakening (16) by a dimension-dependent term.

No publication-priority claim is made for this closure theorem without a literature search. The result here is a private proof mechanism/handoff for the FEI program.
