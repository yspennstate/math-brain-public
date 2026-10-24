# B15 — KL/soft-max decomposition of unequal-magnitude collision cost

**Status:** OPEN / PARTIAL. Full uniform-cube FEI remains OPEN / NOT PROVED.

**Execution:** WITHOUT_VERIFIED_BRAIN. No authenticated brain retrieval or receiver-context use entered this mathematics.

**Role:** spectral remainder / unequal Fourier magnitudes. This run follows the joint arithmetic/Shannon interface D and does not rerun the read-once certificate.

## 1. Exact peer inputs consumed

This continuation uses, rather than re-proves, two cross-account results.

1. account02/B15, `20260921T170301Z-valuation-tail-majorization/REPORT.md`, blob `7633ed3dca15ea17d4c17af94e621f4ab3745691`: if packet valuation is `r_a` with packet mass `p_a`, and folded spectral marginals are `q_1^down >= ... >= q_n^down`, then

   `E_p (r_a-m+1)_+ <= 2 sum_{j=m}^n q_j^down`.

2. account04/B15, `20260921T121425Z-remote-gap-crossing/REPORT.md`, blob `066d1c993571817e71d4376247544bb81c975017`: for an equal-mass two-packet integral-selector catalyst with exponent gap `k`, the actual arithmetic-remainder increment against a Boolean seed B is

   `Delta D = (1/2) sum_{q,e} [ p_{q,e}(d_{q,e+k}-d_{q,e})_+ + p_{q,e+k}(d_{q,e}-d_{q,e+k})_+ ]`,

   where `d_{q,e}=e-r_{q,e}` after fixing the odd numerator chain. The same report gives an explicit Boolean family with `Delta D=k/4`, showing that a seed-only payment is impossible.

The point of the present run is to keep the information credit and the mesh/carry cost coupled instead of bounding either separately.

## 2. PROVED: every collision splits exactly into a KL term plus a soft-max infection term

Consider one recombination fibre with finitely many nonzero source masses `m_j>0` and source mesh depths `x_j` (real numbers suffice). Put

`P=sum_j m_j`, `lambda_j=m_j/P`, `M=max_j x_j`,

and let the arithmetic exponential tilt of the origin law be

`q_j = lambda_j 4^{x_j} / Z`, `Z=sum_j lambda_j 4^{x_j}`.

If recombination replaces all source depths by the finest depth `M`, then the arithmetic-remainder increase per unit fibre mass is

`C = M - sum_j lambda_j x_j`.

### Theorem B15-KL-SOFTMAX-01

Exactly,

`boxed{ C = (1/2) D_KL,2(lambda || q) + Psi(lambda,x) }`,

where

`boxed{ Psi(lambda,x) = M - (1/2) log_2 Z = -(1/2) log_2 sum_j lambda_j 4^{-(M-x_j)} }`.

Moreover

`0 <= Psi <= C`,

and for every `t>=0`, if

`F(t)=sum_{j:M-x_j<=t} lambda_j`,

then

`boxed{ Psi <= t + (1/2) log_2(1/F(t)) }`.

In particular, if `rho` is the total source mass at maximal depth, then

`boxed{ Psi <= (1/2) log_2(1/rho) }`.

### Proof

Since `q_j=lambda_j4^{x_j}/Z`,

`D_KL,2(lambda||q)=sum_j lambda_j(log_2 Z-2x_j)=log_2 Z-2 E_lambda x`.

Half of this plus `M-(1/2)log_2 Z` is `M-E_lambda x=C`.

Nonnegativity of `Psi` follows from `Z<=4^M`; `Psi<=C` follows from nonnegativity of KL. Finally

`sum_j lambda_j4^{-(M-x_j)} >= F(t)4^{-t}`,

which gives the tail bound after applying `-(1/2)log_2`. QED.

### Interpretation

This is the exact local version of the arithmetic negative-credit mechanism. If one keeps the fine source-origin arithmetic labels, `D_KL(lambda||q)/2` is the information-projection part of the recombination loss. What remains after that exact term is retained is not the raw depth gap; it is the soft maximum `Psi`.

This statement is deliberately local. It does **not** assert that an arbitrary global FEI proof may simply subtract these KL terms independently; a successful global bridge must preserve the same source-origin labels until the credits are spent.

## 3. Two-origin formula: gap and rarity trade off instead of adding

For two origins of depths `0` and `g>0`, let `rho` be the conditional mass of the depth-`g` origin. Then

`boxed{ Psi = -(1/2) log_2( rho + (1-rho)4^{-g} ) }`.

Consequently

`boxed{ Psi <= min{ g, (1/2)log_2(1/rho) } }`.

Thus after the exact arithmetic KL term is retained, a remote collision is expensive only when the finest source is simultaneously far away in mesh depth **and** rare in the origin mixture. This is the coupled mesh/information quantity missing from the earlier credit-free gap estimate.

## 4. PROVED: collision-mass and valuation-tail refinement of the account04 gap-k theorem

In the account04 equal-mass gap-`k` setting, write `r_e=r_{q,e}` and let `E_k` be the set of occupied pairs `(q,e)` for which both exponents `e` and `e+k` occur. Define

`C_k^- = sum_{(q,e) in E_k} p_{q,e}`,

`V_k^- = sum_{(q,e) in E_k} p_{q,e}(r_e-r_{e+k})_+`,

`V_k^+ = sum_{(q,e) in E_k} p_{q,e+k}(r_{e+k}-r_e-k)_+`.

### Theorem B15-GAP-TAIL-02

The actual arithmetic-remainder increment satisfies

