Model actually running: **GPT-5.6 Sol. Reasoning/effort level: UNVERIFIED** — no separately authenticated maximum-effort metadata is exposed.

# P26 / LIVE20 T08 — finite-range orbit-Green reuse and a line-square Cayley cutoff class

**Parent status before:** `PARTIAL / OPEN` for Salez Problem 2.3.

**Parent status after:** `PARTIAL / OPEN` for Salez Problem 2.3. The parent conjecture is not claimed solved. The strict new restricted scope is a finite-range orbit-Green reuse theorem together with a new fixed-degree Cayley spectral-expander class, the squares of arithmetic biregular line graphs, with an explicit Gaussian profile and quantitative window.

**Restricted theorem/application status:** `CANDIDATE_FULL`, pending later independent review.

**Publication novelty:** `UNVERIFIED`. A bounded repository search found no prior line-square cutoff theorem in the project, and a bounded public search did not establish a matching published theorem. This is negative evidence only, not a priority claim.

Repository/branch: `yspennstate/math-open-problems` / `master`.

Controlling policy: `operations/PROGRESS20_2026-09-20.md`.

Run root: `proofnet24/P26-progress-cutoff-transfer/runs/2026-09-20/`.

## 0. Compact handoff, preserved failed routes, and companion split

The latest own substantive report read was

`2026-09-20_19-01-50__spherical-synchronized-green-transfer.md`.

It proved a dependent-multifront Green theorem and a 912-regular synchronized distance-two Cayley class with a correlated bivariate Gaussian orthant profile. The preserved parent-level obstruction remains the positive exceptional NBRW sector: ordinary vertex transitivity plus a fixed spectral gap is still not known to force an entropic shell Green front. The older Ihara / first-repeated-directed-edge tangle route remains incomplete, and global point-source stationary `L^2` remains too strong. None of those unchanged facts is counted as progress here.

The newest relevant live companion report read was NM13-01

`proofnet24/NM13-01/progress-cutoff/runs/2026-09-20/2026-09-20T15-20-00Z__eisenstein-halved-nbrw-cutoff.md`.

NM13-01 there owns an incidence/halving route: direct NBRW projection from an Eisenstein Cayley bigraph to its 18-regular left-halved Cayley graph. P26 remains complementary: the present run keeps the **same finite-orbit angular Green front** on a non-tree universal line cover while changing the finite-range walk kernel and proving a new radial clock/spectral transform.

Historical overlap was checked before doing mathematics. P26 already has ordinary graph squares of high-girth regular bases, general same-vertex distance-set graphs, pure exact-distance spherical graphs, line graphs of biregular bigraphs, and the exact line-distance-two Hermitian edge graph. The class below is none of these: it is

\[
Y_n=L(X_n)^2,
\]

the union of line-distance one and true line-distance two on a line graph that has triangles. In particular the old high-girth ordinary graph-square theorem does not apply to the line graph itself.

The root `POSTED.md` exclusion for the Salez Problem 2.4 Cayley product-condition manuscript was rechecked and is not reopened.

## 1. Exact source convention and newer exact scope

Justin Salez, `arXiv:2508.21055v1` (28 August 2025), inserts independent mean-one exponential holding times between discrete jumps. Thus for a discrete transition matrix `P` the exact convention throughout this report is

\[
H_t=e^{t(P-I)}
=e^{-t}\sum_{m\ge0}\frac{t^mP^m}{m!}.
\tag{1.1}
\]

In Section 2.2, expanders have diverging size, uniformly bounded degree and spectral gap bounded away from zero, and Problem 2.3 is exactly

> Prove that all vertex-transitive expanders exhibit cutoff.

The fresh 20 September 2026 scope boundary remains strictly narrower.

* Dylan J. Altschuler, `arXiv:2609.14945v1`, submitted 14 September 2026, proves Gaussian-profile cutoff for every fixed-degree **long-range expander** sequence and proves the strict hierarchy
  \[
  \text{Ramanujan}\Longrightarrow\text{long-range expansion}\Longrightarrow\text{spectral expansion},
  \]
  with neither converse. Long-range expansion is therefore not synonymous with Salez's spectral-expander hypothesis.
