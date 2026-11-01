# B14 — corrected-entropy random-erasure tube and multiscale influence-instability budget

**Status:** PARTIAL / PROVED structural theorem. **Full uniform-cube Friedgut–Kalai Fourier entropy–influence remains OPEN / NOT PROVED.**  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.  
**Route:** existential restriction induction / erasure selector, APPROACHES 5–6.  
**Fresh repository head immediately before this delivery:** `e3d1b81f9275857745846cc0571212d18fc4d6e4`.

This run does not audit or rerun the settled read-once certificate. It combines two already proved ingredients at their exact scopes:

1. the B14 influence potential
   \[
   \Phi(f)=\sum_i\eta(p_i),\qquad
   p_i=\operatorname{Inf}_i(f),
   \]
   where
   \[
   \eta(p)=1-h_2\!\left(\frac12+\sqrt{s(1-s)}\right),\qquad
   s=\min\{p,1-p\},
   \]
   satisfies \(0\le\Phi\le (2/\ln2)I\), is \(4/(3\ln2)\)-strongly concave, and absorbs the singleton Jensen–Shannon restriction term; and

2. the current block restriction theorem
   \[
   \Delta_AH=B_A+JS_A,\qquad
   B_A=H(X_A\mid X_{A^c}),\qquad
   JS_A\le\sum_{i\in A}\eta(p_i),
   \]
   for the Fourier spectral sample \(X\).

The new point is that the same bounded potential absorbs **every physical block simultaneously**, and after Bernoulli averaging this gives an exact one-parameter descent identity for the corrected entropy. The resulting critical-core constraint contains an all-scale variance penalty for how influences move under random restrictions.

No publication-priority claim is made.

## 1. Block potential absorption

Put
\[
\mathcal E(f):=H(f)-\Phi(f).
\]

Fix a physical block \(A\). For each \(k\notin A\), let
\[
p_k^{A,z}:=\operatorname{Inf}_k(f_{A=z}).
\]
Influence is a martingale under uniform restrictions:
\[
p_k=\mathbb E_z p_k^{A,z}.
\]
Define the cross-coordinate potential Jensen gap
\[
G_A(f):=
\sum_{k\notin A}
\left[
\eta(p_k)-\mathbb E_z\eta(p_k^{A,z})
\right]\ge0.
\tag{1.1}
\]

Because coordinates in \(A\) disappear in every child,
\[
\boxed{
\Delta_A\Phi
=
\sum_{i\in A}\eta(p_i)+G_A.
}
\tag{1.2}
\]

The inherited block-JS theorem gives
\[
JS_A\le\sum_{i\in A}\eta(p_i),
\]
hence the **block potential rebate**
\[
\boxed{
R_A^\Phi
:=
\Delta_A\Phi-JS_A
\ge G_A\ge0.
}
\tag{1.3}
\]

Therefore
\[
\boxed{
\Delta_A\mathcal E
=
B_A-R_A^\Phi
\le B_A-G_A
\le B_A
\qquad\text{for every physical block }A.
}
\tag{1.4}
\]

This is the block version of the singleton corrected-entropy identity. It removes the coherent recombination term from the restriction payment without paying \(2/\ln2\) again at each block or each depth.

### Quantitative rebate from strong concavity

Since \(\eta\) is \(m\)-strongly concave with
\[
m=\frac{4}{3\ln2},
\]
Jensen's inequality with curvature yields
\[
\eta(p_k)-\mathbb E_z\eta(p_k^{A,z})
\ge
\frac m2\,\operatorname{Var}_z(p_k^{A,z})
=
\frac{2}{3\ln2}\operatorname{Var}_z(p_k^{A,z}).
\]
Thus
\[
\boxed{
R_A^\Phi
\ge
G_A
\ge
\frac{2}{3\ln2}
\sum_{k\notin A}
\operatorname{Var}_z\!\left(\operatorname{Inf}_k(f_{A=z})\right).
}
\tag{1.5}
\]

So every block restriction has a nonnegative *second-order refund* measuring how much the surviving influences fluctuate across its children.

## 2. Bernoulli random erasure

Let \(A_t\) contain each physical coordinate independently with probability \(t\in[0,1]\). Define
\[
F_f(t):=\mathbb E B_{A_t},
\qquad
\mathcal J_f(t):=\mathbb E JS_{A_t},
\tag{2.1}
\]
and retain the already proved spectral-erasure deficit
\[
D_f(t):=tH(f)-F_f(t)\ge0.
\tag{2.2}
\]

