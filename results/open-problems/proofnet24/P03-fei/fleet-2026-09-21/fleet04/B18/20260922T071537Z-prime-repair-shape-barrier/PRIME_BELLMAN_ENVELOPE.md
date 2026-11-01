# Prime-gate Bellman envelope — exact fixed-point reduction

**Status:** `PROVED REDUCTION / FULL FEI OPEN`.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

This file continues `REPORT.md` in the same run.  The preceding shape barrier says exactly what a low-cap additive repair of the refuted `Gamma^dagger` must do locally.  Here I construct the prime-gate envelope operator suggested by the current source state and prove an exact fixed-point/iteration criterion.  This is a reduction, not a proof that the required iterates stay nonnegative.

## 1. Definition

For a finite symmetric function `Gamma:(0,1)->R` and a Boolean gate `G` with full-support product bias vector `q=(q_1,...,q_k)`, write

\[
R_G(\Gamma;q)
:=
\sum_i {\rm It}_i(G;q)
{\Gamma(q_i)+h_2(V_{q_i})\over V_{q_i}}
-\widetilde H_G(q),
\qquad V_u=4u(1-u).
\tag{1.1}
\]

Thus the all-gate inequality is exactly

\[
\Gamma(p_{\rm out})\le R_G(\Gamma;q).
\tag{1.2}
\]

Let `A_p` consist of

- the unary identity gate at input bias `p`; and
- every composition-prime nonconstant Boolean gate of every finite arity, together with every full-support bias vector whose output measure is `p`.

Define the **prime Bellman envelope**

\[
\boxed{
(\mathcal T\Gamma)(p)
:=\inf_{(G,q)\in\mathcal A_p}R_G(\Gamma;q).
}
\tag{1.3}
\]

When an infimum is unbounded below we allow the value `-infinity`; in the nonnegative iteration theorem below this case is automatically excluded.

For the unary identity, biased influence is `V_p` and its one-bit spectral entropy is `h_2(V_p)`, so

\[
R_{\rm id}(\Gamma;p)=\Gamma(p).
\tag{1.4}
\]

Consequently

\[
\boxed{\mathcal T\Gamma\le\Gamma\quad\hbox{pointwise}.}
\tag{1.5}
\]

## 2. Fixed points are exactly all-gate potentials

### Theorem 2.1

For a finite symmetric `Gamma`, the following are equivalent.

1. `Gamma` satisfies the gate inequality `(G)` for every Boolean gate of every finite arity and every full-support product bias.
2. `Gamma` satisfies `(G)` for every composition-prime gate (with the unary identities included).
3. `Gamma` is a fixed point of the prime Bellman envelope:
   \[
   \boxed{\mathcal T\Gamma=\Gamma.}
   \tag{2.1}
   \]

### Proof

`1 => 2` is immediate.

For `2 => 1`, use the exact gate-slack composition theorem from

`fleet04/B15/20260922T004054Z-gate-margin-composition/REPORT.md`, blob `f28787116ef84606407150d3c4619bb8811bb928`:

\[
D_{A(B_1,\ldots,B_m)}^\Gamma
=D_A^\Gamma+\sum_i\lambda_iD_{B_i}^\Gamma,
\qquad\lambda_i\ge0.
\tag{2.2}
\]

Recursively decompose any decomposable finite gate.  Arity strictly drops inside every nontrivial block, so the process terminates at composition-prime, unary, or constant factors.  Prime factors have nonnegative slack by assumption; unary projections/negations have zero slack for symmetric `Gamma`; endpoint constants are handled by the usual `Gamma(0)=Gamma(1)=0` extension.  Equation (2.2) then gives nonnegative slack for the original gate.

For `2 <=> 3`, condition 2 says every term in the infimum (1.3) is at least `Gamma(p)`, hence `T Gamma >= Gamma`.  The identity gate gives the reverse inequality (1.5).  Therefore equality holds pointwise.  Conversely equality implies every prime-gate term is at least the infimum `Gamma(p)`. QED.

Thus the current FEI gate reformulation can be restated without loss:

> Full FEI follows once one finds a symmetric nonnegative finite fixed point of `T`; its center value is the FEI constant supplied by the induction.

No candidate fixed point is asserted here.

## 3. Order structure and continuity from above

### Lemma 3.1 — monotonicity

If `Gamma <= Lambda` pointwise, then

\[
\boxed{\mathcal T\Gamma\le\mathcal T\Lambda.}
\tag{3.1}
\]

Indeed every coefficient `It_i/V_{q_i}` in (1.1) is nonnegative, so every affine gate functional is monotone, and an infimum of monotone functionals is monotone.

### Lemma 3.2 — continuity from above

Let `Gamma_m` be finite functions with

\[
\Gamma_1\ge\Gamma_2\ge\cdots\downarrow\Gamma
\]
pointwise.  Assume `(T Gamma_m)(p)` and `(T Gamma)(p)` are finite at the point `p`.  Then

\[
\boxed{
(\mathcal T\Gamma_m)(p)\downarrow(\mathcal T\Gamma)(p).
}
\tag{3.2}
\]

### Proof

Monotonicity gives a decreasing sequence bounded below by `T Gamma`, so its limit `L` satisfies `L>=T Gamma`.
For any `epsilon>0`, choose one finite prime-gate instance `(G,q)` with output `p` such that