* Francesco Pedrotti--Justin Salez, `arXiv:2607.05345`, submitted 6 July 2026, prove a universal window theorem in terms of the non-equilibrium Poincare quantity `gamma_*`. The checked theorem does not derive the needed `gamma_*` bound solely from vertex transitivity plus an ordinary fixed spectral gap.
* Shai Evra--Brooke Feigon--Kathrin Maurischat--Ori Parzanchevski, `Ramanujan Bigraphs`, `arXiv:2312.06507` (2026 revision), provide the fully Ramanujan arithmetic `(9,3)` biregular input and the edge-NBRW operator estimates reused below. The earlier P26 line-graph report recovered the concrete Eisenstein edge-simply-transitive congruence family and its Ramanujan property from their Theorems 8.7 and 7.3(1).

## 2. Parent before/after and mechanism-level advance

### Parent before

Salez Problem 2.3 was open. P26 had finite-orbit Green transfer for one particular walk on a non-tree line cover and several spherical rewiring theorems on regular-tree covers.

### Parent after

Salez Problem 2.3 remains open. The strict source-compatible enlargement is:

> **Line-square arithmetic class.** Let `X_n` run through the fully Ramanujan `(9,3)` edge-simply-transitive arithmetic bigraph quotients described above, with girth tending to infinity, and put `Y_n=L(X_n)^2`. Then `Y_n` is a 42-regular Cayley spectral-expander sequence, fails every fixed positive long-range-expansion constant, and rate-one continuous-time SRW on `Y_n` has a Gaussian TV cutoff profile with center
> \[
> \frac{147}{139}\log_4|V(Y_n)|+O(1)
> \]
> and window `Theta(sqrt(log n))`, with finite-size profile error `O_Z(log log n/sqrt(log n))`.

The mechanism-level advance is the **finite-range orbit-Green reuse principle**: once the projected uniform orbit shells of a transitive cover have a quantitative Green front, every fixed-range invariant kernel on the same cover reuses that angular estimate verbatim. Only the finite-state radial/type Markov-additive clock must be recomputed. This is what permits a graph-square operation on a cover with triangles without re-proving any angular mixing theorem.

## 3. Theorem A — finite-range orbit-Green reuse

Let `\widetilde X` be a locally finite transitive graph, root `o`, and let `K` be the stabilizer of `o` in a transitive automorphism group. Suppose each metric sphere has at most `s<infinity` `K`-orbits. Write those orbits as

\[
\mathcal O_{r,\sigma},\qquad \sigma\in\Sigma_r,\quad |\Sigma_r|\le s.
\]

Let `p_n:\widetilde X\to X_n` be finite transitive quotients and let

\[
\nu^{x}_{n,r,\sigma}
\]

be the pushforward to `X_n` of the uniform law on `\mathcal O_{r,\sigma}` after choosing a lift of `x`.

Assume an entropic radius `ell_n -> infinity` and functions `G_n,L_n` satisfy

\[
\sup_x\sup_{\sigma}\sup_{r\ge\ell_n+h}
\chi^2(\nu^x_{n,r,\sigma}\Vert\pi_n)
\le G_n(h),
\tag{3.1}
\]

and the union of projected orbit shells with `r<=ell_n-h` has stationary mass at most

\[
L_n(h).
\tag{3.2}
\]

Now let `\widetilde Q` be **any fixed finite-range symmetric Markov kernel on `\widetilde X` invariant under the transitive group**, and assume it descends to a regular finite kernel `Q_n` on each `X_n`. Run the rate-one continuous-time chain with semigroup

\[
H_t^{(n)}=e^{t(Q_n-I)}.
\]

Let `(R_t,\Sigma_t)` be the metric radius and stabilizer-orbit type of its lift to `\widetilde X`. Then

