# fleet01/B10 — physical marginal caps and a capped-Gibbs danger wedge

**Run:** `20260922T105609Z-b10-fei-2622b4`  
**Programme:** `FEI-ALL-TEAM-20260922T095941Z`  
**Assignment:** `FEI-20260922-fleet01-B10` / pathway B / Danger-region source constraint  
**Classification:** `ESSENTIAL_STEP_APPLIED / BOOLEAN_PHYSICAL_CAP / CAPPED_GIBBS_DANGER_WEDGE`  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Exact target and source state

The assigned target is to strengthen the mere near-product corridor for a possible negative Bellman source by imposing a genuinely Boolean restriction on the influence marginals. The exact source identity consumed is fleet02/B15 at commit `4bd6d05f1eb8325d665f2748f4d74dcee2550a04`:

\[
R_\Gamma=B_{\rm inf}^\Gamma+K_{\rm occ},\qquad
K_{\rm occ}=D_2(P\Vert Q_r),
\]

where `P` is the actual nonempty biased spectral law, `r_i=P(i\in S)=I_i^t/v`, and `Q_r` is the maximum-entropy conditional-product law with those marginals.

I also use fleet04/B17 at commit `603b35e74227d1c2d8ee34c0c527c439c686e30b`, which proves the biased Boolean quadratic equations and the one-equation KL lower bound

\[
K_{\rm occ}\ge {\mathfrak g_U(Q_r;p,q)^2\over 4vL_U^2\ln2}.
\]

The named OTHER-account partner result actually consumed is fleet02/B10 run `20260922T104655Z-f298f290`, immutable creation commit `fd0d86bca8aa49cea57cc6e6d4f5bd18e21374d3`. It proves exact payment on every balanced two-point perturbation of a dictator, with the uniform threshold
\[
C_*=4+1/\ln2.
\]

The recursive-majority low-level projection barrier at commit `bff0d7b6c21485f386841c42582eb04f32705046` is respected: nothing below truncates spectral levels or merges a high-level tail. The source statistics are the full occurrence vector, exact conditional-product I-projection, and exact Boolean fiber equations.

## 1. A sharp physical cap on every influence marginal

Let `G:{0,1}^k->{-1,+1}` be nonconstant under an interior product measure with input biases `p_i`. Let

\[
q=\Pr[G=-1],\qquad v=4q(1-q),\qquad
r_i={I_i^t(G;p)\over v}.
\]

Write
\[
m(t)=\min(t,1-t),\qquad M(t)=\max(t,1-t),\qquad V_t=4t(1-t).
\]

### Theorem 1 — exact Boolean physical-marginal cap

For every coordinate `i`,

\[
\boxed{
r_i\le \rho_i^{\rm phys}(p_i,q)
:={V_{p_i}\over V_q}\min\!\left\{1,{m(q)\over m(p_i)}\right\}.
}
\tag{1.1}
\]

Equivalently,
\[
\rho_i^{\rm phys}=
\begin{cases}
V_{p_i}/V_q,&m(q)\ge m(p_i),\\[1mm]
M(p_i)/M(q),&m(q)<m(p_i).
\end{cases}
\tag{1.2}
\]
In either branch `0<=rho_i^phys<=1`.

### Proof

Fix all coordinates except `i` and write the two fiber values as `g_0,g_1 in {-1,+1}`. In the normalized biased basis,

\[
\phi_i(x_i)={x_i-p_i\over\sqrt{p_i(1-p_i)}}.
\]

The coefficient of `phi_i` in the one-coordinate conditional expansion is

\[
B_i=\mathbb E_{x_i}[G\phi_i]
=\sqrt{p_i(1-p_i)}\,(g_1-g_0).
\]

Hence
\[
B_i^2=V_{p_i}\,1_{\{g_0\ne g_1\}}.
\]
Parseval in the remaining coordinates gives
\[
I_i^t=V_{p_i}d_i,
\tag{1.3}
\]
where `d_i` is the product-measure mass of fibers on which the Boolean output changes when coordinate `i` is flipped.

