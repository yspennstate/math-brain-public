# account03/B09 MOC4 report — spinor cofactor compatibility and external–Weyl edge purge

Run: `20260922T064814Z-b09-moc4-r11`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Assignment: derive an inequality exploiting the special complementary `2 x 2` minors in dimension four and apply it to the determinant-support problem  
Named partner: `account04/B07`  
Outcome: **ESSENTIAL_STEP_APPLIED**. Full MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
Execution: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## 1. Fresh source state

The target is the full complex-normal `4 x 4` Marcus–de Oliveira inclusion

\[
\det(A+B)\in\operatorname{conv}\left\{\prod_{i=1}^4(a_i+b_{\sigma(i)}):\sigma\in S_4\right\},
\]

including repeated spectra and singular cases.

The newest complete campaign-lead input consumed in this run is account03/B07 run
`20260922T064004Z-account03-B07-MOC4-r12`, theorem
`MOC4-KERNEL-QUARTIC-RESERVE-v1` / residual `MOC4-MIXED-SCHUR-LS-RESIDUAL-v1`.
It reduces a putative positive-gap global maximizer to the mixed-Schur boundary branch `MSQR`
or the fully negative-definite branch `NDI`, and strengthens the mixed-Schur branch by the
Lyapunov–Schmidt reserve

\[
J_4(Z_*)+3\langle \ell^\#,(-H_{\rm pair})^+\ell^\#\rangle\le0.
\]

The required named OTHER-account result consumed is the latest account04/B07 handoff
`20260922T061043Z-account04-B07-moc4-r13`, especially
`MOC4-SPINOR-HESSIAN-MOMENT-v1` and `MOC4-PURE-BLOCK-SPINOR-RIGIDITY-v1`.
For the theorem below I also use, from the same named partner's immediately preceding immutable
run `20260922T054300Z-account04-B07-MOC4-r12`, the exact
`MOC4-SPINOR-P-COUPLED-UNISTOCHASTIC-v1` augmentation. Thus no arbitrary bistochastic data are
introduced.

The relevant B09 outer-support geometry from the preceding exact run is Drury's normalized Saxl
outer base: 24 Weyl evaluations and 48 non-Weyl external extreme functionals
`e_{tau,rho'}`. The previous B09 result excluded each external point itself by the partner's
phase identities but did not control the edges leaving those points. This run attacks exactly
that missing unitary-compatibility geometry.

## 2. Genuine complementary-minor gauge

Let `U in SU(4)` be the genuine unitary. In one of the sixteen even-even exterior-square gauges
`(i,j)`, write the anti-linear spinor block as

\[
N=N_{ij}\in M_3(\mathbb C),\qquad p=P_{ij}=|u_{ij}|^2,\qquad t^2=1-p.
\]

Put

\[
B_{\alpha\beta}=|N_{\alpha\beta}|^2.
\]

The named partner proves that for `p<1`, `A=N/t` has singular values `(1,1,0)` and admits a
genuine unitary augmentation

\[
W=\begin{pmatrix}A&\ell\\ r^*&0\end{pmatrix}\in U(4).
\]

Moreover the same original `P=|U|^{\circ2}` supplies the row/column deficits

\[
t^2-\sum_\beta B_{\alpha\beta}=P_{\tau_\alpha(i),j},
\qquad
t^2-\sum_\alpha B_{\alpha\beta}=P_{i,\tau_\beta(j)}.
\tag{2.1}
\]

This is the special dimension-four coupling used below.

## 3. New exact identity: `MOC4-SPINOR-COFACTOR-IDENTITY-v1`

Fix `alpha,beta in {1,2,3}` and let `gamma,delta` be the other two row labels and `mu,nu`
the other two column labels. Then every true unitary satisfies

\[
\boxed{
P_{\tau_\alpha(i),j}P_{i,\tau_\beta(j)}
=
\left|N_{\gamma\mu}N_{\delta\nu}-N_{\gamma\nu}N_{\delta\mu}\right|^2.
}
\tag{3.1}
\]

### Proof

Because `A=N/t` is a rank-two partial isometry with nonzero singular values `1,1`, its adjugate
has rank one and

\[
\operatorname{adj}(A)=\zeta\,r\ell^*
\]

for some unit complex phase `zeta`. Therefore

\[
|\operatorname{cof}_{\alpha\beta}(A)|^2=|\ell_\alpha|^2|r_\beta|^2.
\]

Scaling from `A` to `N=tA` multiplies every `2 x 2` cofactor by `t^2`, so

\[
|\operatorname{cof}_{\alpha\beta}(N)|^2
=t^4|\ell_\alpha|^2|r_\beta|^2.
\]

