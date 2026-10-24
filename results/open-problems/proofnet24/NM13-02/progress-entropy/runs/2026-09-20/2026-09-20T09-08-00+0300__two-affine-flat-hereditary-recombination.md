Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — not authenticated as GPT-6 at maximum.

# NM13-02 T01 — two-affine-flat hereditary recombination: a dimension-free certificate for the exact next P03 obstruction

## 0. Parent status and mathematical movement

**Parent problem.** Friedgut--Kalai Fourier entropy--influence (FEI) on the finite uniform cube: prove one finite universal constant `C` such that

\[
H(\widehat f^{\,2})\le C I(f)
\]

for every Boolean `f` in every dimension.

**Parent scope/bound before -> after:** **OPEN -> OPEN**. The unrestricted universal finite upper bound remains **UNKNOWN -> UNKNOWN**. Nothing below is promoted to full FEI.

**New mechanism-level theorem.** For arbitrary affine subspaces `A,B\subseteq\mathbb F_2^n` (either may be empty) and an arbitrary quadratic polynomial `q`, put

\[
\sigma_A=1-2\,1_A,
\qquad
f(x)=(-1)^{q(x)}\sigma_A(x)\sigma_B(x)
      =(-1)^{q(x)}\sigma_{A\triangle B}(x).
\]

Then there exists a full adaptive physical restriction tree `T` such that

\[
\boxed{R_T(f)\le 24 I(f).}
\tag{0.1}
\]

The constant is independent of dimension, both codimensions, whether the flats are nested/intersecting/disjoint, their relative orientation, and the rank of the quadratic polar form. This is an all-dimensional hereditary theorem with no fresh variables.

This answers, at the hereditary-allocation level, the **exact next obstruction in P03's newest report**: P03 explicitly asks whether the one-flat theorem recombines for

\[
(-1)^q\sigma_{A\triangle B}
\]

with a constant independent of ambient dimension and relative orientation, or whether two flats already break the route. The answer is: **two flats do recombine with a uniform hereditary constant; they do not furnish such a counterexample.**

A supporting terminal theorem proved below is also new:

\[
\boxed{H(\chi\,\sigma_A\sigma_B)\le24 I(\chi\,\sigma_A\sigma_B)}
\tag{0.2}
\]

for every affine character `chi` whenever both nonempty flats have codimension at least three. This terminal estimate is one ingredient of (0.1), not a claim of unrestricted FEI.

## 1. Controlling directive, compact handoff, and exact dependencies

