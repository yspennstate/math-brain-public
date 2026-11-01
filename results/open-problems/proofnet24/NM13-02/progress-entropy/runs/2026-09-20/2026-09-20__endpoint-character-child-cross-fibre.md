Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — not authenticated as GPT-6 at maximum.

# NM13-02 T01 — exact cross-fibre endpoint payment for arbitrary character-child splits

## 0. Parent scope/bound versus mechanism gain

**Parent problem.** Friedgut–Kalai Fourier entropy–influence (FEI): prove a finite universal constant `C` such that

\[
H(\widehat f^{\,2})\le C I(f)
\]

for every Boolean function on every finite uniform cube.

**Parent status before -> after:** **OPEN -> OPEN**.

**Universal finite upper bound before -> after:** **UNKNOWN -> UNKNOWN**.

Neither the theorem below, the finite checker, nor P03's restricted polynomial/affine stopping classes settle full FEI.

**New mechanism gain.** P03's current whole-function endpoint route uses

\[
\Phi_n(f):=n\left(\sum_S|\widehat f(S)|^{2-1/n}-1\right)
\]

and asks for a dimension-free paid physical selector. Its newest affine-fibre continuation proves that a tempting **single Fourier-fibre** payment is false: on a constant-child / one-point-defect split the exceptional fibre charge divided by its own minority square grows like `n`, while the handoff observes only for that special family that the other fibres collectively rescue the whole-function charge. The later polynomial-core continuation preserves this as a live full-scope route: a universal weighted-erasure bound or a valid whole-function endpoint selector is still missing.

This run proves the exact cross-fibre rescue for **every** split having one affine-character child and an otherwise arbitrary Boolean opposite child:

\[
\boxed{
A_i^{(n)}(f)
:=\Phi_n(f)-\frac{\Phi_{n-1}(f^0)+\Phi_{n-1}(f^1)}2
\le 4j_i(f)(1-j_i(f))\le4j_i(f).
}
\tag{0.1}
\]

No hypothesis is placed on the other child. More precisely, the exceptional/mean fibre is paid by **one half of the opposite child's total nonconstant Fourier mass**, while all nonconstant fibres together cost at most the other half. This is exactly the joint cross-fibre allocation that P03's scalar obstruction says a successful endpoint proof must retain.

The theorem yields a paid dependent-branch closure: arbitrary finite chains of character branches can be grafted above any stopping class satisfying `H<=C J` without a depth penalty in the endpoint potential. The resulting direct FEI coefficient is

\[
\boxed{
H(f)\le \frac{2}{\ln2}\max\{4,C/2\}\,J(f)
=\max\{8/\ln2,\,C/\ln2\}\,J(f).
}
\tag{0.2}
\]

Applied to P03's newest polynomially coupled symmetric-core stopping class, this gives a new restriction-tree closure under arbitrary repeated character-child grafts. It is not numerically better than all older character-child entropy-decrement bounds; its point is that it closes the **dimension-adaptive endpoint** payment at those dependent nodes and demonstrates the required cross-fibre mechanism exactly.

---

## 1. Current directive, dependencies, and compact handoff

