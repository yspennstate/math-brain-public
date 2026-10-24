# P0290: a safe scalar sector, exact four-state boundary rays, and the slow-face obstruction

Target: Lasse Leskelä, *Ross's second conjecture and supermodular stochastic ordering*, Queueing Systems 100 (2022), 213--215, DOI `10.1007/s11134-022-09824-0`, journal Problem 2 on p. 214.

Status: **PARTIAL / OPEN**. This note does not prove or refute the source problem. It executes the next prescribed methods B4/B16/B28 after the fixed-`pi` polyhedral reduction. The frozen source metric `Delta_Ross` remains `UNKNOWN/UNMEASURED`.

The source asks whether the workload ordering

\[
c_1\le c_2\quad\Longrightarrow\quad w(c_1)\ge w(c_2)
\]

continues to hold when the baseline intensity is `lambda(t)=f(X(t))`, where `f` is Boolean or more generally deterministic and `X` is a doubly stochastically monotone CTMC. The exact journal statement was rechecked on 2026-09-19 at the accepted-manuscript page 214:

`https://acris.aalto.fi/ws/portalfiles/portal/89616571/Ross_s_second_conjecture_and_supermodular_stochastic_ordering.pdf`.

The recovered R7-04 reduction writes, for a centered real observable `g`,

\[
J_g(c)=\int_0^1(1-u)\langle g,e^{cuQ}g\rangle_\pi\,du,
\]

\[
\Psi(z)=\Phi'(z)=\int_0^1u(1-u)e^{uz}\,du,
\qquad
J_g'(c)=\langle g,Q\Psi(cQ)g\rangle_\pi,
\]

and

\[
H_Q(c)=\frac12\left(Q\Psi(cQ)+[Q\Psi(cQ)]^\dagger\right).
\]

A positive centered eigenvalue of `H_Q(c)` would, by the already proved deterministic-service remainder bound, give a rigorous source-valid workload counterexample at sufficiently small intensity. Thus the remaining second-order question is exactly the sign of `H_Q(c)`.

---

# B4 — prove a weaker obstruction completely: the reflection family is spectrally too damped

The preceding report reduced the exact family

\[
Q_a=
\begin{pmatrix}
-2&2-a&a&0\\
2&-(2+a)&0&a\\
0&2a&-(2+a)&2-a\\
0&0&2&-2
\end{pmatrix},\qquad 0<a\le1,
\]

to one even scalar channel and one odd `2 x 2` block for the self-adjoint derivative. It did not settle the signs of those blocks. Here we isolate what *cannot* be responsible for a reversal in this family.

## 1. Centered matrix and rank-two skew coupling

In the orthonormal centered basis

\[
u=\frac12(1,-1,-1,1)^T,
\quad
v=\frac12(1,1,-1,-1)^T,
\quad
w=\frac12(1,-1,1,-1)^T,
\]

the generator is

\[
M_a=
\begin{pmatrix}
-4&-a&a\\
a&-2a&a\\
-a&a&-4
\end{pmatrix}.
\tag{1.1}
\]

Its symmetric/skew decomposition is

\[
S_a=\frac{M_a+M_a^T}{2}
=
\begin{pmatrix}
-4&0&0\\
0&-2a&a\\
0&a&-4
\end{pmatrix},
\]

\[
A_a=\frac{M_a-M_a^T}{2}
=
\begin{pmatrix}
0&-a&a\\
a&0&0\\
-a&0&0
\end{pmatrix}.
\tag{1.2}
\]

Thus all nonreversibility is a skew coupling between the one-dimensional even channel and a reversible two-dimensional odd bath. There is no skew coupling inside the odd block.

The positive dissipation matrix is `G_a=-S_a`. If

\[
b=a(1,-1)^T,
\qquad
D_a=\begin{pmatrix}-2a&a\\a&-4\end{pmatrix},
\]

then `G_a=diag(4,-D_a)` and

\[
\left\|G_a^{-1/2}A_aG_a^{-1/2}\right\|^2
=\frac14 b^T(-D_a)^{-1}b
=\boxed{\frac{a}{8-a}}.
\tag{1.3}
\]

Consequently, throughout `0<a<=1`,

\[
\boxed{\kappa(a):=\|G_a^{-1/2}A_aG_a^{-1/2}\|\le\frac1{\sqrt7}<1.}
\tag{1.4}
\]

