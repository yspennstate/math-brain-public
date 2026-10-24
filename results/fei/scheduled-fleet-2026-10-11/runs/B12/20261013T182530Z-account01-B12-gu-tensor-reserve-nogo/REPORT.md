# B12 / A056 — tensor no-go theorem for child-only terminal-reserve payment

## Status

**PROVED (pending independent review):** there is no finite universal constant
`C` for either of the one-child terminal-reserve payments

\[
\overline\Theta_{g,y}(\mu)
\le C\,\operatorname{Inf}_y(g)(1-\mu^2),                     \tag{1}
\]

or

\[
\overline\Theta_{g,y}(\mathbb Eh)
\le C\,\operatorname{Inf}_y(g) I(h).                         \tag{2}
\]

The witnesses are genuine Boolean outer gates and genuine Boolean
point-defect children.  This refutes the entire child-only terminal-reserve
mechanism, not merely the previously killed constants 3 and 4.

This is **not** a counterexample to universal GU or to full FEI.  The omitted
outer-coordinate or joint activation/source ledger may still pay the reserve.
Both universal GU and full FEI remain **OPEN**.

## Base pair of Boolean slices

Index the four-cube by masks `0,...,15`.  Define Boolean functions `u,v` by

```text
u=(-1,1,-1,-1,-1,-1,1,-1,1,1,1,-1,1,-1,1,-1),
v=( 1,-1,-1,1,-1,1,1,-1,-1,1,1,-1,1,-1,-1,1).
```

Their truth-table indices are 22338 and 38505.  Exact Walsh transform gives

\[
\widehat v(T)=\mathbf 1_{T=[4]},
\]

so `v` is the full parity, while

\[
\widehat u=\frac18(-1,3,1,-3,1,-3,3,-1,-3,-3,-1,-1,-1,-1,1,1).
\tag{3}
\]

In particular every coefficient of `u` is nonzero.  Put

\[
p_T=\widehat u(T)^2,qquad
C_T=\sum_{R\supseteq T}p_R.
\]

Direct exact rational summation gives

\[
\rho=\langle u,v\rangle=\frac18,
\qquad
A:=\sum_T\frac{p_T}{C_T}=\frac{6911}{960}>7.                \tag{4}
\]

## Tensor family

For every `k>=1`, on `4k` variables set

\[
U_k=u^{\otimes k},\qquad V_k=v^{\otimes k},
\]

and define the Boolean outer gate `g_k(y,z)` by its two slices

\[
g_k(-1,z)=U_k(z),\qquad g_k(1,z)=V_k(z).
\]

Then

\[
\beta_k:=\operatorname{Inf}_y(g_k)
=\frac{1-\rho^k}{2}=\frac{1-8^{-k}}2.                       \tag{5}
\]

Let `Theta_k` be the exact one-biased-child potential proved in
`B12-A056-GU-BIASED-CHILD-COCYCLE-v1`, and let

\[
Q_k=\lim_{\mu\downarrow-1}
\frac{\overline\Theta_k(\mu)}{\beta_k(1-\mu^2)}.             \tag{6}
\]

## Exponential endpoint lower bound

For the tensor spectral law, upper caps factor:

\[
p_{T_1,\ldots,T_k}=\prod_jp_{T_j},\qquad
C_{T_1,\ldots,T_k}=\prod_jC_{T_j}.
\]

Consequently

\[
\sum_T\frac{p_T^{(k)}}{C_T^{(k)}}=A^k.                       \tag{7}
\]

At `mu=-1`, write `b=(V_k-U_k)/2`.  For every spectral atom other
than the full set, `widehat V_k(T)=0`, hence

\[
b_T=-\frac{\widehat U_k(T)}2,qquad
(C_T)'=\frac{1-C_T}{2}.
\]

Differentiating the finite cap formula shows that the contribution of this
atom to `Theta_k'(-1+)` is

\[
-p_T\log_2\frac{C_T}{p_T}
+\frac{p_T(1+C_T)}{2C_T\ln2}.                                \tag{8}
\]

The full-set contribution is nonnegative.  The remaining term `2E_b` is also
nonnegative, while the universal normalization term is
`-2 beta_k/ln 2`.  Since upper-cap entropy tensorizes,
`U(U_k)=kU(u)` and `U(V_k)=0`.  Therefore the endpoint-centered slope `L_k`
satisfies

\[
\begin{aligned}
L_k
&:=\Theta_k'(-1+)+\frac{U(U_k)-U(V_k)}2\\
&\ge \frac{A^k-1}{2\ln2}-\frac{kU(u)}2-\frac{2\beta_k}{\ln2}\\
&\ge \frac{A^k-3}{2\ln2}-2k,                                \tag{9}
\end{aligned}
\]

where `U(u)<=4` and `2 beta_k<=1` were used in the last line.  Whenever the
right side is positive, division by `2 beta_k<=1` gives

\[
\boxed{Q_k\ge\frac{A^k-3}{2\ln2}-2k.}                        \tag{10}
\]

Because `A=6911/960>7`, `Q_k` diverges exponentially.  Thus (1) admits no
finite dimension-independent constant.

