TASK: B18 ACCOUNT: account02 RUN: 2026-09-21T17:06:05Z — arbitrary-q-flip dependent-triple Radon dictionary and frame-normalized FEI compiler criterion

MODEL: GPT-5.6 Sol (self-report)
THINKING LEVEL: UNKNOWN / NOT_EXPOSED; maximum actually supported was requested
THINKING USAGE: NOT_EXPOSED; provider reasoning tokens/time unavailable
EXECUTION: WITHOUT_VERIFIED_BRAIN
FULL FEI STATUS: OPEN / NOT PROVED

# 0. Fresh state and route


Fresh `math-open-problems` master was observed at `0cb5cad0698c4e84db435228f5b26ba13200ee9f` and then `db4a4a3ec92a2dd6cf8d0f84ae54f5dd0afad854`. I read the current `FLEET_RULES.md`, `proofnet24/P03-fei/README.md`, the owner-required read-once `TASKS_2026-09-21.md`, `REPORT.md`, and `APPROACHES.md`, then the newest compatible B16/B18/B13 reports. The current unrestricted lower-bound target is already above `6.521845710923046575`; the old `6.4547837` unrestricted target is obsolete. Full FEI remains open.

The three FLEET_RULES moves used here are:

- **#25 COUNT THE SAME THING TWICE:** identify one physical q-flip derivative disagreement simultaneously as a rank-two three-local spectral/sensitivity transport distance.
- **#11 DUALIZE:** turn that local transport kernel into an exact conditionally-negative-type Hilbert energy on an arbitrary q-flip quotient.
- **#20 FIND WHY THE ALGORITHM FAILS:** isolate the exact frame-normalization obstruction that remains when one tries to sum arbitrary-q-flip source payments.

This is not an audit of the fresh account03/B18 theorem. It uses that theorem as an input and derives a new source-exact dictionary and a stricter compiler criterion.

# 1. Inputs at their exact proved scopes

Let `G=F_2^n`, let `f:G->{-1,+1}`, and let the spectral sample `Xi` have law

\[
\Pr(\Xi=\xi)=\widehat f(\xi)^2.
\]

For a translation `u` define

\[
A_u=\langle\Xi,u\rangle\pmod2,
\qquad
B_u(x)=\mathbf 1\{f(x)\ne f(x+u)\},
\qquad
I_u=\mathbb E B_u.
\]

The fresh account03/B18 theorem proves for every three translations `u,v,w` that the laws of `(A_u,A_v,A_w)` and `(B_u,B_v,B_w)` have identical one- and two-bit marginals and differ only in the cubic Walsh moment. Writing

\[
\tau_{u,v,w}=\mathbb E f(X)f(X+u)f(X+v)f(X+w),
\qquad c_r=\mathbb E f(X)f(X+r),
\]

its cubic discrepancy is

\[
d_{u,v,w}=\frac{\tau_{u,v,w}-c_{u+v+w}}8,
\]

and it proves the sharp identities/bound

\[
W_1^{\rm Ham}=\mathrm{TV}=4|d_{u,v,w}|,
\qquad
|d_{u,v,w}|\le\frac{I_u+I_v+I_w}{6}.
\tag{1.1}
\]

The fresh account03/B16 theorem independently reduces the full paired-selector defect to a double-resolvent current of genuine third finite differences. The fresh account01/B16 theorem gives an exact Hilbert/Radon payment when the pivot is a physical coordinate. The point below is that the source-side Hilbert theorem is in fact valid for **every nonzero q-flip pivot**, and for a special dependent triple its local transport metric is exactly the Radon kernel.

# 2. PROVED: dependent-triple transport equals q-flip derivative disagreement exactly

Fix a nonzero translation `u`. Define the derivative indicator

\[
\eta_u(x)=B_u(x)=\frac{1-f(x)f(x+u)}2.
\tag{2.1}
\]

For another translation `v`, define the derivative-disagreement kernel

\[
p_u(v)=\Pr_X\{\eta_u(X)\ne\eta_u(X+v)\}.
\tag{2.2}
\]

## Theorem B18-QFLIP-DEPENDENT-TRIPLE-DICTIONARY

For every Boolean `f`, every nonzero `u` and every `v`, the special dependent q-flip triple

