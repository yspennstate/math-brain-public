# B14 — block recombination paid by conditional spectral prediction error

**Status:** PARTIAL / PROVED structural theorem. **Full uniform-cube FEI remains OPEN / NOT PROVED.**  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.  
**Live role:** FEI erasure and selector proof.  
**Fresh mathematical source before this derivation:** `master` at `e47f7caf25d0bb7f5cc7823eedaee1660d098e6b`.

This run follows the owner's 21 September instruction to do new FEI mathematics rather than audit the existing certificate. It continues the mass-weighted erasure / existential-selector route and does not revive the refuted every-prescribed-coordinate payment.

## 1. Fresh inherited frontier and nonoverlap

The following current results were used at their exact scopes.

1. `proofnet24/P03-fei/scheduled-continuation/runs/2026-09-20/2026-09-20T12-05-16Z__report.md` proves the arbitrary physical-block Walsh identity and sandwich
   \[
   \Delta_A H=B_A+R_A,\qquad 0\le R_A\le B_A,
   \]
   where
   \[
   B_A=H(S_A\mid S_{A^c}),
   \]
   for the spectral sample `S`, and therefore `B_A<=Delta_A H<=2B_A`.
2. `proofnet24/P03-fei/fleet-2026-09-21/fleet02/B14/2026-09-21T095741Z-critical-descendant-selector/REPORT.md` proves the coordinate-critical descendant and its singleton erasure-heavy consequence.
3. The newer B18 block continuation, creation commit `eaf90a9e0bb46f9127717e599ebdbbf0871a82ec`, extends that maximal-ratio argument to **every physical block**: at a descendant `g` maximizing `r=H/I` among its physical restrictions,
   \[
   \Delta_AH(g)\ge r(g)I_A(g)
   \]
   for every nonempty physical block `A`; it also closes the adaptive physical-block influence lifetime telescope.
4. B17's product-spectrum continuation, creation commit `3bcd8bba7c676834e3da0d5d6f110a556f4c8b58`, shows that exact mutually independent spectral membership bits are rigid: their marginals lie in `{0,1/2,1}`. It also gives a quantitative total-correlation payment. I do not duplicate that result here.

The new point below is different: the block recombination term `R_A`, previously bounded only by `B_A`, has an independent **log-Sobolev / nearest-character payment** by a conditional spectral prediction-error functional. For singleton blocks it reduces exactly to the known overlap bound; for larger blocks it is a new all-dimensional extension in the current repository state. Publication priority is **UNVERIFIED**.

## 2. Conditional spectral prediction error

Let `f:{-1,1}^n->{-1,1}` be Boolean and let
\[
p_S=\widehat f(S)^2.
\]
Fix a nonempty physical coordinate block `A` of size `k`. For each outside label `T subseteq A^c`, define its fibre mass
\[
w_T=\sum_{R\subseteq A}p_{T\cup R}.
\]
When `w_T>0`, let
\[
\mu_T(R)=\frac{p_{T\cup R}}{w_T},\qquad R\subseteq A.
\]
Thus `mu_T` is the conditional law of the inside spectral label `S_A` given `S_{A^c}=T`.

Define the block prediction-error cost
\[
\boxed{
M_A(f)=\sum_{T\subseteq A^c}w_T
       \sum_{i\in A}
       \min\{\Pr_{\mu_T}(i\in R),\Pr_{\mu_T}(i\notin R)\}.
}
\tag{2.1}
\]

Equivalently, for each outside fibre we choose the Hamming-nearest deterministic label `t_T subseteq A`; then
\[
M_A=\sum_Tw_T\min_{t\subseteq A}\mathbb E_{R\sim\mu_T}|R\triangle t|.
\tag{2.2}
\]
So `M_A` is the optimal Bayes Hamming error for predicting all spectral membership bits in `A` from the exact outside spectral label.

Two immediate bounds are
\[
0\le M_A\le I_A:=\sum_{i\in A}\operatorname{Inf}_i(f),
\tag{2.3}
\]
and, symmetrically,
\[
M_A\le |A|-I_A.
\tag{2.4}
\]
For a singleton `A={i}`,
\[
M_{\{i\}}=\sum_{T\not\ni i}\min\{p_T,p_{T\cup\{i\}}\},
\tag{2.5}
\]
which is exactly the mass-overlap quantity in the inherited one-coordinate erasure theorem.

## 3. New theorem: block recombination is paid by `M_A`

Let
\[
c_*:=\frac{2}{\ln 2}=2.885390081777\ldots.
\]

### Theorem 3.1 — prediction-error block recombination bound

For every Boolean `f` and every physical block `A`,
\[
\boxed{
0\le R_A(f):=\Delta_AH(f)-B_A(f)
\le c_* M_A(f).
}
\tag{3.1}
\]
Consequently, combining with the inherited `R_A<=B_A`,
\[
\boxed{
\Delta_AH(f)
\le B_A(f)+\min\{B_A(f),c_*M_A(f)\}
\le B_A(f)+c_*I_A(f).
}
\tag{3.2}
\]

