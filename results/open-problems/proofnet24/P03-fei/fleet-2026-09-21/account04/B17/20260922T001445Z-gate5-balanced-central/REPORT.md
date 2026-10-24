# B17 FEI — exact arity-5 balanced central-slice exclusion

**Run:** `20260922T001445Z-b17-fei-r13`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status:** **ESSENTIAL_STEP_APPLIED / exact computer-assisted exclusion of one full arity-5 central slice. Full uniform-cube FEI remains OPEN / NOT PROVED.**  
**Publication priority:** UNVERIFIED; no novelty claim.

## 0. Live target and scope

The live owner control changed during this invocation. The older slot prompt named the joint interface-D remainder-adversary task, but control revision `2026-09-22.2` gives every FEI worker one converged target: the gate reformulation in

`proofnet24/P03-fei/continuations/2026-09-22-gate-reformulation/REPORT.md`.

For a Boolean gate `G` on `k` independent biased inputs, the exact target is

\[
\Gamma(p_{\rm out})+\operatorname{Ht}_G(p)
\le
\sum_i \operatorname{It}_i(G;p)
\frac{\Gamma(p_i)+h(V_{p_i})}{V_{p_i}},
\qquad
V_p=4p(1-p).
\tag{0.1}
\]

The source report proves that a symmetric nonnegative `Gamma` satisfying (0.1) for every gate and every bias vector is equivalent to FEI. It also defines the gate margin

\[
c_G(p)=
\frac{-D_G(p)}
{I(G;p)/4-p_{\rm out}(1-p_{\rm out})},
\tag{0.2}
\]

where `D_G` is the right side of (0.1) minus the left side. The current read-once fixed-point candidate has

\[
C_0:=\Gamma(1/2)=6.4548.
\tag{0.3}
\]

The current multi-start two-input AND certificate requires margin about

\[
c_{\rm AND}^{\max}=4.3974201\times10^{-3},
\tag{0.4}
\]

so a genuinely five-input gate with a larger value would falsify the observed AND-extremality picture. Arity five was identified by the owner as the first untouched gate arity.

This report eliminates one exact but substantial slice of that adversarial search:

> all five input biases equal `1/2`, and the gate output is balanced.

No claim is made for nonuniform biases or unbalanced output.

## 1. Central-slice reduction

Let `G:{0,1}^5 -> {-1,1}` be balanced under the uniform law. Put

\[
p_i=\frac12\quad(1\le i\le5),
\qquad
p_{\rm out}=\frac12.
\]

Then `V_{p_i}=1`, `h(V_{p_i})=h(1)=0`, and
`\Gamma(p_i)=\Gamma(p_{\rm out})=C_0`. The biased gate spectrum is the ordinary uniform Walsh spectrum. Therefore

\[
D_G=C_0 I(G)-H(G)-C_0
=C_0(I(G)-1)-H(G).
\tag{1.1}
\]

Poincare gives `I(G)>=1`. For a non-dictator, `I(G)>1`, and (0.2) becomes exactly

\[
\boxed{
c_G(1/2,\ldots,1/2)
=
4\left(\frac{H(G)}{I(G)-1}-C_0\right).
}
\tag{1.2}
\]

Thus the central-slice adversary question is reduced to bounding
`H/(I-1)` for balanced five-bit functions.

## 2. Main theorem

### Theorem 2.1 — balanced five-bit central slice

For every balanced Boolean function `G:{0,1}^5 -> {-1,1}`,

\[
\boxed{H(G)\le 6\,(I(G)-1).}
\tag{2.1}
\]

For dictators and their negations, `I=1`, `H=0` and both sides vanish.
For every non-dictator,

\[
\boxed{
c_G(1/2,\ldots,1/2)
\le
4(6-6.4548)
=
-1.8192.
}
\tag{2.2}
\]

Consequently no balanced five-input gate at the uniform bias point can challenge the positive two-input AND margin (0.4).

The proof is analytic for all functions of sufficiently large edge boundary and exact exhaustive integer verification for the finite low-boundary sector.

## 3. Large-boundary proof by a Gibbs envelope

Let `A={x:G(x)=-1}`. Balancedness gives `|A|=16`. Let `B` denote the number of undirected five-cube edges crossing `A,A^c`. Then

\[
I(G)=\frac{B}{16}.
\tag{3.1}
\]

Because the cube is 5-regular,

\[
B=5|A|-2e(A)=80-2e(A),
\tag{3.2}
\]

so `B` is even.

Let

\[
q_S=\widehat G(S)^2
\]

be the squared Walsh spectral law. Balancedness gives `q_emptyset=0`.
On the 31 nonempty subsets define the comparison law

\[
r_S=\frac{3^{-|S|}}{Z},
\qquad
Z=\sum_{\varnothing\ne S\subseteq[5]}3^{-|S|}
=\left(1+\frac13\right)^5-1
=\frac{781}{243}.
\tag{3.3}
\]

Nonnegativity of `D(q||r)` gives

\[
H(G)
\le
\log_2 Z + I(G)\log_2 3.
\tag{3.4}
\]

If `B>=28`, then `I>=7/4`. At `I=7/4`, (3.4) is strictly below
`6(I-1)=9/2`. The comparison is exact:

\[
\log_2(781/243)+\frac74\log_2 3<\frac92
\]

is equivalent to

\[
781^4<2^{18}3^{13},
\tag{3.5}
\]

and the integers are

