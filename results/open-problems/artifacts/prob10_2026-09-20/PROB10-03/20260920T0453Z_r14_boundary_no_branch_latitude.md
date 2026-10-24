Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum, and I do not claim otherwise.**

# PROB10-03 / R14 — no `B -> 0, D -> 1` complete-second stationary branch; adaptive-alpha and homogenized-latitude alternatives

Status: **PARTIAL / SOURCE OPEN / NEW RIGOROUS OBSTRUCTION / NO RIGOROUS THRESHOLD ENDPOINT MOVED**.

Frozen source model throughout:

`M=floor(alpha N)`, iid `g_a~N(0,I_N)`, `||sigma||_2=sqrt(N)`, and

`<g_a,sigma> >= -sqrt(N)` for all `a<=M`, with fixed `alpha` and `N->infinity`.

The repository-supported rigorous bracket entering and leaving this artifact is

`6.30297437506 <= alpha_c(-1) <= 12.78437096216`,

with width `6.48139658710`.

The complete-second-lift values near `12.75` and `12.78` mentioned below are **candidate/numerical unless explicitly certified**.

## 1. Consumed exact reduction

Use the already-proved complete-second-lift reduction

`q=pD^2`,

`c=(1-D^2)/(D(1-p)(1-pD^2))`,

`B=c/(4 gamma)`,

`f_{p,B}(z)=E_H exp[-B(sqrt(p)z+sqrt(1-p)H-1)_+^2]`,

`I=E_Z log f`, `I_B=partial_B I`, and `K=E_Z (partial_z log f)^2`.

On the complete interior branch,

`D^2=K/[-4p^2B^2I_B]`,

`alpha=-c^2/[4B^2I_B]`,

and the remaining stationarity equation is

`H(p,B,D):=I-BI_B-4B^2I_B A_0(p,D)=0`,

where

`A_0(p,D)=T_D/c_D`,

and `T_D` is taken with `gamma` held fixed before the stationary substitution.

The previous R14 `B->0` analysis proved only a **necessary equation coming from the `D^2` reconstruction**, and showed that this scalar necessary equation has a unique interior root. The theorem below checks the other stationarity equation at the same boundary and proves that the two requirements are incompatible. Thus the previous scalar root remains a correct necessary `D`-equation seed but is **superseded as a viable continuation route**.

## 2. Attack A — test the `B -> 0` deformation to destruction

Let

`u(x)=(x-1)_+`,

`mu_1=E[u(G)^2]`, `G~N(0,1)`.

For fixed `p in (0,1)`, let

`Y=sqrt(p)Z+sqrt(1-p)H-1`,

`r_p(Z)=E_H[Y_+ | Z]`,

and

`V_p=E_Z Var_H(Y_+^2 | Z)`.

### Theorem R14-T03-NO-B0-FULL-STATIONARY-BRANCH

There is no sequence of complete-second-lift stationary points `(p_n,B_n,D_n)` satisfying

`B_n -> 0`, `D_n -> 1`, and `p_n -> p_0 in (0,1)`.

In particular, the unique scalar boundary root previously found from the `D^2` equation cannot seed a complete stationary branch.

### Proof

#### Step 1: the `D^2` equation forces the old scalar boundary equation

At `B=0`, the conditional kernel equals one. Dominated differentiation gives

`I_B(p,0)=-mu_1`.

Also

`partial_z log f_{p,B}(z)/B -> -2 sqrt(p) r_p(z)`

in Gaussian `L^2`, so

`K(p,B)/B^2 -> 4p E[r_p(Z)^2]`.

Therefore, from

`D^2=K/[-4p^2B^2I_B]`,

any sequence with `D_n->1`, `B_n->0`, and `p_n->p_0` must satisfy

`E[r_{p_0}(Z)^2]=p_0 mu_1`.                                      (2.1)

Write the Hermite expansion of `u` as weights

`s_k=(E[u(G)He_k(G)])^2/k! >=0`.