For `|A|=1`, (3.1) recovers the inherited sharp scalar overlap estimate
\[
R_i\le\frac2{\ln2}\sum_T\min(p_T,p_{T+i}).
\]
The new content is that the same constant survives for an arbitrary dependent block, with the correct fibrewise nearest-character cost rather than `k` times a marginal bound.

### Proof

The inherited block-Walsh decomposition may be written fibrewise as follows. On a fibre `T`, list the real parent amplitudes
\[
u_T(R)=\widehat f(T\cup R),\qquad R\subseteq A,
\]
put `x_R=u_T(R)/sqrt(w_T)`, and let `W_k` denote the normalized `2^k x 2^k` Walsh matrix. Define
\[
y=W_kx,
\qquad q(a)=y_a^2.
\]
Then `mu_T(R)=x_R^2`, both `mu_T` and `q` are probability laws, and the exact block entropy identity is
\[
R_A=\sum_Tw_T\,[k-H_2(q_T)].
\tag{3.3}
\]

It remains to prove, for every real unit vector `x` on `{0,1}^k`,
\[
\boxed{
k-H_2((W_kx)^2)
\le \frac2{\ln2}\min_{t\in\{0,1\}^k}
       \sum_R |R\triangle t|x_R^2.
}
\tag{3.4}
\]

Set
\[
g(a)=\sum_Rx_R(-1)^{a\cdot R}.
\]
With `u` the uniform law on `{0,1}^k`, `E_u g^2=1` and
\[
q(a)=2^{-k}g(a)^2.
\]
Therefore
\[
\operatorname{Ent}_u(g^2)
:=\mathbb E_u[g^2\ln g^2]
=\ln2\,[k-H_2(q)].
\tag{3.5}
\]

We use the two-point logarithmic Sobolev inequality and tensorization. For two real values `a,b`, writing `m=(a^2+b^2)/2`, homogeneity reduces the local inequality to `m=1`. Put `a^2=1+z`, `b^2=1-z`. Then
\[
\operatorname{Ent}_{1/2}(a^2,b^2)
=\frac{(1+z)\ln(1+z)+(1-z)\ln(1-z)}2.
\]
The scalar inequality already used in the erasure reduction is
\[
\frac{(1+z)\ln(1+z)+(1-z)\ln(1-z)}2
\le1-\sqrt{1-z^2}.
\tag{3.6}
\]
The right side equals
\[
\frac{(|a|-|b|)^2}{2}\le\frac{(a-b)^2}{2}.
\]
Tensorization of entropy on the product cube therefore yields
\[
\operatorname{Ent}_u(g^2)
\le2\sum_{i\in A}\mathbb E_u(D_i g)^2,
\qquad
D_i g(a)=\frac{g(a)-g(a\oplus e_i)}2.
\tag{3.7}
\]
By Walsh Parseval,
\[
\sum_i\mathbb E_u(D_i g)^2
=\sum_R |R|x_R^2.
\tag{3.8}
\]
Combining (3.5)--(3.8) gives
\[
k-H_2(q)\le\frac2{\ln2}\sum_R|R|x_R^2.
\tag{3.9}
\]

Now multiply `g(a)` by an arbitrary character `(-1)^{a\cdot t}`. Its square, hence `q` and the left side of (3.9), are unchanged, while its Walsh coefficients shift from `x_R` to `x_{R\triangle t}`. Thus (3.9) holds with the right side replaced by
\[
\frac2{\ln2}\sum_R|R\triangle t|x_R^2
\]
for every `t`. Minimizing over `t` proves (3.4). Hamming loss separates coordinatewise, so the minimum is exactly
\[
\sum_{i\in A}\min\{\Pr_{\mu_T}(i\in R),\Pr_{\mu_T}(i\notin R)\}.
\]
Multiply by `w_T`, sum the fibres in (3.3), and obtain (3.1). QED.

### Remarks on sharpness and scope

The constant `2/ln2` in the underlying two-point inequality is sharp to first order for a one-bit vector `(sqrt(1-epsilon),sqrt(epsilon))` as `epsilon->0`. This is sharpness for the unrestricted fibre inequality; no claim is made that a Boolean parent realizes every near-extremal fibre configuration simultaneously.

No independence assumption on the block, the children, or sibling restrictions is used. The block may be arbitrarily dependent. Booleanity is needed for the FEI application and the inherited restriction setup, but inequality (3.4) itself is an analytic Walsh statement for every real unit vector.

## 4. New consequence on a restriction-critical FEI core

