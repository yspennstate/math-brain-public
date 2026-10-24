TASK: B13 ACCOUNT: account02 RUN: 2026-09-21T21:58:26.485052Z — sharp cross-plaquette direct-product correction and source-frontier child clustering

MODEL: GPT-5.6 Sol (self-report)  
REQUESTED EFFORT: maximum actually supported  
CONFIGURED / KNOWN REASONING LEVEL: UNKNOWN / NOT_EXPOSED  
PROVIDER REASONING USAGE: null / NOT_EXPOSED  
EXECUTION: WITHOUT_VERIFIED_BRAIN

# Status

**Full uniform-cube Friedgut--Kalai Fourier entropy--influence remains OPEN / NOT PROVED.**

This run changes mechanism again.  The previous B13 block-Holevo theorem used the cross-block sensitivity-support bank only as an upper bound for quantum/restriction mixture information.  Here the same genuinely Boolean bank is turned into a **constructive signed direct-product test**: every physical block cut admits an actual product of two Boolean sign functions such that the residual Boolean correction has dimension-free conditional Shannon entropy at most one half of the cross-support bank.  Both the entropy constant `1/2` and the Hamming constant `1/4` are sharp on the two-bit one-point defect.

This is a quantitative, jointly realizable strengthening of the previous exact statement `P=0 iff tensor factorization`.  It is not a Fourier-entropy continuity theorem and therefore does not close FEI.

# 1. Fresh source state and completed other-account result actually used

Scientific master was refreshed before the derivation.  The named completed other-account input used here is

`proofnet24/P03-fei/fleet-2026-09-21/account03/B13/20260921T2136Z-global-defect-contraction/REPORT.md`,

report blob `c62febb5aa2ed1720edfc0b90a72d479e80f3674`.

That report combines account02/B12 physical support stability with account04/B13 source-frontier elimination and proves that, in the median-character gauge, with

\[
 j_i=\operatorname{Inf}_i(f)\le\tfrac12,\qquad
 d_i=\sum_{k\ne i}\|D_kD_if\|_2^2,
\]
\[
 \Delta_i=\frac{d_i}{j_i}-\frac12\log_2\frac1{j_i},
 \qquad
 \mathcal D(f)=\sum_i j_i\Delta_i,
\]
there is one actual physical source-frontier block `A_*` such that

\[
 \mathbb E_a J(f_{A_*=a})
 \le \left(1+\frac1{\eta_0}\right)\mathcal D(f)
 \tag{1.1}
\]

for an absolute stability threshold `eta_0>0`.  Its explicit remaining gap is the Shannon cost of the reveal block.  Section 6 below applies the new theorem to **that same block**, producing one actual anchor child and a dimension-free conditional sign-code for all the other children.  Thus the peer theorem is used as a source object, not merely cited.

I also retain the mixed-curvature conservation used by that peer chain:

\[
 \kappa_{ik}=p_{ik}+4o_{ik},\qquad
 \sum_{i\ne k}\kappa_{ik}=4d_k.
 \tag{1.2}
\]

No claim below replaces the signed `o_ik` term when signed curvature itself is the target.

# 2. Required comparison with the last THREE substantive own reports

The last three completed substantive account02/B13 reports are:

1. `20260921T211122Z-block-holevo-support-boundary`: for every cut `A|B`, proved `JS_A` and spectral block mutual information are at most the bipartite Boolean phase entropy, which is at most the oriented support-boundary bank; also proved `P=0` iff exact multiplicative tensor factorization.  It left `H(S_A|S_B)` and nonreusing adaptive payment open.
2. `20260921T195704Z-tensor-amortized-incidence`: proved that the global harmonic layer-incidence payment is already full-FEI-strength under Boolean tensor powers, forcing the harmonic route to primitive critical cores.
3. `20260921T192906Z-harmonic-layer-incidence`: refuted row-local Palm mean closure with genuine odd majority, paid all row-cardinality entropy, and isolated the within-layer incidence residual.

## FULL-PROBLEM CHANGE

**Before:** for a physical cut, `P_{A->B}` was known to pay the restriction-mixture information `JS_A` and to vanish exactly on product cuts, but there was no quantitative theorem saying what a small positive `P` forces the **signed Boolean truth table itself** to look like.

**After:** a sharp universal direct-product correction theorem is proved.  Small `P` forces an explicit signed factorization

\[
 f(a,b)=g(a)h(b)c(a,b)
\]

