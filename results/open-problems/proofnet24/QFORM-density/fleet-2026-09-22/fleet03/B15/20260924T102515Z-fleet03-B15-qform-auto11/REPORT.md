SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B15, 2026-09-24T10:25:15Z.
attacking: quantify the failure of Gaussian-mixture approximation for arbitrary cap-one laws, then close the valid Gaussian-mixture target branch with same-constant C0 regularity.

# fleet03/B15 — sharp Gaussian-mixture concentration barrier and rough-law closure obstruction

Run: `20260924T102515Z-fleet03-B15-qform-auto11`.

Status: `GAUSSIAN_MIXTURE_CONCENTRATION_BARRIER_PROVED / WEAK_CLOSURE_OBSTRUCTION_PROVED / PARTNER_APPLIED / FULL_QFORM_OPEN`.

The unrestricted quadratic-form bounded-density conjecture remains OPEN. This report does not alter the target and does not claim a QFORM counterexample. It proves that one currently successful full-matrix theorem — the Gaussian location/scale-mixture branch — cannot be extended to all cap-one product laws by a no-loss weak- or total-variation approximation argument under its present inverse-scale hypothesis.

## 1. Conditional end-to-end logic and first missing implication

The completed full Gaussian-mixture theorem at

`yspennstate/math-open-problems@9dabaf2aaf66687c2b4437fdb359b1aeb4a804bc`
`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_GAUSSIAN_MIXTURE_FULL_THEOREM.md`

proves, for independent

\[
X_i=M_i+\sqrt{T_i}G_i,
\qquad \mathbb E T_i^{-1/2}\le\sqrt{2\pi},
\]

that every target quadratic-affine form has a bounded continuous density, and under `s_3(A)>=1` the height is `<3`.

A tempting closure would be:

1. approximate every cap-one marginal by such Gaussian mixtures;
2. keep the same inverse-scale constant `sqrt(2 pi)`;
3. pass the `<3` interval estimate to the weak limit by Portmanteau.

Step 3 would be valid. The missing step is Step 1. The theorem below proves that Step 1 is impossible even in one dimension, and in fact the admissible Gaussian-mixture class stays a fixed positive distance from `Uniform[0,1]`.

## 2. Sharp interval-concentration theorem

### Theorem 2.1 — `QFORM-GAUSSIAN-MIXTURE-CONCENTRATION-BARRIER-v1`

Let

\[
Y=M+\sqrt T\,G,
\]

where `G~N(0,1)` is independent of the arbitrary pair `(M,T)`, with `T>0` almost surely. Suppose

\[
\mathbb E T^{-1/2}\le \kappa<\infty.
\]

Then for every interval `J` of length `L>0`,

\[
\boxed{
\Pr\{Y\in J\}
\le
2\Phi\!\left(\frac{\kappa L}{2}\right)-1.
}
\tag{2.1}
\]

Equivalently the concentration function obeys

\[
\boxed{
\mathcal Q_Y(L):=\sup_x\Pr\{Y\in[x,x+L]\}
\le q_\kappa(L):=2\Phi(\kappa L/2)-1.
}
\tag{2.2}
\]

The bound is sharp for every `kappa,L`: equality is attained by the single Gaussian with deterministic `T=kappa^{-2}` and mean at the midpoint of `J`.

### Proof

Condition on `(M,T)=(m,t)`. For a centered unimodal Gaussian, among intervals of fixed length `L` the probability is maximal when the interval is centered at the mean. Therefore

\[
\Pr\{Y\in J\mid M=m,T=t\}
\le
2\Phi\!\left(\frac{L}{2\sqrt t}\right)-1.
\tag{2.3}
\]

Put `u=t^{-1/2}` and

\[
g_L(u)=2\Phi(Lu/2)-1,\qquad u\ge0.
\]

Writing `phi` for the standard normal density,

\[
g_L'(u)=L\phi(Lu/2)>0,
\]

and

\[
g_L''(u)
=-\frac{L^3}{4}u\,\phi(Lu/2)\le0.
\tag{2.4}
\]

Hence `g_L` is increasing and concave. Averaging (2.3) and applying Jensen gives

\[
\Pr\{Y\in J\}
\le \mathbb E g_L(T^{-1/2})
\le g_L(\mathbb E T^{-1/2})
\le g_L(\kappa),
\]

which is (2.1). Equality is obtained when `T^{-1/2}=kappa` almost surely and every conditional mean is the midpoint of `J`. QED.

No assumption on the distribution of the random center `M`, its dependence on `T`, support, moments, connectedness, or smoothness is used.

## 3. The exact cap-one Gaussian-mixture barrier

The current full Gaussian-mixture QFORM theorem uses

\[
\kappa_0=\sqrt{2\pi}.
\]

This is precisely the average component-peak condition that implies a marginal density cap one. Theorem 2.1 gives, for every interval of length one,

\[
\boxed{
\Pr\{Y\in J\}
\le q_*:=2\Phi(\sqrt{\pi/2})-1
=0.7899085945560627\ldots .
}
\tag{3.1}
\]

