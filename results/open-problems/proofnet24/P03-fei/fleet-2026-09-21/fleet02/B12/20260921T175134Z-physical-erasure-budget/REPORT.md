TASK: B12 ACCOUNT: fleet02 RUN: 2026-09-21T17:51:34.622415Z — exact physical erasure budget for derivative Palm rows

**Role:** FEI approach 1 — spectral-sample compression / sequential prediction  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; no authenticated brain retrieval or receiver-context use occurred.  
**Status:** **SUBSTANTIVE PARTIAL PROGRESS. Full uniform-cube FEI remains OPEN / NOT PROVED.**

## 0. Fresh state and non-overlap

I read the required FEI continuation in owner order (`TASKS_2026-09-21.md`, then `REPORT.md`, then `APPROACHES.md`), the fresh P03 README and repository entry rules, then the newest relevant B12/B13/B17/B18 handoffs visible before this write. The corrected unrestricted lower bound remains above `6.521845710923046575`; the certified read-once theorem remains a structured theorem only.

This run continues the preceding fleet02/B12 depth-rigidity result. That result introduced, for a Boolean derivative row, an exact depth defect split into support-isoperimetric and internal-sign slacks, and showed that scalar Palm depth alone does not control terminal-to-prefix information. Fresh B13 work supplies block physical/spectral complementarity; fresh B18 work proves exact signed-subcube factorization and shows that an exact-subcube residual sign is itself a lower-dimensional FEI instance. A fresh fleet03/B17 route studies **spectral** total correlation after character gauge. I do not duplicate those routes here. The new object below is the **physical dual total correlation of the sensitive-fibre distribution conditioned on derivative sign**, and it is shown to be exactly conserved by the B12 depth slacks.

Creative moves from `FLEET_RULES.md` used here, different from the preceding B12 run, are **#3 prove a stronger statement** (an exact conservation law rather than another inequality), **#11 dualize** (move from the Palm Fourier law to the physical sensitive-fibre law of the same derivative state), and **#25 count the same thing twice** (same-sign cube edges versus conditional erasure entropy).

No publication-priority claim is made. The only external stability theorem used below is David Ellis, *Almost Isoperimetric Subsets of the Discrete Cube*, CPC 20 (2011), whose theorem gives dimension-free closeness to a subcube from small excess average boundary degree.

## 1. Setup and the previous B12 defect split

Let
\[
g:\{0,1\}^m\to\{0,\pm1\}
\]
be a nonzero Boolean derivative row. Put
\[
E=\{x:g(x)\ne0\},\qquad j=\Pr[x\in E]=\mathbb E g^2>0.
\]
With normalized Walsh coefficients, the derivative Palm law is
\[
\nu(A)=\frac{\widehat g(A)^2}{j}.
\]
Let
\[
d_g=\sum_{r=1}^m\|D_rg\|_2^2,
\qquad
M=\mathbb E_{A\sim\nu}|A|=\frac{d_g}{j},
\qquad
L=\log_2\frac1j.
\]
The B12 depth defect is
\[
\Delta=M-\frac L2.
\tag{1.1}
\]
Write `I(1_E)` for the ordinary total influence of the support indicator. The preceding B12 run used
\[
S_{\rm iso}:=I(1_E)-2jL\ge0,
\qquad
S_{\rm sign}:=4d_g-I(1_E)\ge0,
\tag{1.2}
\]
and the exact identity
\[
\boxed{S_{\rm iso}+S_{\rm sign}=4j\Delta.}
\tag{1.3}
\]
`S_iso` is the weak edge-isoperimetric excess of the support and `S_sign` is the extra derivative energy from internal sign-changing edges.

## 2. New exact theorem: depth defect is a physical erasure-information budget

Draw `X` uniformly from `E` and let
\[
\Sigma=g(X)\in\{\pm1\}.
\]
Define the conditional dual total correlation
\[
\operatorname{DTC}(X\mid\Sigma)
:=H(X\mid\Sigma)-\sum_{r=1}^m H(X_r\mid X_{-r},\Sigma).
\tag{2.1}
\]
This is nonnegative by Han/Shearer, but only the definition is needed for the identity.

### Theorem B12-PHYSICAL-ERASURE-CONSERVATION

For every nonzero `g:{0,1}^m->{0,±1}`,
\[
\boxed{
\mathcal E_{\rm phys}(g)
:=H(\Sigma)+\operatorname{DTC}(X\mid\Sigma)
=\frac{S_{\rm iso}}{2j}+\frac{S_{\rm sign}}{4j}.
}
\tag{2.2}
\]
Equivalently, using (1.3),
\[
\boxed{
\mathcal E_{\rm phys}(g)
=\Delta+\frac{S_{\rm iso}}{4j}
=2\Delta-\frac{S_{\rm sign}}{4j}.
}
\tag{2.3}
\]
Hence
\[
\boxed{\Delta\le\mathcal E_{\rm phys}(g)\le2\Delta,}
\tag{2.4}
\]
and the two old slacks can be recovered exactly from the two scalar quantities `Delta` and `E_phys`:
\[
\boxed{
S_{\rm iso}=4j(\mathcal E_{\rm phys}-\Delta),
\qquad
S_{\rm sign}=4j(2\Delta-\mathcal E_{\rm phys}).
}
\tag{2.5}
\]

