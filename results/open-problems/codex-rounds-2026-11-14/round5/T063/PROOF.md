# Binary bridges and finite swaps

This is a finite-volume result. It verifies the local swap mechanism used in Lemmas 3.2–3.5 of Yan Ru Pei's [November preprint](https://hexagonmath.org/pdf/2611.00291v1), hexagon:2611.00291v1, in a formulation with binary bridges. It also allows spatially varying vertex weights and includes weight one. No uniqueness or scaling limit is asserted.

## 1. Setting and statement

Let R be a finite rectangle of faces of the square lattice, with at least three faces in each coordinate direction. Let B be its outermost ring of faces, and let Λ=R\B. An admissible height function h on R satisfies

\[
h(x)\equiv x_1+x_2\pmod 2,
\qquad |h(x)-h(y)|=1\quad\text{if }x,y\text{ are nearest neighbours}.
\tag{1}
\]

Fix admissible boundary values b_1,b_2 on B, each having a nonempty set of fillings. The two boundary values need not agree. Every vertex v whose four surrounding faces lie in R has weights a_v=b_v=1 and a finite weight c_v≥1. Here b_v denotes a vertex weight, not one of the fixed boundary functions.

Write d_v^+,d_v^- for the two diagonals of the four-face block around v. For a diagonal d={x,y}, put

\[
a(h;d)=\mathbf1_{\{h(x)=h(y)\}}.
\]

The six-vertex weight at v is

\[
w_v(h)=c_v^{a(h;d_v^+)+a(h;d_v^-)-1}.
\tag{2}
\]

Indeed, the four unit increments around a block sum to zero. In cyclic order its heights are either (m,m+1,m,m+1), up to reversal, or (m,m+1,m+2,m+1), up to rotation and reversal. In the first case both diagonal pairs are equal and the weight is c_v; in the second exactly one diagonal pair is equal and the weight is one. This proves (2).

Let μ_i be the finite Gibbs law with boundary b_i and weight W(h)=∏_v w_v(h). Sample h_1,h_2 independently from μ_1,μ_2. The filling sets are finite: any height is bounded by its fixed value at one boundary face plus its distance to that face.

Fix an integer ℓ. Define

\[
D=(h_2-h_1)/2,\qquad q_v=c_v^{-2},\qquad p_v=1-q_v.
\tag{3}
\]

Thus D is integer-valued. For a diagonal d={x,y} of v, write d^⊥={z,t} for the other diagonal. Call d an ℓ-saddle if

\[
D(z)=D(t)=\ell,\qquad D(x)=D(y)=\ell+s
\quad\text{for }s\in\{-1,1\}.
\tag{4}
\]

Conditional on the pair of heights, independently put a binary bridge η_d on every diagonal: at an ℓ-saddle, η_d is Bernoulli(p_v); otherwise η_d=0. An ℓ-saddle with η_d=1 is open. Let G have vertex set {x∈R:D(x)≠ℓ}, all nearest-neighbour edges between these vertices, and all open diagonal bridges. A component is interior if it does not meet B.

**Theorem.** Let A be any union of interior components of G. Exchange the heights on A with shifts by 2ℓ:

\[
(\widetilde h_1,\widetilde h_2)(x)=
\begin{cases}
(h_2(x)-2\ell,h_1(x)+2\ell),&x\in A,\\
(h_1(x),h_2(x)),&x\notin A.
\end{cases}
\tag{5}
\]

Keep every η_d unchanged. The new pair is admissible, has the same boundary values, and has the same graph G. The augmented probability mass of the configuration is unchanged. If A is selected by a rule depending only on G and the fixed boundary data, this is a measure-preserving involution.

Moreover, conditional on

\[
H=h_1+h_2,\qquad U=|D-\ell|,\qquad \eta,
\tag{6}
\]

the signs of D−ℓ on the K interior components are independent fair signs. Equivalently, every choice of those signs has conditional probability 2^(−K), on every conditioning event of positive probability.

All assertions hold for arbitrary assignments c_v≥1, including assignments containing both c_v=1 and c_v>1.

## 2. Nearest-neighbour constraints

For nearest neighbours x,y,

\[
|D(x)-D(y)|\le1,
\tag{7}
\]

because both height differences are unit steps. In particular, two adjacent faces with nonzero D−ℓ have the same sign. Open bridges also join faces of the same sign by (4), so every component of G has a well-defined sign.

If a nearest-neighbour edge crosses from A to its complement, at least one endpoint has D=ℓ: otherwise the edge belongs to G and its endpoints cannot be separated by a union of components. If the selected endpoint has D=ℓ, the swap there is trivial. If the unselected endpoint y has D(y)=ℓ, then h_2(y)=h_1(y)+2ℓ. The new edge increments are the two old increments with the copies exchanged. In either case they remain unit steps. Edges entirely inside or outside A also remain admissible. Parity is preserved because the shifts are even. Since A∩B is empty, the boundary values are preserved.

