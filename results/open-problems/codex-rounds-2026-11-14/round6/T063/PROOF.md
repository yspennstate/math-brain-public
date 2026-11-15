# Local reconstruction of the all-level fold

The statement below verifies the deterministic reconstruction and finite-box entropy comparison in Lemmas 4.4–4.5 of Yan Ru Pei, [*Closing the identification step in the GFF limit: Uniqueness of the zero-slope six-vertex phase for -1 <= Delta < 1/2*](https://hexagonmath.org/pdf/2611.00291v1), November 2026, hexagon:2611.00291v1. The clipping threshold and the count of boundary data are slightly smaller here. No uniqueness or scaling limit is asserted.

## 1. Heights, graphs and bands

Identify the faces with Z². Let h₁,h₂ be integer functions with

    hᵢ(x) = x₁+x₂ (mod 2),   |hᵢ(x)-hᵢ(y)|=1 for nearest neighbours.

Set D=(h₂-h₁)/2. It is integer-valued and satisfies |D(x)-D(y)|≤1 on nearest-neighbour pairs. At each lattice vertex there are two face diagonals. Write d={x,y} and d⊥={z,t} for the two diagonals of one block, and assign a nonnegative integer residual n_d to each diagonal. The same n_d is used at every level.

For an integer ℓ, the minus graph G⁻_ℓ has faces with D<ℓ, nearest-neighbour edges between these faces, and an edge d precisely when

    D(x)=D(y)=ℓ-1,   D(z)=D(t)=ℓ,   n_d=0.                 (1)

The plus graph G⁺_ℓ is defined with D>ℓ and ℓ+1 in place of ℓ-1 in (1). Every graph edge joins faces at distance at most one in the maximum norm. A bridge inside a face rectangle has its entire four-face block inside the rectangle.

Fix an integer M≥2. Suppose G⁻_{jM} has an infinite component for every j∈Z. Let T_j be the union of its infinite components.

First, T_j⊂T_{j+1}. Every nearest-neighbour edge of G⁻_{jM} remains an edge at level (j+1)M. A bridge at level jM can be replaced by the two nearest-neighbour steps through either face of d⊥: all four faces have D<(j+1)M. Thus an infinite connected set at level jM lies in an infinite connected set at the next level. Also x∈T_j implies D(x)<jM.

Every face x belongs to T_j for all sufficiently large j. Choose a face y in an infinite component at some level j₀M and a finite nearest-neighbour path from y to x. Choose j≥j₀ with jM larger than D at every face of this path. The previous inclusion puts y in T_j; the whole path is in G⁻_{jM}, so x∈T_j. For sufficiently negative j, D(x)≥jM, so x∉T_j. Consequently

    k(x)=min{j:x∈T_{j+1}}

is a well-defined integer, and

    x∈T_j  iff  k(x)<j,       D(x)<(k(x)+1)M.             (2)

If x∈T_j and y is its nearest neighbour with D(y)<jM, then y∈T_j by joining it to x. It follows that, for nearest neighbours with k(x)<k(y), writing j=k(x)+1 gives

    D(x)=jM-1,   D(y)=jM,   k(y)=j.                      (3)

Indeed, y∉T_j forces D(y)≥jM, while D(x)≤jM-1 and the Lipschitz bound force equality. Since x∈T_{j+1} and D(y)<(j+1)M, y∈T_{j+1}. Thus k is 1-Lipschitz on nearest-neighbour pairs.

For a diagonal d={x,y}, one also has |k(x)-k(y)|≤1. The nearest-neighbour bound first gives a difference at most two. If k(y)=k(x)+2 and j=k(x)+1, either perpendicular face z has k(z)=j. Applying (3) on x,z and on z,y forces both D(z)=jM and D(z)=(j+1)M-1, impossible for M≥2.

If k(y)=k(x)+1=j on a diagonal, exactly the following possibilities remain:

    (a) D(y)=jM;
    (b) D(x)=jM-1, D(y)=jM+1, D(z)=D(t)=jM;
    (c) D(x)=D(y)=jM-1, D(z)=D(t)=jM, n_d≥1.            (4)

To prove this, x∈T_j and y∉T_j, so D(x)≤jM-1. If D(y)≥jM, the diagonal Lipschitz bound |D(y)-D(x)|≤2 gives (a) or (b); in (b) the nearest-neighbour bounds force the perpendicular values. If D(y)<jM and either perpendicular face has D<jM, nearest-neighbour connections would put y in T_j. Hence both perpendicular faces have D=jM, forcing D(x)=D(y)=jM-1. A zero residual would give an open bridge from x to y and again put y in T_j. This proves (c).

## 2. The fold and its invariant weight

Apply the following transformation at each face, with k=k(x):

    k even:  (h₁',h₂')=(h₁+kM, h₂-kM),
    k odd:   (h₁',h₂')=(h₂-(k+1)M, h₁+(k+1)M).          (5)

All shifts in (5) are even, so parity is preserved. Let

    a(h;d)=1{h(x)=h(y)},
    A_d=a(h₁;d)+a(h₂;d),   A_d'=a(h₁';d)+a(h₂';d),
    n_d'=n_d+(A_d'-A_d)/2.                               (6)

