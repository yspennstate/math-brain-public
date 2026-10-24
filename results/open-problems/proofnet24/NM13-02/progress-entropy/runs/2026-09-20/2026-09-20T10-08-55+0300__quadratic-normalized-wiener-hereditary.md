Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — not authenticated as GPT-6 at maximum.

# NM13-02 T01 — quadratic-normalized Wiener control: paid extraction of an arbitrary quadratic part

## 0. Parent status and substantive movement

**Parent problem.** Friedgut--Kalai Fourier entropy--influence (FEI): prove one finite universal constant `C` such that

\[
H(\widehat f^{\,2})\le C I(f)
\]

for every Boolean function on every finite uniform cube.

**Parent scope/bound before -> after:** **OPEN -> OPEN**. The unrestricted universal finite upper bound remains **UNKNOWN -> UNKNOWN**. No finite-dimensional computation or restricted class below is promoted to full FEI.

**New mechanism-level theorem.** Define the quadratic-normalized Wiener norm

\[
\Lambda_2(f)
:=\min_{\deg q\le2}\Lambda((-1)^qf),
\qquad
\Lambda(g):=\sum_S|\widehat g(S)|.
\tag{0.1}
\]

For `L>=1`, put

\[
C_{\rm QW}(L)
:=\max\left\{15,\;2\log_2 e+12\log_2L\right\}.
\tag{0.2}
\]

Then every Boolean `f` satisfies the direct restricted FEI estimate

\[
\boxed{
H(\widehat f^{\,2})
\le C_{\rm QW}(\Lambda_2(f)) I(f).
}
\tag{0.3}
\]

Moreover `Lambda_2` is nonincreasing under every physical restriction. Consequently there exists a full adaptive physical restriction tree `T` such that

\[
\boxed{
R_T(f)
\le C_{\rm QW}(\Lambda_2(f)) I(f).
}
\tag{0.4}
\]

This is the paid normalization statement missing from P03's newest proof: an arbitrary quadratic phase can be extracted without paying its polar rank in the final constant. The payment depends only logarithmically on the **best residual Wiener norm after quadratic normalization**, and that residual parameter cannot increase on either dependent branch.

This theorem is all-dimensional, uses no fresh variables, and is proved below without assuming P03's separately reported dependent-recombination theorem.

## 1. Current directive, exact peer obstruction, and compact handoff