For every eigenvalue `lambda` of `M_a`, the usual numerical-range estimate gives

\[
|\Im\lambda|\le \kappa(a)(-\Re\lambda).
\tag{1.5}
\]

So even when the family has a complex pair, its damping-to-frequency ratio is uniformly strong.

## 2. Scalar safe-sector lemma

The next lemma is independent of the family.

**Lemma 2.1.** Let `lambda=-alpha+i beta` with `alpha>0` and `|beta|<=alpha`. Then for every `c>0`,

\[
\boxed{\Re\{\lambda\Psi(c\lambda)\}<0.}
\tag{2.1}
\]

### Proof

By conjugation symmetry assume `beta>=0`, set

\[
r=\frac\beta\alpha\in[0,1],\qquad x=\alpha c,
\qquad z=-1+ir.
\]

Since

\[
\Psi(xz)=\int_0^1u(1-u)e^{xuz}\,du,
\]

we have

\[
-\Re\{z\Psi(xz)\}
=\int_0^1u(1-u)q_r(xu)\,du,
\]

where

\[
q_r(t)=e^{-t}(\cos rt+r\sin rt).
\tag{2.2}
\]

Put

\[
A_r(x)=\int_0^x t q_r(t)\,dt,
\qquad
F_r(x)=xA_r(x)-\int_0^x t^2q_r(t)\,dt.
\]

A change of variables gives

\[
-\Re\{z\Psi(xz)\}=\frac{F_r(x)}{x^3},
\tag{2.3}
\]

and direct differentiation gives

\[
F_r'(x)=A_r(x),\qquad F_r(0)=0.
\tag{2.4}
\]

It therefore suffices to prove `A_r(x)>0` for `x>0`. Direct integration yields

\[
A_r(x)=\frac{1-h_r(x)}{1+r^2},
\tag{2.5}
\]

with

\[
h_r(x)=e^{-x}\left((1+r^2)x\cos(rx)+\cos(rx)-r\sin(rx)\right).
\tag{2.6}
\]

Moreover

\[
h_r'(x)=-(1+r^2)xq_r(x).
\tag{2.7}
\]

At `x=0`, `h_r(0)=1`, and initially `h_r` decreases. The positive local maxima after zero can occur only when `q_r(x)=0` on a negative-to-positive crossing. They are at

\[
x_m=\frac{3\pi/2+\arctan r+2\pi m}{r},\qquad m=0,1,\ldots,
\]

for `r>0`. At such a point,

\[
h_r(x_m)
=e^{-x_m}\frac{r}{\sqrt{1+r^2}}
\left((1+r^2)x_m+2\right).
\tag{2.8}
\]

For `0<r<=1`, the function

\[
e^{-x}((1+r^2)x+2)
\]

is strictly decreasing for `x>0`, and `x_m>=3\pi/2>3`. Also

\[
e^x>1+x+x^2/2>2x+2\qquad(x\ge3).
\]

Therefore every positive local maximum in (2.8) is strictly below one. The intervening extrema are negative local minima. Hence `h_r(x)<1` for every `x>0`, so `A_r(x)>0`, then `F_r(x)>0`, and (2.3) proves (2.1). The case `r=0` follows directly from the strictly decreasing real exponential. `square`

## 3. Consequence for `Q_a`

Combining (1.4)--(1.5) with Lemma 2.1:

\[
\boxed{
\text{every individual eigenmode of }Q_a\text{ lies in a scalar sector where the triangular derivative is negative.}
}
\tag{3.1}
\]

The family is nevertheless genuinely nonnormal. An exact commutator calculation gives

\[
[M_a,M_a^T]
=
\begin{pmatrix}
0&6a^2-8a&-2a^2\\
6a^2-8a&0&0\\
-2a^2&0&0
\end{pmatrix},
\tag{3.2}
\]

which is nonzero for every `a>0`.

Therefore any positive eigenvalue of the full self-adjoint derivative `H_{Q_a}(c)` would have to arise from **nonnormal modal interference**, not from an underdamped scalar eigenmode. This is a real narrowing of B4, but it is not a sign proof for `h_+`, `tr H_-`, and `det H_-`. The all-observable family sign remains open.

