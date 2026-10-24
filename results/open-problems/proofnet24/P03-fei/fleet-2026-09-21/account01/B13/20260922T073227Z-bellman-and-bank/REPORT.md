# B13 — prime-Bellman tree semantics and a finite AND-bank obstruction

**Classification:** `ESSENTIAL_STEP_APPLIED / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED**.

## 0. Live candidate and exact predecessor consumed

The current owner-selected target is the all-gate formulation of FEI.  The newest complete compatible lead I consume here is account04/B18, scientific commit

`a6b9372512342993ba16a1892ccda12dddf1e7d7`,

`account04/B18/20260922T071537Z-prime-repair-shape-barrier/PRIME_BELLMAN_ENVELOPE.md`.

For a finite symmetric potential `Gamma`, put

\[
R_G(\Gamma;q)=
\sum_i {\operatorname{It}_i(G;q)\over V_{q_i}}
\bigl(\Gamma(q_i)+h_2(V_{q_i})\bigr)-\widetilde H_G(q),
\qquad V_u=4u(1-u).
\tag{0.1}
\]

The gate inequality is `Gamma(p_out) <= R_G(Gamma;q)`.  Account04/B18 defines the prime Bellman operator

\[
(\mathcal T\Gamma)(p)
=
\inf_{(G,q)\in\mathcal A_p}R_G(\Gamma;q),
\tag{0.2}
\]

where `A_p` consists of unary identities and all composition-prime Boolean gates at full-support product biases with output measure `p`.  It proves that a nonnegative fixed point of `T` is exactly an all-gate potential, and that if every descending iterate `T^m Gamma_0` stays nonnegative then their pointwise limit is such a fixed point.

The seed under discussion is the already-refuted

\[
\Gamma^\dagger(p)=\Gamma_0(p)+0.268204856\,p(1-p),
\qquad \Gamma^\dagger(1/2)=6.521851214.
\tag{0.3}
\]

The exact Numaro composition-prime witness at

\[
p_1=3/8,\quad p_2=\cdots=p_{18}=1/2,
\quad r=p_{out}=967/2048
\tag{0.4}
\]

has

\[
D_{\Gamma^\dagger}=-d,
\qquad d>0.017611.
\tag{0.5}
\]

I also substantively consume account02/B17 commit

`f6f35a38384d3861c56e72fe8b16aae28d8e7218`,

which proves the exact charged-AND inequality framework and the center-zero rigidity theorem.  The present run strengthens its quantitative transport constant enough to cross the previously unclosed `0.258204856` uniform-bank threshold.

The older addressing, majority, tribes, sparse-defect, tensor, and biased-boundary obstructions were checked before this step: the current route uses the already-certified *interior composition-prime* witness rather than another bounded-depth selector, rare-cylinder amplifier, tensor product, or boundary asymptotic.  No conclusion below assumes those mechanisms are universal.

## 1. Exact tree semantics of the prime Bellman iterates

The B18 operator is not merely an abstract functional iteration.  Every finite iterate is exactly an optimization over genuine finite Boolean composition trees.

A **prime tree of height at most `m`** is a rooted tree whose internal nodes are composition-prime Boolean gates, whose leaves are unary identities carrying arbitrary biases in `(0,1)`, and whose child blocks are disjoint.  Let `F_tau` be the resulting composite Boolean gate on the leaves, and let `p_tau` be its root output measure.

### Theorem 1.1 — prime-tree dynamic programming identity

For every finite symmetric `Gamma`, every `m>=0`, and every `p in (0,1)`,

\[
\boxed{
(\mathcal T^m\Gamma)(p)
=
\inf_{\substack{\tau:\,\operatorname{height}(\tau)\le m\\p_\tau=p}}
R_{F_\tau}(\Gamma;q_{\rm leaves}).
}
\tag{1.1}
\]

Unary identities allow shorter trees to be padded, so `<=m` and `=m` are equivalent conventions.

### Proof

The height-zero identity is `R_id(Gamma;p)=Gamma(p)`, so (1.1) holds for `m=0`.

Let an outer prime gate `A` have child-output biases `q_1,...,q_k`, and let

\[
\lambda_i={\operatorname{It}_i(A;q)\over V_{q_i}}\ge0.
\tag{1.2}
\]

The exact gate-slack composition theorem of account04/B15 gives, for a disjoint composition `F=A(B_1,...,B_k)`,

\[
D_F^\Gamma=D_A^\Gamma+\sum_i\lambda_iD_{B_i}^\Gamma.
\tag{1.3}
\]

Since `R_G=D_G+Gamma(p_out)`, (1.3) is equivalent after cancellation to

\[
\boxed{
R_F(\Gamma)
=
\sum_i\lambda_i\bigl(R_{B_i}(\Gamma)+h_2(V_{q_i})\bigr)
-\widetilde H_A(q).
}
\tag{1.4}
\]

Assume (1.1) at height `m`.  For fixed outer `(A,q)`, the child trees are independent and all coefficients `lambda_i` are nonnegative, hence the infimum of the right side of (1.4) factorizes:

\[
\inf_{B_1,...,B_k}R_F(\Gamma)
=
\sum_i\lambda_i\bigl((\mathcal T^m\Gamma)(q_i)+h_2(V_{q_i})\bigr)
-\widetilde H_A(q).
\tag{1.5}
\]

Taking the infimum over all prime outer instances with output `p` is exactly `T(T^m Gamma)(p)`.  This proves (1.1) by induction. `QED`

### Corollary 1.2 — all finite gates are the Bellman closure

Every finite Boolean gate either is composition-prime or has a nontrivial disjoint block decomposition; recursive decomposition strictly lowers arity and therefore terminates.  Conversely every finite prime tree is a finite Boolean gate.  Thus

\[
\boxed{
\inf_{m\ge0}(\mathcal T^m\Gamma)(p)
=
\inf_{\substack{F\text{ finite Boolean gate},\ q\in(0,1)^n\\p_{out}(F;q)=p}}
R_F(\Gamma;q).
}
\tag{1.6}
\]

In particular a strictly negative Bellman iterate has a genuine finite gate/bias witness (up to an arbitrarily small approximation if an infimum is not attained); it is not an artifact of the functional operator.  Conversely, nonnegativity of all finite gate costs in (1.6) is exactly the positivity condition needed by the B18 descending-envelope theorem.

This is the compact conditional end-to-end chain for the current candidate:

\[
\forall F,q:\ R_F(\Gamma^\dagger;q)\ge0
\Longleftrightarrow
\forall m:\ \mathcal T^m\Gamma^\dagger\ge0
\Longrightarrow
\Gamma_\infty\ge0,\ \mathcal T\Gamma_\infty=\Gamma_\infty
\Longrightarrow
\text{full FEI at a finite center cap}.
\tag{1.7}
\]

The first arrow is still the essential open one.

## 2. A stronger finite dual for charged AND transport

Account02/B17 studies a symmetric perturbation `psi` of `Gamma^dagger`.  For two-input AND define

\[
L_{p,q}(\psi)=q\psi(p)+p\psi(q)-\psi(pq),
\qquad
M(p,q)=pq(1-p)(1-q).
\tag{2.1}
\]

Its previous quantitative theorem assumed

\[
L_{p,q}(\psi)\ge-KM(p,q)
\qquad\forall p,q\in(0,1),
\tag{2.2}
\]

and `psi(1/2)=0`, and obtained

\[
{57\over256}\psi(3/8)-\psi(967/2048)
\le0.0696442\,K.
\tag{2.3}
\]

That missed the guaranteed bank threshold by about two percent.  A second exact AND bridge improves the coefficient enough to cross it.

Put

\[
y={57\over1081},\qquad z={313\over1081},
\qquad x={1081\over2048}.
\tag{2.4}
\]

Let the tent map on `(0,1/2)` be

\[
T(t)=\min\{2t,1-2t\}.
\tag{2.5}
\]

The exact arithmetic facts are

\[
T^{253}(y)=y,
\qquad T^{17}(y)=z.
\tag{2.6}
\]

At `q=1/2`, (2.2), symmetry, and `psi(1/2)=0` give

\[
\psi(t)\le{1\over2}\psi(Tt)+Kc(t),
\qquad c(t)={t(1-2t)\over2}.
\tag{2.7}
\]

Therefore on the 253-cycle

\[
\psi(T^j y)\le K U_j,
\tag{2.8}
\]

where

\[
U_j=
{\sum_{ell=0}^{252}2^{-ell}c(T^{j+ell}y)
\over1-2^{-253}}.
\tag{2.9}
\]

Exact rational arithmetic gives

\[
U_0=0.0701844900399009660011296\ldots,
\qquad
U_{17}=0.1041093695635667371056608\ldots.
\tag{2.10}
\]

Now use two genuine AND constraints.  First take

\[
(p,q)=\left({1081\over2048},{1024\over1081}\right),
\qquad pq={1\over2}.
\tag{2.11}
\]

With symmetry this gives

\[
{1024\over1081}\psi(967/2048)
+{1081\over2048}\psi(y)
\ge-KM_0.
\tag{2.12}
\]

Second take

\[
(p,q)=\left({768\over1081},{1081\over2048}\right),
\qquad pq={3\over8}.
\tag{2.13}
\]

This gives

\[
\psi(3/8)
\le {1081\over2048}\psi(z)
+{768\over1081}\psi(967/2048)+KM_1.
\tag{2.14}
\]

Multiply (2.14) by `57/256`.  The coefficient of `psi(967/2048)` becomes

\[
{57\over256}{768\over1081}-1=-{910\over1081}.
\tag{2.15}
\]

The factor needed to eliminate it using (2.12) is exactly

\[
{910/1081\over1024/1081}={455\over512}.
\tag{2.16}
\]

Substituting (2.8)--(2.10) yields the following exact theorem.

### Theorem 2.1 — sharpened witness/AND transport

Every bounded symmetric `psi` with `psi(1/2)=0` satisfying (2.2) obeys

\[
\boxed{
{57\over256}\psi(3/8)-\psi(967/2048)
\le \kappa K,
}
\tag{2.17}
\]

where

\[
\kappa=
{455\over512}xU_0
+{57\over256}xU_{17}
+{455\over512}M_0
+{57\over256}M_1
\tag{2.18}
\]

is an exact rational number satisfying

\[
\boxed{
\kappa
=0.0676346063971711006296130\ldots
<0.067635.
}
\tag{2.19}
\]

The exact checker beside this report proves the cycle identities and the rational comparison in (2.19); no floating-point sign decision is used.

## 3. Crossing the previously open guaranteed-bank threshold

The completed read-once theorem used by account02/B17 proves every AND inequality for

\[
\Gamma_{cert}(p)=\Gamma_0(p)+0.01\,p(1-p).
\tag{3.1}
\]

Hence the refuted `Gamma^dagger` contains the explicitly guaranteed uniform quadratic AND bank

\[
A=0.268204856-0.01=0.258204856.
\tag{3.2}
\]

The exact Numaro witness needs more than `d=0.017611` of repair.  Theorem 2.1 gives

\[
\kappa A
=0.0174635838053982428454308\ldots
<0.017611.
\tag{3.3}
\]

Equivalently any center-zero repair financed only through the uniform bound (2.2) needs

\[
\boxed{
K>{0.017611\over\kappa}
>0.26038445
>0.258204856=A.
}
\tag{3.4}
\]

So the previously remaining `~2%` gap in the B17 uniform-bank accounting is closed.

There is also a deflationary extension relevant to the B18 Bellman envelope.  Let `c=psi(1/2)<=0` and define

\[
\psi_0(t)=\psi(t)-4c\,t(1-t).
\tag{3.5}
\]

Then `psi_0(1/2)=0`, and

\[
L_{p,q}(\psi_0)=L_{p,q}(\psi)-4cM(p,q).
\tag{3.6}
\]

Thus if the perturbation spends at most the guaranteed bank,

\[
L_{p,q}(\psi)\ge-AM(p,q),
\tag{3.7}
\]

then `psi_0` satisfies (2.2) with `K=A+4c<=A` whenever this number is nonnegative; if `A+4c<0`, (3.6) is even stronger than the zero-cost rigidity condition and is impossible for a nonzero bounded center-zero perturbation.

For the prime witness, the full repair functional is

\[
W(\psi)
={57\over256}\psi(3/8)
+{465\over256}\psi(1/2)
-\psi(967/2048).
\tag{3.8}
\]

The normalization (3.5) gives

\[
W(\psi)=
\left[{57\over256}\psi_0(3/8)-\psi_0(967/2048)\right]
+Bc,
\tag{3.9}
\]

with the exact positive coefficient

\[
\boxed{B={1078193\over1048576}=1.02824497222900390625.}
\tag{3.10}
\]

Since `c<=0`, the center term can only make repair harder.  Combining (2.17), (3.3), and (3.9) proves:

### Corollary 3.1 — no non-increasing-center repair from the uniform AND bank alone

There is **no** bounded symmetric perturbation `psi` with `psi(1/2)<=0` that simultaneously satisfies

\[
W(\psi)\ge0.017611
\tag{3.11}
\]

and

\[
L_{p,q}(\psi)\ge-0.258204856\,M(p,q)
\qquad\forall p,q\in(0,1).
\tag{3.12}
\]

This is a theorem about the repair mechanism, not a refutation of FEI and not a refutation of the Bellman envelope itself.  A surviving dominated fixed point may spend the **additional nonuniform positive AND slack already present in `Gamma_cert`** at some pairs.  What (3.11)--(3.12) prove is that it *must* do so; the uniform quadratic bank cannot possibly suffice.

Moreover the contradiction margin is already positive using only the coarse source certificate:

\[
0.017611-\kappa A
>0.00014741619.
\tag{3.13}
\]

## 4. Exact old and new missing implications

**Old missing implication (account04/B18):** prove that every iterate `T^m Gamma^dagger` remains nonnegative, equivalently by Theorem 1.1 prove all finite prime-tree costs in (1.6) are nonnegative.

**New proved structural condition:** any non-increasing-center all-gate repair dominated by `Gamma^dagger` must spend *more* than the uniform `0.258204856 M(p,q)` AND bank somewhere in the finite dual mechanism above.  It therefore must use detailed residual slack of the certified read-once potential; a free/local dent or a uniform-bank-only dent is impossible.

The dual is finite and explicit: it uses the 253 `q=1/2` tent-map AND constraints generated from `57/1081`, plus the two bridge pairs (2.11) and (2.13).  Thus the next smallest honest implication is no longer a global profile statement:

\[
\boxed{
\text{Quantify the actual certified AND residual on this finite 255-constraint dual and decide whether it can supply the }0.00014741619\text{ excess.}
}
\tag{4.1}
\]

If it cannot, this dominated-seed deflationary Bellman repair is killed.  If it can, the same dual identifies exactly where the repair must spend that residual before the next prime constraint is checked.  The authentic `cert_vi_h96k40_f4.npz` bytes are not present in the authorized repository state available to this run, so I do not guess those 255 residual values from an older candidate or from a mock interpolation.

## 5. Status

**Classification:** `ESSENTIAL_STEP_APPLIED`.

The result is not a complete FEI proof.  It adds two source-exact structural facts to the current candidate chain:

1. every Bellman iterate has exact genuine-Boolean prime-tree semantics, so a negative iterate is a finite gate/bias obstruction rather than an abstract functional artifact;
2. the known interior prime witness cannot be repaired at non-increasing center using only the entire explicit uniform AND bank retained above the `0.01` read-once certificate.  Any viable dominated envelope must exploit detailed nonuniform read-once AND slack on an explicit finite constraint set.

Full FEI remains **OPEN / NOT PROVED**.
