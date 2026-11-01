# F0011 — Fourier tiling, an additive-rich subquadratic theorem, and rigorous fixed-basis rarity

Date: 2026-09-19 UTC  
Slot: `R7-06`  
Target: Van H. Vu, *Recent progress in combinatorial random matrix theory*, Conjecture 9.4 (integral spectrum).  
Scope of this note: **restricted structural work only / PARTIAL**. Nothing below proves Vu's source asymptotic.

## 1. Starting point: the self-principal Walsh core

The previous R7-06 run reduced the even-`t`, maximal-binary-rank, two-eigenvalue symmetric-Hadamard boundary to the following exact object. Let

\[
G=\mathbb F_2^m,\qquad h=2m+2,
\]

with `m=2t^2-1` on the branch actually inherited from the Hadamard reduction. A set

\[
Q\subset G,\qquad 0\in Q,\quad |Q|=h,\quad \langle Q\rangle=G
\]

is called *self-principal Walsh* here when

\[
W_Q:=\bigl((-1)^{x\cdot y}\bigr)_{x,y\in Q}
\]

is a real Hadamard matrix. Write `f=1_Q` and use the unnormalised Fourier transform

\[
\widehat f(a)=\sum_{q\in G}f(q)(-1)^{a\cdot q}
              =\sum_{q\in Q}(-1)^{a\cdot q}.
\]

Hadamard orthogonality is exactly

\[
\boxed{(Q+Q)\setminus\{0\}\subseteq Z_Q:=\{a:\widehat f(a)=0\}.}
\tag{1}
\]

For a fixed two-eigenvalue spectrum one additionally fixes the one Fourier coefficient `\widehat f(\mathbf 1_m)=\tau`; none of the upper bounds below needs that extra restriction, so they remain valid after fixing `\tau`.

This note records the B4/B9/B23 attacks prescribed by the previous run.

---

## 2. Exact weighted Fourier-tiling identity

Let convolution be unnormalised:

\[
(f*f)(a)=\sum_{x\in G}f(x)f(a+x).
\]

### Proposition 2.1
Every self-principal Walsh set `Q` satisfies the pointwise identity

\[
\boxed{(f*f)(a)\,\widehat f(a)=h^2\,1_{\{0\}}(a)}
\qquad(a\in G),
\tag{2}
\]

and therefore the dual weighted-tiling identity

\[
\boxed{\sum_{q\in Q}\widehat f(\xi+q)^2=h^2}
\qquad(\xi\in G).
\tag{3}
\]

#### Proof
If `a=0`, then `(f*f)(0)=|Q|=h` because the group has characteristic two, while `\widehat f(0)=h`; hence the product is `h^2`.

If `a\ne0` and `(f*f)(a)>0`, then `a\in Q+Q`, so (1) gives `\widehat f(a)=0`. If `(f*f)(a)=0`, the product vanishes trivially. This proves (2).

Let `N=|G|=2^m`. For the unnormalised transform, `\widehat{f*f}=\widehat f^{\,2}` and `\widehat{\widehat f}=Nf` (there is no sign issue in characteristic two). Taking Fourier transforms of the pointwise product in (2) gives

\[
\frac1N\sum_{\eta\in G}\widehat f(\eta)^2\,Nf(\xi+\eta)=h^2.
\]

The terms with `f(\xi+\eta)=1` are exactly `\eta=\xi+q`, `q\in Q`, proving (3). ∎

### Comment
Equation (3) is stronger than the support statement (1): every translate `\xi+Q` carries exactly the same total squared Fourier mass `h^2`. It is a genuine exact identity, but by itself it does not yet give a subquadratic count.

---

## 3. B4 — prove something weaker completely: additive-rich self-spectral sets are already subquadratic

The objective was to isolate an explicit structural regime in which the desired `2^{o(m^2)}` counting statement can actually be proved.

### Lemma 3.1 (subspace divisibility obstruction)
Suppose `V\le G` is a linear subspace such that

\[
V\setminus\{0\}\subseteq Q+Q.
\]

If `d=\dim V`, then

\[
\boxed{2^d\mid h.}
\tag{4}
\]

In particular `d\le\nu_2(h)`.

#### Proof
For every nonzero `v\in V`, (1) gives `\widehat f(v)=0`, while `\widehat f(0)=h`. Push `f` to the quotient `G/V^\perp\cong V^*`: for a coset `C` of `V^\perp`, let `n_C=|Q\cap C|`. The Fourier transform of the function `C\mapsto n_C` on the `d`-dimensional quotient is precisely the restriction `\widehat f|_V`. All nontrivial Fourier coefficients vanish, so Fourier inversion makes `n_C` constant. There are `2^d` cosets and their counts sum to `h`; hence every count equals `h/2^d`, which is an integer. ∎