At `a=1`, the off-diagonal ray is

`(1,1,0, 2,0,1, 0,2,1, 0,0,2)`

in the ordering `(01,02,03,10,12,13,20,21,23,30,31,32)`. Section B16 below certifies that this is an actual extreme ray of the fixed-uniform double-monotonicity cone. Its nonzero characteristic factor is

\[
\lambda^3+10\lambda^2+33\lambda+32,
\]

whose discriminant is `-416`, so the complex pair occurs already at an extreme ray rather than only in a cone interior.

---

# B16 — exact rational boundary candidates for the uniform four-state cone

Fix the uniform stationary law `pi=(1/4,1/4,1/4,1/4)` and write the twelve off-diagonal rates in the order

`(01,02,03,10,12,13,20,21,23,30,31,32)`.

Uniform stationarity gives three independent linear equalities. Forward stochastic monotonicity gives the eight inequalities

\[
q_{02}+q_{03}\le q_{12}+q_{13},\quad
q_{03}\le q_{13},\quad q_{03}\le q_{23},\quad q_{13}\le q_{23},
\]

\[
q_{20}\le q_{10},\quad q_{30}\le q_{10},\quad q_{30}\le q_{20},\quad
q_{30}+q_{31}\le q_{20}+q_{21},
\tag{4.1}
\]

and monotonicity of the stationary reversal `Q*=Q^T` gives the transposed eight inequalities. Together with twelve nonnegativity inequalities, this is a rational polyhedral cone in a nine-dimensional equality subspace.

Normalizing by

\[
\sum_{i\ne j}q_{ij}=1
\]

gives an eight-dimensional bounded slice. The rational point

\[
\frac1{26}(3,2,1,3,2,2,2,2,3,1,2,3)
\tag{4.2}
\]

satisfies every one of the 28 inequalities with slack at least `1/26`, so the normalized slice has nonempty relative interior.

## 4. Exact certification after floating discovery

A floating halfspace enumeration was used **only to discover candidates**. It returned 37 normalized vertices. Each was reconstructed as a primitive integer ray. A separate exact SymPy checker then verifies, for every one of the 37 candidates:

1. all rates are nonnegative;
2. the three independent uniform-stationarity equations hold exactly;
3. all 16 forward/reverse stochastic-monotonicity inequalities hold exactly;
4. the gcd is one and all 37 directions are distinct;
5. the matrix obtained from the three stationarity equalities plus all active inequalities has exact rank 11 in `R^12`.

Item 5 proves that each listed direction is genuinely an **extreme ray** of the exact cone: the active face has dimension one.

The 37 exact-certified rays split into 15 orbits under transpose and order reversal, with orbit sizes

\[
2,1,2,4,1,4,2,2,1,4,2,2,4,2,4.
\tag{4.3}
\]

Their exact type counts are

- 2 irreducible reversible rays;
- 26 irreducible nonreversible rays;
- 5 reducible reversible rays;
- 4 reducible nonreversible rays.

All nine reducible certified rays have at most three communicating classes, and those classes are contiguous intervals in the source order. The checker also verifies that the `a=1` reflection-family ray above is in the list and that its cubic discriminant is `-416`.

### Important completeness boundary

The exact checker certifies **feasibility and extremality of all 37 discovered rays**, but it does not independently certify that floating halfspace discovery found every extreme ray. Therefore this note does **not** promote “37 is the complete exact ray count” to theorem status. The correct statement is:

\[
\boxed{\text{37 distinct exact extreme rays are certified; completeness of the list remains UNVERIFIED.}}
\tag{4.4}
\]

This distinction matters under the fleet's finite-certificate rule. It also means the next exact polyhedral step, if this route is resumed after the required stuck diagnosis, should be an exact vertex-enumeration or a dual cone certificate, not another floating scan.

---

# B28 — a slow-face theorem: reducible boundary rays cannot create a leading three-state resonance

The prior numerical probes produced tiny apparent positive derivatives near nearly reducible generators; stable recomputation removed them. The following theorem explains structurally why reducible faces are treacherous and why an `O(epsilon)` positive signal there cannot be accepted without more work.

## 5. Singular-perturbation setup

Let `Q_0` be a finite-state generator with a strictly positive stationary law `pi`, and suppose its closed communicating classes are contiguous ordered blocks

