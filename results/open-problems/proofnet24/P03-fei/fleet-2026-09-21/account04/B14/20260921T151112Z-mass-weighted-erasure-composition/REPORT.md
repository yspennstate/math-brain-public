# B14 — mass-weighted erasure composition and singleton activation tax

**Run:** `B14-20260921T151112Z-r11`  
**Status:** **PARTIAL / PROVED exact composition identity and selector corollaries. Full uniform-cube FEI remains OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN` (the authentic `math_brain` package and a local formal runtime were unavailable in this scheduled runtime).  
**Publication priority:** **UNVERIFIED.** This report makes no novelty claim.

Fresh P03 master was read before this derivation, including the owner-prescribed
`continuations/2026-09-21-readonce-certificate/TASKS_2026-09-21.md`,
then `REPORT.md`, then `APPROACHES.md`.  The derivation also preserves the existing
erasure identity
\[
\Delta_i H=B_i+JS_i,\qquad
JS_i\le {2\over\ln2}\min(\operatorname{Inf}_i,1-\operatorname{Inf}_i),
\]
the known counterexamples to every-prescribed-coordinate payment, the recent recursive
Numaro-seed obstruction `rho_0(F_5)>7.096...`, and the proof that a fixed balanced
non-dictator seed cannot make that local selector diverge.

The point of this run is different: isolate exactly **which part of a disjoint
composition can create new erasure entropy at a physical coordinate**.  The answer is:
only the **singleton Fourier mass of the inner function** can hide whether the
corresponding outer spectral coordinate was active.  All nonsingleton inner mass
inherits erasure linearly and pays no new outer activation tax.

## 1. Notation

For nonnegative masses define the homogeneous binary entropy
\[
\mathcal E(a,b)
 =a\log_2{a+b\over a}+b\log_2{a+b\over b},
\]
with the usual zero conventions.  If a random spectral set has masses `p_S`, then
\[
B_i=\sum_{T\not\ni i}\mathcal E(p_T,p_{T\cup\{i\}}).
\]

Let
\[
F(x^{(1)},\ldots,x^{(m)})
 =G(g_1(x^{(1)}),\ldots,g_m(x^{(m)}))
\]
where the physical blocks are disjoint and every `g_j` is a nonconstant Boolean
function.  Put
\[
\mu_j=\widehat g_j(\varnothing),\qquad
V_j=1-\mu_j^2>0.
\]

Use the product distribution on `z in {+-1}^m` with `E z_j=mu_j` and its
orthonormal basis
\[
\psi_j(z_j)={z_j-\mu_j\over\sqrt{V_j}}.
\]
Let
\[
\widetilde G_\mu(A)
 =\mathbb E_\mu\!\left[G(z)\prod_{j\in A}\psi_j(z_j)\right],
\qquad
q_A=\widetilde G_\mu(A)^2,
\]
so `q` is a probability law on outer spectral subsets.  Write
\[
\alpha_j=\Pr_q[j\in A]=\sum_{A\ni j}q_A.
\]

For a physical coordinate `k` in inner block `j`, put
\[
e_{jk}=\widehat g_j(\{k\})^2,\qquad
x_{jk}={e_{jk}\over V_j}.
\]
Because `e_{jk}` is part of the nonconstant Fourier mass, `0<=x_{jk}<=1`.

Finally define the outer activation-erasure function
\[
R_j(x)=
\sum_{C\subseteq[m]\setminus\{j\}}
 \mathcal E(q_C,xq_{C\cup\{j\}}).
\tag{1.1}
\]

## 2. Exact arbitrary-bias composition identity

### Theorem 2.1

For every physical coordinate `k` in block `j`,
\[
\boxed{
B_{j,k}(F)
={\alpha_j\over V_j}
 \left[
   B_k(g_j)-\mathcal E(\mu_j^2,e_{jk})
 \right]
+R_j(x_{jk}).
}
\tag{2.1}
\]

Also
\[
\boxed{
\operatorname{Inf}_{j,k}(F)
={\alpha_j\over V_j}\operatorname{Inf}_k(g_j).
}
\tag{2.2}
\]

These are identities; there is no FEI assumption.

### Proof

Set
\[
h_j={g_j-\mu_j\over\sqrt{V_j}}.
\]
Then `h_j` has mean zero and squared norm one.  Expanding `G` in the biased
orthonormal basis and substituting `z_j=g_j` gives
\[
F=\sum_{A\subseteq[m]}\widetilde G_\mu(A)\prod_{j\in A}h_j.
\]
For every nonempty physical Fourier set `S` in block `j`,
\[
\widehat h_j(S)={\widehat g_j(S)\over\sqrt{V_j}}.
\]
Consequently the squared Fourier law of `F` has the exact hierarchical sampler:

1. draw an outer set `A` with law `q`;
2. for each `j in A`, draw a nonempty inner Fourier set `S_j` with
   probability `hat(g_j)(S_j)^2/V_j`;
3. for `j notin A`, set `S_j=empty`.

Fix `j,k` and erase only physical bit `k`.  If the residual inner set
`S_j\{k}` is nonempty, outer activity `j in A` is already known from the
other visible bits of block `j`; the erasure pair is therefore an ordinary
inner erasure pair multiplied by outer active mass.  Summing these pairs gives
\[
{\alpha_j\over V_j}
\left[B_k(g_j)-\mathcal E(\mu_j^2,e_{jk})\right].
\]
The subtracted term is exactly the original inner pair
`empty <-> {k}`, which is absent from the normalized nonempty inner law.

If the residual inner set is empty, erasing `k` also hides whether outer
coordinate `j` was active.  For each outer residual set `C`, the two masses are
exactly `q_C` and `x_{jk}q_{C+j}`.  Summing these exceptional pairs is
`R_j(x_{jk})`, proving (2.1).

The same hierarchical sampler says that `(j,k)` is present exactly when outer
`j` is active and an inner normalized spectral sample contains `k`, proving
(2.2).  QED.

**Restriction relevance.**  Formula (2.1) is deliberately stated for biased
inner functions.  A physical restriction of a previously balanced inner block
usually makes its mean nonzero; the positive refund
\(\mathcal E(\mu_j^2,e_{jk})\) records the constant/singleton erasure that must
not be charged twice.

## 3. A one-line concavity bound for the activation tax

Let `phi(t)=-t log_2 t`.  For `a,b>=0` and `0<=x<=1`,
\[
\boxed{
\mathcal E(a,xb)
\le
x\mathcal E(a,b)+xb\log_2{1\over x}.
}
\tag{3.1}
\]

Indeed
\[
\phi(xb)=x\phi(b)+xb\log_2(1/x),
\]
while concavity of `phi` and
`a+xb=(1-x)a+x(a+b)` give
\[
\phi(a+xb)\ge(1-x)\phi(a)+x\phi(a+b).
\]
Subtracting proves (3.1).  Therefore
\[
\boxed{
R_j(x)\le x B_j(q)+\alpha_j x\log_2{1\over x},
}
\tag{3.2}
\]
where `B_j(q)=sum_C E(q_C,q_{C+j})` is the erasure entropy of outer
spectral bit `j` under the biased outer law `q`.

Summing (2.1) and using (3.2), with
\[
W_1(g)=\sum_k\widehat g(\{k\})^2,\qquad
T_V(g)=\sum_k e_k\log_2{V\over e_k},
\]
gives the mass-weighted global bound
\[
\boxed{
\begin{aligned}
B(F)\le&
\sum_j {\alpha_j\over V_j}
 \left[
 B(g_j)-\sum_k\mathcal E(\mu_j^2,e_{jk})
 \right]\\
&+\sum_j {W_1(g_j)\over V_j}B_j(q)
+\sum_j {\alpha_j\over V_j}T_{V_j}(g_j).
\end{aligned}
}
\tag{3.3}
\]
The exact influence payment is
\[
\boxed{
I(F)=\sum_j{\alpha_j\over V_j}I(g_j).
}
\tag{3.4}
\]

This is the promised mass weighting: outer erasure is not copied once per
physical coordinate.  It is copied only in proportion to inner singleton
Fourier mass.

## 4. Boolean singleton tax is universally influence-payable

For a Boolean `g`, let
\[
d_k(y)={g(+1,y)-g(-1,y)\over2}\in\{-1,0,1\}.
\]
Then
\[
|\widehat g(\{k\})|=|\mathbb E d_k|
\le\mathbb E|d_k|
=\operatorname{Inf}_k(g)=:p_k.
\]
Hence `e_k<=p_k^2`.  Since `T_V<=T_1`,
\[
{e_k\log_2(1/e_k)\over p_k}
\le
\sqrt{e_k}\log_2{1\over e_k}
\le {2\over e\ln2}.
\]
The last maximum occurs at `sqrt(e_k)=e^{-1}`.  Therefore
\[
\boxed{
T_V(g)\le {2\over e\ln2}I(g)
=1.061475690846\ldots\, I(g).
}
\tag{4.1}
\]
Also
\[
W_1(g)\le\sum_kp_k^2\le
\left(\max_kp_k\right)I(g).
\tag{4.2}
\]

So the only noninherited erasure terms in (3.3) have a universal
influence-paid logarithmic part plus an outer-erasure part damped by the
inner singleton/influence ratio.

## 5. Balanced identical-inner corollary: a three-state recursion

Now assume `G` and `g` are balanced and set
\[
F=G(g^{(1)},\ldots,g^{(m)})
\]
with identical disjoint copies.  Then `V=1`, `q_A=hat(G)(A)^2`, and the refund
in (2.1) vanishes.  Define
\[
b(f)={B(f)\over I(f)},\qquad
r(f)={W_1(f)\over I(f)},\qquad
t(f)={T_1(f)\over I(f)}.
\]
Equations (3.3)-(3.4) give
\[
\boxed{
b(F)\le b(g)+r(g)b(G)+t(g).
}
\tag{5.1}
\]

Singleton Fourier coefficients factor exactly:
\[
\widehat F(\{(j,k)\})
=\widehat G(\{j\})\widehat g(\{k\}),
\]
so
\[
\boxed{
r(F)=r(G)r(g),
\qquad
t(F)=r(g)t(G)+r(G)t(g).
}
\tag{5.2}
\]

Thus erasure propagation under balanced composition is controlled by three
scalar states `(b,r,t)`: inherited erasure `b`, singleton fraction `r`, and
singleton-label entropy `t`.

## 6. Fixed balanced self-composition: explicit uniform selector payment

Let `G` be balanced and not a signed dictator, and define
\[
F_1=G,\qquad
F_{d+1}=G(F_d^{(1)},\ldots,F_d^{(m)}).
\]
Put `b=b(G)`, `r=r(G)`, `t=t(G)`.

Because a balanced function has no empty Fourier mass,
`I(G)>=W_1(G)`.  Equality would force all Fourier mass onto level one.
For a Boolean function that would make `G^2=1` a degree-one square identity,
forcing all products of distinct linear coefficients to vanish; hence exactly
one coefficient has magnitude one and `G` is a signed dictator.  Therefore
for the present non-dictator
\[
\boxed{0\le r<1.}
\tag{6.1}
\]

Iterating (5.2) gives
\[
r(F_d)=r^d,\qquad
t(F_d)=d\,t\,r^{d-1}.
\tag{6.2}
\]
Inserting these states into (5.1) and summing yields
\[
\boxed{
b(F_d)\le
b{1-r^d\over1-r}
+t\,{1-dr^{d-1}+(d-1)r^d\over(1-r)^2}.
}
\tag{6.3}
\]
Hence
\[
\boxed{
\sup_d {B(F_d)\over I(F_d)}
\le {b\over1-r}+{t\over(1-r)^2}<\infty.
}
\tag{6.4}
\]

This gives a second, global explanation for why repeatedly composing one fixed
balanced non-dictator seed cannot make the erasure selector diverge: the outer
activation tax is transported only through singleton Fourier mass, and that
mass fraction multiplies at every level.

This complements, but does not replace, the concurrent account02/B14 theorem
that the **local restriction ratio** `rho_0(F_d)` converges for every fixed
balanced seed.

## 7. Existential physical-coordinate consequence

For every Boolean `f`,
\[
\min_{i:\operatorname{Inf}_i>0}
{B_i(f)\over\operatorname{Inf}_i(f)}
\le {B(f)\over I(f)}
\]
by influence-weighted averaging.  Together with the exact
`Delta_i=B_i+JS_i` identity and the scalar JS bound,
\[
\min_i{\Delta_iH(f)\over\operatorname{Inf}_i(f)}
\le {B(f)\over I(f)}+{2\over\ln2}.
\tag{7.1}
\]

Therefore every depth of the fixed balanced self-composition above has **some**
physical restriction coordinate satisfying
\[
\boxed{
{\Delta_iH(F_d)\over\operatorname{Inf}_i(F_d)}
\le
{b\over1-r}+{t\over(1-r)^2}+{2\over\ln2}.
}
\tag{7.2}
\]

This is an existential payment only.  It does **not** assert the false
every-prescribed-coordinate inequality, and by itself it does not close an
induction through arbitrary restrictions unless the descendants are shown to
retain a comparable bound.

## 8. Why this does not solve FEI

Full FEI remains open.  The exact identity covers disjoint compositions, not
arbitrary Boolean functions.  The older bent-marker and parity-synergy
counterexamples remain untouched.  The finite recursive Numaro construction
with all physical coordinates having large local decrement is also untouched:
(7.2) is a seed-dependent upper bound and is not claimed sharp.

The useful structural change is that the arbitrary-bias formula (2.1) survives
physical restrictions of inner blocks and contains an explicit positive
constant/singleton refund.  A future restriction-tree proof can therefore ask
a sharper question than “bound every local decrement”:

> Can the refunds `E(mu^2,e)` and the multiplicative singleton fractions be
> telescoped along a restriction tree so that each outer erasure payment is
> charged only once?

That is the next B14 target.  It is compatible with the known all-coordinate
counterexamples because it is nonlocal and mass weighted.

## 9. Executed finite diagnostics

`verify_balanced_erasure_composition.py` was run in a clean standard-library
Python subprocess.  It performed:

- 305 direct local checks of the **arbitrary-bias** identity (2.1) by exhaustive
  Fourier transforms of randomly generated small Boolean compositions;
- 20,004 scalar checks of (3.1);
- 50 direct balanced-composition checks of the global bound and the exact
  `(r,t)` state propagation;
- 20,000 sampled checks of the pointwise constant in (4.1).

Result: `PASS`.  Maximum absolute local-identity error was
`4.440892098500626e-16`; exact `(r,t)` recursion error in the sampled cases was
`0.0`.  The smallest recorded scalar slack was `-3.54e-14`, within the
explicit floating-point assertion tolerance; the theorem itself is the
analytic concavity proof above, not the float test.

These diagnostics are formula checks only.  They are not exhaustive evidence
for unrestricted FEI and not a proof assistant verification.
