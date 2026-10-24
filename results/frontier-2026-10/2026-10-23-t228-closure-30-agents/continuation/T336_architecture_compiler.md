# T336: an explicit arithmetic compiler with one ordinary LayerNorm branch

Agent 24, 23 October 2026. New follow-up research; no frozen-package files edited. The construction and proof below are independent of the T228 numerical audit.

**Result.** A finite arithmetic circuit for the finite-feature GP posterior compiles into finite bidirectional residual ReLU attention, with one ordinary full-token pre-LayerNorm feed-forward residual sublayer. A dedicated scratch token contains only design information. Raw labels stay unchanged on the source tokens and enter only a final exact attention dot product. No projected-normalization primitive, input-dependent inverse in the readout, or approximation on the label axis is needed.

The architecture qualification is substantive: attention and ordinary arithmetic blocks here are **not** pre-normalized. Only one specified feed-forward residual sublayer uses LayerNorm. This is not a claim about a standard Transformer that pre-normalizes every attention and feed-forward block, and it is not a softmax-attention construction. Section 10 gives a precise all-label obstruction for a usual fully pre-LN class.

## 1. Architecture and input interface

Fix at most \(n\) context observations, one query, feature dimension \(r\ge1\), and observation-noise variance \(s>0\). Pad the context with zero feature/label rows to exactly \(n\) positions. Use

\[
N=n+2
\]

tokens: \(n\) context positions, one query position, and one additional scratch position \(\star\). The readout is from the scratch token; a fixed additional attention layer can copy it to the query if that interface is required.

Each token has immutable local design coordinates \(d_i\in\mathbb R^F\), immutable raw label \(y_i\), and a positional one-hot \(e_i\in\mathbb R^N\). The query and scratch labels are zero. Scratch local design coordinates are zero. There is also one immutable coordinate \(-p_i\), where

\[
p_i=(e_i)_\star=\mathbf 1\{i=\star\}.
\]

The scratch token consequently has the fixed pair \((p_\star,-p_\star)=(1,-1)\). **There is no separate constant-one register.** Every scratch constant is a multiple of \(p\); the local source input and fixed position encodings are not computed by a nonlinear oracle.

For the main feature-input theorem, \(F=r\), \(d_i=\phi_i\) on context tokens, and \(d_q=q\) on the query. Exact arbitrary-feature evaluation from raw covariates is not free. Section 8 separately costs polynomial features or a supplied finite arithmetic feature circuit.

The attention update is

\[
h_i^+=h_i+\frac1N\sum_{a=1}^{H}\sum_{j=1}^{N}
\operatorname{ReLU}\!\left(\langle Q_a h_i,K_a h_j\rangle\right)V_a h_j.
\tag{1}
\]

All matrices are fixed real matrices for the exact comparator; zeros in the specified connectivity can remain architectural zeros in a trainable family. The factor \(1/N\) is fixed sequence-length scaling, not softmax or score-dependent row normalization. No mask is needed. Fixed masks that keep the same source/target edges would also work.

Except for one explicitly described sublayer, tokenwise feed-forward blocks are identities or ordinary residual ReLU maps without normalization. The one special sublayer is exactly

\[
h_i^+=h_i+W_2\operatorname{ReLU}(W_1\operatorname{LN}_{\epsilon}(h_i)),
\qquad
\operatorname{LN}_{\epsilon}(h)
=\frac{h-\bar h\mathbf1}
{\sqrt{D^{-1}\|h-\bar h\mathbf1\|_2^2+\epsilon}},
\tag{2}
\]

with fixed gain one, bias zero, and \(\epsilon>0\). The normalization width is the **entire embedding width \(D\)**, including every position, local input, label, scratch register, and unused zero coordinate. Thus the source-token LayerNorm internally sees labels; its feed-forward contribution cancels identically, as proved below. Positive epsilon makes the sublayer defined at every source token and every trainable parameter setting.