\[
\boxed{
\delta_x H_t^{(n)}
=
\sum_{r,\sigma}
\Pr(R_t=r,\Sigma_t=\sigma)\,
\nu^x_{n,r,\sigma}.
}
\tag{3.3}
\]

Consequently

\[
\boxed{
\Pr(R_t\le\ell_n-h)-L_n(h)
\le d_n(t)
}
\tag{3.4}
\]

and

\[
\boxed{
 d_n(t)
\le
\Pr(R_t<\ell_n+h)
+\frac12\sqrt{G_n(h)}.
}
\tag{3.5}
\]

### Proof

Because the lifted chain starts at `o` and `\widetilde Q` commutes with `K`, its law at every time is constant on each orbit `\mathcal O_{r,\sigma}`. Conditioning on `(R_t,\Sigma_t)` therefore gives the uniform orbit law, and projection gives (3.3). This is the key kernel-reuse observation: the conditional angular law depends on the orbit geometry, not on which invariant finite-range kernel generated the radial/type weights.

For (3.4), let `A` be the union of the projected shells with radius at most `ell_n-h`. On the event `{R_t<=ell_n-h}` the endpoint lies in `A`, while `pi_n(A)<=L_n(h)`. Testing TV on `A` proves the lower bound.

For (3.5), split the mixture (3.3) according to `{R_t<ell_n+h}`. On its complement every component has `chi^2<=G_n(h)`, hence TV at most `sqrt(G_n(h))/2`; convexity of TV gives (3.5). `QED`

This theorem is stronger than merely re-running the finite-orbit proof for one graph: it is a closure statement under fixed-range invariant rewiring of the same transitive cover.

## 4. Quantitative window from the exact continuous-time radial clock

Assume in addition

\[
G_n(h)\le A(\ell_n+h+2)^b e^{-ah},
\qquad
L_n(h)\le Ae^{-ah},
\tag{4.1}
\]

and that outside a fixed boundary set the pair `(R,J)` is a bounded-increment irreducible finite-state Markov-additive chain. Let its one-jump tilted matrix be

\[
M_\theta(i,j)
=\sum_\delta p(i,j,\delta)e^{\theta\delta},
\tag{4.2}
\]

and let `lambda(theta)` be the Perron branch with `lambda(0)=1`. For Salez's **rate-one Poisson clock**, the matrix mgf is

\[
\exp\{t(M_\theta-I)\},
\]

so the scalar cumulant exponent is `lambda(theta)-1`, not `log lambda(theta)`. Define

\[
v=\lambda'(0)>0,
\qquad
\sigma^2=\lambda''(0)>0,
\qquad
\tau^2=\frac{\sigma^2}{v^3}.
\tag{4.3}
\]

If the boundary correction has a uniform exponential tail, standard finite-state analytic perturbation plus Esseen smoothing gives

\[
\sup_u\left|
\Pr\!\left(\frac{R_t-vt}{\sqrt{\sigma^2t}}\le u\right)-\Phi(u)
\right|
=O\!\left(\frac{\log t}{\sqrt t}\right),
\tag{4.4}
\]

where the logarithm absorbs truncation of the exponentially light boundary correction.

Choose `h_n=C log ell_n` large enough that both Green/support errors in (3.4)--(3.5) are `o(ell_n^{-1/2})`. At

\[
t_n(z)=\frac{\ell_n}{v}+z\sqrt{\ell_n}
\tag{4.5}
\]

we obtain, uniformly on every bounded `z` interval,

\[
\boxed{
 d_n(t_n(z))
=\Phi(-z/\tau)
+O_Z\!\left(\frac{\log\ell_n}{\sqrt{\ell_n}}\right).
}
\tag{4.6}
\]

Therefore, for fixed `epsilon in (0,1)`,

\[
\boxed{
 t_{\rm mix}^{(n)}(\epsilon)
=\frac{\ell_n}{v}
-\tau\Phi^{-1}(\epsilon)\sqrt{\ell_n}
+O_\epsilon(\log\ell_n).
}
\tag{4.7}
\]

## 5. Application geometry: square of a biregular line graph

