# fleet03/B18 — balanced excess I-projection target and complement-parity Boolean credit

**Run:** `20260922T0857Z-fleet03-B18-r11`  
**Classification:** `ESSENTIAL_STEP_APPLIED / COMMON_TARGET_RENORMALIZED / BOOLEAN_DEPENDENCE_CREDIT`.  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Exact common candidate and source correction

This run replaces the now-refuted fixed-potential target by one immutable potential-free Shannon target:

`B-BALANCED-IPROJECTION-v1`.

For a balanced Boolean function

\[
f:\{-1,1\}^n\to\{-1,1\},\qquad \mathbb E f=0,
\]

let

\[
P(S)=\widehat f(S)^2,\quad r_i=P(i\in S)=\operatorname{Inf}_i(f),\quad
\mu=\sum_i r_i=I(f).
\]

Since `f` is balanced, `P(\varnothing)=0`.  Let `Q_r` be the maximum-entropy law on nonempty subsets with coordinate marginals `r`, exactly as in the completed fleet02/B15 I-projection theorem.  Put

\[
H_{\max}(r)=H(Q_r),\qquad
K_{\rm occ}(f)=D_{\rm KL,2}(P\Vert Q_r)=H_{\max}(r)-H(f).
\]

The common target is to prove that there is one finite dimension-independent `C` such that

\[
\boxed{
\mathcal R_C(f):=K_{\rm occ}(f)+C(\mu-1)-H_{\max}(r)\ge0
}
\tag{B1}
\]

for **every balanced Boolean** `f` in every dimension.  By the identity above,

\[
\mathcal R_C(f)=C(I(f)-1)-H(f).
\tag{B2}
\]

Section 2 proves that (B1), for all balanced Boolean functions, is equivalent to full FEI with the **same constant** `C`.  Thus this is not a non-Boolean relaxation or a weaker surrogate.  The I-projection split is retained because it isolates the exact Boolean dependence credit that the common Shannon programme has to pay.

The previously used fixed potential

\[
\Gamma^\dagger=\Gamma_0+0.268204856\,p(1-p)
\]

is no longer treated as universal: the newest completed fleet02/B15 report records a source-certified biased composition-prime Numaro instance with negative `D_{\Gamma^\dagger}`.  The exact Gibbs/I-projection identities survive, but the obsolete fixed-potential universal claim does not.

## 1. Named completed cross-account result consumed substantively

