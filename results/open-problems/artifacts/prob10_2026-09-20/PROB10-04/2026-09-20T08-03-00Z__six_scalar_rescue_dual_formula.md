# PROB10-04 — exact six-scalar conditional rescue dual

Runtime model: **GPT-5.6 Sol; reasoning level UNVERIFIED — not GPT-6 maximum.**

This artifact records the formula to be used by the next interval-certification run.  It is a mathematical derivation, not a numerical endpoint certificate.

## Source objects

Use Díaz--Kirousis--Mitsche--Pérez-Giménez notation with light cutoff `M=23`, fixed core degree masses `hat_delta_{i,j}`, syntactic clause masses `hat_gamma_k`, positive/negative copy totals `lambda_p,lambda_n`, and heavy satisfied-copy masses `h_ps,h_ns`.

For a feasible source point, define

- `u = ell_ps`, `v = ell_ns1`, `w = ell_ns2`;
- `ell_pu=lambda_p-u`, `ell_nu=lambda_n-v-w`;
- `Q=Q_safe`, the number-density of safe `ps` slots;
- `B=B_can`, one canonical `nu` slot for each blocking clause that has a `nu` slot;
- `E=sum_i f_{i,1,1}`, the eligible `j=1` false-leaf density.

Normalize

\[
q=Q/u,\qquad \beta=B/(\lambda_n-v-w),\qquad e=E/v
\]

when the denominators are positive, and use value zero on the corresponding zero-mass boundary.  Every feasible point satisfies

\[
0\le q,\beta,e\le1.
\]

The proved iid-priority rescue survival factor is

\[
\prod_{i=1}^M s_i^{t_{i,1}n+o(n)},\qquad
s_i=1-\frac12\beta q^i e\in[1/2,1].
\]

## Partitions

For positive `nu=(nu_ps,nu_ns1,nu_ns2)`, define the unmodified source variable partitions

\[
\Psi_{i,j}(\nu)=\nu_{ps}^i+(\nu_{ns1}+\nu_{ns2})^j-\nu_{ns2}^j.
\]

For `j=1`, introduce `z>0` and replace the source partition by

\[
\Psi^R_{i,1}(\nu,z;q,\beta,e)
=\nu_{ps}^i\left(1-\frac12\beta q^i e\right)+z\nu_{ns1}.
\tag{A.1}
\]

For the heavy negative split,

\[
\Psi_H(\nu)=\nu_{ns1}+\nu_{ns2}.
\]

For a source extended clause type `alpha`, put

\[
r_Q(\alpha)=ps(\alpha)\,\mathbf 1\{ps(\alpha)+ns(\alpha)\ge2\},
\]

and

\[
r_B(\alpha)=\mathbf 1\{\alpha=((0,1),(1,1))\text{ or }((0,1),(0,2))\}.
\]

Thus `Q=sum_alpha r_Q(alpha)c_alpha` and `B=sum_alpha r_B(alpha)c_alpha`.

For positive `mu=(mu_ps,mu_ns1,mu_ns2)` and real tilts `eta,zeta`, define

\[
\Psi_k^{Q,B}(\mu;\eta,\zeta)
=\sum_{\alpha:p(\alpha)=k}
\frac{2}{w(\alpha)!}
\mu_{ps}^{ps(\alpha)}
\mu_{ns1}^{ns1(\alpha)}
\mu_{ns2}^{ns2(\alpha)}
\exp\{\eta r_Q(\alpha)+\zeta r_B(\alpha)\}.
\tag{A.2}
\]

Finally set, with `0 log 0=0`,

\[
C_\ell(u,v,w)=
 u\log u+(\lambda_p-u)\log(\lambda_p-u)
 +v\log v+w\log w
 +(\lambda_n-v-w)\log(\lambda_n-v-w).
\tag{A.3}
\]

## Dual function

For

\[
\theta=(u,v,w,q,\beta,e)
\]

and dual parameters

\[
y=(\nu_{ps},\nu_{ns1},\nu_{ns2},\mu_{ps},\mu_{ns1},\mu_{ns2},z,\eta,\zeta),
\]

where the first seven entries are positive and the last two are real, define