Consequently, if `U~Uniform[0,1]` and `nu` is any Gaussian location/scale mixture satisfying the theorem's inverse-scale condition, then with the convention

\[
d_{TV}(\mu,\nu)=\sup_E|\mu(E)-\nu(E)|,
\]

we have

\[
\boxed{
d_{TV}(\mathcal L(U),\nu)
\ge 1-q_*
=0.2100914054439373\ldots .
}
\tag{3.2}
\]

Indeed, use the event `[0,1]`.

This is not merely failure of one mollifier construction. It is an intrinsic geometric gap for the entire random-center Gaussian-mixture class under the fixed inverse-scale budget.

## 4. Not even weakly dense

### Corollary 4.1

Let `G_kappa` denote the class of all laws in Theorem 2.1 with the same bound `E T^{-1/2}<=kappa`. Every weak limit of laws in `G_kappa` satisfies, for every open interval `J`,

\[
\mu(J)\le q_\kappa(|J|)<1.
\tag{4.1}
\]

Hence no compactly supported probability law belongs to the weak closure of `G_kappa`.

### Proof

If `nu_n=>mu` and `J` is open, Portmanteau gives

\[
\mu(J)\le\liminf_n\nu_n(J).
\]

Every term is at most `q_kappa(|J|)` by (2.1), proving (4.1).

If `mu` is supported in a finite interval `[a,b]`, choose any `eps>0` and `J=(a-eps,b+eps)`. Then `mu(J)=1`, while `q_kappa(b-a+2eps)<1` for finite `kappa`, contradiction. QED.

In particular, `Uniform[0,1]` cannot be approximated even weakly by the fixed-constant Gaussian-mixture class used in the `<3` QFORM theorem.

## 5. Product amplification

Let

\[
\mu_n=\operatorname{Unif}[0,1]^{\otimes n}
\]

and let

\[
\nu_n=\nu_1\otimes\cdots\otimes\nu_n,
\]

where each `nu_i` satisfies the Gaussian-mixture inverse-scale condition with `kappa_0=sqrt(2 pi)`. Independence gives

\[
\nu_n([0,1]^n)
=\prod_{i=1}^n\nu_i([0,1])
\le q_*^n.
\]

Therefore

\[
\boxed{
d_{TV}(\mu_n,\nu_n)\ge1-q_*^n.
}
\tag{5.1}
\]

For reference,

- `n=3`: the gap is at least `0.5071321184`;
- `n=10`: at least `0.9054267340`;
- `n=20`: at least `0.9910558972`;
- `n=40`: at least `0.9999200030`.

So the approximation obstruction becomes nearly maximal in the high-dimensional product regime relevant to the diffuse QFORM cases.

## 6. Quantitative cost of relaxing the inverse-scale budget

The concentration theorem also quantifies what happens if one allows a larger inverse-scale parameter in an attempted approximation.

If a Gaussian mixture `nu` satisfies

\[
d_{TV}(\nu,\operatorname{Unif}[0,1])\le\varepsilon,
\]

then `nu([0,1])>=1-epsilon`. By (2.1), any bound

\[
\mathbb E T^{-1/2}\le\kappa
\]

must satisfy

\[
1-\varepsilon
\le2\Phi(\kappa/2)-1,
\]

hence

\[
\boxed{
\kappa\ge2\Phi^{-1}(1-\varepsilon/2).
}
\tag{6.1}
\]

Thus `kappa->infinity` is necessary as `epsilon->0`.

The determinant proof in the completed Gaussian-mixture theorem extends verbatim when the common bound `sqrt(2 pi)` is replaced by a common `kappa`. Its weighted exponents satisfy

\[
\sum_i\alpha_i/k=2,
\]

so the resulting certificate is

\[
\boxed{
\|p_Q\|_\infty
\le
\frac{I_k}{2\pi}\,\kappa^2\,e_k(A^2)^{-1/(2k)}.
}
\tag{6.2}
\]

For `k=3`, `s_3(A)>=1`, this becomes

\[
\|p_Q\|_\infty
\le \frac{I_3}{2\pi}\kappa^2.
\tag{6.3}
\]

Combining with (6.1), the constant produced by this **specific determinant/inverse-scale mechanism** must deteriorate at least as

\[
\boxed{
\frac{2I_3}{\pi}
\left[\Phi^{-1}(1-\varepsilon/2)\right]^2,
}
\tag{6.4}
\]

when used along Gaussian-mixture approximants to `Uniform[0,1]`.

Numerically, with `I_3=2.942468198169458...`, the certificate forced by (6.4) is already about `5.07` at TV error `0.1`, `12.43` at error `0.01`, `20.28` at error `0.001`, and `44.82` at error `10^{-6}`. Asymptotically it grows logarithmically in `1/epsilon`.

Important logical scope: (6.4) is a barrier for the **present inverse-scale certificate**, not a lower bound on the true quadratic-output density. The diagonal target `A=I_3` itself has the known universal bound `pi`; the divergence shows precisely that this Gaussian-mixture proof cannot recover that rough law through constant-preserving approximation.