Every changing fiber contains one `+1` endpoint and one `-1` endpoint. Under the `i`-coordinate measure, each of those endpoint signs has conditional mass at least `m(p_i)`. Therefore
\[
q\ge m(p_i)d_i,\qquad 1-q\ge m(p_i)d_i.
\]
Thus
\[
d_i\le \min\{1,m(q)/m(p_i)\}.
\]
Insert this in (1.3) and divide by `v=V_q`. This proves (1.1). The two cases in (1.2) follow because `V_t=4m(t)M(t)`. `QED`

This is stronger than the tautological spectral bound `r_i<=1`: it uses the actual Boolean two-point fiber and the actual output bias.

### Sharp genuine-Boolean example

Take three independent input bits with
\[
(p_1,p_2,p_3)=(1/10,7/20,1/2),
\]
and define `G=+1` exactly when `x_1=1` and `x_2 xor x_3=1`, with `G=-1` otherwise. Then
\[
q=19/20,\qquad v=19/100.
\]
The first coordinate changes the output exactly on half of the remaining fibers, so
\[
I_1^t=V_{1/10}/2=9/50,
\qquad r_1={9/50\over19/100}={18\over19}.
\]
Since `m(q)<m(p_1)`, (1.2) gives
\[
\rho_1^{\rm phys}={M(p_1)\over M(q)}={9/10\over19/20}={18\over19}.
\]
Thus the cap is attained by an actual Boolean source; it is not merely an artifact of a relaxed spectral model.

## 2. The cap turns the Hmax optimizer into a Gibbs exclusion test

For an arbitrary symmetric potential `Gamma`, use the exact prices from the I-projection source,
\[
a_i={\Gamma(p_i)+h_2(V_{p_i})\over V_{p_i}},\qquad
x_i=2^{-a_i},
\]
and let
\[
Z=\prod_i(1+x_i)-1.
\]
Let `nu_Gamma^+` be the conditional-product Gibbs law
\[
\nu_\Gamma^+(S)={\prod_{i\in S}x_i\over Z},\qquad S\ne\varnothing.
\]
Its `i`th occurrence marginal is
\[
s_i=\nu_\Gamma^+(i\in S)
={x_i\prod_{j\ne i}(1+x_j)\over Z}.
\tag{2.1}
\]
Put
\[
T_\Gamma:=\log_2{Z\over x_q}=a_q+\log_2 Z,
\qquad x_q=2^{-a_q}.
\]
The Pythagorean identity in fleet02/B15 gives exactly
\[
\boxed{
B_{\rm inf}^\Gamma=D_2(Q_r\Vert\nu_\Gamma^+)-T_\Gamma.
}
\tag{2.2}
\]

For `0<=u,s<=1`, write
\[
d_2(u\Vert s)=u\log_2{u\over s}+(1-u)\log_2{1-u\over1-s}.
\]
Define the physical-cap mismatch
\[
\Lambda_{\rm phys}
:=\max_{i:\ s_i>\rho_i^{\rm phys}}
 d_2(\rho_i^{\rm phys}\Vert s_i),
\tag{2.3}
\]
with value zero if the index set is empty.

### Theorem 2 — capped-Gibbs danger wedge

Every genuine Boolean gate satisfies
\[
\boxed{
B_{\rm inf}^\Gamma\ge \Lambda_{\rm phys}-T_\Gamma.
}
\tag{2.4}
\]
Consequently:

1. if `Lambda_phys>=T_Gamma`, then **no** Boolean gate at these input/output biases can lie in the negative first-moment region `B_inf^Gamma<0`;
2. if `B_inf^Gamma=-delta<0`, then necessarily
\[
\boxed{0<\delta\le T_\Gamma-\Lambda_{\rm phys}.}
\tag{2.5}
\]

### Proof

