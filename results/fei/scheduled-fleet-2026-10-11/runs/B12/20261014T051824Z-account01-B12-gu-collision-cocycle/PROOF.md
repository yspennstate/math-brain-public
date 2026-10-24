# Signed collision cocycle and the all-coordinate obstruction

## 1. Definitions and normalization

All functions below are genuine Boolean functions on a finite uniform cube.
For a function `q`, write

\[
p_q(S)=\widehat q(S)^2,\qquad
\pi_q(S)=\sum_{T\supseteq S}p_q(T),\qquad
U(q)=\sum_Sp_q(S)\log_2\frac{\pi_q(S)}{p_q(S)}.
\]

Zero masses contribute zero.  Put

\[
\Delta_iU(q)=U(q)-\frac{U(q_{i,+})+U(q_{i,-})}{2},
\qquad G(q)=\sum_i\Delta_iU(q).
\]

For two Boolean functions on the same cube, define the **signed upper-set
collision**

\[
C(g,h)=U(gh)-U(g)-U(h).
\]

No sign is discarded in this definition.

## 2. Exact restriction cocycle

For every coordinate `i`, direct substitution gives

\[
\begin{aligned}
&\Delta_iU(gh)-\Delta_iU(g)-\Delta_iU(h)\\
&\quad=C(g,h)-\frac{C(g_{i,+},h_{i,+})+C(g_{i,-},h_{i,-})}{2}.
\tag{2.1}
\end{aligned}
\]

This is an exact signed identity.  It uses neither a fixed-sign projection nor
an unsigned coefficient-four estimate.

Let an adaptive physical restriction tree choose at each internal node `v`
a coordinate `i_v`; the choice can depend arbitrarily on the preceding branch
outcomes.  Let `g_v,h_v` be the restricted pair and let `w_v=2^{-d(v)}` be its
actual reach probability.  Define

\[
\delta_vC=C(g_v,h_v)-\frac{C(g_{v,+},h_{v,+})+C(g_{v,-},h_{v,-})}{2}.
\]

Because each child has weight `w_v/2`, every nonroot collision cancels once
with its parent contribution.  Therefore

\[
\boxed{\sum_{v\,\mathrm{internal}}w_v\delta_vC
=C(g,h)-\sum_{\ell\,\mathrm{leaf}}w_\ell C(g_\ell,h_\ell).}
\tag{2.2}
\]

Equation (2.2) removes fixed coordinate order, fixed activation depth, and
uniform leaf depth.  All changing activation weights are the actual reach
weights.  The terminal term is retained, rather than silently dropped.  It
vanishes when each leaf pair is disjoint-factorized, or belongs to the
previously proved reused-character-core/disjoint-residual class, because then
`U` is additive and `C=0`.

## 3. Exact GU defect decomposition

For fixed `a>=0` and `0<=b<1`, set

\[
D_{a,b}(q)=G(q)-aI(q)-bU(q).
\]

Summing (2.1) over all physical coordinates gives

\[
G(gh)=G(g)+G(h)+LC(g,h),
\qquad
LC(g,h)=\sum_i\delta_iC.
\tag{3.1}
\]

Let

\[
J(g,h)=\sum_i\Pr_x[g(x)\ne g(x^{\oplus i})
\ \text{and}\ h(x)\ne h(x^{\oplus i})].
\]

On each edge the product changes exactly when one, but not both, factors
changes.  Hence

\[
I(gh)=I(g)+I(h)-2J(g,h).
\tag{3.2}
\]

Combining (3.1), (3.2), and `U(gh)=U(g)+U(h)+C` yields

\[
\boxed{D_{a,b}(gh)=D_{a,b}(g)+D_{a,b}(h)+\mathcal R_{a,b}(g,h),}
\tag{3.3}
\]

where the complete signed overlap remainder is

\[
\boxed{\mathcal R_{a,b}(g,h)=LC(g,h)+2aJ(g,h)-bC(g,h).}
\tag{3.4}
\]

Thus a binary composition forest has the exact implication

\[
D_{a,b}(f_{\rm root})
=\sum_{\ell}D_{a,b}(f_\ell)+\sum_{v\,\mathrm{internal}}
\mathcal R_{a,b}(g_v,h_v).
\tag{3.5}
\]

Consequently, if one fixed pair `(a,b)` with `b<1` admits, for every Boolean
function, such a forest whose leaves have nonpositive defect and whose **total
signed** remainder is nonpositive, then `G<=aI+bU` holds universally.  The
reviewed reduction then gives

\[
U(f)\le\frac{a}{1-b}I(f),\qquad
H(f)\le\left(2+\frac{2a}{1-b}\right)I(f).
\tag{3.6}
\]

This implication is global: it does not require each local remainder to be
nonpositive.  That stronger local demand is false.

## 4. Certified three-bit obstruction to termwise closure

Use truth-table order `000,001,...,111` and take

\[
g=(-1,-1,-1,-1,-1,1,1,1),\qquad
h=(-1,1,1,-1,-1,1,1,-1).
\]

The second factor is the character on coordinates `0,1`.  The nonzero
spectral masses of `g` are `9/16` at set `\{2\}` and `1/16` at every other
set.  Multiplication by `h` translates this mass pattern so the `9/16` mass
is at `\{0,1,2\}`.  Direct upper-set summation gives

\[
U(g)=\frac{11}{16}+\frac9{16}\log_2\frac43,
\qquad U(h)=0,
\]

and

\[
U(gh)=\frac14+\frac3{16}\log_2(120).
\]

Therefore

\[
C(g,h)=\frac1{16}\log_2
\frac{120^3 3^9}{2^{25}}>0,
\tag{4.1}
\]

because `120^3*3^9=34,012,224,000 > 33,554,432=2^25`.
For every coordinate and each sign, direct restriction gives child collision
zero.  Hence

\[
LC(g,h)=3C(g,h).
\tag{4.2}
\]

Moreover

\[
I(g)=\frac54,\qquad I(h)=2,\qquad I(gh)=\frac94,
\qquad J(g,h)=\frac12.
\]

Substitution in (3.4) gives, for every admissible pair,

\[
\boxed{\mathcal R_{a,b}(g,h)=(3-b)C(g,h)+a>0
\quad(a\ge0,\ 0\le b<1).}
\tag{4.3}
\]

Thus the helper assertion `R_{a,b}(g,h)<=0` for every overlapping product is
refuted, even with one factor a character.  This is not a counterexample to
GU or FEI: it only proves that companion-sign, posterior, or terminal reserves
must move globally across composition nodes.  It also explains the ownership
problem precisely: a single adaptive path pays the root collision once by
(2.2), while the all-coordinate `G` operator can charge it in three different
directions at the root.

Finally, collision has no fixed sign.  Taking `h=g` for any `g` with `U(g)>0`
gives `gh=1` and `C(g,g)=-2U(g)<0`; (4.1) supplies a positive example.

## 5. Remaining universal lemma

The exact unpaid statement is no longer an unsigned coefficient estimate.
It is a global single-use allocation problem: construct, for every Boolean
function, a physical adaptive composition forest in which the signed cocycle
terms (2.2), joint-pivotal costs `2aJ`, companion-sign/posterior credits, and
terminal collisions combine so that the total remainder in (3.5) is at most
zero, without reusing any root collision across several coordinate drifts.

The three-bit witness rules out imposing this inequality node by node.  The
next mechanism must group the simultaneous coordinate drifts of one root
before assigning its collision reserve, or carry an explicit companion-sign
potential whose restriction children cancel the multiplicity in (4.2).
