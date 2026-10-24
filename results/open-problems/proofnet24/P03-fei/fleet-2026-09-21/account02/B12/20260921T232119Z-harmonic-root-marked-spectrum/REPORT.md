# B12 FEI interface B — harmonic first-mark code, mixed-prefix Boolean constraints, and a genuine one-source rowwise obstruction

**Run:** `B12-20260921T232119Z-r11`  
**Status:** **PARTIAL. Full uniform-cube Friedgut--Kalai Fourier entropy--influence remains OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. Authorized GitHub control/scientific artifacts were read, but no authenticated mathematical-brain receiver/context was used.  
**Claim level:** universal analytic lemmas plus a genuine Boolean counterfamily and bounded exhaustive diagnostics. No novelty or publication-priority claim.

## 0. Why this run changes mechanism

The later execution reset `FEI-JOINT-FOUR-ACCOUNTS-2026-09-21-192650Z` asks B12 to attack the missing **marked-spectrum / harmonic entropy estimate from one Boolean source**, rather than treating derivative rows as arbitrary independent objects.

The last three substantive account02/B12 reports were:

1. `20260921T211150Z-component-factorial-harmonic-capacity/REPORT.md` (scientific commit `62e2a41bd9ba8bde36e9c6d2cf7c51f9116dc84e`): reciprocal-component internal address entropy is factorial-paid, and a symmetric harmonic trigger capacity is paid nonreusably by actual prefix KL; component-label/exception entropy remains.
2. `20260921T175134Z-physical-erasure-budget/REPORT.md`: exact physical-erasure / dual-total-correlation conservation and near-subcube Palm stability, but small TV plus small mean excess does not control rare address entropy.
3. `20260921T165622Z-depth-rigidity-obstruction/REPORT.md`: depth-only Palm constraints admit an abstract unbounded-loss surrogate, while equality for genuine Boolean derivative rows is rigid.

Those reports leave the same qualitative warning: a proof cannot finish by assigning each derivative row its own independent depth/entropy bill. This run therefore abandons another row-local stability estimate and instead exposes the spectral sample by a **single global random ordering**. The first mark has a harmonic law coupled across every row of the same Boolean source.

### Named completed other-account result consumed

The substantive peer input is account01/B12:

`proofnet24/P03-fei/fleet-2026-09-21/account01/B12/20260921T231256Z-conditional-count-code/REPORT.md`, scientific commit `ffcc39e48292c19a053da6741586e0165a6b72b5`.

It proves the exact conditional ordered-code identity

\[
H(Y\mid T)=H(K\mid T)+\mu H(q)-\mathbb E\log_2(K!)-\mu I_2(L;T,K,P),
\]

the universal component-count collapse

\[
H(Y\mid T)\le H(N\mid T)+\sum_C(E_C-Q_C),
\]

and, on fine closed reciprocal components, the dimension-free bound

\[
H(Y\mid T)\le 6.605753562722450\,\mathbb E|Y|.
\]

Its partial-coverage form leaves the non-fine/nonclosed sector as an explicit singleton-address term `sum_i h_2(p_i)`. The results below are used against exactly that interface: **if the residual branch object is still the squared Fourier spectrum of one Boolean function, the first unresolved address does not need to be encoded by independent singleton marginals.** A global harmonic first-mark code costs at most `4.858823 I`, regardless of the ambient number of exceptional coordinates. The continuation remains nontrivial and is isolated exactly below.

A compatible secondary input is account03/B13 `20260921T2303Z-factorial-component-routing/REPORT.md`, commit `7275779497df5c018827458b03acd07672809742`, which confirms that logarithmic component-local routing addresses are factorial-paid under the natural influence-weighted component selector while raw trigger-size payment is false. The present mechanism works before choosing a component: it codes the first global spectral mark.

## 1. Normalization and the harmonic first mark

Let

\[
f:\{-1,1\}^n\to\{-1,1\},\qquad
p_B:=\widehat f(B)^2,
\]

