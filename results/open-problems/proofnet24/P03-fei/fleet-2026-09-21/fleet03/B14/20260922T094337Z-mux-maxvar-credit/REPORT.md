# B14 — max-variance physical MUX selector and amplified exact block credit

**Classification:** `ESSENTIAL_STEP_APPLIED / EXACT_REALIZABLE_SELECTOR_AND_CREDIT_AMPLIFICATION`.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; authenticated repository sources were read, but no authenticated installed-brain retrieval/context entered the mathematics.  

## 0. Exact candidate, prior gap, and this run's change

The live candidate inherited from the Campaign-A lead is

\[
C^\dagger=6.521851214,\qquad C_0=6.4548,
\qquad a^\dagger=4(C^\dagger-C_0)=0.268204856,
\]
\[
\Gamma^\dagger(u)=\Gamma_0(u)+a^\dagger u(1-u),
\]

with `Gamma_0` the committed h96 read-once source.  The current hard prime family is the one-bit MUX

\[
M(A;D_0,D_1)=D_A,
\qquad \Pr(A=1)=t,
\qquad \Pr(D_j=1)=q_j.
\]

Put

\[
V_u=4u(1-u),\qquad V_j=V_{q_j},\qquad V_t=4t(1-t),
\]

and write `D_Gamma` for the gate defect in the owner formulation.  Its quadratic currency is

\[
W_M={I(M)\over4}-r(1-r),
\qquad r=(1-t)q_0+tq_1.
\]

The prior missing implication is still the universal MUX inequality

\[
D_{\Gamma^\dagger}(M;t,q_0,q_1)\ge0
\quad\text{for every interior }(t,q_0,q_1),
\tag{0.1}
\]

or a genuine bias vector refuting it.  Even (0.1) would only close one prime family, not full FEI.

This run attacks the same MUX hard case with a **distinct realizable sequential restriction policy**:

> `MUX-MAXVAR-TWO-STAGE-v1`: first reveal the physical data bit `D_j` with larger variance `V_j`; then reveal the other physical data bit in each child.

No affine coordinate change is made, so the affine-coordinate charge is exactly zero.

The new proved inferences are:

1. the first max-variance data reveal captures at least half of the *exact* parent quadratic currency, and the two physical data reveals partition that currency exactly;
2. after the first reveal every child is a binary AND/OR-type read-once gate;
3. the full two-data-bit information credit admits a new closed form in five scalar quantities;
4. on every central data square `[epsilon,1-epsilon]^2` this gives a strictly stronger source-independent credit-per-currency lower bound than the previously used total-correlation term alone.  At `epsilon=1/4`, a surviving live-candidate MUX counterexample must have credit-free block margin greater than `7.412697408679571`, not merely `2.432247417333445`.

No fixed-relative `q/16` near-subcube shortcut is used.

## 1. Named compatible peer result consumed

This run substantively consumes

`fleet04/B14/20260922T083023Z-mux-boundary-20/REPORT.md`.

That completed report spends the positive source term left unused by the earlier collar proof and establishes the source-valid deterministic-data collar

\[
0\le y\le {Q\over20L}
\Longrightarrow
D_{\Gamma^\dagger}(M;p,x,y)\ge0,
\tag{1.1}
\]

with its stated `Q,L`, plus the symmetric collars at all four data boundaries.  I do not rerun or weaken it.  The result below applies to the complementary interior geometry: the boundary theorem removes a neighborhood of each data face, while the new credit theorem gives a tunable quantitative barrier whenever both data biases stay away from those faces.

I also retain the exact block cocycle proved earlier by this slot:

\[
D_\Gamma(M)=\mathcal R_{\Gamma,D}+\mathcal C_D,
\qquad
\mathcal C_D=H(Z\mid S)+I(S;K)+\operatorname{TC}(K),
\tag{1.2}
\]

for the physical block `D={D0,D1}`.  The point here is not to restate (1.2), but to compute and strengthen its MUX specialization and to realize it sequentially with an exact selector.

## 2. Exact max-variance physical selector

### Proposition 2.1 — one-data currencies

For the physical split on `D_0`, the two cofactors are

\[
M\vert_{D_0=0}=A D_1,
\qquad
M\vert_{D_0=1}=\neg A\vee D_1.
\tag{2.1}
\]

They disagree exactly when `A=0`.  Thus the disagreement probability is `1-t`, while their output probabilities differ by exactly `1-t`.  The exact one-coordinate quadratic currency from the biased restriction cocycle is therefore

\[
\begin{aligned}
\omega_0
&=q_0(1-q_0)\bigl[(1-t)-(1-t)^2\bigr]\\
&=q_0(1-q_0)t(1-t)\\
&={t(1-t)V_0\over4}.
\end{aligned}
\tag{2.2}
\]

Similarly, the `D_1` cofactors disagree exactly when `A=1`, so

\[
\boxed{\omega_1={t(1-t)V_1\over4}.}
\tag{2.3}
\]

