# ProofNet24 P22 — Kernel Benign Audit / Selected-Source S4 Assistance

**Run timestamp:** 2026-09-15 03:21:09 Asia/Jerusalem  
**Scope:** P04 Target 2 independent preservation audit; post-certification assistance on P04/P20 Target 4. **NO number theory.**

# Exact Target-2 verdict

For fixed \(h>0\), \(d_\ell=2^{2^\ell}\), \(n_\ell=2^{2^{2\ell}}\), iid
\(X_i\sim {\rm Unif}(S^{d_\ell-1})\), iid Gaussian noise of variance
\(\sigma^2\), and every fixed-degree signal sequence
\[
f_d\in\bigoplus_{s=0}^{q_0}\mathcal H_{d,s},
\qquad
\sup_d\|f_d\|_{L^2}\le B,
\]
the actual Gaussian-kernel minimum-norm interpolant satisfies
\[
\boxed{
E_{X_0}\!\left[
(\widehat f_\ell(X_0)-f_{d_\ell}(X_0))^2
\mid X_{1:n_\ell},\varepsilon_{1:n_\ell}
\right]\xrightarrow{\mathbb P}0.
}
\]
The certified proof also gives almost-sure convergence along the prescribed
level sequence under any coupling with the correct levelwise marginals.

\[
\boxed{\texttt{P22-T2-RECHECK-16: PASS}.}
\]

No Target-2 dependency is reopened by the latest P04 report.

# 1. Target-2 audit

Put
\[
R=2^\ell,\qquad d=2^R,\qquad n=d^R,\qquad k=R+\ell-1.
\]
The exact degree-\(s\) harmonic multiplicity is
\[
N_{d,s}
=
\binom{d+s-1}{s}-\binom{d+s-3}{s-2}.
\]
The critical ratios remain
\[
\frac{N_{d,k}}n=d^{\delta_*+o(1)},
\qquad
\frac{D_{<k}}n=d^{-(1-\delta_*)+o(1)},
\qquad
\delta_*=\frac1{\log2}-1.
\]

For \(\gamma=h^{-2}\), the exact Gaussian-kernel Mercer eigenvalue is
\[
\lambda_{d,s}
=
e^{-\gamma}
\sum_{r\ge0}
\frac{\gamma^{s+2r}}
{2^r r!\,d(d+2)\cdots(d+2(s+r)-2)},
\]
equivalently
\[
\lambda_{d,s}
=
e^{-\gamma}\Gamma(d/2)(2/\gamma)^{d/2-1}
I_{s+d/2-1}(\gamma).
\]
The positive Bessel series gives the whole-tail inequality
\[
\boxed{
\lambda_{d,s+1}\le
\frac{\gamma}{d+2s}\lambda_{d,s}.
}
\]

For a pure degree-\(s\) spherical harmonic,
\[
\boxed{
\|Y_s\|_p\le(p-1)^{s/2}\|Y_s\|_2,\qquad p\ge2,
}
\]
with no hidden degree-dependent constant.  At the proof moment order \(p=R\),
the deliberately conservative Rosenthal terms are
\[
dR\,\frac{3^k}{\sqrt n}=d^{-R/2+O(1)}\to0,
\qquad
Rd^2\,\frac{(2R)^k}{n}=d^{-R+\ell+O(1)}\to0.
\]
The infinite harmonic tail is summed factorially rather than truncated at
fixed degree.

The KRM application uses the centered proof-level row-square/correlation-kernel
statistic after U-statistic decoupling and before later global relaxations; no
iid-coordinate or max-entry substitution is made.  The low and high blocks
satisfy
\[
\Psi^\top\Psi=n(I+o_{\rm op}(1)),
\qquad
K_T=\tau(I+o_{\rm op}(1)).
\]
Exact RKHS elimination gives
\[
G_0=\tau\Lambda^{-1}+\Psi^\top W\Psi\succeq cnI,
\qquad
\|G_0^{-1}\|=O(n^{-1}).
\]
Consequently
\[
E_\varepsilon[\mathcal R_\ell\mid X]
\le
C\!\left[
\sigma^2\!\left(\frac{D_{<k}}n+\frac n{N_k}\right)
+
B^2\!\left(\frac{d^{2q_0}}{n^2}
+\frac{d^{2q_0}}{nN_k}\right)
\right]\to0.
\]
Markov in the Gaussian labels yields the realized conditional-risk theorem.