\[
(u,v,u+v)
\]

satisfies

\[
\boxed{
 d_{u,v,u+v}=-\frac14p_u(v)
}
\tag{2.3}
\]

and hence

\[
\boxed{
W_1^{\rm Ham}
\bigl(\operatorname{Law}(A_u,A_v,A_{u+v}),
      \operatorname{Law}(B_u,B_v,B_{u+v})\bigr)
=p_u(v).
}
\tag{2.4}
\]

Consequently the fresh sharp three-local theorem gives the universal q-flip derivative inequality

\[
\boxed{
p_u(v)\le\frac23\bigl(I_u+I_v+I_{u+v}\bigr).
}
\tag{2.5}
\]

The constant `2/3` is sharp already on a rank-two one-minority-vertex face.

### Proof

Because the three spectral parity bits are linearly dependent,

\[
A_u\oplus A_v\oplus A_{u+v}=0,
\]
so the spectral all-ones probability is zero. More directly, in the cubic-discrepancy formula `u+v+(u+v)=0`, so `c_0=1`.

On the physical side,

\[
\begin{aligned}
\tau_{u,v,u+v}
&=\mathbb E f(X)f(X+u)f(X+v)f(X+u+v)\\
&=\mathbb E\bigl[(-1)^{\eta_u(X)}(-1)^{\eta_u(X+v)}\bigr]\\
&=1-2p_u(v).
\end{aligned}
\]

Therefore

\[
d_{u,v,u+v}=\frac{(1-2p_u(v))-1}{8}=-\frac14p_u(v),
\]

which is (2.3). Insert this into `W_1=4|d|` from (1.1) to get (2.4), and then insert it into the sharp `|d|` bound to get (2.5). QED.

### Meaning

The account01 source kernel was not merely analogous to account03's local q-flip transport. It **is exactly that transport distance** on the dependent face `(u,v,u+v)`. This identifies the precise local observable that a compiler/Radon representation should target; no representation change or generic Hamming path is needed at source level.

# 3. PROVED: arbitrary-q-flip energy distance

Since

\[
\eta_u(x+u)=\eta_u(x),
\]
`eta_u` descends canonically to the quotient

\[
W_u=G/\langle u\rangle.
\]

Let the nonconstant quotient Walsh labels be `xi in u^perp\setminus{0}` and put

\[
a_u(\xi)=\widehat{\eta_u}(\xi)^2,
\qquad
E_u=\sum_{\xi\ne0}a_u(\xi)=I_u(1-I_u).
\tag{3.1}
\]

Fourier inversion gives

\[
\boxed{
p_u(v)=2E_u-2\sum_{\xi\ne0}a_u(\xi)(-1)^{\langle\xi,v\rangle}.}
\tag{3.2}
\]

For probability measures `rho,sigma` on `W_u`, define

\[
\mathfrak D_u(\rho,\sigma)
=2\mathbb E_{R\sim\rho,S\sim\sigma}p_u(R+S)
-\mathbb E_{R,R'\sim\rho}p_u(R+R')
-\mathbb E_{S,S'\sim\sigma}p_u(S+S').
\tag{3.3}
\]

## Theorem B18-ARBITRARY-PIVOT-QFLIP-ENERGY

For every nonzero q-flip direction `u`,

\[
\boxed{
\mathfrak D_u(\rho,\sigma)
=2\sum_{\xi\ne0}a_u(\xi)
  \bigl(\widehat\rho(\xi)-\widehat\sigma(\xi)\bigr)^2
\ge0.
}
\tag{3.4}
\]

Thus the exact local three-bit transport metric in (2.4), viewed as the translation kernel `p_u`, is conditionally negative type for **every q-flip pivot**, not only for physical coordinate pivots.

### Proof

Insert (3.2) into each of the three terms of (3.3). The constant `2E_u` cancels. For each nonzero `xi`, the remaining coefficient is

\[
-4\widehat\rho(\xi)\widehat\sigma(\xi)
+2\widehat\rho(\xi)^2+2\widehat\sigma(\xi)^2
=2(\widehat\rho(\xi)-\widehat\sigma(\xi))^2.
\]

Summing with weights `a_u(xi)>=0` proves (3.4). QED.

# 4. PROVED: central odd square payment for any q-flip pivot