\[
372052421521<417942208512.
\tag{3.6}
\]

The right side of (2.1) has slope `6` as a function of `I`, while the Gibbs envelope (3.4) has slope `log_2 3<6`. Hence (2.1) holds strictly for every `I>=7/4`, i.e. every `B>=28`.

It remains only to check the even boundaries `B<=26`.

## 4. Exact low-boundary finite certificate

The adjacent checker enumerates **every** balanced five-bit truth table with edge boundary at most 26, without stochastic sampling and without floating-point decisions.

Write a balanced `A` by its two four-cube slices `A_0,A_1`. For each four-bit mask the checker records its cardinality and internal boundary. It pairs slice cardinalities summing to 16 and uses

\[
B(A)=B(A_0)+B(A_1)+|A_0\triangle A_1|
\tag{4.1}
\]

to prune pairs that cannot have `B<=26`.

Exactly `142,410` balanced truth tables survive:

\[
\begin{array}{c|r}
B & \#\\ \hline
16 & 10\\
22 & 2400\\
24 & 9440\\
26 & 130560
\end{array}
\tag{4.2}
\]

and there are none at the other boundaries below 26.

For each survivor let `W_S` be the unnormalised Walsh integer

\[
W_S=\sum_x G(x)(-1)^{S\cdot x}.
\]

Balancedness makes every `W_S` divisible by four. Define

\[
a_S=\left(\frac{|W_S|}{4}\right)^2.
\tag{4.3}
\]

Parseval and the spectral influence identity become the exact integer relations

\[
\sum_S a_S=64,
\qquad
L:=\sum_S |S|a_S=4B,
\tag{4.4}
\]

and

\[
H(G)=\frac1{64}\sum_{a_S>0}
a_S\log_2\frac{64}{a_S},
\qquad
I(G)=\frac{L}{64}.
\tag{4.5}
\]

Now (2.1) is equivalent, with no approximation, to

\[
\sum_{a_S>0} a_S\log_2 a_S
\ge
768-6L,
\]

or after exponentiating base two,

\[
\boxed{
\prod_{a_S>0}a_S^{a_S}
\ge
2^{768-6L}.
}
\tag{4.6}
\]

The checker evaluates (4.6) as a pure arbitrary-precision integer comparison for every low-boundary truth table.

Result: all `142,410` pass. There are `960` exact equality cases in the non-dictator low-boundary sector, and **every one has at least one zero-influence coordinate**. In particular there is no genuinely five-input equality case. The ten `B=16` cases are exactly dictators/negations, verified directly by their active-coordinate count.

Floating calculations are used only after the exact pass to describe the tight rows:

\[
\begin{array}{c|c|c|c}
B&I&\max H/(I-1)&\text{nonzero }|W|\text{ multiset}\\\hline
22&1.375&4.5366340682647825&4^{\times15},28\\
24&1.5&6&8^{\times8},16^{\times2}\\
26&1.625&5.947067498701919&4^{\times12},8^{\times4},12^{\times4}.
\end{array}
\tag{4.7}
\]

The `B=24` equality value 6 is therefore real but occurs only in the degenerate sector.

Sections 3 and 4 together prove Theorem 2.1.

## 5. What this changes in the live gate search

The current arity-three/four measurements in the source gate report show their worst genuine grid points collapsing to a lower-arity AND constraint as one or more influences die. The exact theorem here provides a complementary arity-five exclusion:

\[
\boxed{
p_1=\cdots=p_5=\frac12,\quad p_{\rm out}=\frac12
\quad\Longrightarrow\quad
c_G\le -1.8192
}
\tag{5.1}
\]

for every non-dictator five-bit gate.

Thus an arity-five falsifier, if one exists for the current `Gamma`, must leave this central balanced slice. The remaining adversarial region is genuinely asymmetric: nonuniform input bias, unbalanced output, or both. The exact central certificate is useful as an anchor for that search because it gives a very large negative margin at the most symmetric point rather than merely failing to find a counterexample numerically.

This does **not** establish the owner's stronger conjecture that decomposable/AND constraints are extremal over every arity and every bias vector. It is one exact target-level exclusion inside the first untouched arity.

## 6. Reproduction

`CHECK_GATE5_BALANCED_CENTRAL.py` is standard-library only. It performs:

1. exact four-slice boundary enumeration;
2. exact Walsh transforms;
3. exact Parseval/influence identities;
4. exact big-integer verification of (4.6);
5. exact degeneracy checks for equality cases;
6. exact integer verification of the Gibbs threshold (3.5).

Executed checker SHA-256:

`4ddf9eb8d1615327ddd5e2811c9c5296d4644195d2bc647e3df39ee5a4c6c08a`

Archived output SHA-256:

`3bb1ff16d45acc020d8e244e8262fb26440f924d3b8dbda3c6082260b0d3de73`

No benchmark answer, mock backend, paid/remote computation, workflow dispatch, email, Drive data, or unrelated private source was used.

## 7. Next exact attack

Remain on the owner's same gate target. The next adversarial calculation should move off the certified central slice rather than reopen an unrelated FEI route: fix a genuinely five-input truth table and vary one or two biases away from `1/2`, measuring and then bounding the **margin `c_G` itself**. Priority should go to boundary/near-degenerate configurations because the arity-three/four data show the only near-binding behavior approaching the two-input AND face.

A valid falsifier must exceed the current AND margin, not merely make `D_G` small or positive.

**Full FEI remains OPEN / NOT PROVED.**