The partner augmentation and (2.1) identify

\[
t^2|\ell_\alpha|^2=P_{\tau_\alpha(i),j},
\qquad
t^2|r_\beta|^2=P_{i,\tau_\beta(j)},
\]

which proves (3.1). No stochastic relaxation is used. `QED`

Taking moduli in the two determinant monomials gives the phase-free cofactor annulus

\[
\boxed{
\left(\sqrt{B_{\gamma\mu}B_{\delta\nu}}-
      \sqrt{B_{\gamma\nu}B_{\delta\mu}}\right)^2
\le
P_{\tau_\alpha(i),j}P_{i,\tau_\beta(j)}
\le
\left(\sqrt{B_{\gamma\mu}B_{\delta\nu}}+
      \sqrt{B_{\gamma\nu}B_{\delta\mu}}\right)^2.
}
\tag{3.2}
\]

Thus every genuine exterior-square point satisfies **144** explicit nonlinear same-unitary
constraints: 16 gauges times 9 cofactors. A useful quadratic weakening is

\[
B_{\gamma\mu}B_{\delta\nu}+B_{\gamma\nu}B_{\delta\mu}
\ge \frac12 P_{\tau_\alpha(i),j}P_{i,\tau_\beta(j)}.
\tag{3.3}
\]

These equations are directly in the B09 complementary-minor variables because each gauge has

\[
B^{ij}_{\alpha\beta}
=\frac12\left(R_{\alpha\beta}-s_i(\alpha)s_j(\beta)D_{\alpha\beta}\right),
\qquad D=\frac14E^TPE.
\]

They therefore constrain exactly the same `(P,R,D)` appearing in the determinant-support
expression; they are not conditions on arbitrary bistochastic arrays.

## 4. Direct support application: `MOC4-EXTERNAL-WEYL-EDGE-PURGE-v1`

Recall the 48 external normalized-Saxl extreme functionals. For `tau in S_4` and either of the
two `rho' in S_3` deranged from the complementary-pair permutation `rho_tau`, their B09
coordinates are

