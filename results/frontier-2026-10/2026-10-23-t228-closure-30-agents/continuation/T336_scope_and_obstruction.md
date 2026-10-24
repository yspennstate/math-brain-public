# T336: exact scope, the unbounded-label obstruction, and a sufficient completion theorem

Author: A30. Follow-up to the frozen T228 campaign. This document does not change or reclassify the prior campaign. It is an independent mathematical scope analysis and a self-contained statistical bridge, not an external review or a novelty certificate.

## 1. Exact request and what the prior work proves

I independently read the exact T336 registry object, the complete A02 continuous-kernel construction, and the complete A05 ERM bridge. The registry asks for a **given prior**, quantitative transformer size for posterior-predictive approximation in KL **uniformly over datasets of size N**, a number of prior-sampled pretraining datasets, and convergence of pretrained predictions to the Bayes predictor as size and sample size grow. It does not itself bound labels or specify an architecture, predictive noise, KL direction, or a mode of convergence for learned predictions. These choices must therefore be stated, rather than silently inherited from a repaired dossier.

| Read source | SHA-256 |
|---|---|
| `a02/T336_REGISTRY.json` | `a62961f2c1f30287356a73e9609430d437e93ba42a85aaad85908fdbd2d5f7d6` |
| `a02/CONTINUOUS_KERNEL_EXTENSION.md` | `5cd1bdd401d2efbd15433e9fa5fc1834e792424fa70fba552da85b776ef45566` |
| `a05/ERM_BRIDGE.md` | `97eeb783f610ea4ce4ead20c547a0ec65ebc4ca0320d7a07e4d38c05bf936d96` |
| `a02/DOSSIER.md` | `326390bfbf2500bd2e11d0143cb5fb53e6eb6ab3f4015b885db7ae328c829399` |
| `a02/C003.md` | `80a484b6a70e58716b1388390148e3cb847f3b8079c2c1dceba5f9601c1f9003` |

A02 proves a useful, genuinely quantitative theorem for continuous kernels, including infinite-rank RBF kernels, on compact raw-input domains. Its deterministic uniform guarantee requires bounded context labels. Its Chebyshev and feature errors explicitly multiply a label bound. Its optional mean and context clips preserve that restricted approximation statement.

A05 handles genuine, unbounded Gaussian training labels. It obtains prior-averaged forward KL by controlling a clipping tail and proving finite-sample ERM concentration. It does not assert a uniform guarantee over all real label vectors. The distinction is mathematically necessary for that construction, not merely a missing sentence in the proof. C003's discontinuous-kernel obstruction is a separate issue.

The primary PFN paper's Corollary 1.1 identifies its expected negative log likelihood with **prior-averaged** forward KL up to a model-independent constant. This supports that mode of learning convergence; it does not convert it into a worst-context bound. I checked the primary PDF, printed page 4: [Müller et al., arXiv:2112.10510v7](https://arxiv.org/pdf/2112.10510v7).

## 2. Why exact label linearity alone does not solve the problem

Fix a design consisting of context covariates and query. For a GP with independent noise variance `s>0`, the noisy predictive is

    p_y = N(a^T y, v),    s <= v <= s+K,

where `a` and `v` depend only on the design and `K` bounds the kernel diagonal. Suppose the proposed mean is `ahat^T y+b`. The predicted variance may even be an arbitrary positive function of `y`.

For any target mean `m`, target variance `v>0`, predicted mean `mhat`, and predicted variance `w>0`, direct minimization in `w` gives

    KL(N(m,v) || N(mhat,w))
       >= (1/2) log(1+(m-mhat)^2/v).                       (2.1)

Indeed the minimizing variance is `w=v+(m-mhat)^2`. Therefore finite worst-label KL implies a bounded mean error. If `ahat != a`, take `y=t(a-ahat)`. The mean error is `t||a-ahat||^2-b`, so (2.1) diverges. Allowing the model to inflate its variance cannot repair the problem.

Consequently, a label-linear mean with any nonzero coefficient approximation error has infinite worst-label forward KL at that design. Exact linearity is useful for analysis and training, but **exact posterior coefficients**, or a uniformly bounded additive mean error with the exact asymptotic slopes, are necessary for this all-label target. Setting a small coefficient tolerance independently of labels does not suffice.

