# account01/B07 — generic arity-three rigidity for biased zero occurrence-KL

**Programme:** `FEI-ALL-TEAM-20260922T095941Z`  
**Assignment:** `FEI-20260922-account01-B07` — biased zero-KL classification  
**Run:** `account01-B07-20260922T110315Z-fei`  
**Outcome:** `ESSENTIAL_STEP_APPLIED / ARITY3_GENERIC_CLASSIFICATION`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Later owner control and exact target

The invocation text still names MOC4, but fresh owner control revision `2026-09-22.3` supersedes it and assigns every B01–B20 worker to FEI. This run therefore performs no new MOC4 work. The current B07 target is to classify genuine biased Boolean gates whose normalized nonempty spectral law equals its occurrence I-projection.

The preceding same-slot report proved three exact zero-KL families: every two-input gate, every one-point-defect gate, and every biased character. It left the sharpened obligation `B-ZEROKL-PRIME-RIGIDITY-v1`: classify essential composition-prime gates of arity at least three.

This run closes the first nontrivial finite-arity slice: **all essential three-input gates at a common interior bias, outside an explicit finite algebraic exceptional set.**

## 2. Exact sources consumed

The I-projection theorem used is account02/B15, commit `4bd6d05f1eb8325d665f2748f4d74dcee2550a04`, `proofnet24/P03-fei/fleet-2026-09-21/account02/B15/20260922T0829Z-influence-iprojection-kl/REPORT.md`. For the normalized nonempty spectral law `P=w^+` with occurrence marginals `r_i=P(i in S)`, it constructs the unique maximum-entropy conditional-product law `Q_r` and proves

\[
K_{\rm occ}=D_{\rm KL,2}(P\Vert Q_r)=H_{\max}(r)-H(P)\ge0.
\]
Hence `K_occ=0` is exactly the equation `P=Q_r`.

The named completed **OTHER-account result actually applied** is account02/B13, commit `a63ce409fd2c5ecd1923f0db902e0493cc3c40a7`, `proofnet24/P03-fei/fleet-2026-09-22/account02/B13/.../REPORT.md`, theorem `PROVED_AUXILIARY / SOURCE-EXACT_SELECTOR_IDENTITY`. For a physical selector of bias `p` with `q=1-p`, if `u_S,v_S` are the two child biased-Fourier coefficients, then the parent coefficients are exactly

\[
x_S=q u_S+p v_S,\qquad y_S=\sqrt{pq}(v_S-u_S).
\tag{2.1}
\]
I use the first identity below to rule out an occurrence marginal `r_i=1` for an essential three-variable gate away from `p=1/2`. This is a genuine biased-basis argument; no uniform Walsh integer lattice is imported.

At both startup and prepublication search, the designated partner `account02/B07` had no completed **current FEI** B07 run discoverable in the current scientific root. I therefore do not invent a partner theorem. The account02/B13 theorem above is the named other-account result actually consumed. Older account02/B07 MOC4 reports are suspended history and are not FEI premises.

The current recursive-majority correction is respected: no finite degree cutoff, merged tail, or unweighted-L2 surrogate is used. The calculation is on the complete seven-atom nonempty spectral law.

## 3. Setup

Let `X_1,X_2,X_3` be independent `{0,1}` variables with the **same** interior bias

\[
\Pr[X_i=1]=p,\qquad 0<p<1,
\]

and let `f:{0,1}^3 -> {+1,-1}` depend essentially on all three coordinates. Write

\[
\phi_i(X_i)=\frac{X_i-p}{\sqrt{p(1-p)}},\qquad
\widehat f(S)=\mathbb E[f\phi_S].
\]

Put

\[
v=\sum_{S\ne\varnothing}\widehat f(S)^2
=1-\widehat f(\varnothing)^2,
\qquad
w_S=\frac{\widehat f(S)^2}{v}\quad(S\ne\varnothing).
\]

Thus `w` is the actual normalized nonempty spectral law.

Define the explicit exceptional set

\[
\mathcal E=\{p\in(0,1):F(p)=0\},
\tag{3.1}
\]
where

