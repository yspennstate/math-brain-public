Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated binding model/effort selector or runtime telemetry is exposed.

# F0011 — correlation-face Gram rigidity, orthogonal-gauge entropy, and singular-cross endpoint modes

Date: 2026-09-19 UTC  
Slot: `R7-06`  
Canonical target: `F0011`, Van H. Vu, *Recent progress in combinatorial random matrix theory*, Conjecture 9.4.  
Methods in this ordinary run: **B3 / B14 / B22**.  
Status: **PARTIAL**. The source asymptotic remains OPEN under bounded current checks.  
Frozen metric: `N_exact = 9 -> 9` (**NO MOVEMENT**).

## 1. Source scope and inherited starting point

Vu's source asks, for the real symmetric Rademacher matrix `M_n^sym`,

\[
\Pr(\operatorname{Spec}M_n^{\rm sym}\subset\mathbb Z)
=2^{-(1/2+o(1))n^2}.
\]

The preceding R7-06 run moved the exact finite metric from `8` to `9` and, on the two-eigenvalue symmetric-Hadamard branch, obtained the half-completion equations

\[
H=\begin{pmatrix}P&C\\ C^T&D\end{pmatrix},\qquad H^2=2rI_{2r},
\]

hence

\[
P^2+CC^T=2rI_r,\qquad PC+CD=0,\qquad C^TC+D^2=2rI_r. \tag{1.1}
\]

It also showed that when `C` is invertible,

\[
D=-C^{-1}PC,\qquad CC^T=K_P:=2rI-P^2. \tag{1.2}
\]

The present run attacks the two exact obstacles left there: how many sign Gram roots can one `K_P` have, and what precisely happens when `C` is singular.

---

## 2. B3 — PROVE SOMETHING STRONGER: a simplex-face certificate gives complete Gram-root rigidity

The useful stronger statement is not merely a bound on cospectral mates. It is an exact classification of all sign square roots of a Gram matrix whenever the associated correlation point sits in a simplicial face.

### Definition 2.1 — sign-correlation polytope

Let

\[
\mathcal C_r^{\pm}
:=\operatorname{conv}\{xx^T:x\in\{\pm1\}^r\}
\subset\operatorname{Sym}_r(\mathbb R).
\]

The vertices are indexed by sign vectors modulo `x ~ -x`. This is the usual Bernoulli correlation/cut-polytope object in the `\{\pm1\}` coordinates; no novelty is claimed for the polytope itself.

### Theorem 2.2 — simplicial-face Gram-root rigidity

Let

\[
C=[c_1\ \cdots\ c_r]\in\{\pm1\}^{r\times r}
\]

be invertible and put

\[
K=CC^T,\qquad q=\frac Kr=\frac1r\sum_{j=1}^r c_jc_j^T.
\]

Assume the `r` vertices

\[
v_j:=c_jc_j^T\in\mathcal C_r^{\pm}
\]

are exactly the vertices of a simplicial face `F` of `\mathcal C_r^{\pm}`. Then every sign matrix `C'` satisfying

\[
C'C'^T=K
\]

has the form