The bounded-label mean clip is even more directly incompatible with this target whenever the true coefficient vector is nonzero. No finite choice of a clipping radius covers every real label vector.

## 3. A continuous GP already obstructs the old architecture

Consider the nonconstant rank-one prior

    f(x)=Gx,  G~N(0,1),  x in [1,2],

one observation `(x,y)` with noise variance `s>0`, and query `1`. The noisy predictive has

    m(x,y)=xy/(s+x^2),
    v(x)=s+s/(s+x^2).

Any finite circuit using affine operations, multiplication, and ReLU selects its mean from a finite library of bivariate polynomials `P_1(x,y),...,P_L(x,y)`. This includes the prior length-normalized ReLU-attention architecture with affine/polynomial raw preprocessing and a direct mean readout.

Write `p_i1(x)` for the coefficient of `y` in `P_i`. The polynomial

    (s+x^2)p_i1(x)-x

is not identically zero: a polynomial cannot equal `x/(s+x^2)` on an interval. Choose `x0 in (1,2)` outside the finite union of its real roots over `i`. For each branch, `P_i(x0,y)-x0*y/(s+x0^2)` is a nonconstant polynomial in `y`. Its absolute value tends to infinity as `y` tends to positive infinity. The minimum over finitely many branches also tends to infinity. Equation (2.1) then proves infinite worst-case forward KL, even with an arbitrary positive variance decoder.

This proof does not require a stable branch, a regular partition, or a label-independent predicted variance. It does require that the **decoded mean itself** select from finitely many polynomials. Softmax, normalization, division, and nonlinear Gaussian parameter decoders can invalidate that hypothesis. For example, polynomial natural parameters can already give a rational decoded mean; such a decoder must be counted and named. The result is not a universal transformer impossibility.

A27 independently developed and completed this obstruction, with stronger quantitative interval and growth statements, in `followup/T336_unbounded_label_independent.md`. That report's initially communicated SHA-256 is `82ebfbbee8cca6d7f8ac1a797b5f605e7e25507bdffdd6d3b51f9a3a25ef4f44`; this paragraph identifies that historical version and does not certify later edits.

## 4. A meaningful specified prior and an exact normalization route

A fixed finite-rank polynomial GP is a legitimate and nontrivial instance of the registry's “given prior” quantifier. A concrete example is

    X=[-1,1],  f(x)=G0+G1*x+G2*x^2,
    (G0,G1,G2)~N(0,I3),  observation noise N(0,s), s>0.

This has continuous kernel `k(x,x')=1+xx'+x^2*x'^2`, diagonal bounded by `K=3`, arbitrary continuous covariates, repeated observations, arbitrary real labels, and a nontrivial three-dimensional posterior. Restricting to this specified prior does not amount to choosing a constant predictor, finite lookup domain, single context, or noiseless problem. It does remain a finite-rank GP result, not an RBF or all-prior theorem.

More generally, let the fixed polynomial feature map be `phi:X->R^r`, with compact `X`, `||phi(x)||^2<=K`, and `f(x)=G^T phi(x)` for `G~N(0,Ir)`. Pad to `n` context rows using zero feature rows. Write `Phi` for the resulting `n by r` feature matrix, `q=phi(x*)`, and

    H=s Ir+Phi^T Phi,    D=det H.

The exact formulas are

    a_i = q^T adj(H) phi(x_i) / D,
    m = sum_i a_i y_i,
    v = s+s q^T adj(H)q / D.                              (4.1)

Padding coefficients are set to zero. Positive `s` covers repeated and rank-deficient designs.

The determinant has the sum-of-squares identity

    D=s^r + sum_{k=1}^{min(n,r)}
                sum_{|I|=|J|=k} s^(r-k) det(Phi_IJ)^2.    (4.2)

One proof applies Cauchy–Binet to the vertically stacked matrix `[sqrt(s) Ir; Phi]` and groups the selected identity rows. All terms are nonnegative; the empty minor gives `s^r`. The number of terms, including the empty minor, is

    M=sum_k binom(n,k)binom(r,k)=binom(n+r,r).