Then

    D'=D-kM       (k even),
    D'=(k+1)M-D   (k odd).                               (7)

The transformation preserves h₁+h₂. To check admissibility and residuals, introduce the level swap s_ℓ(a,b)=(b-2ℓ,a+2ℓ). The face maps g_k in (5) satisfy g_j=g_{j-1}∘s_{jM}. For a nearest-neighbour pair with distinct bands j-1,j, equation (3) gives D(y)=jM, so s_{jM} acts trivially on y. The transformed increments therefore remain unit increments. Equal-band pairs are subjected to the same translation or exchange and have unit increments as well.

On a diagonal with equal bands, A_d'=A_d. On a diagonal with unequal bands, applying the common g_{j-1} to both faces preserves the equality sum, so its change is the change from swapping only the higher-band endpoint at level jM. In case (a) that endpoint is fixed and the change is zero. In case (b) the opposite endpoint differences become equal, giving A_d'-A_d=2. In case (c) the equal differences become opposite, giving A_d'-A_d=-2. For the latter two claims one can check the heights directly: when the perpendicular difference is ℓ and an endpoint difference is ℓ+s, s=±1, the unit-step constraints force

    h₁(x)=h₁(z)-s,   h₂(x)=h₂(z)+s.

Thus equality across d in both copies occurs exactly when the two endpoint signs agree. Swapping one sign changes both equality indicators. Consequently n_d' is an integer, is unchanged in (a), increases by one in (b), and decreases by one in (c). Case (c) has n_d≥1, so n_d'≥0.

Equation (2) and (7) also give

    D'≤M-1 on even bands,       D'≥1 on odd bands.         (8)

Across a nearest-neighbour transition j-1,j, equation (3) gives

    (D'(x),D'(y))=(1,0)       if j is even,
    (D'(x),D'(y))=(M-1,M)     if j is odd.                (9)

In particular D' is 1-Lipschitz.

Allow any finite c_v>1 at each vertex v. Put q_d=c_v⁻² for its two diagonals. The invariant exponent and internal weight on a rectangle Λ are

    τ_d=n_d-A_d/2,
    W_Λ=∏_{d⊂Λ} q_d^{τ_d}=∏_{d⊂Λ} c_v^{A_d}q_d^{n_d}. (10)

Equation (6) gives τ_d'=τ_d at every diagonal, with no summation or limiting argument. The usual pair of six-vertex weights differs from ∏c_v^{A_d} by the constant ∏_v c_v⁻². Thus (10) is the relevant augmented weight, up to a factor independent of the heights. Independent geometric residuals have mass ∏(1-q_d)q_d^{n_d}; their extra normalizing factors are also unchanged.

## 3. Two graph facts used in inversion