Let `X=(L\sqcup R,E)` be a simple `(K+1,k+1)`-biregular graph with girth greater than four. On `ell^2(E)`, let

* `C_L` be adjacency between distinct edges sharing their `L` endpoint;
* `C_R` be adjacency between distinct edges sharing their `R` endpoint.

Then line-graph adjacency is

\[
A_1=C_L+C_R.
\tag{5.1}
\]

If the girth is greater than four, two disjoint ancestor edges are at line distance two exactly when they are the outer edges of a unique three-edge path. Hence true line-distance-two adjacency is

\[
A_2=C_LC_R+C_RC_L.
\tag{5.2}
\]

Thus the simple line-graph square has

\[
\boxed{
A_Y=A_1+A_2
=C_L+C_R+C_LC_R+C_RC_L
}
\tag{5.3}
\]

and degree

\[
\boxed{D=K+k+2Kk.}
\tag{5.4}
\]

If a group acts simply transitively on `E`, then it acts regularly on the vertices of `Y`; because (5.3) is automorphism-invariant, `Y` is an ordinary Cayley graph.

## 6. Exact spectrum of the line square

Let `M` be the `L x R` biadjacency matrix of the ancestor, and let `s` be a singular value with `x=s^2`. Let `U_L,U_R` be the unnormalised endpoint incidence maps from edge space to the two vertex sides, so

\[
C_L=U_L^*U_L-I,
\qquad
C_R=U_R^*U_R-I.
\tag{6.1}
\]

For singular vectors `u,v` satisfying

\[
Mv=su,
\qquad
M^*u=sv,
\]

put `a=U_L^*u` and `b=U_R^*v`. The span of `a,b` is invariant. Direct use of

\[
U_LU_L^*=(K+1)I,
\quad
U_RU_R^*=(k+1)I,
\quad
U_LU_R^*=M
\]

gives, in the basis `(a,b)`,

\[
A_Y|_{\langle a,b\rangle}
=\begin{pmatrix}
 x-K-1&ks\\
 Ks&x-k-1
\end{pmatrix}.
\tag{6.2}
\]

Its trace and determinant are

\[
2x-(K+k+2),
\qquad
(x-1)\bigl(x-(K+1)(k+1)\bigr),
\]

so the two branches are

\[
\boxed{
\Lambda_\pm(x)
=x-\frac{K+k+2}{2}
\pm\frac12\sqrt{(K-k)^2+4Kkx}.
}
\tag{6.3}
\]

On the orthogonal edge subspace killed by both endpoint incidence maps, `C_L=C_R=-I`, hence `A_Y=0`. At `x=0`, (6.3) gives the remaining unpaired values `-(k+1)` and `-(K+1)`. Thus all spectral sectors are accounted for.

For the `(9,3)` case, `K=8,k=2`. The output degree is

\[
\boxed{D=42.}
\tag{6.4}
\]

A fully adj-Ramanujan ancestor has nontrivial squared singular values

\[
x\in[2,18]\cup\{0\},
\]

while the Perron value is `x=27`. The function `Lambda_+(x)` is strictly increasing. Hence

\[
\Lambda_+(18)=12+3\sqrt{33},
\qquad
\Lambda_+(27)=42,
\]

and the normalized one-sided output gap satisfies

\[
\boxed{
\operatorname{gap}(Y_n)
\ge
1-\frac{12+3\sqrt{33}}{42}
=
\frac{10-\sqrt{33}}{14}
=0.3039598109\ldots .
}
\tag{6.5}
\]

Thus `(Y_n)` is a fixed-degree vertex-transitive spectral-expander sequence.

## 7. The angular Green front is inherited without change

Let

\[
Z=L(T_{K+1,k+1})
\]

be the line graph of the universal biregular tree, rooted at an edge. Every positive metric sphere of `Z` splits into exactly two root-stabilizer orbits, according to whether the far endpoint lies on the `L` or `R` side. The sphere sizes are

