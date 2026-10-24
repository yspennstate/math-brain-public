# Addendum — projective plaquette inequality and double inverse-noise payment

**Status:** proved source lemmas; unrestricted FEI remains **OPEN**. This addendum continues the same account01/B16 signed-transport run and makes no novelty claim.

The main report proves that
\[
\beta_f(u)=\min_{\varepsilon=\pm1}\Pr\{f(X+u)\ne\varepsilon f(X)\}
=\frac{1-|\mathbb E f(X)f(X+u)|}{2}
\]
is a translation pseudometric. The same projective errors also control the exact dependent-face q-flip observable itself, before any square is taken.

## 1. `B16-PROJECTIVE-PLAQUETTE-BOUND`

For translations `u,v`, put
\[
P_f(u,v)
:=\Pr_X\{f(X)f(X+u)f(X+v)f(X+u+v)=-1\}.
\tag{1.1}
\]
This is exactly the derivative-disagreement kernel `p_u(v)` in the current B18 dictionary.

### Theorem

For every Boolean `f` and every `u,v`,
\[
\boxed{
P_f(u,v)
\le 2\min\{\beta_f(u),\beta_f(v),\beta_f(u+v)\}.
}
\tag{1.2}
\]
In particular,
\[
\boxed{P_f(u,v)\le\beta_f(u)+\beta_f(v).}
\tag{1.3}
\]

### Proof

Choose the minimizing projective sign `eps_u` for direction `u` and define
\[
A_u(x)=1_{\{f(x+u)\ne\varepsilon_u f(x)\}}.
\]
Then `E A_u=beta_f(u)`. The projective sign cancels around a plaquette, so
\[
f(x)f(x+u)f(x+v)f(x+u+v)
=(-1)^{A_u(x)+A_u(x+v)}.
\]
Therefore
\[
P_f(u,v)
=\Pr\{A_u(X)\ne A_u(X+v)\}
\le\Pr\{A_u(X)=1\}+\Pr\{A_u(X+v)=1\}
=2\beta_f(u).
\]
The plaquette product is symmetric in the three nonzero directions of the dependent face `(u,v,u+v)`, so the same proof gives the bounds `2 beta_f(v)` and `2 beta_f(u+v)`. This proves (1.2). Since `2 min(a,b)<=a+b`, (1.3) follows. QED.

This is the folded/projective analogue of the sharp three-local B18 estimate. It is weaker in the balanced case but stronger when one direction has small projective influence, and it is exactly adapted to the character-minimized budget `J`.

## 2. Weighted edge form

Let vertices carry arbitrary translation labels `h_a`, and let `lambda_ab>=0`. If the dependent-face source attached to edge `(a,b)` is the natural plaquette `P_f(h_a,h_b)`, then (1.3) gives
\[
\boxed{
\sum_{a<b}\lambda_{ab}P_f(h_a,h_b)
\le\sum_a d_a\beta_f(h_a),
\qquad
d_a=\sum_{b\ne a}\lambda_{ab}.
}
\tag{2.1}
\]
Thus the same weighted vertex-load quantity that pays the central Radon square in the main report also pays the **linear local transport metric** itself, with no extra dimension factor.

This is conditional only on the compiler actually coupling a current edge to the corresponding dependent face. It does not assert that the current handoff has already established that coupling.

## 3. Random-generator version

Let fixed translation generators be `h_1,...,h_m`. For a random subset `R`, set
\[
U_R=\sum_{j\in R}h_j.
\]
The projective triangle inequality holds realization by realization, hence
\[
\boxed{
\mathbb E\beta_f(U_R)
\le\sum_j\Pr(j\in R)\beta_f(h_j).
}
\tag{3.1}
\]
No independence hypothesis is needed.

For two independently generated random directions `U,V`, Theorem 1.2 therefore yields
\[
\boxed{
\mathbb E P_f(U,V)
\le2\min\left\{
\sum_j\Pr(j\in R_U)\beta_f(h_j),
\sum_j\Pr(j\in R_V)\beta_f(h_j)
\right\}.
}
\tag{3.2}
\]
This is directly compatible with correlated clone-pair thinning laws: only the one-player marginals are needed on the right side.

## 4. Product-noise and a double inverse-noise integral

Specialize to the physical coordinate generators and let `U_p,V_q` be independent directions whose coordinates are independently selected with probabilities `p,q` respectively. Then
\[
\mathbb E\beta_f(U_p)\le pJ(f),
\qquad
\mathbb E\beta_f(V_q)\le qJ(f).
\]
Hence
\[
\boxed{
\mathbb E P_f(U_p,V_q)
\le2\min(p,q)J(f).
}
\tag{4.1}
\]
This linear small-noise gain is sufficient to absorb **two** inverse-noise singularities simultaneously:
\[
\begin{aligned}
\int_0^{1/2}\!\int_0^{1/2}
\frac{\mathbb E P_f(U_p,V_q)}{pq}\,dp\,dq
&\le
2J(f)\int_0^{1/2}\!\int_0^{1/2}
\frac{1}{\max(p,q)}\,dp\,dq\\
&=\boxed{2J(f)}.
\end{aligned}
\tag{4.2}
\]
Likewise, for any fixed pivot `u`,
\[
\boxed{
\int_0^{1/2}\frac{\mathbb E P_f(u,U_p)}p\,dp
\le J(f).
}
\tag{4.3}
\]

The integral in (4.2) is finite for a structural reason: the projective plaquette probability vanishes linearly when either noise scale tends to zero. This is the same two-resolvent geometry that the current paired-selector theorem exposes combinatorially through `1/(s|T|)`.

What is **not** yet proved is that the actual fully refunded compiler double-resolvent can be pushed forward to the physical product-noise law in (4.2) while preserving its R32 signs, R16 refunds, dual-code multiplicity, and terminal mixed difference. The theorem gives an exact payment if that push-forward is established.

## 5. New compiler target

The current signed-transport route now has two source-side closure mechanisms with the same projective budget:

1. **quadratic/Radon source:** weighted central squares are paid by original-coordinate incidence with constant `1/270` (main report);
2. **linear dependent-face source:** weighted plaquette transport is paid by the same vertex load, and a double product-noise inverse integral costs at most `2J` (this addendum).

The next exact question is therefore not another local Boolean inequality. It is whether the two-parameter thinning in the paired-selector double-resolvent can be converted, after the already-required signed aggregation, into one of these projective noise measures with bounded physical incidence. A failure should be exhibited on authentic compiler coefficients, not on an unconstrained parity game.