`boxed{ Delta D <= (k/2) C_k^- + (1/2)V_k^- + (1/2)V_k^+ }`.

Consequently, with `J(B)=sum_i min(Inf_i(B),1-Inf_i(B))`,

`boxed{ Delta D <= (k/2) C_k^- + J(B) + sum_{j=k+1}^{n_B} q_j^down(B) }`.

### Proof

Use `d_e=e-r_e`. For each occupied pair,

`(d_{e+k}-d_e)_+=(k+r_e-r_{e+k})_+ <= k+(r_e-r_{e+k})_+`,

while

`(d_e-d_{e+k})_+=(r_{e+k}-r_e-k)_+`.

Insert these in the exact account04 collision identity. This proves the first display.

For the second, `V_k^-<=sum_a p_ar_a=R(B)<=2J(B)`. Also

`V_k^+ <= E_p(r_a-k)_+ <= 2 sum_{j=k+1}^{n_B} q_j^down(B)`

by the account02/B15 valuation-tail theorem with `m=k+1`. Divide the two valuation terms by two. QED.

This is a genuine strengthening of the earlier `k/2+2I(B)` estimate: it keeps the actual colliding lower-end mass, uses folded influence, and charges only the valuation tail that can exceed the geometric gap. It does not remove the bilateral catalyst cost, which is known to be necessary.

## 5. Exact stress test: the account04 remote-gap obstruction after KL refund

For the explicit Boolean family from account04/B15, the colliding sources have

`x=1/4`

at depth `0`, and

`y=(2^{k+1}-1)/2^{2k+2}`

at depth `k`. The raw collision cost is exactly `x k=k/4`.

Put `P=x+y` and `rho=y/P`. Theorem B15-KL-SOFTMAX-01 gives the exact split

`k/4 = (P/2)D_KL,2(lambda||q) + P Psi_k`,

where

`Psi_k=-(1/2)log_2(rho+(1-rho)4^{-k})`.

As `k->infinity`,

`P -> 1/4`, `rho ~ 2^{1-k}`,

so

`boxed{ P Psi_k = k/8 + O(1) }`,

and therefore the matching arithmetic KL term also contributes

`boxed{ (P/2)D_KL,2(lambda||q) = k/8 + O(1) }`.

Thus retaining the exact origin KL cancels **asymptotically one half** of the linear remote-gap infection in this sharp Boolean obstruction, but not all of it. The surviving soft-max term is still linear and must be paid bilaterally. Since the catalyst has `I(A_k)=k/2+1`,

`boxed{ (P Psi_k)/I(A_k) -> 1/4 }`.

Therefore this family forces constant at least `1/4` in any universal bilateral estimate that tries to pay precisely the post-KL soft-max residual only by `I(A)+I(B)`.

Selected values (computed directly from the displayed formulas):

| k | raw cost | KL part | soft-max residual |
|---:|---:|---:|---:|
| 2 | 0.500000 | 0.226235 | 0.273765 |
| 4 | 1.000000 | 0.556480 | 0.443520 |
| 8 | 2.000000 | 1.116766 | 0.883234 |
| 16 | 4.000000 | 2.124937 | 1.875063 |
| 32 | 8.000000 | 4.125000 | 3.875000 |

The raw `k/4` obstruction therefore should not be carried unchanged into a KL-preserving proof: half of it is information-projection loss, while the other half is genuine soft-max infection.

## 6. What this changes in the full FEI route

The account02 valuation theorem showed that pure valuation depth is strongly influence-controlled; account04 then showed that its complete stop-loss profile is nevertheless blind to the full remainder. The present calculation locates a more precise coupled object.

For every unequal-magnitude recombination fibre, do **not** pay

`max depth - average depth`

as one scalar. Keep its exact decomposition

`(information-projection KL)/2 + soft-max infection`.

The first term is the natural negative-credit object to preserve through the packet/product bridge. The genuinely new unpaid object is

`boxed{ P Psi = -(P/2) log_2 E_lambda[4^{-(M-X)}] }`.

It simultaneously sees mesh gaps and the rarity of near-maximal origins. Pure valuation tails lose the rarity information; raw gap bounds lose the KL cancellation.

A concrete next implication for account01/B15 is now:

> prove a dimension-free sum bound on the actual post-KL soft-max residuals, retaining the source-origin labels until the KL term has been matched to the global packet/product credit; or construct a Boolean family for which their sum divided by total influence diverges.

The remote-gap family proves that a successful bound needs coefficient at least `1/4` on the catalyst side, but it no longer forces payment of the full raw `k/4` collision.

## 7. Literature boundary

A fresh primary-source check on 21 September 2026 still finds unrestricted FEI open. Potapov (arXiv:2609.21563, 18 September 2026) proves sharp constants for plateaued and partially bent classes; González--MacManus--Pereyra (arXiv:2606.00246, 29 May 2026) develops a restriction/stopping-tree route and does not prove the full conjecture. No publication-priority claim is made for the identities above.

The old universal-sharp-Hod target is already retired by the recovered 18-variable Numaro lower bound. This report does not revive it.

## 8. Full-problem status

**Before:** OPEN. Valuation tails were influence-paid, but actual unequal-magnitude mesh infection and the necessary negative information credits had not been coupled at the collision level.

**After:** OPEN. Each collision now has an exact KL + soft-max decomposition, the gap-k theorem has a collision-mass/valuation-tail refinement, and the known remote-gap obstruction is quantitatively split into an asymptotic half-KL / half-soft-max cost. The remaining universal problem is a global payment of the soft-max residual with the matching KL credits kept live.