The controlling policy is `operations/PROGRESS20_2026-09-20.md`, blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`. LIVE20 assigns NM13-02 to T01 hereditary entropy/recombination theory, paired with P03. It requires substantive derivation first and explicitly says that restricted classes do not settle full FEI.

`POSTED.md` was checked for exact-scope exclusions. It contains no posted unrestricted FEI theorem and no posted theorem matching the two-affine-flat statement here. This report does not reopen any posted exclusion.

### Compact handoff of prior NM13-02 mathematics

The following earlier NM13-02 results remain preserved with their stated scopes.

1. **Quadratic rank telescope.** For a quadratic phase `(-1)^q`, every full adaptive physical restriction tree has exact hereditary allocation `R=r/2`, where `r` is the polar rank; hence `R<=I`.
2. **Exact influence budget / max-splicing.** Queried influence plus weighted residual-leaf influence equals root influence, allowing genuinely branch-dependent leaf certificates to be grafted without summing their constants.
3. **Character-child and one-defect payments.** Character-canalizing branches and one-point perturbations of arbitrary quadratic phases have dimension-free hereditary certificates.
4. **Descendant-influence payment.** `B_i<= (1/ln 2) j_i +(I(f^+)+I(f^-))/2`.
5. **Hybrid branch propagation.** Combining descendant and minor-child routes yields a branch-dependent recursion and, in particular, a uniform `<3` hereditary constant for arbitrary-depth nested-canalizing cores under arbitrary quadratic twists.

The false pointwise erasure shortcut, fixed-coefficient affine-drift route, Han absolute-overlap selector, derivative-degree scalar scheduler, and retired resolvent/interpolation routes remain false/retired. Nothing below reintroduces them.

### P03 dependency used only as target identification

The newest P03 report is

`proofnet24/P03-fei/runs/2026-09-20/2026-09-20T08-27-46+0300__fei-affine-flat-quadratic-hereditary.md`, blob `be68be1be01e8abbb9f45dd62c5cc238d5e6119d`.

It proves a one-affine-flat restricted theorem and ends by identifying the first genuine recombination test `(-1)^q sigma_{A triangle B}`. The proof below does **not** assume P03's one-flat theorem as a black box: Sections 3--5 independently establish the local ingredients needed here, including a self-contained one-flat hereditary base. P03 retains ownership of its stronger one-flat constants and its separate recombination theorem.

P03 also reports

\[
S_T\le \frac2{\ln2}J_T\le\frac2{\ln2}Q_T.
\tag{1.1}
\]

That peer result is **not needed** for (0.1). Only in Section 7 is it mentioned as a clearly marked project-conditional consequence pending later independent review.

## 2. Current primary-source status

A fresh bounded source check on 20 September 2026 recovered González--MacManus--Pereyra, arXiv:2606.00246, *Further evidence towards the Fourier Entropy-Influence conjecture* (submitted 29 May 2026). Its current abstract still states the universal FEI assertion as a conjecture and develops a stopping-tree sufficient framework and proper subclasses; it says that a key restriction inequality, **if** valid for all Boolean functions, would imply full FEI. It is not a universal proof.

The current Li--Han strengthening, arXiv:2512.03117 (2 December 2025), proves the sharp-constant general estimate

\[
H(\widehat f^{\,2})
\le I(f)+\sum_i I_i(f)\ln\frac1{I_i(f)},
\]

so the coordinate-influence logarithmic term remains. This also does not give universal `H<=CI`.

A bounded search for FEI together with affine-subspace/symmetric-difference/quadratic-phase terms did not recover the two-flat theorem proved below. This is negative search evidence only; **publication priority is UNVERIFIED**.

## 3. Preliminaries used in the proof

Work on `F_2^n`, with base-two entropy. For a Boolean `g`, let `Z` be its squared-Fourier random set,

\[
\Pr(Z=S)=\widehat g(S)^2.
\]

For a physical coordinate `i`, write

\[
\alpha_i(g)=\operatorname{Inf}_i(g),
\qquad
j_i(g)=\min\{\alpha_i(g),1-\alpha_i(g)\},
\qquad
B_i(g)=H(Z_i\mid Z_{-i}).
\]

For an adaptive physical tree `T`, `R_T` denotes the cylinder-weighted sum of these `B_i` payments over internal nodes.

### Lemma 3.1 (one-step influence identity)

For the two physical restrictions `g^+,g^-` at coordinate `i`,

\[
\boxed{I(g)=\alpha_i(g)+\frac{I(g^+)+I(g^-)}2.}
\tag{3.1}
\]

This follows by separating the queried-direction edge contribution from all residual-coordinate edges and averaging the two slices. Iteration gives the usual exact influence budget.

### Lemma 3.2 (Han--Shearer hereditary selection)

For every Boolean `g`,

\[
\boxed{\sum_i B_i(g)\le H(\widehat g^{\,2}).}
\tag{3.2}
\]

Indeed `B_i=H(Z)-H(Z_{-i})`, and

\[
\sum_iH(Z_{-i})\ge(n-1)H(Z).
\]

For completeness, order the coordinates. By the chain rule,

\[
H(Z_{-i})=
\sum_{j\ne i}H(Z_j\mid Z_{<j}\setminus\{Z_i\})
\ge
\sum_{j\ne i}H(Z_j\mid Z_{<j}),
\]

because removing a conditioning variable can only increase conditional entropy. Summing in `i` gives `(n-1)H(Z)`.

Consequently, if a restriction-closed state satisfies `H<=K I`, then unless it is constant there is some coordinate with

\[
B_i\le K\alpha_i.
\tag{3.3}
\]

Also the spectral marginal identity gives

\[
\Pr(i\in Z)=\alpha_i(g),
\]

hence

\[
B_i(g)\le h_2(j_i(g)).
\tag{3.4}
\]

### Lemma 3.3 (product perturbation of physical influence)

For Boolean `u,v`, on every `i`-edge the disagreement indicator of `uv` is the xor of the disagreement indicators of `u` and `v`. Therefore

\[
\boxed{|\operatorname{Inf}_i(uv)-\operatorname{Inf}_i(u)|
\le \operatorname{Inf}_i(v),}
\tag{3.5}
\]

and

\[
\operatorname{Inf}_i(uv)
\le\operatorname{Inf}_i(u)+\operatorname{Inf}_i(v).
\tag{3.6}
\]

### Lemma 3.4 (Reed--Muller minimum weight, degree at most `d`)

If a nonzero multilinear polynomial `P:F_2^m->F_2` has degree at most `d`, then

\[
\Pr[P=1]\ge2^{-d}.
\tag{3.7}
\]

Proof is by induction on `m`. Write `P=P_0+x_mP_1`. If `P_1=0`, the two slices coincide and induction on `P_0` doubles the support. If `P_1\ne0`, the two slice supports have total size at least the Hamming distance between `P_0` and `P_0+P_1`, namely `|supp(P_1)|`; induction on the degree-`<=d-1` polynomial `P_1` gives at least `2^{m-d}` points. QED.

### Corollary 3.5 (degree-three hereditary certificate)

If `g=(-1)^P` with `deg P<=3`, then there is a full physical tree with

\[
\boxed{R_T(g)\le\kappa_3 I(g),
\qquad
\kappa_3=4h_2(1/4)=3.245112497836531\ldots.}
\tag{3.8}
\]

If `P` is affine, the squared spectrum is a point mass and all `B_i=0`. Otherwise choose a coordinate belonging to a monomial of degree at least two. Its derivative `D_iP` is a nonconstant polynomial of degree at most two, so both `D_iP` and `1+D_iP` are nonzero. Lemma 3.4 gives

\[
1/4\le\alpha_i(g)\le3/4,
\qquad j_i(g)\ge1/4.
\]

Since `h_2(t)/t` decreases on `(0,1/2]`, (3.4) gives `B_i<=kappa_3 j_i<=kappa_3 alpha_i`. Restrict and induct; (3.1) closes the tree estimate.

## 4. A self-contained one-flat hereditary base

This section is deliberately included so that the two-flat theorem does not assume P03's reported one-flat proof has already been independently certified.

Let `A=a+V` be a nonempty affine flat of codimension `r`, let `W=V^\perp`, and `delta=2^{-r}`. Then

\[
\widehat{1_A}(\xi)
=\delta(-1)^{\xi\cdot a}1_{\{\xi\in W\}}.
\tag{4.1}
\]

For `sigma_A=1-2 1_A`, the zero Fourier coefficient is `1-2delta`, and every nonzero `xi in W` has squared coefficient `4delta^2`. Put

\[
M=4\delta(1-\delta).
\]

Then exactly

\[
H(\sigma_A)=h_2(M)+M\log_2(2^r-1).
\tag{4.2}
\]

If `r>=3`, then `delta<=1/8` and `M>= (7/2)delta`. Using `h_2(x)<=x log_2(e/x)` and `e<7/2`,

\[
h_2(M)\le Mr,
\qquad
M\log_2(2^r-1)\le Mr,
\]

so

\[
H(\sigma_A)\le2Mr\le8\delta r.
\tag{4.3}
\]

For a physical coordinate `i`, translation by `e_i` either preserves `A` or moves it to a disjoint coset. Hence

\[
\operatorname{Inf}_i(\sigma_A)\in\{0,2\delta\}.
\tag{4.4}
\]

If `k` coordinates are active, the `n-k` inactive standard basis vectors lie in `V`, so `n-k<=n-r`, hence `k>=r`. Therefore

\[
I(\sigma_A)=2\delta k\ge2\delta r,
\]

and

\[
\boxed{H(\sigma_A)\le4I(\sigma_A).}
\tag{4.5}
\]

If `chi` is an affine character, multiplication by `chi` translates the Fourier law and preserves entropy. Since every influence in (4.4) is at most `1/4`, a character either preserves that coordinate influence or replaces it by its complement, which can only increase it. Thus

\[
H(\chi\sigma_A)\le4I(\chi\sigma_A)
\qquad(r>=3).
\tag{4.6}
\]

Now let `q` be quadratic and `g=(-1)^q sigma_A`. If `r<=2`, the indicator `1_A` is a polynomial of degree at most two (write it as the product of the independent affine equations defining `A`), so `q+1_A` is quadratic and the prior NM13-02 quadratic certificate applies.

If `r>=3` and the polar form of `q` has a nonzero row `i`, then `Inf_i((-1)^q)=1/2`. By (3.5) and (4.4),

\[
\left|\operatorname{Inf}_i(g)-\frac12\right|\le2\delta\le\frac14.
\]

Thus `j_i(g)>=1/4`, and (3.4) gives the local payment `B_i<=kappa_3 alpha_i<4 alpha_i`.

If the polar form is zero, `(-1)^q` is an affine character, so (4.6) and Lemma 3.2 produce a coordinate with `B_i<=4 alpha_i`.

Physical restrictions preserve the form “quadratic phase times one affine-flat sign” (the flat may disappear and its codimension can stay put or fall by one). Induction on dimension with (3.1) therefore proves:

\[
\boxed{R_T((-1)^q\sigma_A)\le4I((-1)^q\sigma_A)}
\tag{4.7}
\]

for some full adaptive physical tree, for every quadratic `q` and every affine flat `A` (including the empty flat).

## 5. The new terminal theorem for two high-codimension flats

Let `A,B` be distinct nonempty affine flats of codimensions `r_A,r_B>=3`, with densities

\[
\delta_A=2^{-r_A},\qquad\delta_B=2^{-r_B},
\]

and put

\[
h=\sigma_A\sigma_B=\sigma_{A\triangle B},
\qquad
\mu=\Pr(A\triangle B).
\]

Then `mu<=delta_A+delta_B<=1/4`.

We prove

\[
\boxed{H(h)\le48\mu\log_2(1/\mu).}
\tag{5.1}
\]

The edge-isoperimetric inequality on the cube gives

\[
I(h)\ge2\mu\log_2(1/\mu),
\tag{5.2}
\]

hence `H(h)<=24 I(h)`.

For completeness, (5.2) follows from the standard edge-boundary induction. If a set `D` has slice sizes `a<=b`, the two within-slice boundaries satisfy the induction hypothesis and the cross-slice boundary has size at least `b-a`. After dividing by `a+b`, the remaining scalar inequality is `h_2(a/(a+b))>=2a/(a+b)`, true by concavity of `h_2` on `[0,1/2]`. Since total influence counts every undirected boundary edge twice, (5.2) follows.

It remains to prove (5.1).

### 5.1 Intersecting flats

Suppose `C=A cap B` is nonempty. Translate a common point to the origin; squared Fourier magnitudes and physical influences are unchanged. Then `A,B,C` are linear. Write

\[
W_A=V_A^\perp,\quad W_B=V_B^\perp,\quad
W_C=W_A+W_B,\quad T=W_A\cap W_B,
\]

and `delta_C=|C|/2^n`. Since

\[
1_{A\triangle B}=1_A+1_B-2 1_C,
\]

for nonzero frequency `xi`,

\[
\widehat h(\xi)
=-2\delta_A1_{W_A}(\xi)
 -2\delta_B1_{W_B}(\xi)
 +4\delta_C1_{W_C}(\xi).
\tag{5.3}
\]

Partition nonzero frequencies into

- `W_A\setminus W_B`,
- `W_B\setminus W_A`,
- `W_C\setminus(W_A\cup W_B)`,
- `(W_A\cap W_B)\setminus\{0\}`.

Within these categories the Fourier coefficient is respectively

\[
-2\delta_A+4\delta_C,
\quad
-2\delta_B+4\delta_C,
\quad
4\delta_C,
\quad
-2\mu.
\tag{5.4}
\]

Let the four category masses be `m_A,m_B,m_C,m_T`. Their support sizes and masses obey

\[
N_A\le1/\delta_A,\quad m_A\le4\delta_A,
\]

\[
N_B\le1/\delta_B,\quad m_B\le4\delta_B,
\]

\[
N_C\le1/\delta_C,\quad m_C\le16\delta_C.
\tag{5.5}
\]

Also if `t=dim T`, then

\[
2^t\le1/\max(\delta_A,\delta_B)\le2/\mu,
\quad
m_T\le8\mu,
\quad
\log_2N_T\le L+1\le\tfrac32L,
\tag{5.6}
\]

where `L=log_2(1/mu)>=2`.

The zero-frequency squared mass is `(1-2mu)^2`, so total nonzero spectral mass is

\[
M=4\mu(1-\mu),
\quad 3\mu\le M\le4\mu.
\tag{5.7}
\]

The entropy needed merely to choose among zero and the four nonzero categories is at most

\[
h_2(M)+M\log_2 4\le8\mu L.
\tag{5.8}
\]

Indeed `h_2(M)<=M log_2(e/M)<=ML<=4mu L` because `e<3<=M/mu`, while `2M<=8mu<=4mu L`.

We also need only elementary density comparisons. Assume `delta_A>=delta_B`. If the densities are equal and `A!=B`, then `C` is proper in both, so `delta_C<=delta_A/2` and `mu>=delta_A`. If `delta_A>delta_B`, dyadicity gives `delta_B<=delta_A/2`, hence

\[
\mu=\delta_A+\delta_B-2\delta_C
\ge\delta_A-\delta_B\ge\delta_A/2\ge\delta_B.
\]

Thus in all cases

\[
\delta_A\le2\mu,
\qquad
\delta_B\le\mu,
\qquad
\delta_C\le\mu.
\tag{5.9}
\]

Because `x log_2(1/x)` is increasing on `[0,1/4]`, and if `mu<x<=2mu` then trivially `x log(1/x)<=2mu L`, we obtain

\[
\delta_A r_A+\delta_B r_B\le3\mu L,
\qquad
\delta_C r_C\le\mu L.
\tag{5.10}
\]

Conditional entropy within a category is at most the log of its support size. Therefore (5.5)--(5.10) give

\[
\begin{aligned}
H(h)
&\le 8\mu L
 +4\delta_A r_A+4\delta_B r_B
 +16\delta_C r_C
 +m_T\log_2N_T\\
&\le(8+12+16+12)\mu L
=48\mu L.
\end{aligned}
\tag{5.11}
\]

### 5.2 Disjoint flats

If `A cap B` is empty, then `mu=delta_A+delta_B`. For an affine flat `A=a+V`,

\[
\widehat{1_A}(\xi)=\delta_A(-1)^{\xi\cdot a}1_{W_A}(\xi).
\]

For nonzero frequencies the spectrum of `h=1-2 1_A-2 1_B` lies in `W_A union W_B`. On the two one-sided parts the squared coefficient is `4delta_A^2` or `4delta_B^2`. On `T=W_A cap W_B`, the two affine phases can add or cancel, but pointwise

\[
|\widehat h(\xi)|\le2(\delta_A+\delta_B)=2\mu.
\]

Thus the nonzero-category entropy is bounded exactly as above, with only three categories. The category-choice term is at most `8mu L`; the two one-sided support terms contribute at most

\[
4\delta_A r_A+4\delta_B r_B\le8\mu L,
\]

and the common-support term is at most `12mu L` by (5.6). Hence in fact

\[
H(h)\le28\mu L,
\tag{5.12}
\]

which is stronger than (5.1).

### 5.3 Affine-character twists

For every coordinate,

\[
\operatorname{Inf}_i(h)
\le\operatorname{Inf}_i(\sigma_A)+\operatorname{Inf}_i(\sigma_B)
\le2\delta_A+2\delta_B\le\frac12.
\tag{5.13}
\]

Multiplication by an affine character translates the Fourier law, hence preserves entropy. In a coordinate used by the character it replaces influence `alpha` by `1-alpha`; by (5.13) this can only increase the influence. Therefore

\[
\boxed{H(\chi h)=H(h)\le24I(h)\le24I(\chi h).}
\tag{5.14}
\]

This proves the terminal theorem (0.2).

## 6. Main theorem: quadratic twist of two arbitrary affine flats

### Theorem 6.1

For every quadratic `q` and affine flats `A,B` (possibly empty),

\[
f=(-1)^q\sigma_A\sigma_B
\]

admits a full adaptive physical restriction tree satisfying

\[
\boxed{R_T(f)\le24I(f).}
\tag{6.1}
\]

### Proof

Induct on the ambient dimension. Physical restrictions preserve the class: a quadratic remains quadratic, while an affine flat either disappears or restricts to an affine flat whose codimension stays the same or falls by one.

At a node, apply the first applicable case.

**Case 1: one flat is empty.** Use the independently proved one-flat certificate (4.7), with constant `4<24`.

**Case 2: `A=B`.** The two signs cancel and `f=(-1)^q`; use the prior NM13-02 quadratic rank certificate, with constant `1<24`.

**Case 3: one nonempty flat has codimension at most two.** Its indicator is a polynomial of degree at most two. Absorb that indicator into `q`; the state becomes a quadratic phase times one affine-flat sign, and (4.7) applies.

**Case 4: both codimensions equal three.** Each flat indicator has degree at most three, hence the exponent

\[
q+1_A+1_B
\]

has degree at most three. Corollary 3.5 gives a hereditary certificate `kappa_3<24`.

**Case 5: both codimensions are at least three, not both three, and the quadratic polar form is nonzero.** Choose a coordinate `i` in a nonzero polar row. The pure quadratic phase has influence `1/2` in that coordinate. By Lemma 3.3 and (4.4),

\[
\left|\alpha_i(f)-\frac12\right|
\le \operatorname{Inf}_i(\sigma_A\sigma_B)
\le2\delta_A+2\delta_B.
\]

At least one codimension is at least four, so

\[
2\delta_A+2\delta_B\le\frac14+\frac18=\frac38.
\]

Therefore

\[
j_i(f)\ge\frac18.
\]

By (3.4) and monotonicity of `h_2(t)/t`,

\[
B_i(f)
\le C_8 j_i(f)
\le C_8\alpha_i(f),
\qquad
C_8=8h_2(1/8)=4.348515545596771\ldots<24.
\tag{6.2}
\]

Query `i` and use the induction hypothesis in the two children. If their influences are `a,b`, then

\[
R_T(f)
\le C_8\alpha_i+12(a+b)
\le24\left(\alpha_i+\frac{a+b}{2}\right)
=24I(f)
\]

by (3.1).

**Case 6: both codimensions are at least three and the polar form is zero.** Then `(-1)^q` is an affine character. The terminal theorem (5.14) gives

\[
H(\widehat f^{\,2})\le24I(f).
\]

By Lemma 3.2 there is a coordinate with `B_i<=24 alpha_i` unless `f` is constant, in which case there is nothing to pay. Query such an `i`, invoke induction in the children, and use (3.1) exactly as in Case 5.

The cases exhaust all states, and the induction terminates after at most `n` physical restrictions. QED.

## 7. Application to P03's exact unresolved obstruction

P03's newest report asks whether the first two-flat recombination

\[
(-1)^q\sigma_{A\triangle B}
\]

has a dimension/orientation-independent payment, or whether overlap of two affine flats already defeats the one-flat mechanism.

Theorem 6.1 gives the explicit answer

\[
\boxed{\mathcal A((-1)^q\sigma_{A\triangle B})\le24}
\tag{7.1}
\]

for **every** quadratic `q` and **every** pair of affine flats, with no assumptions on nesting, transversality, disjointness, codimensions, or polar rank. Thus the first genuine affine-flat recombination does not produce the obstruction P03 was looking for.

The mechanism is genuinely different from literal defect cardinality: `A triangle B` can contain exponentially many points. It is also different from a bounded-height decision-tree argument: two oblique flats can be defined by many linear parity constraints rather than a few physical coordinates. The proof instead combines:

- exact affine-flat Fourier support;
- a two-flat entropy estimate on the polar-zero terminal regime;
- perturbative protection of a nonzero quadratic polar row;
- the low-codimension degree-three base; and
- hereditary selection through Han--Shearer plus the exact influence identity.

This is the requested substantive application, not merely a framework.

### Project-conditional FEI consequence, not promoted

If P03's separately reported dependent-recombination theorem (1.1) is later accepted after independent review, then any full tree from Theorem 6.1 would give

\[
H(\widehat f^{\,2})
=R_T+S_T
\le\left(24+\frac2{\ln2}\right)I(f)
=26.8853900817779\ldots I(f)
\tag{7.2}
\]

for the two-flat quadratic class. Because (1.1) is a peer claim rather than a theorem independently re-audited in this run, (7.2) is labeled **PROJECT-CONDITIONAL**. The hereditary theorem (6.1) itself is independent of that dependency.

## 8. What failed / what remains open

The natural stronger hope was that the one-flat constant `4` might simply tensor/recombine with no loss. I did not prove that. The spectral overlap category `W_A cap W_B` can carry coherent addition or cancellation of the two affine phases, and the crude support-entropy argument pays up to `24` after edge isoperimetry. The checker suggests this constant is very far from sharp, but finite evidence is not used to reduce the theorem constant.

More importantly, this does **not** extend automatically to an unbounded number of flats. With `m` affine flats, the Fourier support can stratify into many sums/intersections of annihilator spaces; a naive category argument can grow with `m`. Thus the remaining full-scope obstruction is now more precise:

> prove an arrangement-level entropy/payment theorem whose constant does not grow with the number of affine components, or identify a genuinely bad many-flat arrangement.

A promising next nonredundant route is to replace the number of flat components by a restriction-stable **annihilator-arrangement rank/branching complexity** and seek an amortized bound for the entropy of the frequency-incidence category. If that fails, the materially different route is to search for a many-flat counterexample to uniform hereditary allocation rather than continue polishing the two-flat constant.

All restricted fresh-control theorems remain restricted. No finite verification, no one-flat/two-flat theorem, and no project-conditional recombination corollary is labeled full FEI.

## 9. Executed checker

The exact checker used for sanity testing was executed locally before upload and then saved unchanged at

`proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T09-08-00+0300__check_two_affine_recombination.py`

creation commit `bfab9501a3ccb73c8d91e6c155265c79bdfb4a73`, blob `4580f55765d2ccc3e3114e3d389e6eb7c03b4538`.

Its actual output was saved at

`proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T09-08-00+0300__two_affine_recombination_check.json`

creation commit `efd01eda830bd2f1a9f35cb21f848505eadf687e`, blob `c7721017ee44a4c12b35d8686401659013f40dc7`.

It records `PASS` and performs three distinct checks:

1. all **18,360 ordered distinct pairs** of nonempty codimension-at-least-three affine flats in dimension four for the terminal direct inequality; maximum observed `H/I = 3.402475551198587`, with zero violations of `H<=24I`;
2. the full recursive strategy for all **346,112** combinations of a quadratic phase and an ordered pair of affine flats (including empty) in dimension three; maximum observed `R/I = 1.5574963279910676`, with zero violations of `R<=24I`;
3. **5,000** deterministic-seed dimension-four quadratic/two-flat samples through the same recursive strategy; maximum observed `R/I = 1.8266230937148955`, with zero violations.

The checker is a sanity check only. The theorem is the all-dimensional argument above.

## Metrics

- parent full FEI: `OPEN -> OPEN`;
- unrestricted universal finite source constant: `UNKNOWN -> UNKNOWN`;
- new hereditary class before: one affine-flat sign defect under quadratic twist (P03 constant 4), plus NM13-02 decision-tree/nested classes;
- new hereditary class after: arbitrary **two-affine-flat symmetric-difference defect** under arbitrary quadratic twist;
- new hereditary constant on that class: `24`;
- fresh variables: `none`;
- ambient-dimension dependence: `none`;
- dependence on affine codimensions/orientation/intersection type: `none`;
- independent audit: `pending`;
- publication priority: `UNVERIFIED`.

## ledger_delta

```yaml
ledger_delta:
  owner: NM13-02
  parent: T01_Friedgut_Kalai_FEI
  source_status_before: OPEN_PARTIAL
  source_status_after: OPEN_PARTIAL
  universal_constant_before: UNKNOWN
  universal_constant_after: UNKNOWN
  new_claim:
    id: NM13-02-T01-TWO-AFFINE-FLAT-HEREDITARY-01
    status: PROVED_SELF_CHECKED
    statement: "For every quadratic q and affine subspaces A,B of F_2^n, f=(-1)^q sigma_A sigma_B admits a full adaptive physical restriction tree with R_T(f)<=24 I(f)."
    exact_P03_obstruction: "(-1)^q sigma_{A triangle B}"
    full_FEI: false
    fresh_variables: false
    audit: pending
    priority: unverified
  supporting_claims:
    - "If codim(A),codim(B)>=3 and chi is affine, H(chi sigma_A sigma_B)<=24 I(chi sigma_A sigma_B)."
    - "Independent self-contained one-flat base R<=4I used inside the two-flat induction."
    - "Degree<=3 phases admit hereditary constant kappa_3=4 h_2(1/4)."
  mechanism_gain:
    - first genuine affine-flat recombination beyond P03's one-flat theorem is uniformly bounded
    - intersecting and disjoint annihilator-overlap categories are paid by density times log-density and edge isoperimetry
    - nonzero quadratic polar rows retain folded influence at least 1/8 outside the degree-three corner
    - polar-zero nodes are handled by a direct two-flat FEI terminal inequality plus Han-Shearer selection
  preserved_failures:
    - pointwise_erasure
    - fixed_coefficient_affine_drift
    - Han_absolute_overlap_selector
    - derivative_degree_scalar_schedule
    - resolvent_interpolation
  peer_dependency_not_promoted:
    P03_paid_recombination: "S_T <= (2/ln 2) J_T <= (2/ln 2) Q_T"
    consequence_if_later_accepted: "restricted two-flat FEI constant <= 24+2/ln2 = 26.8853900817779..."
  artifacts:
    checker: "proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T09-08-00+0300__check_two_affine_recombination.py"
    checker_commit: bfab9501a3ccb73c8d91e6c155265c79bdfb4a73
    checker_blob: 4580f55765d2ccc3e3114e3d389e6eb7c03b4538
    output: "proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T09-08-00+0300__two_affine_recombination_check.json"
    output_commit: efd01eda830bd2f1a9f35cb21f848505eadf687e
    output_blob: c7721017ee44a4c12b35d8686401659013f40dc7
  residual_obstruction: "uniform control for unbounded affine-flat arrangements / many simultaneously hard branches"
  next_attack: "annihilator-arrangement rank/branching potential; if it grows, search for a many-flat hereditary-allocation counterexample"
```

**End of complete substantive run report.**
