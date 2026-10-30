# B17 FEI new proof mechanism — one-point tensors expose the missing KL logarithm

**Run:** `B17-20260921T111115Z-r28`  
**Status:** PARTIAL; full Fourier entropy–influence (FEI) remains OPEN / NOT PROVED.  
**Brain label:** WITHOUT_VERIFIED_BRAIN.  
**Fresh source state read before derivation:** `yspennstate/math-open-problems` master `a0db60b3f18db223bfb0a220241b69132d94139c`.  
**Live role:** FEI new proof mechanisms.  
**Named universal obstruction attacked:** the product-phase/total-correlation route needs a **KL-scale** dependence payment in the many-rare-coordinate regime; the available phase comparison first produces an unweighted square-root/Hellinger displacement, which loses the rare-event logarithm.  
**Method:** exact Boolean construction + tensorization + sequential comparison. This is deliberately different from the previous B17 exact-product rigidity proof and from the signed-diagonal route.

## 1. Why this calculation is needed

For a Boolean function `f`, let

\[
\mu(S)=\widehat f(S)^2,\qquad p_i=\Pr_\mu(i\in S)=\operatorname{Inf}_i(f),
\]

and let `Q` be the product law with the same marginals. Then

\[
\operatorname{TC}(\mu)=D_{\rm KL,2}(\mu\|Q)=\sum_i h_2(p_i)-H(f),
\]

so for a candidate FEI constant `C`,

\[
H(f)-CI(f)=\sum_i\bigl(h_2(p_i)-Cp_i\bigr)-\operatorname{TC}(\mu). \tag{1}
\]

The preceding fleet04/B17 run proved exact product rigidity and a first Hellinger-scale Boolean dependence bound. The current B18 integration sharpened the remaining issue: a global Hellinger displacement is bounded, whereas the KL payment required in (1) can be extensive.

This run asks a more adversarial question:

> Is that scale mismatch merely an artifact of hypothetical distributions, or does it already occur in an explicit exact Boolean family with completely known Fourier spectrum?

It occurs in the simplest possible family: one-point defects, and even more decisively in their disjoint tensor products.

## 2. Exact one-point-defect spectrum

Fix `d>=2` and let `g_d:{-1,1}^d->{-1,1}` equal `-1` at one vertex and `+1` everywhere else. Put

\[
p=2^{1-d}.
\]

After translating the exceptional vertex if necessary, direct Walsh summation gives

\[
\widehat g_d(\varnothing)=1-p,
\qquad
|\widehat g_d(S)|=p\quad(S\ne\varnothing). \tag{2}
\]

Therefore its spectral law is

\[
\mu_d(\varnothing)=(1-p)^2,
\qquad
\mu_d(S)=p^2\quad(S\ne\varnothing). \tag{3}
\]

For each coordinate `i`, exactly `2^{d-1}` nonempty subsets contain `i`, hence

\[
\Pr(i\in S)=2^{d-1}p^2=p. \tag{4}
\]

Thus

\[
I(g_d)=dp,
\qquad Q_d=\operatorname{Bernoulli}(p)^{\otimes d}. \tag{5}
\]

The entropy and total correlation are consequently exact:

\[
H_d=-(1-p)^2\log_2(1-p)^2-(2^d-1)p^2\log_2 p^2, \tag{6}
\]

\[
\operatorname{TC}_d=d h_2(p)-H_d. \tag{7}
\]

In particular `H_d/I_d -> 4`; this family is not an FEI counterexample.

## 3. PROVED: global Hellinger payment loses an unbounded logarithmic factor on exact Boolean functions

Let

\[
A_d=\sum_S\sqrt{\mu_d(S)Q_d(S)}
\]

be Hellinger affinity and use the same square-root displacement convention as the product-phase route,

\[
t_d=\|\sqrt{\mu_d}-\sqrt{Q_d}\|_2^2=2(1-A_d). \tag{8}
\]

From (3), summing the product-law square roots gives the closed form

\[
\boxed{
A_d=(1-2p)(1-p)^{d/2}
+p\bigl(\sqrt p+\sqrt{1-p}\bigr)^d.
} \tag{9}
\]

For fixed `C`, define the product-marginal excess in (1)

\[
P_C(d)=d\bigl(h_2(p)-Cp\bigr). \tag{10}
\]

Because `p=2^{1-d}`,

\[
\frac{h_2(p)}p=d-1+\frac1{\ln2}+o(1), \tag{11}
\]

while expansion of (9) gives

\[
t_d=(d+2+o(1))p. \tag{12}
\]

Hence

\[
\boxed{
\frac{P_C(d)}{t_d}\sim d
}\qquad(d\to\infty). \tag{13}
\]

So no dimension-independent constant multiplying this global Hellinger displacement can pay the product-marginal excess, even on exact Boolean functions whose FEI ratio tends only to `4`.

At `C=6.4547837`, the excess becomes positive already at `d=7`. Selected exact-form numerical evaluations are:

| d | p | H/I | P_C(d) | TC | t | P_C/t |
|---:|---:|---:|---:|---:|---:|---:|
| 7 | 0.015625 | 3.8043571 | 0.1068136 | 0.3967040 | 0.0985382 | 1.0840 |
| 8 | 0.0078125 | 3.8427826 | 0.1238913 | 0.2871414 | 0.0621629 | 1.9930 |
| 10 | 0.001953125 | 3.8841784 | 0.0778614 | 0.1280685 | 0.0212280 | 3.6679 |
| 16 | 3.0518e-5 | 3.9302714 | 0.00487690 | 0.00610957 | 5.4363e-4 | 8.9710 |
| 20 | 1.9073e-6 | 3.9442655 | 5.33596e-4 | 6.29365e-4 | 4.18545e-5 | 12.7488 |
| 30 | 1.8626e-9 | 3.9628463 | 1.34043e-6 | 1.47968e-6 | 5.95998e-8 | 22.4905 |

The table is only a check of the closed forms; (13) is analytic.

## 4. PROVED: tensorization turns the scale mismatch into a decisive no-go theorem

Fix any `d` for which `P_C(d)>0`, and place `m` independent one-point-defect blocks on disjoint variables:

\[
F_{d,m}(x^{(1)},\ldots,x^{(m)})=\prod_{r=1}^m g_d(x^{(r)}). \tag{14}
\]

Fourier coefficients tensor exactly, hence

\[
\mu_{d,m}=\mu_d^{\otimes m},
\qquad
Q_{d,m}=Q_d^{\otimes m}. \tag{15}
\]

Therefore

\[
H(F_{d,m})=mH_d,
\quad I(F_{d,m})=mdp,
\quad \operatorname{TC}_{d,m}=m\operatorname{TC}_d,
\quad P_C(d,m)=mP_C(d). \tag{16}
\]

Hellinger affinity also tensorizes, but the global displacement saturates:

\[
A_{d,m}=A_d^m,
\qquad
\boxed{t_{d,m}=2(1-A_d^m)\le2.} \tag{17}
\]

Thus, for every fixed `d` with `P_C(d)>0`,

\[
P_C(d,m)\to\infty,
\qquad \operatorname{TC}_{d,m}\to\infty,
\qquad t_{d,m}\le2. \tag{18}
\]

### Refuted proof strategy

There is no universal constant `K` for which a lower bound of the form

\[
\operatorname{TC}(\mu)\ge K\,t(\mu,Q)
\]

—or any FEI closure that only extracts a fixed multiple of the **global** square-root/Hellinger displacement—can by itself pay the right side of (1). The obstruction is witnessed by explicit Boolean tensor products, not by an inadmissible synthetic distribution.

For example, at `C=6.4547837` and `d=8`, `P_C(8)=0.1238913...`; at `m=64`, the required excess is `7.9290443...` while global `t` is only `1.7348962...` and can never exceed `2`.

This sharpens the qualitative warning in the current product-phase integration by supplying an exact admissible family and an exact tensorization mechanism.

## 5. Stronger boundary check: even unweighted *chain-additive* Hellinger energy misses the logarithm

One might repair global saturation by applying square-root distance conditionally and adding it along a chain. This still loses the crucial rare-event logarithm.

For distributions `mu,Q` on ordered bits, define

\[
\mathcal E_{\rm Hel}(\mu\|Q)
=\sum_i \mathbb E_{X_{<i}\sim\mu}
\left\|\sqrt{\mu(X_i\mid X_{<i})}-\sqrt{Q_i}\right\|_2^2. \tag{19}
\]

The KL chain rule and the Bernoulli Hellinger bound give generally

\[
D_{\rm KL,nats}(\mu\|Q)\ge\mathcal E_{\rm Hel}(\mu\|Q). \tag{20}
\]

For the one-point defect, symmetry makes every coordinate order equivalent. After `k` preceding zeros, put

\[
D_k=\Pr_\mu(X_1=\cdots=X_k=0)
=1-2p(1-2^{-k}), \tag{21}
\]

and

\[
q_k=\Pr_\mu(X_{k+1}=1\mid X_1=\cdots=X_k=0)
=\frac{p2^{-k}}{D_k}. \tag{22}
\]

If the observed prefix contains a `1`, all compatible nonempty Fourier labels have equal mass in (3), so the next membership bit is exactly fair: conditional probability `1/2`. Writing

\[
r^2(q,p)=(\sqrt q-\sqrt p)^2+(\sqrt{1-q}-\sqrt{1-p})^2, \tag{23}
\]

we obtain the exact finite sum

\[
\boxed{
\mathcal E_d
=\sum_{k=0}^{d-1}
\Bigl[D_k r^2(q_k,p)+(1-D_k)r^2(1/2,p)\Bigr].
} \tag{24}
\]

For each fixed `k`, as `d->infinity` (`p->0`), the summand divided by `p` tends

\[
(1-2^{-k/2})^2+2(1-2^{-k})(2-\sqrt2). \tag{25}
\]

The latter tends to `5-2 sqrt(2)`. A bounded-tail/Cesaro argument applied to (24) therefore gives