Controlling policy: `operations/PROGRESS20_2026-09-20.md`, blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`. LIVE20 assigns NM13-02 to T01 hereditary entropy/recombination theory paired with P03.

Current P03 dependencies actually consumed:

1. `proofnet24/P03-fei/continuations/2026-09-20-affine-fibres/REPORT.md`, blob `29d8afcabc09ee1564a1e0db51cf42a21ffa804d`, and its handoff blob `5f236046ea4cb44c91b74866e7677b83266dbd02`. These establish the sharp affine-fibre gluing theorem and, crucially here, Proposition 10.1: the coefficientwise endpoint charge on the exceptional one-point-defect fibre satisfies
   \[
   T_n/\delta_n^2=n+\frac32-2\ln2+o(1),
   \]
   so no uniform payment by that fibre's own minority square can work. The handoff separately notes that in the one-point family the full whole-function charge remains bounded because other fibres share the budget.
2. `proofnet24/P03-fei/continuations/2026-09-20-polynomial-cores-and-tags/HANDOFF.md`, blob `c25d6a9f9cff6abfb4b730c3fe5cd7342f01ea1e`, and current `proofnet24/P03-fei/README.md`, blob `816372d8c14d65d3b064d364385c8b6da51b9eb0`. These are newer than the affine-fibre report and preserve the exact full-scope gap: either prove a universal weighted-erasure allocation or a whole-function dimension-adaptive endpoint selector retaining Boolean convolution/cross-fibre cancellation. The polynomially coupled symmetric-core and polynomial-tag results are stopping classes, not unrestricted FEI.

Compact NM13-02 mathematics preserved unchanged:

- quadratic phases have exact rank telescopes and hereditary allocation constant `1`;
- queried influence plus weighted residual leaf influence is an exact budget, enabling max-splicing of branch-dependent certificates;
- one-point perturbations of arbitrary quadratic phases have hereditary constant
  \[
  C_\chi=2+\frac1{\sqrt e\ln2}=2.8750387749\ldots;
  \]
- character-child entropy allocation, oblique-derivative approximate quotient peeling, variance-paid separators, quadratic-normalized Wiener control, and the two-flat theorem remain restricted positive mechanisms;
- fresh-control theorems remain restricted because they append variables and do not establish fixed-domain FEI;
- the false pointwise erasure shortcut, fixed-coefficient affine-drift route, Han absolute-overlap selector, derivative-degree scalar scheduler, blind root-curvature payment, fixed-`s<2` Renyi payment, and general-orthogonal-involution relaxation remain retired.

The present proof does **not** assume P03's universal endpoint selector; it proves a new local endpoint inequality on an all-dimensional class of physical splits. The elementary endpoint entropy comparison needed for the final corollary is rederived below.

### Primary-source status checked 20 September 2026

A bounded fresh source check found González–MacManus–Pereyra, arXiv:2606.00246 (submitted 29 May 2026, updated 2 June 2026), still explicitly presenting universal FEI as a conjecture and explaining that their restriction inequality would imply full FEI if it held for all Boolean functions. Li–Han, arXiv:2512.03117 (submitted 2 December 2025), sharpens Han's general inequality but still retains the coordinate-profile term `sum_i I_i log(1/I_i)`. No source-matching universal FEI proof was recovered. This is bounded status recovery, not a novelty certificate.

---

## 2. Endpoint potential and exact physical charge

For a Boolean `f:F_2^n->{-1,1}` define, for `n>=1`,

\[
s_n:=2-\frac1n,
\qquad
M_n(f):=\sum_S|\widehat f(S)|^{s_n},
\qquad
\Phi_n(f):=n(M_n(f)-1).
\tag{2.1}
\]

For `n=1`, every Boolean function is an affine character, so `M_1=1` and `Phi_1=0`.

At a physical split on coordinate `i`, with children `g=f^0`, `h=f^1` on `m=n-1` variables, define

\[
A_i^{(n)}(f)
:=\Phi_n(f)-\frac{\Phi_m(g)+\Phi_m(h)}2.
\tag{2.2}
\]

This definition gives an exact tree telescope by induction: for every finite physical restriction tree `T`,

\[
\Phi_n(f)
=\sum_{v\in T_{\rm int}}w_v A_{i(v)}^{(d_v)}(f_v)
 +\sum_{\ell\in T_{\rm leaf}}w_\ell\Phi_{d_\ell}(f_\ell).
\tag{2.3}
\]

No probabilistic theorem is used in (2.3); it is simply repeated substitution of (2.2).

It is useful to write the potential coefficientwise:

\[
\psi_d(t):=d\bigl(t^{2-1/d}-t^2\bigr),\qquad 0\le t\le1,
\tag{2.4}
\]

so Parseval gives

\[
\Phi_d(u)=\sum_S\psi_d(|\widehat u(S)|).
\tag{2.5}
\]

This is exactly the decomposition in which P03 found the single-fibre obstruction.

---

## 3. Reduction of a character child to a constant child

Assume one child, say `g`, is an affine character up to sign on the residual cube.

Multiplying the parent by the same residual character translates every Fourier coefficient in the residual frequency and therefore preserves every `M_p`, hence preserves `A_i`. It makes `g` constant. Multiplying additionally by the query character `(-1)^{x_i}` swaps `h` with `-h` at the level relevant to the split, again preserving all Fourier magnitudes and `A_i`. Therefore we may assume

\[
g\equiv1,
\qquad
\mu:=\Pr[h=-1]=j_i(f)\le\frac12.
\tag{3.1}
\]

Write residual Fourier coefficients

\[
a_T=\widehat h(T),\qquad a_\varnothing=1-2\mu\ge0,
\qquad t_T:=|a_T|\quad(T\ne\varnothing).
\tag{3.2}
\]

Parseval gives the exact variance budget

\[
\sum_{T\ne\varnothing}t_T^2
=1-(1-2\mu)^2
=4\mu(1-\mu).
\tag{3.3}
\]

Because `h` is Boolean on `m` variables, each nonzero Walsh coefficient lies on the dyadic lattice

\[
t_T\ge 2^{1-m}.
\tag{3.4}
\]

Indeed `2^m a_T` is a sum of `2^m` signs, hence an even integer.

The parent Fourier pair associated with `T=emptyset` has magnitudes `(1-mu,mu)`. For every nonempty `T`, the parent has the two equal magnitudes `(t_T/2,t_T/2)`. Thus

\[
A_i^{(n)}(f)=T_n(\mu)+\sum_{T\ne\varnothing}U_n(t_T),
\tag{3.5}
\]

where

\[
T_n(\mu)
:=\psi_n(1-\mu)+\psi_n(\mu)
 -\frac12\psi_m(1)-\frac12\psi_m(1-2\mu),
\tag{3.6}
\]

and

\[
U_n(t):=2\psi_n(t/2)-\frac12\psi_m(t).
\tag{3.7}
\]

`T_n` is P03's exceptional fibre quantity. The point is to pay it from the **shared variance (3.3)** rather than from `mu^2`.

---

## 4. Exceptional fibre is paid by half the shared nonconstant mass

### Lemma 4.1
For every `n>=2`, `m=n-1`, and every Boolean-admissible `0<=mu<=1/2`,

\[
\boxed{T_n(\mu)\le2\mu(1-\mu)
=\frac12\sum_{T\ne\varnothing}t_T^2.}
\tag{4.1}
\]

### Proof
Define

\[
C_n(\mu):=
 n\bigl[(1-\mu)^{s_n}+\mu^{s_n}-1\bigr]
 -\frac m2\bigl[(1-2\mu)^{s_m}-1\bigr].
\tag{4.2}
\]

A direct subtraction of the square terms in (3.6) gives

\[
T_n(\mu)=C_n(\mu)+2\mu(1-\mu).
\tag{4.3}
\]

So it suffices to prove `C_n(mu)<=0`.

For `n=2`, the residual cube has one bit, hence after folding `mu` is `0` or `1/2`; direct substitution gives `C_2(0)=0` and `C_2(1/2)=2(2^{-1/2}-1)+1/2<0`.

Now let `n>=3` and put `m=n-1`,

\[
a=1-\frac1n=\frac m{m+1},
\qquad
b=1-\frac1m=\frac{m-1}{m}.
\]

Set `F_n=-C_n`. Then

\[
F_n(0)=0,
\tag{4.4}
\]

and

\[
F_n(1/2)
=n\left(1-2^{-1+1/n}\right)-\frac{n-1}{2}
=\frac{n+1-n2^{1/n}}2\ge0.
\tag{4.5}
\]

The last inequality follows from `2^{1/n}<=1+1/n`, equivalently `2<=(1+1/n)^n`.

Differentiate on `(0,1/2)`:

\[
F_n'(\mu)
=(2n-1)\bigl[(1-\mu)^a-\mu^a\bigr]
 -(2n-3)(1-2\mu)^b.
\tag{4.6}
\]

Set `x=mu/(1-mu) in (0,1)`. The ratio of the two positive shape factors is

\[
R(x):=
\frac{(1-\mu)^a-\mu^a}{(1-2\mu)^b}
=
\frac{1-x^a}{1-x}
(1-x)^{1-b}(1+x)^{b-a}.
\tag{4.7}
\]

All three factors on the right are decreasing in `x`:

- `(1-x^a)/(1-x)` is the secant slope of the concave function `t^a` between `x` and `1`, hence decreases as `x` increases;
- `1-b=1/m>0`, so `(1-x)^{1-b}` decreases;
- `b-a=-1/[m(m+1)]<0`, so `(1+x)^{b-a}` decreases.

Thus `R` is strictly decreasing from `1` to `0`. Equation (4.6) therefore changes sign at most once, from positive to negative. Hence `F_n` increases and then decreases, so its minimum on `[0,1/2]` is attained at an endpoint. By (4.4)-(4.5), `F_n>=0`, equivalently `C_n<=0`. Insert this in (4.3). QED.

This lemma is the exact cross-fibre correction to P03's Proposition 10.1: `T_n/mu^2` may diverge, but `T_n` is always paid by half of the **total** nonconstant spectral square mass of the opposite child.

---

## 5. Every nonconstant fibre costs at most half its square mass

### Lemma 5.1
Let `t>0` be the magnitude of a Fourier coefficient of a Boolean function on `m=n-1` variables. Then

\[
\boxed{U_n(t)\le\frac12t^2.}
\tag{5.1}
\]

### Proof
Expanding (3.7),

\[
U_n(t)+\frac12t^2
=n2^{1-s_n}t^{s_n}-\frac m2t^{s_m}
=:B_n(t).
\tag{5.2}
\]

By the Boolean lattice (3.4), write `t=2^{-q}` with the inequality range replaced by

\[
0\le q\le m-1
\]

for the purpose of maximizing the continuous upper envelope; an actual coefficient need only satisfy `t>=2^{1-m}`, and the same calculation applies with `q=-log_2 t`.

Divide (5.2) by `t^2`:

\[
G_n(q):=\frac{B_n(t)}{t^2}
=\frac n2\,2^{(q+1)/n}-\frac m2\,2^{q/m}.
\tag{5.3}
\]

Its derivative is

\[
G_n'(q)=\frac{\ln2}{2}
\left(2^{(q+1)/n}-2^{q/m}\right)\ge0,
\tag{5.4}
\]

because `(q+1)/n>=q/m` is equivalent to `m>=q`. Therefore the maximum occurs at `q=m-1`, where

\[
G_n(q)\le n2^{-1/n}-m2^{-1/m}.
\tag{5.5}
\]

Let `g(x)=x2^{-1/x}=x e^{-(\ln2)/x}`. Then

\[
g'(x)=e^{-u}(1+u)<1,
\qquad u=\frac{\ln2}{x}>0,
\tag{5.6}
\]

because `e^u>1+u`. Hence

\[
n2^{-1/n}-(n-1)2^{-1/(n-1)}<1.
\tag{5.7}
\]

Thus `B_n(t)<=t^2`, and (5.2) gives `U_n(t)<=t^2/2`. QED.

---

## 6. Main theorem: arbitrary character-child endpoint payment

### Theorem 6.1
Let `f` be Boolean on `n>=2` variables and split physically at coordinate `i`. If either child is an affine character up to sign, then

\[
\boxed{
A_i^{(n)}(f)\le4j_i(f)(1-j_i(f))\le4j_i(f).
}
\tag{6.1}
\]

### Proof
Use Section 3 to reduce to `g=1` and `mu=j_i(f)<=1/2`. Equations (3.5), Lemma 4.1, Lemma 5.1, and Parseval (3.3) give

\[
\begin{aligned}
A_i^{(n)}(f)
&=T_n(\mu)+\sum_{T\ne\varnothing}U_n(t_T)\\
&\le \frac12\sum_{T\ne\varnothing}t_T^2
   +\frac12\sum_{T\ne\varnothing}t_T^2\\
&=4\mu(1-\mu).
\end{aligned}
\]

Since `mu=j_i(f)`, this is (6.1). QED.

The theorem is all-dimensional and the opposite child is completely arbitrary. It is not a finite-dimensional inference.

### What it says about P03's coefficientwise obstruction

On the one-point family `mu=delta_n=2^{1-n}`, P03 proved

\[
T_n/\delta_n^2=n+\frac32-2\ln2+o(1).
\]

The present theorem identifies the general shared budget that makes this harmless. For this family every nonzero child Fourier coefficient has magnitude `2delta_n`, and one obtains exactly

\[
\frac{U_n}{\delta_n^2}
=4\left[n2^{-1/n}-(n-1)2^{-1/(n-1)}\right]
=2+o(1)
\]

when `U_n` is expressed in P03's normalization from (3.7). Consequently

\[
A_i=T_n+(\delta_n^{-1}-1)U_n,
\qquad
\boxed{A_i/\operatorname{Inf}_i\to2.}
\tag{6.2}
\]

The checker reproduces the exact finite values: the exceptional fibre ratio `T_n/delta_n^2` grows from `3.95` at `n=4` to `300.11` at `n=300`, while the whole charge divided by influence tends to `2`. Thus the obstruction is genuinely to **individual-fibre accounting**, not to the whole-function endpoint selector at a character-child node.

---

## 7. Paid dependent-branch recombination with a stopping class

Define folded total influence

\[
J(f)=\sum_i j_i(f),\qquad j_i=\min\{\alpha_i,1-\alpha_i\}.
\]

For a physical split on `i`, residual coordinate influences average:

\[
\alpha_k(f)=\frac{\alpha_k(g)+\alpha_k(h)}2,
\qquad k\ne i.
\]

Since `q -> min(q,1-q)` is concave,

\[
\boxed{
J(f)\ge j_i(f)+\frac{J(g)+J(h)}2.
}
\tag{7.1}
\]

Iterating (7.1) over a restriction prefix gives the folded budget

\[
\sum_{v\in T_{\rm int}}w_vj_{i(v)}(f_v)
+\sum_{\ell\in T_{\rm leaf}}w_\ell J(f_\ell)
\le J(f).
\tag{7.2}
\]

Now suppose every internal node of a finite prefix has at least one affine-character child, and every noncharacter stopping leaf satisfies a direct folded FEI certificate

\[
H(f_\ell)\le C J(f_\ell).
\tag{7.3}
\]

Character leaves have zero spectral entropy and zero endpoint potential.

We rederive the two endpoint/Shannon comparisons needed here. For squared Fourier masses `p_S`, set `X=-ln p_S`. Then

\[
\Phi_d=d\,\mathbb E_p\left(e^{X/(2d)}-1\right).
\]

Since `e^u-1>=u`,

\[
\Phi_d\ge\frac12H_{\rm nat}=\frac{\ln2}{2}H,
\qquad
\boxed{H\le\frac2{\ln2}\Phi_d.}
\tag{7.4}
\]

For Boolean functions on `d` variables, every nonzero Fourier coefficient has magnitude at least `2^{1-d}`, hence `X/(2d)<ln2`. The function `(e^u-1)/u` is increasing, so on `[0,ln2]`,

\[
e^u-1\le\frac{u}{\ln2}.
\]

Therefore

\[
\boxed{\Phi_d\le\frac12H.}
\tag{7.5}
\]

Apply the exact telescope (2.3), Theorem 6.1, (7.3), (7.5), and the budget (7.2):

\[
\begin{aligned}
\Phi_n(f)
&\le 4\sum_vw_vj_{i(v)}(f_v)
 +\frac C2\sum_\ell w_\ell J(f_\ell)\\
&\le\max\{4,C/2\}J(f).
\end{aligned}
\tag{7.6}
\]

Combining with (7.4) proves

\[
\boxed{
H(f)\le\max\{8/\ln2,\,C/\ln2\}\,J(f)
\le\max\{8/\ln2,\,C/\ln2\}\,I(f).
}
\tag{7.7}
\]

This is a paid dependent-branch recombination theorem: the noncharacter continuation may depend arbitrarily on all previous branch values; only the branch actually cut off at each internal node must be a character.

---

## 8. Application to P03's newest stopping class

P03's current polynomial-core continuation proves, for

\[
F=(-1)^P\prod_t h_t,
\]

with disjoint part-symmetric cores `h_t`, maximum part count `d_max`, and `deg P<=r`, the direct folded certificate

\[
H(F)\le C_{\rm poly}J(F),
\]

where

\[
C_{\rm poly}
=\max\left\{12.04+\log_2d_{\max},\;2^rh_2(2^{-r})+\frac2{\ln2}\right\}.
\tag{8.1}
\]

Its tag-phase continuation supplies additional affine-fibre stopping leaves, but explicitly does not claim arbitrary restriction closure.

Take **any** finite physical prefix above such leaves in which each queried node has one affine-character child and the other child is allowed to continue dependently. The root need not itself have a polynomial-core or affine-fibre representation. Theorem 7.1 gives

\[
\boxed{
H(f)\le
\max\left\{\frac8{\ln2},\frac{C_{\rm poly}}{\ln2}\right\}J(f).
}
\tag{8.2}
\]

For fully symmetric cores and polynomial coupling degree at most seven, P03 has `C_poly=12.04`, so the closure coefficient is

\[
12.04/\ln2=17.3700482923\ldots.
\]

This constant is **not** advertised as an improvement over every previously available specialized bound. The demonstrated gain is structural: P03's newest direct stopping class can now be preceded by arbitrarily deep branch-dependent character pruning with no depth loss in the dimension-adaptive endpoint accounting, and the precise single-fibre obstruction is removed on every such node for an arbitrary opposite child.

---

## 9. Failure / remaining obstruction

The theorem does not prove the universal selector because it uses the exact sparsity of one child's spectrum: after a character twist, one child has a single Fourier atom. At a node with **two genuinely hard children**, the exceptional fibre no longer has a single shared variance pool of the form (3.3), and the present proof does not control coherent cancellation between two nontrivial spectra.

I also tested the natural next generalization "replace the character child by an arbitrary quadratic child and normalize by multiplying by that quadratic." This does not immediately preserve `M_s`: quadratic multiplication is an orthogonal block transform in Fourier space, not a permutation. Its `ell_s` operator inflation is rank-dependent at a fixed exponent, and I did not obtain a clean cancellation with the parameter-change credit. That extension is therefore **UNPROVED**, not silently assumed.

The next nonredundant target is a two-hard-child cross-fibre inequality: identify a conserved joint square-mass/Hellinger budget that simultaneously pays the exceptional aligned fibres and the nonexceptional fibres, ideally invariant under quadratic block transforms. If that fails after a second recovery, the preserved fallback is the oblique-derivative basis route from the preceding NM13-02 report.

Full FEI remains open.

---

## 10. Executed sanity checks

Checker:

`proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20__endpoint-character-child-cross-fibre-check.py`

Creation commit: `a1330928996289ac69e6b243250a534f929b9516`.
Blob after readback: `607e54210f0ddd2e00f9fb6fa90ab6b8b9be7369`.

Archived output:

`proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20__endpoint-character-child-cross-fibre-check.out`

Creation commit: `8a411d871370025361e5a12a618e8dd73a57212a`.
Blob after readback: `59f2883aa193188724244e124b50c1a00b17e14f`.

Actual output status: `PASS`.

The checker:

- exhaustively enumerated all `65,812` Boolean opposite children in residual dimensions `m=1,2,3,4` with a constant child and checked `A<=4j(1-j)`, the exact fibre decomposition, `T<=Var/2`, and `sum U<=Var/2`;
- checked the lattice scalar bound `B_n(t)<=t^2` for every allowed dyadic amplitude through `n=200`; the largest observed ratio was `0.999993978120713...`;
- checked `C_n(mu)<=0` on every dyadic folded density through `n=14` and additional 1001-point high-precision grids for dimensions through `128`;
- evaluated the one-point obstruction through `n=300`: the maximum whole `A/j` in that range is `2.181938939861118...` at `n=4`, and the ratio tends numerically to `2`, while `T_n/delta_n^2` grows linearly.

The all-dimensional theorem rests on Sections 4–6, not on this finite verification.

---

## 11. ledger_delta

```yaml
ledger_delta:
  parent_problem: T01_Fourier_entropy_influence
  parent_scope_before: OPEN_unrestricted_all_finite_uniform_cubes
  parent_scope_after: OPEN_unrestricted_all_finite_uniform_cubes
  universal_constant_before: UNKNOWN
  universal_constant_after: UNKNOWN
  latest_peer_obstruction_consumed:
    - P03_affine_fibre_single_fibre_endpoint_charge_unbounded
    - P03_polynomial_core_handoff_whole_function_endpoint_selector_still_unproved
  mechanism_before:
    - one_point_family_only_had_special_aggregate_cancellation_calculation
    - no_exact_arbitrary_opposite_child_cross_fibre_endpoint_payment
  mechanism_after:
    theorem: character_child_endpoint_cross_fibre_payment
    statement: A_i_n_le_4_j_i_times_1_minus_j_i
    opposite_child: arbitrary_boolean
    exceptional_fibre_payment: at_most_half_opposite_child_nonconstant_fourier_square_mass
    nonexceptional_payment: at_most_half_opposite_child_nonconstant_fourier_square_mass
    branch_recombination: arbitrary_depth_character_pruning_above_CJ_stopping_leaves_no_depth_loss_in_Phi
  application:
    target: newest_P03_polynomial_and_affine_stopping_classes
    gain: character_child_physical_prefix_closure_for_dimension_adaptive_endpoint_route
    example_constant_full_symmetric_r_le_7: 12.04_over_ln2_equals_17.3700482923
  not_claimed:
    - full_FEI
    - universal_endpoint_selector
    - quadratic_child_extension
    - independent_review
    - publication_priority
  preserved_false_routes:
    - pointwise_erasure
    - absolute_overlap_Han_selector
    - fixed_affine_drift
    - derivative_degree_scalar
    - blind_curvature_selector
    - fixed_Renyi_exponent_payment
    - general_orthogonal_involution_relaxation
  checker:
    path: proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20__endpoint-character-child-cross-fibre-check.py
    commit: a1330928996289ac69e6b243250a534f929b9516
    blob: 607e54210f0ddd2e00f9fb6fa90ab6b8b9be7369
  output:
    path: proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20__endpoint-character-child-cross-fibre-check.out
    commit: 8a411d871370025361e5a12a618e8dd73a57212a
    blob: 59f2883aa193188724244e124b50c1a00b17e14f
  runtime_model: GPT-5.6_Sol
  reasoning_level: UNVERIFIED
```

No historical/peer file was overwritten. No email, Drive object, public post, paid compute, workflow, access setting, permission, repository visibility, or schedule was changed.