\[
R_G(\Gamma;q)< (\mathcal T\Gamma)(p)+\epsilon.
\]

Because this instance has only finitely many inputs, pointwise convergence gives

\[
R_G(\Gamma_m;q)\downarrow R_G(\Gamma;q).
\]

Since `T Gamma_m <= R_G(Gamma_m;q)`, taking limits yields

\[
L\le R_G(\Gamma;q)<T\Gamma(p)+\epsilon.
\]

Let `epsilon` tend to zero. QED.

Output negation and input negations preserve composition-primality and send biases to their complements.  Therefore `T` preserves symmetry whenever the input potential is symmetric.

## 4. Descending-envelope criterion

Fix a finite symmetric seed `Gamma_0` and iterate

\[
\Gamma_{m+1}=\mathcal T\Gamma_m.
\tag{4.1}
\]

By (1.5),

\[
\Gamma_0\ge\Gamma_1\ge\Gamma_2\ge\cdots.
\tag{4.2}
\]

### Theorem 4.1 — positivity of all iterates is sufficient

If every iterate is finite and nonnegative on `(0,1)`, then the pointwise limit

\[
\Gamma_\infty(p):=\inf_m\Gamma_m(p)
\tag{4.3}
\]

is symmetric, nonnegative, and satisfies

\[
\boxed{\mathcal T\Gamma_\infty=\Gamma_\infty.}
\tag{4.4}
\]

Consequently `Gamma_infty` satisfies every Boolean gate inequality, and full uniform-cube FEI follows with constant

\[
C\le\Gamma_0(1/2).
\tag{4.5}
\]

### Proof

Nonnegativity gives a finite pointwise limit.  Lemma 3.2 applied to the decreasing sequence gives

\[
\mathcal T\Gamma_\infty
=\lim_m\mathcal T\Gamma_m
=\lim_m\Gamma_{m+1}
=\Gamma_\infty.
\]

Theorem 2.1 then supplies all gate inequalities.  The center cannot increase because the iteration is decreasing. QED.

### Theorem 4.2 — exact dominated-fixed-point criterion

There exists a nonnegative fixed point `Psi` with

\[
0\le\Psi\le\Gamma_0
\tag{4.6}
\]

if and only if every iterate `Gamma_m=T^m Gamma_0` is nonnegative.

The forward direction follows by monotonicity:

\[
\Psi=\mathcal T^m\Psi\le\mathcal T^m\Gamma_0=\Gamma_m.
\]

The reverse direction is Theorem 4.1.  Thus failure of a finite iterate to remain nonnegative rules out a universal potential **dominated by that particular seed**, while survival of all iterates proves FEI at the seed's center.

This theorem does not say every possible FEI potential must lie below `Gamma_0`; a negative iterate for one seed would refute only the dominated-fixed-point route, not FEI.

## 5. Exact action on the known prime witness

Take the refuted seed

\[
\Gamma_0=\Gamma^\dagger,
\qquad \Gamma^\dagger(1/2)=6.521851214.
\]

For Numaro's composition-prime 18-input gate at

\[
p_1=3/8,\quad p_2=\cdots=p_{18}=1/2,
\quad r=p_{\rm out}=967/2048,
\]
fleet03/B12 proves

\[
D_{\Gamma^\dagger}=-d,
\qquad d=0.0176114199558017537894958865691\ldots.
\]

Since this exact prime gate is one admissible term in the infimum defining `T`, its right side is

\[
R_G(\Gamma^\dagger;p)
=\Gamma^\dagger(r)-d.
\]

Therefore the first exact envelope step obeys

\[
\boxed{
(\mathcal T\Gamma^\dagger)(r)
\le\Gamma^\dagger(r)-d.
}
\tag{5.1}
\]

So the canonical prime-envelope update immediately chooses the **downward-dent mechanism** isolated in `REPORT.md`; it never repairs a violated output constraint by increasing that output value, because the identity gate already makes the operator deflationary.

The open question has therefore become a sharply defined one:

\[
\boxed{
\text{Do all iterates }\mathcal T^m\Gamma^\dagger\text{ remain nonnegative?}
}
\tag{5.2}
\]

A proof of (5.2) would close full FEI with `C=6.521851214`.  A negative iterate would rigorously kill this **dominated-envelope seed** and identify the finite prime-gate cascade responsible, without refuting FEI itself.

## 6. Relation to the current fleet04 B12--B14 state

The latest B12--B14 MUX/collar results were proved for the old fixed `Gamma^dagger`.  Under the operator viewpoint they are best retained as certificates that particular prime-gate functionals do not drive the first envelope step in their certified regions.  The new off-centre 18-input prime witness does drive it at `r`, so the next useful calculation is not another collar for the unchanged seed: it is the **second-envelope response to the forced dent (5.1)**, especially on gates that use a bias near `r` as an input.

The exact zero-depth mixed-curvature classification remains a valid endpoint theorem but supplies no automatic lower bound on the envelope iterates, so it is not double-counted.

**Next smallest honest implication:** prove that the forced first dent cannot amplify to negativity under the prime envelope, or exhibit the first source-valid prime gate/bias cascade for which it does.  This is an exact yes/no calculation in the current universal proof chain.