The controlling policy is `operations/PROGRESS20_2026-09-20.md`, blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`. LIVE20 assigns NM13-02 to T01 hereditary entropy/recombination theory, paired with P03, with substantive derivation taking priority over routine auditing.

`POSTED.md` was checked for exact-scope exclusions. It contains a posted entropy/singularity result of a different scope, but no posted unrestricted FEI theorem and no posted quadratic-normalized Wiener theorem matching (0.3)--(0.4).

### Compact handoff of prior NM13-02 mathematics

Preserved without change:

1. quadratic phases have the exact rank hereditary telescope and hereditary constant at most `1`;
2. exact influence-budget/max-splicing allows branch-dependent leaf certificates without adding constants;
3. character-child and one-defect payments give dimension-free hereditary control;
4. descendant-influence payment and the hybrid branch recursion handle cubic-star and nested-canalizing quadratic-twist classes;
5. arbitrary quadratic twists of two affine-flat signs have the earlier NM13-02 hereditary constant `24`.

P03 subsequently sharpened the specialized two-flat constant and, in its newest report

`proofnet24/P03-fei/runs/2026-09-20/2026-09-20T09-29-44+0300__fei-wiener-hereditary-arrangements.md`

(blob `5a79ac2d8b2bbc29831c4b2764c18e24090a37e2`), proved a Wiener-norm hereditary theorem for arbitrary Boolean functions and bounded affine-flat arrangements. It explicitly identifies the remaining full-scope obstruction as a **paid quadratic/nonquadratic normalization or max-splicing theorem whose cost stays universal when both raw Wiener norm and quadratic rank are large**. It also gives an exact parallel-flat cancellation example showing that componentwise codimension payments are not stable under recombination.

The theorem here attacks precisely that obstruction. It does not overwrite P03's claim: P03 controls raw `Lambda`; NM13-02 controls the new quotient parameter `Lambda_2`, obtained after the best quadratic extraction.

The false pointwise-erasure shortcut, fixed-coefficient affine drift, Han absolute-overlap selector, derivative-degree scalar scheduler, blind curvature/query ratio and retired resolvent/interpolation routes remain false or retired. None is revived.

## 2. Current primary-source status

A fresh bounded check on 20 September 2026 recovered González--MacManus--Pereyra, arXiv:2606.00246, *Further evidence towards the Fourier Entropy-Influence conjecture* (submitted 29 May 2026). Its current abstract still states universal FEI as a conjecture. It develops a coordinate-restriction/stopping-tree sufficient framework and restricted positive classes; it explicitly says that its key branching inequality would imply full FEI **if** it held universally. It does not claim that universal inequality.

The current Li--Han paper, arXiv:2512.03117 (2 December 2025), still proves the general estimate with the coordinate-profile logarithmic correction rather than a universal constant multiple of total influence.

A bounded fresh search also recovered earlier bounded-spectral-norm FEI literature, including Shalev's 2018 extremal-class result and Chakraborty--Kulkarni--Lokam--Saurabh's Fourier-entropy bounds. I did **not** recover, in the bounded queries `quadratic phase + Fourier entropy influence + spectral/Wiener norm` and `quadratic normalized spectral norm + FEI`, the exact parameter `Lambda_2` or theorem (0.3)--(0.4). This is negative search evidence only: **publication priority is UNVERIFIED**.

## 3. Preliminaries

All entropy is base two. For Boolean `g`, let

\[
p_S=\widehat g(S)^2,
\qquad
H(g)=-\sum_Sp_S\log_2p_S,
\qquad
I(g)=\sum_i\operatorname{Inf}_i(g).
\]

For the spectral random set `Z`, write

\[
B_i(g)=H(Z_i\mid Z_{-i}).
\]

We use the exact one-step identity

\[
I(g)=\operatorname{Inf}_i(g)
+\frac{I(g^+)+I(g^-)}2,
\tag{3.1}
\]

and Han--Shearer

\[
\sum_iB_i(g)\le H(g).
\tag{3.2}
\]

Both were proved self-containedly in the preceding NM13-02 report.

### Lemma 3.1 (restriction monotonicity of Wiener norm)

For either physical restriction at coordinate `i`,

\[
\Lambda(g^\pm)\le\Lambda(g).
\tag{3.3}
\]

Indeed, for every residual Fourier label `S`,

\[
\widehat{g^\pm}(S)=\widehat g(S)\pm\widehat g(S\cup\{i\}),
\]

so the triangle inequality and summation over pairs give (3.3).

### Lemma 3.2 (direct Wiener FEI, independently rederived)

For every Boolean `g`, with `M=Lambda(g)`,

\[
\boxed{
H(g)\le C_W(M)I(g),
\qquad
C_W(M):=\max\{4,2\log_2e+4\log_2M\}.
}
\tag{3.4}
\]

#### Proof

Multiply by a global sign so that

\[
\varepsilon:=\Pr(g=-1)\le1/2.
\]

If `epsilon=0`, `g` is constant. Otherwise the nonconstant spectral mass is

\[
W=1-\widehat g(\varnothing)^2
=4\varepsilon(1-\varepsilon).
\]

Conditioning the spectral law on nonempty Fourier labels gives

\[
H(g)=h_2(W)+W H(q).
\]

Shannon entropy is at most Renyi entropy of order `1/2`, hence

\[
H(q)
\le2\log_2\frac{M}{\sqrt W}.
\]

Using `h_2(x)<=x log_2(e/x)`,

\[
H(g)
\le W\bigl(\log_2e+2\log_2M-2\log_2W\bigr).
\tag{3.5}
\]

Let `t=log_2(1/epsilon)>=1`. Since

\[
2\varepsilon\le W\le4\varepsilon,
\]

we have `-2 log_2 W <= 2t-2`. Put

\[
D=\log_2e+2\log_2M-2.
\]

If `D>=0`, then `2t+D <= (2+D)t`, so

\[
H(g)
\le4\varepsilon(\log_2e+2\log_2M)t.
\]

The cube edge-isoperimetric inequality gives

\[
I(g)\ge2\varepsilon t,
\]

hence

\[
H(g)\le(2\log_2e+4\log_2M)I(g).
\]

If `D<0`, (3.5) gives `H(g)<=8 epsilon t<=4I(g)`. This proves (3.4). QED.

### Lemma 3.3 (quadratic flat spectrum)

Let `q` be quadratic with alternating polar matrix `M_q` of rank `r`. Then the squared Fourier law of `(-1)^q` is uniform on an affine coset of `im M_q`; in particular

\[
\Lambda((-1)^q)=2^{r/2}.
\tag{3.6}
\]

This is the flat-spectrum statement underlying the earlier exact quadratic rank telescope. One direct proof observes that the autocorrelation

\[
\mathbb E_x(-1)^{q(x)+q(x+h)}
\]

vanishes unless `M_q h=0` and otherwise has modulus one. Fourier inversion then forces squared spectral mass to be uniform on one affine coset of the `r`-dimensional image.

### Lemma 3.4 (full-rank principal alternating minor)

If an alternating matrix over `F_2` has rank `r`, there is a coordinate set `J` of size `r` such that the principal submatrix `M[J,J]` is nonsingular.

A short induction uses a nonzero pivot pair `M_ij=1`. Taking the Schur complement of that principal `2 x 2` alternating block produces another alternating matrix and drops rank by exactly two. A nonsingular principal minor of the Schur complement lifts, together with `{i,j}`, to a nonsingular principal minor of the original matrix. QED.

## 4. Quadratic-normalized direct FEI

### Theorem 4.1

For every Boolean `f`,

\[
\boxed{H(f)\le C_{\rm QW}(\Lambda_2(f))I(f)}
\tag{4.1}
\]

with `C_QW` from (0.2).

### Proof

Choose a quadratic `q` attaining the finite minimum in (0.1), and write

\[
u=(-1)^qf,
\qquad
L=\Lambda(u)=\Lambda_2(f),
\qquad
\ell=\log_2L.
\]

Let `r` be the polar rank of `q`.

By Fourier convolution, `l1` is submultiplicative. Lemma 3.3 therefore gives

\[
\Lambda(f)
=\Lambda((-1)^q u)
\le2^{r/2}L.
\tag{4.2}
\]

Since Shannon entropy is at most Renyi entropy of order `1/2`,

\[
H(f)\le2\log_2\Lambda(f)
\le r+2\ell.
\tag{4.3}
\]

We split according to whether the quadratic rank dominates the residual Wiener complexity.

### Case A: `r >= 4 ell`

If `r=0`, then `ell=0` and (4.2) gives `Lambda(f)=1`, hence `H(f)=0`; there is nothing to prove. Assume `r>0`.

Choose `J`, `|J|=r`, with `M_q[J,J]` nonsingular by Lemma 3.4. Restrict all coordinates outside `J` arbitrarily. On every resulting branch `y`,

\[
f_y=(-1)^{q_y}u_y,
\]

where `q_y` is a full-rank quadratic on `r` variables and, by Lemma 3.1,

\[
\Lambda(u_y)\le L.
\]

Full-rank quadratic phases are bent: every Fourier coefficient of `(-1)^{q_y}` has modulus `2^{-r/2}`. Therefore convolution gives, for every Fourier label `S`,

\[
|\widehat{f_y}(S)|
\le2^{-r/2}\Lambda(u_y)
\le2^{-r/2}L.
\]

Thus every spectral probability is at most `L^2 2^{-r}`, and min-entropy yields

\[
H(f_y)\ge r-2\ell\ge r/2.
\tag{4.4}
\]

On the other hand spectral subadditivity gives

\[
H(f_y)
\le\sum_{j\in J}h_2(\alpha_j(f_y)),
\qquad
\alpha_j=\operatorname{Inf}_j.
\tag{4.5}
\]

If `I(f_y)<r/10`, concavity of `h_2` gives

\[
H(f_y)
\le r h_2(I(f_y)/r)
<r h_2(1/10)
<r/2,
\]

contradicting (4.4). The last strict inequality is exact: `h_2(1/10)<1/2` is equivalent after exponentiating to

\[
10^{10}<2^5 9^9,
\]

and

\[
2^5 9^9-10^{10}=2397455648>0.
\]

Hence every outside restriction satisfies

\[
I(f_y)\ge r/10.
\]

Averaging the `J`-coordinate influences over all outside restrictions gives

\[
I(f)\ge r/10.
\tag{4.6}
\]

Combining (4.3), `r>=4 ell`, and (4.6),

\[
H(f)
\le r+2\ell
\le\frac32r
\le15I(f).
\tag{4.7}
\]

### Case B: `r < 4 ell`

From (4.2),

\[
\Lambda(f)
<2^{2\ell}L=L^3.
\]

Apply the independently proved direct Wiener estimate (3.4):

\[
H(f)
\le\max\{4,2\log_2e+4\log_2\Lambda(f)\}I(f)
\]

and therefore

\[
H(f)
\le\max\{4,2\log_2e+12\ell\}I(f)
\le C_{\rm QW}(L)I(f).
\tag{4.8}
\]

Cases A and B prove (4.1). QED.

## 5. Hereditary allocation after quadratic normalization

### Lemma 5.1

For every physical restriction `f^b` of `f`,

\[
\boxed{\Lambda_2(f^b)\le\Lambda_2(f).}
\tag{5.1}
\]

### Proof

Take a minimizing representation `f=(-1)^q u` with `Lambda(u)=Lambda_2(f)`. Restricting coordinate `i=b` gives

\[
f^b=(-1)^{q^b}u^b,
\]

where `q^b` is still quadratic. Lemma 3.1 gives `Lambda(u^b)<=Lambda(u)`, so the minimum defining `Lambda_2(f^b)` is no larger. QED.

### Theorem 5.2 (quadratic-normalized hereditary allocation)

For every Boolean `f`, there exists a full adaptive physical restriction tree `T` with

\[
\boxed{
R_T(f)
\le C_{\rm QW}(\Lambda_2(f))I(f).
}
\tag{5.2}
\]

### Proof

Set `L=Lambda_2(f)` and `C=C_QW(L)`. By Lemma 5.1 every physical restriction `g` of `f` has `Lambda_2(g)<=L`. Since `C_QW` is nondecreasing, Theorem 4.1 gives

\[
H(g)\le C I(g).
\]

Han--Shearer (3.2) then implies that every nonconstant restriction has some coordinate `i` with

\[
B_i(g)\le C\operatorname{Inf}_i(g).
\]

Query such an `i`, recurse on both children, and use the exact influence identity (3.1):

\[
R_T(g)
\le C\operatorname{Inf}_i(g)
+\frac C2\bigl(I(g^+)+I(g^-)\bigr)
=CI(g).
\]

Induction on dimension closes the full tree. QED.

This is the sought **paid dependent-branch normalization**: the extracted quadratic may change differently on the two branches, but the branchwise control parameter `Lambda_2` never increases and no rank payment is accumulated level by level.

## 6. Application to P03's exact newest obstruction

P03's newest report proves a raw-Wiener hereditary theorem and arbitrary bounded affine-flat arrangements for affine-character twists, then isolates the missing step: combine that residual control with a quadratic certificate without paying the raw Wiener growth `2^{r/2}` or the quadratic rank `r` twice.

Theorem 5.2 supplies exactly such a bridge.

Let

\[
f=(-1)^q\chi\prod_{a=1}^m\sigma_{A_a},
\qquad
\sigma_A=1-2\,1_A,
\]

where `q` is arbitrary quadratic, `chi` is an affine character, and the `A_a` are arbitrary affine flats.

For one affine flat,

\[
\Lambda(\sigma_A)\le3,
\]

and Wiener norm is submultiplicative under products. Since affine characters have Wiener norm one,

\[
\Lambda_2(f)
\le\Lambda\left(\chi\prod_{a=1}^m\sigma_{A_a}\right)
\le3^m.
\tag{6.1}
\]

Therefore both the direct entropy bound and the hereditary allocation satisfy

\[
\boxed{
H(f)\le K_m^{(2)}I(f),
\qquad
R_T(f)\le K_m^{(2)}I(f),
}
\tag{6.2}
\]

with

\[
\boxed{
K_m^{(2)}
=\max\left\{15,\;2\log_2e+12m\log_23\right\}.
}
\tag{6.3}
\]

This extends P03's arbitrary bounded-`m` affine-flat arrangement theorem from affine-character twists to **arbitrary quadratic twists**, uniformly in the quadratic polar rank.

For `m=1` and `m=2`, the existing specialized one-flat and two-flat theorems have better constants and remain the preferred results. The point of (6.2) is not constant optimization: it is the general paid normalization mechanism and its extension to every fixed `m`.

Numerically,

\[
C_{\rm QW}(3)=21.9049400904318\ldots,
\]

\[
C_{\rm QW}(9)=40.92449009908567\ldots.
\]

### Cancellation-sensitive application

P03's explicit obstruction example partitions one codimension-two flat into arbitrarily many parallel higher-codimension flats. Component count can then be huge while the product of all flat signs collapses exactly to one flat sign.

The parameter `Lambda_2` automatically sees that recombination **after** quadratic normalization. If the residual product simplifies to one flat sign, then `Lambda_2(f)<=3` regardless of how many components were used before simplification and regardless of the rank of the quadratic twist. The generic theorem therefore gives the uniform constant `21.90494009...` on that recombined state. The already-known one-flat theorem is sharper, but this example demonstrates that the new normalization mechanism is not fooled by the very cancellation that invalidated P03's componentwise codimension accounting.

For a pure quadratic phase, raw Wiener norm is `2^{r/2}` while `Lambda_2=1`; thus the quotient parameter also removes the exponential raw-Wiener inflation caused solely by quadratic rank. The exact quadratic telescope remains far sharper (`1` instead of `15`), but the new theorem pays no rank-dependent constant.

## 7. What this does and does not solve

**Demonstrated gain.** The precise newest P03 obstruction was a cancellation-aware paid extraction of the quadratic part. Theorems 4.1 and 5.2 provide one: `Lambda_2` is defined after optimal quadratic extraction, is monotone on both dependent branches, and yields a logarithmic-in-residual-norm direct and hereditary FEI certificate.

**Why full FEI remains open.** This run does not prove a universal bound on `Lambda_2(f)`. The constant in (0.3)--(0.4) still depends on `log Lambda_2(f)`. Hence the unrestricted source-level quantity stays UNKNOWN.

**Remaining obstruction.** Either:

1. find a further quotient/control parameter that is universally bounded or universally payable by influence while dominating `log Lambda_2`, or
2. combine `Lambda_2` with the exact quadratic/symmetric/decision-tree leaf certificates through a second amortized potential so that branches with large normalized Wiener norm terminate cheaply for a different reason.

This is narrower than P03's preceding obstruction because raw quadratic rank has now been separated from residual Wiener complexity without losing hereditary monotonicity.

Publication priority for the exact theorem is UNVERIFIED pending a broader literature search and later independent review.

## 8. Sanity checks actually executed

New checker:

`proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T10-08-55+0300__check_quadratic_normalized_wiener.py`

created at commit `0b7dd14ec6036a2aecd64c1f6556b23ff7435e25`.

Archived executed output:

`proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T10-08-55+0300__check_quadratic_normalized_wiener.out`

created at commit `a9814610a5593c2ab63802756e787920d55ab3ad`.

The checker:

- exhaustively evaluates all **276 Boolean functions in dimensions 1, 2, 3**;
- computes `Lambda_2` by exact enumeration of all affine/quadratic phase twists in those dimensions;
- checks `H<=C_QW(Lambda_2) I` and physical-restriction monotonicity of `Lambda_2`;
- tests **120 deterministic-seed random dimension-four Boolean functions**, each against all `1024` quadratic/affine twists;
- checks the exact integer witness for `h_2(1/10)<1/2`.

Recorded output: `PASS`.

Key values:

- exhaustive minimum theorem slack: `0.0`;
- exhaustive minimum `Lambda_2` restriction-monotonicity slack: `0.0`;
- random dimension-four minimum theorem slack: `17.549887939539722`;
- random minimum monotonicity slack: `0.0`.

These computations are self-checks only. The theorem is all-dimensional and rests on the arguments above.

## 9. Metrics

- parent FEI status: `OPEN -> OPEN`;
- universal finite source constant: `UNKNOWN -> UNKNOWN`;
- newly controlled parameter: `Lambda_2(f)=min_{deg q<=2} Lambda((-1)^q f)`;
- hereditary branch behavior of `Lambda_2`: `not previously available -> monotone nonincreasing`;
- arbitrary quadratic twists of bounded-`m` affine-flat arrangements: `specialized m<=2 / affine-character arbitrary-m -> arbitrary quadratic twist for every fixed m`;
- fresh controls used: `no`;
- independent audit: `pending`;
- publication priority: `UNVERIFIED`.

## ledger_delta

```yaml
ledger_delta:
  owner: NM13-02
  parent: T01_Friedgut_Kalai_FEI
  source_status_before: OPEN
  source_status_after: OPEN
  universal_constant_before: UNKNOWN
  universal_constant_after: UNKNOWN
  mechanism_gain:
    parameter: "Lambda_2(f)=min_{deg q<=2} ||hat{((-1)^q f)}||_1"
    theorem: "H(fhat^2)<=C_QW(Lambda_2(f)) I(f), C_QW(L)=max(15,2 log2 e+12 log2 L)"
    hereditary: "Lambda_2 is nonincreasing under physical restrictions and some full tree has R_T<=C_QW(Lambda_2(f)) I(f)"
  application:
    target: "P03 newest paid quadratic/nonquadratic normalization obstruction"
    result: "arbitrary quadratic twists of products of m affine-flat signs have direct and hereditary constant max(15,2 log2 e+12 m log2 3), independent of quadratic rank"
    cancellation_test: "parallel-flat recombination is detected by actual post-normalization Wiener norm rather than component count"
  preserved_stronger_special_cases:
    - quadratic_rank_telescope_constant_1
    - P03_one_flat_specialized_constant
    - P03_two_flat_specialized_constant
    - NM13-02_two_flat_constant_24_history
  preserved_failures:
    - pointwise_erasure_shortcut
    - all_fixed_coefficient_affine_drift
    - Han_absolute_overlap_selector
    - derivative_degree_scalar_schedule
    - blind_curvature_query_ratio
    - resolvent_interpolation
  peer_coordination:
    companion: P03
    latest_peer_obstruction: "paid quadratic/nonquadratic normalization with cancellation-sensitive residual complexity"
    overlap_policy: "P03 raw-Wiener claims untouched; NM13-02 proves a quadratic-quotiented normalization theorem"
  checker: PASS
  independent_audit: PENDING
  publication_priority: UNVERIFIED
  next_obstruction: "universally payable control of log Lambda_2, or a second stopping potential that terminates large-Lambda_2 branches on other certified classes"
```

**End of complete substantive run report.**