Fix an integer κ and put j=κ+1. On the faces with band κ, edges of the original G⁻_{jM} correspond exactly to edges of the following image graph:

    H_κ=G⁺_0(h₁',h₂',n')       if κ is odd,
    H_κ=G⁻_M(h₁',h₂',n')       if κ is even.             (11)

For nearest-neighbour edges this follows from (2), (7) and (8). For bridges the details are as follows.

Suppose first that an original bridge joins two band-κ faces. Its endpoints have D=jM-1, its perpendicular faces have D=jM, and n_d=0. A perpendicular face has band at most κ+1=j by the Lipschitz bound, and at least j by (2) and its value D=jM. Hence it has band j. If κ is odd, (7) gives D'=1 on the endpoints and 0 on the perpendicular faces. If κ is even, (7) gives M-1 on the endpoints and M on the perpendicular faces. Equal endpoint bands leave the residual unchanged. These are precisely the two image bridges in (11).

Conversely, suppose an image bridge joins two band-κ faces. If κ is odd, its endpoint values D'=1 force D=jM-1. A perpendicular face z with D'(z)=0 has band κ-1, κ, or κ+1. Band κ is excluded by (8); band κ-1, which is even, would give D(z)=(κ-1)M, differing from the endpoint by 2M-1>1. Therefore k(z)=κ+1 and D(z)=jM. If κ is even, image endpoints have D'=M-1, again giving D=jM-1. A perpendicular face with D'=M cannot have band κ by (8). Band κ-1, which is odd, gives D(z)=(κ-1)M and the same impossible difference 2M-1. Thus it has band κ+1 and D(z)=jM. In both parities equal endpoint bands give n_d=n_d'=0, proving the converse.

There is no edge of H_κ between bands κ and κ+1. For nearest-neighbour edges, (9) puts the higher-band face at 0 when κ is odd and at M when κ is even, outside H_κ. For a possible diagonal edge crossing these bands, case (a) in (4) has the higher endpoint at that excluded level. In case (b), the fold creates an image saddle, but n_d'=n_d+1≥1 closes its bridge. In case (c), the fold gives unequal endpoint differences, so it creates no image saddle. This exhausts (4).

## 4. Boundary data and reconstruction

Let Λ be a face rectangle with side lengths at least two. Let ∂Λ be its outer face ring, b=|∂Λ|, choose a corner b₀, and let δ be its nearest-neighbour diameter. Set

    L=M+δ+1,       clip_{u,v}(s)=max(u,min(v,s)).

Define X_Λ to consist of the two height gradients inside Λ, D(b₀) modulo 2M, and all residuals n_d with d⊂Λ. Define Y_Λ to consist of the two image gradients, D'(b₀) modulo 2M, the clipped values clip_{-1,M+1}(D'(x)) for x∈Λ, and all n_d' with d⊂Λ. Equivalently one may record D mod 2M and D' mod 2M at every face, since the gradients determine all relative differences.

The boundary datum is

    B_Λ=((k(b')-k(b₀))_{b'∈∂Λ}, k(b₀) mod 2,
         clip_{-L,L}(D'(b₀))).                            (12)

**Theorem.** The pairs (X_Λ,B_Λ) and (Y_Λ,B_Λ) determine each other. The internal weight (10) is the same for the two patterns. Moreover

    #{possible B_Λ} ≤ K_Λ:=2·3^{b-1}(2L+1).              (13)

All these data are unchanged if h₂ is increased by 4M, h₁ is fixed, and k is increased by two. Under that change the image heights both increase by 2M. Thus the data are defined on the same quotient by relative shifts as in the cited lemma.

For the count, take a fixed nearest-neighbour spanning tree of the boundary ring, rooted at b₀. Its b-1 increments each belong to {-1,0,1}, so there are at most 3^{b-1} boundary difference lists. There are two choices of parity and 2L+1 integer choices of the last entry in (12). This proves (13); constraints along the omitted boundary edges can only reduce the count.

We use two elementary observations. First, if k is nonconstant on Λ, some nearest-neighbour pair has different bands. Equation (9) puts D' between 0 and M at that pair. Every face, including b₀, is within δ nearest-neighbour steps of either endpoint. Hence |D'(b₀)|≤M+δ<L. In particular saturation of the last entry of (12) implies that k is constant throughout Λ. If that entry is L, Lipschitz continuity also gives D'(x)≥L-δ=M+1 for all x∈Λ; if it is -L, then D'(x)≤-L+δ=-M-1≤-1.

Second, for every j,

    T_j∩Λ = {faces connected inside G⁻_{jM}|Λ
             to a boundary face b' with k(b')<j}.        (14)

A connection to such a boundary face joins an infinite component. Conversely, from x∈T_j∩Λ take an infinite path in its component and stop before its first exit from Λ. The last face inside is on ∂Λ, because graph edges are nearest-neighbour edges or diagonals. The internal portion of the path proves (14).

To recover Y_Λ from X_Λ and B_Λ, first handle saturation. Here k is constant, so the gradients in (5) are either the original gradients or their exchange, according to its parity. Equation (7) gives D'≡D or -D modulo 2M, respectively. The clipped D' values are all -1 or all M+1, according to the saturation sign, and n'=n. These determine Y_Λ.

Otherwise D'(b₀) is known exactly. Choose the representative of the relative-shift class with k(b₀)=p∈{0,1}, where p is the recorded parity. Formula (7) then recovers D(b₀): it is D'(b₀) for p=0 and 2M-D'(b₀) for p=1. The original gradients recover D everywhere in Λ. The boundary band labels are now known, so (14) recovers every T_j∩Λ, hence every k(x). Formulae (5)–(6) determine Y_Λ. This is a finite procedure: for j≤min_{∂Λ}k the set in (14) is empty; for

    j>max(max_{∂Λ}k, floor(max_Λ D/M))

all faces are minus faces connected by nearest-neighbour paths and all boundary faces are seeds. Thus T_j∩Λ=Λ.

To recover X_Λ from Y_Λ and B_Λ, saturation is inverted by the same constant-parity exchange and the sign of D modulo 2M. Otherwise the exact value D'(b₀), together with the image gradients, recovers D' on Λ. It remains to recover k. Normalize its boundary labels by k(b₀)=p as above.

Start at κ=min_{∂Λ}k. By (14), the set S_κ={x∈Λ:k(x)<κ} is empty. Suppose S_κ is already known. In Λ\S_κ take the graph H_κ from (11), retaining edges with both endpoints in this set. Declare seeds to be boundary faces with k=κ and faces in Λ\S_κ that are nearest-neighbour adjacent to S_κ. Then

    {x∈Λ:k(x)=κ} = {faces reached from these seeds}.     (15)

Every seed has band κ: boundary seeds by definition, and the others because they have band at least κ and are adjacent to a face with band below κ. Every H_κ edge changes the band by at most one. Section 3 excludes an edge from κ to κ+1, while all smaller bands have been removed. Therefore every reached face has band κ.

For the converse, let k(x)=κ. Since x∈T_{κ+1}, follow a path in the original infinite minus component at level jM=(κ+1)M until it first exits Λ or enters S_κ. Before that stopping point every face has band κ: it belongs to T_{κ+1} and is outside T_κ. Section 3 changes its path edges into H_κ edges. If the next step exits Λ, the current face is a boundary seed. If it enters S_κ, that step must be nearest-neighbour: a bridge at level jM has endpoints of difference jM-1, whereas a face with band below κ has D<κM, hence D≤κM-1<jM-1. The current face is therefore a seed of the second kind. This proves (15).

Equation (15) recovers the layer κ and hence S_{κ+1}; induction recovers all bands. It is enough to continue through max_{∂Λ}k+δ, because k is 1-Lipschitz. The induction must not stop at max_{∂Λ}k: an interior finite mountain can have a larger band than every boundary face.

Invert (5) pointwise using the recovered k, then invert (6) to recover n. The image sum h₁'+h₂'=h₁+h₂ and the recovered differences also give the same inverse. Only a common additive height constant is undetermined, which does not affect X_Λ. Equation (10) already proves equality of weights. This completes the theorem.

## 5. Finite-box free energy

Let P be any probability law on the triples above. No stationarity, independence of residuals, or Gibbs property is needed. Assume E_P[n_d]<∞ for every internal diagonal of the box in question. All other entries of X_Λ and Y_Λ have finite alphabets, and n_d'≤n_d+1, so their entropies are finite. One way to see the residual entropy bound is to compare each nonnegative integer variable with the reference law 2^{-n-1}: nonnegativity of relative entropy gives H(n)≤(E[n]+1)log 2. The bound follows first for finite truncations and then for the full variable. Finite subadditivity handles all residuals in the box.

Define

    FE(Z)=Σ_z P(Z=z) log(P(Z=z)/W_Λ(z)).

The mean of |log W_Λ| is finite because the box has finitely many diagonals, every c_v is finite, A_d≤2, and all residual means are finite. The weight is determined by either pattern. The reconstruction theorem gives a bijection of the joint pattern supports preserving their weights and probabilities. Thus

    J=FE(X_Λ,B_Λ)=FE(Y_Λ,B_Λ).

Here the joint free energy uses W_Λ(X_Λ), or equivalently W_Λ(Y_Λ), without a boundary weight. The Shannon chain rule gives

    FE(X_Λ)=J+H(B_Λ|X_Λ),
    FE(Y_Λ)=J+H(B_Λ|Y_Λ).

Subtracting proves the exact identity and its bound:

    FE(Y_Λ)-FE(X_Λ)=H(B_Λ|Y_Λ)-H(B_Λ|X_Λ),
    |FE(Y_Λ)-FE(X_Λ)|≤log K_Λ
       =(b-1)log 3+log 2+log(2M+2δ+3).                 (16)

For growing squares at fixed M the right-hand side divided by area tends to zero. This certifies the local entropy step of the fold, with explicit finite-moment assumptions. Establishing equilibrium, conditional geometric residuals, the Gibbs property of the image, and uniqueness requires additional arguments.

## 6. Finite wired version and checks

The same proof holds in a finite rectangle if the T_j are defined as minus components connected to prescribed boundary seeds, provided the seed families are nested and each seed is a minus face at its level. Require that the wired sets are empty at sufficiently low levels and fill the rectangle at sufficiently high levels. Define k from first membership as above. Their closure under minus edges gives (3)–(4), and (14) holds with their resulting boundary k labels: every path to an original seed reaches a boundary face in T_j, while connectivity to any boundary face already in T_j cannot add a new component. In the proof of (15), follow a path to a wired boundary seed in place of an infinite path. All other steps are unchanged. No assertion that every such finite datum extends to an infinite-volume sample is needed.

The script check_fold.py constructs these finite wired components directly, applies the fold, and implements the two decoders independently. It exhausts two-by-two height profile pairs with relative offsets -4 through 4, band widths 2 and 3, every boundary threshold offset in {0,1}, and every residual assignment in {0,1}. Larger deterministic-seed tests use three-by-three, four-by-three and three-by-four rectangles, M∈{2,3,4,7}, residuals in {0,1,2,7}, saturated and unsaturated boundary data, and both band parities. Residual values are deterministic inputs, not a truncation of a geometric probability distribution. The proof covers all nonnegative residual values.

The invariance check uses the exact integer equality 2n_d-A_d=2n_d'-A_d', which verifies (10) for every c_v>1 at once. Both decoders must return the exact original or image pattern, including all residuals. Relative shifts h₂↦h₂+4M, k↦k+2 must leave the encoded data unchanged. A direct assignment enumeration independently checks the three-by-three height library.

For an explicit interior-mountain case, use row order on a three-by-three box and take

    h₁=(0,-1,0, -1,-2,-1, 0,-1,0),   h₂=-h₁,

M=2, all residuals positive, and boundary seed thresholds zero. Then D=0 on the corners, 1 on the other boundary faces, and 2 at the centre. At level 2 all boundary faces are connected minus faces and the centre is excluded. At level 4 every face is included. Hence k=0 on the boundary and k=1 at the centre. This checks the extra induction layer in Section 4 explicitly.

The reconstruction statement is already present in the cited preprint; its proof above and the smaller boundary count are the result established here beyond the earlier fixed-level swap theorem. The hypotheses I⁻=Z, M≥2 and c_v>1 for geometric residuals remain explicit. The earlier binary c_v=1 construction does not supply a normalizable geometric residual law at that endpoint. No inference to c_v<1 or to a Gaussian free field limit is made.