\[
\boxed{C'=C\Pi\Delta}
\tag{2.1}
\]

for a permutation matrix `\Pi` and a diagonal sign matrix `\Delta`. Consequently the sign-Gram-root fiber has exactly

\[
\boxed{2^r r!}
\tag{2.2}
\]

members.

#### Proof

Because all coefficients in

\[
q=\frac1r(v_1+\cdots+v_r)
\]

are strictly positive and `v_1,...,v_r` are all vertices of the simplex `F`, the point `q` lies in the relative interior of `F`.

Now let

\[
C'=[c'_1\ \cdots\ c'_r]\in\{\pm1\}^{r\times r},
\qquad C'C'^T=K.
\]

Then

\[
q=\frac1r\sum_{j=1}^r c'_jc_j'^T
\]

is a convex representation of `q` by vertices of `\mathcal C_r^{\pm}`. Since `F` is a face, choose a supporting affine functional `\ell` with

\[
F=\{z\in\mathcal C_r^{\pm}:\ell(z)=\alpha\},
\qquad \ell(z)<\alpha\quad(z\notin F).
\]

As `q\in F`,

\[
\alpha=\ell(q)=\frac1r\sum_{j=1}^r\ell(c'_jc_j'^T).
\]

Every summand is at most `\alpha`; therefore every summand equals `\alpha`. Hence every vertex `c'_jc_j'^T` lies in `F`.

A simplex has unique barycentric coordinates. Relative to the vertex list `v_1,...,v_r`, the barycentric coordinates of `q` are exactly `(1/r,...,1/r)`. In the representation through the `c'_j`, the barycentric coefficient of `v_i` is the number of indices `j` with `c'_jc_j'^T=v_i`, divided by `r`. Uniqueness therefore forces every `v_i` to occur exactly once.

Finally

\[
xx^T=yy^T\quad\text{for }x,y\in\{\pm1\}^r
\]

implies `y=\pm x`: compare any fixed coordinate against all others, or note that the two rank-one ranges coincide and both vectors have the same norm. Thus, after a column permutation, every `c'_j` is an independent sign change of the corresponding `c_j`, proving (2.1).

Conversely every `C\Pi\Delta` has the same Gram matrix `CC^T`, so all `2^r r!` such matrices are roots. Because `C` is invertible, no two of its columns are equal up to sign, and the signed-permutation action is free. This proves (2.2). ∎

### Corollary 2.3 — a checkable exposed-face certificate

The hypothesis of Theorem 2.2 is certified if there exists a symmetric matrix `A` and scalar `\alpha` such that

\[
c_j^TAc_j=\alpha\quad(1\le j\le r),
\]

\[
x^TAx<\alpha
\quad\text{for every sign class }\{\pm x\}
\notin\{\pm c_1,\ldots,\pm c_r\},
\tag{2.3}
\]

and the matrices `c_jc_j^T` are affinely independent.

#### Proof

The linear functional `Z\mapsto\operatorname{tr}(AZ)` takes value `\alpha` on precisely the listed correlation vertices and a strictly smaller value on all other vertices, so they are exactly the vertices of an exposed face. Affine independence makes that face a simplex. ∎

This gives a finite, exact certificate for Gram-root rigidity whenever one has a candidate root.

### Corollary 2.4 — fixed-half Hadamard completions on the rigid branch

Fix a symmetric sign matrix `P` and let

\[
K_P=2rI-P^2.
\]

Suppose `K_P` is positive definite and one sign Gram root `C` of `K_P` satisfies the simplex-face hypothesis of Theorem 2.2. Then the number of sign pairs `(C',D')` satisfying the half-completion equations (1.1) with this fixed `P` is at most

\[
\boxed{2^r r!=2^{O(r\log r)}}.
\tag{2.4}
\]

#### Proof

Positive definiteness of `K_P=C'C'^T` makes every root `C'` invertible. Theorem 2.2 gives at most `2^r r!` roots. For each root, the middle block equation in (1.1) uniquely forces

\[
D'=-(C')^{-1}PC'.
\]

Some of these forced matrices may fail to be symmetric sign matrices, which can only reduce the count. ∎

**B3 outcome.** On a precisely certified correlation-polytope regime, the completion entropy for a fixed first half is only `O(r log r)`, without fixing the second-half cospectral mate in advance. Therefore any quadratic fixed-`P` completion entropy must occur at Gram points `K_P/r` with non-simplicial or otherwise multiply representable correlation structure. This is a restricted theorem, not a uniform F0011 bound.

---

## 3. B14 — FIND THE GROUP ACTING: the obvious orthogonal gauge is still quadratically large after relabeling

The preceding run parametrized the mod-two complement by

\[
T\in O_I(r,2):=\{T\in GL(r,2):TT^T=I\},
\]

where `r=m+1` is even. The first question is whether most of the apparent `T` entropy is merely the permutation gauge coming from ordering the two affine bases. The answer is no.

### Theorem 3.1 — exact size of `O_I(2k,2)`

For `r=2k`,