\[
|\mathcal S_{2m}|=2(Kk)^m,
\qquad
|\mathcal S_{2m+1}|=(K+k)(Kk)^m.
\tag{7.1}
\]

Hence, for finite quotients with `n=|E(X_n)|=|V(Y_n)|`, the entropic radius is

\[
\boxed{
\ell_n=\log_{\sqrt{Kk}}n+O(1).
}
\tag{7.2}
\]

The earlier P26 finite-orbit line theorem identified the projected uniform laws on these two orbit types with directed-edge NBRW endpoint laws and, from the EFMP Ramanujan NBRW estimate, proved

\[
\sup_{\sigma}\sup_{r\ge\ell_n+h}
\chi^2(\nu_{n,r,\sigma}\Vert\pi_n)
\le
C_{K,k}(\ell_n+h+2)^2(Kk)^{-h/2}.
\tag{7.3}
\]

Equation (7.1) also gives

\[
L_n(h)\le C_{K,k}(Kk)^{-h/2}.
\tag{7.4}
\]

The point of Theorem A is that neither (7.3) nor (7.4) depends on whether the lifted walk uses only line edges or line edges together with line-distance-two edges. The orbit laws are geometric. For `Kk=16`,

\[
G_n(h)\le C(\ell_n+h+2)^2 4^{-h},
\qquad
L_n(h)\le C4^{-h}.
\tag{7.5}
\]

Thus `h_n=4 log_4 ell_n` is already enough for the Green/support error to be at most the quantitative CLT scale.

## 8. Exact radial/type clock for the 42-regular output

Use type `L` when the far endpoint of the current ancestor edge lies on the `L` side and type `R` otherwise. Away from the finite root boundary, one **line-edge** move from type `L` has radial counts

\[
-1:1,\qquad 0:k-1,\qquad +1:K,
\]

and from type `R` the roles of `K,k` are exchanged.

A true **line-distance-two** move has counts

\[
L:\quad
-2:1,\ -1:k-1,\ +1:(K-1)k,\ +2:Kk,
\tag{8.1}
\]

\[
R:\quad
-2:1,\ -1:K-1,\ +1:(k-1)K,\ +2:Kk.
\tag{8.2}
\]

Combining the two disjoint neighbor sets for `K=8,k=2`, and retaining the next type, gives the exact rows

\[
L:\quad
(L,-2):1,\ (L,0):1,\ (L,+2):16,
\ (R,-1):2,\ (R,+1):22,
\tag{8.3}
\]

\[
R:\quad
(L,-1):8,\ (L,+1):10,
\ (R,-2):1,\ (R,0):7,\ (R,+2):16.
\tag{8.4}
\]

Each row sums to 42. The type transition matrix is

\[
M_0=
\begin{pmatrix}
3/7&4/7\\
3/7&4/7
\end{pmatrix},
\qquad
\pi_{\rm type}=(3/7,4/7).
\tag{8.5}
\]

The tilted one-jump matrix is

\[
M_\theta=\frac1{42}
\begin{pmatrix}
 e^{-2\theta}+1+16e^{2\theta}
 &2e^{-\theta}+22e^\theta\\
 8e^{-\theta}+10e^\theta
 &e^{-2\theta}+7+16e^{2\theta}
\end{pmatrix}.
\tag{8.6}
\]

Differentiating its Perron branch at zero gives the exact rate-one continuous-time constants

\[
\boxed{v=\frac{139}{147},}
\tag{8.7}
\]

\[
\boxed{\sigma^2=\frac{14746}{7203},}
\tag{8.8}
\]

and

\[
\boxed{
\tau^2=\frac{\sigma^2}{v^3}
=\frac{6502986}{2685619}
=2.4214104830\ldots .
}
\tag{8.9}
\]

There is also a direct exponential boundary check. For `q=1/2`, the two rowwise exponential moments are

\[
\mathbb E_L[2^{-\Delta R}]=\frac47<1,
\qquad
\mathbb E_R[2^{-\Delta R}]=\frac67<1.
\tag{8.10}
\]