The imported primary-source hypotheses remain matched: KRM's kernel-matrix
method is based on U-statistic decoupling and noncommutative Khintchine with a
correlation-kernel matrix, while the Mercer ratio comes from the positive
DLMF series for \(I_\nu\).

# 2. Peer audit: `P20-S4-SPHERICAL-AVERAGE-32`

**Audit ID:** `P22-AUDIT-P20-S4-AVG-16`  
**Source:** `P20_kernel_hard_edge_2026-09-15_03-11-22__run-report.md`  
**Library id:** `file_000000008598820c8962ddf994f26e7d`  
**Verdict:** \(\boxed{\text{PASS}}\).

Let \(L\subset\operatorname{Sym}_d^0\) have Frobenius-orthonormal basis
\(A_1,\ldots,A_k\), and put
\[
C_L=\sum_{a=1}^kA_a^2.
\]
For \(V_L=\sum_ac_aA_a\) with \(c\) uniform on \(S^{k-1}\),
\[
E[c_ac_bc_cc_d]
=
\frac{\delta_{ab}\delta_{cd}
+\delta_{ac}\delta_{bd}
+\delta_{ad}\delta_{bc}}{k(k+2)}.
\]
Expanding \(\operatorname{tr}(V_L^4)\) gives
\[
\boxed{
E\,\operatorname{tr}(V_L^4)
=
\frac{
2\operatorname{tr}(C_L^2)
+\sum_{a,b}\operatorname{tr}(A_aA_bA_aA_b)}
{k(k+2)}.
}
\]
For symmetric \(A,B\),
\[
|\operatorname{tr}(ABAB)|
=|\langle AB,BA\rangle_F|
\le\operatorname{tr}(A^2B^2),
\]
hence
\[
\boxed{
\frac{\operatorname{tr}(C_L^2)}{k(k+2)}
\le E\,\operatorname{tr}(V_L^4)
\le
\frac{3\operatorname{tr}(C_L^2)}{k(k+2)}.
}
\]
Every coefficient and pairing checks.

# 3. New theorem: a scalar tangent probe for contraction geometry

Let
\[
E_d=\operatorname{Sym}_d^0,
\qquad
m=\frac{(d-1)(d+2)}2.
\]
For \(u\in S^{d-1}\), define the positive operator \(R_u:E_d\to E_d\) by
\[
\langle A,R_uA\rangle_F=\|Au\|_2^2.
\]

## `P22-T4-TANGENT-PROBE-16` — PROVED

The exact spectrum of \(R_u\) is
\[
\boxed{
\frac{d-1}{d}\ (1\text{ time}),\qquad
\frac12\ (d-1\text{ times}),\qquad
0\ (m-d\text{ times}).
}
\]
Indeed, the radial traceless vector
\[
B_u=\sqrt{\frac d{d-1}}
\left(uu^\top-\frac1dI\right)
\]
has \(\|B_u\|_F=1\) and
\(\|B_uu\|^2=(d-1)/d\); tangent vectors
\((uy^\top+yu^\top)/\sqrt2\), \(y\perp u\), have value \(1/2\);
and the transverse sector \(Au=0\) has value zero.  Therefore
\[
\boxed{
\operatorname{tr}R_u=\frac md,
\qquad
\operatorname{tr}(R_u^2)
=
\left(\frac{d-1}{d}\right)^2+\frac{d-1}{4}.
}
\]