### Corollary 3.2 (no large affine cube)
If an affine subspace `A=x+V` is contained in `Q`, then

\[
\boxed{\dim A\le\nu_2(h).}
\tag{5}
\]

Indeed `A+A=V\subseteq Q+Q`, so Lemma 3.1 applies.

On the inherited square-order branch `h=4t^2`, this reads

\[
\dim A\le 2+2\nu_2(t).
\tag{6}
\]

Thus an affine-block construction cannot hide a linear-dimensional cube inside `Q`; when `t` is odd, the bound is only two.

### Theorem 3.3 (polynomial translation symmetry has subquadratic total entropy)
For fixed `\varepsilon>0`, let `\mathcal F_{m,\varepsilon}` be the family of all `h=2m+2` element subsets `Q\subseteq\mathbb F_2^m` whose translation stabiliser

\[
V_Q:=\{v\in G:Q+v=Q\}
\]

satisfies `|V_Q|\ge m^\varepsilon`. Then

\[
\boxed{
|\mathcal F_{m,\varepsilon}|
\le
2^{O_\varepsilon(m^{2-\varepsilon}+m\log m)}
=2^{o(m^2)}.
}
\tag{7}
\]

Consequently the same bound holds for the self-principal Walsh members of this family, even after imposing any fixed trace/Fourier coefficient.

#### Proof
`V_Q` is a subspace. Its translation action on `Q` is free, so `|V_Q|` divides `h`; in particular, if `d=\dim V_Q`, then

\[
\varepsilon\log_2m\le d\le\log_2h=O(\log m).
\tag{8}
\]

For a fixed `d`, the number of `d`-dimensional subspaces of `G` is the Gaussian binomial coefficient

\[
{m\brack d}_2
=\prod_{j=0}^{d-1}\frac{2^m-2^j}{2^d-2^j}
\le 2^{d(m-d+1)}.
\tag{9}
\]

Fix one such `V`. Every `V`-invariant `h`-set is a union of `k=h/2^d` cosets of `V`. Therefore the number of possible `Q` is at most

\[
\binom{2^{m-d}}{k}
\le (2^{m-d})^k
=2^{h(m-d)/2^d}.
\tag{10}
\]

We are deliberately overcounting: we do not enforce that the full stabiliser equal `V`, that `0\in Q`, that `Q` span, or that `W_Q` be Hadamard.

Summing over at most `O(\log m)` possible `d` gives exponent

\[
O(m\log m)+O\!\left(\frac{m^2}{m^\varepsilon}\right),
\]

which is `o(m^2)`. ∎

### Consequence of B4
Any hypothetical `2^{\Omega(m^2)}` obstruction family inside the self-principal slice must be **additively primitive** in a strong sense: its translation stabiliser is smaller than every fixed power of `m`, and Lemma 3.1 also excludes a linear-dimensional affine cube. The additive-rich regime is therefore not where quadratic entropy can hide.

---

## 4. B9 — randomise without false independence: a fixed external basis is quadratically rare

The previous row-exposure route failed because the useful basis can depend on the completed object. Here the basis is frozen *externally*, and the simultaneous Fourier-zero equations can be bounded rigorously without pretending they are independent.

Fix an ordered basis

\[
A=(a_1,\dots,a_m)
\]

of `G`. For an `h`-set `Q` containing zero, let `E_A(Q)` be the event

\[
\widehat{1_Q}(a_i)=0
\quad(1\le i\le m),
\qquad
\widehat{1_Q}(a_i+a_j)=0
\quad(i<j).
\tag{11}
\]

Equivalently, the `m+1` sign columns

\[
1,\ \chi_{a_1}|_Q,\ldots,\chi_{a_m}|_Q
\]

are pairwise orthogonal.

### Theorem 4.1 (fixed-basis quadratic-rarity bound)
Let `Q` be uniformly distributed over all `h=2m+2` element subsets of `G` that contain zero. Whenever

\[
1-\binom h2 2^{-m}>0,
\]

one has

\[
\boxed{
\Pr(E_A(Q))
\le
\frac{2^{-m(m+1)/2}}
     {1-\binom h2 2^{-m}}
=2^{-m^2/2+O(m)}.
}
\tag{12}
\]

No independence among the `\binom{m+1}{2}` orthogonality equations is assumed.

#### Proof
First use an iid ordered model. Set `q_0=0` and choose `q_1,\ldots,q_{h-1}` independently and uniformly from `G`. Because `A` is a basis, the bits

\[
(a_1\cdot q_r,\ldots,a_m\cdot q_r)
\]

are independent uniform vectors in `\mathbb F_2^m` as `r` varies. Thus, after the first fixed `+1` entry, the sign columns `c_1,\ldots,c_m` are independent uniform vertices of the cube `\{\pm1\}^{h-1}`; let `c_0` be the all-one column.

