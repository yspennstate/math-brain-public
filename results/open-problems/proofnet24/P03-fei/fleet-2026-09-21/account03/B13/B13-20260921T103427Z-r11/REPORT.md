# B13 FEI Booleanity profile — circulant orthostochastic recoding and a Sidon-layer obstruction

**Status:** PARTIAL. Full uniform-cube FEI remains **OPEN / NOT PROVED**.  
**Brain label:** **WITHOUT_VERIFIED_BRAIN**. No authentic mathematical/cognitive brain package was present in this runtime, so no brain retrieval is claimed.  
**Routes:** APPROACHES 2, 13, 14, with a new coding/orthogonality subroute.  
**No novelty claim:** the arguments below are recorded as new-to-this-run/repository targets unless already identified as inherited; publication priority has not been established. A brief current-literature check still found FEI described as a conjecture in the 2026 note *Further evidence towards the Fourier Entropy-Influence conjecture* (arXiv:2606.00246).

## 1. Exact universal statement attempted

For a Boolean function `f:{-1,1}^n->{-1,1}`, let

\[
\mu(A)=\widehat f(A)^2,\qquad q_i=\Pr_{S\sim\mu}(i\in S)=\operatorname{Inf}_i(f),
\]

and for two independent spectral samples `S,S'` define

\[
D(f):=\sum_i q_i(1-q_i)=\frac12\,\mathbb E|S\triangle S'|.
\]

The stronger universal statement attacked in this run is

\[
\tag{PD_beta}
H(f)\le \beta(1/2)\,D(f),\qquad \beta(1/2)\simeq 6.4547837.
\]

`PD_beta` is **OPEN**. It would imply FEI immediately because `D(f)<=I(f)`. The point of the attempt is that `D` is parity-shift invariant and is exactly half the mean pairwise Hamming dispersion of the spectral point process, making coding/point-process tools natural.

The already-established repository normalization
\[
J(f)=\sum_i\min(q_i,1-q_i)
\]
is not new here: multiplication by a character translates the Fourier law and shows the optimal FEI constant is equivalently the optimal constant in `H<=C J`. Writing `r_i=min(q_i,1-q_i)<=1/2`,
\[
D=\sum_i r_i(1-r_i),\qquad \frac12J\le D\le J.
\]
Thus a finite universal `H/D` bound is equivalent to FEI up to a factor two, while `PD_beta` is a genuinely stronger sharp-constant candidate.

## 2. Decisive dead route: block-correlation range constraints alone cannot encode Booleanity

APPROACHES route 2 records
\[
R(T):=\Pr(S\cap T=\varnothing)
\]
as the block-rerandomization correlation profile. For **every** probability law on random subsets, Boolean or not, `R(T)` is automatically in `[0,1]`. For the dangerous independent product law with marginals `p_i`,
\[
R(T)=\prod_{i\in T}(1-p_i),
\]
which also stays in `[0,1]` for every block. Therefore the proposed route-13 first test “find a block whose implied correlation leaves `[-1,1]`” cannot work for a product spectral law. More generally, elementary avoidance-profile inequalities such as monotonicity and the usual supermodularity are generic random-set facts; by themselves they do not see Booleanity.

**REFUTED subroute:** range-only / generic random-set inequalities on `T -> Pr(S avoids T)` are insufficient to distinguish Fourier-squared laws of Boolean functions from arbitrary subset laws. The missing datum is the Fourier **phase/sign compatibility**.

## 3. Exact phase characterization: Boolean spectral laws are circulant orthostochastic

Put `G=F_2^n` and write `a_A=hat f(A)`. Since `f^2=1`, Fourier convolution gives, for every `T in G`,
\[
\sum_A a_Aa_{A+T}=\mathbf 1_{T=0}. \tag{1}
\]
Conversely, if a real vector `a` of norm one satisfies (1), its inverse Walsh transform `f` obeys `f^2=1`, hence is Boolean.

Equivalently define the circulant matrix
\[
U_{R,C}=a_{R+C}.
\]
Equation (1) says exactly that `U` is orthogonal. Its entrywise square is
\[
P_{R,C}=U_{R,C}^2=\mu(R+C).
\]
So a probability law `mu` is a Boolean spectral law iff there are signs on `sqrt(mu)` that make this circulant matrix orthogonal. Structural hash/support data alone are not enough; the signed off-origin autocorrelations all have to cancel simultaneously.

This recodes the FEI target as an entropy-versus-Hamming-radius problem for a special class of **circulant orthostochastic** probability kernels. No claim is made that this terminology or characterization is new in the literature; the proof above is elementary and exact.

## 4. New proved lemma: Sidon projection forces orthogonal layer vectors

This is the concrete coding-theoretic step obtained in this run.

Split the Fourier coordinates as `G=F_2^m x F_2^k`. For `b in F_2^m` define the layer vector
\[
v_b=(a_{b,\ell})_{\ell\in F_2^k}\in\mathbb R^{2^k},
\]
and let
\[
B=\{b:v_b\ne0\}
\]
be the support projected to the first `m` coordinates.

Call `B` **Sidon (in characteristic two)** when every nonzero `t` has at most one unordered representation `t=b+b'` by distinct `b,b' in B`.

### Lemma (PROVED)
If `f` is Boolean and the projected Fourier support `B` is Sidon, then the nonzero vectors `{v_b:b in B}` are pairwise orthogonal. Consequently
\[
|B|\le2^k,\qquad H(B)\le k,
\]
and the full spectral entropy obeys
\[
\boxed{H(S)\le2k.}\tag{2}
\]

