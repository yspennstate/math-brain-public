# account04/B14 — coordinate-marginal entropy amplifies the terminal MUX block credit

**Classification:** `ESSENTIAL_STEP_APPLIED / REALIZABLE_TERMINAL_BLOCK_SELECTOR / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**

## 1. Live target and exact inherited ingredients

The later owner control converges the FEI fleet on the all-gate formulation.  This run stays on B14's restriction/selector interface and uses the one-address-bit MUX hard family

\[
M(A;D_0,D_1)=D_A,
\qquad \Pr(A=1)=t,
\qquad \Pr(D_j=1)=q_j.
\]

The physical terminal policy from `account03/B14/20260922T073515Z-mux-data-block-selector/REPORT.md` reveals the original data block
\[
T=\{D_0,D_1\}.
\]
Every child is a constant or a literal, so its gate defect vanishes.  Put
\[
V_t=4t(1-t),\qquad V_j=4q_j(1-q_j),
\]
\[
d=q_0+q_1-2q_0q_1,\qquad r=(1-t)q_0+tq_1.
\]
The exact quadratic/Poincare currency captured by this block is
\[
\boxed{W_M={V_t(V_0+V_1)\over16}.}
\tag{1.1}
\]
The exact nonmodular block-information credit is
\[
\boxed{
\mathcal C_D
=d\,h_2(V_t)+h_2(q_0)+h_2(a)+h_2(q_1)+h_2(b)-\widetilde H_M,
}
\tag{1.2}
\]
where
\[
a=V_0(1-t),\qquad b=V_1t,
\]
and `Htilde_M` is the entropy of the six biased-Walsh squared masses
\[
(1-2r)^2,
\quad V_t(q_1-q_0)^2,
\quad (1-t)^2V_0,
\quad t^2V_1,
\quad t(1-t)V_0,
\quad t(1-t)V_1.
\tag{1.3}
\]

The immediately preceding B14 result used only the total-correlation subterm of `C_D`, proving a sharp fixed-sum TC lower bound.  The present run uses a different method: entropy subadditivity across the **physical spectral-coordinate indicators** and an exact binary-channel reduction.

## 2. Coordinate-marginal lower bound for the full information credit

Let `S` be the random biased-Fourier support subset distributed according to the six masses (1.3).  Its three coordinate marginals are exactly
\[
\Pr(A\in S)=V_t d,
\qquad
\Pr(D_0\in S)=a,
\qquad
\Pr(D_1\in S)=b.
\tag{2.1}
\]
Indeed the first identity is the biased influence of the address coordinate, and the other two follow by grouping the two masses containing each data coordinate.

Because a random subset is determined by its coordinate indicators, ordinary entropy subadditivity gives
\[
\widetilde H_M=H(S)
\le h_2(V_t d)+h_2(a)+h_2(b).
\tag{2.2}
\]
Substitution in (1.2) cancels the two block-coordinate marginal entropies and proves:

### Theorem 2.1 — full-credit marginal bound

For every interior MUX bias,
\[
\boxed{
\mathcal C_D
\ge
 d\,h_2(V_t)+h_2(q_0)+h_2(q_1)-h_2(V_t d).
}
\tag{2.3}
\]

This lower bound uses the **entire exact terminal block credit**, not merely its `TC(K)` term.

There is a useful bias-free simplification.  Let `B~Bernoulli(V_t)` and `E~Bernoulli(d)` be independent and set `Y=BE`.  Since `Pr(Y=1)=V_t d`,
\[
H(Y)\le H(E,Y)=H(E)+H(Y\mid E)=h_2(d)+d h_2(V_t).
\]
Hence
\[
\boxed{
 d h_2(V_t)-h_2(V_t d)\ge-h_2(d),
}
\tag{2.4}
\]
and therefore
\[
\boxed{
\mathcal C_D\ge h_2(q_0)+h_2(q_1)-h_2(d).
}
\tag{2.5}
\]
The right side is exactly the equivocation of one independent data bit after observing their XOR: if `E=D_0\oplus D_1`, then
\[
h_2(q_0)+h_2(q_1)-h_2(d)=H(D_0,D_1\mid E)=H(D_0\mid E).
\tag{2.6}
\]
So the physical terminal restriction earns at least the data-XOR equivocation as nonreused information credit.

## 3. Exact central-square amplification

Assume
\[
q_0,q_1\in[1/4,3/4].
\tag{3.1}
\]
By complementing either data bit if necessary, the quantity in (2.5) is unchanged because `h_2(q)` is symmetric and complementing one bit sends `d` to `1-d`.  Thus reduce to
\[
x,y\in[1/4,1/2],
\qquad d=x+y-2xy\in[0,1/2].
\]
Define
\[
F(x,y)=h_2(x)+h_2(y)-h_2(x+y-2xy).
\]
On this square,
\[
{\partial F\over\partial x}
=h_2'(x)-(1-2y)h_2'(d)\ge0,
\tag{3.2}
\]
because `d>=x`, `h_2'` is nonnegative and decreasing on `[0,1/2]`, and `0<=1-2y<=1`.  Symmetrically `partial F/partial y>=0`.  Hence
\[
F(x,y)\ge F(1/4,1/4)
=2h_2(1/4)-h_2(3/8).
\tag{3.3}
\]
Also from (1.1), `W_M<=1/8`.  Combining (2.5), (3.3), and (1.1) gives the explicit terminal-selector theorem
\[
\boxed{
{\mathcal C_D\over W_M}
\ge 8\,[2h_2(1/4)-h_2(3/8)]
=8-9\log_2 3+5\log_2 5
=\log_2{800000\over19683}.
}
\tag{3.4}
\]
Numerically,
\[
\boxed{{\mathcal C_D\over W_M}\ge5.3449779679464049\ldots .}
\tag{3.5}
\]