Expose the columns sequentially. Suppose `c_0,\ldots,c_{i-1}` are already pairwise orthogonal. We claim their tails in `\mathbb R^{h-1}` are linearly independent. If a linear combination of those tails vanishes, then for some coefficients `\alpha_j`

\[
\sum_{j=0}^{i-1}\alpha_jc_j=s e_0,
\qquad s=\sum_{j=0}^{i-1}\alpha_j,
\tag{13}
\]

where `e_0` is the first coordinate vector. Taking the inner product with `c_k` gives

\[
h\alpha_k=s
\qquad(0\le k<i).
\]

Hence every `\alpha_k=s/h`, and summing gives `s=is/h`. Since `i<h`, this forces `s=0` and all coefficients vanish.

Therefore the conditions that the next random cube vertex `c_i` be orthogonal to `c_0,\ldots,c_{i-1}` cut out an affine subspace of codimension exactly `i` in `\mathbb R^{h-1}`. An affine subspace of codimension `i` contains at most `2^{h-1-i}` vertices of the `(h-1)`-cube: choose `h-1-i` coordinates on which the direction space projects injectively. Consequently

\[
\Pr(c_i\perp c_0,\ldots,c_{i-1}\mid\text{previous orthogonality})\le2^{-i}.
\]

Multiplication over `i=1,\ldots,m` yields

\[
\Pr_{\rm iid}(E_A)\le
2^{-\sum_{i=1}^m i}
=2^{-m(m+1)/2}.
\tag{14}
\]

Let `D` be the event that all `q_0,\ldots,q_{h-1}` are distinct. By the union bound,

\[
\Pr(D)\ge1-\binom h2 2^{-m}.
\tag{15}
\]

Conditioned on `D`, forgetting the order gives exactly the uniform `h`-subset model conditioned to contain zero. Hence

\[
\Pr(E_A\mid D)
\le\frac{\Pr(E_A)}{\Pr(D)},
\]

which is (12). ∎

### Exact limitation of B9
For every self-principal `Q`, an internally chosen vector-space basis `A\subset Q` satisfies `E_A(Q)`. The theorem above is only for a basis fixed independently of `Q`. A union bound over all ambient ordered bases costs about `|GL(m,2)|=2^{m^2+O(m)}`, which overwhelms the `2^{-m^2/2}` gain. Thus (12) is a genuine quadratic anti-concentration statement, but the **adaptive-basis entropy** is still the missing step.

---

## 5. B23 — actively try to build quadratic entropy, and record why the obvious mechanisms fail

The purpose here was not to prove the desired upper bound but to test whether the restricted counting conjecture might itself be false.

### 5.1 Linear-coordinate orbit: entrywise preservation is only orthogonal gauge

A tempting construction is to start from one `Q` and apply all `T\in GL(m,2)`, apparently producing about `2^{m^2}` images. This does not preserve the self-principal Walsh matrix by the natural correspondence unless `T` is orthogonal.

#### Lemma 5.1
Suppose `Q` spans `G` and

\[
(-1)^{(Tx)\cdot(Ty)}=(-1)^{x\cdot y}
\qquad\text{for all }x,y\in Q.
\tag{16}
\]

Then `T^TT=I`.

#### Proof
Equation (16) says

\[
x^T(T^TT-I)y=0
\]

for all `x,y\in Q`. Since `Q` spans `G` in each variable, bilinearity extends the identity to all `x,y\in G`; hence the matrix vanishes. ∎

This is exactly the orthogonal gauge already identified in the previous run. The lemma does **not** assert that a nonorthogonal `T` can never accidentally send one self-principal set to another; it rules out the straightforward entrywise-invariant `GL(m,2)` orbit as a source of genuine quadratic entropy.

### 5.2 The simplest coordinate seed is impossible for `m\ge5`

#### Lemma 5.2 (orthonormal-subset bound)
If `u_1,\ldots,u_s\in Q` satisfy

\[
u_i\cdot u_j=\delta_{ij},
\]

then

\[
\boxed{s\le\frac{m+3}{2}.}
\tag{17}
\]

#### Proof
Fix `i\ne j`. Because `0,u_i,u_j\in Q`, the three nonzero frequencies `u_i,u_j,u_i+u_j` lie in `Q+Q`; hence all three Fourier coefficients vanish by (1). Let `N_{ab}` count points `q\in Q` with

\[
(u_i\cdot q,u_j\cdot q)=(a,b).
\]

The equations `\widehat f(u_i)=\widehat f(u_j)=\widehat f(u_i+u_j)=0` together with `\sum N_{ab}=h` give