## 7. Designated partner applied to an actual inequality

The completed designated partner result is fleet04/B15 Theorem 6.1 at

`yspennstate/math-open-problems@a1654d5fe319f483999583921d127819e40bc868`
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B15/20260923T221909Z-fleet04-B15-ruled-trace-c0-r8/REPORT.md`.

It states: for any fixed rank-at-least-three target instance, once a separate argument proves

\[
\Pr\{Q\in I\}\le M|I|
\]

for every interval, the exact rough-product law has a canonical density in `C_0(R)` with the same height `M`.

Apply this to the actual Gaussian-mixture target inequality from the completed full-matrix theorem. For `s_3(A)>=1`, that theorem gives

\[
\Pr\{Q\in I\}
\le I_3|I|,
\qquad I_3=2.942468198169458\ldots<3.
\tag{7.1}
\]

Therefore the partner compiler yields, with zero height loss,

\[
\boxed{
p_Q\in C_0(\mathbb R),
\qquad
\|p_Q\|_\infty\le I_3<3.
}
\tag{7.2}
\]

The source Gaussian proof already obtains continuity by an integrable characteristic function, so (7.2) is an independent regularity closure of the same interval inequality and verifies compatibility of the two mechanisms.

The latest fleet04/B15 atomic-boundary theorem at

`yspennstate/math-open-problems@68a56e5fdbdc5b2812c544824e4ca584ec014263`
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B15/20260924T081140Z-fleet04-B15-atomic-boundary-r10/REPORT.md`

was also consumed. It remains compatible with this run: its jump formula concerns one-sided ruled mixtures, whereas the present obstruction concerns the topology of the Gaussian-mixture input class and does not invoke a moving-boundary trace.

## 8. Consequence for full-QFORM proof assembly

The Gaussian-mixture theorem is a genuine full-matrix, all-sign, all-rank target theorem for its input class. But its class with the constant needed for the `<3` bound is not dense in the rough cap-one laws under either total variation or weak convergence. Therefore:

\[
\boxed{
\text{Gaussian-mixture theorem + weak/TV closure cannot by itself prove full QFORM.}
}
\tag{8.1}
\]

Any successful extension must do at least one of the following:

- replace the inverse-scale moment by an estimate controlled directly by the final marginal cap, including separated narrow components;
- use a rough-law decomposition in which the bad component is paid by a different QFORM receiver rather than by the Gaussian determinant bound;
- establish a new approximation theorem whose quadratic-output bound is uniform while the inverse-scale parameter diverges;
- bypass Gaussian approximation altogether and prove the universal interval estimate directly.

This is a proof-route obstruction, not a counterexample to the owner conjecture.

## 9. Absolute continuity and continuity status

Absolute continuity remains strictly easier than the universal height problem. For every nonconstant quadratic-affine polynomial `q(x)=x^T A x+b^T x+c` and every absolutely continuous joint input law, `q(X)` is absolutely continuous: its critical set `{2Ax+b=0}` is empty or a proper affine subspace, hence null, and coarea on `{|grad q|>=1/m}` sends one-dimensional null target sets to zero source mass.

For the actual owner target, every matrix has rank at least three. The completed fixed-instance theorem plus the fleet04/B15 compiler imply that once the universal interval constant is proved, the stronger `C_0` conclusion follows with the same constant. Thus this run again separates the issues cleanly:

- absolute continuity: already unconditional for nonconstant quadratics under absolutely continuous inputs;
- fixed-instance boundedness and `C_0`: already available for rank at least three;
- universal target height: still OPEN;
- Gaussian-mixture branch: universal height `<3` and `C_0`, but not a dense input subclass under its present scale condition.

## 10. Exact status and next mechanism

Proved this run:

1. sharp interval concentration (2.1) for arbitrary random-center Gaussian scale mixtures under an inverse-half-scale moment;
2. a fixed `0.2100914054...` TV gap from `Uniform[0,1]` at the QFORM theorem's cap-one parameter;
3. non-density even in weak topology;
4. exponential product amplification `1-q_*^n`;
5. the quantitative divergence (6.1)-(6.4) of the present determinant/inverse-scale certificate along any Gaussian-mixture approximation to the uniform marginal;
6. same-constant `C_0` closure of the valid Gaussian-mixture QFORM inequality by the designated partner theorem.

Not proved:

- no universal bound for all arbitrary cap-one product laws;
- no QFORM counterexample;
- no claim that every possible Gaussian-mixture-based proof must fail, only that the current fixed inverse-scale closure and its direct parameter relaxation cannot supply a no-loss dense-class passage.

The next B15-relevant mechanism should target a rough-law decomposition that isolates separated narrow Gaussian components while preserving product provenance and assigns their small submass to an already-paid half-Riesz/grouped receiver. Repeating a fixed-constant Gaussian smoothing argument is now ruled out by Theorem 2.1.

Execution label: `WITHOUT_VERIFIED_BRAIN`. Repository retrieval/write/readback is distinct from native receiver ingestion.