\[
\begin{aligned}
F(p)={}&(2p-1)(8p^2-8p+1)(2p^2-1)(2p^2-4p+1)\\
&\cdot(18p^2-24p+7)(2p^2-6p+3)(18p^2-12p+1)(2p^2+2p-1).
\end{aligned}
\tag{3.2}
\]

Equivalently, `E` has eleven points:

\[
\frac12,\quad \frac12\pm\frac{\sqrt2}{4},\quad
\frac1{\sqrt2},\quad 1-\frac1{\sqrt2},
\]
\[
\frac{4\pm\sqrt2}{6},\quad
\frac{3-\sqrt3}{2},\quad
\frac{2\pm\sqrt2}{6},\quad
\frac{\sqrt3-1}{2}.
\tag{3.3}
\]

## 4. Full support at zero KL in the generic essential slice

### Lemma 4.1

Assume `p in (0,1)`, `p != 1/2`, `f` depends essentially on all three variables, and `K_occ(f;p)=0`. Then

\[
0<r_i<1\qquad(i=1,2,3),
\tag{4.1}
\]

and consequently every nonempty spectral atom has positive mass:

\[
w_S>0\qquad(S\ne\varnothing).
\tag{4.2}
\]

### Proof

If `r_i=0`, every Fourier coefficient with `i in S` vanishes. Since the product measure has full support, `f` is independent of coordinate `i`, contradicting essentiality.

Suppose `r_i=1`. Then every nonempty coefficient not containing `i` vanishes. In the exact selector notation (2.1), these are the coefficients

\[
x_S=q u_S+p v_S\qquad(S\ne\varnothing)
\]

of the physical conditional expectation

\[
h(x_{-i})=q f(0,x_{-i})+p f(1,x_{-i}).
\]

Thus `h` is constant. But for a Boolean pair `(f(0,y),f(1,y))`, its value lies in

\[
\{1,-1,2p-1,1-2p\}.
\]

For `0<p<1`, `p != 1/2`, these four numbers are distinct. Hence the ordered Boolean pair must be the same for every `y`; `f` is constant or depends only on `i`, contradicting three-variable essentiality. Thus (4.1) holds.

Since `K_occ=0`, `w=Q_r`. In the I-projection, Bernoulli parameters are `t_i=c r_i`, where

\[
1-c=\prod_i(1-c r_i).
\]

If `c=1`, the right side is positive by `r_i<1`, contradiction. Hence `0<c<1`, so every `t_i` lies strictly between zero and one. The conditional product law `Q_r` therefore assigns positive mass to all seven nonempty subsets. This gives (4.2). `QED`

## 5. Three exact toric equations are necessary and sufficient

For positive weights on the seven nonempty subsets of `[3]`, conditional-product structure is equivalent to only three equations.

### Lemma 5.1 — positive three-variable toric criterion

Let all `w_S>0` for `S != empty`. Then `w` is an independent Bernoulli law conditioned on nonemptiness iff

\[
\boxed{w_{12}w_3=w_{13}w_2,}
\tag{5.1}
\]
\[
\boxed{w_{12}w_3=w_{23}w_1,}
\tag{5.2}
\]
\[
\boxed{w_{123}w_1=w_{12}w_{13}.}
\tag{5.3}
\]

### Proof

Necessity is immediate from

\[
w_S=A\prod_{i\in S}z_i,
\qquad A>0,\ z_i>0.
\]

For sufficiency set

\[
A=\frac{w_1w_2}{w_{12}},\qquad
z_1=\frac{w_{12}}{w_2},\qquad
z_2=\frac{w_{12}}{w_1},\qquad
z_3=\frac{w_{13}}{w_1}.
\]

Equations (5.1)–(5.3) reconstruct respectively `w_3,w_23,w_123` and therefore every nonempty weight as `A prod_{i in S} z_i`. Since the weights sum to one,

\[
A\left(\prod_i(1+z_i)-1\right)=1,
\]

which is exactly the normalization of an independent Bernoulli law conditioned on nonemptiness. `QED`

Because the common factor `v^{-2}` cancels in (5.1)–(5.3), they may be tested directly on the seven squared Fourier coefficients.

## 6. Main theorem: generic common-bias arity-three classification