### Proof
Take distinct `b,b' in B` and put `t=b+b'`. Apply the Booleanity autocorrelation (1) to the shift `(t,0)`:
\[
0=\sum_{c,\ell}a_{c,\ell}a_{c+t,\ell}.
\]
Because `B` is Sidon, the only projected support pair separated by `t` is the unordered pair `{b,b'}`. The ordered terms therefore give
\[
0=2\sum_\ell a_{b,\ell}a_{b',\ell}=2\langle v_b,v_{b'}\rangle.
\]
Thus all nonzero `v_b` are mutually orthogonal in a space of dimension `2^k`, proving `|B|<=2^k` and `H(B)<=log_2|B|<=k`. Finally
\[
H(S)=H(B)+H(S_{\rm layer}\mid B)\le k+k=2k.
\]
This proves (2). ∎

### Influence-paid corollary (structured class only)
After the standard parity centering, suppose the `k` layer coordinates all have centered influence at least `tau>0`, and the projection onto the other coordinates is Sidon. Then `J>=k tau`, so
\[
H(f)\le2k\le\frac{2}{\tau}J(f)\le\frac{2}{\tau}I(f).
\]
This is a genuine FEI bound for the stated structured class, **not** a proof of full FEI.

## 5. Why simple support multiplicity is still too weak: the doubled-star obstruction

For `m>=2`, let
\[
B_m=\{0,e_1,\ldots,e_m\}\subset F_2^m,
\qquad A_m=B_m\times F_2.
\]
`B_m` is Sidon. The uniform law on `A_m` is a generic point-process counterexample to an entropy/mean-radius inequality:
\[
H=\log_2(2(m+1)),\qquad
J=\frac12+\frac{m}{m+1},
\]
so `H/J -> infinity`.

Doubling the star by one layer repairs the most obvious “unique difference” defect: every occurring horizontal difference is represented in both layers. Nevertheless it **still cannot be a Boolean spectral support**. The Sidon-layer lemma with `k=1` would require `|B_m|<=2`, while `|B_m|=m+1>=3`.

Equivalently, if one writes the two layer coefficients at a base point `b` as `(u_b,w_b)`, the horizontal autocorrelation for each pair `b!=b'` forces
\[
u_bu_{b'}+w_bw_{b'}=0,
\]
so the nonzero two-vectors would have to be pairwise orthogonal; three such vectors cannot exist in `R^2`.

This matters because it shows the next useful Booleanity constraint is not merely “every difference has at least two representations.” The **global compatibility of all cancellations** is the coding obstruction.

## 6. Executed counterexample search for `PD_beta`

Reproducer: `pair_dispersion_search.py` (Git blob `61021236fdc4c17caaf70fba0d2b0d21b80a3996`). Results: `pair_dispersion_results.json`.

The finite search did **not** refute `PD_beta`:

| family | tested scope | largest `H/D` |
|---|---:|---:|
| all Boolean functions, quotienting global negation | n<=4 | 4.1435368231 |
| width-2 tribes = AND of `s` OR-pairs | s=2..40, n up to 80 | 4.8258764303 |

For the exhaustive search the maxima were `4.0` at `n=2`, `4.0` at `n=3`, and `4.1435368231` at `n=4`. The `n=4` maximizer in the script's truth-table convention is integer `14`, with
\[
H=2.8486815659,\ I=J=1,\ D=11/16,
\]
and influence vector `(1/8,1/8,3/8,3/8)`.

For width-2 tribes the largest tested value occurred at `s=40` (`n=80`):
\[
H/D=4.8258764303,
\quad H/I=4.8258440757,
\quad q_i=6.7043901\times10^{-6}.
\]
These are finite/structured checks only. They do not prove `PD_beta`, do not prove that beta is the sharp dispersion constant, and do not improve the certified read-once theorem.

The same reproducer brute-forces phase signs for the doubled-star supports. Perfect off-origin autocorrelation signs exist for the degenerate base `m=1` but not for `m=2,3,4,5`, exactly matching the analytic Sidon-layer obstruction. This is a sanity check of the proof, not its basis.

## 7. What moved, what died, and the next full-FEI attack

**PROVED in this run:** (i) the exact circulant-orthostochastic/sign-autocorrelation formulation of Boolean spectral laws; (ii) the Sidon-projection orthogonality lemma and its `H<=2k` structured consequence; (iii) range-only avoidance-profile constraints cannot distinguish Booleanity.

**REFUTED route:** trying to kill the independent product profile by finding a block correlation outside `[-1,1]`; every probability law already gives an avoidance profile in `[0,1]`. Also, “no uniquely represented difference” is too weak as a standalone substitute for the signed compatibility equations: the doubled star has the multiplicity repair while retaining unbounded generic `H/J`.

**OPEN:** `PD_beta` and full FEI.

**Next attack:** make the Sidon lemma robust and turn it into an additive-energy dichotomy. After parity centering, separate a small set of payment/anchor coordinates and view the remaining Fourier coefficients as row vectors `v_b`. If the rare-pattern projection has low difference multiplicity, the Booleanity equations should force many rows to be nearly orthogonal, and a rank/Welch-type argument should bound its entropy by the anchor dimension. If it has high additive energy, use the resulting additive structure over `F_2^m` to compress the rare patterns into a low-dimensional affine model, where the existing centroid/lattice/erasure machinery may pay the entropy. The concrete next lemma is a **weighted bounded-multiplicity extension of the Sidon orthogonality lemma**, with an entropy bound in terms of layer dimension plus the excess additive energy. That attacks the full obstruction rather than rechecking any settled FEI certificate.