\[
N_{00}=N_{01}=N_{10}=N_{11}=h/4=(m+1)/2.
\tag{18}
\]

Among `0,u_1,\ldots,u_s`, the pattern `00` occurs for `0` and every `u_k` with `k\ne i,j`, so already at least `s-1` times. Therefore

\[
s-1\le(m+1)/2,
\]

which is (17). ∎

In particular a self-principal `Q` cannot contain an orthonormal basis once `m\ge5`. So the obvious construction `Q\supset\{0,e_1,\ldots,e_m\}` fails before one even tries to choose the remaining points.

### 5.3 Affine blocks and ordinary products do not preserve the extremal size law

A large affine block is excluded by Corollary 3.2. More quantitatively, Theorem 3.3 says that even allowing polynomial-size translation symmetry yields only a `2^{o(m^2)}` total family.

The ordinary Cartesian-product construction also misses the special size relation. If `Q_i\subset\mathbb F_2^{m_i}` are each of the present type, then `|Q_i|=2m_i+2`, whereas

\[
|Q_1\times Q_2|=(2m_1+2)(2m_2+2)
>2(m_1+m_2)+2
\tag{19}
\]

for nontrivial factors. Thus the standard product mechanism for spectral/Hadamard sets exits the `|Q|=2m+2` slice rather than generating a quadratic family inside it.

### B23 outcome
The three most immediate quadratic-family mechanisms tested here — an unrestricted linear-coordinate orbit, a simple orthonormal-coordinate seed, and a large affine/product block — all fail for exact reasons. This is **not** evidence that no `2^{\Omega(m^2)}` self-principal family exists; it narrows what such a family would have to look like: additively primitive, non-orthonormal in its seed geometry, and not generated by the obvious `GL` gauge or Cartesian products.

---

## 6. What has and has not been proved

The strongest complete result of this run is Theorem 3.3:

> For every fixed `\varepsilon>0`, self-principal Walsh sets with polynomial-size translation stabiliser form only `2^{o(m^2)}` possibilities in the *labelled ambient group itself*.

The strongest probabilistic result is Theorem 4.1:

> For any basis fixed independently of `Q`, the necessary half-Hadamard/OA constraints have probability at most `2^{-m^2/2+O(m)}` for a random `h`-set.

The exact remaining obstruction is to make the useful basis canonical or otherwise control its adaptivity without paying `2^{\Theta(m^2)}`. Equation (3) is a new exact invariant available for that task.

None of these statements moves the frozen finite metric `N_exact`, which remains 8, and none closes Vu's source conjecture.

---

## 7. Dated literature boundary, 2026-09-19

The broad connection between spectral sets and complex/Fourier Hadamard matrices is classical; see Kolountzakis–Matolcsi, *Complex Hadamard matrices and the Spectral Set Conjecture* (2006), and Herr–Wiegand, *Identifying Complex Hadamard Submatrices of the Fourier Matrices via Primitive Sets* (2021). No novelty claim is made for that bridge.

Hadamard switching is also a substantial existing theory: Orrick's switching operations produce many inequivalent real Hadamard matrices, and Abiad–Peters relate Hadamard switching to graph switching. A fresh bounded 2026-09-19 search also found Abiad–Crnković–Peters–Švob, *Switching graphs and designs*, arXiv:2609.20030 (submitted 2026-09-17, updated 2026-09-18), which extends switching ideas for graphs/designs, and Davis, *Counting partial Hadamard matrices in the cubic regime*, arXiv:2603.30013 (submitted 2026-03-31), which gives asymptotics for rectangular partial Hadamard matrices in a different regime. These do not, from the inspected statements, provide the needed `2^{o(m^2)}` enumeration for the present self-principal `|Q|=2m+2` Walsh slice.

The bounded current search did not surface a paper claiming Vu's Conjecture 9.4 asymptotic. This is negative evidence only, not a certification of global openness or novelty.

## 8. Suggested next attack

The remaining post-STUCK2 route should attack the adaptive-basis gap rather than add another 2-adic layer. A nonrepeating next triple is:

- **B10 (derandomise):** choose a canonical internal basis from `Q` with a description invariant under the orthogonal gauge, then try to transfer Theorem 4.1 without a `GL(m,2)` union bound.
- **B25 (count twice):** double-count pairs `(Q,A)` where `A\subset Q` is an ordered basis satisfying the OA constraints, using both the fixed-`A` quadratic rarity and a lower bound on the number of admissible bases inside each completed `Q`.
- **B28 (typical versus exceptional):** split off the additive-rich sets already covered by Theorem 3.3, and show that an additively primitive typical set cannot support enough adaptive bases; any failure should expose a new structured exceptional family.

The next run must still distinguish a restricted theorem from full F0011 and must not claim source resolution from a literature-search miss.