### Theorem 6.1 — `B-ZEROKL-ARITY3-GENERIC-RIGIDITY-v1`

Let `f:{0,1}^3->{+1,-1}` depend essentially on all three coordinates and let all three physical inputs have common bias

\[
p\in(0,1)\setminus\mathcal E.
\]

Then

\[
\boxed{K_{\rm occ}(f;p)=0}
\]

if and only if, up to output sign, `f` is one of the following:

1. a **one-point-defect gate**, i.e. it differs from a constant on exactly one truth-table atom; or
2. **three-bit parity**, equivalently a product of three literals after the `{0,1}` to `{±1}` identification.

In particular, on this entire generic common-bias regime there is **no essential composition-prime arity-three zero-KL gate**.

### Proof

The preceding same-slot report analytically proves that every one-point-defect gate and every biased character has `K_occ=0`, so the displayed families are sufficient.

For necessity, encode a truth table by a mask `m in {0,...,255}`, with bit `k=1` when the lexicographically ordered atom `k` has value `+1`. There are exactly 218 masks depending essentially on all three coordinates.

For each mask, the exact normalized biased coefficient satisfies

\[
\widehat f(S)^2
=\frac{N_{m,S}(p)^2}{[p(1-p)]^{|S|}},
\tag{6.1}
\]

where `N_{m,S}` is obtained by the finite exact expectation

\[
N_{m,S}(p)=\sum_{x\in\{0,1\}^3}
 f_m(x)\Pr_p[X=x]\prod_{i\in S}(x_i-p).
\tag{6.2}
\]

Insert (6.1) into the three toric equations (5.1)–(5.3), clear the nonzero interior denominators, and denote the resulting rational polynomials by

\[
T_{m,1}(p),T_{m,2}(p),T_{m,3}(p)\in\mathbb Q[p].
\]

The exact symbolic certificate archived with this report exhausts the 218 essential masks. Precisely 18 masks make all three polynomials identically zero:

\[
1,2,4,8,16,32,64,105,127,128,150,191,223,239,247,251,253,254.
\tag{6.3}
\]

The sixteen masks in (6.3) other than `105,150` are exactly the eight one-point defects and their output complements. Masks `105,150` are parity and its complement.

For each of the remaining 200 essential masks, the certificate computes

\[
g_m(p)=\gcd(T_{m,j}:T_{m,j}\not\equiv0)
\]

over `QQ[p]`. After removing the boundary factors `p` and `p-1`, **every irreducible factor appearing in any such common gcd** is one of

\[
\begin{gathered}
18p^2-12p+1,\quad 18p^2-24p+7,\quad 2p+1,\quad2p-1,\quad2p-3,\\
2p^2+2p-1,\quad2p^2-1,\quad2p^2-2p+1,\quad2p^2-4p+1,\\
2p^2-6p+3,\quad8p^2-8p+1,\quad8p^2-8p+3.
\end{gathered}
\tag{6.4}
\]

Among these, exactly the eight factors in (3.2) have a root in `(0,1)`. Therefore if `p notin E`, no one of the 200 nonfamily masks can satisfy all three toric equations. By Lemma 4.1 the zero-KL law has full support, and by Lemma 5.1 zero KL is equivalent to those toric equations. Thus only the 18 masks (6.3) remain. This proves the classification. `QED`

The proof is finite and exact: no floating-point root test is needed for the classification. The executable certificate uses SymPy polynomial arithmetic over `QQ[p]`; its archived stdout begins with `PASS`.

## 7. The exceptional set is not merely a proof artifact

The certificate also supplies an exact exceptional witness. Take truth-table mask `7`, i.e. `+1` on `000,001,010` and `-1` on the other five atoms. It is essential in all three variables and is not one of the 18 generic families.

Its seven unnormalized squared biased-Fourier coefficients are

\[
\widehat f_1^2=4p(1-p)^3(p+1)^2,
\]
\[
\widehat f_2^2=\widehat f_3^2=4p^3(1-p)^3,
\]
\[
\widehat f_{12}^2=\widehat f_{13}^2=4p^4(1-p)^2,
\]
\[
\widehat f_{23}^2=4p^2(1-p)^4,
\qquad
\widehat f_{123}^2=4p^3(1-p)^3.
\tag{7.1}
\]

