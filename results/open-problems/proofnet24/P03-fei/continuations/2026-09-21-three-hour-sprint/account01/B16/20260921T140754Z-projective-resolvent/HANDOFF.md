# B16 FEI handoff — spatial/radial resolvent coincidence

**Full FEI remains OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

Two exact signed-transport results were added.

First, a codimension-only local charge is invariant under one dummy split iff `q_c=Lambda*2^{-c}`. For this unique projective law, the random-order ordered-min Walsh multiplier is

\[
A_{n,r}=\frac{\Lambda}{2(r+1)}-\frac{\Lambda}{n}+\frac{\Lambda2^{-n}}n,
\]
so
\[
A_{n,0}-A_{n,r}=\frac\Lambda2\frac r{r+1}.
\]
Combining this with the exact q-flip Fourier sign gives the **uncentered** payment
\[
\langle K,p_i\rangle
=\Lambda\sum_{U\ne0}\frac{|U|}{|U|+1}\widehat\eta_i(U)^2
=\Lambda\langle g_i,L(I+L)^{-1}g_i\rangle
\le\Lambda E_i.
\]
Thus the constant displacement mode is automatically canceled inside the exact spectral gap; it is not an extra positive bill. For the proved parity-switch refunded law `q_c=2^{3-c}` (`Lambda=8`), the payment is exactly `1` per active coordinate and `2` total for every dummy extension, matching that diagnostic's two-bit spectral entropy.

Second, consuming the newest account04 first-hit two-scale handoff, the radial moment bank has an exact Hardy resolvent factorization. For
\[
m_v(t)=\sum_{A:v\in R_A}c_A t^{q_A-1}
\]
and `H m(t)=t^{-1} int_0^t m(s)ds`,
\[
\operatorname{Var}_{[0,1]}m_v
=\|(I-H)m_v\|_2^2
=\|D(I+D)^{-1}m_v\|_2^2,
\qquad D=t\partial_t.
\]
Equivalently, after signed same-degree aggregation `a_{v,q}=sum c_A`,
\[
K_{rad}
=\sum_v\int_0^1
\left[\sum_q\frac{q-1}{q}a_{v,q}t^{q-1}\right]^2dt.
\]
The radial transfer function is therefore again exactly `z/(1+z)`. Splitting `t` at `1/2` gives
\[
Var(m)=\tfrac12V_-+\tfrac12V_++B(m)^2,
\qquad
B(m)=\sum_q\frac{1-2^{1-q}}q a_q,
\]
with the low half exactly
\[
V_-=
\int_0^1\left[
\sum_q2^{-(q-1)}\frac{q-1}{q}a_qu^{q-1}
\right]^2du.
\]
So the low radial half already carries the exponential moment damping expected from R16; the remaining radial burden is localized to the near-terminal high half plus one signed scalar bridge.

**Next target:** prove that the authentic R16 first-separation/moment reservoir pays the low-half Hardy square, and that the authorized terminal/Shapley ledger pays the high-half plus bridge, while keeping all R32 `2 mod 4` credits signed. In parallel, seek a positive projective disintegration of the fully refunded spatial residual into geometric components; if its total `Lambda` mass is uniformly bounded, the spatial payment is finished by the first theorem.

Files in this folder: `REPORT.md`, `RADIAL_HARDY_RESOLVENT.md`, both exact rational checkers and their output JSON files.