The exact parent currency is

\[
\boxed{W_M={t(1-t)(V_0+V_1)\over4}=\omega_0+\omega_1.}
\tag{2.4}
\]

Hence if `j` is chosen so that `V_j=max(V_0,V_1)`, then

\[
\boxed{
\omega_j={V_j\over V_0+V_1}W_M\ge {W_M\over2}.
}
\tag{2.5}
\]

The factor `1/2` is sharp when `V_0=V_1`.

### Why this is a realizable induction policy

After the first data reveal, both branches in (2.1) are binary AND/OR-type read-once gates.  Revealing the remaining data bit terminalizes them to constants/literals.  In either order, the average second-stage currency is exactly the other `omega`, because the block identity and (2.4) give

\[
W_M=\omega_j+\mathbb E W_{\text{first-stage child}}
\]

and the child currency vanishes after the second reveal.  Thus the adaptive physical policy spends the parent currency **once and exactly**:

\[
\boxed{W_M=\omega_{\rm first}+\mathbb E\omega_{\rm second}.}
\tag{2.6}
\]

There is no affine recoding, no geometry-loss factor beyond the sharp first-step selector `1/2`, and no non-realizable conditional query.

This does **not** by itself prove the local defect has the required sign.  The missing induction obligation is now correctly localized: charge any negative first-step local remainder against the retained binary-child slack and the exact information credit, rather than demanding a false credit-free sign.

## 3. Exact closed form for the two-data-bit information credit

Write

\[
d=q_0+q_1-2q_0q_1,\qquad
\delta=q_1-q_0,
\]
\[
a=(1-t)V_0,\qquad b=tV_1,\qquad c=1-a-b,
\]
\[
s=V_t d,\qquad e=V_t\delta^2.
\tag{3.1}
\]

Here `a,b,c` are the marginal probabilities that the block Fourier-layer variable `K` equals `{D0}`, `{D1}`, and the empty set.  The six exact squared biased-Walsh masses of the MUX are

\[
(1-2r)^2,\quad e,\quad(1-t)^2V_0,\quad t^2V_1,\quad t(1-t)V_0,\quad t(1-t)V_1.
\tag{3.2}
\]

Let `S` indicate whether the outside/address Fourier coordinate is present.

### Lemma 3.1 — branch conditional entropy

Restricting the two data bits gives the four functions `0,A,1-A,1`.  Therefore `S=1` can occur only on an off-diagonal data assignment and, conditional on such an assignment, has probability `V_t`.  Hence

\[
\boxed{
H(Z\mid S)
=h_2(q_0)+h_2(q_1)+d\,h_2(V_t)-h_2(s).
}
\tag{3.3}
\]

### Lemma 3.2 — exact outside/block mutual information

From (3.2),

\[
\Pr(S=1\mid K=\{D_0\})=t,
\qquad
\Pr(S=1\mid K=\{D_1\})=1-t,
\]

and

\[
\Pr(S=1\mid K=\varnothing)={e\over c}
\]

when `c>0`.  Since `Pr(S=1)=s`,

\[
\boxed{
I(S;K)
=h_2(s)-(a+b)h_2(t)-c\,h_2(e/c),
}
\tag{3.4}
\]

with the continuous convention `c h_2(e/c)=0` at `c=0`.

The total-correlation term is

\[
\boxed{
\operatorname{TC}(K)
=h_2(a)+h_2(b)-H_3(c,a,b).
}
\tag{3.5}
\]

Adding (3.3)--(3.5) cancels `h_2(s)` and gives the new compact exact formula

\[
\boxed{
\begin{aligned}
\mathcal C_D={}&h_2(q_0)+h_2(q_1)+d\,h_2(V_t)\\
&-(a+b)h_2(t)-c\,h_2(e/c)\\
&+h_2(a)+h_2(b)-H_3(c,a,b).
\end{aligned}}
\tag{3.6}
\]

This is exactly the same source-independent block credit as in (1.2), now expressed without the six-point spectral entropy.  It is useful because its three currencies are visible separately and no term is silently erased.

## 4. A stronger central-data credit theorem

The previous B14 data-block report used only

\[
\operatorname{TC}(K)\ge {ab\over\ln2},
\tag{4.1}
\]

which implied

\[
{\mathcal C_D\over W_M}
\ge {4V_0V_1\over\ln2\,(V_0+V_1)}.
\tag{4.2}
\]

The conditional-entropy term supplies a second, independent payment in the interior.

### Theorem 4.1 — amplified block credit

Fix `0<epsilon<=1/2` and suppose

\[
q_0,q_1\in[\epsilon,1-\epsilon].
\]

Then

\[
H(Z\mid S)
=H(Z)-I(Z;S)
\ge H(Z)-H(S)
\ge 2h_2(\epsilon)-1.
\tag{4.3}
\]

Since conditional entropy is nonnegative, write