The previous TC-only Schur-convex theorem guaranteed `3.7076254015...` units of credit on the same central square.  Thus (3.5) gains more than `1.63735` additional units of quadratic currency by retaining the coordinate-marginal part of the already-generated block information.

## 4. Stronger live-candidate margin filter

Write, as in the terminal block theorem,
\[
\bar c_D:=-{\mathcal R_{\Gamma_0,D}\over W_M},
\qquad
c_M=-{D_{\Gamma_0}(M)\over W_M}
=\bar c_D-{\mathcal C_D\over W_M}.
\tag{4.1}
\]
For the source-current lift
\[
a^\dagger=0.268204856,
\]
a negative live-candidate MUX point in the central data square must therefore satisfy
\[
\boxed{
\bar c_D>
0.268204856+\log_2{800000\over19683}
=5.6131828239464049\ldots .
}
\tag{4.2}
\]
The immediately preceding TC-only filter required only
\[
\bar c_D>3.9758302575\ldots .
\]
So the realizable data-block selector now eliminates a strictly larger source-defined part of the MUX residual without altering the potential.

## 5. Exact source-to-next-arrow use of account01/B18 curvature refund

The source-exact account01/B18 theorem `20260921T1856Z-curvature-refunded-crossing/REPORT.md` proves for every physical restriction block `A`
\[
\boxed{
\Delta_A\mathcal F
\le B_A-\sum_{j\notin A}\mathfrak j'(p_j)c_j(A),
}
\tag{5.1}
\]
with the exact folded drift
\[
\boxed{
D_A=\mathcal J(f)-\mathbb E\mathcal J(f_{A=z})=I_A+C_A.
}
\tag{5.2}
\]
The precise source-to-next-arrow lesson is that a physical restriction creates nonmodular information/crossing credit which must be retained rather than erased by a blind induction.

For the current all-gate MUX branch, the terminal physical block `{D_0,D_1}` has exactly the same structural role: the block cocycle isolates the generated nonmodular bank `C_D`, and every child is already terminal.  The previous B14 bound retained only one subterm `TC(K)`.  Theorem 2.1 spends strictly more of the **same once-generated bank** by using the coordinate marginals of the actual spectral support.  There is no reuse of a refund and no replacement by a prescribed-coordinate payment.

The known addressing obstruction therefore remains intact.  No assertion of the false form `B_i<=K Inf_i` is made for a prescribed coordinate.  The selector is the genuine original-coordinate block `{D_0,D_1}`, and (5.2) remains the exact folded-drift identity.

## 6. Realizable stopping interpretation and next missing implication

On the MUX hard family, the policy is a genuine finite stopping policy: reveal both physical data bits and stop.  Its four children are constants/literals, so there is no hidden child deficit and no second use of the information bank.  In the language of interface A, all unpaid terminal Shannon information is represented in the one exact block cocycle and the new lower bound spends part of that bank immediately.

This does **not** by itself construct the still-missing universal `O(J)` strategy for arbitrary Boolean functions, and it does not prove FEI.  Under the later owner convergence instruction the next source-defined arrow is narrower: compare the actual h96 credit-free remainder `bar c_D` against (4.2), together with the already-certified physical address-selector and deterministic-data boundary regions.  A surviving central-square MUX counterexample now has to clear the explicit barrier `5.613182823946...`; otherwise this prime family is safe there.

## 7. Diagnostic verification

`CHECK_MUX_MARGINAL_CREDIT.py` evaluates the six exact MUX spectral masses, the exact block-credit identity (1.2), and the lower bound (2.3) on a deterministic `99^3=970,299` interior grid.  It also checks the central-square theorem (3.4).  The diagnostic passed:

- maximum mass-sum error: `6.6613381477509392e-16`;
- minimum sampled `exact credit - marginal lower bound`: `0.0027269178025190188`;
- central constant: `5.3449779679464049`;
- minimum sampled `exact credit/W - central constant`: `7.0899757706093114`.

The checker is diagnostic only; Theorems 2.1 and (3.4) are analytic.

Checker SHA-256: `dfc30764a9a72a3823ebf633b7c7a409e2771e20a632ffd777c9039abb47a495`  
Captured output SHA-256: `10468f73e628dcc2b96a97002bd161b4777a47d0c03d888d1f231665e2729d97`.

No benchmark gold, paid/remote compute, workflow dispatch, email/Drive data, unrelated private data, or weakened source/proof gate was used.