Let the nonconstant weighted minors in (4.2) be `q_1,...,q_(M-1)`, so `D=s^r+sum q_j^2`. Fix a strictly positive LayerNorm stabilization constant `e`. Choose

    lambda^2=(1+M e)/s^r.

Apply LayerNorm, with gain one and bias zero, to the `2M` coordinates

    (lambda q_1,-lambda q_1,...,lambda q_(M-1),-lambda q_(M-1),1,-1).

Their mean is zero. Their empirical variance plus `e` is exactly `lambda^2 D/M`. If `z` is the normalized coordinate originating from `+1`, then

    (lambda^2/M) z^2 = 1/D.                               (4.3)

Thus (4.1) uses polynomial arithmetic, one explicit normalization, products, and sums; it does not need an approximate inverse. A28 supplied this construction independently; I checked its scaling, including the stabilization term. Minors computed by the Leibniz formula give a finite explicit arithmetic circuit; for fixed rank, the number of minor terms is polynomial in `n`. A complete transformer size theorem must still count feature evaluation, cofactors, all gates, routing, padding, and the normalization width.

### Architecture boundary and the full-token normalization refinement

The required coefficient output is **label independent**, and raw labels remain available to a final exact linear readout. Applying full-token LayerNorm indiscriminately would put labels or unrelated registers into the sum of squares and destroy (4.3). A24 has supplied a stronger compiler interface that uses an ordinary full-token LayerNorm inside one residual feed-forward stage, without a new projected-normalization primitive.

Use a separate scratch token and immutable source-token design/label registers. Fixed routing writes only to scratch working registers. Before the normalization stage, clear the scratch token except for the paired weighted minors, two special constants `(+1,-1)`, and its persistent position/balance pair `(+1,-1)`. Let `d_tok` be the entire token width. Thus the scratch squared norm is

    2 lambda^2(D-s^r)+4.

Its coordinate mean is zero. With fixed normalization floor `e>0`, choose

    lambda^2=(4+d_tok e)/(2s^r).

The full-token normalization denominator squared is exactly `2 lambda^2 D/d_tok`. A fixed feed-forward selector subtracts the two normalized special coordinates, producing `b=2/denominator` on the scratch token. Hence

    lambda^2 b^2/(2d_tok)=1/D.                             (4.4)

On every source token, both special coordinates are identically zero. Their normalized values are therefore equal, even if the normalization's mean and denominator depend on a source label. The same fixed difference selector is identically zero there. Thus this stage preserves every source token and transmits no source-label dependence into the scratch coefficient computation. Scratch designs can then be reloaded to compute the adjugate numerators in (4.1).

This cancellation must hold for every trained parameter choice. LayerNorm gains and biases, the special-coordinate selector, scratch routing, source workspace zeros, immutable label registers, and the final linear-label readout are **structural fixed parts** of the architecture. They are not varied by ERM. Only designated design-arithmetic coefficients vary. Affine constants use the scratch-position indicator, so source workspaces remain zero even under trainable biases. The coefficient and variance clips likewise use role-scaled bounds, and so leave zero source workspaces unchanged.

Products are implementable by two signed ReLU-attention heads because `ReLU(u)-ReLU(-u)=u`. I independently read A24's complete compiler, `followup/T336_architecture_compiler.md`, and checked its fixed positional gathering, scratch-only affine/product gates, erasure inventory, full-width normalization, source cancellation, second gather, exact signed label readout, and all size terms. The architecture is an **LN-augmented residual ReLU-attention transformer with one full-token pre-LN feed-forward stage**, not an assertion about a stock softmax transformer with normalization before every attention block.

The distinction is substantive. In a standard pre-LN stack with fixed finite weights, positive normalization floor, query-only affine output, and no unnormalized cross-token readout, normalized token states are bounded. Each query update is then bounded uniformly in labels. Starting from a label-free query, finitely many such updates cannot produce an unbounded Bayes mean. An unnormalized label route is therefore part of this proposed construction, not an ignorable implementation detail.

The proposed representation is exact in the usual arbitrary-real-weight, exact-arithmetic model. Finite-precision coefficient rounding can restore the obstruction in Section 2; no finite-bit all-label guarantee follows.