\[
C_1<\cdots<C_m.
\]

Let `Q_1` be another generator with the same stationary law and put

\[
Q_\varepsilon=Q_0+\varepsilon Q_1,\qquad \varepsilon>0.
\]

Assume `Q_epsilon` is irreducible and doubly stochastically monotone for sufficiently small `epsilon`.

Let `Pi` be the `L^2(pi)` orthogonal projection onto functions constant on each `C_r`, i.e.

\[
(\Pi g)|_{C_r}
=\frac1{\pi(C_r)}\sum_{i\in C_r}\pi_i g_i.
\tag{5.1}
\]

The effective generator on the block space is

\[
\bar Q=\Pi Q_1\Pi,
\tag{5.2}
\]

or, in block coordinates,

\[
\bar q_{rs}
=\frac1{\pi(C_r)}
\sum_{i\in C_r}\sum_{j\in C_s}\pi_i(q_1)_{ij}
\qquad(r\ne s).
\tag{5.3}
\]

Its stationary law is `bar pi_r=pi(C_r)`.

## 6. Finite-dimensional averaging lemma

**Lemma 6.1.** For every fixed `t>0`,

\[
\exp\{t(Q_0/\varepsilon+Q_1)\}
\longrightarrow
\Pi\exp(t\bar Q)\Pi
\qquad(\varepsilon\downarrow0)
\tag{6.1}
\]

on functions, with the quotient semigroup identified with the class-constant subspace.

### Proof

Because every state has positive stationary mass, there are no transient states of `Q_0`; its state space is the disjoint union of the closed irreducible classes. Thus zero is a semisimple eigenvalue of `Q_0`, its kernel is exactly the class-constant subspace, and its spectral projection at zero is `Pi`. On `(I-Pi)` every eigenvalue has strictly negative real part.

In the decomposition `ran(Pi) direct-sum ran(I-Pi)`, the generator `Q_0/epsilon+Q_1` has a fast block `Q_0|_{ran(I-Pi)}/epsilon+O(1)`. Variation of constants gives exponential decay of the fast component outside an initial layer of width `O(epsilon)`. The slow component then satisfies

\[
\dot y=\Pi Q_1\Pi y+O(\varepsilon)
\]

uniformly on every compact interval bounded away from zero. Gronwall's inequality gives (6.1). In finite dimensions no domain or tightness issue is present. `square`

## 7. Derivative limit without differentiating the singular semigroup

For a centered real observable `g`, define the covariance of the accelerated chain

\[
C_\varepsilon(s)
=\langle g,\exp\{s(Q_0/\varepsilon+Q_1)\}g\rangle_\pi.
\]

By Lemma 6.1, for every `s>0`,

\[
C_\varepsilon(s)\to
\bar C(s):=
\langle \Pi g,e^{s\bar Q}\Pi g\rangle_\pi.
\tag{7.1}
\]

Every stationary Markov semigroup is an `L^2(pi)` contraction by Jensen's inequality, so

\[
|C_\varepsilon(s)|\le\|g\|_\pi^2.
\tag{7.2}
\]

Set

\[
K_\varepsilon(t):=J_{g,Q_\varepsilon}(t/\varepsilon)
=\int_0^1(1-u)C_\varepsilon(tu)\,du.
\tag{7.3}
\]

For any bounded covariance `C`, if

\[
K(t)=\int_0^1(1-u)C(tu)\,du,
\]

then elementary differentiation after changing variables gives

\[
\boxed{
K'(t)=\frac1{t^3}\int_0^t(2s-t)C(s)\,ds.
}
\tag{7.4}
\]

This identity is the useful point: it avoids differentiating the singularly perturbed semigroup. By (7.1)--(7.2) and dominated convergence,

\[
K_\varepsilon'(t)
\longrightarrow
J'_{\Pi g,\bar Q}(t).
\tag{7.5}
\]

But the chain rule in (7.3) gives

\[
K_\varepsilon'(t)
=\frac1\varepsilon
J'_{g,Q_\varepsilon}(t/\varepsilon).
\]

Hence the exact slow-face asymptotic is

\[
\boxed{
\lim_{\varepsilon\downarrow0}
\frac1\varepsilon
J'_{g,Q_\varepsilon}(t/\varepsilon)
=J'_{\Pi g,\bar Q}(t).
}
\tag{7.6}
\]