\[
A_\epsilon=\max\{0,2h_2(\epsilon)-1\}.
\]

Also `W_M<=1/8`, while (4.1)--(4.2) and `V_j>=4epsilon(1-epsilon)` give

\[
{\operatorname{TC}(K)\over W_M}
\ge {8\epsilon(1-\epsilon)\over\ln2}.
\tag{4.4}
\]

Dropping only the nonnegative `I(S;K)` therefore proves

\[
\boxed{
{\mathcal C_D\over W_M}
\ge
\kappa_{\rm amp}(\epsilon)
:=8A_\epsilon+{8\epsilon(1-\epsilon)\over\ln2}.
}
\tag{4.5}
\]

This is uniform in the address bias `t`.

For `epsilon=1/4`,

\[
\boxed{
\kappa_{\rm amp}(1/4)
=7.144492552679571\ldots
}
\tag{4.6}
\]

compared with the TC-only lower bound `2.164042561333445...` on the same square.

Define, as before, the credit-free block margin request

\[
\bar c_D=-{\mathcal R_{\Gamma_0,D}\over W_M}.
\]

Because

\[
c_M=\bar c_D-{\mathcal C_D\over W_M},
\]

a genuine counterexample to the live lift `a^dagger=0.268204856` in the central data square must satisfy

\[
\boxed{
\bar c_D>
0.268204856+7.144492552679571
=7.412697408679571.
}
\tag{4.7}
\]

This is an exact necessary condition, not a grid observation.

More generally, (4.5) is a tunable family of barriers.  It can be intersected directly with the peer denominator-20 boundary collars: the peer theorem certifies sufficiently near-face points, while (4.5) increasingly penalizes a putative counterexample as both data biases move into the interior.

## 5. Attempted refutation and dead route

A tempting stronger claim would be that the two-data-bit information credit itself pays a **uniform positive fraction** of `W_M` over the whole open cube.  That is false.

Take

\[
t={1\over2},\qquad q_0={1\over2},\qquad q_1\downarrow0.
\]

At the boundary point `q_1=0`, one has

\[
\mathcal C_D=0,
\qquad W_M={1\over16}>0.
\]

By continuity,

\[
\boxed{
\inf_{(t,q_0,q_1)\in(0,1)^3}{\mathcal C_D\over W_M}=0.
}
\tag{5.1}
\]

So no universal constant `eta>0` can replace the localized bound (4.5).  Numerically, along this exact family the ratio is about `4.8e-6` at `q_1=1e-8` and tends to zero.  This does **not** create an FEI obstruction: it lies precisely next to a deterministic-data face controlled by the consumed peer collar (1.1).  It only refutes the credit-only global closure route.

## 6. What remains

**Exact candidate version:** `MUX-MAXVAR-TWO-STAGE-v1` for `Gamma^dagger`.

**Prior missing implication:** all-bias nonnegativity (0.1) for the current MUX prime family.

**New proved inference:** the max-variance physical data selector captures at least `W/2` at the first realizable step, the two data steps partition `W` exactly, all first-step children are binary read-once gates, and the exact block information credit satisfies (3.6) and the amplified interior bound (4.5).

**Failed claim:** a globally positive constant lower bound `C_D/W_M>=eta` is refuted by (5.1).

**Replacement obligation:** use the max-variance first step and the known binary-child slack to prove that its signed local deficit is paid on the residual region outside the denominator-20 data collars; equivalently, prove the credit-free block request stays below the barrier in (4.5), using the actual h96 source.  If that fails, return an explicit interior product-bias vector with `c_M>a^dagger`.

**Consumed peer artifact:** `fleet04/B14/20260922T083023Z-mux-boundary-20/REPORT.md`.

**Applied to claim:** the peer result controls the data-face regime where (5.1) shows no global credit fraction is possible; the new theorem controls a complementary interior regime with a quantitative necessary margin barrier.

**Remaining implication to full FEI:** even a complete MUX closure leaves the universal composition-prime gate inequality open.  Full uniform-cube FEI therefore remains **OPEN**.

**Next recipient:** `fleet01/B18` (Campaign-A lead).  The most useful next calculation is to intersect its exact current MUX residual with (4.5), and in the intermediate annulus use the first-step binary-child slack exposed by (2.1)--(2.6), rather than another credit-free address split.

## 7. Independent regression check

`CHECK_MUX_MAXVAR_CREDIT.py` verifies independently from the six exact Walsh masses that (3.6) equals the original block-credit formula and that (2.4) equals `omega_0+omega_1`.  On 200,000 deterministic pseudorandom tests it recorded maximum errors `3.442e-15` and `2.082e-17`, respectively.  On 100,000 sampled points in `[1/4,3/4]^2` the smallest observed exact ratio `C_D/W_M` was `12.478671385860208`, above the proved lower bound `7.144492552679571`.  The random scan is only regression evidence; the theorem is the algebra in Sections 2--4.