so `sum_B p_B=1`. Let `S` denote the spectral sample with `P(S=B)=p_B`, and

\[
I(f)=\sum_B |B|p_B=\sum_i j_i,
\qquad
j_i:=\operatorname{Inf}_i(f)=\sum_{B\ni i}p_B.
\]

For a coordinate `i`, define the first-order uniform-prefix shadow

\[
v_i:=\sum_{B\ni i}\frac{p_B}{|B|}.
\tag{1.1}
\]

Sample `S`. If `S` is nonempty, choose a uniformly random ordering of its members and let `J` be the first coordinate. If `S=emptyset`, set `J=bot`. Then

\[
\Pr(J=i)=v_i,
\qquad
\Pr(J=\bot)=p_\varnothing=\widehat f(\varnothing)^2.
\tag{1.2}
\]

Moreover

\[
\sum_i v_i=\sum_{B\ne\varnothing}p_B=\operatorname{Var}(f).
\tag{1.3}
\]

Thus `J` is a genuine single-source address variable, not an independently assembled family of row labels.

## 2. Universal theorem: the first harmonic mark has influence-relative entropy

Write the removed derivative

\[
g_i:=D_if,
\]

with the standard cube normalization

\[
D_if(x_{\setminus i})=\frac{f(x_i=1)-f(x_i=-1)}2.
\]

Because `f` is Boolean,

\[
g_i\in\{-1,0,1\},
\qquad
\|g_i\|_2^2=j_i,
\qquad
\widehat g_i(T)=\widehat f(T\cup\{i\}).
\tag{2.1}
\]

### Lemma 2.1 — hypercontractive harmonic-mass bound

For every `0<j_i<=1`,

\[
\boxed{
\frac{v_i}{j_i}
\le
\int_0^1 j_i^{(1-t)/(1+t)}\,dt
\le
\min\left(1,\frac{2}{\ln(1/j_i)}\right).
}
\tag{2.2}
\]

The rightmost fraction is interpreted as `+infinity` when `j_i=1`.

#### Proof

For `0<=t<=1`, Bonami--Beckner with `rho=sqrt(t)` gives

\[
\sum_T t^{|T|}\widehat g_i(T)^2
=\|T_{\sqrt t}g_i\|_2^2
\le \|g_i\|_{1+t}^2.
\]

Since `|g_i|` is an indicator of its support,

\[
\|g_i\|_{1+t}^2=j_i^{2/(1+t)}.
\tag{2.3}
\]

Also `1/(|T|+1)=int_0^1 t^{|T|}dt`, hence

\[
v_i
=\int_0^1\sum_T t^{|T|}\widehat g_i(T)^2dt
\le\int_0^1j_i^{2/(1+t)}dt.
\]

Divide by `j_i`. If `lambda=ln(1/j_i)`, then after the substitution `u=(1-t)/(1+t)`,

\[
\int_0^1j_i^{(1-t)/(1+t)}dt
=\int_0^1\frac{2e^{-\lambda u}}{(1+u)^2}du
\le\min\left(1,\frac2\lambda\right).
\]

QED.

### Theorem 2.2 — harmonic root-code theorem

Let

\[
C_{\rm harm}:=\frac2{\ln2}\left(1+\frac1{2e}\right)
=3.4161279272009697\ldots
\]

and

\[
C_{\rm root}:=C_{\rm harm}+\frac1{\ln2}
=4.8588229680899335\ldots .
\]

Then for every Boolean `f`,

\[
\boxed{
H(J)\le C_{\rm root}\,I(f).
}
\tag{2.4}
\]

In particular, the entire first spectral-coordinate address, including the empty-spectrum symbol, has a dimension-independent expected Shannon budget.

#### Proof

Write `psi(x)=x log_2(1/x)` with `psi(0)=0`, and let

\[
L_i:=\log_2(1/j_i),\qquad c:=\frac2{\ln2}.
\]

