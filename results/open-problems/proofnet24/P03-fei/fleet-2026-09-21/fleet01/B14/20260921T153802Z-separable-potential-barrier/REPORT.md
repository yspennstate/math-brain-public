# B14 — smooth separable-potential barrier and a free Fourier-level credit

**Status:** PARTIAL / new structural theorem and a new restriction-potential direction. **Full uniform-cube FEI remains OPEN / NOT PROVED.**

**Execution:** `WITHOUT_VERIFIED_BRAIN`. No authenticated brain retrieval/context was used. The current private FEI master, owner-prescribed `TASKS_2026-09-21.md`, `REPORT.md`, and `APPROACHES.md` were read first, together with the compatible B14 selector/potential continuations. No read-once certificate was rerun and no FEI audit was performed.

**Publication priority:** UNVERIFIED. No novelty claim is made.

The immediate inherited state is:

1. for the spectral sample `S` of a Boolean function,
   \[
   \Delta_iH=B_i+JS_i,
   \qquad B_i=H(S_i\mid S_{-i});
   \]
2. the already-proved influence potential
   \[
   \Phi_\eta(f)=\sum_j\eta(\operatorname{Inf}_j(f)),
   \qquad 0\le \Phi_\eta\le c_*I,
   \quad c_*=2/\ln2,
   \]
   absorbs all recombination: `Delta_i Phi_eta >= JS_i`;
3. the newer quadratic separable potential
   \[
   P_2(f)=c_*\left(I(f)-\frac13\sum_j\operatorname{Inf}_j(f)^2\right)
   \]
   also absorbs `JS_i`, but on the recursive Numaro obstruction its normalized drop converges uniformly to `c_*`;
4. for the balanced Numaro seed `G` and self-compositions `F_r`, the compatible B14 theorem proves
   \[
   \rho_0(F_r):=\min_i\frac{\Delta_iH(F_r)}{\operatorname{Inf}_i(F_r)}\longrightarrow \rho_*(G)<\infty,
   \]
   while uniformly over leaf coordinates
   \[
   \max_i p_i(F_r)\to0,
   \qquad
   \max_i\frac{D_i(F_r)}{p_i(F_r)}\to0,
   \tag{0.1}
   \]
   where
   \[
   p_i=\operatorname{Inf}_i,
   \qquad
   D_i=\sum_{j\ne i}\bigl(p_j(f_i^+)-p_j(f_i^-)\bigr)^2.
   \]

The first theorem below explains *why* both existing separable potentials asymptotically do the same thing. The second part identifies a genuinely different positive spectral credit that does not pay an extra global influence surcharge.

## 1. A general no-gain theorem for smooth coordinate-separable influence potentials

Let `phi` be a real function with `phi(0)=0`, differentiable at zero and `C^2` on `[0,delta]` for some `delta>0`. Define
\[
P_\phi(f):=\sum_j\phi(p_j(f)),
\qquad p_j(f)=\operatorname{Inf}_j(f).
\tag{1.1}
\]
For a restriction in physical coordinate `i`, influence averaging is exact:
\[
p_j(f)=\frac{p_j(f_i^+)+p_j(f_i^-)}2,\qquad j\ne i.
\tag{1.2}
\]
Put
\[
d_{ij}:=p_j(f_i^+)-p_j(f_i^-).
\]
Then
\[
\Delta_iP_\phi
=\phi(p_i)+\sum_{j\ne i}
\left[
\phi(p_j)-\frac{\phi(p_j(f_i^+))+\phi(p_j(f_i^-))}{2}
\right].
\tag{1.3}
\]

### Theorem 1.1 — small-influence collapse

Assume a sequence of Boolean functions `f_r` has
\[
\epsilon_r:=\max_i p_i(f_r)\to0,
\qquad
\delta_r:=\max_{i:p_i>0}\frac{D_i(f_r)}{p_i(f_r)}\to0.
\tag{1.4}
\]
Then, with `sigma=phi'(0)`,
\[
\boxed{
\max_{i:p_i>0}
\left|
\frac{\Delta_iP_\phi(f_r)}{p_i(f_r)}-\sigma
\right|\longrightarrow0.
}
\tag{1.5}
\]

