# R19 / I0110 — persistent-relator covers and deck-collision extraction

Status: **NEW STRUCTURAL ROUTE / PARTIAL.** This note does not claim closure of Salez Problem 2.1 and does not change the frozen `M_9=9/9` common-certificate count. Its purpose is to repair the remaining source-scope weakness of ELE: the auxiliary lift should be selected from the graph/transition structure *before* any mixing-distance information is inspected.

## 1. Idea before code

The previous R19 theorem C014 showed that if one deletes the model-generated lifts from ELE and merely asks for existential pre/post state-space witnesses, the resulting condition is equivalent to cutoff itself. Thus the missing ingredient is not another inequality; it is a **prior, structural selector** for the lift.

Two source families force apparently incompatible lifts:

- sparse random regular / lift-type models want a tree or universal-cover geometry;
- random Abelian Cayley models want a relation-rich coordinate geometry such as `Z^k` rather than the free tree.

The proposed selector is: **fill only short relations that are persistent under a macroscopic automorphism orbit, and then take the universal cover of the resulting 2-complex.** This automatically leaves an asymmetric graph at its ordinary universal cover, while it fills all bounded-length relations in a Cayley graph because translations reproduce every relation at linearly many locations.

Once a regular quotient lift has been selected, the post-entropic ELE collision defect has an exact group-action formula: it is the excess probability that two retained lifted trajectories agree modulo a deck transformation. This is a structural quantity on the selected cover.

## 2. C015 — exact deck-collision identity

Let `Phi : Xtilde -> X` be a quotient map of countable sets. Assume a group `Gamma` acts freely on `Xtilde` and transitively on every fiber of `Phi`, so that

\[
X \cong \Gamma\backslash \widetilde X.
\]

Let `pi` be a probability law of full support on `X`. Let `rtilde >= 0` be summable on `Xtilde`, with total mass

\[
m:=\sum_{z\in\widetilde X}\widetilde r(z)<\infty,
\]

and let its push-forward be

\[
r(x):=\sum_{z:\Phi(z)=x}\widetilde r(z).
\]

Define the centered weighted collision defect

\[
D_\pi(r;m):=\sum_{x\in X}\frac{(r(x)-m\pi(x))^2}{\pi(x)}.
\]

### Theorem C015

One has the exact identity

\[
\boxed{
D_\pi(r;m)
=
\sum_{\gamma\in\Gamma}\sum_{z\in\widetilde X}
\frac{\widetilde r(z)\widetilde r(\gamma z)}{\pi(\Phi z)}
-m^2.
}
\tag{2.1}
\]

If `pi` is uniform on an `N`-point state space, this becomes

\[
\boxed{
D_{U_N}(r;m)
=
N\sum_{\gamma\in\Gamma}
\langle \widetilde r,\gamma\widetilde r\rangle_{\ell^2(\widetilde X)}
-m^2.
}
\tag{2.2}
\]

Here `(gamma rtilde)(z):=rtilde(gamma z)`; changing `gamma` to `gamma^{-1}` does not change the total sum.

### Proof

Because `sum_x r(x)=m` and `sum_x pi(x)=1`, expansion gives

\[
D_\pi(r;m)
=
\sum_x\frac{r(x)^2}{\pi(x)}-m^2.
\tag{2.3}
\]

For each fixed fiber, freeness and transitivity imply that every ordered pair `(z,w)` in that fiber has a unique `gamma in Gamma` with `w=gamma z`. Therefore, by Tonelli (all terms are nonnegative),

\[
\begin{aligned}
\sum_x\frac{r(x)^2}{\pi(x)}
&=
\sum_x\frac1{\pi(x)}
\sum_{z,w:\Phi z=\Phi w=x}\widetilde r(z)\widetilde r(w)\\
&=
\sum_{\gamma\in\Gamma}\sum_{z\in\widetilde X}
\frac{\widetilde r(z)\widetilde r(\gamma z)}{\pi(\Phi z)}.
\end{aligned}
\]

Substitution into (2.3) proves (2.1); uniform `pi=1/N` gives (2.2). QED.

### Abelian specialization

If `phi : Z^k -> G` is a surjective homomorphism onto a finite Abelian group and `Lambda=ker(phi)`, then `Gamma=Lambda` acts by translations. For any retained lift law `rtilde` on `Z^k`,