Define the new **potential-dissipation curve**
\[
\boxed{
C_{\Phi,f}(t)
:=
\mathbb E\,\Delta_{A_t}\Phi-t\Phi(f)
=
\mathbb E\,G_{A_t}.
}
\tag{2.3}
\]
The second equality follows directly from (1.2), because
\[
\mathbb E\sum_{i\in A_t}\eta(p_i)=t\Phi.
\]
Hence \(C_{\Phi,f}(t)\ge0\).

There is also a useful one-coordinate representation. For \(k\), draw a Bernoulli-\(t\) subset \(A_t^{(k)}\subseteq[n]\setminus\{k\}\), then draw a uniform restriction value \(Z\), and set
\[
P_{k,t}:=\operatorname{Inf}_k(f_{A_t^{(k)}=Z}).
\]
Then \(\mathbb EP_{k,t}=p_k\), and
\[
\boxed{
C_{\Phi,f}(t)
=
(1-t)\sum_k
\left[
\eta(p_k)-\mathbb E\eta(P_{k,t})
\right].
}
\tag{2.4}
\]
Strong concavity gives the all-scale lower bound
\[
\boxed{
C_{\Phi,f}(t)
\ge
\frac{2(1-t)}{3\ln2}
\sum_k\operatorname{Var}(P_{k,t}).
}
\tag{2.5}
\]

Finally, averaging the block-JS bound gives
\[
\boxed{
0\le \mathcal J_f(t)\le t\Phi(f).
}
\tag{2.6}
\]

## 3. Exact corrected-erasure dual identity

Average (1.4) without discarding the exact rebate. Since
\[
\Delta_A\mathcal E
=
B_A+JS_A-\Delta_A\Phi,
\]
we have
\[
\overline{\Delta\mathcal E}_f(t)
:=
\mathbb E\,\Delta_{A_t}\mathcal E
=
F_f(t)+\mathcal J_f(t)-t\Phi(f)-C_{\Phi,f}(t).
\tag{3.1}
\]

Because \(\mathcal E=H-\Phi\), subtraction from the corrected linear chord gives the exact identity
\[
\boxed{
t\mathcal E(f)
-
\overline{\Delta\mathcal E}_f(t)
=
D_f(t)+C_{\Phi,f}(t)-\mathcal J_f(t).
}
\tag{3.2}
\]

This is the main new formula. It resolves the random-erasure descent defect into three terms with fixed signs or interpretations:

- \(D_f(t)\): dependence deficit of the spectral-membership law;
- \(C_{\Phi,f}(t)\): multiscale influence-instability paid by concavity of the bounded potential;
- \(\mathcal J_f(t)\): the coherent restriction/recombination information still returned to the child spectrum.

The earlier raw-\(H\) random-erasure argument required an auxiliary Bayes-error surcharge. In (3.2), that surcharge disappears after subtracting the bounded influence potential.

## 4. Corrected-ratio descent certificate

Assume \(I(f)>0\) and put
\[
\rho(f):=\frac{\mathcal E(f)}{I(f)}.
\]
The exact block influence identity gives
\[
\mathbb E I_{A_t}=tI(f).
\]

### Theorem 4.1

If for some \(0<t<1\),
\[
\boxed{
D_f(t)+C_{\Phi,f}(t)>\mathcal J_f(t),
}
\tag{4.1}
\]
then there is a nonempty proper physical block \(A\) for which
\[
\Delta_A\mathcal E(f)<\rho(f)I_A(f),
\tag{4.2}
\]
and consequently at least one nonconstant child \(f_{A=z}\) has
\[
\frac{\mathcal E(f_{A=z})}{I(f_{A=z})}>\rho(f).
\tag{4.3}
\]

#### Proof

By (3.2),
\[
\mathbb E\left[
\Delta_{A_t}\mathcal E-\rho I_{A_t}
\right]
=
-\left(D_f(t)+C_{\Phi,f}(t)-\mathcal J_f(t)\right)<0.
\]
The empty block contributes \(0\). The full block also contributes \(0\), because restriction of all coordinates leaves constants and therefore
\[
\Delta_{[n]}\mathcal E=\mathcal E=\rho I.
\]
Hence some nonempty proper block has (4.2). Using
\[
\mathcal E(f)-\mathbb E_z\mathcal E(f_{A=z})
=\Delta_A\mathcal E,
\qquad
I(f)-\mathbb E_zI(f_{A=z})=I_A,
\]
(4.2) implies
\[
\mathbb E_z\mathcal E(f_{A=z})
>
\rho\,\mathbb E_zI(f_{A=z}),
\]
so at least one nonconstant child has corrected ratio \(>\rho\). QED.

This is an existential selector. It does not assert the known-false every-prescribed-coordinate payment.

## 5. All-scale tube for a corrected-critical descendant