\[
P^{\rm ext}=\frac13(J_4-P_\tau),
\qquad
D^{\rm ext}=\frac14E^TP^{\rm ext}E,
\qquad
R^{\rm ext}=\frac13P_{\rho_\tau}+\frac23P_{\rho'},
\]

and

\[
e_{\tau,\rho'}(f)
=\frac23\bigl(B_{\rho_\tau}(f)+B_{\rho'}(f)\bigr)-\frac13f(\tau),
\tag{4.1}
\]

where each `B_rho` is the mean over the four permutations in that Klein-four fiber.

The exact verifier finds, for every external point, 24 cofactor positions at which the left side
of (3.1) equals `1/9` while both pairing products on the right side of (3.2) vanish. This
recovers pointwise non-genuineness, but the new result is stronger:

### Theorem — all external-to-Weyl edges are target-safe

Fix one external point `e=e_{tau,rho'}` and a Weyl evaluation `delta_sigma`. Consider the outer
edge

\[
L_\lambda=\lambda e+(1-\lambda)\delta_\sigma,
\qquad 0\le\lambda\le1.
\]

1. If `sigma != tau`, then **every** point with `0<lambda<=1` violates at least one cofactor
   annulus (3.2). Hence no interior point of that edge is a genuine exterior-square unitary.
2. If `sigma=tau`, the 144 cofactor inequalities force

   \[
   \lambda\in\{0,3/4\}.
   \tag{4.2}
   \]

   The nontrivial point is not dangerous: using (4.1),

   \[
   \frac34e_{\tau,\rho'}+\frac14\delta_\tau
   =\frac12\left(B_{\rho_\tau}+B_{\rho'}\right),
   \tag{4.3}
   \]

   which is an explicit convex average of eight Weyl evaluations and therefore satisfies every
   MOC4 support inequality.

Consequently **no external–Weyl edge of the complete 72-vertex Saxl outer base can carry a
MOC4 support violation at a genuine unitary**.

### Proof of the exceptional edge condition

By left-right orbit symmetry it is enough to inspect the canonical mass patterns; the exact
verifier checks the statement on all 48 external points. On the exceptional edge to `delta_tau`
there is one cofactor for which

\[
P_{\tau_\alpha(i),j}P_{i,\tau_\beta(j)}
=\frac{\lambda(1-\lambda)}3,
\]

while exactly one determinant pairing has squared magnitude `lambda^2/9`. The upper annulus
therefore gives, for `lambda>0`,

\[
\frac{\lambda(1-\lambda)}3\le\frac{\lambda^2}{9}
\quad\Longrightarrow\quad \lambda\ge\frac34.
\]

A second cofactor has the roles reversed:

\[
P_{\tau_\alpha(i),j}P_{i,\tau_\beta(j)}=\frac{\lambda^2}{9},
\qquad
\text{available pairing mass}=\frac{\lambda(1-\lambda)}3,
\]

hence `lambda<=3/4`. This proves (4.2). Formula (4.3) is immediate from (4.1).

For `sigma!=tau`, the finite combinatorics are even sharper: one of the 24 zero-RHS external
cofactors keeps both determinant pairings identically zero along the whole edge, whereas its two
same-unitary `P` deficits are positive for every `lambda>0`. The verifier checks all
`48*23=1104` such forbidden open edges exactly with rational arithmetic. `QED`

## 5. Exact structured stress application

The previous B09 external-spinor stress datum used

`a=((4,2),(-2,3),(0,-2),(-3,-2))`,
`b=((-4,-4),(0,-2),(1,2),(-3,3))`, and support multiplier `(1,-1)` in Gaussian-pair notation.

Exact endpoint enumeration gives

\[
M=240.
\]

Among the 48 external functionals there is a unique outer maximizer

\[
e_*=740/3>240,
\]

with `tau=(2,3,0,1)` and `rho'=(1,2,0)`. Its associated Weyl endpoint is extremely low:

\[
f(\tau)=-1538.
\]

The theorem eliminates every edge from `e_*` to the other 23 Weyl endpoints completely. On the
only exceptional Weyl edge, cofactor compatibility permits only `lambda=0` or `lambda=3/4`; the
nontrivial point has exact support

\[
\frac34\frac{740}{3}+\frac14(-1538)=-\frac{399}{2}<240.
\]

Thus the dangerous external atom cannot produce a support violation by moving toward **any
single Weyl endpoint**. The remaining obstruction is necessarily a genuinely higher-dimensional
mixture involving coordinated motion in at least two outer directions (and, at a genuine
maximizer, simultaneously the lead's stationarity/Hessian/Lyapunov–Schmidt conditions).

This is strictly stronger than merely saying the external point itself is non-genuine.

## 6. Integration with the current lead residual

The lead's nonconstant support is written in the same exterior variables as

\[
s=\langle D,K\rangle+\frac12\langle R,X\rangle.
\]

In gauge `(i,j)` this is

\[
s=\left\langle R,\frac X2+C^{ij}\right\rangle
 -2\langle B^{ij},C^{ij}\rangle,
\qquad C^{ij}_{\alpha\beta}=s_i(\alpha)s_j(\beta)K_{\alpha\beta}.
\]

Therefore (3.1)–(3.3) can be inserted directly into both live lead branches:

- `MSQR`: together with the mixed-Schur Lyapunov–Schmidt reserve, they prevent replacing the
  complementary-minor layer by an arbitrary outer mass direction;
- `NDI`: together with the strict spinor reserve/payment bounds, they give a finite family of
  quadratic same-unitary constraints on every candidate strict support maximizer.

The new edge theorem also sharpens the B09 external-functional route: a counterexample cannot be
obtained from one external Saxl atom plus one Weyl atom. A remaining positive-gap candidate must
use a higher-dimensional external face and satisfy all 144 cofactor annuli at once.

### Next exact obligation

`MOC4-MULTI-EXTERNAL-COFACTOR-PAYMENT-v1`: combine the 144 cofactor annuli with the 72-point
Saxl outer decomposition and the lead's current mixed-Schur/negative-definite stationarity gates.
The immediate finite subproblem is to show that any support-positive combination involving one
or more external atoms must pay enough weight into low-support directions to erase the external
excess, or else construct a genuine true-unitary witness violating that claim. This is now a
higher-dimensional face problem; all external–Weyl edges are closed.

No claim of a full MOC4 proof or counterexample is made.

## 7. Exact verification

`verify_cofactor_edge_purge.py` uses only the Python standard library and exact `Fraction`
arithmetic. It verifies:

- all 48 external B09 coordinate points;
- exactly 24 zero-RHS cofactor violations at each external point;
- all 1152 external–Weyl edges;
- all 1104 edges with `sigma!=tau` are identically cofactor-incompatible in their open part;
- all 48 exceptional `tau` edges have the two exact polynomial constraints giving
  `lambda in {0,3/4}`;
- at `lambda=3/4`, the functional equals the Weyl-safe mean in (4.3);
- the structured stress values `M=240`, `e_*=740/3`, `f(tau)=-1538`, and safe-point value
  `-399/2`.

The captured exact output is in `VERIFICATION.txt`.