For any \(k\)-subspace \(L\) with projector \(P_L\),
\[
\boxed{
u^\top C_Lu=\operatorname{tr}(P_LR_u).
}
\]
Now suppose the law of \(L\) is invariant under physical conjugation by
\(O(d)\), with deterministic rank \(k\).  For fixed \(u_0\), put
\[
Z=\operatorname{tr}(P_LR_{u_0})=u_0^\top C_Lu_0.
\]
Then
\[
EZ=\frac{k}{d}.
\]
Using
\[
E_{u\sim S^{d-1}}(u^\top Cu)^2
=
\frac{2\operatorname{tr}(C^2)+(\operatorname{tr}C)^2}{d(d+2)}
\]
and \(\operatorname{tr}C_L=k\), physical invariance yields the exact identity
\[
\boxed{
E\operatorname{tr}(C_L^2)
=
\frac{k^2}{d}
+
\frac{d(d+2)}2\operatorname{Var}(Z).
}
\]
Thus the average-contraction target
\[
E\operatorname{tr}(C_L^2)=O(k^2/d)
\]
is reduced to
\[
\boxed{
\operatorname{Var}\{\operatorname{tr}(P_LR_{u_0})\}
=O(k^2/d^3).
}
\]
At the critical hard-edge scale \(k\asymp d^{3/2}\), this asks only for
\[
\boxed{\operatorname{Var}(Z)=O(1).}
\]

For comparison, if \(P_L\) is Haar rank \(k\) in \(\mathbb R^m\),
\[
\operatorname{Var}\{\operatorname{tr}(P_LA)\}
=
\frac{2k(m-k)}{m(m-1)(m+2)}
\left[
\operatorname{tr}(A^2)-\frac{(\operatorname{tr}A)^2}{m}
\right].
\]
For \(A=R_u\) and \(k\asymp d^{3/2}\), this is \(\asymp d^{-3/2}\).
The actual theorem therefore has enormous slack relative to Haar.

# 4. New theorem: exact radial-source comparison on thick singular shells

The latest P20 report correctly weakens the uniform bottom-subspace theorem
to the selected direction
\[
W_k=
\frac{P_{E_k}H^{-1}b}{\|P_{E_k}H^{-1}b\|},
\]
because the already-proved tail satisfies
\[
\eta_k=O_P(d^{-1/4}),
\qquad k\asymp d^{3/2}.
\]
The remaining issue is whether inverse weighting biases the selected direction
toward \(S_4\)-bad vectors.

## `P22-T4-SOURCE-SHELL-COMP-16` — PROVED

Let the exact radial source have iid coordinates
\[
b_i=\mu_d+\xi_i,
\]
with
\[
|\mu_d|=O(d^{-1/2}),\qquad
0<c\le E\xi_i^2\le C,\qquad
E\xi_i^4\le C.
\]
Let \(U,V\in\mathbb R^{m\times r}\) have orthonormal columns,
\(D=\operatorname{diag}(w_1,\ldots,w_r)\), \(w_j>0\), and assume
\((U,V,D)\) is independent of \(b\). Put
\[
y=VDU^\top b,\qquad
S_2=\operatorname{tr}(D^2),\qquad
\rho=\frac{\|D\|_{\rm op}^2}{S_2}.
\]
If \(v_j\) are the columns of \(V\), put
\[
M_j=T(v_j),\qquad
C_D=\sum_jw_j^2M_j^2.
\]
Assume
\[
\boxed{
\frac{\operatorname{tr}(C_D^2)}{S_2^2}=O(d^{-1}),
\qquad
\rho=O(d^{-3/2}).
}
\]
Then, conditionally on \((U,V,D)\),
\[
\boxed{
\operatorname{tr}\!\left[
T\!\left(\frac y{\|y\|}\right)^4
\right]=O_P(d^{-1}).
}
\]

### Proof

Write \(b=\mu{\bf1}+\xi\),
\[
y_0=VDU^\top\xi,\qquad
a=\mu VDU^\top{\bf1},\qquad y=y_0+a.
\]
For
\[
A=UD^2U^\top,
\]
the exact nonzero-mean iid quadratic-form expansion gives
\[
\operatorname{Var}(b^\top Ab)
\le
C\left[
\operatorname{tr}(A^2)
+\mu^2m\|A\|^2
+|\mu|\sqrt{m\operatorname{tr}(A^2)}\,\|A\|
\right].
\]
Because
\[
\operatorname{tr}(A^2)\le\rho S_2^2,\qquad
\|A\|=\rho S_2,
\]
the relative variance is at most
\[
C\left[\rho+d\rho^2+\sqrt d\,\rho^{3/2}\right]=o(1).
\]
Moreover
\[
E\|y\|^2\ge cS_2,
\]
so \(\|y\|^2\ge c_1S_2\) with high probability.