If `j_i>=1/8`, then `v_i<=j_i`. If `j_i<=1/e`, monotonicity of `psi` on `[0,1/e]` gives

\[
\psi(v_i)\le\psi(j_i)=j_iL_i\le3j_i.
\]

If `j_i>1/e`, the global maximum `psi(x)<=1/(e ln2)` is also less than `3j_i`.

If `j_i<1/8`, Lemma 2.1 gives

\[
v_i\le \frac{cj_i}{L_i}=:u_i<1/e.
\]

Hence

\[
\frac{\psi(v_i)}{j_i}
\le c\left(1+\frac{\log_2(L_i/c)}{L_i}\right).
\tag{2.5}
\]

For `L>0`, the last quotient is maximized at `L=ec`, with value `1/(2e)`. Thus in both regimes

\[
\psi(v_i)\le C_{\rm harm}j_i.
\tag{2.6}
\]

Summing gives

\[
\sum_i\psi(v_i)\le C_{\rm harm}I(f).
\tag{2.7}
\]

For the empty atom, the elementary inequality `p ln(1/p)<=1-p` gives

\[
\psi(p_\varnothing)
\le\frac{1-p_\varnothing}{\ln2}
=\frac{\operatorname{Var}(f)}{\ln2}
\le\frac{I(f)}{\ln2}.
\tag{2.8}
\]

Using (1.2), `H(J)=psi(p_emptyset)+sum_i psi(v_i)`, proving (2.4). QED.

### What this does to the account01/B12 frontier

The account01 partial-coverage theorem leaves non-fine/nonclosed coordinates as separate marginal address costs. Whenever the residual object under consideration is still one Boolean squared spectrum, (2.4) shows that **the first unresolved global address can instead be encoded as one harmonic mark for `<=4.858823 I` bits in expectation**. No ambient alphabet size, number of exceptional rows, or independent-row continuity term occurs.

This does not by itself encode the terminal spectral set. The exact continuation is next.

## 3. Exact harmonic recursion: the remaining implication is global and one-source

Conditional on `J=i`, write `T=S\setminus\{i\}`. From the first-mark experiment,

\[
q_i^{\rm H}(T)
:=\Pr(T\mid J=i)
=\frac{p_{T\cup\{i\}}}{(|T|+1)v_i}.
\tag{3.1}
\]

Thus the continuation law is not the ordinary normalized derivative spectrum; it has the harmonic factor `1/(|T|+1)`.

### Theorem 3.1 — exact one-step harmonic entropy recursion

\[
\boxed{
H(f)
=H(J)+\sum_i v_i H(q_i^{\rm H})
-\mathbb E_p[\mathbf1_{\{|S|>0\}}\log_2|S|].
}
\tag{3.2}
\]

#### Proof

Given nonempty `S`, the first member of its random ordering is uniform in `S`, so

\[
H(S,J)=H(S)+\mathbb E[\mathbf1_{|S|>0}\log_2|S|].
\]

On the other hand, `J=bot` forces `S=emptyset`, while (3.1) is the conditional remainder law for `J=i`. Hence

\[
H(S,J)=H(J)+\sum_i v_i H(q_i^{\rm H}).
\]

Equate the two expressions. QED.

Combining Theorems 2.2 and 3.1, full FEI would follow from a universal constant `C_cont` such that

\[
\boxed{
\sum_i v_i H(q_i^{\rm H})
-\mathbb E_p[\mathbf1_{\{|S|>0\}}\log_2|S|]
\le C_{\rm cont}I(f).
}
\tag{3.3}
\]

The critical point is that all `q_i^H` in (3.3) arise from the **same Boolean source**. The next sections identify a higher-prefix Boolean constraint and show why a row-by-row replacement of (3.3) is false even under genuine Boolean realizability.

## 4. Higher marked prefixes retain a quantized mixed-derivative constraint

For nonempty `A subseteq[n]`, let `a=|A|` and

