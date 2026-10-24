# B17 — exact gate-composition margin law and a Numaro-scale quadratic repair

**Run:** `20260922T004252Z-b17-fei-r14`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status:** `CANDIDATE_REFUTED` for the old read-once potential; `AUXILIARY_ONLY` for the replacement.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED**.

## 0. Live target and newest compatible peer result

The live owner target is the all-gate reformulation

\[
\Gamma(p_{\rm out})+H_t(G;p)
\le \sum_i \operatorname{It}_i(G;p)
\frac{\Gamma(p_i)+h(V_{p_i})}{V_{p_i}},\qquad V_p=4p(1-p),
\tag{G}
\]

with gate defect `D_G = RHS-LHS` and Poincare defect

\[
W_G:=I(G;p)/4-p_{\rm out}(1-p_{\rm out})\ge0.
\]

For the requested-margin convention in the live gate report,

\[
c_G=-D_G/W_G \qquad (W_G>0),
\]

so **larger** `c_G` is worse.

The newest compatible other-account B15 result I consumed is

`account03/B15/20260922T002607Z-readonce-gamma-counterexample/REPORT.md`, blob
`e49efe403698395b700278d067c245c12a7b15eb`.

It applies the published balanced n=18 Numaro seed with exact influence `261/128` and a certified entropy interval to the gate inequality. At uniform bias it proves

\[
6.5218457109230465756581439729485784683666622922105
\le \frac{H(G)}{I(G)-1}
\le
6.5218457109230465756581439729485784683666622931729.
\tag{0.1}
\]

Therefore the old read-once potential with cap `C0=6.4548` is already refuted as a universal all-gate potential: the seed asks for

\[
0.2681828436921863026325758917943138734666491688420
\le c_G\le
0.2681828436921863026325758917943138734666491726916,
\tag{0.2}
\]

far above the old AND margin `0.0043974201`. I do not repeat that witness. The replacement below starts at the scale forced by (0.1).

The earlier account01/B15 negative-softplus result is also conceptually relevant: it showed that dropping signed/KL credits makes the Shannon remainder strictly harder. The composition calculation below is the gate analogue: the child defects are retained with their signs instead of being discarded in a blind arity induction.

## 1. Exact composition law for gate defects

Let an outer Boolean gate `A` have inputs indexed by `j=1,...,m`. Feed its `j`th input by a Boolean gate `B_j` on a disjoint fresh block. Write `q_j` for the output bias of `B_j`, and let

\[
\alpha_j:=\frac{\operatorname{It}_j(A;q)}{V_{q_j}}.
\]

The standard biased composition identities underlying (G) give

\[
I(A\circ(B_1,\ldots,B_m))=\sum_j\alpha_j I(B_j),
\tag{1.1}
\]

and

\[
H_t(A\circ(B_1,\ldots,B_m))
=H_t(A;q)+\sum_j\alpha_j\bigl(H_t(B_j)-h(V_{q_j})\bigr).
\tag{1.2}
\]

Insert the definition of each child defect into the right side of (G). Every child contributes its full signed defect, and the remaining terms are exactly the outer defect. Thus

\[
\boxed{
D_{A\circ B}=D_A+\sum_j\alpha_jD_{B_j}.
}
\tag{1.3}
\]

This is an identity, not an inequality.

The Poincare defect has the parallel identity. Since
`q_j(1-q_j)=V_{q_j}/4`, (1.1) gives

\[
\begin{aligned}
W_{A\circ B}
&=\frac14\sum_j\alpha_j I(B_j)-p_{\rm out}(1-p_{\rm out})\\
&=W_A+\sum_j\alpha_jW_{B_j}.
\end{aligned}
\tag{1.4}
\]

Consequently, whenever the displayed denominators are positive,

\[
\boxed{
 c_{A\circ B}
 =\frac{W_Ac_A+\sum_j\alpha_jW_{B_j}c_{B_j}}
        {W_A+\sum_j\alpha_jW_{B_j}}.
}
\tag{1.5}
\]

Zero-Poincare-defect dictator/constant factors are handled directly (or by the corresponding continuous boundary limit) and do not create a larger margin.

### Consequence

For every decomposable gate instance,

\[
\boxed{c_{A\circ B}\le \max\{c_A,c_{B_1},\ldots,c_{B_m}\}.}
\tag{1.6}
\]

Thus a decomposable gate can never be the first source of a larger required margin. Any universal extremality proof can reduce recursively to composition-prime gate instances. This is the exact slack-preserving arity induction that the live owner note says the naive Shannon expansion was missing: dropping the child terms in (1.3) destroys the weighted-average law.

This theorem holds for **any** symmetric potential `Gamma`; it is not tied to the refuted read-once shape.

## 2. Canonical one-parameter repair at the Numaro scale

Let `Gamma_0` be the old read-once candidate, with `Gamma_0(1/2)=C0=6.4548`, and define

\[
\Gamma_c(p):=\Gamma_0(p)+c\,p(1-p).
\tag{2.1}
\]

For every gate instance,

\[
D_G(\Gamma_c)=D_G(\Gamma_0)+cW_G.
\tag{2.2}
\]

Therefore the old margin `c_G` is *exactly* the smallest quadratic correction needed by that gate instance. This makes the n=18 counterexample prescribe a canonical first repair rather than merely killing the old candidate.

Let `c_*` be the Numaro value from (0.2), and choose its certified upper endpoint if a one-sided safe value is desired. Then

\[
\Gamma_*(p):=\Gamma_0(p)+c_*p(1-p)
\tag{2.3}
\]

has cap

\[
\Gamma_*(1/2)=C_0+c_*/4
=\frac{H(G_{18})}{I(G_{18})-1}
\approx6.5218457109230466.
\tag{2.4}
\]