All are positive in the interior. The three toric numerators factor as

\[
0,\qquad
-16p^3(p-1)^5(2p^2-1),\qquad
-16p^4(p-1)^4(2p^2-1).
\tag{7.2}
\]

Hence at the exact algebraic bias

\[
\boxed{p=1/\sqrt2}
\]

all three toric equations hold, so by Lemma 5.1 the complete nonempty spectral law is exactly conditional product and

\[
\boxed{K_{\rm occ}=0.}
\]

Thus at least one point of `E` genuinely supports an additional zero-KL truth table. The exceptional locus cannot simply be deleted by claiming the gcd list is an artifact of clearing denominators.

This witness is a counterexample only to the extension of the **generic arity-three classification through all biases**. It is not a counterexample to FEI.

## 8. How the result changes the Path-B proof search

The previous equality bank showed that biased zero-KL is much larger than the balanced character-times-bent family. The present theorem nevertheless recovers a sharp rigidity statement after two restrictions: three essential inputs and a generic common bias.

For Path B this gives a useful local conclusion. At generic common bias, every arity-three source with `K_occ=0` is composition-decomposable through binary gates: a one-point-defect is a nested AND/OR/literal clause, and parity is a nested XOR/product of literals. Therefore any **composition-prime** arity-three source at such a bias has strictly positive `K_occ`.

What this theorem does **not** supply is a uniform quantitative lower bound on `K_occ`; a sequence can approach the finite exceptional set or a decomposable equality family. Such a quantitative statement would need distance-to-locus information and must still respect the recursive-majority multiscale barrier.

The exact restriction I-projection chain rule from account01/B15 is compatible with this picture: it preserves weighted child `K_occ` with coefficient one but includes the genuine negative Jensen-Shannon mixture term. Therefore a useful next step is not to throw away that term, but to classify or quantitatively separate the exceptional arity-three equality strata in a way that can be inserted into the physical restriction ledger.

## 9. First surviving missing implication

The next source-valid target is now:

> **`B-ZEROKL-ARITY3-EXCEPTIONAL-CLASSIFICATION-v1` (OPEN).** For each of the eleven common biases in `E`, classify all essential three-input Boolean truth tables satisfying the three toric equations, and determine which are composition-prime under the project’s exact disjoint-composition definition.

After that finite exceptional slice, the genuinely higher-dimensional target remains:

> **`B-ZEROKL-PRIME-RIGIDITY-v2` (OPEN).** For essential composition-prime gates of arity at least four under interior product bias, describe the zero set of the full conditional-product toric ideal intersected with the exact biased Boolean multiplication equations, and prove that away from an explicit algebraic exceptional locus it is empty or belongs to a controlled decomposable equality family.

The arity-three theorem suggests an algebraic strategy: use the occurrence-I-projection toric ideal first, then intersect it with the actual biased Boolean source equations; do not invoke the uniform Walsh lattice except on the balanced uniform slice where its hypotheses genuinely hold.

## 10. Certificate and provenance

Exact certificate source:

`proofnet24/P03-fei/fleet-2026-09-22/account01/B07/account01-B07-20260922T110315Z-fei/verify_arity3_zero_kl.py`

Creation commit: `7bf0ab0a25fbde5aa6d5da6e49b0d1655c7d1088`.

Archived exact stdout:

`proofnet24/P03-fei/fleet-2026-09-22/account01/B07/account01-B07-20260922T110315Z-fei/verify_arity3_zero_kl.out`

Creation commit: `26dd7aed602c52a92b0e8b98774f8df751f9195d`.

The certificate was executed in this invocation with exact symbolic polynomial arithmetic and returned `PASS`. This is author-side computational verification of the stated finite enumeration, not an independent end-to-end review. The analytic reductions in Sections 4–5 are included so the computation is restricted to the finite truth-table/polynomial factorization step.

A scoped manual privacy review of the new scientific files found only mathematical text/code and no credentials, account secrets, scheduler identifiers, machine paths, benchmark material, or unrelated private data.
