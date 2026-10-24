Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED.** No authenticated maximum-effort metadata is exposed.

# NM13-02 T01 — dyadic-gap one-exception recombination and unequal flat-tail hereditary closure

## 0. Parent scope/bound versus mechanism gain

**Parent problem.** Friedgut--Kalai Fourier entropy--influence (FEI): find a universal finite constant `C` such that

\[
H(\widehat f^{\,2})\le C I(f)
\]

for every Boolean sign function on every finite uniform cube.

**Parent status before -> after:** **OPEN -> OPEN**.

**Unrestricted universal finite constant before -> after:** **UNKNOWN -> UNKNOWN**.

The current primary-source status was checked again in this run. González--MacManus--Pereyra, arXiv:2606.00246, still formulate universal FEI as a conjecture and state that their one-step restriction inequality would imply full FEI if it held for every Boolean function. Li--Han, arXiv:2512.03117, still prove the sharpened general bound with the additional coordinate-profile term `sum_i I_i log(1/I_i)`; this is not a universal `C I(f)` theorem.

**Newest P03 obstruction recovered.** The current P03 handoff is

`proofnet24/P03-fei/continuations/2026-09-20-flat-tail-and-arithmetic-drift/HANDOFF.md`

(blob `440d976984b4030cb0439e8bdbaed8abe9eee87f`). It reports, pending later independent review, a direct `<4` FEI theorem when all nonzero Fourier coefficients away from one label have one common magnitude, plus a `6+log2(R+1)` theorem for finitely many exceptional frequency labels. It also records exact failures of several arithmetic-remainder selector proposals and leaves a dimension-independent treatment of **arbitrary unequal Boolean Fourier weights** as the universal obstruction.

The immediately preceding NM13-02 report proved universal spectral-TV allocation and exact/constant Hellinger payment when sibling spectra are toggle-compatible or have only one amplitude-drift fibre. It explicitly left **two one-exception flat-tail children with different tail magnitudes** UNPROVED, because every common tail-support frequency then becomes a drift fibre.

This run closes that specific hereditary recombination gap. The new theorem is stronger than the flat-tail statement:

> **One-exception 2-separated recombination.** If, away from one residual Fourier label `e`, every common-support magnitude pair is either equal or differs by a factor at least two (zero/nonzero pairs are also allowed), then
> \[
> \boxed{B_i(f)\le 8M_i(f)\le 8j_i(f).}
> \]

For Boolean one-exception flat-tail children, unequal tail magnitudes are automatically distinct powers of two, so the factor-two separation is automatic. Equal tails retain the preceding sharper `4j_i` theorem. Thus every common-exception one-flat-tail sibling pair, including unequal tails, has a dimension-free hereditary payment.

The mechanism is applied unconditionally to a new finite-field graph selector family in which the two children have nested flat Fourier tails of amplitudes differing by `2^{2(n-m)}`, while the parent has several unequal nontrivial spectral scales. A full physical tree satisfies

\[
\boxed{R_T(F_{m,n})\le 8 I(F_{m,n})}
\]

for every `1<=m<n`. The child direct bounds needed for that application are rederived below, so the application does not assume P03's reported one-exception theorem.

Full FEI is not claimed. The remaining obstruction includes many common-support fibres with unequal ratios in `(1,2)` and/or several uncontrolled exceptional drift fibres; the mass-conservation argument below no longer pays those cases.

---

## 1. Controlling policy, current assignment, exclusions, compact handoff