Equation (1) is the ReLU-attention form in Bai et al., Definition 1; the selective choice to include (2) at exactly one stage is an explicitly stated augmentation. Primary reference: [Bai et al., arXiv:2306.04637v2, Section 2.1](https://arxiv.org/html/2306.04637v2#S2.SS1). Nothing in that reference is being cited as a proof of the exact reciprocal construction here.

## 2. Exact scratch-only attention primitives

All mutable work registers start at zero on every token. Every primitive below preserves zero work registers on all source tokens and writes only on the scratch token. The immutable source design, labels, positions, and balance coordinate are never output coordinates of a value matrix.

**Gather.** For each of the \(n+1\) source positions \(j\), use one head

\[
Qh_i=p_i,\qquad Kh_k=(e_k)_j,
\]

whose value writes \(N d_k\) into a fresh \(F\)-coordinate copy block for position \(j\). Its score is one exactly for \((i,k)=(\star,j)\), and zero otherwise. Hence one layer with \(n+1\) heads copies all local design inputs to scratch. Labels are not copied.

**Affine gate.** Suppose scratch work registers \(a,b\) are zero elsewhere. To create \(g=\alpha a+\beta b+c\) in a fresh zero register, use

\[
Qh_i=p_i,\quad Kh_j=p_j,\quad
Vh_j=N(\alpha a_j+\beta b_j+cp_j)e_g.
\]

Only the scratch self-edge contributes. The same formula allows arbitrary fixed affine fan-in and simultaneous writes of any fixed affine vector.

**Multiplication gate.** To create \(g=ab\), use two heads:

\[
Q_+h_i=a_i,\quad K_+h_j=b_j,\quad V_+h_j=Np_j e_g,
\]

\[
Q_-h_i=-a_i,\quad K_-h_j=b_j,\quad V_-h_j=-Np_j e_g.
\]

All non-scratch queries and keys are zero. At scratch, the update is

\[
\operatorname{ReLU}(ab)-\operatorname{ReLU}(-ab)=ab.
\]

This identity is exact for all signs and all real magnitudes. No boundedness assumption, product approximation, nonlinear readout, or attention-weight interpretation is used. Each scalar product costs one layer and two heads; each scalar affine gate costs one layer and one head. Fresh registers avoid residual overwrite errors.

These primitives prove by induction that any finite straight-line arithmetic circuit can run on scratch. They also implement fixed register erasure and routing: a constant scratch self-edge can subtract every old working coordinate while writing arbitrary linear combinations into initially empty coordinates.

## 3. The determinant as a sum of squares

Let \(\Phi\in\mathbb R^{n\times r}\) contain padded context features, let \(q\in\mathbb R^r\) be the query feature, and set

\[
H=sI_r+\Phi^T\Phi,\qquad \Delta=\det H>0.
\]

The Cauchy–Binet identity applied to \(\begin{pmatrix}\Phi\\\sqrt{s}I_r\end{pmatrix}\) gives

\[
\Delta=s^r+
\sum_{k=1}^{\min(n,r)}\ 
\sum_{\substack{I\subseteq[n],\ J\subseteq[r]\\|I|=|J|=k}}
s^{r-k}(\det\Phi_{I,J})^2.
\tag{3}
\]

There are

\[
M=\sum_{k=0}^{\min(n,r)}\binom nk\binom rk=\binom{n+r}{r}
\]

terms including the positive constant. Write the \(M-1\) nonconstant polynomial quantities as

\[
u_\ell=s^{(r-k)/2}\det\Phi_{I,J},\qquad
\Delta=s^r+\sum_{\ell=1}^{M-1}u_\ell^2.
\]

Their minors are evaluated by finite additions and products, for example the Leibniz formula. These quantities depend only on design inputs, never labels.

## 4. Full-token LayerNorm, with exact source cancellation

Allocate \(2(M-1)\) scratch normalization coordinates for pairs \((+\lambda u_\ell,-\lambda u_\ell)\), and two special coordinates for \((+1,-1)\). All these coordinates are zero on source tokens. Before (2), execute one fixed affine scratch-attention layer that:

1. writes these pairs from the completed minor registers;
2. sets the special pair to \((p,-p)\);
3. erases **all** copied design and arithmetic work registers, leaving them zero;
4. leaves immutable local input/label/position coordinates alone.

The original source tokens are unchanged. On scratch, local design and label coordinates are zero by initialization. Exactly one positional coordinate remains one, balanced by the immutable \(-p=-1\). All other positions are zero. In particular, there is no forgotten constant-one coordinate or preinitialized variance coordinate. The normalized scratch vector has precisely

\[
(\lambda u_1,-\lambda u_1,\ldots,
\lambda u_{M-1},-\lambda u_{M-1},1,-1,1,-1)
\]

among its nonzero coordinates, with the final pair representing position and balance. Consequently its mean is zero and

\[
\|h_\star\|^2=2\lambda^2\sum_\ell u_\ell^2+4.
\]

Choose, **after fixing the total embedding width \(D\)**,

\[
\lambda^2=\frac{4+D\epsilon}{2s^r}.
\tag{4}
\]

The scratch LayerNorm denominator then satisfies the exact identity

\[
\frac{\|h_\star\|^2}{D}+\epsilon
=\frac{2\lambda^2}{D}\left(s^r+\sum_\ell u_\ell^2\right)
=\frac{2\lambda^2}{D}\Delta.
\tag{5}
\]

The free choice of \(D\) only changes a fixed real coefficient in (4); there is no circular gate-count dependency.

Let \(\ell(h)\) subtract the normalized special minus-coordinate from the normalized special plus-coordinate. Set the two rows of \(W_1\) in (2) to \(\ell\) and \(-\ell\); let \(W_2\) write their signed difference into one fresh zero register \(z\), and nowhere else. Thus the residual sublayer writes

\[
z_i=\operatorname{ReLU}(\ell(\operatorname{LN}_\epsilon(h_i)))
-\operatorname{ReLU}(-\ell(\operatorname{LN}_\epsilon(h_i)))
=\ell(\operatorname{LN}_\epsilon(h_i)).
\]

At a source token, both special coordinates equal zero. They undergo the same centering and division, regardless of its raw label, so their normalized values are identical. Hence \(z_i=0\), and **the entire source token remains unchanged**. This is an algebraic identity, not an approximation for large labels or a bound on their effect.

At scratch,

\[
z_\star=\frac{2}{\sqrt{(2\lambda^2/D)\Delta}}.
\]

Two further arithmetic gates produce

\[
\rho=\frac{\lambda^2}{2D}z_\star^2=\frac1\Delta.
\tag{6}
\]

This is an ordinary full-token LayerNorm followed by an ordinary two-unit ReLU FFN residual. It does not assume a group-normalization operation. Fixed unit gains, zero biases, and the specified difference selector are essential to the source cancellation.

## 5. Reloading the erased design and the all-label readout

After the normalization sublayer, repeat the fixed gather layer. The source inputs are unchanged, and their copy blocks on scratch were cleared, so this reload is exact. Recompute any cleared feature values, \(H\), and its adjugate \(C=\operatorname{adj}(H)\). No information needed for those computations is being retained secretly through normalization.

Use arithmetic gates to form

\[
u=Cq,\qquad t=\rho u=H^{-1}q,
\qquad a=\Phi t,\qquad v=s+s q^Tt.
\tag{7}
\]

All these quantities are label-independent and live only on scratch. The exact posterior mean is \(m=a^Ty\), and \(v\ge s\) is the noisy predictive variance.

The mean is implemented by exactly two final attention heads. Let \(a_i\in\mathbb R^n\) denote the coefficient registers on token \(i\); they are zero unless \(i=\star\). Let \(e_j^{\rm ctx}\in\mathbb R^n\) be the first \(n\) positional coordinates. Use

\[
Q_\pm h_i=\pm a_i,\qquad
K_\pm h_j=e_j^{\rm ctx},\qquad
V_\pm h_j=\pm N y_j e_{\rm mean}.
\tag{8}
\]

At scratch the signed score pair contributes \(a_jy_j\) for context position \(j\). Query and scratch keys are zero. At every other target, \(a_i=0\) and the update is zero. Thus a fresh mean coordinate receives exactly \(a^Ty\), for **every** \(y\in\mathbb R^n\), including arbitrary signs and unbounded magnitudes. Labels are used only by this fixed final value projection. A linear readout selects \((m,v)\), directly as Gaussian mean and variance.

## 6. Explicit size for feature inputs

Count a scalar affine gate with arbitrary fixed fan-in as one gate, and an ordinary scalar product as one gate. Its fan-in coefficients are included in the dense attention matrix count. Let

\[
G_{\rm min}=\sum_{k=1}^{\min(n,r)}
\binom nk\binom rk\,[k!(k-1)+1],
\]

\[
G_{\rm adj}=r^2\big[(r-1)!\max(r-2,0)+1\big].
\]

The first expression builds every weighted minor \(u_\ell\) by Leibniz products and one signed affine sum. The second builds all cofactors, with an affine constant gate safely covering \(r=1\), when the adjugate is \([1]\).

A sufficient total arithmetic gate count is

\[
\boxed{
S=nr^2+2r^2+nr+n+3r+3+G_{\rm min}+G_{\rm adj}.
}
\tag{9}
\]

The terms count: \(nr^2+r^2\) gates for \(H\); the minors and adjugate; two gates for (6); \(r^2+r\) for \(Cq\); \(r\) for multiplication by \(\rho\); \(nr+n\) for \(a=\Phi t\); and \(r+1\) for \(v\). The only pre-normalization arithmetic is the minor circuit. Every other listed calculation occurs after re-gathering, so no erased intermediate is reused. In particular, \(H\) is not unnecessarily computed before the normalization.

With feature-input width \(F=r\), choose

\[
\boxed{D=N(F+1)+S+2M+4,\qquad N=n+2.}
\tag{10}
\]

This includes local design, one raw label, \(N\) positional coordinates, the negative scratch-role coordinate, \((n+1)F\) copied design coordinates, \(S\) gate slots, \(2M\) normalization slots, the normalized scalar slot \(z\), and the mean slot. Unused coordinates can be zero-padded, provided (4) uses the actual resulting width.

The complete implementation has

\[
\boxed{L\le S+5,\qquad H_{\max}\le\max(n+1,2).}
\tag{11}
\]

The five additional stages are initial gather, affine preparation/erasure, the one LayerNorm-FFN sublayer, re-gather, and label readout. Arithmetic stages have at most two heads; the gather uses \(n+1\). The normalized FFN has hidden width two. There are no other required nontrivial FFNs.

For ordinary dense \(D\times D\) attention matrices, a conservative stored-weight bound, including fixed LayerNorm gains/biases and a two-output linear readout, is

\[
\boxed{P_{\rm dense}\le
3(S+4)\max(n+1,2)D^2+8D.}
\tag{12}
\]

This deliberately counts zero and fixed entries. Fixed affine input placement and positional encodings are not included, consistently with the usual register-input convention. The learnable parameter count can be much smaller. The result is an arbitrary-real-weight size theorem, not a finite-bit or numerically stable implementation claim. The determinant/adjugate construction is factorial/combinatorial in rank; no efficient polynomial-rank complexity is asserted.

For \(n=0\), all empty sums and the two label heads can be omitted; the displayed bounds remain valid. The circuit then returns the prior noisy predictive exactly.

## 7. A structurally safe non-singleton trainable class

The exact comparator belongs to a finite parameter box once its finitely many weights are bounded by a sufficiently large \(W\). A statistically meaningful larger class can vary arithmetic and feature-circuit weights. It must preserve the following architectural restrictions for **every** allowed parameter vector, not merely at the exact comparator:

- Input placement, positions, balance, source labels, and source designs are immutable. Gather is fixed and reads design only.
- Arithmetic query/key inputs are restricted to scratch-working coordinates and \(p\), all zero on source tokens. Values write only working coordinates. Affine offsets are represented using \(p\), not a universal bias that acts on sources.
- Preparation/erasure is fixed. Normalization gains/biases and the special-coordinate difference FFN are fixed as in Section 4.
- The final label readout (8) is fixed; no earlier free matrix may read labels.

Inductively, source working coordinates remain zero under every arithmetic layer. The normalization pair is zero at every source; the normalized contribution cancels there, so source labels cannot affect scratch through that stage. Scratch itself has no label input. Reloading remains label-independent. Consequently all coefficient and variance outputs before the final readout are functions of design alone for every allowed parameter setting.

This invariance does not require the pre-normalization minors to be correct for a non-comparator parameter. They may be arbitrary design functions. Fixed erasure and paired routing still isolate the branch. For ERM sensitivity bounds, the identically zero source-normalization contributions can be algebraically removed; the remaining normalization is entirely label-independent, with denominator at least \(\sqrt\epsilon\).

Suppose \(\|\phi(x)\|\le R\). The exact comparator satisfies

\[
s\le v\le V:=s+R^2,\qquad
\|a\|_2^2=q^TH^{-1}(H-sI)H^{-1}q
\le q^TH^{-1}q\le R^2/s.
\]

Choose \(A\ge R/\sqrt s\). Add one fixed unnormalized residual-MLP layer before (8) using

\[
a_j\leftarrow a_j+\operatorname{ReLU}(-Ap-a_j)
-\operatorname{ReLU}(a_j-Ap),
\]

\[
v\leftarrow v+\operatorname{ReLU}(sp-v)
-\operatorname{ReLU}(v-Vp).
\tag{13}
\]

On scratch these are the clips to \([-A,A]\) and \([s,V]\). On a source, \(p=a_j=v=0\), so they leave zero unchanged. Scaling the clip offsets by \(p\) is necessary: an ordinary source variance clip would otherwise introduce a spurious positive source working value. The exact comparator is preserved, while all class members have bounded coefficients and a positive bounded variance.

This costs one additional layer, hidden width \(2(n+1)\), and at most \(4D(n+1)\) extra dense FFN entries. Width is unchanged. Thus the ERM-compatible architecture has depth at most \(S+6\), maximum FFN hidden width \(2(n+1)\), and the bound (12) plus \(4D(n+1)\). Arbitrarily freeing the architectural zeros, the label exclusions, or the normalization difference-selector entries would define a different class and would not inherit this proof.

For a concrete non-singleton witness when \(n\ge1\), choose \(A=1+R/\sqrt s\), freeze the exact circuit except for \(n\) designated coefficient biases \(b_j\in[-1/2,1/2]\), and make the existing affine sum gate for \(a_j\) compute \(\sum_k\Phi_{jk}t_k+b_jp\). These are the already allocated affine offset entries; no additional layer, register, or matrix is needed. At the comparator, \(b=0\). The bound \(|a_j|\le R/\sqrt s\) shows these biased exact coefficients never reach the clip endpoints, so distinct biases give distinct label-linear predictors. This witness has exactly \(P=n\) free parameters and the same stored bound and \(S+6\) clipped depth as above.

The intended broader ERM class need not freeze the posterior computation: take **every permitted coefficient in all arithmetic and feature-circuit Q/K/V maps free**, subject to the declared scratch-working read/write supports, label exclusion, and fixed constant routing. Include the \(n\) offset entries above among these free coordinates. All-parameter source-zero and label-independence invariance was proved structurally, so it continues to hold throughout this larger box. Its exact comparator is the explicit circuit assignment, and it contains the non-singleton witness. If \(P_{\rm other}\) counts the other free entries, its free dimension is \(P=P_{\rm other}+n\); the fixed gather, preparation, normalization selector, clips, and final readout remain fixed. The same \(S+6\) depth and stored-weight bound (12) plus \(4D(n+1)\) apply. Free-parameter dimension and the larger count of stored fixed matrices must not be conflated in an ERM covering bound.

## 8. Raw feature computation and multiple queries

If each feature coordinate is a polynomial in \(d\) raw inputs with at most \(T\) monomials and degree at most \(d_\phi\), take local design width \(F=d+1\), including a context-presence flag; the query flag is fixed present. An arithmetic feature evaluation for all \(n+1\) sources, including multiplication of context features by the presence flag, costs at most

\[
E_\phi=(n+1)r\,[T\max(d_\phi-1,0)+1]+nr
\]

gates. Use the raw-input gather, evaluate these features before the minor computation, then evaluate them again after clearing and re-gathering. Replacing \(S\) by \(S+2E_\phi\) in (10)–(12), and replacing \(F=r\) by \(F=d+1\), is a sufficient explicit bound. This counts the recomputation instead of assuming it survives normalization. A general supplied finite arithmetic feature circuit can be treated by its actual gate count in the same way.

An arbitrary bounded or continuous finite-rank feature map need not have an exact finite arithmetic circuit. Such a map must either be supplied as input features, or a separate exact feature implementation must be given. Replacing it by an approximation does not automatically preserve an all-real-label uniform-KL statement: any nonzero coefficient error can be magnified by unbounded labels. The previously established bounded-label approximation constructions address a different scope.

For finitely many queries, store all query features, compute the label-independent coefficient matrix and \(s\Phi_\ast H^{-1}\Phi_\ast^T\) after the same single normalization, and add \(sI\) for noisy targets. Two final label heads per output mean coordinate implement the matrix-vector product. This is a finite extension of the same primitives; equations (9)–(12) specifically state the fully counted one-query bound.

## 9. What this establishes for T336

For the stated finite-feature GP, supplied features or exactly compiled polynomial features, fixed maximum context length, and positive noise, the architecture produces the exact noisy predictive mean and variance for all contexts and **all real labels**. Its forward KL is identically zero. The source-label cancellation and role-scaled clips also supply the label-independent coefficient interface used by the separate prior-averaged ERM analysis.

This proves an explicit finite neural implementation of the algebraic circuit; it does not hide division in a Gaussian decoder. It uses an ordinary LayerNorm primitive, but at a specially controlled location in an otherwise unnormalized ReLU-attention architecture. It therefore does not silently upgrade the historical no-LayerNorm C002 architecture, prove a result about conventional softmax Transformers, or settle arbitrary discontinuous/raw-input kernels. It also does not prove SGD convergence or publication-level novelty.

A close primary precedent is [Akyürek et al., arXiv:2211.15661v3, Appendix C.6, Lemma 8](https://arxiv.org/html/2211.15661v3#A3.SS6), which explicitly uses LayerNorm for approximate division with large constants. That precedent prevents treating normalization-based arithmetic itself as new. The construction here proves the displayed exact finite-constant identities and explicitly preserves the all-label path; no exhaustive novelty claim follows.

## 10. Why a standard fully pre-LN replacement is not automatic

There is a direct obstruction for the following precisely delimited class. Suppose the input embedding is fixed affine in raw design coordinates and labels; the design domain is compact; token count, width, depth, and weights are finite; and every residual update has the form

\[
h^{\ell+1}=h^\ell+F_\ell(\operatorname{LN}_\epsilon(h^\ell)),
\tag{14}
\]

where \(\epsilon>0\) and each \(F_\ell\) is continuous on the compact closure of the bounded normalized-input range. Standard finite attention/FFN blocks with finite weights meet that continuity condition. A final Gaussian mean is an affine readout of \(h^L\).

LayerNorm's image is bounded: with unit gain/bias, each normalized token has Euclidean norm at most \(\sqrt D\); any fixed finite affine gain/bias keeps it bounded. Therefore each residual increment in (14) is uniformly bounded, independently of labels. Summing finitely many increments gives

\[
h^L=h^0+O(1)
\]

uniformly over design and all labels. An affine mean readout consequently has the form

\[
\widehat m(x,y)=b^Ty+O(1),
\]

with a design-independent vector \(b\). A final full LayerNorm before readout makes the mean bounded, which is an even stronger restriction.

Already with one context from the rank-one GP \(k(t,u)=tu\), query one, and context \(x\in[1,2]\), the exact mean is \(a(x)y\), where \(a(x)=x/(s+x^2)\) is not constant on that interval. Choose an \(x\) for which \(a(x)\ne b\). The mean error is then unbounded as \(|y|\to\infty\). Even arbitrary positive predicted variance cannot repair uniform forward KL, because, for target variance \(v>0\) and mean error \(e\),

\[
\inf_{w>0}\operatorname{KL}(N(m,v)\|N(m+e,w))
=\tfrac12\log(1+e^2/v).
\]

Thus this fully pre-LN class has infinite all-label worst-case forward KL in that elementary model. The proposition excludes nonlinear design-label products already hidden in the input embedding, unnormalized value paths, multiplicative external readouts, and other bypasses; those would change its assumptions. Our construction escapes it explicitly through unnormalized arithmetic attention and the final raw-label value path. This is why the architecture qualification cannot be dropped.

## 11. Supplementary exact wiring check

`followup/check_T336_architecture_compiler.py` evaluates the actual fixed-score ReLU-attention sums, scratch clearing, full-width normalization difference, re-gather, adjugate/product gates, clips, and final label heads using exact Python fractions. Its rank-one test has \(n=r=s=1\), context feature \(3/4\), query feature \(-2\), width \(D=72\), and \(\epsilon=1/18\). These make \(\lambda=2\) and the scratch normalization denominator \(5/12\), so every nonzero normalization value used by the FFN is rational. Source-token selected differences vanish identically regardless of their common, potentially irrational denominator.

All 12 combinations of labels \(0,-7/3,10^{100},-10^{100}\) and biases \(0,1/2,-1/2\) passed exact equality checks. The reciprocal was \(16/25\), the unbiased coefficient \(-24/25\), and the noisy variance \(89/25\); every source token remained exactly unchanged. Results are in `followup/check_T336_architecture_compiler.json`. This is a finite wiring check, not a substitute for the general algebraic proof or a numerical-stability claim.