## 8. Inheritance of double monotonicity

Because the classes are contiguous blocks, an increasing function on the ordered class space lifts to an increasing function on the original state space. The semigroups generated by `Q_epsilon/epsilon` are stochastically monotone. Passing to the limit (6.1) shows that the quotient semigroup is stochastically monotone. Applying the same argument to the stationary reversals shows that `bar Q*` is also stochastically monotone. Therefore the effective quotient chain is doubly stochastically monotone.

If `m<=3`, the earlier R7-04 three-state theorem applies and gives

\[
J'_{\Pi g,\bar Q}(t)\le0.
\tag{8.1}
\]

Combining with (7.6):

\[
\boxed{
\limsup_{\varepsilon\downarrow0}
\frac1\varepsilon J'_{g,Q_\varepsilon}(t/\varepsilon)\le0.
}
\tag{8.2}
\]

Thus a perturbation away from such a reducible face cannot generate a **positive leading-order slow-scale derivative**. If the quotient derivative is strictly negative, the full derivative is negative for all sufficiently small `epsilon`. If the quotient derivative vanishes, any putative positivity is necessarily subleading `o(epsilon)` and requires a higher-order analysis rather than floating eigensolver evidence.

## 9. Application to the certified four-state boundary rays

The exact checker in B16 verifies that each of the nine reducible certified rays has at most three contiguous communicating classes. Hence (8.2) applies to perturbations away from every one of those certified rays, as long as the perturbation remains in the fixed-uniform source cone and becomes irreducible.

This identifies the minimal obstruction to the naive boundary strategy: a second-order counterexample cannot be obtained merely by approaching one of these reducible rays and exploiting the induced slow quotient at first order. A successful near-face construction would need a genuinely subleading nonnormal interaction, or a face not covered by the presently non-complete 37-ray candidate catalogue.

A bounded coarse two-ray numerical probe was used only after this derivation as a stress test; it found no robust positive derivative. An apparent small positive value near a reducible face disappeared under stable quadrature, consistent with (8.2). This numerical observation is not a certificate and is not used in any theorem above.

---

# 10. Literature and source-status check, 2026-09-19

The peer-reviewed accepted manuscript still states the deterministic-image question as journal Problem 2 on p. 214. The author's publication page still lists the 2022 paper and no later source-specific solution notice was found in a bounded exact-title / deterministic-image / doubly-monotone search on 2026-09-19. The Aalto research portal currently lists the article with one Scopus citation. This is negative search evidence only; it is **not** proof of novelty or current openness.

Relevant current pages checked:

- `https://math.aalto.fi/~lleskela/paper039.html`
- `https://math.aalto.fi/~lleskela/publications.html`
- `https://research.aalto.fi/en/publications/rosss-second-conjecture-and-supermodular-stochastic-ordering/`
- DOI `10.1007/s11134-022-09824-0`.

---

# 11. Honest status and next protocol state

Frozen source metric:

`Delta_Ross: UNKNOWN/UNMEASURED -> UNKNOWN/UNMEASURED (NO MOVEMENT)`.

No source-valid positive workload margin has been certified, and no universal workload monotonicity theorem has been proved. The new results are structural:

1. the reflection family has a uniform exact sector constant `sqrt(a/(8-a))<=1/sqrt(7)` and every individual eigenvalue lies in a scalar-safe triangular-derivative sector;
2. any remaining reflection-family reversal must be a genuinely nonnormal modal-interference effect;
3. 37 distinct exact extreme rays of the uniform four-state cone are certified, in 15 transpose/reversal orbits, but catalogue completeness is explicitly unverified;
4. the complex-spectrum reflection endpoint `a=1` is one of those exact extreme rays;
5. every certified reducible ray has <=3 contiguous classes, and the slow-face theorem rules out a positive leading `O(epsilon)` second-order resonance when perturbing away from it.

This is the third consecutive ordinary P0290 run with no movement of the frozen source metric. Under Section I, the **next R7-04 P0290 run must be thinking-only STUCK1 diagnosis**, not another ordinary search. It must record the exact blocking formula, attempted routes and failures, missing ingredient, simplest unresolved case, nearest solved analogue, exactly one recovery action, and three new B methods.