LayerNorm-based division and transformer ridge algorithms are prior ideas. I checked [Akyürek et al., arXiv:2211.15661v3](https://arxiv.org/pdf/2211.15661v3), Appendix C.6, Lemma 8, printed pages 24–25: its displayed division construction is approximate, using large constants. It cannot by itself justify exact coefficients for arbitrarily large labels. No priority claim is made for the present assembly.

### Explicit size from the checked compiler

For reference, the compiler gives the following conservative counts. Scalar affine gates may have arbitrary fixed fan-in, whose coefficients are included in the dense matrix count. Define

    Gmin=sum_{k=1}^{min(n,r)} binom(n,k)binom(r,k)[k!(k-1)+1],
    Gadj=r^2[(r-1)! max(r-2,0)+1],
    S0=nr^2+2r^2+nr+n+3r+3+Gmin+Gadj.

For a raw-input feature map in dimension `d` with at most `Tphi` monomials per coordinate and degree at most `dphi`, let

    Ephi=(n+1)r[Tphi max(dphi-1,0)+1]+nr,
    S=S0+2Ephi,    F=d+1,    Ntok=n+2,
    M=binom(n+r,r),
    d_tok=Ntok(F+1)+S+2M+4,
    H=max(n+1,2).

The feature calculation is counted twice because the scratch inputs are erased before normalization and reloaded afterward. The presence flag is included in `F`; masking each context feature is included in `Ephi`. Explicit coefficient biases occupy the already counted affine offsets in the coefficient-sum gates. With these biases and role-scaled output clips, valid bounds are

    depth <= S+6,
    attention heads per layer <= H,
    FFN hidden width <= 2(n+1),
    total stored scalar entries
      <= 3(S+4)H d_tok^2+8d_tok+4d_tok(n+1).                (4.5)

The counts include fixed and zero matrix entries, fixed normalization gain/bias, and the two-output readout. Fixed affine input placement/position constants use the explicit register-input convention. For supplied features, take `F=r` and `S=S0`. No supplied-feature shortcut is used in the raw polynomial theorem.

For the concrete quadratic GP above, `r=3`, `d=1`, `Tphi=1`, `dphi=2` are sufficient. Thus

    S=34n+69+9 binom(n,2)+13 binom(n,3),
    d_tok=3n+10+S+2 binom(n+3,3).

These bounds are polynomial in context length for this fixed prior. They are intentionally loose and do not assert favorable joint complexity in growing rank. All weights and the necessary finite `W` are obtained from the explicit finite construction after the total token width fixes the normalization scale.

## 5. Non-singleton ERM without any label clipping

The exact representation can be combined with a real learning theorem. Take `n>=1` for this nontrivial learning claim. It is unnecessary to make the training class a singleton, freeze the correct coefficient map, clip context labels, or clip target labels.

Let `Z` denote the complete design: context covariates, length, and query covariate. Its distribution is arbitrary but independent of the GP and noises. Every pretraining task uses a fresh independent GP draw and fresh noises. Write `y` for the padded context-label vector and `Y` for the noisy query target. Conditional on `Z`, `(y,Y)` is centered jointly Gaussian; every nonpadding marginal variance is at most

    V=s+K.

Consider the class

    q_theta(.|Z,y)=N(a_theta(Z)^T y, v_theta(Z)),
    ||a_theta(Z)||_2 <= C,     s <= v_theta(Z) <= V.        (5.1)

Only the **structure** of label linearity and the routing/cancellation constraints above are fixed; the designated design-arithmetic coefficients in the coefficient and variance branches are trainable. Choose a compact parameter box `Theta=[-W,W]^P`, `W>=1`, containing the exact representation `theta_*` in those designated coordinates. Here `P=P_other+n` counts the freely varying permitted design-arithmetic coefficients and explicit coefficient biases, not every stored structural matrix entry. Architecture size must separately count all stored parameters. The main theorem uses this larger structured class, with feature/coefficient computations genuinely trainable. The normalization gains/biases, difference selector, routing, clips, and exact label readout are fixed.

To witness non-singletonness explicitly, choose `A=1+sqrt(K/s)` and hold the other weights at the exact comparator while varying the `n` scratch coefficient biases in `[-1/2,1/2]^n`. Those perturbations survive clipping because the exact coefficients have magnitude at most `sqrt(K/s)`, and produce distinct predictive maps for `n>=1`. This subfamily is only a witness contained in the larger training box; the main learning result is not restricted to estimating a zero bias on a frozen Bayes computation. Smaller rectangular parameter boxes also satisfy the same covering bounds using a common upper bound `W`.

Fixed coordinate clips to `[-A,A]`, with `A>=sqrt(K/s)`, enforce (5.1) with `C=sqrt(n)A`. They preserve the exact comparator: for the true posterior coefficient vector,

    ||a||_2^2 = b^T(G+sI)^(-2)b
               <= (1/s)b^T(G+sI)^(-1)b <= K/s,

where `G` is the context Gram matrix and `b` its query covariance vector. Fixed variance clipping to `[s,V]` also preserves the exact comparator. These are clips on design-dependent coefficients and variance, not on any label or on the final mean.

Define the shifted negative log likelihood

    ell_theta = (1/2)log(v_theta/s)
                   +(Y-a_theta^T y)^2/(2v_theta).

The population excess loss over Bayes is exactly

    R(theta)=E_(Z,y) KL(p(.|Z,y) || q_theta(.|Z,y)).          (5.2)

All expectations are finite. The target conditional variance is in `[s,V]`, so its conditional entropy is finite; the loss bounds below justify the identity directly.

### 5.1 Uniform subexponential loss bound

For every fixed `theta`, conditional on `Z`, the residual `Y-a_theta(Z)^T y` is centered Gaussian. By the triangle inequality in conditional L2,

    Var(Y-a_theta^T y | Z)
       <= V(1+||a_theta||_1)^2
       <= V(1+sqrt(n)C)^2 =: T.                           (5.3)

Set

    A0 = log(V/s)/log(2) + 2T/s.

Since `ell_theta <= (1/2)log(V/s)+(Y-a_theta^T y)^2/(2s)`, Gaussian integration gives

    E exp(ell_theta/A0) <= 2.                              (5.4)

Indeed the deterministic exponential factor is at most `sqrt(2)` and the Gaussian square factor is at most `sqrt(2)`. The coefficient branch's independence from labels is what makes the conditional residual Gaussian; this argument must not be applied to an unrestricted label-dependent network.

For `J` independent tasks, (5.4) implies

    P(|(P_J-P)ell_theta| > A0[sqrt(8u/J)+u/J]) <= 2exp(-u).
                                                               (5.5)

For completeness, (5.4) gives `E ell^k <= 2 k! A0^k`. Expanding the centered moment generating function and using `log x<=x-1` gives, for `|lambda|A0<1`,

    log E exp(lambda(ell-E ell))
        <= 2 A0^2 lambda^2/(1-A0|lambda|).

For negative lambda, `exp(-t)-1+t<=t^2/2` gives the same bound. Chernoff's argument with variance factor `4A0^2` and scale `A0` yields (5.5). This is the same elementary concentration mechanism as A05, with a different envelope that does not clip labels.

For any finite subclass of cardinality `H`, a `xi`-approximate empirical minimizer therefore satisfies, with probability at least `1-delta`,

    R(theta_hat) <= inf_H R + xi
                   +2A0[sqrt(8log(2H/delta)/J)
                              +log(2H/delta)/J].           (5.6)

### 5.2 Explicit full-box ERM bound

Suppose the clipped coefficient and variance maps have uniform parameter bounds

    ||a_theta(Z)-a_theta'(Z)||_2 <= La ||theta-theta'||_inf,
    |v_theta(Z)-v_theta'(Z)| <= Lv ||theta-theta'||_inf.     (5.7)

Section 5.3 gives an explicit way to calculate these constants for the proposed architecture. Set

    D0=(n+1)V,
    G0=La sqrt(1+C^2)/s + Lv(1+C^2)/(2s^2),
    Cpop=Lv/(2s)+G0 D0.

Differentiating the Gaussian loss along the straight line between the two output pairs, and using `||a||<=C` throughout that line, gives the pointwise bound

    |ell_theta-ell_theta'|
       <= [Lv/(2s)+G0(||y||^2+Y^2)] ||theta-theta'||_inf.  (5.8)

This follows from `|Y-a^T y|<=sqrt(1+C^2)sqrt(||y||^2+Y^2)`. Taking expectations proves the stated population Lipschitz constant.

Conditional on a design, the covariance of the padded vector `(y,Y)` has trace at most `D0`. Its eigenvalues are nonnegative with sum at most `D0`; the Gaussian square moment formula and `prod(1-u_i)>=1-sum u_i` for `sum u_i<=1/2` give

    E exp((||y||^2+Y^2)/(4D0)) <= sqrt(2).

Thus, with probability at least `1-delta/2`,

    P_J(||y||^2+Y^2) <= Q_J,
    Q_J=2D0 log(2)+4D0 log(2/delta)/J.

Put `Cemp=Lv/(2s)+G0 Q_J`. A parameter grid of covering radius `rho>0` has at most `(2+2W/rho)^P` points. Applying (5.5) to that grid with

    u=P log(2+2W/rho)+log(4/delta)

and then (5.8) between each point and its grid neighbor proves, simultaneously for all parameters, with probability at least `1-delta`,

    |(P_J-P)ell_theta|
       <= A0[sqrt(8u/J)+u/J]+rho(Cpop+Cemp).

Since the class contains the exact comparator, every `xi`-approximate full-box empirical minimizer obeys

    R(theta_hat) <= xi +2A0[sqrt(8u/J)+u/J]
                        +2rho(Cpop+Cemp).                 (5.9)

Exact empirical minimizers exist: the parameter box is compact and the loss is continuous, with a positive variance floor. This is an ERM theorem, not a claim that SGD finds that minimizer.

Here is an entirely explicit sufficient sample size. Given target `epsilon>0` and confidence `delta in (0,1)`, define

    Qdelta=2D0 log(2)+4D0 log(2/delta),
    Cbar=Lv/s+G0(D0+Qdelta),
    rho=min(1, epsilon/[8(Cbar+1)]),
    u=P log(2+2W/rho)+log(4/delta).

If

    xi <= epsilon/4,
    J >= max(1, 512 A0^2 u/epsilon^2, 8 A0 u/epsilon),      (5.10)

then (5.9) is at most `epsilon`. The net term is at most `epsilon/4`; the two concentration contributions sum to at most `epsilon/2`. This bound is conservative but finite and contains no unknown statistical oracle.

### 5.3 Computable parameter Lipschitz constants

Because the effective coefficient branch depends only on compact designs, its register magnitudes and parameter sensitivities can be propagated through its finite arithmetic graph. The full-token source-normalization contribution is identically zero for every allowed parameter by the fixed selector; prune that branch algebraically before applying these bounds. The surviving scratch normalization is label free. This makes (5.7) quantitative rather than a parameter-count assumption.

For each scalar register `r_j`, retain a uniform magnitude bound `B_j` and a parameter Lipschitz bound `L_j` in infinity parameter distance. Input design registers have known bounded magnitudes and sensitivity zero. For an affine gate `w0+sum w_j r_j`, with trainable coefficients bounded by `W`, valid bounds are

    Bnew=W(1+sum B_j),
    Lnew=1+sum B_j+W sum L_j.

For a product, use

    Bnew=B_i B_j,    Lnew=B_i L_j+B_j L_i.

ReLU and fixed scalar clipping are 1-Lipschitz, so they preserve the sensitivity bound. Fixed coefficients can use their exact magnitudes, omitting their parameter-variation terms.

For LayerNorm on `d` scalar registers with fixed `e>0`, mean subtraction is an orthogonal projection and the map `u -> u/sqrt(||u||^2/d+e)` has Euclidean derivative norm at most `e^(-1/2)`. Therefore each normalized coordinate has magnitude at most `sqrt(d)` and sensitivity at most

    e^(-1/2) sqrt(sum_j L_j^2).

For the full-token compiler, gains and biases are fixed to one and zero, and the special-coordinate difference selector is fixed. Allowing them to vary independently could destroy source cancellation and therefore falls outside this class.

These recurrences also cover the addition/product/ReLU implementation of attention and its fixed masks or length normalization. Apply them to the actual trainable attention matrices and their scalar expansion, not merely to the ideal arithmetic gate identities at the comparator. Finally take `La=sqrt(sum_i L_ai^2)` and `Lv=L_vout` after the fixed output clips. Every number is explicitly calculable from the costed compiler, input radius, `W`, and `e`; fixed structural coefficients use their known magnitudes even if they exceed `W`. The strictly positive normalization floor is required for this full-box argument; exact normalization at the comparator alone would not control arbitrary trained parameters.

## 6. The completed theorem for the specified-prior interpretation

Combining the checked compiler with the statistical proof above establishes the following specified-prior theorem, with no bounded-label repair:

> Fix a known finite-rank polynomial GP on a compact raw domain, positive observation-noise variance, and a maximum context length `n`. In the explicitly compiled residual ReLU-attention architecture with one full-token LayerNorm feed-forward stage, structural source cancellation, fixed positions, and exact raw-label readout, the bounds (4.5) give a finite network representing the noisy posterior predictive exactly. This is uniform over all context/query covariates, repeated designs, all lengths at most `n`, and every real context-label vector. For any design distribution independent of the GP/noises, full-box approximate ERM over the larger non-singleton structured coefficient class satisfies (5.9) and the sample bound (5.10), and hence converges to Bayes in prior-averaged forward KL.

The representational error is zero, so it is below every positive requested epsilon. Exact representation removes the label-amplification obstruction. The capacity can be enlarged using genuine additional trainable coefficient blocks while preserving the exact comparator; choose sample sizes so the explicit right side of (5.9) tends to zero. There is no claim that arbitrary uncontrolled growth of parameter count relative to data is consistent. With summable failure probabilities, the same bounds give almost-sure risk convergence along the chosen sequence by Borel–Cantelli.

This does **not** say that every finite-sample trained network has finite worst-label KL. Typical coefficient errors still produce infinite worst-label KL by Section 2. Even coefficient convergence to zero does not imply convergence of that supremum. The quantified representation theorem and the quantified prior-average learning theorem are separate parts of the result, matching the expressivity-versus-pretraining distinction rather than concealing it.

If one instead interprets the registry as demanding a finite-sample uniform-all-label guarantee for the *learned* network itself, this completion target is insufficient. One would need exact recovery of the entire coefficient map or additional structural restrictions; ordinary approximate ERM does not supply that. No such stronger closure should be claimed.

## 7. Current disposition

The original A02/A05 pair cannot be promoted to the literal all-label representation theorem. Exact label-linearity alone does not fix it. A finite-domain lookup prior or a constant-kernel prior would be valid special cases but would avoid the substantive continuous-design denominator problem; they are unnecessary because the finite-rank polynomial route addresses it directly.

The sum-of-squares normalization mechanism is algebraically valid; the complete compiler and every count used in (4.5) have now been read and independently checked; and Section 5 proves a nontrivial statistical theorem for its larger structured trainable class. I accept the resulting **specified finite-rank polynomial GP theorem**, with exact all-real-label representation and prior-averaged ERM learning as separate quantified conclusions. It is a substantive completion of this specified-prior interpretation of T336, rather than a promotion of the earlier bounded-label theorem or a finite-domain/constant-prior shortcut.

This acceptance does not establish literature novelty, efficient training, SGD convergence, standard-softmax-transformer realization, RBF all-label representation, arbitrary-prior approximation, learned uniform-all-label convergence, or an official solved-row count. If any of those stronger interpretations is intended, the accepted theorem does not settle it.

The exact final compiler snapshot read for this integration is:

| Reviewed file | SHA-256 |
|---|---|
| `followup/T336_architecture_compiler.md` | `8dbb67bbc8609cb86b0a1fb888f61c64abf36b07c8ebfc0464b0d0e5a4adf175` |
| `followup/T336_unbounded_label_independent.md` | `82ebfbbee8cca6d7f8ac1a797b5f605e7e25507bdffdd6d3b51f9a3a25ef4f44` |

I read the final compiler's larger freely trainable arithmetic/feature class and its explicit bias witness, verified that biases use existing coefficient affine offsets, and checked the resulting `S+6` clipped depth and stored-weight count. Section 5's statistical argument was additionally checked independently by A27 and the coordinator; those checks are internal collaboration, not external peer review. Future edits to the pinned compiler are not silently covered by this acceptance.

No frozen campaign file was modified by this follow-up. No remote save or final packaging step is certified here.