whose Boolean correction has conditional physical Shannon entropy at most `P/2` and Hamming mass at most `P/4`.  Applied in the opposite orientation, all physical restriction children are clustered around one **actual anchor child** with the same sharp budget.  Combining (1.2) gives an explicit derivative-depth payment.

**Full-bound status:** NO FULL-BOUND MOVEMENT.  The theorem pays a new signed physical interaction residual but does not yet convert that physical correction code into the Fourier conditional entropy `H(S_A|S_B)`.  FEI remains open.

## MECHANISM CHANGE

**Before:** bipartite phase states plus Holevo/Han information and edge isoperimetry.

**After:** a classical signed **direct-product test** built from A-edge ratio rows, independent anchor pairs, Poincare on the opposite block, and edge isoperimetry only after forming the actual child-to-anchor ratio.  This is neither the harmonic/Palm mechanism nor another sign-free profile.

Creative moves: `#1 change the category` (cross-support bank to direct-product testing), `#19 make it an algorithm` (choose an actual anchor block value and majority branch signs), and `#25 count the same thing twice` (cross plaquette syndrome as both ratio-row variation and expected child-ratio boundary).

# 3. Setup: the same physical cross-support bank

Let

\[
 f:\mathbb F_2^A\times\mathbb F_2^B\to\{-1,+1\}
\]

and assume both blocks are nonempty.  For an `A`-edge `e=(a,a+e_i)`, `i in A`, define its signed ratio row on the `B` cube by

\[
 u_e(b)=f(a,b)f(a+e_i,b)\in\{-1,+1\}.
 \tag{3.1}
\]

The support indicator of the `i`-derivative is `(1-u_e)/2`.  Hence its `k`-boundary probability is exactly

\[
 \Pr_b[u_e(b)\ne u_e(b+e_k)].
\]

Averaging over the quotient `A`-edge basepoint and summing across the cut recovers the bank from the preceding B13 report:

\[
 P_{A\to B}(f)
 =\sum_{i\in A}\sum_{k\in B}
   \mathbb E_{a_{-i}}
   \Pr_b[u_{i,a_{-i}}(b)\ne u_{i,a_{-i}}(b+e_k)].
 \tag{3.2}
\]

This is a property of one actual Boolean function; no independent row law or non-Boolean square distribution is introduced.

# 4. PROVED: sharp cross-plaquette tensor-correction theorem

### Theorem B13-CROSS-PLAQUETTE-TENSOR-CORRECTION

For every Boolean `f` and every nontrivial cut `A|B`, there exist Boolean functions

\[
 g:\mathbb F_2^A\to\{-1,+1\},\qquad
 h:\mathbb F_2^B\to\{-1,+1\}
\]

and a Boolean correction

\[
 c(a,b)=f(a,b)g(a)h(b)
\]

such that, writing

\[
 q_b=\Pr_a[c(a,b)=-1],
\]

we have `0<=q_b<=1/2` for every `b` and

\[
 \boxed{
 \mathbb E_b\left[2q_b\log_2\frac1{q_b}\right]
 \le \frac12 P_{A\to B}(f).
 }
 \tag{4.1}
\]

With the convention `0 log(1/0)=0`, this implies

\[
 \boxed{
 H(c(X_A,X_B)\mid X_B)
 =\mathbb E_b h_2(q_b)
 \le\frac12P_{A\to B}(f),
 }
 \tag{4.2}
\]

and

\[
 \boxed{
 \Pr[c(X_A,X_B)=-1]
 =\mathbb E_b q_b
 \le\frac14P_{A\to B}(f).
 }
 \tag{4.3}
\]

The factors can be chosen constructively with `g(a)=f(a,b_0)` for one **actual physical anchor** `b_0`; `h(b)` is then the majority sign of the ratio `f(a,b)f(a,b_0)` over uniform `a`.

### Proof

For two independent uniform points `b,b'` of the `B` cube, define the child-ratio function on the `A` cube

\[
 R_{b,b'}(a)=f(a,b)f(a,b').
 \tag{4.4}
\]

Fix an `A` edge `e`.  Its edge ratio in `R_{b,b'}` changes precisely when

\[
 u_e(b)\ne u_e(b').
\]

If `m_e=E_b u_e(b)`, then

\[
 \Pr_{b,b'}[u_e(b)\ne u_e(b')]
 =\frac{1-m_e^2}{2}
 =\frac12\operatorname{Var}(u_e).
 \tag{4.5}
\]

The cube Poincare inequality, in the same influence normalization as (3.2), gives