Choose a nonconstant physical descendant \(g\) maximizing
\[
\rho(g)=\frac{\mathcal E(g)}{I(g)}
\]
among all nonconstant physical descendants. Theorem 4.1 cannot fire at \(g\). Therefore, simultaneously for every \(0<t<1\),
\[
\boxed{
D_g(t)+C_{\Phi,g}(t)
\le
\mathcal J_g(t)
\le
t\Phi(g).
}
\tag{5.1}
\]

Combining with (2.5),
\[
\boxed{
D_g(t)
+
\frac{2(1-t)}{3\ln2}
\sum_k\operatorname{Var}(P_{k,t})
\le
\mathcal J_g(t)
\le
t\Phi(g)
\le
\frac{2t}{\ln2}I(g).
}
\tag{5.2}
\]

This is a **multiscale critical-core budget**. A hypothetical high-FEI-ratio function can be passed to a corrected-critical descendant for which, at every erasure density:

1. spectral dependence \(D_g(t)\),
2. plus the all-orders instability of the influence martingales,

must both fit inside the same JS information bank \(\mathcal J_g(t)\), itself bounded by the single initial potential \(t\Phi(g)\).

The constraint is independent of the candidate FEI constant. If the original function violates \(H\le CI\), then
\[
\rho(g)>C-\frac2{\ln2},
\]
but (5.1)–(5.2) hold regardless of how large that corrected ratio is.

## 6. Endpoint recovery and why this moves the route

As \(t\downarrow0\),
\[
\frac{D_f(t)}t
\longrightarrow
\operatorname{DTC}(X),
\qquad
\frac{\mathcal J_f(t)}t
\longrightarrow
\sum_i JS_i.
\]
Also
\[
\frac{C_{\Phi,f}(t)}t
\longrightarrow
\sum_{i\ne k}
\left[
\eta(p_k)
-
\frac{\eta(p_k(f_{i,+}))+\eta(p_k(f_{i,-}))}{2}
\right].
\]
Thus (5.1) recovers the previously proved singleton second-order necessary condition
\[
\operatorname{DTC}(X)+\sum_{i\ne k}G_{ik}
\le
\sum_iJS_i.
\]

The new statement is not merely that endpoint: it requires the analogous inequality at **every restriction scale** \(t\), and (2.5) packages all higher-order influence variation into the same inequality.

At the other extreme, \(t\uparrow1\), all three terms vanish continuously, as they must.

## 7. Finite deterministic check

`verify_corrected_erasure_tube.py` directly computes Fourier spectra, physical restrictions, block erasures, block JS terms, the potential and all physical descendants. It exhausts Boolean truth tables up to global sign for \(n\le3\), checks all physical blocks, chooses a corrected-ratio-maximal descendant, and checks \(t\in\{1/4,1/2,3/4\}\).

Counts:

- \(n=1\): 2 global-sign classes, 2 block cases, 3 corrected-critical curve cases;
- \(n=2\): 8 classes, 24 block cases, 21 curve cases;
- \(n=3\): 128 classes, 896 block cases, 381 curve cases.

No negative violation was observed for
\[
\Delta_A\Phi-JS_A\ge0,
\qquad
C_{\Phi,f}(t)\ge
\frac{2(1-t)}{3\ln2}\sum_k\operatorname{Var}(P_{k,t}),
\qquad
\mathcal J-D-C_\Phi\ge0
\]
on corrected-critical descendants. The largest floating residual in the exact identity (3.2) was \(2.78\times10^{-16}\).

These finite calculations are sanity checks only; the proof above is analytic.

Exact local source SHA-256 before repository upload:  
`7e817dc1cebe7a347e2cff4c56ec0d3e896c75c533d8a10d611f163bc804b1d1`.

Exact local verification-output SHA-256:  
`2aa784e5f0501d8b521d5d7a27d3f0e48e25b8a4063ad258580eb71293931d33`.

## 8. What remains open

This does **not** prove full FEI. The remaining universal obstruction is now especially concrete:

> prove that every Boolean function with sufficiently large corrected ratio \(\mathcal E/I\) has some scale \(t\in(0,1)\) at which
> \[
> D_f(t)+C_{\Phi,f}(t)>\mathcal J_f(t),
> \]
> or derive an equivalent proper-block selector.

The dichotomy suggested by (5.2) is sharper than the earlier singleton version.

- If \(C_{\Phi,f}(t)\) is large at some scale, influence instability itself helps defeat corrected criticality.
- If \(C_{\Phi,f}(t)\) stays small over a range of scales, then all influence martingales are quantitatively stable under random restrictions. The next step is to combine that stability with the existing signed all-shift Boolean orthogonality / product-spectrum rigidity to show that \(D_f(t)\) cannot simultaneously remain below \(\mathcal J_f(t)\) at every scale.

That is the next B14 target. Full FEI remains OPEN.