\[
h_A:=D_Af,
\qquad
w_A:=\|h_A\|_2^2
=\sum_{B\supseteq A}p_B.
\tag{4.1}
\]

Because `f` is `plus/minus 1`-valued, its iterated normalized difference satisfies

\[
h_A(x)\in 2^{1-a}\mathbb Z\cap[-1,1].
\tag{4.2}
\]

In particular every nonzero value has magnitude at least

\[
\delta_A:=2^{1-a}.
\tag{4.3}
\]

Define the uniform-prefix shadow

\[
v_A:=\sum_{B\supseteq A}\frac{p_B}{\binom{|B|}{a}}.
\tag{4.4}
\]

This is exactly the probability that the unordered first `a` entries of a uniform ordering of `S` equal `A`.

### Lemma 4.1 — quantized mixed-derivative noise bound

For every `0<=t<=1`,

\[
\boxed{
\sum_T t^{|T|}\widehat f(A\cup T)^2
\le
w_A\,[4^{a-1}w_A]^{(1-t)/(1+t)}.
}
\tag{4.5}
\]

#### Proof

Bonami--Beckner gives

\[
\sum_Tt^{|T|}\widehat h_A(T)^2
\le\|h_A\|_{1+t}^2.
\]

Since `1+t<=2` and every nonzero `|h_A|>=delta_A`,

\[
|h_A|^{1+t}\le\delta_A^{t-1}|h_A|^2.
\]

Therefore

\[
\|h_A\|_{1+t}^2
\le(w_A\delta_A^{t-1})^{2/(1+t)}
=w_A(w_A\delta_A^{-2})^{(1-t)/(1+t)},
\]

and `delta_A^{-2}=4^{a-1}`. QED.

### Theorem 4.2 — sparse mixed-prefix shadow bound

Put

\[
\theta_A:=4^{a-1}w_A.
\]

If `theta_A<1` and `lambda_A=ln(1/theta_A)`, then

\[
\boxed{
\frac{v_A}{w_A}
\le
\min\left(1,\ a!\left(\frac2{\lambda_A}\right)^a\right).
}
\tag{4.6}
\]

In particular, if `lambda_A>=4a`, then

\[
\boxed{v_A\le2^{-a}w_A.}
\tag{4.7}
\]

#### Proof

For `B=A union T`, the beta-integral identity is

\[
\frac1{\binom{a+|T|}{a}}
=a\int_0^1s^{a-1}(1-s)^{|T|}ds.
\tag{4.8}
\]

Insert (4.5) with `t=1-s`:

\[
\frac{v_A}{w_A}
\le a\int_0^1s^{a-1}\theta_A^{s/(2-s)}ds.
\]

Since `s/(2-s)>=s/2`,

\[
\frac{v_A}{w_A}
\le a\int_0^\infty s^{a-1}e^{-\lambda_As/2}ds
=a!\left(\frac2{\lambda_A}\right)^a.
\]

The trivial bound `v_A<=w_A` supplies the minimum with 1. If `lambda_A>=4a`, then `a!<=a^a` gives (4.7). QED.

**Meaning.** The harmonic continuation in (3.3) is not an arbitrary family of subset laws. Every marked prefix inherits a quantitative constraint from the quantized mixed derivative of the same Boolean source. This is a concrete input for a multilevel code, though no summation theorem strong enough for (3.3) is proved here.

## 5. Decisive counterexample: a rowwise harmonic FEI is false even inside one genuine Boolean source

A tempting next step would be to prove (3.3) by bounding each harmonic derivative row separately. The following genuine Boolean family rules out that route.

Let `m=2r+1` be odd and let

\[
M_m(y)=\operatorname{sgn}\left(\sum_{k=1}^m y_k\right),
\qquad
g(y)=\frac{1+M_m(y)}2\in\{0,1\}.
\]

Define

\[
\boxed{f_m(x_0,y)=1-g(y)+x_0g(y).}
\tag{5.1}
\]