The controlling owner policy is `operations/PROGRESS20_2026-09-20.md`, blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`. LIVE20 assigns NM13-02 to T01 hereditary entropy/recombination theory paired with P03. Root `POSTED.md` was checked for exclusions; no posted/retired claim is reintroduced here.

Prior NM13-02 mathematics is preserved with its original hypotheses. In particular:

- exact quadratic-rank allocation and quadratic hereditary leaves;
- one- and two-affine-flat classes and bounded arrangement certificates;
- hybrid decision-tree / nested-spine recursion;
- variance-paid physical separators;
- quadratic-normalized Wiener control;
- derivative spectral-flat selectors and oblique derivative payment;
- character-child endpoint cross-fibre payment;
- complete physical-block compression;
- multiway Fourier-orthogonal label splicing;
- bidirectional biquadratic block selection;
- hereditary dependency-bank routing;
- the previous universal spectral-TV inequality `B_i<=TV`, exact toggle payment `B_i=2M_i`, and one exceptional drift-fibre bound `B_i<=4M_i`.

The restricted fresh-control theorem remains restricted to appended fresh controls and is not a fixed-domain proof of FEI. The false pointwise-erasure converse, fixed-coefficient affine drift, all-coordinate absolute-overlap selector, derivative-degree scalar schedule, blind curvature payment, fixed-Renyi payment, frozen-parent endpoint payment, marginal-entropy substitution, arbitrary orthogonal-involution relaxation, and P03's newly refuted arithmetic-selector constants remain retired.

The only earlier NM13-02 fact used for the final tree graft is **complete-block compression**: any Boolean leaf `u` admits a full physical query tree with hereditary allocation at most `H(u)`. This converts a direct leaf entropy bound into a hereditary leaf bound without requiring the leaf class to remain closed under further restrictions.

P03's newest positive theorems are treated as peer reports pending later independent review. The project-conditional corollary in Section 6 states what follows if their direct `<4` one-exception theorem survives review, but the explicit finite-field theorem in Section 7 is independent of that peer claim.

---

## 2. One split: allocation and Hellinger notation

Let `i` be a physical coordinate and let `g,h` be the two Boolean restrictions after fixing `i`. For every residual Fourier label `T`, set

\[
u_T=\widehat g(T),\qquad v_T=\widehat h(T),\qquad
x_T=|u_T|,\quad y_T=|v_T|.
\]

The two parent coefficients in the fibre over `T` are

\[
\widehat f(T)=\frac{u_T+v_T}{2},\qquad
\widehat f(T\cup\{i\})=\frac{u_T-v_T}{2}.
\]

The hereditary allocation at the split is

\[
B_i(f)=H(S_i\mid S_{[n]\setminus\{i\}})
      =\sum_T \Phi(x_T,y_T),
\tag{2.1}
\]

where

\[
\Phi(x,y)=\frac{x^2+y^2}{2}
 h_2\!\left(\frac{(x-y)^2}{2(x^2+y^2)}\right),
\qquad \Phi(0,0)=0.
\tag{2.2}
\]

Define the child-spectrum Hellinger defect

\[
M_i(f)=\frac14\sum_T(x_T-y_T)^2.
\tag{2.3}
\]

As preserved from the previous report,

\[
M_i(f)\le j_i(f):=\min\{\operatorname{Inf}_i(f),1-\operatorname{Inf}_i(f)\}.
\tag{2.4}
\]

For completeness, triangle inequality and Parseval give

\[
\sum_Tx_Ty_T\ge\left|\sum_Tu_Tv_T\right|
=|\langle g,h\rangle|
=|1-2\operatorname{Inf}_i(f)|,
\]

and (2.4) follows from (2.3).

The new work is to control (2.1) directly by (2.3) when many common-support amplitudes differ but have a multiplicative gap.

---

## 3. Three scalar estimates

Throughout, entropy is in bits. For `0<p<=1/2`,

\[
h_2(p)=p\log_2(1/p)+(1-p)\log_2(1/(1-p)).
\]

The elementary inequality `-ln(1-p)<=p/(1-p)` gives

\[
\boxed{h_2(p)\le p\log_2(1/p)+\frac p{\ln2}.}
\tag{3.1}
\]

We also use the strict elementary bound

\[
\ln2>\frac23,
\qquad\text{hence}\qquad
\frac1{\ln2}<\frac32.
\tag{3.2}
\]

One proof of (3.2) is to use the tangent line to the convex function `1/x` at `x=3/2` on `[1,2]`; strict convexity puts `1/x` strictly above that tangent off the contact point, and the tangent integrates to `2/3`.

For a nonzero fibre put

\[
s=x^2+y^2,\qquad d=|x-y|,\qquad
p=\frac{d^2}{2s}\in[0,1/2].
\tag{3.3}
\]

Then

\[
\Phi(x,y)=\frac s2h_2(p),\qquad d^2=2ps,
\tag{3.4}
\]

and

\[
|x^2-y^2|=2s\sqrt{p(1-p)}.
\tag{3.5}
\]

### Lemma 3.1 — a factor-two amplitude gap is quadratically cheap

If `xy=0`, or if `x,y>0` and `max(x,y)/min(x,y)>=2`, then

\[
\boxed{\Phi(x,y)\le\frac54(x-y)^2.}
\tag{3.6}
\]

#### Proof

For `xy=0`, `p=1/2`. Otherwise write `r=max(x,y)/min(x,y)>=2`. Then

\[
p=\frac{(r-1)^2}{2(r^2+1)}\ge\frac1{10},
\]

because

\[
5(r-1)^2-(r^2+1)=2(2r-1)(r-2)\ge0.
\]

For `p>=1/10`, (3.1)--(3.2) give

\[
h_2(p)
\le p\left(\log_2 10+\frac1{\ln2}\right)
<5p.
\]

Indeed `log_2 10<7/2` since `10^2<2^7`, and `1/ln2<3/2`. Insert this into (3.4):

\[
\Phi\le\frac s2(5p)=\frac54d^2.
\]

QED.

### Lemma 3.2 — a very small exceptional mismatch is paid by squared-mass drift

If `p<1/64`, then

\[
\boxed{h_2(p)\le\sqrt{p(1-p)}}
\tag{3.7}
\]

and hence

\[
\boxed{\Phi(x,y)\le\frac14|x^2-y^2|.}
\tag{3.8}
\]

#### Proof

From (3.1), it is enough to show

\[
\sqrt p\left(\log_2(1/p)+\frac1{\ln2}\right)\le\sqrt{1-p}.
\tag{3.9}
\]

The left side is

\[
\frac{\sqrt p\,[\ln(1/p)+1]}{\ln2}.
\]

The numerator `sqrt(p)[ln(1/p)+1]` has derivative `[ln(1/p)-1]/(2sqrt p)`, hence is increasing throughout `(0,1/64]`. Therefore the left side of (3.9) is at most

\[
\frac18\left(6+\frac1{\ln2}\right)<\frac{15}{16}.
\]

But for `p<=1/64`,

\[
\sqrt{1-p}\ge\frac{\sqrt{63}}8>\frac{15}{16},
\]

because `63>225/4`. This proves (3.7). Equation (3.8) follows from (3.4)--(3.5).

QED.

### Lemma 3.3 — a non-tiny exceptional mismatch is Hellinger-quadratic

If `p>=1/64`, then

\[
\boxed{\Phi(x,y)\le\frac{15}{8}(x-y)^2.}
\tag{3.10}
\]

#### Proof

By (3.1)--(3.2) and `p>=1/64`,

\[
h_2(p)
\le p\left(6+\frac1{\ln2}\right)
<\frac{15}{2}p.
\]

Use (3.4) and `d^2=2ps`:

\[
\Phi\le\frac s2\cdot\frac{15}{2}p
=\frac{15}{8}d^2.
\]

QED.

---

## 4. Main theorem: one-exception 2-separated hereditary recombination

### Definition 4.1

A child pair `(g,h)` is **2-separated away from `e`** if, for every residual Fourier label `T!=e`, at least one of the following holds:

1. `x_T=y_T`;
2. `x_Ty_T=0`;
3. `max(x_T,y_T)/min(x_T,y_T)>=2`.

Thus equal common-support amplitudes cost nothing; unequal common-support amplitudes must be separated by a factor at least two; arbitrary behaviour is allowed at the single exceptional label `e`.

### Theorem 4.2 — one-exception 2-separated payment

If `(g,h)` is 2-separated away from one label `e`, then

\[
\boxed{B_i(f)\le8M_i(f)\le8j_i(f).}
\tag{4.1}
\]

#### Proof

Put

\[
A=\sum_{T\ne e}(x_T-y_T)^2,
\qquad
W=\sum_{T\ne e}|x_T^2-y_T^2|,
\qquad
z=(x_e-y_e)^2.
\tag{4.2}
\]

Every nonzero term off `e` obeys Lemma 3.1, so

\[
\sum_{T\ne e}\Phi(x_T,y_T)\le\frac54A.
\tag{4.3}
\]

Moreover, for every off-exception fibre with a nonzero difference,

\[
\frac{|x_T^2-y_T^2|}{(x_T-y_T)^2}
=\frac{x_T+y_T}{|x_T-y_T|}\le3.
\tag{4.4}
\]

This is immediate for a zero/nonzero pair, and for a positive ratio `r>=2` it is `(r+1)/(r-1)<=3`. Hence

\[
W\le3A.
\tag{4.5}
\]

Both child squared Fourier laws have total mass one, so mass conservation at the exceptional fibre gives

\[
|x_e^2-y_e^2|
=\left|\sum_{T\ne e}(y_T^2-x_T^2)\right|
\le W\le3A.
\tag{4.6}
\]

Let `p_e` be the value in (3.3) for `(x_e,y_e)`.

**Case 1: `p_e<1/64`.** Lemma 3.2 and (4.6) give

\[
\Phi(x_e,y_e)
\le\frac14|x_e^2-y_e^2|
\le\frac34A.
\]

Together with (4.3),

\[
B_i(f)\le\left(\frac54+\frac34\right)A=2A
\le2(A+z)=8M_i(f).
\]

**Case 2: `p_e>=1/64`.** Lemma 3.3 gives

\[
\Phi(x_e,y_e)\le\frac{15}{8}z.
\]

Hence

\[
B_i(f)
\le\frac54A+\frac{15}{8}z
\le2(A+z)=8M_i(f).
\]

Finally use (2.4). QED.

### Remarks

1. The theorem is not a finite-dimensional statement; the proof is all-dimensional and purely analytic.
2. The constant eight was chosen for a clean proof, not claimed sharp. The checker below sees substantially smaller ratios in all tested cases.
3. The single exceptional fibre is essential to the mass-conservation step (4.6). With two uncontrolled exceptional fibres, their signed squared-mass changes can cancel while their absolute drift remains large.
4. The factor-two gap is also essential to this proof. If many common-support ratios approach one, the quotient `(x+y)/|x-y|` in (4.4) diverges.

---

## 5. Boolean flat tails automatically satisfy the multiplicative-gap hypothesis

### Lemma 5.1 — binary-unit tail quantization

Let `u` be a nonconstant Boolean sign function. Suppose that, after moving one exceptional Fourier label to zero by a character twist, every nonzero Fourier coefficient away from zero has one common magnitude `a>0`. Then

\[
\boxed{a=2^{-k}}
\]

for an integer `k>=1`.

#### Proof

Write

\[
u(x)=c+aV(x),
\]

where `V` is an integer-valued sum of characters with coefficients `+/-1`. Since `u` is nonconstant Boolean, it takes both values `+1` and `-1`; subtracting two values gives

\[
2=a\,[V(x)-V(y)],
\]

so `2/a` is an integer.

Every Fourier coefficient of a Boolean function is dyadic. Write `a=q2^{-k}` in lowest terms with `q` odd. Then

\[
\frac2a=\frac{2^{k+1}}q\in\mathbb Z,
\]

forcing the odd integer `q` to divide a power of two; hence `q=1`. The noncharacter case has `k>=1`.

QED.

### Corollary 5.2 — common-exception one-flat-tail siblings

Suppose both Boolean children have the same exceptional Fourier label `e`, and away from `e` each child has at most one nonzero Fourier magnitude. Then

\[
\boxed{B_i(f)\le8j_i(f).}
\tag{5.1}
\]

If the two tail magnitudes agree, the preceding NM13-02 one-exception theorem retains the sharper

\[
B_i(f)\le4j_i(f).
\tag{5.2}
\]

#### Proof

If a child has no tail, it is a character supported at the exceptional label and the 2-separated condition is immediate. Otherwise Lemma 5.1 makes its tail magnitude a power of two. Two distinct powers of two differ by a factor at least two, while equal powers produce zero-drift common fibres. Theorem 4.2 applies.

QED.

This is the precise extension left open in the preceding NM13-02 report: different flat-tail amplitudes may overlap on arbitrarily many frequencies, yet their Boolean dyadic quantization prevents the dangerous near-equal regime.

---

## 6. Dependent-branch hereditary closure

### Theorem 6.1 — 8-hereditary closure of 2-separated one-exception stopping trees

Consider a finite physical stopping tree. Assume every internal split is 2-separated away from one residual Fourier label in the sense of Definition 4.1. Assume each stopping leaf `u` has a direct certificate

\[
H(f_u)\le K I(f_u)
\]

for one constant `K<=8`. Then there is a full physical restriction tree extending the stopping tree with

\[
\boxed{R_T(f)\le8I(f).}
\tag{6.1}
\]

#### Proof

Complete-block compression turns each direct leaf certificate into a full leaf tree with allocation at most `K I(f_u)<=8I(f_u)`. Work backward. If a node queries `i` and its two child continuations already cost at most eight times their influences, Theorem 4.2 and the exact influence decomposition give

\[
\begin{aligned}
R_{\text{node}}
&\le B_i(f)+\frac{R_g+R_h}{2}\\
&\le8j_i(f)+4[I(g)+I(h)]\\
&\le8\operatorname{Inf}_i(f)+4[I(g)+I(h)]\\
&=8I(f).
\end{aligned}
\]

QED.

### Project-conditional P03 splice

P03 currently reports a direct coefficient `<4` for every one-exception flat-tail Boolean function. If that peer theorem survives later independent review, then Corollary 5.2 and Theorem 6.1 imply hereditary coefficient eight for any dependent stopping tree whose internal sibling pairs are common-exception one-flat-tail functions, even when their tail magnitudes vary from branch to branch. This sentence is **PROJECT-CONDITIONAL**; it is not used in the unconditional application below.

---

## 7. Unconditional application: quotient/full finite-field graph selectors with unequal nested tails

The point of this example is to realize the new mechanism on nonaffine children whose tail supports overlap heavily while their tail amplitudes differ.

### 7.1 The basic graph phase

Let `q=2^r`, identify an `r`-bit block with `F_q`, and define

\[
G_r(x,z,y)=1-2\,1_{\{y=xz\}},
\qquad x,z,y\in\mathbb F_q.
\tag{7.1}
\]

Use additive characters `psi(t)=(-1)^{Tr(t)}`. At frequency `(alpha,beta,gamma)`, the graph-indicator transform is

\[
q^{-3}\sum_{x,z}\psi(\alpha x+\beta z+\gamma xz).
\]

If `gamma=0`, this vanishes unless `alpha=beta=0`. If `gamma!=0`, summing in `z` forces `x=-beta/gamma`, leaving one term of magnitude `q/q^3=q^{-2}`. Therefore

\[
\widehat G_r(0)=1-\frac2q,
\tag{7.2}
\]

and every nonzero Fourier coefficient has either magnitude zero or

\[
\boxed{a_r=\frac2{q^2}=2^{1-2r}.}
\tag{7.3}
\]

The tail support is exactly

\[
\{(\alpha,\beta,\gamma):\gamma\ne0\},
\]

of size

\[
N_r=q^2(q-1).
\tag{7.4}
\]

Thus `G_r` is a genuine one-exception flat-tail function, but its negative set is the nonlinear multiplication graph, not an affine flat for `r>=2`.

### 7.2 Exact influence and an independent direct entropy bound

For any physical bit in the `y` block, toggling that bit adds a fixed nonzero field element to `y`, so exactly two `y` values per `(x,z)` lie on exactly one of the two graph equations. Hence each `y` bit has influence `2/q`.

For a bit in the `x` block, toggling adds a nonzero `delta` to `x`. If `z=0` the two graph equations agree; if `z!=0`, their right sides differ and again exactly two `y` values cause a sign change. Thus each `x` bit has influence

\[
\frac{2(q-1)}{q^2},
\]

and the same holds in the `z` block. Therefore

\[
\boxed{I(G_r)=\frac{6r}{q}-\frac{4r}{q^2}.}
\tag{7.5}
\]

Let

\[
c=1-\frac2q,\qquad p_0=c^2,\qquad
s=1-p_0=\frac{4(q-1)}{q^2}.
\]

By (7.3)--(7.4),

\[
H(G_r)=-p_0\log_2p_0+s(4r-2).
\tag{7.6}
\]

Since `-p_0 ln p_0<=1-p_0=s`,

\[
H(G_r)\le s\left(4r-2+\frac1{\ln2}\right).
\tag{7.7}
\]

Comparing (7.7) with `(8/3)I(G_r)` and multiplying by `q^2` leaves the positive difference

\[
\frac{16r}{3}+4\left(2-\frac1{\ln2}\right)(q-1)>0.
\]

Hence, independently of P03's direct theorem,

\[
\boxed{H(G_r)<\frac83 I(G_r).}
\tag{7.8}
\]

### 7.3 Lift a smaller graph into a larger ambient cube

Fix `1<=m<n`. On each of the three `n`-bit blocks choose the coordinate projection

\[
\pi:\mathbb F_2^n\to\mathbb F_2^m
\]

onto the first `m` bits, identify the quotient with `F_{2^m}`, and define

\[
\widetilde G_{m,n}(x,z,y)
=G_m(\pi x,\pi z,\pi y).
\tag{7.9}
\]

Its Fourier transform is the ordinary lift of the `G_m` transform: it vanishes unless all three frequency blocks lie in the dual `m`-dimensional coordinate subspace, and on that subspace it equals the corresponding coefficient of `G_m`. Therefore its tail amplitude is

\[
a_m=2^{1-2m}
\]

and its tail support is a subset of the tail support of the full `G_n`, because every lifted tail frequency has nonzero `y`-frequency and the full `G_n` support contains **all** frequencies with nonzero `y`-frequency.

The two children consequently have the same exceptional label zero, nested tail supports, and amplitude ratio

\[
\boxed{\frac{a_m}{a_n}=2^{2(n-m)}\ge4.}
\tag{7.10}
\]

The common-support mismatch is exactly the many-fibre unequal-amplitude geometry that the preceding NM13-02 report left open.

### 7.4 Add a physical selector

Define on one selector bit `b` plus the three ambient `n`-bit blocks

\[
F_{m,n}(b,x,z,y)=
\begin{cases}
\widetilde G_{m,n}(x,z,y),&b=0,\\
G_n(x,z,y),&b=1.
\end{cases}
\tag{7.11}
\]

At the root selector split, Theorem 4.2 gives

\[
B_b(F_{m,n})\le8j_b(F_{m,n})\le8\operatorname{Inf}_b(F_{m,n}).
\tag{7.12}
\]

After that split, query all residual coordinates in each child. Complete-block compression and (7.8) give child costs at most `(8/3)I`. Therefore

\[
\begin{aligned}
R_T(F_{m,n})
&\le8\operatorname{Inf}_b(F_{m,n})
 +\frac43\bigl[I(\widetilde G_{m,n})+I(G_n)\bigr]\\
&\le8\left(\operatorname{Inf}_b(F_{m,n})
 +\frac{I(\widetilde G_{m,n})+I(G_n)}2\right)\\
&=8I(F_{m,n}).
\end{aligned}
\]

Thus

\[
\boxed{R_T(F_{m,n})\le8I(F_{m,n})\quad\text{for all }1\le m<n.}
\tag{7.13}
\]

This is an all-dimensional analytic hereditary theorem, not an extrapolation from the checker.

### 7.5 Why the parent is genuinely multiscale

Let `u=a_n/2=2^{-2n}`. On tail frequencies belonging to `G_n` but not to the lifted `G_m`, the two parent coefficients have magnitude exactly `u`. On each of the `N_m=2^{2m}(2^m-1)` overlapping tail labels, the two parent magnitudes are

\[
\frac{a_m+a_n}{2}
=u\left(2^{2(n-m)}+1\right),
\qquad
\frac{a_m-a_n}{2}
=u\left(2^{2(n-m)}-1\right),
\tag{7.14}
\]

both strictly larger than `u` and distinct. Hence the parent is not itself a one-exception flat-tail function; it has several nontrivial scales.

If one applies P03's newest generic few-exception sufficient theorem directly to this parent, its number `R_exc` of frequency labels larger than the unit `u` satisfies at least

\[
R_{\rm exc}\ge2N_m=2^{2m+1}(2^m-1).
\tag{7.15}
\]

Thus that generic sufficient coefficient is at least

\[
6+\log_2(R_{\rm exc}+1)=3m+O(1),
\]

whereas the dependent-branch hereditary certificate (7.13) stays at eight. This is a comparison of available sufficient certificates, not a claim that P03 has no other representation of `F_{m,n}`.

---

## 8. What failed / what remains

The new theorem does **not** control arbitrary unequal Boolean Fourier weights. Its proof uses two rigid features:

1. **one exceptional fibre**, so total squared-mass conservation converts the exceptional drift into the aggregate off-exception drift; and
2. **factor-two separation** away from that fibre, so squared-mass drift and Hellinger-square drift are comparable.

For a general Boolean spectrum, dyadic coefficients can have odd numerators. Distinct magnitudes such as `(2r+1)2^{-k}` and `(2r+3)2^{-k}` can have ratios arbitrarily close to one as `r` grows. On many such common-support fibres, `(x+y)/|x-y|` is large, and (4.4) gives no constant. Likewise, with several exceptional fibres, signed mass changes can cancel among exceptions and (4.6) breaks.

So this run does **not** prove a universal bound on P03's arithmetic remainder `D`, does not rescue the refuted prescribed-coordinate `D` selector, and does not settle FEI. The arithmetic-selector failures in P03 remain valid corrections.

The next nonredundant attack should therefore target one of two strictly narrower gaps:

- a **multiscale grouping lemma** that bundles many near-equal dyadic amplitudes and pays their aggregate common-support drift without summing a logarithmic number of scales; or
- a **multi-exception signed-cancellation ledger** that replaces the single-fibre mass conservation step by a branch-stable transport/coupling quantity.

A useful stress test is a sibling pair with many common support labels carrying adjacent odd dyadic numerators; a method that only rephrases TV/Hellinger without using Boolean arithmetic will inherit the same near-equal-ratio blowup and should be rejected early.

---

## 9. Executed sanity checker

The checker was actually executed before repository delivery. It returned `PASS`.

Preserved code:

`proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T20-08-00+0300__check_dyadic_gap_recombination.py`

creation commit `e93fb1dd6effbc5c534f5284223131c3bf57427b`.

Preserved output:

`proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T20-08-00+0300__check_dyadic_gap_recombination.out`

creation commit `4801816b91f7bc7289991ed85b21cad68322787e`.

The executed checks include:

- 240 dyadic scalar factor-gap fibres for Lemma 3.1;
- 200,001 points for the two exceptional scalar regimes in Lemmas 3.2--3.3;
- 12,869 certified ordered Boolean child pairs through residual dimension three modulo global sign, including 9,123 unequal-tail/character certificates and 3,746 same-tail certificates;
- zero violations of `B<=8M<=8j` and of the preserved same-tail `B<=4M` check;
- five actual quotient/full finite-field graph pairs `(m,n)=(1,2),(1,3),(2,3),(2,4),(3,4)`, with exact truth tables/FWHTs, nested support checks, child entropy/influence checks, and parent exceptional-count checks.

The largest observed `B/M` among the certified exhaustive Boolean pairs was `3.523111966872339`, below the analytic constant eight. In the finite-field graph pairs the largest observed `B/M` was `2.848288075798017`. These are sanity data only; none is used as a substitute for the analytic proof.

---

## 10. ledger_delta

```yaml
ledger_delta:
  worker: NM13-02
  parent: T01_Friedgut_Kalai_FEI
  parent_scope_before: universal finite C for every Boolean function on every finite uniform cube
  parent_scope_after: unchanged
  parent_status_before: OPEN
  parent_status_after: OPEN
  unrestricted_universal_C_before: UNKNOWN
  unrestricted_universal_C_after: UNKNOWN
  precise_P03_obstruction_read: arbitrary unequal Boolean Fourier weights; newest flat-tail/arithmetic-selector handoff
  prior_NM13_02_gap: common-exception flat-tail siblings with unequal tail magnitudes were UNPROVED
  new_theorem: one-exception 2-separated recombination B_i <= 8 M_i <= 8 j_i
  boolean_corollary: every common-exception one-flat-tail sibling pair has B_i <= 8 j_i; equal tails retain B_i <= 4 j_i
  hereditary_closure: dependent stopping trees with these internal splits and leaf direct constant <=8 have R_T <= 8 I
  unconditional_application: quotient/full finite-field multiplication-graph selector F_{m,n} has R_T <= 8 I for all 1<=m<n
  application_gain: parent has multiple unequal tail scales and generic few-exception sufficient coefficient grows as 3m+O(1), while branch certificate stays 8
  peer_claim_status: P03 direct one-exception theorem treated as pending independent review; not needed for explicit application
  checker_status: PASS
  checker_commit: e93fb1dd6effbc5c534f5284223131c3bf57427b
  output_commit: 4801816b91f7bc7289991ed85b21cad68322787e
  residual_obstruction: many near-equal common-support amplitudes and/or multiple exceptional drift fibres
  false_lemmas_preserved: yes
  fresh_control_restriction_preserved: yes
  full_FEI_claimed: false
  public_posting_or_email_or_drive_or_paid_compute_or_schedule_change: false
```