\[
\boxed{
|O_I(2k,2)|
=2^{2k-1}|Sp(2k-2,2)|
=2^{2k-1+(k-1)^2}\prod_{i=1}^{k-1}(2^{2i}-1).
}
\tag{3.1}
\]

In particular

\[
\boxed{
\log_2|O_I(r,2)|=\frac{r^2}{2}-\frac r2+O(1).
}
\tag{3.2}
\]

#### Proof

Let `V=\mathbb F_2^{2k}` with the standard symmetric bilinear form

\[
B(x,y)=x^Ty.
\]

Put `e=(1,\ldots,1)`. In characteristic two,

\[
B(x,x)=\sum_i x_i=B(x,e)
\tag{3.3}
\]

for every `x`. Hence every isometry fixes `e`: if `A^TA=I`, then for every `x`,

\[
B(Ax,e)=B(Ax,Ax)=B(x,x)=B(x,e)=B(Ax,Ae),
\]

and nondegeneracy gives `Ae=e`.

Let

\[
W=e^\perp.
\]

Because `2k` is even, `e\in W`. Equation (3.3) says `B` is alternating on `W`, and the radical of its restriction is exactly `\langle e\rangle`. Thus

\[
\overline W=W/\langle e\rangle
\]

is a nondegenerate symplectic space of dimension `2k-2`. Restriction therefore gives a homomorphism

\[
\rho:O_I(2k,2)\longrightarrow Sp(\overline W).
\tag{3.4}
\]

It is surjective. Indeed choose a symplectic complement `U\subset W` to `\langle e\rangle`, so `\dim U=2k-2`, and choose `f` with

\[
B(e,f)=1,\qquad B(f,U)=0.
\]

Then any symplectic isometry of `U` extends to `V` by fixing `e` and `f`.

It remains to count the kernel. If `A\in\ker\rho`, then for `u\in U`

\[
Au=u+\phi(u)e
\]

for a unique linear functional `\phi\in U^*`. Write

\[
Af=f+v+\alpha e,
\qquad v\in U,\ \alpha\in\mathbb F_2.
\]

The equations `B(Af,Au)=B(f,u)=0` become

\[
B(v,u)+\phi(u)=0\qquad(u\in U).
\]

Since `B|_U` is nondegenerate, `v` is uniquely determined by `\phi`. The parameter `\alpha` is free; the self-pairing condition is automatic from (3.3) and `B(Af,e)=1`. Hence

\[
|\ker\rho|=2^{\dim U}\cdot2=2^{2k-1}.
\tag{3.5}
\]

Finally, if `s=k-1`, the symplectic group has size

\[
|Sp(2s,2)|=2^{s^2}\prod_{i=1}^s(2^{2i}-1).
\tag{3.6}
\]

For completeness, this follows by counting ordered symplectic bases recursively: choose the first nonzero basis vector in `2^{2s}-1` ways, its partner with pairing one in `2^{2s-1}` ways, and then a symplectic basis of their orthogonal complement. Thus

\[
|Sp(2s,2)|=(2^{2s}-1)2^{2s-1}|Sp(2s-2,2)|,
\]

which iterates to (3.6). Combining (3.5)-(3.6) proves (3.1). Since

\[
\sum_{i=1}^{k-1}\log_2(1-2^{-2i})=O(1),
\]

expansion of (3.1) gives (3.2). ∎

### Corollary 3.2 — permutation double cosets still have quadratic entropy

Let `S_r` act through permutation matrices on the left and right of `O_I(r,2)`. Then

\[
\boxed{
|S_r\backslash O_I(r,2)/S_r|
\ge \frac{|O_I(r,2)|}{(r!)^2}
=2^{r^2/2-O(r\log r)}.
}
\tag{3.7}
\]

#### Proof

Every double coset contains at most `(r!)^2` elements. Apply Theorem 3.1 and Stirling's bound `\log_2(r!)=O(r\log r)`. ∎

This is exactly the relabeling action visible in the information-set form `[I_r\mid T]`: permuting the first and second affine bases sends

\[
T\mapsto P_1^{-1}TP_2.
\]

