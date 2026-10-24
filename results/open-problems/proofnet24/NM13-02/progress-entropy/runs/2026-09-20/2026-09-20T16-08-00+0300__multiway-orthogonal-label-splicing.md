Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED.** No authenticated GPT-6 / maximum-effort metadata is exposed in this runtime.

# NM13-02 T01 — multiway spectral-orthogonal label splicing and a paid connected-core application

## 0. Parent scope/bound versus mechanism gain

**Parent problem.** Friedgut–Kalai Fourier entropy–influence (FEI): prove a finite universal constant `C` such that

\[
H(\widehat f^{\,2})\le C I(f)
\]

for every Boolean function on every finite uniform cube.

**Parent status before -> after:** **OPEN -> OPEN**.

**Universal finite constant before -> after:** **UNKNOWN -> UNKNOWN**.

No finite-dimensional check or restricted stopping class below is promoted to full FEI.

**Mechanism gain.** P03's newest report isolates the remaining issue in its spectral-orthogonal splice as making the accumulated virtual-selector surcharge summable by influence. This run proves a many-way flattening theorem: an arbitrary finite family of pairwise Fourier-support-disjoint controller phases can be spliced through one physical label partition, and the entire extra spectral branch uncertainty is bounded by the physical boundary of that partition. The surcharge is paid **once**, independently of the number of labels or of any binary splice depth:

\[
B_A(F)\le \sum_z\beta_z H(u_z)+2I_Y(F).
\]

Combined with the preceding NM13-02 block-compression theorem, this yields a full hereditary tree bound

\[
R_{\mathcal T}(F)
\le C_A I_A(F)+(K_Y+2)I_Y(F)
\]

whenever the controllers have direct constant `C_A` and the physical `A`-leaves have hereditary constant `K_Y`.

For the concrete signed-translation-rigid connected cubic cycle

\[
P_d(a,y)=\sum_{j=1}^d a_jy_jy_{j+1}\pmod2,
\qquad y_{d+1}=y_1,
\]

the theorem and the preserved exact quadratic hereditary certificate give

\[
\boxed{R_{\mathcal T}((-1)^{P_d})\le \frac95 I((-1)^{P_d})}
\]

for every `d>=3`. Thus P03's cumulative selector-surcharge obstruction is completely paid on an unbounded connected, signed-rigid family by a single label-boundary budget.

---

## 1. Current dependencies and compact handoff