Choose any linear basis of the quotient `W_u ~= F_2^{n-1}`. For `0<=t<=1/2`, let

\[
\rho_t=\operatorname{Ber}((1-t)/2)^{\otimes(n-1)},
\qquad
\sigma_t=\operatorname{Ber}((1+t)/2)^{\otimes(n-1)}.
\tag{4.1}
\]

For a quotient Walsh label of Hamming weight `k`,

\[
\widehat\rho_t=t^k,
\qquad
\widehat\sigma_t=(-t)^k.
\]

Set

\[
\delta_u(t)=\mathbb E_{\rho_t}p_u-\mathbb E_{\sigma_t}p_u.
\tag{4.2}
\]

Then

\[
\boxed{
\delta_u(t)=-4\sum_{|\xi|\ {m odd}}a_u(\xi)t^{|\xi|}
}
\tag{4.3}
\]

and

\[
\boxed{
\mathfrak D_u(\rho_t,\sigma_t)
=8\sum_{|\xi|\ {m odd}}a_u(\xi)t^{2|\xi|}.
}
\tag{4.4}
\]

Define

\[
\mathcal S_u
=\int_0^{1/2}t(1/2-t)\delta_u(t)^2\,dt.
\tag{4.5}
\]

## Theorem B18-ARBITRARY-PIVOT-CENTRAL-SQUARE

For every nonzero q-flip pivot `u` and every quotient basis,

\[
\boxed{
\mathcal S_u
\le\frac1{40}
\left[\sum_{|\xi|\ {m odd}}2^{-(|\xi|-1)}a_u(\xi)\right]^2
\le\frac{E_u^2}{40}.
}
\tag{4.6}
\]

### Proof

Equation (4.3) follows from (3.2): the constant mode cancels between the two measures, even levels cancel, and odd levels double. Equation (4.4) follows from (3.4).

Expanding the square in (4.5), for odd `k,l>=1` use

\[
\int_0^{1/2}t^{k+l+1}(1/2-t)\,dt
=\frac{2^{-(k+l+3)}}{(k+l+2)(k+l+3)}.
\]

Because `(k+l+2)(k+l+3)>=20`, each coefficient after multiplication by `16` is at most

\[
\frac1{40}2^{-(k-1)}2^{-(l-1)}.
\]

Summing proves the first inequality, and dropping the damping factors proves the second. QED.

This is the account01 central-Radon square theorem with the physical-coordinate hypothesis removed. The price is that an unrestricted compiler must now control how many arbitrary pivots it uses and with what weights; that is addressed next.

# 5. PROVED: exact all-q-flip capacity identities

Let

\[
\mu(\xi)=\widehat f(\xi)^2,
\qquad
c_u=\mathbb E f(X)f(X+u)=\sum_\xi\mu(\xi)(-1)^{\langle\xi,u\rangle}.
\tag{5.1}
\]

Then `I_u=(1-c_u)/2` and `E_u=(1-c_u^2)/4`.

## Theorem B18-QFLIP-CAPACITY-MOMENTS

Summing over all `u in G` (the `u=0` terms vanish where appropriate),

\[
\boxed{
\sum_u I_u=2^{n-1}\bigl(1-\mu(0)\bigr)
=2^{n-1}\bigl(1-(\mathbb Ef)^2\bigr).
}
\tag{5.2}
\]

\[
\boxed{
\sum_u E_u
=2^{n-2}\left(1-\sum_\xi\mu(\xi)^2\right).
}
\tag{5.3}
\]

If

\[
\mathcal A_4(\mu)
:=\sum_{\xi_1+\xi_2+\xi_3+\xi_4=0}
  \mu(\xi_1)\mu(\xi_2)\mu(\xi_3)\mu(\xi_4),
\]
then

\[
\boxed{
\sum_u E_u^2
=2^{n-4}
\left(1-2\sum_\xi\mu(\xi)^2+\mathcal A_4(\mu)\right).
}
\tag{5.4}
\]

### Proof

Orthogonality of characters gives

\[
\sum_u c_u=2^n\mu(0),
\qquad
2^{-n}\sum_uc_u^2=\sum_\xi\mu(\xi)^2,
\]

and

\[
2^{-n}\sum_uc_u^4=\mathcal A_4(\mu).
\]