#### Proof

For large `r`, all parent and child influences occurring in (1.3) lie in a fixed small interval where
\[
M:=\sup|\phi''|<\infty.
\]
Indeed the two child influences are nonnegative and average to `p_j`, hence each is at most `2p_j<=2epsilon_r`.

For any `a,b` in that interval, with `m=(a+b)/2`, the midpoint Taylor remainder gives
\[
\left|\phi(m)-\frac{\phi(a)+\phi(b)}2\right|
\le \frac M8(a-b)^2.
\tag{1.6}
\]
Applying this to every `j!=i` in (1.3),
\[
\left|
\frac{\Delta_iP_\phi}{p_i}-\frac{\phi(p_i)}{p_i}
\right|
\le\frac M8\frac{D_i}{p_i}.
\tag{1.7}
\]
Because `phi(p)/p -> phi'(0)=sigma` as `p->0`, (1.4) makes the first term converge uniformly to `sigma`, while the right side of (1.7) converges uniformly to zero. This proves (1.5). QED.

### Corollary 1.2 — the recursive Numaro obstruction defeats the whole smooth separable class

Apply Theorem 1.1 to the inherited Numaro self-compositions `F_r`, for which (0.1) is already proved. Then
\[
\boxed{
\min_i\frac{\Delta_i(H-P_\phi)(F_r)}{p_i(F_r)}
\longrightarrow \rho_*(G)-\sigma.
}
\tag{1.8}
\]
Indeed the subtraction in (1.5) is uniform over all leaf coordinates, so it commutes with the minimum.

Suppose in addition the proposed potential has a pointwise linear budget
\[
0\le\phi(t)\le L t\qquad(0\le t\le1).
\tag{1.9}
\]
Then `sigma<=L`. If a restriction proof sought a universal residual selector
\[
\exists i:\quad
\Delta_i(H-P_\phi)\le Kp_i
\tag{1.10}
\]
for every nonconstant Boolean state, the family `F_r` forces
\[
K\ge\rho_*(G)-\sigma.
\tag{1.11}
\]
The final reconstruction
\[
H=(H-P_\phi)+P_\phi\le (K+L)I
\]
therefore has the unavoidable barrier
\[
\boxed{K+L\ge\rho_*(G)+(L-\sigma)\ge\rho_*(G).}
\tag{1.12}
\]

So **no bounded smooth potential that is merely a sum of one-coordinate functions of the influence vector can improve the asymptotic one-coordinate selector barrier of this recursive family after paying its own global influence budget**.

This is a no-go theorem for a proof architecture, not a lower bound for the true FEI constant and not a counterexample to FEI. A nonlocal stopping argument, a block potential, or a potential using genuinely spectral information is not covered by (1.12).

### Existing potentials fall exactly on this barrier

- For the already-proved JS absorber `Phi_eta`, `phi=eta`, `sigma=eta'(0)=c_*`, and its global budget is `L=c_*`.
- For the quadratic potential `P_2`,
  \[
  \phi_2(p)=c_*\left(p-\frac{p^2}{3}\right),
  \]
  so again `sigma=L=c_*`.

Thus both potentials asymptotically subtract precisely `c_*` from the local selector and then add precisely `c_*` back through their global budget. The newer exact `P_2` composition calculation is therefore an instance of a general phenomenon, not an accident specific to the quadratic formula.

## 2. A way around the barrier: add a nonnegative spectral potential instead of subtracting a budgeted one