Thus the obvious left/right relabeling gauge removes only subquadratic entropy.

### Proposition 3.3 — a larger ambient stabilizer cannot be divided out automatically

For one completed set `Q` of size `2r`, the number of ordered choices of an internal affine information basis, together with an ordering of the complementary basis, is at most

\[
(2r)^r r!=2^{O(r\log r)}.
\tag{3.8}
\]

Therefore a group element from a large ambient form-stabilizer is a legitimate *same-object gauge* only when it carries one internal information-set representation of `Q` to another; the number of such representations is subquadratic in entropy. One cannot quotient by an entire `2^{\Theta(r^2)}` ambient isometry group without separately proving that its action identifies the same original `Q`.

#### Proof

An ordered affine basis has `r` points and every point is selected from a set of size `2r`, giving fewer than `(2r)^r` ordered choices. Once the first half is chosen, there are at most `r!` orderings of the complement. Every same-object normalization through information sets is represented among these choices. ∎

**B14 outcome.** The binary orthogonal parameter really has `r^2/2+o(r^2)` ambient bits, and ordinary relabeling or actual internal-information-set gauge can account for only `O(r log r)` of them. Any proof must use the *exact weight-complement/Hadamard equations* to eliminate almost all orthogonal parameters; group quotienting alone cannot supply the needed saving.

---

## 4. B22 — READ THE FAILURES: the singular-cross branch is exactly endpoint spectral support

The generic completion argument from the preceding run failed when `C` was singular. The singularity is not an amorphous exceptional set: it has an exact spectral decomposition.

### Theorem 4.1 — endpoint-mode decomposition

Let

\[
H=\begin{pmatrix}P&C\\C^T&D\end{pmatrix}
\]

be real symmetric and satisfy

\[
H^2=s^2I_{2r}\qquad(s>0).
\tag{4.1}
\]

Define

\[
E=\ker C^T,\qquad F=\ker C,
\qquad k=\dim E=\dim F=\operatorname{corank}C.
\]

Then:

1. the left singular space is exactly the endpoint spectral space of `P`,
   \[
   \boxed{E=E_s(P)\oplus E_{-s}(P)};
   \tag{4.2}
   \]
2. the right singular space is exactly the endpoint spectral space of `D`,
   \[
   \boxed{F=E_s(D)\oplus E_{-s}(D)};
   \tag{4.3}
   \]
3. `E^\perp` and `F^\perp` are invariant under `P` and `D`, and
   \[
   C_0:=C|_{F^\perp}:F^\perp\to E^\perp
   \]
   is an isomorphism;
4. writing `P_0=P|_{E^\perp}` and `D_0=D|_{F^\perp}`, the residual core obeys
   \[
   \boxed{D_0=-C_0^{-1}P_0C_0},
   \tag{4.4}
   \]
   \[
   \boxed{C_0C_0^T=s^2I-P_0^2>0}.
   \tag{4.5}
   \]

Thus every singular-cross solution is an endpoint-supported spectral piece of dimension `k` plus an invertible-cross core of dimension `r-k`.

#### Proof

Expanding (4.1) gives

\[
P^2+CC^T=s^2I,\qquad PC+CD=0,
\qquad C^TC+D^2=s^2I. \tag{4.6}
\]

Since `CC^T` is positive semidefinite,

\[
E=\ker C^T=\ker(CC^T)=\ker(s^2I-P^2).
\]

The spectral theorem for the symmetric matrix `P` identifies the last kernel with the direct sum of the `+s` and `-s` eigenspaces, proving (4.2). The same argument with `C^TC=s^2I-D^2` proves (4.3).

Equations (4.2)-(4.3) make `E` and `F` invariant, and symmetry of `P,D` makes their orthogonal complements invariant as well. Basic linear algebra gives

\[
\operatorname{ran}C=(\ker C^T)^\perp=E^\perp.
\]

The restriction of `C` to `F^\perp` is injective and both spaces have dimension `r-k`, so `C_0` is an isomorphism. Restricting `PC+CD=0` to `F^\perp` gives

\[
P_0C_0+C_0D_0=0,
\]