Then

`E[r_p^2]=sum_{k>=0}s_k p^k`, `mu_1=sum_{k>=0}s_k`,

and for `p<1`

`E[r_p^2]-p mu_1=(1-p)G(p)`,

where

`G(p)=s_0-sum_{k>=2}s_k p(1+p+...+p^{k-2})`.

Since `s_2>0`, `G` is strictly decreasing on `(0,1)`. Hence (2.1) has at most one interior solution.

We now locate it rigorously below `1/4`.

Let

`phi=phi(1)`, `Q=P(G>1)`, `r=Q/phi`.

The exact checker accompanying this artifact proves, by rational lower Riemann sums and the elementary bound `(1-a/m)^m<e^{-a}`,

`13/20 < r < 33/50`.                                             (2.2)

For `u=(G-1)_+`,

`s_0=(phi-Q)^2=phi^2(1-r)^2`,

while Gaussian integration by parts gives

`E[u He_2]=phi`, hence `s_2=phi^2/2`.

At `p=1/4`,

`G(1/4) <= s_0-s_2/4`.

By the lower bound in (2.2),

`s_0/phi^2=(1-r)^2 < (7/20)^2=49/400 < 1/8 = (s_2/4)/phi^2`.

Thus `G(1/4)<0`, whereas `G(0)=s_0>0`. The unique root `p_*` of (2.1) therefore satisfies

`0<p_*<1/4`.                                                       (2.3)

#### Step 2: the remaining stationarity equation forces a second, incompatible equation

First compute the deterministic boundary term. With the inherited definitions of `T` and `c`, direct symbolic simplification gives

`lim_{D->1} A_0(p,D)=(1-p^2)/4`.                                 (2.4)

For the stochastic term, note that

`I_BB(p,0)=V_p`.

The identity

`d/dB [I-BI_B] = -B I_BB`

therefore gives, by dominated convergence,

`(I-BI_B)/B^2 -> -V_p/2`.                                        (2.5)

Using `I_B->-mu_1` and (2.4),

`[-4B^2 I_B A_0]/B^2 -> mu_1(1-p^2)`.                            (2.6)

Hence any complete stationary sequence with `H=0` and the stated boundary behavior must satisfy

`V_{p_0}=2 mu_1(1-p_0^2)`.                                      (2.7)

We show that (2.7) is impossible at the only possible `p_0=p_*` from Step 1.

Put `W=(G-1)_+^2`. Conditioning cannot increase second moment, so

`V_p = E Var(W|Z) <= E[W^2]`.

The elementary truncated-normal recurrence gives

`mu_1=E W=2Q-phi=phi(2r-1)`,

`E[W^2]=E(G-1)_+^4=10Q-6phi=phi(10r-6)`.

The upper bound `r<33/50` in (2.2) is exactly equivalent to

`E[W^2] < (15/8) mu_1`.                                         (2.8)

On the other hand, (2.3) gives

`2 mu_1(1-p_*^2) > 2 mu_1(1-1/16)=(15/8)mu_1`.                 (2.9)

Combining (2.8)-(2.9),

`V_{p_*} <= E[W^2] < (15/8)mu_1 < 2mu_1(1-p_*^2)`,

contradicting (2.7). This proves the theorem. QED.

### Exact finite certificate for (2.2)

The Mills ratio has the representations

`r=int_1^infty exp(-(t^2-1)/2) dt`,

and, by integration by parts,

`r=1-int_1^infty exp(-(t^2-1)/2)t^{-2} dt`.

On `[1,4]` both integrands are decreasing. With `h=3/400`, right endpoints `t_j=1+jh`, and `m=1000`, put

`L_j=(1-((t_j^2-1)/2)/m)^m`.

Since `L_j<exp(-(t_j^2-1)/2)`, exact rational arithmetic yields

`h sum_j L_j > 13/20`,

`h sum_j L_j/t_j^2 > 17/50`.