\[
 \operatorname{Var}(u_e)
 \le\sum_{k\in B}\Pr_b[u_e(b)\ne u_e(b+e_k)].
 \tag{4.6}
\]

Average (4.5)--(4.6) over all `A` edges.  By definition (3.2),

\[
 \boxed{
 \mathbb E_{b,b'} I_A(R_{b,b'})
 \le\frac12P_{A\to B}(f).
 }
 \tag{4.7}
\]

For a fixed pair `(b,b')`, let

\[
 q(b,b')=\min\{\Pr_a[R_{b,b'}(a)=1],\Pr_a[R_{b,b'}(a)=-1]\}.
\]

The minority set of `R_{b,b'}` is a genuine subset of the `A` cube.  Edge isoperimetry therefore gives

\[
 I_A(R_{b,b'})
 \ge2q(b,b')\log_2\frac1{q(b,b')}.
 \tag{4.8}
\]

Combine (4.7)--(4.8) and average.  There exists one anchor `b_0` such that

\[
 \mathbb E_b\left[2q(b,b_0)\log_2\frac1{q(b,b_0)}\right]
 \le\frac12P_{A\to B}(f).
 \tag{4.9}
\]

Set `g(a)=f(a,b_0)`.  For each `b`, choose `h(b)` to be the majority sign of `f(a,b)g(a)`.  Then the correction `c=fgh` has minority fraction exactly `q_b=q(b,b_0)`, proving (4.1).

For `0<=q<=1/2`,

\[
 h_2(q)\le2q\log_2(1/q),
 \qquad
 2q\le2q\log_2(1/q).
\]

Equations (4.2)--(4.3) follow.  QED.

# 5. Sharpness and relation to exact tensor primitivity

Take the two-bit one-point defect, with one negative truth-table value and three positive values, and the singleton cut.  Directly,

\[
 P_{A\to B}=1.
\]

For the optimal anchor, one `B`-fiber has `q=0` and the other has `q=1/2`.  Hence

\[
 \mathbb E_b 2q_b\log_2(1/q_b)=\frac12,
\]
\[
 H(c\mid B)=\frac12,
\qquad
 \Pr(c=-1)=\frac14.
\]

Thus the constants in (4.1)--(4.3) are simultaneously sharp.

At the other endpoint, if `P_{A->B}=0`, (4.3) forces `c=1` identically, recovering

\[
 f(a,b)=g(a)h(b).
\]

So the theorem quantitatively upgrades the preceding B13 exact primitivity criterion rather than introducing a different notion of product structure.

# 6. Child-clustering form and the account03/B13 source-frontier block

Swap the roles of `A` and `B` in Theorem 4.1.  For a physical restriction of the block `A`, there exists one **actual anchor branch** `a_0` and signs `sigma_a` such that, with

\[
 \epsilon_a
 =\Pr_b[f(a,b)\ne\sigma_a f(a_0,b)]\le\frac12,
 \tag{6.1}
\]

we have

\[
 \boxed{
 \mathbb E_a\left[2\epsilon_a\log_2\frac1{\epsilon_a}\right]
 \le\frac12P_{B\to A}(f),
 }
 \tag{6.2}
\]
\[
 \boxed{
 \mathbb E_a h_2(\epsilon_a)
 \le\frac12P_{B\to A}(f),
 \qquad
 \mathbb E_a\epsilon_a\le\frac14P_{B\to A}(f).
 }
 \tag{6.3}
\]

This is a dimension-free **physical Shannon clustering theorem for the actual restriction family**: after one reveal, every child is compared to one genuine child, not to an abstract proxy distribution.

Now use the mixed-curvature conservation (1.2).  Since `p_{ki}<=kappa_{ki}`,

\[
 P_{B\to A}
 \le\sum_{i\in A}\sum_{k\ne i}\kappa_{ki}
 =4\sum_{i\in A}d_i.
 \tag{6.4}
\]

Therefore

\[
 \boxed{
 \mathbb E_a h_2(\epsilon_a)
 \le2\sum_{i\in A}d_i.
 }
 \tag{6.5}
\]

Writing the row defects explicitly,

\[
 2d_i=j_i\log_2\frac1{j_i}+2j_i\Delta_i,
\]
so (6.5) is equivalently

\[
 \boxed{
 \mathbb E_a h_2(\epsilon_a)
 \le
 \sum_{i\in A}j_i\log_2\frac1{j_i}
 +2\mathcal D_A,
 \qquad
 \mathcal D_A:=\sum_{i\in A}j_i\Delta_i.
 }
 \tag{6.6}
\]

Apply this to the **same source-frontier block `A_*`** supplied by account03/B13.  We now have simultaneously

\[
 \mathbb E_aJ(f_{A_*=a})
 \le\left(1+\frac1{\eta_0}\right)\mathcal D(f),
 \tag{6.7}
\]

and one actual anchor child `f_{a_0}` for which

\[
 \mathbb E_a h_2\!\left(
   \Pr_b[f_{A_*=a}(b)\ne\sigma_a f_{A_*=a_0}(b)]
 \right)
 \le
 \sum_{i\in A_*}j_i\log_2\frac1{j_i}+2\mathcal D_{A_*}.
 \tag{6.8}
\]

This is the concrete use of the peer result.  The first line pays the **post-restriction centered influence** by the positive row-defect bank.  The second line pays the **signed inter-child physical interaction code** by the revealed rows' exact base depth plus their positive defects.  There is no ambient-dimension continuity factor and no repeated use of a row.

It also pinpoints the incompatibility with the tempting stronger conclusion `Shannon reveal cost = O(mathcal D)`: even a zero-defect exact-subcube row carries the base selector term `j_i log_2(1/j_i)`.  Account03/B13's theorem correctly never claimed that `mathcal D` alone pays this term.  Any closure must amortize the base selector term through the joint Boolean source geometry/crossing credits, not discard it.

# 7. Transfer and limits

The theorem is invariant under the median-character recentering used by the joint programme.  A character splits across `A|B` into an `A` character times a `B` character, so it only changes the factors `g,h`; the correction minority fractions and the cross support-boundary probabilities are unchanged.  Spectral entropy is preserved by the character shift, and the centered parent has `I=J`.  Thus no affine or gauge cost is hidden in (6.7)--(6.8).

What is **not** proved is equally important.  A low physical correction entropy does not by itself imply a dimension-free bound on the Fourier entropy change between `f_a` and the anchor child.  Using Fannes continuity would reintroduce an ambient-dimension factor and is explicitly not allowed as closure.  The still-unpaid universal arrow is therefore a **Boolean convolution/erasure transfer for an actual anchor-child correction**, or an adaptive crossing argument that spends the base selector term in (6.8) once.

The killed global phase/rank/l1 template and sign-free parity-profile relaxations are not reopened.  No lattice integrality is assumed.  No tensor product is used as positive evidence; rather, `P=0` is exactly the product endpoint of the theorem.

# 8. Executed finite falsification / regression search

`check_cross_plaquette_tensor_correction.py` was executed with the Python standard library.  It exhaustively enumerated every Boolean function modulo global output sign through dimension four and every **directed** nontrivial block cut:

- `n=2`: 8 functions, 16 directed cuts;
- `n=3`: 128 functions, 768 directed cuts;
- `n=4`: 32,768 functions, 458,752 directed cuts;
- total: **32,904 functions and 459,536 directed cut cases**.

For every case it formed `P_{A->B}`, searched all physical anchors in `B`, and checked the three conclusions (4.1)--(4.3).  Recorded maximum excess for the logarithmic correction cost, conditional entropy, and Hamming distance was `0.000e+00`; there were zero `P=0` factorization failures.  There were 7,880 finite equality cases, including the explicit two-bit one-point defect with

`P=1`, `Phi=1/2`, `Hcorr=1/2`, `distance=1/4`.

Result: **PASS**.  The checker is a self-check of the algebra and constants; the theorem above is analytic.

Checker source SHA-256: `159b6c34ffb42f5116fa536532c12fb79b67208866295c63f320fe8ff8cc747d`.  
Archived stdout SHA-256: `fdd3aec6db5a260faa494ec9a4cef8f79b128778f0c34fd594b6efa90ddc3902`.

# 9. Next exact target

The next nonduplicative A/B target is now narrower than "pay the reveal block": use the source-frontier DAG and crossing refunds to spend

\[
 \sum_{i\in A_*} j_i\log_2(1/j_i)
\]

**once**, while using the new anchor-child correction code for the genuinely nonproduct remainder.  A successful step must convert this physical signed code to the restriction Fourier entropy without a `dimension * error` term.  The mandatory stress tests are the exact zero-defect one-point family, near-products with a sparse interaction correction, and the current positive-defect L-shape obstruction.  Until that conversion is proved, full FEI remains OPEN.