At uniform bias the Numaro seed is exactly binding up to the certified entropy interval. More generally, every gate instance whose old required margin is at most `c_*` satisfies (G) for `Gamma_*`.

Equation (1.5) gives a nontrivial closure property: if a collection of factor instances all require at most `c_*`, then **every disjoint gate composition built from those same instances also requires at most `c_*`**. In particular, recursive self-compositions of the balanced Numaro seed do not create a larger margin: their margin remains the seed margin, matching the peer's exact asymptotic identity.

This is only a replacement **candidate**. A universal proof still has to show that no composition-prime gate/bias instance asks for more than `c_*`; a single such instance refutes (2.3).

## 3. Exact sparse arity-5 boundary calculation

I executed a new exact-integer Walsh classification for five-input gates at uniform input bias whose minority output support `A` has dyadic size `|A|=1,2,4`. This is not the already-run NPN grid.

For `|A|=1`, every set is a vertex face and gives the symmetric `AND_5` instance.

For `|A|=2`, every two-set has the same nonconstant Walsh magnitude multiset: fifteen nonzero indicator coefficients of magnitude `2`. Hence its spectral entropy depends only on `|A|`. Its total influence is minimized exactly when the two vertices are adjacent. There are `80` such coordinate edges and `416` nonedges. Relative to the adjacent `AND_4`-with-dummy instance, every nonedge raises influence by `1/8` with **no entropy change**, so its old gate defect increases by `C0/8>0`; hence its required margin is strictly negative.

For `|A|=4`, there are two affine-rank types.

* rank 2: the indicator has seven nonconstant Walsh sums of magnitude `4` and no magnitude-`2` sums. All such sets therefore have the same entropy as a two-dimensional affine plane. There are `1240` affine planes. Only the `80` coordinate square faces have four internal cube edges and attain the minimum influence `3/4`; all skew planes have larger influence and therefore strictly smaller required margin.
* rank 3: every four-set has exactly three nonconstant Walsh sums of magnitude `4` and sixteen of magnitude `2`. Compared with a coordinate square, its entropy is **exactly larger by `1/2` bit**. Every rank-3 four-set has at most three internal cube edges, hence influence at least `7/8`, an increase of at least `1/8`. Its defect gap is therefore at least

\[
\frac{C_0}{8}-\frac12
=\frac{6137}{20000}>0.
\tag{3.1}
\]

Thus, under the live candidate's dyadic AND-chain normalization,

\[
\boxed{
c_G(1/2,\ldots,1/2)\le0
\quad\text{for every five-input gate with }|A|\in\{1,2,4\},
}
\tag{3.2}
\]

with equality precisely on the corresponding coordinate faces. The closest rank-3 four-set has descriptive margin

\[
-\frac{8(C_0-4)}7=-2.8054857142857\ldots .
\]

So the first sparse dyadic arity-5 layers do **not** produce a replacement adversary; their extremizers collapse to decomposable coordinate faces.

## 4. Exact Boolean perturbation stress test around the n=18 seed

The checker reconstructs the published 18-variable seed from the already-recovered ten slices and refuses it unless the complete truth-table SHA-256 is

`f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839`.

It recovers `I=261/128` exactly. I then performed a deterministic sample of `5000` **balanced Boolean two-point swaps** (one `+1` point flipped to `-1` and one `-1` point flipped to `+1`), recomputing the entire Walsh spectrum each time. This preserves Boolean realizability and balance, so the uniform-bias gate target is still exactly `H/(I-1)`.

No sampled swap exceeded the seed. The best sampled neighbor had

\[
H=6.777132773744987,\qquad I=2.0391845703125,
\]

and

\[
\frac{H}{I-1}=6.521587182252899,
\]

which is lower than the seed by about `2.5852867e-4`.

This is **finite numerical stress evidence only**, not an exhaustive local-optimality theorem. The Boolean truth tables and Walsh transforms are exact integers; the entropy comparisons in this subsection are binary64 descriptive values. The certified seed interval remains the authoritative value for `c_*`.

## 5. What changed and what remains

**Refuted predecessor:** universal validity/extremality of the read-once `Gamma_0`; the newest account03/B15 result already settles that negatively.

**New proved inference:** exact signed defect and Poincare-defect composition laws (1.3)-(1.5), hence decomposable-gate margins are weighted averages of factor margins.

**Executed replacement:** the canonical Numaro-scale quadratic repair `Gamma_* = Gamma_0 + c_*p(1-p)`. It is minimal within this one-parameter family at the balanced seed, stable under disjoint composition of already-paid factor instances, and survives the new sparse arity-5 exact classification plus the finite balanced perturbation stress test.

**First remaining decisive implication:** either

1. prove `c_G^{(0)}(p) <= c_*` for every composition-prime Boolean gate and every bias vector, which would make `Gamma_*` a universal all-gate potential and prove FEI with cap about `6.521845711`; or
2. construct one exact Boolean prime gate/bias instance with `c_G^{(0)}(p)>c_*`, then lift the cap/shape again rather than returning to the dead read-once candidate.

No claim of full FEI, publication priority, or interval-certified arity-5 universality is made.

## 6. Executed checker

`check_gate_margin_repair.py` uses exact integer Walsh sums for the sparse five-input classification and exact truth-table/Walsh reconstruction for the n=18 seed. Its deterministic perturbation entropy ratios are explicitly descriptive floating-point stress data.

Executed checker SHA-256:

`98d9d87f7b3c376d01e2033038dd53c7736fa841256a421b1e701637bc12b58b`

Sanitized checker-output SHA-256:

`15e3d4eed690b7d8ad288a67482f377b54029fc7305113bd043bda3e2d46058d`