This is Boolean and

\[
D_0f_m=g.
\tag{5.2}
\]

Let

\[
\tau_r:=\binom{2r}{r}4^{-r}.
\]

For majority,

\[
\widehat g(\varnothing)=\frac12,
\qquad
\widehat g(\{k\})=\frac{\tau_r}{2}\quad(1\le k\le m).
\tag{5.3}
\]

For this derivative row define harmonic masses

\[
r_T:=\frac{\widehat g(T)^2}{|T|+1},
\qquad
V:=\sum_Tr_T,
\qquad
J_{\rm H}:=\sum_T|T|r_T,
\]

and its unnormalized harmonic Shannon contribution

\[
\mathcal H_{\rm H}(g)
:=\sum_{T:r_T>0}r_T\log_2\frac{V}{r_T}.
\tag{5.4}
\]

Since `||g||_2^2=1/2`,

\[
V\le\frac12,
\qquad
J_{\rm H}\le\frac12,
\qquad
V+J_{\rm H}\le1.
\tag{5.5}
\]

But the singleton terms alone give

\[
\mathcal H_{\rm H}(g)
\ge
\frac{m\tau_r^2}{8}\log_2\frac{2}{\tau_r^2}.
\tag{5.6}
\]

Indeed each singleton has harmonic mass `tau_r^2/8`, while the empty harmonic mass is `1/4`, so `V/(tau_r^2/8)>=2/tau_r^2`.

The elementary central-binomial bounds

\[
\frac1{2\sqrt r}\le\tau_r\le\frac1{\sqrt r}
\tag{5.7}
\]

imply

\[
\frac{m\tau_r^2}{8}\ge\frac1{16},
\qquad
\log_2\frac2{\tau_r^2}\ge\log_2(2r).
\]

Therefore

\[
\boxed{
\mathcal H_{\rm H}(D_0f_m)
\ge\frac1{16}\log_2(2r)\longrightarrow\infty,
\qquad
V+J_{\rm H}\le1.
}
\tag{5.8}
\]

Consequently there is no universal constant `C` for a rowwise theorem of the form

\[
\mathcal H_{\rm H}(D_if)\le C(V_i+J_{{\rm H},i})
\]

for every derivative row of every Boolean function. This is not an arbitrary-row relaxation: `g` is literally a derivative of the Boolean function (5.1).

This counterexample is compatible with the possibility of (3.3), because the other derivative rows and the global source influence of `f_m` can carry the missing payment. It proves that the continuation must exploit **cross-row compatibility / common-source Booleanity**, exactly as the execution reset requires.

## 6. Exact global prefix process (useful handoff identity)

The shadows `v_A` define the full unordered-prefix Markov tree. At a prefix `A`, `a=|A|`, the stopping probability is

\[
\Pr(\text{stop at }A\mid A)=\frac{p_A}{v_A},
\tag{6.1}
\]

and for `i notin A`,

\[
\Pr(\text{next mark }i\mid A)
=\frac{v_{A\cup\{i\}}}{(a+1)v_A}.
\tag{6.2}
\]

Indeed

\[
\frac1{a+1}\sum_{i\notin A}v_{A\cup\{i\}}=v_A-p_A.
\tag{6.3}
\]

Multiplying transitions along an ordering of a terminal set `S` gives exactly `p_S/|S|!`. Hence

\[
H(S)+\mathbb E\log_2(|S|!)
\]

is the Shannon cost of this single-source prefix tree. Theorem 2.2 controls the root node uniformly; Theorem 4.2 constrains sparse deeper nodes; Section 5 proves that summing independent row bounds at those nodes is not valid.

This is the concrete object for the next B12 attack: a **global prefix-tree Kraft / information payment using the coupled shadows `v_A`**, with factorial order already present as an exact rebate.

## 7. Finite diagnostics