Insert `I_u=(1-c_u)/2`, `E_u=(1-c_u^2)/4`, and `E_u^2=(1-2c_u^2+c_u^4)/16`. QED.

These identities quantify the source bank before any compiler incidence weights are imposed.

# 6. PROVED conditional closure criterion: arbitrary-q-flip frames are sufficient

The previous B18 restriction integration established, for a restriction-maximal core `g` and target dimension `q`, the exact KL-refunded descent toll

\[
\Gamma_q(g)=\frac{\operatorname{UNPAID}_q(g)}{I(g)},
\qquad
\operatorname{UNPAID}_q=\mathcal R_q-K_q\ge0.
\tag{6.1}
\]

The fresh source theorem allows a strictly broader compiler target than the earlier physical-coordinate formulation.

## Theorem B18-QFLIP-FRAME-COMPILER

Assume that for one valid restriction step the **already fully refunded and KL-subtracted** compiler remainder satisfies

\[
\operatorname{UNPAID}_q(g)
\le
\Lambda
\sum_{r}\lambda_r\,\mathcal S_{u_r}^{(r)}(g),
\qquad \lambda_r\ge0,
\tag{6.2}
\]

where each `u_r` is any nonzero q-flip direction, each superscript `(r)` permits its own quotient basis, and `mathcal S` is the exact dependent-triple/Radon square from (4.5). If the induced pivot family has the dimension-free frame bound

\[
\boxed{
\sum_r\lambda_r E_{u_r}(g)^2\le A I(g),
}
\tag{6.3}
\]

then the step loses at most

\[
\boxed{
\Gamma_q(g)\le\frac{\Lambda A}{40}.
}
\tag{6.4}
\]

Hence there is a `q`-dimensional physical restriction child `h` with

\[
\frac{H(h)}{I(h)}
\ge
\frac{H(g)}{I(g)}-\frac{\Lambda A}{40}.
\tag{6.5}
\]

### Proof

Apply (4.6) to every term in (6.2):

\[
\operatorname{UNPAID}_q(g)
\le\frac{\Lambda}{40}
\sum_r\lambda_r E_{u_r}(g)^2
\le\frac{\Lambda A}{40}I(g).
\]

Divide by `I(g)` and use (6.1). QED.

The theorem is **conditional** only at (6.2)--(6.3). The source-side representation and payment are proved above. It says exactly what the fresh B16 double-resolvent current must deliver: not another local q-flip inequality, but a refund-preserving source representation whose weighted arbitrary-pivot capacities form a dimension-free frame.

# 7. REFUTED shortcut: unweighted arbitrary-pivot capacity has no dimension-free frame bound

The frame condition cannot be deleted.

Take the genuine Boolean phase

\[
f(x)=(-1)^{x_1x_2}
\]

with `n-2` dummy variables. Its folded physical influence is

\[
J(f)=\min(I_{e_1},1-I_{e_1})+\min(I_{e_2},1-I_{e_2})=1.
\]

For a translation `u=(a,b,*)`,

\[
f(x)f(x+u)=(-1)^{a x_2+b x_1+ab}.
\]

Thus if `(a,b)=(0,0)`, then `I_u=0,E_u=0`; if `(a,b)\ne(0,0)`, this derivative sign is a nonconstant character, hence

\[
I_u=\frac12,
\qquad E_u=\frac14,
\qquad E_u^2=\frac1{16}.
\]

There are exactly `3*2^{n-2}` such directions. Let `(U_1,...,U_n)` be a uniformly random ordered linear basis of `F_2^n`. Every `U_j` is uniform on the nonzero directions, so

\[
\boxed{
\mathbb E\sum_{j=1}^n E_{U_j}^2
=
\frac{3n\,2^{n-6}}{2^n-1}
\sim\frac{3n}{64},
}
\tag{7.1}
\]

while `J(f)=1`.

Therefore the proposed universal frame statement

\[
\sum_{u\in\mathcal B}E_u^2\le C J(f)
\]

for every or even average unit-weight q-flip basis with dimension-independent `C` is false. This does **not** say that the actual central square `mathcal S_u` must saturate `E_u^2/40` simultaneously. It says that a compiler proof using only the crude per-pivot capacity envelope (4.6) and then unit-summing pivots cannot close FEI. The double-resolvent/incidence weights or genuine signed cancellation must supply the missing normalization.