Direct evaluations, used only as checks of the proved pattern, are

| `k` | outer slice dimension | `beta_k` | endpoint ratio `Q_k` |
|---:|---:|---:|---:|
| 1 | 4 | `7/16` | `6.342950020628696` |
| 2 | 8 | `63/128` | `39.53728743191995` |
| 3 | 12 | `511/1024` | `272.28968829783093` |

## Source-influence no-go theorem

The stronger conclusion (2) requires retaining the point-defect influence,
not replacing it by variance.  For each `k`, take the point defect `h_k` on

\[
n_k=8k
\]

bits.  Its mean and influence are

\[
\mu_k=-1+2^{1-8k},\qquad I(h_k)=8k\,2^{1-8k}.                \tag{11}
\]

Write `epsilon=2^{1-8k}`, `r=epsilon/2=2^{-8k}`, and
`q=1-r`.  For a non-full spectral atom of `U_k`, the mixed cap and atom in
the exact potential are

\[
M_T=qC_T+r,qquad c_T^2=q^2p_T.                               \tag{12}
\]

The smallest cap obeys `C_T>=64^{-k}`.  Hence

\[
0\le\frac{r}{qC_T}\le 2^{1-2k}\le\frac12.
\]

Using `ln(1+x)>=x/2` for `0<=x<=1`, subtracting the endpoint chord atom by
atom, and dropping nonnegative terms gives

\[
\overline\Theta_k(\mu_k)
\ge r\left[
\frac{q(A^k-1)}{2\ln2}-4k-\frac2{\ln2}
\right].                                                     \tag{13}
\]

Here the last negative term pays `beta_k psi(mu_k)`: if
`delta=1-mu_k^2`, then

\[
\psi(\mu_k)=(1-\delta)\log_2\frac1{1-\delta}
\le\frac{\delta}{\ln2}\le\frac{4r}{\ln2},
\]

and `beta_k<=1/2`.  Finally,

\[
\beta_k I(h_k)\le8kr.
\]

Combining this with (13), whenever the bracket is positive,

\[
\boxed{
\frac{\overline\Theta_k(\mu_k)}{\beta_k I(h_k)}
\ge
\frac1{8k}\left[
\frac{q(A^k-1)}{2\ln2}-4k-\frac2{\ln2}
\right]\longrightarrow\infty.}                             \tag{14}
\]

Thus no finite child-source-influence constant exists either.  This is an
actual Boolean family at every `k`.

## Small exact falsifier for constant 4

Already at `k=1`, compose `g_1` with the two-bit point defect, whose mean is
`mu=-1/2`.  Exact rational Walsh/cap arithmetic gives

\[
\frac{\overline\Theta_1(-1/2)}{\beta_1(1-1/4)}
=4.05321651593768265527\ldots>4.                             \tag{15}
\]

The full formal expression is archived in `symbolic_outer5_witness.out`.
After clearing its log coefficients, strict positivity over 4 is equivalent
to an integer comparison whose two sides have exact bit lengths 3,358 and
3,340.  Therefore the sign in (15) is certified by arbitrary-precision
integer arithmetic, not by the displayed decimal.

## Search and verification scope

- 13,912,896 five-input slice pairs were evaluated, including every pair
  whose four-bit slices differ on one or two truth-table points, plus five
  million seeded unrestricted pairs.
- Two million unrestricted six-input slice pairs were sampled as a secondary
  falsifier search.  This search is numerical and not used in the theorem.
- Exact Fraction arithmetic proves `rho=1/8` and `A=6911/960`.
- Direct tensor checks at `k=1,2,3` reproduce (5), (7), and the endpoint
  ratios above.
- The finite constant-4 witness uses an exact formal log expression and an
  exact integer sign comparison.

## Previous and new status

- Previous: constant 3 was refuted; constant 4 remained a plausible finite
  terminal-reserve payment after all four-input outer gates survived a grid
  search.
- New: constant 4 is refuted by a six-physical-input Boolean composition, and
  every finite constant in both (1) and (2) is refuted by the tensor family.
- Preserved: the exact one-biased-child formula and its adaptive cocycle.
  What fails is paying the entire endpoint reserve from the child channel
  alone.

## Next unpaid step

The proof must now retain an outer or joint reserve.  For this family, the
exploding term is the cap-ratio sum `sum_T p_T/C_T`; it is generated by the
parity slice colliding coherently with the full-support tensor slice.  The next
candidate ledger should charge this term to outer-coordinate decrements (or a
joint activation/source decrement) before completing the child hierarchy.
Any proposed ledger must be tested on this tensor family and on shared-input
overlap; a scalar child-only near/separated split cannot succeed.

## Reproduction

```bash
python3 search_endpoint_outer5.py --slice-bits 4 --max-flips 2 --random-pairs 5000000 --seed 20261013
python3 search_endpoint_outer5.py --slice-bits 5 --max-flips 0 --random-pairs 2000000 --batch 8192 --seed 20261013
python3 certify_outer5_endpoint.py
python3 symbolic_outer5_witness.py
python3 verify_tensor_growth.py
```

