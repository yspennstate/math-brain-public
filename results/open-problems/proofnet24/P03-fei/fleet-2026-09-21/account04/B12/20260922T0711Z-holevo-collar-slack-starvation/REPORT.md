# account04/B12 — optimized Holevo collar and child-slack starvation

**Run:** `B12-20260922T071142Z-r44`  
**Classification:** `ESSENTIAL_STEP_APPLIED / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Control:** owner revision `2026-09-22.2`; fixed all-gate Gamma target.  

## 0. Exact predecessor and target

The named other-account result consumed is

`proofnet24/P03-fei/fleet-2026-09-21/account02/B13/20260922T055830Z-holevo-low-delta-collar/REPORT.md`, blob `d31f54036cbc71c9ed9850b6da5c2b093f2f77e1`.

For the live fixed candidate

\[
C^\dagger=6.521851214,\qquad
\Gamma^\dagger=\Gamma_0+0.268204856\,u(1-u),
\]

that report proves, at a balanced-child physical pivot, with
\(u=\min(t,1-t)\), \(0<\delta\le1/4\),
\(\ell=\log_2(1/u)\), \(d=\log_2(1/\delta)\), and \(u\le2^{-10}\),

\[
\frac{\mathcal L_{\Gamma^\dagger,j}}{\delta u}
>
A\ell-Bd+C,                                             \tag{0.1}
\]

where

\[
A=\frac{576007}{638750},\qquad
B=\frac{4092}{511},\qquad
C=-\frac{198979}{25550}.                                \tag{0.2}
\]

It also proves the minimum-essential-arity/global-bias-minimizer secant relation

\[
\mathcal L_j\le-u\,|d_1-d_0|,                           \tag{0.3}
\]

where \(d_0,d_1\ge0\) are the two proper-restriction slacks.  These are the exact implications consumed here.  The predecessor chose the sufficient collar \(\ell\ge10+9d\); it explicitly noted that exponent 9 and offset 10 were conservative.

The current owner target is to prove the fixed all-gate inequality for all composition-prime gates, or find a source-valid counterexample.  This report strengthens the boundary exclusion and then extracts a new structural consequence from the child slack that the naive arity induction discarded.

## 1. A parameterized sharp-from-this-envelope collar

From (0.1), suppose

\[
\ell\ge K+p d.                                           \tag{1.1}
\]

Then

\[
A\ell-Bd+C\ge (pA-B)d+(KA+C).                           \tag{1.2}
\]

Hence, provided

\[
p>\frac BA=\frac{5115000}{576007}=8.880100415446339\ldots,
\qquad
K>\frac{-C}{A}=\frac{4974475}{576007}=8.636136366398325\ldots, \tag{1.3}
\]

and the resulting region stays inside \(u\le2^{-10}\), every balanced-child pivot in that region has strictly positive local gluing.

Because \(\delta\le1/4\) means \(d\ge2\), it is enough additionally that \(K+2p\ge10\).  Thus the predecessor's scalar envelope itself proves the following whole family:

\[
\boxed{
0<\delta\le\tfrac14,\quad
u\le2^{-K}\delta^p,\quad
p>B/A,\ K>-C/A,
\quad\Longrightarrow\quad
\mathcal L_{\Gamma^\dagger,j}>0,
}                                                        \tag{1.4}
\]

whenever \(K+2p\ge10\).

This identifies the limiting exponent and offset obtainable from the present analytic envelope without changing its entropy estimates.  No claim is made that these limits are sharp for the true local gluing problem.

## 2. Concrete stronger collar

Take

\[
p=\frac{8881}{1000}=8.881,
\qquad
K=\frac{87}{10}=8.7.                                    \tag{2.1}
\]

Exact arithmetic gives

\[
pA-B=\frac{518167}{638750000}>0,                       \tag{2.2}
\]

\[
KA+C=\frac{367859}{6387500}>0,                           \tag{2.3}
\]

and

\[
K+2p=\frac{13231}{500}=26.462>10.                       \tag{2.4}
\]

Therefore

\[
\boxed{
0<\delta\le\tfrac14,\qquad
u\le 2^{-87/10}\delta^{8881/1000}
\quad\Longrightarrow\quad
\mathcal L_{\Gamma^\dagger,j}>0.
}                                                        \tag{2.5}
\]

Equivalently, a negative balanced-child pivot of a minimum critical core must obey

\[
\boxed{
u> 2^{-87/10}\delta^{8881/1000}.}               \tag{2.6}
\]

This strictly dominates the predecessor's \(2^{-10}\delta^9\) collar on the whole interval \(0<\delta\le1/4\).  Indeed

\[
\frac{2^{-87/10}\delta^{8881/1000}}
     {2^{-10}\delta^9}
=2^{13/10}\delta^{-119/1000}
\ge 2^{769/500}
=2.903916559807788\ldots.                               \tag{2.7}
\]

Thus the forbidden rare-bias width is enlarged by at least a factor 2.90, and by a larger factor as \(\delta\downarrow0\).

## 3. New child-slack starvation theorem

The stronger point is not only the optimized collar.  Keep a balanced-child pivot in a minimum-essential-arity, global-bias-minimizing counterexample, and assume

\[
0<\delta\le\tfrac14,\qquad u\le2^{-10},\qquad
\mathcal L_j<0.                                          \tag{3.1}
\]

Define

\[
R:=Bd-A\ell-C.                                           \tag{3.2}
\]

By (0.1) and \(\mathcal L_j<0\), necessarily \(R>0\), and

\[
\mathcal L_j>-u\delta R.                                \tag{3.3}
\]

Relabel the two physical children so that the rare branch has probability \(u\) and the common branch probability \(1-u\).  Write their nonnegative proper-restriction slacks as \(d_{\rm rare}\) and \(d_{\rm common}\).  The exact one-coordinate cocycle is

\[
D_*=(1-u)d_{\rm common}+u d_{\rm rare}+\mathcal L_j<0.   \tag{3.4}
\]

Combining (3.3) and (3.4) gives the strict starvation bound

\[
\boxed{
(1-u)d_{\rm common}+u d_{\rm rare}<u\delta R.
}                                                        \tag{3.5}
\]

In particular,

\[
\boxed{d_{\rm rare}<\delta R,}                           \tag{3.6}
\]

\[
\boxed{
d_{\rm common}<\frac{u}{1-u}\,\delta R
\le\frac{1024}{1023}\,u\delta R.}                       \tag{3.7}
\]

Finally, combining the secant inequality (0.3) with (3.3) yields

\[
-u\delta R<\mathcal L_j\le-u|d_1-d_0|,
\]
so

\[
\boxed{|d_1-d_0|<\delta R.}                              \tag{3.8}
\]

Thus a negative balanced-child pivot cannot merely sit just outside the positive collar: its proper restrictions must simultaneously be almost tight.  In the boundary regime the common branch is forced to have an additional factor \(u\) of slack suppression.

This is precisely the child continuation credit that a blind arity induction loses.

## 4. Implication for the owner's decomposable-extremality target

The owner asks for a proof that a worst gate margin is attained at a decomposable gate, or a falsifying prime gate.  Sections 2--3 give a necessary boundary signature for any source-valid prime counterexample to the current fixed candidate:

* a balanced-child pivot cannot enter the enlarged collar (2.5);
* if it is still in the rare-bias regime \(u\le2^{-10}\), both child restriction slacks are quantitatively starved by (3.5)--(3.8), with the common child smaller by an explicit factor \(u/(1-u)\).

Therefore a hypothetical prime obstruction approaching a bias face must approach a chain of nearly tight proper restrictions rather than carrying an arbitrary positive child slack.  A remaining decisive route is to prove a **nondecomposable slack-gap theorem**: a composition-prime critical gate cannot have this simultaneous all-pivot starvation.  Such a gap would convert the present boundary rigidity into the desired decomposable extremality.  Unequal child output measures and intermediate-bias pivots remain unpaid.

No new comparable gate margin \(c_G\) is claimed here; the result is a structural necessary condition for violation of the fixed \(C^\dagger,\Gamma^\dagger\) candidate.  Full FEI remains **OPEN / NOT PROVED**.

## 5. Compatibility and retired shortcuts

The account04/B18 mixed-curvature identity remains untouched.  In particular this argument neither assumes nor implies \(\sum_k d_k=O(J)\).  It does not use fixed-relative near-subcube payment, affine rebasing, a sign-free spectral relaxation, an ambient-dimensional entropy continuity bound, or the refuted blind arity induction.

Mechanism change from the preceding B12 MUX tube: this run leaves the MUX-specific six-mass decomposition and works instead with the general balanced-child all-gate local cocycle, preserving the two child slacks and extracting a critical-core rigidity statement.

## 6. Exact check

`CHECKER.py` verifies all rational constants in (0.2), the two strict coefficients in (2.2)--(2.3), the source-region condition (2.4), the uniform domination exponent in (2.7), and rational-grid instances of the algebraic starvation implication.  The proof of Sections 1--3 is analytic; the finite checks are regression evidence only.
