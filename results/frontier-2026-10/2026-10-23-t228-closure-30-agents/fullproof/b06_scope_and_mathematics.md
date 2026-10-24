# B06: strict completion audit and independent mathematical investigation

24 October 2026. Independent reviewer: B06. The registry and earlier campaign files were read without modification. T353 and T228 are excluded as new candidates. This report does not assign a solved count or certify publication novelty.

## 1. Decision

The earlier scope audit's existential counting rule is not the rule authorized by the present task. A categorical disjoint-support random-feature model cannot now be counted as the full T357 target, and a finite-rank polynomial GP cannot be counted as the full ordinary-GP/RBF T336 target. Their proved theorems remain useful, but changing the label on them does not enlarge their quantifiers.

The following mathematical findings are substantive:

1. **T336, raw-input RBF:** a finite arithmetic/ReLU/LayerNorm circuit, even with rational or natural-parameter Gaussian decoding, has infinite worst-case forward KL over real context labels. Section 4 gives a new self-contained algebraic obstruction already for one observation. This is stronger than the earlier polynomial-only obstruction and directly blocks extending the polynomial-GP normalization compiler to exact RBF coefficients.
2. **T336, ordinary normalized transformers:** a fully pre-LN transformer with affine embeddings and affine output has a design-independent asymptotic label slope; a post-LN/final-LN Gaussian mean is bounded. Both fail the RBF all-label target. A separate finite-mixture-head argument covers the fixed-bin Riemann output family used in the PFN paper, independent of the transformer body.
3. **T321:** the actual empirical Gaussian phase-retrieval loss, at a fixed linear measurement ratio, supports a complete negative Poincare/LSI conclusion and a genuine discrete MALA mixing lower bound. I independently checked B01's data event, partition comparison, constants, and lower-bound proof. Root's additional truncated-MALA minorization gives a quantitative upper time bound with explicit truncation error. This stays within a model expressly named in the row; it does not substitute a toy double well.
4. **T355:** a quantitative theorem for the whole compact normally attracting minimizer-manifold class is substantially broader than one solvable example. However, uniform comparison of the raw iterates from time zero with a manifold-valued limit requires an on-manifold/vanishing-distance start or an explicit initial-layer term. This is a mathematical necessity. The parent has acknowledged it.
5. **T357, final Gaussian continuation:** the new finite-time AMP computation, model-conditional TV theorem, uniform-time GD geometry, and strict scalar overconfidence argument now address every mathematical clause of the explicit Gaussian random-feature branch, with the ratio and step restrictions stated in Section 8 below. This is a substantial change from the older first-step/categorical record. It is still not evidence that a previously recognized, still-open published conjecture has been newly solved.

None of the relevant registry rows checked here is itself a verbatim numbered conjecture in its cited paper. The exact original row and the published source must remain separate objects. A complete proof of a row's explicit fixed-model formulation is not automatically a solution of a previously open published conjecture.

## 2. What completion must mean

There are two independent tests, and both must pass before saying that a new published open problem has been solved.

**Statement test.** Pin the exact registry row, its version, and the exact source passage. Preserve the model, data law, quantifiers, limits, output functional, algorithm and initialization. If a row expressly offers an alternative, such as phase retrieval *or* a planted network, choosing one offered branch is legitimate. Replacing a continuous dense design by categorical indicators, or an infinite-rank kernel by a polynomial feature map, changes the problem when the user has expressly rejected that substitution. Every conjunct of the chosen statement needs a theorem, a counterexample to the precise assertion, or a clearly stated remaining gap.

**Status test.** Establish what the source actually asks and whether subsequent literature already answers it. An unverified registry flag, an unpublished local audit, or failure to find a theorem in a few searches is not evidence of current openness. A research programme can be advanced without becoming a solved published conjecture.

The strict operational checklist is:

| Obligation | Pass criterion |
|---|---|
| Target identity | Exact row and source location, with a statement of any difference between them |
| Model preservation | The asserted theorem treats the intended law and architecture, or an alternative explicitly offered in the original row |
| Quantifiers | No change from all datasets to typical datasets, all relevant times to one time, uniform KL to expected KL, or a full class to one selected instance |
| Algorithm | Actual updates, normalization, step-size scale, decoder and initialization specified |
| Asymptotic transfer | Limit-law conclusions transferred to the requested finite-model statistic in the requested probability mode |
| Every requested clause | Representation, learning, trajectory/stopping, or mixing/discretization clauses all checked separately |
| Proof audit | No unproved uniformity, stability, concentration, compactness, or interchange-of-limits step |
| Published status | Source claim verified and sufficiently close later results compared; novelty uncertainty disclosed |

An impossibility theorem can settle a false affirmative assertion. It must concern the full intended class. A no-go theorem for one restricted implementation does not rule out another architecture that the statement allows.

### Source reconciliation

The following primary texts were opened independently during this audit:

- [Muller et al., *Transformers Can Do Bayesian Inference*, arXiv:2112.10510v7](https://arxiv.org/html/2112.10510v7), Sections 3--4 and 8. Corollary 1.1 identifies the training objective with **prior-averaged** forward KL. The paper describes simple linear input projections and a fixed-bin distribution head with fixed tail components. Its future-work section does not state the registry's all-dataset size/sample-complexity conjecture.
- [Bai et al., arXiv:2102.07856v2](https://arxiv.org/html/2102.07856v2), Sections 2--3 and 7. The source establishes score-conditional logistic-regression overconfidence and raises nonlinear calibration/training as future directions. It does not pin the categorical construction, the Gaussian random-feature trajectory, or a numbered neural-GD conjecture matching T357.
- [Raginsky--Rakhlin--Telgarsky, arXiv:1702.03849v3](https://arxiv.org/html/1702.03849v3), Sections 2 and 4. Their algorithm is unadjusted stochastic-gradient Langevin, their theorem assumes globally Lipschitz gradients, and the discussion already identifies multiwell inverse-temperature bottlenecks. It asks for structurally favorable settings with small inverse gaps; it does not formulate the registry's precise empirical phase-retrieval statement.
- [Li--Wang--Arora, arXiv:2110.06914v4](https://arxiv.org/html/2110.06914v4), Theorem 4.6 and Appendix B. The source supplies a qualitative slow-time limit. The row's explicit uniform power-rate request is a further quantitative problem.

These source summaries are deliberately short; the proofs below are independent calculations, not reproductions of those papers.

## 3. Strict T336 and T357 obligation maps

### T336

The exact registry request asks for transformer size for posterior-predictive approximation in KL **uniformly over datasets of size N**, a number of prior-sampled pretraining datasets, and convergence to Bayes prediction as both grow. The full ordinary RBF target needs at least:

| Clause | Required for the full target | Existing result |
|---|---|---|
| Prior | Fixed ordinary RBF GP on a nontrivial compact raw-input domain, with fixed positive noise and specified kernel hyperparameters | Polynomial finite-rank GP is a different prior |
| Representation | All covariate configurations, including repeats, and every real label vector | Earlier continuous-kernel theorem has a label bound; exact compiler covers polynomial features |
| KL | Direction fixed; every output distribution properly normalized | Existing follow-up uses forward Gaussian KL |
| Architecture | Allowed primitives, normalization placement, label path and decoder counted explicitly | Earlier exact implementation is a custom LN-augmented unnormalized ReLU-attention compiler |
| Size | Explicit dependence on N, dimension, noise, kernel parameters and epsilon | Finite-rank counts do not establish RBF counts |
| Learning | A genuinely varying class and a stated statistical/optimization rule with finite sample count | Structured ERM result is prior-averaged, with an exact comparator only for the polynomial prior |
| Convergence | Stated topology and probability mode, with a single sequence satisfying representation and learning guarantees | Average-risk convergence cannot be relabeled all-label uniform convergence |

No optimization theorem for SGD is required merely because the row says “pretrained”; a legitimate ERM theorem can answer a statistical sample-complexity request if that is explicitly declared. But an oracle pretraining rule must not be presented as an SGD convergence theorem. Likewise the original row does not explicitly require learned convergence uniformly in labels. It does explicitly require that uniformity in the representation clause.

### T357

The categorical construction has a complete count-state recurrence and strong stopping statements *for that categorical model*. Under the user's current full-scope requirement it is excluded as the completion target. For the Gaussian-input, Gaussian-feature single-index version the completion checklist is:

1. Actual two-layer/random-feature cross-entropy GD, with its initialization and step normalization.
2. Proportional sample and width limits, with an exact limiting population law across the needed training times.
3. The requested population score-calibration curve or error, conditional on the trained predictor, not merely an annealed one-test joint law.
4. A signed overconfidence conclusion in an identified nonempty regime. Positive absolute calibration error alone does not establish overconfidence.
5. A nonvacuous early-stopping conclusion tied to a risk or accuracy requirement, with the necessary uniformity if stopping times depend on dimension or data.
6. Current-source and novelty comparison.

The older Gaussian first-step theorem verifies a joint and replica limit, population risk convergence, and high-probability positive lower bounds on calibration error. On its own it does **not** establish convergence of finite-network unbinned calibration error, an arbitrary-time GD trajectory, or a stopping theorem. Weak convergence of test laws does not make conditional regression or unbinned calibration continuous. The existing independent review explicitly states these boundaries; the earlier categorical scope certificate cannot fill the Gaussian gaps. The new B04 total-variation theorem closes the first-step calibration-convergence gap; the updates in Section 7 below distinguish this new result from the older theorem.

## 4. New T336 theorem: raw-input RBF defeats finite algebraic mean computation

This theorem is already about an ordinary infinite-rank kernel. No finite-rank or categorical replacement is made.

Fix a lengthscale ell>0, noise variance s>0, and the RBF kernel

\[
k(t,u)=\exp\{- (t-u)^2/(2\ell^2)\}
\]

on a compact interval containing zero and a nonempty interval I of possible query points. Use one context observation at zero with arbitrary real label y. The noisy query posterior is

\[
P_{t,y}=N(a(t)y,v(t)),\qquad
a(t)=\frac{e^{-ct^2}}{1+s},\quad
v(t)=1+s-\frac{e^{-2ct^2}}{1+s},\quad
c=\frac1{2\ell^2}.
\tag{R1}
\]

In particular 0<v(t)<=1+s. Consider any predictor

\[
Q_{t,y}=N(m(t,y),w(t,y)),\qquad 0<w(t,y)<\infty.
\]

The variance may be any positive function; it need not be algebraic or label independent.

### 4.1 Finite uniform KL forces exact asymptotic slopes

For target variance v and mean error e, direct minimization over the predicted variance gives

\[
\inf_{w>0}D_{KL}(N(m_0,v)\Vert N(m_0+e,w))
=\frac12\log(1+e^2/v).
\tag{R2}
\]

The minimizing variance is v+e^2. Therefore a finite uniform KL bound K would force

\[
|m(t,y)-a(t)y|\le \sqrt{(1+s)(e^{2K}-1)}
\tag{R3}
\]

for all t in I and all real y. In particular,

\[
\lim_{y\to+\infty}\frac{m(t,y)}y=a(t)
\quad\hbox{for every }t\in I.
\tag{R4}
\]

This is why ordinary kernel approximation, a small inverse-matrix error, or a very high polynomial degree cannot meet this quantifier. A nonzero coefficient error is multiplied by arbitrarily large labels.

### 4.2 Algebraic-circuit lemma

Suppose m is computed by a fixed finite circuit from t,y and fixed real constants, using arithmetic operations, division wherever defined, square roots wherever defined, and ReLU or other finite selections among such algebraic expressions. Then there is a nonzero polynomial

\[
P(t,y,u)\in\mathbb R[t,y,u]
\quad\hbox{such that}\quad P(t,y,m(t,y))=0.
\tag{R5}
\]

One elementary justification is algebraic elimination. The inputs lie in the rational-function field R(t,y). Adding, multiplying or dividing finitely many elements algebraic over that field, or adjoining square roots, keeps a finite algebraic extension. Each choice of the finitely many ReLU branches therefore has an annihilating polynomial; multiply these nonzero polynomials and clear denominators. Continuity gives the identity at any exceptional input where a cleared denominator vanishes but the implemented circuit remains defined. ReLU itself introduces no transcendental operation: its output selects the previous output or zero. Ordinary LayerNorm with positive epsilon consists entirely of these permitted operations. Rational Gaussian decoding, including mean = information/precision, is permitted too.

More generally, the theorem below only needs (R5), so any other implementation satisfying a polynomial identity is covered without discussing its gates.

### 4.3 The obstruction

**Theorem.** If (R5) holds, then

\[
\sup_{t\in I,\,y\in\mathbb R}D_{KL}(P_{t,y}\Vert Q_{t,y})=\infty.
\tag{R6}
\]

**Proof.** Suppose the supremum were finite. Substitute u=yz into P and write

\[
P(t,y,yz)=\sum_{j=0}^M y^j Q_j(t,z),\qquad Q_M\not\equiv0.
\]

The substituted polynomial is nonzero: the substitution u=yz is injective into the polynomial ring, or invertible after adjoining 1/y. Divide its value at z=m(t,y)/y by y^M and let y tend to positive infinity. By (R4) the lower-order terms vanish, and

\[
Q_M(t,a(t))=0\quad(t\in I).
\tag{R7}
\]

It remains to show that a(t)=C exp(-ct^2), C=(1+s)^-1, satisfies no such nonzero polynomial identity on an interval. Write a putative identity as

\[
\sum_{j=0}^J p_j(t)C^j e^{-jct^2}=0.
\]

Each side is real analytic on all of R; equality on I implies equality on R. Let j0 be the least index for which p_j is a nonzero polynomial. Dividing by C^j0 exp(-j0 ct^2) gives

\[
p_{j_0}(t)+\sum_{j>j_0}p_j(t)C^{j-j_0}e^{-(j-j_0)ct^2}=0.
\]

Every term in the sum tends to zero as t tends to positive infinity. Hence the nonzero polynomial p_j0(t) would tend to zero, which is impossible. This contradicts (R7) and proves (R6). Square.

**Architecture consequence.** Finite unnormalized arithmetic attention with ReLU, the one-LayerNorm reciprocal compiler in the earlier follow-up, extra square-root/division gates, and a rational/natural-parameter Gaussian head cannot meet the all-label RBF requirement from raw coordinates. The old natural-parameter escape from the rank-one polynomial obstruction is now included and fails because the needed coefficient is transcendental.

**Limits.** Softmax, sigmoid, tanh and GELU are not algebraic gates. Exact externally supplied RBF features also violate the raw algebraic-input hypothesis. Thus this is not a no-go theorem for all conceivable transformers. Infinite rank alone is not a computational impossibility: for fixed context length only finitely many kernel entries and a finite matrix inverse are needed if suitable exact nonalgebraic primitives are supplied. No exact general-softmax construction or universal softmax impossibility is established here.

## 5. Two other exact T336 no-go results

### 5.1 Ordinary full pre-LN and post-LN label paths

Let the token count, width, depth and weights be finite. Suppose input embeddings are affine in raw design and labels; the design lies in a compact set; every pre-LN residual update has the form

\[
H_{l+1}=H_l+F_l(\operatorname{LN}_{\varepsilon}(H_l)),
\qquad\varepsilon>0,
\]

and F_l is continuous on the compact closure of the bounded normalized token range. Standard finite softmax attention and continuous feedforward blocks satisfy this bounded-input condition. Therefore each residual increment is uniformly bounded independently of the labels, and

\[
H_L=H_0+O(1).
\]

An affine Gaussian mean readout has m(Z,y)=b^T y+O(1), where b is fixed by the affine input and readout maps and is independent of the design Z. A query-only readout with a label-free query has b=0. A final LayerNorm, or ordinary post-LN stack without an unnormalized bypass, makes the mean bounded directly.

For RBF N=1, the exact coefficient a(t) in (R1) is nonconstant on a suitable interval. Choose t with a(t) != b. Then the mean error diverges linearly with y, and (R2) gives infinite worst-case forward KL even if the predicted variance is unrestricted. Thus adding ordinary softmax to an otherwise fully normalized stack does not defeat this obstruction. An unnormalized label value path or multiplicative external decoder changes the hypothesis and must be stated.

### 5.2 Finite fixed-component distribution heads

This version does not assume a Gaussian output. Fix any finite family of probability densities r_1,...,r_J, and permit arbitrary context-dependent mixing weights:

\[
q_y(z)=\sum_{j=1}^J w_j(y)r_j(z),\qquad w_j(y)\ge0,\quad\sum_jw_j(y)=1.
\]

At a fixed nondegenerate GP design let the target be P_y=N(ay,v) with a != 0 and v>0. Fix c0>0 and set A_y=[ay-c0,ay+c0]. Its target probability p0=P_y(A_y) is independent of y and lies strictly between zero and one. Integrability of each r_j gives

\[
q_y(A_y)\le\sum_{j=1}^J\int_{A_y}r_j(z)\,dz\longrightarrow0
\quad (|y|\to\infty).
\]

Binary data processing now yields

\[
D_{KL}(P_y\Vert Q_y)
\ge p_0\log\frac{p_0}{q_y(A_y)}
 +(1-p_0)\log\frac{1-p_0}{1-q_y(A_y)}\longrightarrow\infty.
\]

This applies to a fixed finite histogram/Riemann decoder with fixed bin endpoints and fixed tail components, regardless of the power of the transformer body. Dynamic location/scale or other context-dependent components escape the theorem. The PFN paper's average-risk objective is not contradicted: tail labels are rare under the prior, while this result is worst-case over every real label.

### 5.3 Learning does not undo a representation impossibility

If each finite architecture in a sequence has infinite all-label worst-case KL, increasing sample size or architectural size cannot produce the required finite epsilon uniform representation at any finite stage. A prior-averaged learning theorem may nevertheless hold, and ordinary compact-label approximation may be excellent. These are different claims.

For a label-linear learned class, uniform-all-label finite KL furthermore requires exact posterior slopes after learning. Finite statistical coefficient error is not enough. The original row does not explicitly require that stronger uniform topology for the learned convergence clause, but it cannot be inserted into a proof by calling average KL “generalization.”

## 6. Independent T321 proof audit

The following audit refers to B01's `fullproof/b01_target_triage.md`, read in full on 24 October 2026 and re-read after the convexification, necessary-temperature and arbitrary-accuracy truncated-MALA sections were added. The accepted exact version is pinned in Section 9. This certificate does not automatically cover later edits.

### 6.1 Model and event

The model is the actual empirical loss

\[
L(x)=\frac1{4m}\sum_{i=1}^m\big((a_i^T x)^2-(a_i^T v)^2\big)^2,
\quad a_i\stackrel{iid}{\sim}N(0,I_d),\quad\|v\|=1.
\]

B01 takes m=10^6 d and d>=100. Its four-halfspace growth bound and conservative VC deviation exponent m/512 establish, simultaneously for all p,q,

\[
\frac1m\sum_i(a_i^Tp)^2(a_i^Tq)^2
\ge\frac1{1024}\|p\|^2\|q\|^2.
\]

I checked the probability arithmetic. The covariance-net bound ||m^-1 sum a_i a_i^T||op<=2 and max_i ||a_i||^2<=4d imply

\[
A=\frac1m\sum_i(a_i^Tv)^2\|a_i\|^2\le8d,
\qquad B=\frac1m\sum_i\|a_i\|^4\le8d^2.
\]

The total exceptional probability is bounded by 10 exp(-d/2). No uniform dimension-free quartic upper bound is used; such a bound would be false at fixed sampling ratio.

### 6.2 Partition function, temperature and barrier

Put a=1/4096 and D(x)=||x-v||^2||x+v||^2. The event gives L>=aD. Since D is at least the squared distance to {v,-v},

\[
Z_\gamma\le2(\pi/(a\gamma))^{d/2}.
\]

For q_beta=N(v,I/beta), direct Gaussian moments give beta E_q L=A+3B/(4beta)<=14d when beta>=d. Jensen and Gaussian entropy give

\[
Z_\beta\ge (2\pi/\beta)^{d/2}e^{-14d}.
\]

Thus, with H=14+(1/2)log(1/a),

\[
\pi_\beta(L\ge u)\le2e^{Hd-\beta u/2}.
\]

At beta=(2/epsilon)(Hd+log(2/delta)), the near-minimizer probability is at least 1-delta. On |v^T x|<=1/2 one has D>=(1-(v^Tx)^2)^2>=9/16, so the barrier height is b=9a/16. For epsilon<=b/2, its Gibbs mass is at most 2 exp(-beta b/4). The clipped odd sign test has variance at least one minus that mass and energy at most four times that mass, proving

\[
C_P\ge\frac1{16}e^{\beta b/4}.
\]

The same lower bound applies to the log-Sobolev constant under the convention Ent(f^2)<=2C_LS integral ||grad f||^2. The relaxation time of the physical generator beta^-1 Delta-grad L dot grad is beta C_P; omitting beta would mix conventions.

### 6.2a Existence and explicit finite upper bounds for both inequalities

The final B01 version also proves that both constants are finite. This is needed to answer the row's separate log-Sobolev question, rather than merely saying that any putative LSI constant would be large.

The small-ball event implies

\[
\nabla^2L(x)\succeq(c_0\|x\|^2-8d)I,
\qquad c_0=3/1024.
\]

Let A0=4d+1/2 and R0^2=(8d+12A0+1)/c0. The piecewise function h in B01 Section 4a satisfies h(s)=s on [0,1], h(s)=3/2 on [2,infinity), h'>=0, and h''>=-3/2. Its values and first two derivatives match at both joins; in the transition interval, h'=1-3t^2+2t^3 and h''=-6t(1-t), t=s-1. Therefore u(x)=A0 R0^2 h(||x||^2/R0^2) is C^2 and bounded between zero and 3A0 R0^2/2. Its Hessian is 2A0 I in the inner ball, is at least -12A0 I in the annulus, and is zero outside. The specified R0 makes the Hessian of L+u at least I in all three regions.

Bakry--Emery applied to beta(L+u), followed by the Holley--Stroock bounded-perturbation inequality, gives

\[
C_P(\pi_\beta)\le C_{LS}(\pi_\beta)
\le\beta^{-1}\exp(3\beta A_0R_0^2/2)<\infty.
\]

I independently opened [Menz--Schlichting, arXiv:1202.1510v4](https://arxiv.org/pdf/1202.1510), Theorems 3.1--3.2, and checked the normalization. The C^2 convexification suffices for these criteria. The upper and lower exponential rates are not matching: the upper exponent is O(beta d^2), the lower exponent is Omega(beta). No matching-rate claim is accepted.

### 6.3 A necessary-temperature supplement

The low-energy region lies in two balls of radius sqrt(epsilon/a). Combining its volume with the preceding partition lower bound and vol(B_1)<= (2 pi e/d)^(d/2) gives, for beta>=d,

\[
\pi_\beta(L\le\epsilon)
\le2\left(\frac{e^{29}\beta\epsilon}{ad}\right)^{d/2}.
\tag{T1}
\]

For beta<d use q=N(v,I/d) in the same Jensen argument. The identical bound holds with beta/d replaced by one. Consequently, if epsilon is sufficiently small that 2(e^29 epsilon/a)^(d/2)<1-delta, concentration with probability 1-delta forces beta>=d; then (T1) forces

\[
\beta\ge\frac{ae^{-29}d}{\epsilon}
\left(\frac{1-\delta}{2}\right)^{2/d}.
\tag{T2}
\]

This supplies a necessary scale rather than only a deliberately cold sufficient schedule. The constants and resulting small-epsilon range are extremely conservative and must remain visible. It is not legitimate to extend (T2) beyond that range without a sharper proof.

The final B01 specialization is correct: c_star=a exp(-29)/16 and epsilon_star=min(c_star,c_star b/(4H)). If epsilon<=epsilon_star and any beta gives low-energy probability at least 3/4, then beta>=c_star d/epsilon. The beta<d argument and the hypothetical beta<c_star d/epsilon each bound the probability by 2(1/16)^(d/2)<3/4. The additional restriction epsilon<=c_star b/(4H) implies Hd<=beta b/4 and hence

\[
C_P(\pi_\beta)\ge\frac1{16}
\exp\{c_\star b d/(4\epsilon)\}.
\]

Thus for every sufficiently small fixed tolerance the exponential obstruction applies to every sufficiently concentrating Gibbs temperature, not just the selected sufficient temperature.

### 6.4 Actual discrete lower bound

On ||x||<=2, ||grad L(x)||<=(2^3+2)B<=80d^2. For h<=1/(320d^2), a Langevin proposal from v^T x>=1/2 in this ball has projected mean at least 1/4 and crossing probability at most exp(-beta/(64h)). A Metropolis rejection cannot create a crossing. Separating the barrier strip and the outside-ball tail therefore bounds stationary sign flow by 5 exp(-beta b/4).

The initial law pi_beta conditioned on v^T x>0 is 2-warm. Invariance preserves that density upper bound. A union bound on sign crossings gives

\[
\|\mu_0P_h^k-\pi_\beta\|_{TV}
\ge\frac12-10k e^{-\beta b/4}.
\]

This is a rigorous theorem about discrete MALA. It does not rely on a diffusion approximation or on a false transfer of the diffusion Poincare constant into a MALA upper bound.

### 6.5 Quantitative upper bound with truncated MALA

Let K=B(0,2); use the same Langevin proposal, reject proposals outside K, and use the ordinary Metropolis ratio inside K. The invariant law is exactly pi_K=pi_beta(.|K). Let

\[
G=80d^2,\qquad L_{max}=50d^2,\qquad
q_{min}=\left(\frac\beta{4\pi h}\right)^{d/2}
\exp\left\{-\frac{289\beta}{64h}\right\}.
\]

These constants follow from ||y-x+h grad L(x)||<=4+hG<=17/4 for x,y in K. The off-diagonal accepted density is

\[
\min\{q_h(x,y),e^{-\beta(L(y)-L(x))}q_h(y,x)\}
\ge q_{min}e^{-\beta L_{max}}.
\]

Writing v_K=vol(K), the kernel therefore minorizes epsilon_K times the uniform probability on K, where

\[
\epsilon_K=v_K q_{min}e^{-50\beta d^2}>0.
\]

Since this is a genuine lower bound on a probability kernel, epsilon_K<=1. The common minorization yields, from every initial law supported on K,

\[
\|\mu P_{h,K}^k-\pi_\beta\|_{TV}
\le (1-\epsilon_K)^k+\pi_\beta(K^c)
\le e^{-k\epsilon_K}+2e^{Hd-9a\beta/2}.
\tag{T3}
\]

Equation (T3) is the fixed-radius instance. The final B01 proof correctly improves this to arbitrary requested accuracy zeta **without changing beta or the target**. Set

\[
R=\max\left\{2,\sqrt{1+\sqrt{\frac{2}{a\beta}
                 (Hd+\log(4/\zeta))}}\right\}.
\]

Then pi_beta(||x||>R)<=zeta/2 because L>=a(||x||^2-1)^2. On K=B(0,R), take

\[
M_R=2d^2(R^2+1)^2,\qquad G_R=8d^2(R^3+R),
\]

and

\[
q_{min,R}=\left(\frac\beta{4\pi h}\right)^{d/2}
e^{-\beta(2R+hG_R)^2/(4h)},\qquad
\eta_K=v_dR^d e^{-\beta M_R}q_{min,R}.
\]

The same accepted-density argument gives a valid minorization for every h>0; choosing h<=1/(4G_R) also respects the small-step bottleneck regime. From every initial law in K, including the deterministic start at zero,

\[
k\ge\eta_K^{-1}\log(2/\zeta)
\quad\Longrightarrow\quad
\|\mu P_{h,K}^k-\pi_\beta\|_{TV}\le\zeta.
\]

This is the correct all-accuracy upper time bound. The target differs only by the quantified truncation mass; invariant-distribution step-size bias within K is exactly zero by Metropolis correction. No claim of pathwise closeness to the diffusion is needed for this direct sampling guarantee. For R=2 the same truncated chain also has the checked exponential lower bound from its own positive-sign conditional Gibbs start: its strip mass is at most twice the full-target strip mass, and no outside-ball term is needed.

The row says “discretized Langevin dynamics” without prescribing ULA. An expressly named truncated MALA algorithm is a defensible implementation of that clause. Its acceptance ratio and truncation must be in the theorem statement. It must never be called the source's ULA/SGLD algorithm or presented as a ULA error estimate.

### 6.6 What this would and would not complete

Together, the finite-sample data event, concentration, functional-inequality lower bounds, discrete lower bound, and (T3) discharge the mathematical clauses of the row's expressly offered **phase-retrieval branch**, for the stated sampling ratio, epsilon range and MALA choice. This is materially different from retroactively counting one artificial categorical model: phase retrieval is written in the row itself.

The negative mechanism is the two signs in raw parameter space. It says nothing about efficiently finding either minimizer, sampling on the sign quotient, an algorithm allowed global sign flips, or the planted-network alternative. A conditional-Gibbs lower-bound start is stated rather than computationally generated; the upper bound works from every start in K. The upper bound is deliberately enormous, not a sharp metastability estimate.

The source already anticipates the general mechanism. The exact Gaussian empirical theorem may be a useful explicit result, but its publication novelty remains unverified. This report does not certify “a previously open published conjecture solved.”

## 7. Additional candidate checks

### T355: initial layer and rates

Suppose the limiting X_t lies on a minimizer manifold M and X_0=Phi(theta_0). If theta_0 is a fixed point a positive distance from M, the requested sup over k including zero cannot tend to zero for all smooth test functions. Choose a smooth bounded function that agrees with squared distance to M in a small tube containing theta_0. Then f(theta_0)>0 but f(X_0)=0. This is a direct obstruction to a uniform raw-iterate error bound from an arbitrary basin start.

A valid theorem can instead give an initial-layer term of the form C dist(theta_0,M) exp(-lambda k eta), compare projected observables, assume dist(theta_0,M)=O(sqrt(eta)), or retain a deterministic fast transient. On-manifold initialization is particularly clear. The parent is pursuing the full compact normally attracting manifold class with this distinction explicit, which is a legitimate broad theorem rather than an isolated toy example.

Relevant primary comparisons opened here are [*Singular-limit analysis of gradient descent with noise injection*, arXiv:2404.12293](https://arxiv.org/html/2404.12293), which explicitly corrects the initial jump and gives qualitative convergence, and [Gess--Kassing--Rana, arXiv:2402.03467v2](https://arxiv.org/abs/2402.03467), which proves weak rates for intrinsically Riemannian/retracted SGD. The latter must be distinguished from ambient SGD attracted to M. The ICLR 2024 momentum paper's slow-time Theorem 4.5 also gives qualitative limits. These observations do not establish novelty of the proposed quantitative theorem.

### T352: complete fixed-parameter obstruction, unresolved original-status claim

B02's `fullproof/b02_target_triage.md` proves a time-uniform fixed-order Renyi bound C_alpha/n^2 for compact-state, bounded-gradient, fresh-minibatch noisy SGD, when diameter, gradient bound, state-noise level and step are fixed in n. I checked the main bridge: Gaussian Dobrushin contraction gives state TV=O(1/n); Gaussian final-step smoothing controls the weighted L^r norm of the density difference by O(1/n); the zero first-order term in an integer-power expansion gives Renyi O(1/n^2). The derivative tilt is centered at r a+(1-r)c, so its displacement from a is (r-1)(a-c), matching B02's constant.

This rules out a positive n-independent plateau under those fixed-parameter quantifiers. Its constants may be exponentially bad in diameter/noise, so it is not a sharp all-parameter convex-rate theorem. B02 found existing nonconvex privacy results and explicitly declined to count a new full original-row/open-problem closure. That restraint is justified.

### Other triage candidates

B01 identifies T318 random-feature posterior tempering as close to existing proportional Bayesian-uncertainty work, and T268 width-independent sample complexity as already opposed by known spectral-norm fat-shattering lower bounds. Neither currently offers a cleared new published-conjecture target. T353 and T228 remain excluded from a new count.

### New T357 finite-horizon lemmas: independent B03 audit

After the preceding scope assessment, I read B03's complete `fullproof/b03_gaussian_dynamics.md`. For the version pinned below, **Sections 1--6 and 8 pass this independent mathematical audit**. The acceptance is specifically for fixed finite horizons, with all stated step-size and nondegeneracy restrictions retained.

- The recursion uses the correct raw-readout coefficient b=a/sqrt(m) and lambda_d=cd/n. The operator norm estimate uses conditional Gaussian concentration and two sphere nets, not entrywise boundedness alone.
- Removing one feature makes the corresponding residual independent of that feature conditional on data and the remaining features. Its Gaussian Lipschitz bound is O(sqrt(d)). The leave-one-feature score difference is O_P(sqrt(log d)) for fixed horizon. This yields the claimed O_P(sqrt(log d/d)) coordinate bound despite training-sample reuse.
- For any fixed linear combination of test scores, the gradient is bounded and the Hessian operator norm tends to zero. The Ornstein--Uhlenbeck integration-by-parts argument gives the displayed characteristic-function bound without requiring nonsingular variance. Tight covariance matrices and a sequential argument justify a matched-Gaussian approximation with realized-network covariance.
- The first-step coefficient norm has the exact form lambda_d^2 m^-1 R^T K R. Conditional Bernoulli noise supplies the positive lower limit c^2 v rho_beta/(alpha gamma). Under lambda_d ||K||op<=4, logistic convexity plus descent gives ||b^t||>=||b^1||/2 for every positive iterate. This is a lower bound only; the fixed-horizon upper and delocalization bounds are not thereby made uniform over all times.
- In the teacher-coordinate decomposition, the Taylor remainder has Frobenius norm O_P(1). The centered derivative-feature matrix has norm O_P(sqrt(d)); its mean correction has the same order. The extreme teacher coordinates contribute O_P(log d/sqrt(d)) after feature normalization. Hence the normalized feature remainder is operator-small as claimed, and finite-step logistic stability transfers it.

Section 7 correctly does **not** claim a completed state-evolution theorem. The subsequently added Section 8 closes its matrix conditions: operator clipping gives a globally O(d^(-1/2))-Lipschitz map from the base Gaussian arrays; fixed polynomial matrix entries inherit that bound. Signed-permutation symmetry determines their means. Gaussian concentration, a union bound and Borel--Cantelli give the simultaneous entrywise polynomial bounds required by Wang--Zhong--Fan Proposition D.1(b). The Hermite covariance estimate converges in operator norm, and the inspected Louart--Liao--Couillet Theorems 1--2 apply after conditioning on the features. The fixed-point law is unique by the increasing-versus-decreasing rearrangement stated in the report. Bi-orthogonal invariance of the Gaussian surrogate then identifies the limiting diagonal distribution. I checked the cited source definitions and hypotheses rather than inferring dynamics from spectral matching alone.

One cross-dimension precision was required and has been incorporated: the almost-sure conditional source application uses a product construction with the complete data-array sequence independent of the complete feature-array sequence. This resolves conditioning on a feature sequence that could otherwise encode data from a different dimension. The final in-probability conclusions depend only on per-dimension laws and therefore incur no restriction. At the point of that matrix audit, the AMP embedding, nonlinear iteration transfer and deterministic test-path overlap computation were separate proof obligations. The subsequent accepted composition is recorded below; the matrix lemma alone did not settle them.

B04's separate TV transfer theorem, independently audited by B02, closes the earlier first-step exact-calibration gap. Combining the new structural and transfer results can also give fixed-horizon matched-covariance calibration proxies and qualitative positive calibration gaps in the stated nondegenerate small-step regime. These are real advances beyond the old first-step lower bounds. Those structural/TV lemmas alone do not supply a deterministic calibration trajectory or unrestricted early stopping. The later dynamics and contraction arguments below supply those additional inputs on their stated domains. This paragraph does not recertify B04's entire analytic proof by borrowing B02's verdict.

### Final finite-time and uniform-time composition

I subsequently read B01's entire `b01_GD_state_evolution_check.md`, B02's entire `b02_uniform_time_GD.md`, B03's assembled Sections 9--10, and `T357_PRIMARY_SOURCE_COMPARISON.md`.

For the finite-time recursion, I independently reopened Fan's original paper, Sections 2.4 and 5.1, and Wang--Zhong--Fan Theorem 2.22 and Assumption 2.17. The lower-triangular transpose convention, covariance sums, and aspect-ratio factors match those sources. Expanding the already audited spectral fixed point gives
\(rM(z)=M_{\mathcal H}(rz(1+M(z)))\); substituting the ordinary free transform of \(\nu+a^2\mathrm{MP}_\gamma\) gives the stated rectangular cumulants \(\kappa_2=v\) and \(\kappa_{2k}=a^{2k}\delta^{k-1}\) for \(k\ge2\). This is a formal-series calculation, so it imposes no small-step assumption. The covariance sums reduce to the finite triangular inverses displayed by B01.

The causal construction is valid: the current column covariance uses no as-yet undefined current column function because the last column of the row derivative matrix is zero. The column derivative matrix has strictly positive diagonal equal to the step. The covariance decomposition has the positive terms \(r\nu\Delta_t\) and \(\nu\Gamma_t\); the new row residual is a strictly monotone function of a fresh nondegenerate conditional Gaussian on a training row. This proves positive definiteness at each fixed stage. No unproved regularization limit is needed. Adding back the prescribed AMP memory terms cancels them exactly, and the explicit normalized-norm induction replaces frozen scalar overlaps by empirical overlaps. The mask-zero test block then identifies conditional fresh-test laws and moments. These arguments close the earlier finite-time dynamics gap for all positive finite aspect ratios and fixed positive steps.

For the whole trajectory I independently checked B02's arguments, including the following sensitive points:

- The noisy-label small-ball lower bound conditions on the original input before assigning the label. It does not assume the label and random-feature score are independent.
- The robust covariance estimate holds after arbitrary deletion of a controlled fraction of rows, so it applies to the sample-dependent set where a candidate score is moderate.
- Coercivity confines both the full and every omitted-feature trajectory to the same deterministic sublevel ball; Hessian bounds on that ball give a dimension-independent contraction.
- The omitted-feature object is defined on every sample, including exceptional samples, using no omitted feature. Gaussian concentration is applied with that independence before intersecting with the good geometry event.
- Concentration is union-bounded through a deterministic logarithmic time horizon. Contraction controls the infinite tail. Thus delocalization is genuinely uniform in time.
- A uniform positive orthogonal score variance and a compact covariance set imply a strictly positive exact-calibration floor by B04's deterministic TV theorem and the nonidentity of a logistic-normal regression curve with a sigmoid.
- Fixed-time deterministic overlaps extend uniformly to all integer times and the MLE by splitting into a finite prefix and a common geometric tail. This is a proved limit argument, not an assumed exchange of limits.

The analytic pair-TV theorem is imported from B04 with B02's dedicated independent audit. This report's new independent checks concern its hypotheses, its uniform application, and the composition; they do not claim another complete derivation of the analytic smoothing theorem.

Finally, `b06_gaussian_overconfidence.md` gives the strict scalar signed-overconfidence proof. Its Section 6 proves that an explicit weak-teacher open regime makes the first-step risk-optimal scale satisfy B02's stable-step bound. Thus the signed-overconfidence, genuine risk improvement, and all-time stopping obstruction can hold in one and the same fixed Gaussian RF model. There is no need to stitch together incompatible step choices.

## 8. Final audit boundary

The earlier follow-up did not complete the ordinary RBF or full Gaussian T357 objectives. The new continuation has changed the Gaussian result, while the RBF architecture boundaries remain.

The final mathematical T357 acceptance map is:

| Original-row clause | Accepted Gaussian result | Restriction that must remain visible |
|---|---|---|
| Two-layer network, cross-entropy GD | Actual dense Gaussian-input tanh random features; output-layer full-batch GD from zero | Hidden features are fixed; no feature-learning claim |
| Dependence on sample/input ratio, width and time | Explicit deterministic finite-time Gaussian recursion, including every finite set of positive times | Any fixed positive finite aspect ratios and fixed positive step; this is not arbitrary-ratio uniform late-time convergence |
| Exact population calibration | Model-conditional unbinned CE and integrated curve, via conditional pair-TV convergence | Uses the stated Gaussian teacher/features and nondegenerate positive-time limit |
| Signed overconfidence | Strict average signed OC at the unique first-step risk-optimal step, for every positive scalar signal/noise/teacher parameter | Average confidence minus accuracy; far-tail pointwise underconfidence also occurs |
| Whether early stopping calibrates | No positive-time stopping rule achieves exact calibration in the whole-trajectory regime; time zero is calibrated | Sufficiently large fixed sample-to-width ratio and sufficiently small fixed positive step |
| Nonvacuous common model | Explicit open weak-teacher regime has the risk-optimal first iterate inside that stable-step interval and improves on risk \(\log2\) | The conservative sample-to-width condition makes the fitted output layer underparameterized |
| Published open-problem status | Source comparison distinguishes prior RF calibration, postprocessing, and early-stopped consistency theorems | No verified novelty or previously recognized named-conjecture resolution is certified |

The row explicitly permits random features and asks for a solvable regime. A theorem for the entire ordinary Gaussian proportional family at each fixed time, with an additional all-time theorem on a stated open parameter domain, directly answers that branch in a way the categorical surrogate did not. Calling it a theorem for all architectures, all aspect ratios at infinite time, all step schedules, or feature learning would still be false. The original row's title does not make the large-sample all-time theorem an overparameterized-output-layer theorem.

The phase-retrieval branch has a complete mathematical treatment with the explicitly specified truncated MALA algorithm; its source/novelty status must still be reported honestly. A quantitative attracting-manifold theorem must retain its initialization and regularity hypotheses, and later-literature status prevents counting an already established rate request as newly resolved.

The final user-facing result should name the exact theorem proved, list any remaining mathematical clause, and separately state whether publication novelty was established. It should not reuse the earlier existential-regime scope audit to override the user's explicit demand.

### Final synthesis acceptance

The frozen `fullproof/T357_THEOREM_AND_SYNTHESIS.md` was read in full, including its common-step corollary and final normalization/TV clarifications. It passes this independent scope and mathematical-composition review as a complete answer to the original row's expressly permitted Gaussian random-feature regime. Its finite-time theorem includes all positive finite aspect ratios; its arbitrary-stopping extension has the explicit large-sample and small-fixed-step restrictions. It does not claim external validation, formal verification, certified novelty, or universal late-time behavior in overparameterized output layers.

The scalar proof in `b06_gaussian_overconfidence.md`, including the common regime and risk-constrained stopping corollary, also received independent PASS reviews from B02 and B04 on the pinned final version. The acceptance record does not reinterpret the earlier categorical construction as the full target.

## 9. Exact audit pins

SHA-256 values below were computed from the actual local bytes on 24 October 2026. Registry-row hashes omit their terminating newline. These hashes identify the read versions and do not certify that remote copies have been saved.

| Read file | SHA-256 |
|---|---|
| `a03/registry422.jsonl` | `c1a7636d5ef95888a26e92b36a017e2a2aae72d7140de9f6d39c695c67d2d3b0` |
| `followup/ORIGINAL_PROBLEM_SCOPE_AUDIT.md` | `8f194fc68cbb1fa778d70f20bf4ba6eb1ea0447c4f531512f6d3269e35676390` |
| `followup/T336_architecture_compiler.md` | `8dbb67bbc8609cb86b0a1fb888f61c64abf36b07c8ebfc0464b0d0e5a4adf175` |
| `followup/T336_scope_and_obstruction.md` | `5c1ea4e7c3691c4eef8814b25ede5ebb9997b476c524fbf674cfed55b9bb75d0` |
| `followup/T336_unbounded_label_independent.md` | `82ebfbbee8cca6d7f8ac1a797b5f605e7e25507bdffdd6d3b51f9a3a25ef4f44` |
| `followup/T336_constructive_independent_review.md` | `2dd90e470a6d77653f39fee975167282fd190766ed31fb45b408ee6176cccebb` |
| `followup/T357_CATEGORICAL_COMPLETE_THEOREM.md` | `2afde40ad003392b17d90cbc90f94a87d96fcef2771695a03c35af62b271c3bd` |
| `followup/T357_gaussian_first_step_independent_review.md` | `7c9b8412cc8d38e184972b9256773d7854cf7878b2bb2e1df5a8eafda80fc73f` |
| `followup/T357_gaussian_calibration_consequences.md` | `124e5b2782f1fa000fc0103f04ce834eaaa70bb18b1483dfbd0d64fe0b4363fd` |
| **`fullproof/b01_target_triage.md` -- accepted full mathematical T321 proof** | **`5e3ca9790f24971549c46034c44d44c4616007c71d745e5a13d1598a1af27784`** |
| `fullproof/b02_target_triage.md` | `842a137b09cfcf815c883f99740f1349d61a2216fba47c4c8b46b47d5d2e492b` |
| **`fullproof/b03_gaussian_dynamics.md` -- accepted Sections 1--6 and 8--10** | **`b5992c4a107b715a92fe79413ef79e1acb000afe3300e78c1e0af114340b59c9`** |
| `fullproof/b04_calibration_transfer.md` -- consulted; B02 owns complete independent audit | `f5c70cb70355d6a2d579b2482e8a3a384e50b754195a5721453d8e91703e889d` |
| `fullproof/b02_gaussian_calibration_audit.md` | `6105f68431fb7aac91a8951d8990b1471d7197fed7f0b5c06dff89eb581a77b7` |

| Additional completed proof/audit | SHA-256 |
|---|---|
| `fullproof/T357_THEOREM_AND_SYNTHESIS.md` -- accepted frozen synthesis | `7b773eba4446340893bd8e67a1397ba06b154bf79b9f89a348e68c1a93282d51` |
| `fullproof/b04_calibration_transfer.md` -- final module consulted; analytic audit remains B02 | `ce160157647aed6aa8d405979525f31649ce8f91d99ca9ce8821d3d849eaa574` |
| `fullproof/b01_GD_state_evolution_check.md` -- independent finite-time recursion audit | `077b6c8134a2780f4ad5132be70fe50ccdfccd7240d00a50b4ea775d1ea0338f` |
| `fullproof/b02_uniform_time_GD.md` -- independent all-time geometry/composition audit | `1102592bcfdc5b3b9b82476b7d6065b7f0c596f3f6b14b05d1362637f104483f` |
| `fullproof/b06_gaussian_overconfidence.md` -- self-contained scalar proof and common regime | `b65ea33e7e0208b825f429f5369ac1fbd1e470803848356df749b7208fbcb532` |
| `fullproof/T357_PRIMARY_SOURCE_COMPARISON.md` -- scope comparison reviewed | `6b67e57cd3f359ad08a5dea7bd667d5fc831ecae8ccc0d5bc46c248cac22c2e8` |

| Exact registry row | SHA-256 |
|---|---|
| T321 | `4c17d8716b21260580601d973d4f576d7a7b69515a7a19268fec9ae738ad5ef9` |
| T336 | `f0b9babf34c4b5b0e656737f8acbce6b6782e26c448487d1600d763c7295aa89` |
| T352 | `63bd493b5c09ed10cd0b4635f9c377443d8e6142f730c217d3fc4db00b9aa357` |
| T355 | `bd398b25a5bcac7af28e6066cf48302411c7e930b24adfaae40461b23f0e34d4` |
| T357 | `354d0cd4e71345e105368edaeedc7639da543a2cb8e476a6bfaa3df14715b330` |

The final T321 proof's extra contemporary comparison, [Lytras--Makras--Sabanis, arXiv:2608.06283v1](https://arxiv.org/html/2608.06283v1), Section 8.2, was also independently opened. It treats a tamed Euler method and complex Gaussian phase retrieval. Its connected phase symmetry and algorithm differ from the real-sign bottleneck proved here. The existence of this related paper further supports withholding an unqualified novelty claim; no duplicate of the exact real-model lower theorem is certified or ruled out by this limited comparison.