hence (4.4). Restricting the first equation in (4.6) to `E^\perp` gives (4.5); positivity is strict because the endpoint eigenspaces were removed. ∎

### Corollary 4.2 — the entire trace imbalance lives on singular endpoint modes

Let

\[
e_\pm=\dim E_{\pm s}(P),\qquad
f_\pm=\dim E_{\pm s}(D).
\]

Then

\[
\boxed{
\operatorname{tr}H
=s\bigl[(e_+-e_-)+(f_+-f_-)\bigr].
}
\tag{4.7}
\]

Consequently

\[
\boxed{
\operatorname{corank}C=k
\ge \frac{|\operatorname{tr}H|}{2s}.
}
\tag{4.8}
\]

#### Proof

By (4.4), `D_0` is similar to `-P_0`, so `\operatorname{tr}D_0=-\operatorname{tr}P_0`. The core traces therefore cancel. The endpoint pieces contribute exactly the right side of (4.7). Since

\[
|e_+-e_-|\le e_++e_-=k,
\qquad
|f_+-f_-|\le f_++f_-=k,
\]

(4.8) follows. ∎

### Corollary 4.3 — fixed two-eigenvalue multiplicity forces cross-block corank

If the full `2r x 2r` matrix `H` has `+s` multiplicity `a` and `-s` multiplicity `2r-a`, then

\[
\operatorname{tr}H=s(2a-2r),
\]

and hence every half split obeys

\[
\boxed{
\operatorname{corank}C\ge |a-r|.
}
\tag{4.9}
\]

Thus a fixed two-eigenvalue spectral fiber whose multiplicities are macroscopically unbalanced is forced deep into the singular-cross boundary; the balanced trace-zero fiber is the only one not constrained by this inequality.

### Smallest exceptional family

For `k=1`, Theorem 4.1 says the singular branch consists of exactly one endpoint eigenline on each half plus an `(r-1)`-dimensional invertible-cross core. This is the smallest unresolved singular family to attack next. The failure of the generic argument is therefore localized to a one-dimensional endpoint mode, not to an arbitrary rank defect.

**B22 outcome.** The singular exception has been converted into a recursive spectral object: endpoint-supported modes plus a generic core. In particular, nonzero trace is quantitatively synonymous with unavoidable cross-block singularity.

---

## 5. Why the neighboring nonsymmetric fixed-flag obstruction does not transfer

The neighboring R7-07 work on Vu's nonsymmetric Gaussian-integral-spectrum conjecture constructs `2^{n^2/2+O(n)}` sign matrices triangularizable in one fixed nonorthogonal basis. That mechanism is important to check against F0011, but symmetry kills it.

### Proposition 5.1 — fixed complete flags contain only `2^{O(n)}` symmetric sign matrices

Fix a complete flag

\[
0=V_0<V_1<\cdots<V_n=\mathbb R^n,
\qquad \dim V_i=i.
\]

The family of real symmetric matrices preserving every `V_i` is an `n`-dimensional linear subspace. Consequently it contains at most

\[
\boxed{2^n}
\]

matrices from the sign cube `\{\pm1\}^{n\times n}`.

#### Proof

For each `i`, let

\[
W_i=V_i\cap V_{i-1}^\perp,
\]

a one-dimensional space. If `M=M^T` preserves every `V_i` and `x\in W_i`, then `Mx\in V_i`. For every `y\in V_{i-1}`,

\[
\langle Mx,y\rangle=\langle x,My\rangle=0
\]

because `My\in V_{i-1}`. Hence `Mx\in W_i`; every `W_i` is an eigenline. The orthogonal decomposition

\[
\mathbb R^n=W_1\oplus\cdots\oplus W_n
\]

therefore diagonalizes all matrices in the family in one fixed orthonormal basis. The family is an `n`-dimensional linear subspace of `\mathbb R^{n^2}`.

Finally, if a `d`-dimensional linear subspace of `\mathbb R^N` is intersected with `\{\pm1\}^N`, at most `2^d` points occur: choose `d` coordinate functionals whose restrictions form a basis of the dual; projection to those coordinates is injective. Here `d=n`. ∎