These imply (2.2). The checker executes these comparisons with `fractions.Fraction`; no floating-point number is used as a theorem premise.

## 3. Attack B — reduce ambition first: a `12.78` interior certificate candidate

The boundary deformation is now ruled out, so the highest-value upper-side route remains a true interior complete-second stationary certificate.

A different tactical choice is to certify **a smaller source improvement first** rather than immediately proving the larger `12.75` candidate. Using the already-proved closed one-dimensional kernel and exact two-scalar reconstruction, a numerical-only solve at

`alpha=12.78`

gives approximately

`p=0.6445929558545802`,

`B=4.8607761199420505`,

`D=0.6609587800306822`,

`Psi=0.016259103550683496>0`.

If independently outward-certified, this would move the upper endpoint by

`12.78437096216-12.78 = 0.00437096216`.

This is **NUMERICAL ONLY** and is not entered into the source metric. The point of the scout is methodological: the objective margin is slightly larger than at `12.75`, and one may choose an arbitrarily small Newton/Kantorovich box around a high-precision center, trading the size of the endpoint improvement for much weaker whole-box Hessian requirements. The unresolved ingredient is still directed compact integral enclosure, so no theorem endpoint is claimed here.

## 4. Attack C — exact homogenization to a fixed-latitude random cone

The affine threshold can be homogenized without changing the source problem.

For `x=sigma/sqrt(N)`, the source constraints are

`||x||=1`, `g_a dot x >= -1`.

Define

`y=(x,1)/sqrt(2) in S^N subset R^{N+1}`

and

`h_a=(g_a,1)`.

Then

`g_a dot x >= -1  <=>  h_a dot y >=0`,

and the last coordinate is fixed:

`y_{N+1}=1/sqrt(2)`.

Therefore

`SAT <=> {y in S^N: y_{N+1}=1/sqrt(2), h_a dot y>=0 for every a}` is nonempty.   (4.1)

This is an exact **fixed-latitude cone-intersection formulation**.

It is not directly Wendel/Cover: the normals `h_a=(g_a,1)` are not centrally symmetric or rotationally invariant in `R^{N+1}`, and the witness is restricted to one latitude rather than the full sphere. Thus a naive homogeneous-cone counting formula does not solve the negative-margin problem. What (4.1) does provide is a clean rank-one-deformation target for conic/intrinsic-volume methods: the only failure of isotropy is the deterministic last coordinate.

This is a distinct exact reformulation from the earlier polar-inradius statement; no threshold movement is claimed from it.

## 5. Source-level versus auxiliary movement

### Source metric

Before:

`alpha_L=6.30297437506`, `alpha_U=12.78437096216`, width `6.48139658710`.

After:

`alpha_L=6.30297437506`, `alpha_U=12.78437096216`, width `6.48139658710`.

**Movement: none.**

### Auxiliary movement

1. The previous `B->0, D->1` deformation fallback is now **rigorously impossible for complete stationarity**; its scalar root is only a necessary root of the `D` reconstruction, not a full branch seed.
2. A smaller `alpha=12.78` interior candidate is recorded as a potentially easier first rigorous source improvement, with every decimal explicitly numerical-only.
3. The affine feasibility problem has an exact fixed-latitude homogeneous-cone formulation, isolating a rank-one anisotropy rather than a generic affine obstruction.

## 6. Remaining full-scope gap

The full source remains open. The most direct source-moving obligation is still to certify one genuine interior complete-second stationary point with positive comparison value and then invoke the stationarized fl-RDT source implication. The `12.78` target can be used as a smaller first endpoint movement if its directed enclosure is materially easier than `12.75`; otherwise the existing `12.75` certificate candidate remains stronger.

The `B->0` deformation should **not** be pursued further unless the limiting regime changes (for example `D` does not tend to one, or a different lift/parameter scaling is used).

No claim of exact capacity, publication novelty, or independent validation is made.