Data processing for KL under the map `S -> 1_{i in S}` gives
\[
D_2(Q_r\Vert\nu_\Gamma^+)\ge d_2(r_i\Vert s_i).
\]
By Theorem 1, `r_i<=rho_i^phys`. If `s_i>rho_i^phys`, the function `u -> d_2(u||s_i)` is decreasing on `[0,s_i]`, hence
\[
d_2(r_i\Vert s_i)\ge d_2(\rho_i^{\rm phys}\Vert s_i).
\]
Take the maximum over such coordinates and substitute in (2.2). This proves (2.4), and (2.5) is immediate. `QED`

Thus the formal Hmax optimizer cannot use arbitrary occurrence marginals: before signs or high-order structure are considered, every dangerous `Q_r` must lie in the Boolean output-bias cap box, and its Gibbs-reference mismatch cannot already consume the available threshold `T_Gamma`.

## 3. A second exact screen from a single biased Boolean equation

The previous theorem uses only Boolean fiber geometry. The signed quadratic equations give an additional, independent screen.

For `mu=sum_i r_i>1`, let `c in (0,1]` be the I-projection root
\[
1-c=\prod_i(1-cr_i),
\]
so the unconditioned Bernoulli parameter is `t_i=cr_i`. Let
\[
q_i^{(1)}:=Q_r(\{i\})
={r_i(1-c)\over1-cr_i}
\tag{3.1}
\]
with the continuous boundary convention. Define
\[
\kappa_i={1-2p_i\over\sqrt{p_i(1-p_i)}},
\qquad
L_i=\sqrt{M(p_i)/m(p_i)},
\]
and
\[
F_i:=\left[
|\kappa_i|vr_i
-2\sqrt{v(1-v)q_i^{(1)}}
-2v(1-r_i)\sqrt{{cr_i\over1-cr_i}}
\right]_+.
\tag{3.2}
\]
If `mu=1`, set instead
\[
F_i=\left[|\kappa_i|vr_i-2\sqrt{v(1-v)r_i}\right]_+.
\tag{3.3}
\]

### Theorem 3 — sign-free one-coordinate Booleanity reserve

Every genuine Boolean gate satisfies
\[
\boxed{
K_{\rm occ}\ge {F_i^2\over4vL_i^2\ln2}
\quad\text{for every }i.
}
\tag{3.4}
\]

### Proof

Use the fleet04/B17 Booleanity-gap theorem with `U={i}`. In one `i`-fiber the quadratic matrix is
\[
\begin{pmatrix}0&1\\1&\kappa_i\end{pmatrix}.
\]
For an arbitrary sign realization of the I-projection magnitudes, the quadratic expression equals
\[
\kappa_i vr_i
+2a_\varnothing\sigma_i\sqrt{vQ_r(\{i\})}
+2v\sum_{\substack{T\ne\varnothing\\i\notin T}}
 \sigma_T\sigma_{T\cup\{i\}}
 \sqrt{Q_r(T)Q_r(T\cup\{i\})}.
\tag{3.5}
\]
Here `a_empty^2=1-v`. Under `Q_r`, for every nonempty `T` not containing `i`,
\[
Q_r(T\cup\{i\})={cr_i\over1-cr_i}Q_r(T),
\]
and
\[
\sum_{\substack{T\ne\varnothing\\i\notin T}}Q_r(T)=1-r_i.
\]
Therefore the total magnitude available to cancel the diagonal term in (3.5) is at most exactly the two subtracted terms in (3.2). Reverse triangle inequality gives
\[
\mathfrak g_{\{i\}}\ge F_i.
\]
Fleet04/B17 then yields (3.4). If `mu=1`, `Q_r` is supported on singletons and the internal-pair sum vanishes, giving (3.3). `QED`

## 4. Combined necessary condition for an actual violating source