The adjacent standard-library checker exhaustively evaluates all nonconstant Boolean functions through dimension four and separately evaluates the controlled-majority derivative family.

It reports:

- nonconstant Boolean functions through `n=4`: `65,804`;
- nonzero mixed prefixes: `943,372`;
- Bonami/quantization moment checks at `t=1/4,1/2,3/4`: `2,830,116`;
- sparse-shadow checks: `521,936`;
- maximum observed `H(J)/I`: `2.5086205845070944`;
- maximum moment-bound excess: `0.0`;
- maximum sparse-shadow-bound excess: `0.0`;
- controlled-majority `H_H/(V+J_H)` rises from `1.0638101559` at `m=3` to `1.6514954736` at `m=15`;
- canonical result digest: `96599015be5a0d03b2c4a58824338ccd95c3213f3d2d9ca11a2d4839050c00ef`.

These are diagnostics only. The universal claims above are algebraic/analytic and do not rely on finite enumeration.

## 8. FULL-PROBLEM CHANGE

**Before this run.** The latest own interface-B result paid reciprocal-component internal identity by the factorial bank and paid a nonreused harmonic trigger capacity by actual prefix KL, but component-label/exception entropy remained. The newest account01/B12 count-code theorem then eliminated macro/interleaving entropy on the fine closed sector, while leaving non-fine/nonclosed rows as separate singleton-address costs `sum h_2(p_i)` and leaving the global physical/reveal frontier open.

**After this run.** Full FEI is still **OPEN / NOT PROVED** and no dimension-independent FEI constant is claimed. However, the rank-one marked-spectrum address is no longer an unpaid ambient singleton-marginal object when it comes from one Boolean squared spectrum:

\[
H(J)\le4.8588229680899335\,I(f).
\]

The exact remaining one-source implication is now

\[
\boxed{
\sum_i v_i H(q_i^{\rm H})
-\mathbb E[\mathbf1_{|S|>0}\log_2|S|]
\le C_{\rm cont} I(f)
}
\tag{8.1}
\]

for some universal finite `C_cont`, or any stronger global code implying it. Every deeper marked prefix satisfies the quantized mixed-derivative constraint (4.5)--(4.7). A rowwise reduction of (8.1) to independent harmonic derivative-row entropy is now rigorously refuted by the genuine Boolean controlled-majority family (5.1).

So the full-problem movement is **not a new FEI constant**; it is the removal of the first global address layer and a strict localization of the surviving obstruction to cross-row/common-source continuation information.

## 9. MECHANISM CHANGE

**Previous mechanism:** reciprocal-trigger graph contraction, factorial component routing, near-subcube stability, and row/edge harmonic-capacity payments.

**Mechanism executed here:** expose the actual global spectral sample by one uniform random ordering; pay its first mark via a hypercontractive harmonic integral; represent all deeper prefixes by the coupled shadow family `v_A`; inject Booleanity through the quantization of the true mixed derivatives `D_A f`; and test the natural rowwise continuation bridge on a genuine controlled-majority Boolean source.

This is materially different from another depth, TV, raw-pair, rank, or l1 estimate. It also explains precisely why the next proof step must be global: the first mark is cheap, the deeper marked laws are constrained, but a single derivative row may have logarithmically unbounded harmonic entropy relative to its own local harmonic mass/depth.

## 10. Next exact target

Attack the full prefix-tree identity (6.1)--(6.3), not independent derivative rows. A sufficient next theorem would be a multilevel Kraft/Carleson inequality of the form

\[
\sum_A \text{(prefix mass)}\times\text{(new coordinate entropy at A)}
\le C I(f)+\mathbb E\log_2(|S|!),
\]

where the same factorial bank is spent only once and sparse nodes are controlled through (4.6), while dense nodes are amortized by actual descendant mass. Any candidate must be checked against the controlled-majority construction above, parity, one-point defects, addressing, and amplified high-ratio seeds.

**Full unrestricted FEI remains OPEN / NOT PROVED.**