Thus `2^{-R}` has a strict multiplicative drift away from the root outside the boundary region; the resulting downward-excursion and boundary-occupation tails are exponential. The boundary correction is therefore admissible in Section 4.

## 9. Quantitative cutoff profile

For the `(9,3)` family, `sqrt(Kk)=4`, so

\[
\ell_n=\log_4 n+O(1),
\qquad n=|V(Y_n)|.
\]

Theorem A, (7.5), and the Markov-additive Berry--Esseen estimate therefore give, uniformly for every fixed `Z` and `|z|<=Z`,

\[
\boxed{
 d_{Y_n}\!\left(
 \frac{147}{139}\log_4 n
 +z\sqrt{\log_4 n}
 \right)
 =
 \Phi\!\left(
 -z\sqrt{\frac{2685619}{6502986}}
 \right)
 +O_Z\!\left(
 \frac{\log\log n}{\sqrt{\log n}}
 \right).
}
\tag{9.1}
\]

In particular the window is `Theta(sqrt(log n))`, and for every fixed `epsilon in (0,1)`,

\[
\boxed{
 t_{\rm mix}(\epsilon)
 =
 \frac{147}{139}\log_4 n
 -\sqrt{\frac{6502986}{2685619}}\,
 \Phi^{-1}(\epsilon)\sqrt{\log_4 n}
 +O_\epsilon(\log\log n).
}
\tag{9.2}
\]

This is ordinary simple random walk on the 42-regular output graph itself, under Salez's exact continuous-time convention. EFMP NBRW enters only as the angular shell-Green input.

## 10. The outputs are spectral but not long-range

One output step has line-graph displacement at most two. By (7.1), a line ball of radius `2r` in the universal cover has size at most

\[
C\,(\sqrt{Kk})^{2r}=C(Kk)^r.
\]

For `Kk=16`, therefore

\[
|B_{Y_n}(x,r)|\le C16^r.
\tag{10.1}
\]

But a 42-regular long-range expander requires the singleton tree-growth benchmark `41^r` throughout the appropriate pre-saturation logarithmic range. Taking

\[
r_n=\left\lfloor\frac12\log_{41}n\right\rfloor
\]

gives

\[
\frac{|B_{Y_n}(x,r_n)|}{41^{r_n}}
\le C\left(\frac{16}{41}\right)^{r_n}
\longrightarrow0.
\tag{10.2}
\]

Hence no fixed positive long-range-expansion constant exists. This class is genuinely **spectral-but-not-long-range**, so Altschuler's output theorem does not apply directly.

## 11. Essential checker, correction note, and sanity status

The decisive symbolic checker was executed locally in this run and archived as

`2026-09-20_19-56-32__line_square_finite_range_green_checker_corrected.py`

with executed output

`2026-09-20_19-56-32__line_square_finite_range_green_checker_corrected.out`.

It terminates from the marker

`P26_T08_LINE_SQUARE_FINITE_RANGE_GREEN_CORRECTED_EXACT_PASS`

and verifies exactly:

* the spectral discriminant `(K-k)^2+4Kkx` and factorized determinant;
* degree 42, `Lambda_+(18)=12+3 sqrt(33)`, `Lambda_+(27)=42`, and gap `(10-sqrt(33))/14`;
* both radial/type rows and their row sums;
* type stationary law `(3/7,4/7)`;
* `v=139/147`, `sigma^2=14746/7203`, `tau^2=6502986/2685619`;
* exponential moments `4/7` and `6/7`;
* the strict branching mismatch `16<41`.

A sanity check caught an orientation bookkeeping mistake **before this report was written**: a provisional support checker had accidentally swapped the `K-1` and `k-1` distance-two inward sectors. Those provisional immutable support files are intentionally not overwritten and are **not evidence for this report**. The corrected checker above uses (8.1)--(8.4), was re-executed, and is the only checker counted in the ledger delta. This correction changed the radial constants but not the spectral theorem or the class definition.

## 12. Residual obstruction, next attack, and failed-route history

### Residual obstruction