Let `g` be the all-block restriction-critical descendant supplied by the inherited B18 theorem, and put
\[
r=\frac{H(g)}{I(g)}.
\]
For every nonempty physical block `A`,
\[
\Delta_AH(g)\ge r I_A(g).
\tag{4.1}
\]
Combining (4.1) with (3.1) gives
\[
\boxed{
B_A(g)\ge r I_A(g)-c_*M_A(g).
}
\tag{4.2}
\]
Together with the inherited `Delta_A<=2B_A`,
\[
\boxed{
B_A(g)
\ge
\max\left\{\frac r2 I_A(g),\;rI_A(g)-c_*M_A(g)\right\}
\qquad\text{for every nonempty }A.
}
\tag{4.3}
\]

Thus if `f` violates FEI at coefficient `C` and `g` is its maximal-ratio descendant, then for every nonempty proper block
\[
\boxed{
\frac{B_A(g)}{I_A(g)}
>
\max\left\{\frac C2,\;C-c_*\frac{M_A(g)}{I_A(g)}\right\}.
}
\tag{4.4}
\]

Because `M_A<=I_A`, for every `C>2c_*=4/ln2`, the second branch is uniformly stronger than `C/2`. At the Hod calibration `C=6.4547837...`, every proper block of a hypothetical critical counterexample would have
\[
\frac{B_A}{I_A}>6.4547837-2.8853901=3.5693936\ldots,
\tag{4.5}
\]
with a still stronger requirement whenever the outside spectral label predicts some of the block bits better than the trivial all-zero guess.

This strictly extends the inherited singleton erasure-heavy condition to **all physical blocks**.

## 5. Bipartition consequence: cross-block dependence is overlap-paid

Let `A` and `A^c` be a nontrivial bipartition of the relevant coordinates of the same critical descendant. Spectral entropy gives the exact identity
\[
B_A+B_{A^c}
=H(S_A\mid S_{A^c})+H(S_{A^c}\mid S_A)
=H(S)-I(S_A;S_{A^c}).
\tag{5.1}
\]
Apply (4.2) to both blocks and use `I_A+I_{A^c}=I(g)` and `H(g)=rI(g)`. The `rI` terms cancel exactly:
\[
\boxed{
I(S_A;S_{A^c})
\le c_*\,[M_A(g)+M_{A^c}(g)].
}
\tag{5.2}
\]

So a maximal-ratio counterexample core cannot have arbitrary cross-block spectral dependence: for **every** physical cut, that mutual information must be paid by the optimal fibrewise Hamming prediction errors on the two sides. The cruder `M_A<=I_A` gives
\[
I(S_A;S_{A^c})\le c_* I(g).
\tag{5.3}
\]
At the Hod calibration this is at most about `0.4470 H(g)`.

The inherited factor-two block sandwich alone only gives `I(S_A;S_{A^c})<=H(g)/2`; (5.2) is adaptive to the actual conditional spectral geometry and can be much smaller.

## 6. What this does and does not solve

**PROVED in this run:**

1. the block nearest-character Walsh log-Sobolev inequality (3.4);
2. the all-dimensional recombination payment `R_A<= (2/ln2)M_A` (3.1);
3. the strengthened all-block erasure requirement (4.3)--(4.4) on every restriction-critical descendant;
4. the exact bipartition dependence cap (5.2).

**NOT PROVED:** full FEI, a bounded proper-block selector, or a quantitative stability theorem converting B17's exact product-spectrum rigidity into the required selector.

**Why the result moves the target:** B18 reduced FEI to finding one proper block with bounded `B_A/I_A`, while B17 showed that an exactly product spectral law with many tiny marginals is impossible. Equations (3.1) and (5.2) insert a concrete intermediate object between these facts: `M_A` measures, on each outside fibre, how close the inside spectral law is to a deterministic Fourier corner. A full closure can now target a stability dichotomy of the following form:

> in every low-influence Boolean spectral law, either some proper block has bounded `B_A/I_A`, or some cut has enough mutual information relative to `M_A+M_{A^c}` to contradict (5.2) on the maximal-ratio descendant.

The next B14 run should attack precisely that stability statement (or falsify it with an explicit Boolean family), not re-run the existing finite FEI atlas and not retry an every-prescribed-coordinate payment.

## 7. Current literature check and claim discipline

A bounded current search found González--MacManus--Pereyra, arXiv:2606.00246 (29 May 2026), which uses restriction entropy decrement / stopping-tree ideas, and Potapov, arXiv:2609.21563 (18 September 2026), which proves FEI for plateaued and partially bent functions. The current repository also contains the stronger recent internal block-Walsh and product-spectrum mechanisms listed above. I did not locate the fibrewise nearest-character block remainder (3.1) in that bounded search, but a search miss is not a priority proof. **Publication priority remains UNVERIFIED.**

**Final status:** full FEI is **OPEN**. This report supplies a new exact payment mechanism and a sharper necessary structure for any hypothetical counterexample core.
