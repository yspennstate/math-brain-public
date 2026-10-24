# R15 idea note — K-excess controls the whole K-K contact energy

Date: 2026-09-20 UTC.  
Track: R15 retained F0111 screen only; **PENDING / SELF_CHECK_ONLY / NOT CLAIMED**.  
This note does not reopen Burdzy--Scheutzow Problem 7.2 and does not claim a solution of Talagrand's discrete Convexity Conjecture.

## New route

The preceding smooth-secants report bounded the K-block entropy term by

\[
K_{\rm sec}:=\frac{U_K-N}{S}\frac{c_K\log c_K}{c_K-1},
\qquad c_K=\frac{U_K}{L_K},
\]

but it bounded the K-K coefficient energy independently by the older roof

\[
\overline E_K=\frac{y(N-1)}2\log^2c_K.
\]

That loses the exact fact that the K coordinates collapse to the zero face when the K excess

\[
\eta_K:=U_K-N=\sum_{j\in K}(e^{q_j}-1)
\]

goes to zero. The new idea is to make the pair energy pay for the same excess.

At exact contact put

\[
v_j=e^{q_j}=Sr_j,\qquad 1\le v_j\le c_K,
\qquad \sum_{j\in K}v_j=N+\eta_K.
\]

The secant bound gives

\[
\sum_{j\in K}r_jq_j=\frac1S\sum_jv_j\log v_j\le K_{\rm sec},
\]

while \(\log v\le v-1\) gives

\[
\sum_{j\in K}q_j\le\eta_K.
\]

Now use the contact Hessian rather than a separate projective bound. If
\(H=D^2(P-F)(q)\succeq0\), then

\[
H_{ii}=r_i(1-r_i),\qquad H_{ij}=B_{ij}-r_ir_j.
\]

Every \(2\times2\) principal minor gives

\[
B_{ij}\le r_ir_j+\sqrt{r_ir_j(1-r_i)(1-r_j)}
\le\sqrt{r_ir_j}\le\frac{r_i+r_j}{2}.
\]

Therefore the exact K-K contact energy

\[
E_{KK}:=\sum_{i<j\in K}B_{ij}q_iq_j
\]

satisfies

\[
\begin{aligned}
E_{KK}
&\le\frac12\sum_{i<j}(r_i+r_j)q_iq_j\\
&=\frac12\left[
\left(\sum_i r_iq_i\right)\left(\sum_jq_j\right)
-\sum_i r_iq_i^2
\right]\\
&\le\frac12\left(\sum_i r_iq_i\right)\left(\sum_jq_j\right)
\le\frac{\eta_K}{2}K_{\rm sec}.
\end{aligned}
\]

So the previous necessary smooth gate can be strengthened to

\[
\boxed{
\widehat\Gamma_N(\delta,s)
:=\log S-\left(1+\frac{\eta_K}{2}\right)K_{\rm sec}-H_J^*\le0,
\qquad N=12,13.
}
\]

This removes the older independent K-K roof altogether. In particular, at the exact scalar boundary \(U_K=N\), one has \(\eta_K=0\), hence every \(v_j=1\), every \(q_j=0\), and both the K entropy and K-K energy vanish exactly.

## Why this route is promising

The remaining scalar cells are already extremely narrow. The old gate was weakest near the scalar collision where \(U_K\downarrow N\); the new bound is designed precisely for that regime because the K-K energy is now second-order in the K excess rather than bounded by an unrelated block-capacity quantity.

The next proof target is to show \(\widehat\Gamma_N>0\) on the complete scalar-feasible cells for \(N=12,13\). A route-finding numerical scan may be used only to locate the likely extremal boundary; it is not evidence. Closure still requires a written global sign argument or exact interval/Bernstein/Taylor certificate and independent audits.

## Section-B moves

- **#3 PROVE SOMETHING STRONGER:** replace a K-K bound independent of the K excess by a bound forced to vanish with that excess.
- **#25 COUNT THE SAME THING TWICE:** rewrite \(\sum_{i<j}(r_i+r_j)q_iq_j\) exactly as a product of first moments minus the diagonal correction.
- **#27 SWAP THE QUANTIFIERS:** instead of optimizing separately over every heterogeneous K distribution, prove one excess-only inequality valid simultaneously for all such distributions.