For the centered numerator define
\[
B_i=T(VDU^\top e_i).
\]
Then
\[
T(y_0)=\sum_i\xi_iB_i
\]
and exact fourth-moment pairing gives
\[
E\operatorname{tr}(T(y_0)^4)
=
\sigma_b^4\!\left[
2\operatorname{tr}(C_D^2)+R_D\right]
+\kappa_4\sum_i\operatorname{tr}(B_i^4),
\]
where
\[
|R_D|\le\operatorname{tr}(C_D^2).
\]
Writing
\[
\ell_i=\|B_i\|_F^2
=e_i^\top UD^2U^\top e_i,
\]
we have
\[
\sum_i\ell_i=S_2,\qquad
\max_i\ell_i\le\rho S_2,
\]
hence
\[
\sum_i\operatorname{tr}(B_i^4)
\le
\sum_i\ell_i^2
\le
\rho S_2^2.
\]
Therefore
\[
E\operatorname{tr}(T(y_0)^4)=O(S_2^2/d).
\]

The deterministic source-mean part obeys
\[
\|a\|^2
\le
\mu^2m\|D\|^2
\le
Cd\rho S_2,
\]
so
\[
\|T(a)\|_{S_4}^4
\le\|a\|^4
\le
Cd^2\rho^2S_2^2
=O(S_2^2/d).
\]
The Schatten triangle inequality and the denominator lower bound yield the
claim.

### Shell corollary

If
\[
\frac{\max_jw_j}{\min_jw_j}\le\Lambda
\]
for fixed \(\Lambda\), the shell rank satisfies
\[
r\ge c_0d^{3/2},
\]
and the unweighted shell subspace \(L=\operatorname{span}(v_1,\ldots,v_r)\)
satisfies
\[
\operatorname{tr}(C_L^2)\le K\frac{r^2}{d},
\]
then the theorem applies. Indeed,
\[
\rho\le\frac{\Lambda^2}{r},
\]
and
\[
0\preceq C_D\preceq(\max_jw_j^2)C_L,
\]
which gives
\[
\frac{\operatorname{tr}(C_D^2)}{S_2^2}
\le\frac{K\Lambda^4}{d}.
\]

Thus contraction-average geometry really does transfer to the exact
non-Gaussian radial source on every sufficiently thick bounded-condition-number
inverse shell.  The unresolved regime is the thin set of highly amplified
bottom modes where \(\rho\) is not small.

# 5. Counterexample and route audit

- **Microscopic hard-edge universality is needed for Target 2:** REJECTED.
- **Fixed-degree constants may be extrapolated to the growing cutoff:** REJECTED.
- **Maximum-entry control may replace the centered KRM proof statistic:** REJECTED.
- **Physical invariance / mean-projector isotropy / fixed probes imply uniform
  \(S_4\)-goodness:** DISPROVED by the P04/P20 planted model.
- **Uniform bottom-subspace \(S_4\)-goodness is necessary for the selected
  inverse vector:** FALSE.  The planted model is supremum-bad but
  typical-direction good.
- **Contraction average alone proves the selected vector theorem:** FALSE.
  Source-angular comparison is also needed; the new shell theorem supplies it
  only when inverse weights have effective rank \(\gtrsim d^{3/2}\).
- **The source mean is harmless on every shell:** FALSE as a uniform claim.
  The proof shows explicitly why a sufficiently thick shell suppresses its
  worst-case contribution.

# 6. Ledger

## PROVED — Target 2