### Proof

Let `e_=` be the number of cube edges whose two endpoints lie in `E` and have the same sign, `e_+-` the number whose two endpoints lie in `E` with opposite signs, and `b=|partial E|` the number of support-boundary edges.

Because `X` is uniform on `E`,
\[
H(X)=\log_2|E|=m+\log_2 j.
\tag{2.6}
\]
For a fixed coordinate `r`, after conditioning on `(X_{-r},Sigma)` there are either one or two admissible values of `X_r`. There are two exactly when the corresponding `r`-edge is an internal same-sign edge. Therefore
\[
\sum_r H(X_r\mid X_{-r},\Sigma)=\frac{2e_=}{|E|}.
\tag{2.7}
\]
Since `Sigma` is a deterministic function of `X`,
\[
H(\Sigma)+H(X\mid\Sigma)=H(X).
\]
Also
\[
m|E|=2e_=+2e_{+-}+b.
\tag{2.8}
\]
Combining (2.6)--(2.8),
\[
\mathcal E_{\rm phys}
=\frac b{|E|}+\frac{2e_{+-}}{|E|}-L.
\tag{2.9}
\]
On the other hand, with the present derivative normalization,
\[
I(1_E)=\frac{2b}{2^m},
\qquad
 d_g=\frac{b}{2\,2^m}+\frac{2e_{+-}}{2^m}.
\tag{2.10}
\]
Since `j=|E|/2^m`, substituting (2.10) into (1.2) turns (2.9) exactly into (2.2). Equation (2.3) follows from (1.3), and then (2.4)--(2.5) are immediate. `QED`

## 3. Exact sequential-prediction form

For every ordering `pi=(pi_1,...,pi_m)`, the chain rule gives
\[
\operatorname{DTC}(X\mid\Sigma)
=
\sum_{t=1}^m
I\!\left(
X_{\pi_t};X_{\pi_{t+1:m}}
\mid X_{\pi_{1:t-1}},\Sigma
\right).
\tag{3.1}
\]
Thus (2.2) has the genuinely sequential form
\[
\boxed{
\mathcal E_{\rm phys}
=H(\Sigma)+
\sum_t I(X_{\pi_t};X_{\pi_{>t}}\mid X_{\pi_{<t}},\Sigma),
}
\tag{3.2}
\]
independently of the order. The depth defect therefore does not merely say that a Palm row is deep; up to the explicit factor interval `[1,2]`, it is exactly the amount of **physical sign information plus future/past predictive dependence** present in the sensitive-fibre distribution.

For a full-support Boolean function `sigma:{0,1}^m->{±1}`, `j=1`, `S_iso=0`, and `Delta=I(sigma)`. The theorem specializes to the elementary exact identity
\[
\boxed{
I(\sigma)=H(\sigma(X))+\operatorname{DTC}(X\mid\sigma(X)).
}
\tag{3.3}
\]
This specialization is not claimed as new; it is recorded because it shows exactly what the B12 derivative defect becomes on the B18 residual Boolean factor.

Two endpoints now have a clean interpretation:

* exact-subcube support (`S_iso=0`): `E_phys=Delta`; by the fresh B18 factorization, `Delta` is precisely the influence of the lower-dimensional residual sign function;
* constant sign on support (`S_sign=0`): `E_phys=2 Delta`; all defect is geometric support dependence.

So the B18 signed-subcube recursion and the preceding B12 support-stability programme are not separate phenomena: (2.5) gives an exact interpolation between them.

## 4. New quantitative consequence: a dimension-free TV-stable signed-subcube Palm row

The previous B12 run identified a quantitative row-shape theorem as the next missing local bridge. At the level of total variation, it can now be completed.