Controlling policy: `operations/PROGRESS20_2026-09-20.md`, blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`. LIVE20 assigns NM13-02 to T01 hereditary entropy/recombination theory paired with P03.

Newest P03 substantive dependency consumed:
`proofnet24/P03-fei/runs/2026-09-20/2026-09-20T15-29-48+0300__fei-spectral-orthogonal-controller-splicing.md`, current blob `7a4cf6bd978750ce2fe13c95ac5f5db36c6032e9`.
It proves for two controller phases with disjoint Fourier supports an exact block factorization with a virtual-selector term `B_sel`, proves `B_sel<=h2(M)` with a KL rebate, obtains zero surcharge for isospectral siblings, and explicitly leaves the general task of making accumulated virtual-selector surcharges summable by influence on the signed-translation-rigid connected core. Those P03 claims remain peer results pending later independent review; the theorem below is proved independently from Fourier orthogonality plus the already-proved NM13 block theorem.

Immediately preceding own report:
`proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T15-08-00+0300__block-compression-balanced-controller.md`, blob `c155fb1d672bfe9858463391f2db0d15c5b5559d`. It proves that every complete adaptive physical query of block `A` pays hereditary allocation at most

\[
R_{\mathcal T_A}(f)\le B_A(f):=H(S_A\mid S_{A^c}),
\]

and that the queried influence of the block is exactly `I_A(f)`.

Preserved earlier NM13-02 mathematics used here: quadratic phases have exact hereditary allocation at most their influence (the quadratic-rank telescope); exact max-splicing/influence budgets; one-point quadratic defects; descendant-influence and variance-paid separators; quadratic-normalized Wiener control; affine-flat and guarded-selector classes; oblique-derivative payments; character-child cross-fibre rescue. Restricted fresh-control results remain restricted. Retired false routes remain retired: pointwise erasure, fixed affine drift, all-coordinate absolute-overlap selector, derivative-degree scalar scheduling, blind root curvature, fixed-`s<2` Renyi payment, frozen-parent endpoint payment, marginal-entropy substitution, and arbitrary orthogonal-involution relaxation.

### Primary-source status checked 20 September 2026

González–MacManus–Pereyra, arXiv:2606.00246 (submitted 29 May 2026), still states universal FEI as a conjecture and says its key restriction inequality would imply full FEI if universal; it proves restricted stopping classes. Li–Han, arXiv:2512.03117 (submitted 2 December 2025), still has the additional coordinate-profile term `sum_i I_i log(1/I_i)`. No source-matching universal FEI proof was recovered in the bounded fresh check. Publication priority for the theorem below is **UNVERIFIED**.

---

## 2. Setup

Let the physical cube split into disjoint coordinate blocks `A` and `Y`. Let `Z` be a finite label set. For each `z in Z`, let

\[
u_z:\{-1,1\}^A\to\{-1,1\}
\]

be Boolean, and assume their Fourier supports are pairwise disjoint:

\[
\boxed{\operatorname{supp}\widehat u_z\cap
\operatorname{supp}\widehat u_{z'}=\varnothing
\quad(z\ne z').}
\tag{2.1}
\]

Let `q:{-1,1}^Y->Z` be an arbitrary physical label map and `s:{-1,1}^Y->{-1,1}` an arbitrary sign. Define

\[
\boxed{F(a,y)=s(y)u_{q(y)}(a).}
\tag{2.2}
\]

Write

\[
E_z=\{y:q(y)=z\},\qquad
c_z(y)=s(y)1_{E_z}(y),\qquad
\beta_z=\Pr(E_z).
\tag{2.3}
\]

Define the physical label boundary

\[
L(q):=\sum_{j\in Y}\Pr_y[q(y)\ne q(y^{\oplus j})].
\tag{2.4}
\]

---

## 3. Exact many-way spectral factorization

### Theorem 3.1
Under (2.1)-(2.2), let `S=(S_A,S_Y)` be the spectral random set of `F`. Then there is a latent label `Z_*` such that

\[
\boxed{
B_A(F):=H(S_A\mid S_Y)
=H(Z_*\mid S_Y)+\sum_z\beta_z H(u_z).
}
\tag{3.1}
\]

Moreover

\[
\boxed{I_A(F)=\sum_z\beta_z I(u_z).}
\tag{3.2}
\]

The latent label has marginal law `Pr(Z_*=z)=beta_z`, hence

\[
H(Z_*\mid S_Y)\le H(\beta).
\tag{3.3}
\]

### Proof
Fourier factorization gives, for `U subseteq A`, `T subseteq Y`,

\[
\widehat F(U,T)=\sum_z\widehat u_z(U)\widehat c_z(T).
\]

For a fixed `U`, condition (2.1) allows at most one nonzero summand. Therefore

\[
\widehat F(U,T)^2
=\sum_z \widehat u_z(U)^2\widehat c_z(T)^2.
\tag{3.4}
\]

Interpret the right side as a disjoint mixture. Its component `z` has total mass

\[
\sum_T\widehat c_z(T)^2=\|c_z\|_2^2=\beta_z.
\]

Because the controller Fourier supports are disjoint, the mixture label `Z_*` is a deterministic function of `S_A` wherever the spectral law has positive mass. Conditional on `Z_*=z`, the `A`- and `Y`-spectral labels are independent, with controller law `\widehat u_z^2`. Hence

\[
H(S_A\mid S_Y)
=H(Z_*\mid S_Y)+H(S_A\mid Z_*,S_Y)
=H(Z_*\mid S_Y)+\sum_z\beta_zH(u_z),
\]

which is (3.1). Its marginal is `beta`, proving (3.3).

Summing `|U|` against (3.4) and using Parseval for each `c_z` gives

\[
I_A(F)=\sum_z\beta_z I(u_z),
\]

proving (3.2). QED.

This is the many-way analogue of P03's two-controller factorization, but the proof above is self-contained and does not take over the peer claim.

---

## 4. Entropy of a cube partition is paid by its label boundary

### Lemma 4.1
For every finite-valued map `q` on a uniform cube,

\[
\boxed{H(q(Y))\le L(q).}
\tag{4.1}
\]

### Proof
For each cell `E_z`, let

\[
b_z:=\sum_j\Pr[1_{E_z}(Y)\ne1_{E_z}(Y^{\oplus j})].
\]

Every label-changing edge belongs to exactly two cell boundaries, so

\[
\sum_zb_z=2L(q).
\tag{4.2}
\]

If every `beta_z<=1/2`, cube edge-isoperimetry gives

\[
b_z\ge2\beta_z\log_2(1/\beta_z),
\]

and summing yields `H(beta)<=L(q)`.

Otherwise there is exactly one cell, say `z=0`, with `beta_0>1/2`. Put `epsilon=1-beta_0`. For every `z!=0`, edge-isoperimetry gives

\[
\beta_z\log_2(1/\beta_z)\le b_z/2.
\]

Therefore the small-cell entropy contributes at most

\[
\frac12\sum_{z\ne0}b_z=L(q)-b_0/2.
\tag{4.3}
\]

The big-cell term obeys

\[
\beta_0\log_2(1/\beta_0)
\le \epsilon\log_2(1/\epsilon)
\le b_0/2.
\tag{4.4}
\]

The first inequality is the elementary comparison
`x log(1/x) >= (1-x)log(1/(1-x))` for `0<x<=1/2`; the second is edge-isoperimetry applied to the complement of `E_0`. Adding (4.3)-(4.4) gives (4.1). QED.

Equality is possible, e.g. for the identity labeling of the whole cube, so this is not a vacuous envelope.

---

## 5. The label boundary is already present in residual influence

### Lemma 5.1
For `F` in (2.2),

\[
\boxed{L(q)\le2I_Y(F).}
\tag{5.1}
\]

### Proof
Fix a residual coordinate `j` and an edge `y<->y^{\oplus j}`.

If the labels agree, the edge may or may not change `F` according to the sign `s`; this contribution is nonnegative and can be ignored.

If the labels are distinct, say `z!=z'`, then disjoint Fourier support implies orthogonality:

\[
\mathbb E_a[u_z(a)u_{z'}(a)]
=\sum_U\widehat u_z(U)\widehat u_{z'}(U)=0.
\]

Thus, regardless of the two signs `s(y),s(y^{\oplus j})`, exactly half of controller assignments `a` make the two endpoint values of `F` disagree. Therefore

\[
\operatorname{Inf}_j(F)
\ge\frac12\Pr[q(y)\ne q(y^{\oplus j})].
\]

Summing over `j` proves (5.1). QED.

Combining Theorem 3.1 with Lemmas 4.1 and 5.1 gives the central paid factorization:

\[
\boxed{
B_A(F)
\le \sum_z\beta_z H(u_z)+2I_Y(F).
}
\tag{5.2}
\]

The constant `2` in front of residual influence is sharp for this coarse partition-boundary mechanism: take two equiprobable label cells separated by every edge of one physical bit and two orthogonal controller characters. Then `H(beta)=L=1` while the label-changing part of `I_Y` is `1/2`.

---

## 6. Hereditary many-way splicing

### Theorem 6.1
Assume, in addition, that all controller phases satisfy the direct estimates

\[
H(u_z)\le C_A I(u_z),
\tag{6.1}
\]

and that after fixing the complete block `A`, every physical leaf `F_a(y)` has a full hereditary certificate with constant `K_Y`:

\[
R_{\mathcal T_a}(F_a)\le K_Y I(F_a).
\tag{6.2}
\]

Then `F` has a full physical restriction tree satisfying

\[
\boxed{
R_{\mathcal T}(F)
\le C_A I_A(F)+(K_Y+2)I_Y(F)
\le\max\{C_A,K_Y+2\}I(F).
}
\tag{6.3}
\]

### Proof
Query every coordinate of `A` first, in any complete adaptive order. The preceding NM13-02 block-compression theorem gives

\[
R_{\mathcal T_A}(F)\le B_A(F).
\]

By (5.2), (6.1), and the exact controller influence identity (3.2),

\[
R_{\mathcal T_A}(F)
\le C_A I_A(F)+2I_Y(F).
\tag{6.4}
\]

Graft the leaf trees (6.2). The exact physical restriction identity gives

\[
\mathbb E_a I(F_a)=I_Y(F),
\]

so the average descendant cost is at most `K_Y I_Y(F)`. Adding to (6.4) proves (6.3). QED.

**Interpretation for P03's newest obstruction.** A binary implementation of many spectral-orthogonal branches can expose a virtual selector at several levels. The theorem flattens all those labels into one physical partition and charges their total branch uncertainty only once, through `H(beta)<=L(q)<=2I_Y`. Therefore cumulative selector surcharge is summable on this whole many-way geometry without a depth factor.

---

## 7. Quadratic-label lifting: a new cubic hereditary class

Let `A={a_1,...,a_d}` be tag/controller coordinates and `Y` arbitrary. Let

\[
q_0,q_1,\ldots,q_d:\{0,1\}^Y\to\mathbb F_2
\]

all have algebraic degree at most two. Define

\[
\boxed{
F(a,y)=(-1)^{q_0(y)+\sum_{j=1}^d a_jq_j(y)}.
}
\tag{7.1}
\]

Set `q(y)=(q_1(y),...,q_d(y))`. Then

\[
F(a,y)=s(y)\chi_{q(y)}(a),\qquad s(y)=(-1)^{q_0(y)}.
\]

The controllers `chi_z` are distinct characters, hence have pairwise disjoint one-point Fourier supports and zero Fourier entropy. Thus `C_A=0` in Theorem 6.1. After fixing `a`, the remaining phase

\[
q_0+\sum_ja_jq_j
\]

is quadratic, and the preserved NM13-02 quadratic-rank theorem gives hereditary constant `K_Y=1`. Therefore

\[
\boxed{
R_{\mathcal T}(F)\le3I_Y(F)\le3I(F).
}
\tag{7.2}
\]

This is uniform in `d`, ambient dimension, rank and overlap pattern of the quadratic labels. It is fresh-variable-free and all-dimensional.

The known generic degree-three hereditary coefficient in the project is

\[
4h_2(1/4)=3.245112497836531\ldots,
\]

so (7.2) strictly improves that coefficient on the full quadratic-label selector subclass.

---

## 8. Signed-translation-rigid connected cycle application

For `d>=3`, use `2d` variables `a_1,...,a_d,y_1,...,y_d` and define

\[
P_d(a,y)=\sum_{j=1}^d a_jy_jy_{j+1}\pmod2,
\qquad y_{d+1}=y_1,
\tag{8.1}
\]

\[
f_d=(-1)^{P_d}.
\]

This is (7.1) with `q_j(y)=y_jy_{j+1}` and `q_0=0`, so it already satisfies `R<=3I_Y`.

### Exact influence budget
For a controller coordinate `a_j`, the phase changes iff `y_j=y_{j+1}=1`, hence

\[
\operatorname{Inf}_{a_j}(f_d)=\frac14,
\qquad I_A(f_d)=\frac d4.
\tag{8.2}
\]

For a residual coordinate `y_j`, the label vector `q(y)` changes iff at least one of its two neighbors `y_{j-1},y_{j+1}` equals one. That event has probability `3/4`, and an actual label change makes two distinct controller characters disagree on exactly half of controller assignments. Hence

\[
\operatorname{Inf}_{y_j}(f_d)=\frac12\cdot\frac34=\frac38,
\qquad I_Y(f_d)=\frac{3d}{8}.
\tag{8.3}
\]

Therefore

\[
I(f_d)=\frac{5d}{8}
\]

and (7.2) sharpens to

\[
\boxed{
R_{\mathcal T}(f_d)
\le3I_Y(f_d)
=\frac{9d}{8}
=\frac95 I(f_d).
}
\tag{8.4}
\]

### Connected high-degree interaction core
The degree-three ANF hyperedges are

\[
\{a_j,y_j,y_{j+1}\},\qquad j=1,\ldots,d.
\]

They form one connected cycle through the `y` variables. Their minimum vertex cover is

\[
\tau=\lceil d/2\rceil:
\]
choosing alternating `y` variables achieves this, while every chosen `y` covers at most two edges and every chosen `a` covers only one. Thus the old hit-every-cubic-monomial depth certificate can grow with `d`; the new block payment does not.

### Signed-translation rigidity
Write a possible translation as `(A,Y)`. The degree-two homogeneous part of the derivative

\[
P_d(a+A,y+Y)+P_d(a,y)
\]

is

\[
\sum_j A_jy_jy_{j+1}
+\sum_j a_j(Y_jy_{j+1}+Y_{j+1}y_j).
\tag{8.5}
\]

If the derivative were constant, every coefficient in (8.5) would vanish. The monomial `y_jy_{j+1}` forces `A_j=0` for every `j`; then the distinct monomials `a_jy_{j+1}` and `a_jy_j` force every `Y_j=0`. Hence there is no nonzero translation for which the multiplicative derivative is constant `+1` or `-1`.

So `f_d` is signed-translation-rigid and its degree-`>=3` ANF interaction hypergraph is a single connected component: exactly the geometry highlighted in P03's newest handoff. The gain is not merely another isospectral quotient; it pays a genuinely many-label branch uncertainty by the physical residual boundary.

---

## 9. What did not close

1. **Generic two-hard overlap remains.** Pairwise disjoint controller Fourier supports are essential to the exact mixture law (3.4). If two controller spectra overlap, coherent cross terms return and there is no latent component label determined by `S_A`. This is still the main uncontrolled geometry.
2. **Arbitrary quadratic twists in the controller block are not absorbed.** Multiplying all controller characters by a common non-affine quadratic phase generally makes their Fourier supports overlap in rank-dependent cosets. Grouping by those cosets did not produce a dimension/rank-independent replacement in this run. No such extension is claimed.
3. **The factor two boundary payment is sharp for the coarse partition step.** Improving the universal coefficient below two requires using the conditional spectral information `H(Z_*|S_Y)` or P03's Hellinger/KL rebate, not only the unconditional label law `beta`.
4. **No full FEI selector follows.** A general Boolean function need not admit a useful spectral-orthogonal controller family whose leaves lie in a certified class. Thus (6.3) is a new hereditary closure mechanism, not universal FEI.

The next nonredundant target is to replace exact support disjointness by a quantitative overlap matrix and prove an amortized correction that is paid by residual influence/Hellinger defect without a factor growing in the number of controller components. A counterfamily with bounded physical boundary but unavoidable coherent overlap would be equally decisive.

---

## 10. Executed sanity checker

Executed checker:
`proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T16-08-00+0300__check_multiway_orthogonal_label_splicing.py`

creation commit `d28130242dc2b626b7149da0044ea9652f9eb1fd`, blob `cd14630fb0bd95867f73d7480ca6780a695a5f22`.

Preserved actual output:
`proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T16-08-00+0300__multiway_orthogonal_label_splicing_check.json`

creation commit `51275ff572d3252ea1ee52f84b4737c5e6392331`, blob `f56b1fe98d643e44854991170632202acb2271e0`.

The checker returned `PASS` and includes three genuinely new checks:

- all `4096` character-controller cases with `|A|=|Y|=2`, exhausting every label map and residual sign, with zero violations of `B_A<=H(label)<=L<=2I_Y` and zero controller-influence identity error;
- `256` cases using an explicit pair of non-character dimension-three Boolean controllers whose Fourier supports are `{0,2,4,6}` and `{1,3,5,7}`, with maximum exact factorization error `4.44e-16` and zero boundary-payment violation;
- the connected cycle family for `3<=d<=7`, checking the exact block entropy, label entropy, boundary and influence formulas; exact minimum cubic vertex cover `ceil(d/2)` through `d=8`; and brute-force absence of signed translations for `d=3,4,5`.

The largest exact-block certificate ratio recorded for the sampled cycle dimensions was `1.6043618656`, below the analytic `9/5` hereditary envelope. The finite computation is a sanity check only; the theorem is proved analytically above.

---

## 11. ledger_delta

```text
ledger_delta:
  problem: NM13-02 / T01 Fourier entropy-influence
  source_status_before: OPEN
  source_status_after: OPEN
  universal_constant_before: UNKNOWN
  universal_constant_after: UNKNOWN
  new_mechanism:
    - exact many-way spectral-orthogonal controller factorization
      B_A = sum_z beta_z H(u_z) + H(Z_* | S_Y)
    - cube-partition entropy payment H(beta) <= label_boundary
    - label_boundary <= 2 I_Y for orthogonal controller labels
    - paid hereditary closure R <= C_A I_A + (K_Y+2) I_Y
    - no dependence on label count or binary splice depth
  new_application:
    - quadratic-label selector phases have hereditary constant <= 3
    - signed-rigid connected cubic cycle P_d=sum_j a_j y_j y_{j+1}
      has R <= (9/5) I for every d>=3
    - cycle cubic vertex-cover number is ceil(d/2), so the gain is not a shallow hitting-set artifact
  precise_P03_obstruction_addressed:
    - cumulative virtual-selector surcharge is summable on arbitrary many-way exact spectral-orthogonal label partitions
  remaining_obstruction:
    - quantitative coherent overlap when controller Fourier supports are not disjoint
    - arbitrary non-affine quadratic controller twist remains unproved
  fresh_control_used: false
  finite_checker_status: PASS
  exhaustive_character_cases: 4096
  noncharacter_pair_cases: 256
  independent_review: PENDING
  publication_priority: UNVERIFIED
  full_FEI_closed: false
```

**End of immutable run report.**