Suppose a genuine Boolean source violates the candidate gate inequality, so
\[
R_\Gamma=B_{\rm inf}^\Gamma+K_{\rm occ}<0.
\]
Then `B_inf=-delta<0` and `K_occ<delta`. Theorems 2 and 3 imply the fully explicit necessary condition
\[
\boxed{
\max_i {F_i^2\over4vL_i^2\ln2}
<\delta
\le T_\Gamma-\Lambda_{\rm phys}.
}
\tag{4.1}
\]
Thus a proposed dangerous marginal/output-bias tuple is excluded if either
\[
\Lambda_{\rm phys}\ge T_\Gamma
\]
or
\[
\max_i {F_i^2\over4vL_i^2\ln2}
\ge T_\Gamma-\Lambda_{\rm phys}.
\tag{4.2}
\]
This is a strict strengthening of the previous description “a violator must be close to its maximum-entropy product model”: it first restricts which maximum-entropy marginals are physically realizable by a Boolean source at the stated input and output biases, and then spends one exact signed Boolean equation against the residual deficit.

No claim is made that the maximum in (4.1) is enough universally. The all-equations source explicitly warned that a maximum can lose the necessary logarithmic scale.

## 5. Exact use of the named fleet02/B10 partner result

The new cap is most informative off the balanced-uniform face. At `p_i=1/2` and balanced output `q=1/2`, one has `rho_i^phys=1` and `kappa_i=0`, so the present coordinate screens can become silent. This is precisely where the named fleet02/B10 theorem supplies complementary mathematics rather than redundant evidence.

For every balanced two-point dictator perturbation in dimension `k>=3`, that source sets `eta=2^{2-k}` and proves
\[
I(f)-1=
\begin{cases}
(k-1)\eta,&d=1,\\
(k-2)\eta,&d\ge2,
\end{cases}
\]
with the exact entropy
\[
H(f)=(1-\eta)^2\log_2{1\over(1-\eta)^2}
 +(2\eta-\eta^2)2(k-2),
\]
and concludes
\[
H(f)<\left(4+{1\over\ln2}\right)(I(f)-1).
\]
Hence for every center `C>=C_*` this entire genuine Boolean near-dictator face already satisfies `K_occ>=-B_inf`; it need not be recovered from the off-center cap theorem. The combined residual is therefore narrower: a future counterexample must avoid the partner's paid balanced two-point face and, off-center, must satisfy every inequality in (4.1).

## 6. Recursive-majority preflight

The current recursive-majority correction refutes extracting only fixed or sub-half-depth labelled spectral levels followed by one merged tail. The present theorem does not do this. The cap (1.1) is a direct Boolean fiber identity, `Q_r` uses all exact coordinate occurrence marginals, and Theorem 3 is an exact Boolean equation for the full source. Therefore the low-level projection counterfamily does not refute these statements. Conversely, nothing here claims that these coordinate screens alone pay recursive majority; the missing joint/multiscale credit remains explicit.

## 7. First unpaid implication

After this run, a genuine violating source for a proposed finite-cap potential must lie in the residual set
\[
r_i\le\rho_i^{\rm phys}\quad\forall i,
\qquad
\Lambda_{\rm phys}<T_\Gamma,
\qquad
\max_i{F_i^2\over4vL_i^2\ln2}<T_\Gamma-\Lambda_{\rm phys},
\tag{7.1}
\]
and must also avoid the paid balanced two-point near-dictator face from fleet02/B10.

The first essential missing implication is now a **joint** source theorem on this residual set: combine several signed Boolean equations, or a genuinely multiscale conditional KL decomposition, so that their nonreusing logarithmic credit proves
\[
K_{\rm occ}\ge T_\Gamma-D_2(Q_r\Vert\nu_\Gamma^+)=-B_{\rm inf}^\Gamma.
\]
A repeat of a single maximum-gap or unweighted-L2 bound is specifically not authorized by the known barriers.

This report proves a new arbitrary-arity source constraint and a nontrivial danger-region exclusion; it does **not** prove FEI or universal all-gate nonnegativity.