\[
\boxed{
D_{U_G}(\phi_\#\widetilde r;m)
=
|G|\sum_{\lambda\in\Lambda}\sum_{a\in\mathbb Z^k}
\widetilde r(a)\widetilde r(a+\lambda)-m^2.
}
\tag{2.4}
\]

Thus the modified `L^2` / collision calculation in the random-Abelian source is literally a deck-translation overlap calculation.

## 3. A graph-intrinsic selector: the persistent-relator cover

Fix a finite connected graph `G` with `N` vertices and an integer `L` satisfying `4 <= L < N`. Let `Aut(G)` act on the set of simple cycles of `G`.

Call a simple cycle `C` with `|C|<=L` **L-persistent** if

\[
|\operatorname{Aut}(G)\cdot C|\ge \frac{N}{L}.
\tag{3.1}
\]

Form a finite 2-complex `K_L(G)` from the graph `G` by attaching a 2-cell along every `L`-persistent cycle. Let

\[
\widetilde K_L(G)\longrightarrow K_L(G)
\]

be its universal topological cover, and denote by `Gtilde_L` the 1-skeleton of `Ktilde_L(G)`. Restriction of the covering map gives a regular graph cover

\[
\Phi_L:\widetilde G_L\to G.
\]

The construction depends only on the isomorphism class of `G`: a graph isomorphism carries automorphism orbits of cycles to automorphism orbits of the same sizes and therefore carries `K_L(G)` to the corresponding 2-complex.

It is also finite-algorithmic at the selector level: brute-force computation of `Aut(G)`, enumeration of cycles of length at most `L`, orbit computation, and a spanning-tree presentation of `pi_1(K_L(G))` produce a finite presentation of the deck group and hence a finite description of the selected cover. Efficiency is not claimed.

## 4. C016 — the selector automatically distinguishes asymmetric and Cayley geometry

### Theorem C016

For the persistent-relator cover above:

1. If `Aut(G)` is trivial, then no cycle is `L`-persistent, so `Gtilde_L -> G` is the ordinary universal graph cover.
2. If `G` admits a subgroup `H <= Aut(G)` acting freely and transitively on vertices (in particular, if `G` is a Cayley graph with its left-translation action), then **every** simple cycle of length at most `L` is `L`-persistent.

### Proof

For (1), every automorphism orbit has size one. Since `L<N`, we have `1<N/L`, so no cell is attached. Thus `K_L(G)` is just the graph `G`, whose universal topological cover has the ordinary universal graph cover as its 1-skeleton.

For (2), let `C` be a simple cycle of length `ell<=L`, and fix a vertex `v in C`. Let `Stab_H(C)` be the setwise stabilizer of `C`. Because `H` acts freely on vertices, the map

\[
\operatorname{Stab}_H(C)\to V(C),\qquad h\mapsto h(v)
\]

is injective. Hence `|Stab_H(C)|<=ell`. Since `|H|=N`, orbit-stabilizer yields

\[
|H\cdot C|
=\frac{N}{|\operatorname{Stab}_H(C)|}
\ge\frac{N}{\ell}
\ge\frac{N}{L}.
\]

The full `Aut(G)`-orbit is at least as large as the `H`-orbit, so `C` is `L`-persistent. QED.

### Consequences for the two anchor geometries

- Uniform random `d`-regular graphs are asymptotically almost surely asymmetric for `3<=d<=N-4` (Kim--Sudakov--Vu, 2002). On that high-probability event, this selector returns the ordinary universal cover, exactly the geometry behind the random-regular entropic proofs.
- Every Cayley graph has a regular translation subgroup. Hence this selector fills every bounded-length cycle. In an Abelian Cayley graph it therefore fills every nondegenerate commutator square, automatically exposing the relation-rich geometry that the free tree misses.

The second bullet does **not** claim that `Gtilde_L` is always exactly the `Z^k` coordinate lift in the full Abelian source class; torsion and additional short relations matter. It proves only that a single graph-intrinsic selector moves in the correct opposite directions on the two structurally opposite anchor families.

## 5. C017 — an entropic deck-extraction criterion that deterministically triggers cutoff

The preceding construction suggests a non-tautological specialization of the frozen ELE criterion. The following theorem is stated for uniform stationary law; the directed/nonuniform source family will require a relative-information analogue.

Let `(X_n,P_n)` be finite Markov chains with uniform stationary law on `N_n` states, `N_n->infty`. Suppose before any mixing-distance calculation we specify a regular Markov quotient

\[
\Phi_n:\widetilde X_n\to X_n
\]

with deck group `Gamma_n`, and a lifted process whose law `q_{n,t}` satisfies

\[
(\Phi_n)_\#q_{n,t}=p_{n,t}
\]

for the source-relevant initial state. (The persistent-relator cover is one canonical way to make this choice.)

Write the information content and entropy

\[
J_{n,t}(z):=-\log q_{n,t}(z),
\qquad
h_n(t):=\mathbb E[J_{n,t}(\widetilde X_{n,t})].
\]

Assume there are structurally selected times `t_n^-<t_n^+`, with `t_n^+/t_n^-->1`, and numbers `a_n->infty`, `b_n=o(a_n)`, such that

\[
h_n(t_n^-)\le \log N_n-a_n,
\tag{5.1}
\]

and

\[
\Pr\bigl(|J_{n,t_n^-}-h_n(t_n^-)|>b_n\bigr)\to0.
\tag{5.2}
\]

At `t_n^+`, suppose a structurally specified retained subprobability `rtilde_n<=q_{n,t_n^+}` has mass `m_n->1` and satisfies the deck-collision condition

\[
\boxed{
N_n\sum_{\gamma\in\Gamma_n}\sum_z
\widetilde r_n(z)\widetilde r_n(\gamma z)-m_n^2\to0.
}
\tag{5.3}
\]

Then the chains exhibit cutoff across `[t_n^-,t_n^+]`.

### Proof

For the lower bound, set

\[
E_n:=\{z:J_{n,t_n^-}(z)\le h_n(t_n^-)+b_n\}.
\]

By (5.2), `q_{n,t_n^-}(E_n)->1`. Every `z in E_n` has

\[
q_{n,t_n^-}(z)\ge e^{-h_n(t_n^-)-b_n},
\]

so

\[
|E_n|\le e^{h_n(t_n^-)+b_n}
\le N_n e^{-a_n+b_n}.
\]

Hence the projected set `A_n=Phi_n(E_n)` has uniform stationary mass

\[
U_n(A_n)\le e^{-a_n+b_n}\to0,
\]

while `p_{n,t_n^-}(A_n)>=q_{n,t_n^-}(E_n)->1`. Therefore

\[
\|p_{n,t_n^-}-U_n\|_{TV}\to1.
\]

For the upper bound, push `rtilde_n` forward to `r_n`. The omitted subprobability has mass `1-m_n`. By C015, (5.3) is exactly

\[
D_{U_n}(r_n;m_n)\to0.
\]

Therefore

\[
\|p_{n,t_n^+}-U_n\|_{TV}
\le (1-m_n)+\frac12\sqrt{D_{U_n}(r_n;m_n)}\to0.
\]

Since total variation is nonincreasing and `t_n^+/t_n^-->1`, cutoff follows. QED.

### Why C017 is not C014 in disguise

C014 allowed arbitrary endpoint witnesses and proved that such unrestricted witnesses are equivalent to cutoff. C017 forbids this: the quotient lift is selected structurally in advance, the lower witness is an information shell of its actual lifted law, and the upper witness is tested through the deck action of that same preselected quotient. No total-variation optimizing set or post-hoc clipping construction appears in the hypotheses.

A particularly canonical implementation is to choose a predetermined `L_n` (for example `max(4,floor(log log N_n))`) and use the persistent-relator cover `Gtilde_{L_n}`. One may then choose `t_n^\pm` from entropy levels of the lifted process, rather than from the mixing time. Verifying the resulting hypotheses across all nine Salez families is **not done here**.

## 6. What moved conceptually, and what did not

The frozen count remains `M_9=9/9`; no new source family exists to add. The advance is instead in the semantic obstruction that kept the saturated ELE package from answering Salez's wording:

- C014 showed that deleting lift structure makes the criterion tautological.
- C015 identifies a graph/group invariant — deck-translation collision — that is exactly the ELE upper defect for regular quotient lifts.
- C016 gives a single graph-intrinsic, pre-mixing selector that returns tree geometry on asymmetric graphs and fills ubiquitous relations on Cayley graphs.
- C017 turns those ingredients into a deterministic cutoff criterion with no TV-selected hypothesis.

This is still **PARTIAL**. The next deciding task is not to broaden the abstraction again. It is to test the predetermined persistent-relator selector on the full nine-family list, beginning with the two opposite anchors `[80]` random regular and `[52]` random Abelian Cayley, and then the nonuniform directed family `[21]`. For `[52]`, one must prove that the selected relation cover supports the same Shannon-scale information concentration and truncated deck-collision estimate throughout the full source class, not only in a generic torsion-free-looking subregime. For `[21]`, one needs the relative-information/nonuniform stationary version of C017.