\[
\begin{aligned}
\mathcal D(\theta;y)=\;&C_\ell(u,v,w)+h_{ps}\log\nu_{ps}\\
&+\sum_{(i,j):j\ne1}\hat\delta_{i,j}
 \log\frac{\Psi_{i,j}(\nu)}{\hat\delta_{i,j}}\\
&+\sum_i\hat\delta_{i,1}
 \log\frac{\Psi^R_{i,1}(\nu,z;q,\beta,e)}{\hat\delta_{i,1}}\\
&+h_{ns}\log\frac{\Psi_H(\nu)}{h_{ns}}\\
&+\sum_{k=0}^3\hat\gamma_k
 \log\frac{\Psi_k^{Q,B}(\mu;\eta,\zeta)}{\hat\gamma_k}\\
&-u\log(\nu_{ps}\mu_{ps})
-v\log(\nu_{ns1}\mu_{ns1})
-w\log(\nu_{ns2}\mu_{ns2})\\
&-ev\log z-\eta qu
-\zeta\beta(\lambda_n-v-w).
\end{aligned}
\tag{A.4}
\]

Zero fixed masses are omitted from the corresponding `delta log(Psi/delta)` or `gamma log(Psi/gamma)` sums.

## Theorem — conditional dual upper bound

Let `F_R(x)` denote the Díaz exponential objective `F(x)` multiplied by the iid-priority rescue factor `prod_i s_i^{t_{i,1}}`.  For every feasible source point `x` with normalized outer coordinates `theta`, and for **every** dual tuple `y` as above,

\[
\boxed{\log F_R(x)\le \mathcal D(\theta;y).}
\tag{A.5}
\]

Consequently

\[
\sup_{x\in P}\log F_R(x)
\le
\sup_{\theta\in\Omega}
\inf_y\mathcal D(\theta;y),
\tag{A.6}
\]

where it is already safe to use the simple compact relaxation

\[
\Omega=\{0\le u\le\lambda_p,\ v,w\ge0,\ v+w\le\lambda_n,\ 0\le q,\beta,e\le1\}.
\tag{A.7}
\]

If the fiber with fixed exact aggregates `(u,v,w,qu,beta( lambda_n-v-w),ev)` has a relative-interior feasible point, then ordinary finite-dimensional entropy duality gives equality between its primal maximum and `inf_y D`; hence the reduction is exact on such fibers.  Boundary fibers still obey the one-sided bound (A.5), which is all an upper-threshold certificate needs.

## Proof

The proof is only repeated applications of the log-sum inequality

\[
\sum_r x_r\log\frac{a_r}{x_r}
\le X\log\frac{\sum_r a_r}{X},\qquad X=\sum_r x_r,
\tag{A.8}
\]

with equality iff `x_r` is proportional to `a_r` on its active support.

### Variable blocks, `j != 1`

For fixed degree `(i,j)`, apply (A.8) to the true state of weight `nu_ps^i` and the false states `k=1,...,j` of weights

\[
{j\choose k}\nu_{ns1}^k\nu_{ns2}^{j-k}.
\]

The total mass is `hat_delta_{i,j}` by source constraint (11), so

\[
\begin{aligned}
&-t_{i,j}\log t_{i,j}
-\sum_k f_{i,j,k}\log\frac{f_{i,j,k}}{{j\choose k}}\\
&\le
\hat\delta_{i,j}\log\frac{\Psi_{i,j}}{\hat\delta_{i,j}}
-i t_{i,j}\log\nu_{ps}
-\sum_k kf_{i,j,k}\log\nu_{ns1}
-\sum_k(j-k)f_{i,j,k}\log\nu_{ns2}.
\end{aligned}
\tag{A.9}
\]

### Rescue-modified `j=1` blocks

For `(i,1)`, the rescued objective has the additional term `t_{i,1} log s_i`.  Apply (A.8) to weights `nu_ps^i s_i` and `z nu_ns1`:

\[
\begin{aligned}
&-t_{i,1}\log t_{i,1}-f_{i,1,1}\log f_{i,1,1}
+t_{i,1}\log s_i\\
&\le
\hat\delta_{i,1}\log\frac{\Psi^R_{i,1}}{\hat\delta_{i,1}}
-i t_{i,1}\log\nu_{ps}
-f_{i,1,1}\log\nu_{ns1}
-f_{i,1,1}\log z.
\end{aligned}
\tag{A.10}
\]

Summing the last term gives `-E log z=-ev log z`.

### Heavy negative split

Source constraint (12) and weights `(nu_ns1,nu_ns2)` give

\[
-h_{ns1}\log h_{ns1}-h_{ns2}\log h_{ns2}
\le h_{ns}\log\frac{\nu_{ns1}+\nu_{ns2}}{h_{ns}}
-h_{ns1}\log\nu_{ns1}-h_{ns2}\log\nu_{ns2}.
\tag{A.11}
\]

### Clause blocks with the two rescue aggregates

For fixed syntactic positive-literal count `k`, source constraint (14) gives total mass `hat_gamma_k`.  Apply (A.8) with the weights in (A.2).  Summing over `k` and using source copy constraint (18) plus `Q=qu`, `B=beta ell_nu` yields

\[
\begin{aligned}
-\sum_\alpha c_\alpha\log\bigl((w(\alpha)!/2)c_\alpha\bigr)
\le\;&
\sum_k\hat\gamma_k\log\frac{\Psi_k^{Q,B}}{\hat\gamma_k}\\
&-u\log\mu_{ps}-v\log\mu_{ns1}-w\log\mu_{ns2}\\
&-\eta qu-\zeta\beta(\lambda_n-v-w).
\end{aligned}
\tag{A.12}
\]

### Collecting copy constraints

Source constraint (17) says

\[
\sum i t_{i,j}=u-h_{ps},\qquad
\sum kf_{i,j,k}=v-h_{ns1},\qquad
\sum(j-k)f_{i,j,k}=w-h_{ns2}.
\]

Combining these with (A.11) changes all variable-side multiplier terms into

\[
h_{ps}\log\nu_{ps}-u\log\nu_{ps}-v\log\nu_{ns1}-w\log\nu_{ns2}.
\]

Adding the fixed copy numerator `C_ell` from the definition of source `F` and then (A.12) gives exactly (A.4), proving (A.5).

For relative-interior fibers, the conditional objective is a finite sum of strictly concave negative-entropy terms plus fixed linear weights, over a compact polytope cut out by linear equalities.  Standard Lagrange/Fenchel duality therefore has no gap; its logarithmic multipliers are precisely `(nu,mu,z,eta,zeta)`.  This proves the equality assertion on such fibers.  Weak duality (A.5) needs no interior assumption.

## Why the tempting direct use of Díaz equation (25) is invalid

The positive copy-entropy term has the opposite curvature.  Even for only `ps` versus `pu`, total `lambda=1`, and `r=nu_ps mu_ps=2`, the post-dual copy term is

\[
H(x)=x\log x+(1-x)\log(1-x)-x\log2.
\]

The stationary point is `x=2/3` and

\[
H(2/3)=-\log3,
\]

whereas the boundary value is

\[
H(0)=0>-\log3.
\]

More generally, `H''(x)=1/x+1/(1-x)>0`, so the Díaz stationary copy split minimizes this one-dimensional block.  Thus their equation (25) is a critical-point value, exactly as the paper states; it cannot simply be reinterpreted as an arbitrary-multiplier global upper bound.  Fixing `(u,v,w)` is what removes this wrong-curvature obstruction.

## Source-level meaning

At `M=23`, the source ambient primal dimension is

\[
K=(M+1)^2(1+M/2)+23=7223.
\]

(A.6) reduces the **adversarial outer maximization** to six scalar coordinates; the nine dual coordinates are minimizing certificate parameters, not additional adversarial primal coordinates.  This is auxiliary mechanism progress only.  A threshold improvement still requires a rigorous interval proof that, at some `alpha<4.4898`, the source prefactor `B` and continuity slack satisfy

\[
(1+10^{-7})B\exp\left\{\sup_{\theta\in\Omega}\inf_y\mathcal D(\theta;y)\right\}<1,
\]

with the `M=23` heavy/light truncation and simple-formula transfer retained.