A positive spectral term placed on the **left** of the target inequality has a different accounting rule. Let
\[
W_k(f):=\sum_{|S|=k}\widehat f(S)^2,
\qquad W_1(f)=\sum_j\widehat f(\{j\})^2.
\tag{2.1}
\]
Since `W_1>=0`, define
\[
\mathcal E_\lambda(f):=H(f)-\Phi_\eta(f)+\lambda W_1(f),
\qquad\lambda\ge0.
\tag{2.2}
\]
If one could prove `mathcal E_lambda<=K I`, then
\[
H=\mathcal E_\lambda+\Phi_\eta-\lambda W_1
\le (K+c_*)I.
\tag{2.3}
\]
**There is no additional `lambda W_1` surcharge** because it is nonnegative and is subtracted in the reconstruction.

This makes positive spectral potentials qualitatively different from (1.1), and therefore a natural route after Theorem 1.1.

## 3. Exact Fourier-level restriction flux

### Theorem 3.1

For every Boolean function and every coordinate `i`, let
\[
W_k^{(i)}:=\sum_{\substack{|S|=k\\ i\in S}}\widehat f(S)^2.
\]
Then
\[
\boxed{
\Delta_i W_k=W_k^{(i)}-W_{k+1}^{(i)}.
}
\tag{3.1}
\]

#### Proof

Pair the Fourier coefficients as
\[
u_T=\widehat f(T),\qquad v_T=\widehat f(T\cup\{i\}),\qquad i\notin T.
\]
The two restrictions have coefficients `u_T+v_T` and `u_T-v_T`. Hence the average squared restricted coefficient is
\[
\frac{(u_T+v_T)^2+(u_T-v_T)^2}{2}=u_T^2+v_T^2.
\]
Thus the level-`k` child average receives parent mass from `u_T^2` at level `k` and `v_T^2` at parent level `k+1`. Collecting levels gives (3.1). QED.

More generally, for nonnegative coefficients `c_k` and `c_0=0`,
\[
Q_c(f):=\sum_{k\ge1}c_kW_k(f)\ge0
\]
has exact drop
\[
\boxed{
\Delta_iQ_c
=\sum_{k\ge1}(c_k-c_{k-1})W_k^{(i)}.
}
\tag{3.2}
\]
This is a discrete degree-space flux formula: descending spectral mass crosses the jumps of the coefficient profile `c_k`.

For `W_1`, put
\[
e_i:=\widehat f(\{i\})^2,
\qquad
Q_i:=\sum_{j\ne i}\widehat f(\{i,j\})^2.
\]
Then
\[
\boxed{\Delta_iW_1=e_i-Q_i.}
\tag{3.3}
\]
Booleanity gives
\[
|\widehat f(\{i\})|\le \operatorname{Inf}_i(f)=p_i,
\qquad e_i\le p_i^2.
\tag{3.4}
\]
Combining the inherited corrected-entropy identity
\[
\Delta_i(H-\Phi_\eta)=B_i-R_i,
\qquad R_i\ge0,
\]
with (3.3),
\[
\boxed{
\Delta_i\mathcal E_\lambda
=B_i-R_i+\lambda(e_i-Q_i).
}
\tag{3.5}
\]
Thus degree-two mass adjacent to `i` is a genuine *negative* local charge, while the only new positive term is at most `lambda p_i^2`. In the low-influence regime the tax is second order.

This is an actual new selector target:
\[
\exists i:\quad
B_i-R_i-\lambda Q_i
\le (K-\lambda p_i)p_i,
\tag{3.6}
\]
with no `lambda` added to the final FEI constant. It uses spectral information invisible to a coordinate-separable influence potential.

## 4. Balanced-composition propagation of the level-one credit

Let
\[
F=G(g^{(1)},\ldots,g^{(m)})
\]
with balanced outer and identical balanced inner functions on disjoint blocks. For a physical coordinate `k` in logical block `j`, put
\[
s_j=|\widehat G(\{j\})|,
\quad e_k(g)=\widehat g(\{k\})^2,
\quad Q_k(g)=\sum_{\ell\ne k}\widehat g(\{k,\ell\})^2.
\]
Also put
\[
Q_j(G)=\sum_{r\ne j}\widehat G(\{j,r\})^2.
\]
Direct Fourier factorization gives
\[
\boxed{e_{j,k}(F)=s_j^2e_k(g),}
\tag{4.1}
\]
\[
\boxed{
Q_{j,k}(F)=s_j^2Q_k(g)+e_k(g)W_1(g)Q_j(G).
}
\tag{4.2}
\]
Hence
\[
\boxed{
\Delta_{j,k}W_1(F)
=s_j^2\bigl(e_k(g)-Q_k(g)\bigr)
-e_k(g)W_1(g)Q_j(G).
}
\tag{4.3}
\]
The second term is always favorable for (3.5): outer degree-two coupling creates additional negative local flux.