# 8. Exact obstruction after this integration

The fresh account03/B18 theorem removed the **local q-flip geometry** obstruction. The present run removes the **physical-coordinate pivot** obstruction on the source energy side. What remains is now exact:

> **ARBITRARY-Q-FLIP FRAME OBSTRUCTION.** Express the fully refunded double-resolvent compiler curl `Xi_ab(x,y)`, after the KL subtraction already isolated by B18, as a signed/weighted superposition of the dependent-face kernels `p_u(v)` (equivalently the local three-bit transport metrics (2.4)) such that the resulting weights satisfy a dimension-free frame inequality of the form (6.3). The representation must preserve dual-code multiplicity, plaquette signs, R16/moment refunds and the terminal mixed difference.

This is narrower than asking for another three-local transport theorem or another source norm. Account02/B16 should continue to own the signed compiler multiplier/refund algebra; B12/B13 own spectral/derivative profile structure; B14 owns erasure/selector structure; B15 owns packet/chain-rule structure; B17 owns normal forms. B18's nonoverlapping integration target is the frame-normalized compiler implication above.

# 9. Ledger

## PROVED in this run

- `B18-QFLIP-DEPENDENT-TRIPLE-DICTIONARY`: the dependent triple `(u,v,u+v)` has local spectral-vs-physical Hamming `W1` exactly equal to the derivative disagreement kernel `p_u(v)`.
- The sharp consequence `p_u(v) <= (2/3)(I_u+I_v+I_{u+v})`.
- `B18-ARBITRARY-PIVOT-QFLIP-ENERGY`: the local transport kernel is conditionally negative type for every nonzero q-flip pivot.
- `B18-ARBITRARY-PIVOT-CENTRAL-SQUARE`: the account01 central odd source square bound extends verbatim to every q-flip pivot.
- `B18-QFLIP-CAPACITY-MOMENTS`: exact first, quadratic and fourth-additive-energy aggregate identities (5.2)--(5.4).
- The implication `B18-QFLIP-FRAME-COMPILER`: (6.2)+(6.3) imply the FEI descent toll (6.4).

## CONDITIONAL

- Any FEI closure through (6.4) remains conditional on deriving the actual fully refunded compiler representation (6.2) and the dimension-free frame estimate (6.3).

## REFUTED at exact scope

- A dimension-free **unit-weight arbitrary-q-flip E^2 frame** controlled only by folded physical influence. The phase `(-1)^{x_1x_2}` gives expected basis load asymptotic to `3n/64` while `J=1`.
- Consequently, applying the per-pivot source capacity bound independently and summing pivots with unit weights is not a dimension-free proof strategy.

## OPEN

- The fully refunded compiler-to-dependent-face representation with the correct weights.
- A dimension-free frame bound after those exact weights, or a counterexample killing this compiler route.
- Full unrestricted FEI.

# 10. Literature applicability check

Fresh public literature checking during this run still found unrestricted FEI open. Potapov, arXiv:2609.21563 (18 September 2026), proves FEI for plateaued functions with sharp class constant 4 and for partially bent functions with sharp class constant 2; it does not cover arbitrary Boolean functions. Han's Combinatorica 45 (2025) bound retains the coordinate influence-profile entropy term. González--MacManus--Pereyra, arXiv:2606.00246, gives a restriction/stopping framework and explicitly leaves the universal branching inequality as the missing step. The current public FEI constant tracker records the certified Numaro lower bound `C>6.521845710923046575` and no finite universal upper bound. No novelty or publication-priority claim is made for the q-flip/Radon dictionary above.

# 11. Operational notes

The required current-hour login write to `math-research-brain` was attempted before substantive work and was blocked by the platform safety layer; no exclusive-work claim is made and the blocker is preserved as `CHECKIN_WRITE_BLOCKED`. Own-account scheduler inventory was inspected only: all 20 managed slots were enabled with hourly recurrences; B18 made zero scheduler mutations. Task-level quiet-delivery flags remained disabled for notifications/email. No broad mixed-domain memory, sealed benchmark answer, private archive, paid compute, workflow dispatch, email or Drive write was used.