So the R7-07 fixed-shear construction is genuinely nonsymmetric and cannot be imported as a quadratic-entropy counterfamily to F0011. This is a noncircular neighboring-track check, not an audit of R7-07.

---

## 6. What the nearby literature supplies — and where it stops

Bounded current checks on 2026-09-19/20 included the following.

1. **Goldberger–Strassler (2022),** *A practical algorithm for completing half-Hadamard matrices using LLL*, J. Algebraic Combin. 55, 217–244, DOI `10.1007/s10801-021-01077-z`. Their problem is exactly adjacent: complete a partial Hadamard matrix, and solve integer Gram square roots `XX^T=G`. Their practical half-completion algorithm depends on an unproved LLL-performance conjecture and is not a uniform asymptotic enumeration theorem. The present B3 theorem instead isolates a rigorous polyhedral regime where all sign Gram roots are explicitly classified.

2. **Alexander Van Werde (2026),** *Finding all cospectral mates over a number field*, arXiv:`2608.12410`, submitted 2026-08-11. The algorithmic theorem assumes nonzero discriminant/distinct eigenvalues and a fixed totally real number field. The full two-eigenvalue symmetric-Hadamard object has massive repeated spectrum and discriminant zero. On a simple-spectrum block `P`, the method is relevant in principle, but finiteness over a chosen field is not a uniform subquadratic counting bound, and the singular-cross branch is precisely where the polar/conjugacy reduction degenerates.

3. **Tuomo Valtonen (2026),** *Classification of Symmetric Hadamard Matrices Up to Order 32*, arXiv:`2608.06920`, v2 updated 2026-09-10. This supplies a current finite-classification boundary, not an asymptotic `2^{o(n^2)}` enumeration theorem.

4. The sign-correlation polytope used in B3 is classical and affinely equivalent to the cut-polytope/Bernoulli-correlation formulation. No novelty claim is made for that object or its standard facial language.

The bounded current search did not surface a paper proving Vu Conjecture 9.4 or the restricted asymptotic count isolated here. This is a search miss only, not an openness or novelty certificate.

---

## 7. Exact remaining gap and next attack

The frozen finite metric does not move in this run:

\[
\boxed{N_{\rm exact}:9\longrightarrow9.}
\]

The new results split the asymptotic obstruction into two sharply defined pieces.

- **Invertible-cross branch:** Theorem 2.2 gives `2^{O(r\log r)}` completions for every fixed half whose correlation Gram point lies in a simplicial face. What remains is to control non-simplicial/high-representation Gram points and to determine whether they alone can carry `2^{\Theta(r^2)}` mass.
- **Singular-cross branch:** Theorem 4.1 reduces corank `k` to `k` endpoint modes plus an invertible core. Corank one is the smallest unresolved exception, while a spectral multiplicity imbalance of `|a-r|` forces at least that much corank.
- **Group entropy:** Theorem 3.1 shows that the raw orthogonal complement parameter has quadratic entropy and ordinary relabeling removes only `o(r^2)` bits. The exact Hadamard equations, not group quotienting, must provide the decisive pruning.

The next nonrepeating method triple is:

- **B19 / MAKE IT AN ALGORITHM:** turn Corollary 2.3 into a deterministic reconstruction/certificate procedure for a sign Gram root and prove what happens when the supporting-face LP is not simplicial;
- **B24 / FIND THE EXTREMAL OBJECT:** maximize the number of sign roots of `CC^T=K` over positive-definite Gram matrices `K`, testing whether the Hadamard point `K=rI` or another highly non-simplicial correlation point is the true entropy extremizer;
- **B30 / ONE SCALE AT A TIME:** solve the singular boundary by corank, beginning with `k=1`, and either obtain a subquadratic completion theorem for the one-endpoint-mode family or exhibit the exact obstruction.

Both permitted HARD stuck recoveries remain consumed. This is the first ordinary no-movement run after the preceding `8 -> 9` metric movement; two more consecutive ordinary no-movement runs would force direct handoff/retirement rather than a STUCK3.