## 5. Targeted calculation: fixed `W_1` alone does not kill the Numaro recursive obstruction

The companion checker reconstructs the already-used Numaro seed and rejects unless its truth-table SHA-256 is

`f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839`.

It obtains exactly
\[
W_1(G)=\frac{14625}{32768},
\qquad
s_C=\frac{57}{256},
\qquad
Q_C(G)=\frac{485}{8192}.
\]
Along the all-core leaf path of the recursive self-compositions, the normalized `W_1` drops are
\[
-0.0432428728,\;-0.0360522456,\;-0.0106531601,\;-0.00263294394,\;-0.000612173676
\]
for depths one through five. Thus a fixed coefficient such as `lambda=4` reduces the inherited all-core raw selector ratios only to
\[
4.37934310,\;6.18480630,\;6.84749967,\;7.04132106,\;7.09361192.
\]
The credit decays rapidly and does **not** neutralize the recursive obstruction.

This is a useful negative result rather than a reason to abandon (3.2): it says a single fixed jump at level one is too shallow. A successful positive spectral bank must move credit across multiple levels, blocks, or restriction states.

As a separate finite diagnostic, exhaustive `n=4` truth tables up to global sign gave worst existential ratio `4.86766874675` for raw `H`, versus `4.30726126011` for `H+4W_1`; a coarse `lambda` grid put the finite best near `4.185`. These numbers are only route diagnostics and are not universal statements.

## 6. What is proved and what changes

### PROVED

1. The smooth separable-potential collapse theorem (1.5).
2. On the inherited Numaro recursive family, every such potential shifts the asymptotic selector only by its derivative at zero.
3. If its global budget is `P_phi<=L I`, any residual-selector proof pays at least the same amount back; the total one-coordinate restriction constant cannot beat `rho_*(G)` by this architecture.
4. Exact level-flux identities (3.1)-(3.3), including the free positive level-one correction to the already-proved JS absorber.
5. Exact balanced-composition propagation (4.1)-(4.3).

### NOT PROVED / OPEN

- No universal bound on the residual selector in (3.6).
- No choice of fixed or adaptive level coefficients is proved to close FEI.
- No dimension-free quantitative stability theorem converting the hard-core endpoint obstruction into a selector payment is obtained here.
- Full uniform-cube FEI remains OPEN.

### Route consequence

The next potential should **not** be another smooth sum `sum_j phi(Inf_j)`: Theorem 1.1 shows that this whole class is asymptotically budget-neutral on the strongest current recursive selector obstruction. The surviving potential mechanisms are genuinely nonseparable: block activation, Fourier-level transport, translation-pair cancellation, or a state-dependent positive spectral bank.

The most concrete next target is to choose a nonnegative multilevel profile `c_k` (possibly state-dependent but with a globally telescoping definition) so that the negative flux in (3.2) pays the erasure residual while the positive jumps occur only where Boolean top-degree/integrality or block activation already supplies credit. Any candidate should first be tested on the Numaro recursion, rare tribes, parity-synergy/bent lifts, and the central-cone FEI-complete normal form.

## 7. Reproducibility

Companion checker: `check_singleton_level_potential.py`.

It verifies the exact `W_1` flux identity on all `32,768` four-variable truth tables up to global sign, reconstructs the Numaro seed, propagates the exact balanced-composition recurrence, and records the finite diagnostics above. The checker is a regression test only; the universal theorems are the algebraic arguments in this report.