\[
\boxed{
\frac{\mathcal E_d}{dp}\longrightarrow 5-2\sqrt2
=2.171572875\ldots .
} \tag{26}
\]

Combining (10)-(11) and (26),

\[
\boxed{
\frac{(\ln2)P_C(d)}{\mathcal E_d}
\sim \frac{\ln2}{5-2\sqrt2}\,d
=0.3191913\ldots\,d.
} \tag{27}
\]

Hence merely making the Hellinger payment additive does **not** fix the route. A successful comparison must retain a logarithmic likelihood-ratio factor, or work directly at KL/relative-entropy scale.

This boundary check is important because it rules out the most immediate proposed repair of the global Hellinger theorem.

## 6. What the exact family says the missing mechanism must look like

The conditional description above identifies where the required logarithm lives. Under `Q_d`, every coordinate remains rare with probability `p`. Under `mu_d`, once a previously observed spectral bit is `1`, every later bit becomes fair. On those rare histories the conditional likelihood ratio is of order `1/p`, so the **conditional KL** contribution contains `log(1/p)`, precisely the factor discarded by an unweighted square-root comparison.

This suggests a new universal target:

> **Rare-history activation / KL target.** Derive from the Boolean Fourier phase-cancellation identities a lower bound on the chain-rule KL contributions on histories where a rare marginal becomes conditionally order-one. The estimate must preserve the `log(q/p)` likelihood ratio; replacing it by an unweighted L2/Hellinger displacement is provably too lossy.

Equivalently, any multiscale phase argument should be organized by rare-coordinate likelihood scale, not merely by Euclidean distance from the matched product law.

This target is compatible with the current curl-free phase constraint but does not duplicate it: the current report supplies an exact Boolean model showing the scale and localization that the curl-free argument has to recover.

## 7. Relation to current primary literature

A bounded primary-literature comparison was made before any novelty claim. No publication-priority claim is made for the construction or comparison above.

- O'Donnell--Tan, *A composition theorem for the Fourier Entropy-Influence conjecture* (ICALP 2013; arXiv:1304.1347), treats disjoint composition and is relevant to the exact tensorization in (14)-(16).
- Wan--Wright--Wu, *Decision Trees, Protocols, and the Fourier Entropy-Influence Conjecture* (arXiv:1312.3003), gives communication/decision-tree formulations and another proof of FEI+ composition.
- Xiao Han, *A New Bound for the Fourier-Entropy-Influence Conjecture*, Combinatorica 45 (2025), proves an upper bound of the form `O(I + sum_i I_i log(1/I_i))`.
- Peijie Li--Guangyue Han, *Strengthening Han's Fourier Entropy-Influence Inequality via an Information-Theoretic Proof* (arXiv:2512.03117, 2025), reports the corresponding information-theoretic inequality with sharp coefficient normalization in its formulation.

The last two references reinforce, rather than supersede, the calibration found here: the natural general upper bound already carries the rare-coordinate logarithm. This report does **not** claim a new general entropy upper bound; it identifies why a specific Hellinger-based Booleanity mechanism cannot remove that logarithm and what a KL-scale replacement must retain.

## 8. Executed checks

`verify_onepoint_hll_kl.py` was executed in this run. It:

1. brute-force Walsh-transformed the one-point defect for `d=2,3,4,5` and recovered (2)-(4) with zero reported marginal error in floating arithmetic;
2. evaluated (6)-(10) at `d=6,7,8,10,12,16,20,30`;
3. checked tensor formulas for `d=8`, `m=1,2,4,8,16,32,64`, including `t<=2`.

Checker SHA-256:
`ec73f3d9de7f0cfa8eb1d9c75f34ab3b37f7e8704e432f2e642783d31657692e`.

The finite checks are sanity checks only; all universal/asymptotic statements above are proved from the closed forms.

## 9. Claim ledger

**PROVED:**

- Exact spectral law (2)-(4) and entropy/TC formulas for one-point defects.
- Exact Hellinger affinity (9).
- `P_C(d)/t_d ~ d` for every fixed `C`.
- Exact tensor identities (15)-(17), giving an explicit Boolean no-go family for global-Hellinger-only FEI payment.
- Exact conditional Hellinger formula (24) and asymptotic `E_d/(dp) -> 5-2 sqrt(2)`.
- Therefore any fixed-coefficient unweighted chain-additive Hellinger payment also misses the required product excess by a factor growing linearly in `d`.

**REFUTED PROOF STRATEGIES:**

- A fixed multiple of global Hellinger/square-root displacement can close the product-phase FEI route.
- Tensorizing that same global displacement fixes the scale problem.
- Replacing global Hellinger by an unweighted additive conditional-Hellinger energy is enough uniformly.

**OPEN / NEXT OBLIGATION:**

Prove a Booleanity-driven **KL-scale rare-history activation inequality** (or an equivalent log-weighted multiscale phase inequality) from the simultaneous phase-cancellation/curl-free constraints, strong enough to pay
`sum_i (h2(p_i)-C p_i)_+`. Full FEI remains open.