For completeness, the condition is necessary as well for a fixed swap set. Suppose an edge x∈A,y∉A has both D(x)−ℓ and D(y)−ℓ nonzero. They have the same sign by (7). Writing e=h_1(y)−h_1(x), the new increments are

\[
e-2(D(x)-\ell),\qquad e+2(D(y)-\ell).
\]

Their difference has magnitude at least four, whereas two unit steps differ by at most two. Hence such a swap is inadmissible.

## 3. All possible changes across a diagonal

For a diagonal d define

\[
\chi_d= a(\widetilde h_1;d)+a(\widetilde h_2;d)
        -a(h_1;d)-a(h_2;d).
\tag{8}
\]

If both endpoints are selected, the two equality indicators are exchanged; if neither is selected, neither changes. Thus χ_d=0 in these cases. If exactly one endpoint is selected and either endpoint has D=ℓ, the same sum is unchanged. To see this when the unselected endpoint y has D(y)=ℓ, the equality h_2(x)−2ℓ=h_1(y) is precisely the old equality h_2(x)=h_2(y); the other new equality is the old equality for h_1. A selected endpoint with D=ℓ is unchanged outright.

It remains to consider endpoints x∈A,y∉A with both D(x)−ℓ and D(y)−ℓ nonzero. Each face z of d^⊥ is nearest-neighbour adjacent to both x and y. If D(z)≠ℓ, both adjacent edges would belong to G, forcing x and y into the same component. Consequently D=ℓ on d^⊥. By (7),

\[
D(x)=\ell+s,\qquad D(y)=\ell+t,
\qquad s,t\in\{-1,1\}.
\tag{9}
\]

For a face z∈d^⊥ the unit-step constraint for both heights forces

\[
\begin{aligned}
h_1(x)&=h_1(z)-s,&h_1(y)&=h_1(z)-t,\\
h_2(x)&=h_2(z)+s,&h_2(y)&=h_2(z)+t.
\end{aligned}
\tag{10}
\]

For example, h_2(x)−h_2(z)=h_1(x)−h_1(z)+2s must be ±1, which forces h_1(x)−h_1(z)=−s. The remaining identities follow identically.

If s=t, both copies are equal across d. If s=−t, neither is equal across d. Swapping x reverses s and leaves t fixed, so it interchanges these cases. Therefore

\[
\chi_d=
\begin{cases}
-2,&\text{a saddle is separated},\\
+2,&\text{opposite signs in (9) are separated},\\
0,&\text{otherwise}.
\end{cases}
\tag{11}
\]

In the second case d changes from a nonsaddle to a closed saddle. In the first case d was necessarily closed: an open bridge could not cross the selected component union.

## 4. Exact cancellation of weights

For fixed heights and bridge bits let

\[
b_d(h_1,h_2,\eta_d)=
\begin{cases}
p_v,&d\text{ is a saddle and }\eta_d=1,\\
q_v,&d\text{ is a saddle and }\eta_d=0,\\
1,&d\text{ is not a saddle and }\eta_d=0,\\
0,&d\text{ is not a saddle and }\eta_d=1.
\end{cases}
\tag{12}
\]

The unnormalised augmented mass is

\[
M(h_1,h_2,\eta)=W(h_1)W(h_2)\prod_d b_d(h_1,h_2,\eta_d).
\tag{13}
\]

Summing over η gives W(h_1)W(h_2), since p_v+q_v=1 independently at every saddle. Thus its normalising constant is exactly Z_1Z_2.

Equation (2) shows that the ratio of pair weights under a swap is ∏_d c_v^(χ_d). The only nontrivial cancellations are

| Change at d | Pair factor | Bridge factor before | Bridge factor after |
|---|---:|---:|---:|
| Separated closed saddle becomes nonsaddle | c_v^(−2)=q_v | q_v | 1 |
| Separated opposite signs become closed saddle | c_v^2=q_v^(−1) | 1 | q_v |

Each row gives the same product before and after. In every other case χ_d=0 and the saddle status is preserved. Indeed, the set {D=ℓ} and the endpoint magnitudes |D−ℓ| are preserved; when both nonzero endpoints are selected or neither is selected, whether their signs agree is also preserved. A diagonal with a zero endpoint cannot be a saddle.

Consequently M is unchanged. This also covers c_v=1: then q_v=1, and all configurations of positive mass have closed bridges at that vertex. There is no division by p_v.

Every open bridge has both endpoints selected or neither. Its endpoints therefore remain a saddle of the same absolute size, and its perpendicular faces still have D=ℓ. Thus the unchanged open bridge set is valid after the swap. The vertex set and nearest-neighbour edges of G are unchanged as well. This proves graph invariance.

Applying (5) twice on the same set is the identity. A selection rule based on the preserved graph and boundary therefore chooses the same set after the first swap. It is a mass-preserving bijection of the finite state space, proving invariance of the augmented Gibbs law.

## 5. Conditional signs