Set
\[
\epsilon_{\rm iso}:=\frac{S_{\rm iso}}{2j}
=2(\mathcal E_{\rm phys}-\Delta).
\tag{4.1}
\]
Then the support average boundary degree is
\[
\frac{|\partial E|}{|E|}=L+\epsilon_{\rm iso}.
\]
For `epsilon_iso` below the absolute threshold in Ellis's 2011 stability theorem, there is a coordinate subcube `Q` such that
\[
\delta:=\frac{|E\triangle Q|}{|E|}
\le
\frac{2\epsilon_{\rm iso}}{\log_2(1/\epsilon_{\rm iso})}.
\tag{4.2}
\]
Let
\[
\theta=\min\{\Pr(\Sigma=1),\Pr(\Sigma=-1)\}.
\]
From (2.2),
\[
h_2(\theta)=H(\Sigma)\le\mathcal E_{\rm phys}\le2\Delta.
\tag{4.3}
\]
Choose the majority sign `s` and put `h=s 1_Q`. Then directly
\[
\|g-h\|_2^2
\le j(\delta+4\theta).
\tag{4.4}
\]
Writing `q=mu(Q)`, the symmetric-difference bound gives `|q/j-1|<=delta`. If `delta<1`, normalization and (4.4) give
\[
\left\|\frac g{\sqrt j}-\frac h{\sqrt q}\right\|_2
\le
\sqrt{\delta+4\theta}
+
\frac{\delta}{1+\sqrt{1-\delta}}
=:\tau.
\tag{4.5}
\]
Walsh transform is unitary, and for unit vectors `a,b`,
\[
\frac12\sum_A\bigl||a_A|^2-|b_A|^2\bigr|
\le\|a-b\|_2.
\]
Therefore, if `nu_g` is the derivative Palm law and `nu_Q` is the uniform law on all subsets of the fixed-coordinate set of `Q`,
\[
\boxed{
\operatorname{TV}(\nu_g,\nu_Q)\le\tau.
}
\tag{4.6}
\]
Because `epsilon_iso -> 0` and `theta -> 0` when `Delta -> 0`, this is a dimension-free **TV row-shape stability theorem**. It strengthens the previous exact-equality rigidity to a quantitative statement. It does **not** yet control Shannon entropy.

## 5. Decisive obstruction: TV stability plus first moment is not a Shannon bridge

The last caveat is essential. Let `R` be the uniform subset law on a fixed set `F` of size `r`. For integer `k>=2`, introduce a disjoint pool `U_k` of
\[
N_k=2^{k^2}
\]
fresh coordinates and put `epsilon_k=1/k`. Define an abstract subset law `P_k` by:

* with probability `1-epsilon_k`, draw `A~R` and output `A`;
* with probability `epsilon_k`, draw `A~R`, choose `J` uniformly from `U_k`, and output `A union {J}`.

The two branches have disjoint supports, so exactly
\[
\operatorname{TV}(P_k,R)=\epsilon_k=\frac1k,
\tag{5.1}
\]
\[
\mathbb E_{P_k}|S|-\frac r2=\frac1k,
\tag{5.2}
\]
but
\[
\boxed{
H(P_k)-r
=h_2(1/k)+\frac1k\log_2N_k
=h_2(1/k)+k\to\infty.
}
\tag{5.3}
\]
Thus even `TV -> 0` **and** vanishing excess first moment do not imply any dimension-free Shannon excess bound for arbitrary subset laws. This construction is deliberately **not** claimed to be a Boolean Fourier row and therefore does not refute FEI. It refutes only the tempting continuation

> near-subcube TV control + mean-degree control => bounded Shannon loss.

The missing B12 ingredient must be cost-sensitive and Boolean/recursive: rare off-subcube spectral mass must have its **address entropy** paid, not merely its probability mass.

## 6. Executed checker

`check_physical_erasure_budget.py` was executed in this run using the Python standard library. It exhaustively checked every nonzero ternary function through dimension three:

* `8` rows in dimension 1,
* `80` rows in dimension 2,
* `6560` rows in dimension 3,
* `6648` total exact-structure cases.

It checked (2.2)--(2.5), the Parseval/Palm mean identity, and the deterministic normalized-TV proxy inequality underlying (4.5)--(4.6), with maximum conservation discrepancy `4.440892098500626e-16`, maximum Parseval mean discrepancy `2.220446049250313e-16`, and zero TV-bound violations. It also evaluated the synthetic family (5.1)--(5.3) through `k=32`; there the TV/mean excess has fallen to `1/32` while Shannon excess is already `32.20062232431272` bits. Result digest:

`39f6dc13bcaf46db591c0bd5821f7f6fd0f93e836424204dafffe67776d561ed`.

These finite checks support the algebra only. Ellis stability is an external proved theorem, and neither the checker nor the TV theorem proves full FEI.

## 7. Ledger and next attack

**PROVED in this run**

1. Exact physical erasure conservation (2.2)--(2.5) for every ternary Boolean derivative row.
2. Exact order-independent sequential-prediction decomposition (3.2).
3. A dimension-free TV-stable signed-subcube Palm-row theorem by combining the exact slack identity with Ellis stability and Fourier unitarity.
4. A sharp abstract obstruction showing that TV closeness plus first-moment closeness cannot by itself control Shannon entropy.

**NOT PROVED**

* Full FEI.
* A Shannon-stable near-subcube row theorem.
* Any dimension-independent conversion from the new physical erasure budget to spectral entropy beyond the already equivalent full-FEI target.

**Next B12 target.** Use (3.2) as the payment ledger and the B18 exact-subcube recursion as the zero-geometric-defect endpoint. The next nontrivial bridge is to orient the Ellis subcube `Q`, split the Palm spectrum into its fixed-coordinate and free-coordinate parts, and prove a **Boolean address-entropy inequality** for the rare off-`Q` component. It must charge selector/address entropy to the physical erasure increments in (3.2), not to total variation alone, and it must reduce exactly to lower-dimensional FEI on the `S_iso=0` branch.