The parent obstruction is unchanged in identity but sharper in location. Theorem A shows that, once a finite-orbit shell Green front exists, a substantial family of non-tree finite-range rewirings is essentially free: angular mixing is reusable and the remaining work is finite-state radial probability. What Salez Problem 2.3 still lacks is a mechanism forcing such a shell Green front from **arbitrary vertex transitivity plus ordinary spectral expansion**. The difficult positive exceptional NBRW sector remains the central unresolved angular obstruction.

### Preserved failed routes

1. `Ihara / first repeated directed edge`: incomplete; no bound strong enough to force the entropic Green front.
2. `Global point-source stationary L2`: too strong and known to fail on cutoff classes.
3. `Kill every positive exceptional mode by a positive short scalar filter`: no general cancellation mechanism; positive slow modes survive.

No unchanged check above is counted as progress.

### Next attack

The next P26 attack is the finite-rank **angular defect transfer** suggested by the previous run, now formulated on a single finite-orbit cover rather than a product. Seek a decomposition for late shell likelihood ratios

\[
\frac{d\nu_{r,\sigma}}{d\pi}-1
=u_{r,\sigma}+\sum_{j=1}^m a_{r,\sigma,j}\phi_j,
\]

where the residual `u` is Green-small, `m=O(1)`, and the exceptional coefficient vector evolves under a fixed finite-dimensional transfer matrix. The target theorem would replace `G_n(h)->0` in Theorem A by a Green-small residual plus finitely many explicit positive exceptional fronts, and prove cutoff from the joint radial/exceptional crossing law. The synchronized multifront theorem shows this strategy can succeed when the fronts are literal coordinates; the next task is to derive it for angular spectral defects.

This next step is `CONJECTURAL`; it is not promoted to a theorem here.

## 13. ledger_delta

```yaml
ledger_delta:
  parent: "T08 / Salez arXiv:2508.21055 Problem 2.3"
  parent_before: "PARTIAL / OPEN"
  parent_after: "PARTIAL / OPEN"
  source_level_advance:
    theorem: "finite-range orbit-Green reuse with quantitative Gaussian window"
    application: "42-regular Cayley line squares L(X_n)^2 of fully Ramanujan arithmetic (9,3) bigraphs"
    output_gap_lower: "(10-sqrt(33))/14"
    cutoff_center: "(147/139) log_4 n + O(1)"
    profile: "Phi(-z sqrt(2685619/6502986))"
    profile_error: "O_Z(log log n / sqrt(log n))"
    long_range_status: "fails every fixed positive LRE constant; cover branching 16 versus degree benchmark 41"
  mechanism_advance:
    statement: "angular orbit Green bounds are reusable under arbitrary fixed finite-range invariant rewiring of the same transitive cover; only the radial/type Markov-additive clock changes"
    demonstrated_transfer: "line graph -> line-square walk on a triangular non-tree cover, preserving the EFMP shell Green front"
  exact_continuous_time:
    convention: "H_t=exp(t(P-I))"
    radial_speed: "139/147"
    variance_rate: "14746/7203"
    tau_squared: "6502986/2685619"
  companion_split:
    NM13_01: "incidence/halving and direct NBRW projection"
    P26: "finite-orbit angular Green reuse plus finite-range radial clocks"
  preserved_failures:
    - "positive exceptional NBRW sector unresolved"
    - "Ihara/first-repeat tangle route incomplete"
    - "global point-source stationary L2 too strong"
    - "positive scalar filter cannot generally cancel positive slow modes"
  sanity_correction:
    provisional_checker: "orientation bookkeeping error; preserved but excluded from evidence"
    corrected_marker: "P26_T08_LINE_SQUARE_FINITE_RANGE_GREEN_CORRECTED_EXACT_PASS"
  status: "CANDIDATE_FULL for restricted theorem/application; independent review still required"
  publication_novelty: "UNVERIFIED"
  next_attack: "finite-rank angular defect transfer with a Green-small residual and explicit positive exceptional coefficient dynamics"
```

End of complete P26 substantive T08 report.