The exact completed peer result used here is fleet02/B15

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B15/20260922T0829Z-influence-iprojection-kl/REPORT.md`

at creation commit

`4bd6d05f1eb8325d665f2748f4d74dcee2550a04`, report blob

`5ce14eaaec34f0d91f2d430dba576e19dddc6894`.

Its Theorems 2.1 and 3.1 prove the following exact facts.  For a probability law `P` on nonempty subsets with coordinate marginals `r_i` and `\mu=\sum_i r_i>1`, there is a unique positive `c\in(0,1]` satisfying

\[
1-c=\prod_i(1-c r_i).
\tag{1.1}
\]

Writing `t_i=c r_i`, independent Bernoulli(`t_i`) bits conditioned on being nonempty give `Q_r`, and

\[
H_{\max}(r)={\sum_i h_2(c r_i)-h_2(c)\over c},
\qquad
K_{\rm occ}=H_{\max}(r)-H(P).
\tag{1.2}
\]

Moreover this is the full conditional-product I-projection: for every conditional-product Gibbs law `\nu_y^+`,

\[
D(P\Vert\nu_y^+)=K_{\rm occ}+D(Q_r\Vert\nu_y^+).
\tag{1.3}
\]

The peer left the exact signed-Boolean dependence payment `K_occ` as the first genuinely unpaid Shannon term.  The present run applies that theorem to an equivalent full-FEI normalization and proves a new all-dimensional lower bound on `K_occ` from the Boolean convolution equations.

## 2. Same-constant equivalence: full FEI iff balanced excess FEI

### Theorem 2.1

For a constant `C<\infty`, the following are equivalent.

1. For every Boolean `g`,
   \[
   H(g)\le C I(g).
   \tag{2.1}
   \]
2. For every balanced Boolean `f`,
   \[
   H(f)\le C\,[I(f)-1].
   \tag{2.2}
   \]

Thus `B-BALANCED-IPROJECTION-v1`, equation (B1), is exactly a same-constant formulation of full FEI.

### Proof: (2.2) implies (2.1)

Given arbitrary Boolean `g(x)`, add one fresh uniform sign `z` and define

\[
f(z,x)=z\,g(x).
\]

Then `f` is balanced.  Its Fourier spectrum is the spectrum of `g` with the fresh coordinate adjoined to every spectral set.  Hence

\[
H(f)=H(g),\qquad I(f)=I(g)+1.
\]

Applying (2.2) gives

\[
H(g)=H(f)\le C[I(f)-1]=C I(g).
\]

### Proof: (2.1) implies (2.2)

Fix balanced Boolean `f` and write

\[
\mu=I(f),\qquad h=H(f).
\]

If `\mu=1`, Poincare equality puts every Fourier atom on level one.  Thus

\[
f=\sum_i b_i\chi_i.
\]

Since `f^2\equiv1`, every cross coefficient `2b_i b_j` vanishes, so at most one `b_i` is nonzero; normalization makes `f` a character up to sign and `h=0`.  Therefore (2.2) holds.

Assume `\mu>1`.  Define `F_1=f`, and recursively form `F_{m+1}` by using `f` as an outer gate and plugging one independent disjoint copy of `F_m` into each input.  Because every `F_m` is balanced, the outer gate always sees independent uniform signs.  The spectral composition law is exact: the outer spectral set is recoverable from the final set because every active inner block contributes a nonempty spectral set.  Therefore

\[
I(F_{m+1})=\mu I(F_m),
\qquad
H(F_{m+1})=h+\mu H(F_m).
\tag{2.3}
\]

Inductively,

\[
I(F_m)=\mu^m,
\qquad
H(F_m)=h\,{\mu^m-1\over\mu-1}.
\tag{2.4}
\]

Applying full FEI (2.1) to every finite `F_m` gives

\[
h\,{1-\mu^{-m}\over\mu-1}\le C.
\]

Letting `m\to\infty` yields `h\le C(\mu-1)`, proving (2.2).  `QED`

This equivalence accounts for the recurring `H/(I-1)` composition ratios in the current lower-bound constructions: they are not merely convenient diagnostics; their universal boundedness is exactly FEI.

## 3. New theorem: complement-parity lower bound on the irreducible KL

The peer I-projection leaves `K_occ` as the only information term not already explained by the individual occurrence marginals.  Booleanity gives an explicit nonzero payment away from a reducible boundary.

### Theorem 3.1 — complement-parity Boolean credit

Let `f` be balanced Boolean, `\mu=I(f)>1`, and define `c,Q_r,t_i=c r_i` by (1.1).  With the convention that the right side is zero when any `t_i\in\{0,1\}`,

\[
\boxed{
K_{\rm occ}(f)
\ge
\Delta_{\rm comp}(r)
:=
{1\over c^2\ln2}
\prod_{i=1}^n t_i(1-t_i).
}
\tag{3.1}
\]

If all active marginals satisfy `0<r_i<1`, then `0<c<1`, all `0<t_i<1`, and the right side is strictly positive.

### Proof

Write the signed Fourier coefficients as

\[
a_S=\widehat f(S),\qquad P(S)=a_S^2.
\]

For every nonempty `U`, Booleanity `f^2\equiv1` gives the exact signed convolution identity

\[
C_a(U):=\sum_S a_S a_{S\triangle U}=0.
\tag{3.2}
\]

Choose signs for a comparison vector `b` by

\[
b_\varnothing=0,
\qquad
b_S=\operatorname{sgn}(a_S)\sqrt{Q_r(S)}\quad(S\ne\varnothing),
\tag{3.3}
\]

with arbitrary sign where `a_S=0`.  Then `\|a\|_2=\|b\|_2=1`.

Take `U=[n]`, so `S\triangle U=S^c`.  For every proper nonempty `S`, the conditional-product formula gives

\[
Q_r(S)Q_r(S^c)
={1\over c^2}\prod_i t_i(1-t_i).
\tag{3.4}
\]

Set

\[
m={1\over c}\sqrt{\prod_i t_i(1-t_i)}.
\tag{3.5}
\]

The proper nonempty subsets form exactly

\[
2^{n-1}-1
\]

unordered complementary pairs.  This number is odd.  Each pair contributes either `+2m` or `-2m` to `C_b([n])`; the pair `{\varnothing,[n]}` contributes zero because `b_\varnothing=0`.  Hence

\[
|C_b([n])|\ge2m.
\tag{3.6}
\]

Let `T` be the unitary permutation `Tb(S)=b(S^c)`.  From (3.2), `C_a([n])=0`, and therefore

\[
2m
\le |\langle b,Tb\rangle-\langle a,Ta\rangle|
\le 2\|a-b\|_2.
\tag{3.7}
\]

Thus

\[
\|a-b\|_2^2\ge m^2.
\tag{3.8}
\]

Because the signs in (3.3) are aligned,

\[
\|a-b\|_2^2
=\sum_S(\sqrt{P(S)}-\sqrt{Q_r(S)})^2
=2[1-\operatorname{BC}(P,Q_r)],
\tag{3.9}
\]

where `BC` is the Bhattacharyya coefficient.  Monotonicity of Renyi divergence, or directly the order-1/2 bound, gives

\[
D_{\rm KL,2}(P\Vert Q_r)
\ge -2\log_2\operatorname{BC}(P,Q_r)
\ge {2[1-\operatorname{BC}(P,Q_r)]\over\ln2}.
\tag{3.10}
\]

Combining (3.8)--(3.10) proves (3.1).  `QED`

No unsigned probability-law relaxation can prove (3.1): it uses the signed Boolean convolution equation (3.2) and the odd number of surviving complementary pairs.

## 4. Exact equality branch and minimal-counterexample consequence

### Corollary 4.1

If a balanced Boolean `f` has `K_occ(f)=0`, then one of the following holds.

1. `I(f)=1`, in which case `f` is a character up to sign; or
2. some coordinate `j` has `r_j=\operatorname{Inf}_j(f)=1`.

In case 2 every Fourier set contains `j`, so

\[
g=\chi_j f
\]

is Boolean and independent of coordinate `j`, with

\[
H(g)=H(f),\qquad I(g)=I(f)-1.
\tag{4.1}
\]

Thus exact I-projection equality is a reducible character-lift branch for the balanced-excess target.  In particular a minimum-dimensional counterexample to (B1), after deleting irrelevant coordinates, cannot have `K_occ=0`.

### Proof

For `\mu>1`, if no `r_i` equals one after irrelevant coordinates are removed, then all `0<r_i<1`.  Equation (1.1) cannot have `c=1`, because its right side would be `\prod_i(1-r_i)>0`; hence `0<c<1`.  Theorem 3.1 then gives `K_occ>0`, contradiction.  Therefore some `r_j=1`.  Since the total spectral mass is one, `P(i\notin S)=0` for `i=j`, so every nonzero Fourier coefficient contains `j`.  Multiplication by `\chi_j` removes `j` from every spectral set and proves (4.1).  `QED`

This solves the exact-equality subproblem from the peer report at the level actually needed by a minimal-counterexample argument: the dangerous conditional-product manifold has no irreducible interior balanced Boolean point.

## 5. Applying the new credit to the common target

Substituting Theorem 3.1 into (B1) gives the source-exact sufficient region

\[
\boxed{
H_{\max}(r)
\le
C(\mu-1)+\Delta_{\rm comp}(r)
\quad\Longrightarrow\quad
H(f)\le C[I(f)-1].
}
\tag{5.1}
\]

Equivalently, every balanced counterexample to FEI at constant `C` must satisfy

\[
\boxed{
H_{\max}(r)-C(\mu-1)>
{1\over c^2\ln2}\prod_i t_i(1-t_i),
}
\tag{5.2}
\]

as well as all signed Boolean equations.  The bound is dimension-dependent through the product and therefore does **not** close FEI.  It is a real paid arrow in the exact common proof chain, not a claimed universal constant.

A second exact payment, useful for the builders, is ordinary data processing.  Let `\Pi_d` retain every individually labelled atom `S` with `1\le |S|\le d` and merge all remaining sets into one tail symbol.  Then

\[
\boxed{
K_{\rm occ}(f)
\ge
\Delta_d(f;r)
:=D_{\rm KL,2}(\Pi_dP\Vert\Pi_dQ_r).
}
\tag{5.3}
\]

This explicitly charges coordinate identities: singleton and pair labels are not merged with one another.  It is a Shannon projection, not a non-Boolean assertion.  What remains open is a dimension-free Boolean lower bound on one such source-valid dependence credit in precisely the region where `H_max(r)-C(\mu-1)>0`.

## 6. Decisive refutation attempt: singleton information alone is insufficient already at n=4

The deterministic checker beside this report enumerates every balanced Boolean function through `n=4` and tests the exact identities and lower bounds.  For orientation only it uses

\[
C_{\rm diag}=6.521851214;
\]

this number is **not** asserted here to be a proved universal FEI upper constant.

The combination of complement parity (3.1) with the fully coordinate-labelled singleton projection `\Delta_1` fails to certify **192** balanced four-variable truth tables.  A first explicit witness has negative vertices

`(0,1,2,3,4,5,8,10)`

in lexicographic binary order.  Its exact/diagnostic values are

\[
I=3/2,\qquad H=3,
\]

\[
H_{\max}(r)=3.3192810811465\ldots,
\qquad
K_{\rm occ}=0.3192810811465\ldots,
\]

\[
\Delta_{\rm comp}=0.00323941420485\ldots,
\qquad
\Delta_1=0.0192919823040\ldots.
\]

Hence the proposed lower bound using only `max(Delta_comp,Delta_1)` leaves residual

\[
-0.0390634918425\ldots<0,
\]

even though the **actual** balanced-excess residual is positive:

\[
C_{\rm diag}(I-1)-H
=0.260925607\ldots>0.
\]

So the stronger shortcut

> complement parity plus singleton-label information alone pays the full dangerous Shannon deficit

is **REFUTED**.  This is a failure of the proposed proof mechanism, not a counterexample to FEI.

For comparison, the same finite checker finds that retaining all individually labelled atoms through level two, `\Delta_2`, certifies every balanced truth table through `n=4` at `C_diag`.  That is finite evidence only; no all-dimensional `\Delta_2` theorem is claimed.

## 7. Smallest honest proof chain after this run

The complete common Campaign-B chain is now:

1. **PROVED:** full FEI at constant `C` is equivalent to balanced excess FEI `H(f)\le C(I(f)-1)` with the same `C` (Theorem 2.1).
2. **PROVED, consumed from fleet02/B15:** the balanced spectral entropy is
   \[
   H(f)=H_{\max}(r)-K_{\rm occ}(f).
   \]
3. **PROVED here:** in the irreducible interior,
   \[
   K_{\rm occ}\ge\Delta_{\rm comp}>0,
   \]
   and exact equality reduces by a character coordinate to lower dimension.
4. **PROVED here:** every labelled low-level coarse graining `\Delta_d` is an additional valid lower bound on `K_occ`.
5. **REFUTED here:** `max(Delta_comp,Delta_1)` is enough universally; 192 genuine balanced `n=4` sources already escape that payment.
6. **UNPAID / DECISIVE:** prove one finite `C` for which
   \[
   K_{\rm occ}(f)\ge H_{\max}(r)-C(\mu-1)
   \tag{7.1}
   \]
   for every irreducible balanced Boolean source, using enough signed Boolean dependence structure; or construct a genuine Boolean family showing this exact inequality unbounded for every finite `C` (which would disprove FEI).

Equation (7.1) is now the single immutable Campaign-B target.  It keeps the actual source signs, original coordinate labels, every negative information credit, and all dimensions.

## 8. Next recipients

- **fleet02/B15:** apply its I-projection machinery to (7.1) and attempt a quantitative lower bound from additional signed convolution equations beyond the full-complement parity equation; preserve `K_occ` rather than returning to a scalar Gibbs normalizer.
- **fleet01/B12:** combine its proved dominant-character endpoint bound with `Delta_2` or another labelled low-level projection, so the leakage is paid by actual excess level rather than a single binary tail entropy.
- **fleet02/B17:** adversarially test **this exact target/version** on recursive majority, tribes, Numaro/shared-graft seeds, sparse balanced defects and tensors; specifically test whether fixed-depth `Delta_d` can fail as dimension grows.
- **fleet04/B15:** compare its packet/price split to the same `K_occ` target and identify which packet credits survive after the full influence I-projection.

Do not revive the globally refuted fixed `Gamma^dagger` claim.  A new all-gate potential may still be useful, but Campaign B no longer needs one merely to state the exact full-FEI Shannon target.

## 9. Status

**Old missing implication:** force enough residual KL from signed Boolean realizability in the low-price Gibbs region for a fixed all-gate candidate.

**New proved inference:** full FEI is reduced with the same constant to the potential-free balanced I-projection inequality (7.1); the exact I-projection equality branch is reducible; and every irreducible interior source has the explicit complement-parity KL payment (3.1).

**Exact failed claim:** complement parity plus all singleton-labelled KL information already pays the target.  It fails on 192 balanced `n=4` functions at the diagnostic constant.

**Replacement obligation:** derive a dimension-free payment from pair/higher signed convolution structure, or find a genuine asymptotic Boolean adversary to (7.1).  A finite `Delta_2` check is not closure.

**Peer artifact consumed:** fleet02/B15 `20260922T0829Z-influence-iprojection-kl`, commit `4bd6d05f1eb8325d665f2748f4d74dcee2550a04`.

**Implication to full FEI:** proving (7.1) for one finite `C` and all balanced Boolean functions proves full FEI with exactly the same `C`; no additional potential or arity passage is required.

**Full FEI remains OPEN / NOT PROVED.**

No novelty or publication-priority claim is made for standard I-projection or composition facts.  No credentials, scheduler identifiers, machine paths, unrelated private material, held-out benchmark content, email/Drive data, paid services, workflow dispatch, permission changes or public-posting actions are included.