- exact Mercer spectrum and whole-tail ratio;
- harmonic multiplicities and critical cutoff;
- growing-degree dimension-free hypercontractivity;
- factorial infinite-tail summation;
- conservative Rosenthal closure;
- centered KRM decoupling/NCK step;
- high-tail operator-norm isotropy;
- low-block matrix Chernoff;
- exact RKHS low/high elimination;
- inverse-Gram control;
- low/high Gaussian-noise risk;
- fixed-degree signal bias and tail leakage;
- conditional excess risk \(\to0\) in probability;
- almost-sure prescribed-level strengthening;
- two complete OTHER-worker audits;
- ProofNet24 certification;
- `P22-T2-RECHECK-16` PASS.

## PROVED — post-closure

Inherited:
- trace/traceless radial decomposition and \(b\perp H\);
- alpha moment and no-anchor inverse-source tail;
- planted-orbit no-go;
- selected-bottom reduction;
- \(d^{3/2}\) dimension barrier;
- fixed-mode density modules.

New this run:
- `P22-AUDIT-P20-S4-AVG-16` PASS;
- `P22-T4-TANGENT-PROBE-16`;
- exact tangent-operator spectrum;
- exact contraction-variance identity;
- Haar tangent-probe calibration;
- `P22-T4-SOURCE-SHELL-COMP-16`.

## OPEN

1. For the actual bottom spectral subspace at \(k\asymp d^{3/2}\),
   \[
   \operatorname{Var}\{\operatorname{tr}(P_{E_k}R_u)\}=O(1).
   \]
2. Equivalently at expectation scale,
   \[
   E\operatorname{tr}(C_{E_k}^2)=O(k^2/d).
   \]
3. Source-selected \(S_4\) control on thin/dominant inverse shells.
4. Full selected-bottom theorem
   \[
   \operatorname{tr}(T(W_k)^4)=O_P(d^{-1}).
   \]
5. Growing bottom modes, secular comparison, graph-factor \(L^1\) removal,
   reciprocal resistance, and the final fixed-\(t\) hard-edge law.

# 7. Highest-value next attack

## `P22/P20-T4-TANGENT-VAR-17`

For
\[
k=\lfloor c d^{3/2}\rfloor
\]
and one fixed \(u\in S^{d-1}\), prove
\[
\boxed{
\operatorname{Var}\!\left[
\operatorname{tr}(P_{E_k(H)}R_u)
\right]=O(1).
}
\]
This is a scalar spectral-projector statistic for a fixed rank-\(d\) physical
probe, not a uniform Grassmannian theorem and not a microscopic \(p^{-2}\)
hard-edge theorem.

Promising routes are:

1. a smoothed spectral projector / resolvent for
   \(\operatorname{tr}(f(H^\top H)R_u)\) near the \(k\)-th singular scale;
2. leave-many-rows-out conditioning using only genuinely fresh original
   harmonic rows;
3. exchangeable row replacement and an Efron--Stein variance bound after
   spectral smoothing, followed by control of the transition window.

Once this average-contraction module is proved,
`P22-T4-SOURCE-SHELL-COMP-16` handles all thick dyadic inverse shells.
The remaining thin shells become a one-vector bottom-mode problem rather than
a whole-subspace problem.

# Bottom line

Target 2 remains rigorously solved and certified.

The new post-closure contribution is a lower-complexity route to the actual
selected inverse direction.  The P20 average-\(S_4\) identity is independently
verified, and its geometry is reduced to one fixed tangent probe:
\[
\boxed{
E\operatorname{tr}(C_{E_k}^2)
=
\frac{k^2}{d}
+
\frac{d(d+2)}2
\operatorname{Var}\{\operatorname{tr}(P_{E_k}R_u)\}.
}
\]
At \(k\asymp d^{3/2}\), the desired average geometry needs only an \(O(1)\)
variance bound.

Separately, the new source-shell theorem proves that whenever a dyadic
inverse-weight shell is sufficiently thick and has natural contraction-average
geometry, the exact non-Gaussian radial source selects an \(S_4\)-good
direction from it.

The remaining obstruction is therefore concentrated in the geometry of the
thin, highly amplified bottom singular shells.