The data (H,U,η) determine G: its vertices are {U>0}, its nearest-neighbour edges join adjacent such vertices, and its other edges are the specified open bridges. Every component meeting B has a fixed sign, determined by the boundary heights.

Given one configuration in a fiber of (6), independently choosing which of its K interior components to swap produces 2^K distinct configurations in that fiber. Distinctness follows because each component is nonempty and U>0 on it. All configurations so obtained have identical positive mass by Section 4.

There are no further configurations in the fiber. A component has constant sign by Section 2. Once its sign σ is chosen, D=ℓ+σU at each of its faces, and

\[
h_1=H/2-D,\qquad h_2=H/2+D.
\tag{14}
\]

At faces with U=0 the same formula with D=ℓ already determines both heights. Boundary component signs are fixed, leaving exactly the K interior signs. Thus the fiber has precisely 2^K elements, all of equal mass. Its sign law is uniform on {−1,1}^K, which is the asserted conditional independence.

## 6. An independent derivation of the bridge probability

At c_v>1 put q=q_v∈(0,1), and let n_d be independent with

\[
\mathbb P(n_d=j)=(1-q)q^j,\qquad j\ge0.
\tag{15}
\]

At a saddle declare the bridge open precisely when n_d=0; ignore n_d at nonsaddles. Then

\[
\mathbb P(\text{open}\mid\text{saddle})=1-q,\qquad
\mathbb P(\text{closed}\mid\text{saddle})
=\sum_{j\ge1}(1-q)q^j=q.
\tag{16}
\]

This recovers the binary law independently by marginalising the geometric residuals. At a separated saddle the equality sum falls by two, so the residual transformation is n'_d=n_d−1; at a separated opposite-sign diagonal it is n'_d=n_d+1. The former is permitted exactly when the saddle is closed. For the former case, using the pair-weight ratio c_v^(−2), equality of augmented masses is the identity

\[
c_v^2(1-q)q^j=(1-q)q^{j-1},\qquad j\ge1,
\tag{17}
\]

which is equivalent to c_v^2q=1. This agrees with the direct cancellation in Section 4. Conversely, the closed-saddle-to-nonsaddle cancellation forces q=c_v^(−2).

At c_v=1 there is no probability distribution (15) with q=1. The binary construction remains well defined, with no open bridges, as proved directly above. It does not require taking a limit of residual variables.

## 7. Why nearest-neighbour components alone do not suffice

Order a single block as (SW,SE,NW,NE), and take

\[
h_1=(0,1,1,0),\qquad h_2=(2,1,1,2),\qquad\ell=0.
\tag{18}
\]

Both are admissible and both vertices have weight c. Here D=(1,0,0,1), so the two nonzero faces are separate nearest-neighbour components, with a saddle between them. Swapping only SW gives

\[
\widetilde h_1=(2,1,1,0),\qquad
\widetilde h_2=(0,1,1,2).
\tag{19}
\]

Both new vertices have weight one. The pair weight changes from c^2 to one. Thus admissibility alone does not preserve Gibbs mass. At c=2 the missing factor is 1/4; it is exactly the probability of a closed saddle. An open bridge prevents this separation. This is an obstruction to the unaugmented swap, not a counterexample to Pei's augmented lemma.

## 8. Scope of the audit and exact checks

The proof establishes one finite-volume ingredient of the uniqueness argument. It does not establish ergodicity, roughness, existence of a canonical height lift, the folding reconstruction, or uniqueness of a translation-invariant pressure maximiser. In particular, it does not discharge the conditional uniqueness premise in the earlier torus-limit results. The binary graph here is defined at one fixed level ℓ; no simultaneous infinite-level or infinite-volume interchange is justified by the finite argument.

The script `check_binary_swaps.py` independently uses monotone coordinates ψ=(h+x_1+x_2)/2 for its local tests and direct h-coordinate filling enumeration for its domain tests. It exhausts the six possible normalised ψ blocks in each copy, relative offsets −4 through 4, and every swap mask. It checks admissibility, the diagonal change table, exact rational weights at c=1,3/2,2,3, graph invariance and the involution. Offsets outside this finite window are covered by the proof, not by an exhaustive infinite search.

It also enumerates entire domains with 2x2 and 3x2 interior faces, a fixed collar, equal, shifted and reflected boundary heights, uniform or inhomogeneous weights, and levels zero and nonzero. Every bridge configuration of positive mass and every union of interior components is checked. Each resulting state must occur in the independently enumerated state set with the same mass and graph. All sign fibers have exactly 2^K elements, each of conditional mass 2^(−K). The code separately enumerates all edge assignments of the earlier 2x2 torus and checks the old partition polynomials.

These finite tests corroborate the conventions and boundary cases. Sections 1–6 prove the result for every finite rectangle, integer level and assignment c_v≥1. The local swap mechanism is already present in Pei's geometric formulation; no claim of global novelty is made for its binary marginal.
