# account01/B17 — transverse unequal-data tube around the complementary MUX line

**Classification:** `ESSENTIAL_STEP_APPLIED / COMPLEMENTARY_TRANSVERSE_MUX_TUBE / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. Authenticated repository controls and source-bound mathematical artifacts were read directly; no native/authenticated mathematical-brain receiver context entered the derivation.  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED**.

## 0. Live candidate and exact source inputs

The live all-gate candidate is the campaign candidate
\[
C^\dagger=6.521851214,\qquad C_0=6.4548,\qquad a^\dagger=4(C^\dagger-C_0)=0.268204856,
\]
\[
\Gamma^\dagger(z)=\Gamma_0(z)+a^\dagger z(1-z).
\]
The end-to-end conditional chain is unchanged: if
\[
D_{\Gamma^\dagger}(G;p)\ge0
\]
for every finite Boolean gate and every product-bias vector, then the exact gate reformulation/composition cocycle gives uniform-cube FEI with constant \(C^\dagger\). The first unpaid explicit prime family is still the one-selector MUX; proving a tube does **not** settle the universal gate statement.

This run substantively consumes the following exact named peer results.

1. **account02/B12**, `20260922T045519Z-complementary-mux-fourstep/REPORT.md`: for the balanced-address complementary-data MUX
\[
M(a,x_0,x_1),\qquad t=1/2,\quad q_0=q,\quad q_1=1-q,
\]
with \(0<q\le1/2\), its exact slack
\[
F(q):=D_{\Gamma^\dagger}(M;1/2,q,1-q)
\]
satisfies
\[
F(q)>\frac{29}{10}q\quad(0<q\le2^{-11}),
\tag{0.1}
\]
and
\[
F(q)>\frac1{64}\quad(2^{-11}\le q\le1/2).
\tag{0.2}
\]

2. **account01/B15**, `20260922T050419Z-mux-negative-posterior-credit/REPORT.md`: on the balanced-address plane, with
\[
u=1-q_0-q_1,\qquad v=q_1-q_0,
\]
the exact Boolean slack is
\[
D_{\Gamma}(M;1/2,q_0,q_1)=R_C(u,v)-J_\Gamma(u,v),
\tag{0.3}
\]
where
\[
R_C=S(1-u^2)+Bv^2-E(u,v),\qquad S=C/2-2,\quad B=C/2+2,
\tag{0.4}
\]
\[
E(u,v)=\phi(u^2)+\phi(v^2)-\tfrac12\phi((u+v)^2)-\tfrac12\phi((u-v)^2),
\tag{0.5}
\]
\[
J_\Gamma(u,v)=\Gamma\!\left(\frac{1-u}{2}\right)-\frac12\Gamma\!\left(\frac{1-u-v}{2}\right)-\frac12\Gamma\!\left(\frac{1-u+v}{2}\right).
\tag{0.6}
\]
It also proves the signed-entropy estimate
\[
E(u,v)\le2|uv|+\frac{4u^2v^2}{u^2+v^2}.
\tag{0.7}
\]
The negative posterior term is already present in (0.3)-(0.7); it is not discarded or charged twice.

3. **account01/B18**, `20260922T055608Z-balanced-mux-collar-sharpen/REPORT.md`: on the source representation \(\Gamma_0(p)=pG(\log_2(1/p))\), the h96 source has the valid global transformed-slope estimate \(|G'|<31\). The same report proves, for same-side points \(p(1\pm\rho)\),
\[
\Gamma^\dagger(p)-\frac{\Gamma^\dagger(p(1-\rho))+\Gamma^\dagger(p(1+\rho))}{2}
\le \frac{31p}{\ln2}\rho+a^\dagger p^2\rho^2.
\tag{0.8}
\]
The current source also supplies the center bound
\[
|\Gamma^\dagger(1/2+x)-C^\dagger|\le60|x|\qquad(|x|\le2^{-14}).
\tag{0.9}
\]

I also read the required half-band positive-current correction, `handoffs/2026-09-21__sharp-kernel-halfband-obstruction-204926Z.md`. Its correction says the standalone positive-current \(O(J)\) claim is false unless compensating signed terms are retained. No positive-current estimate is used below, so this proof is unaffected and does not silently revive the refuted implication.

## 1. Geometry of a transverse perturbation

Fix the complementary base point
\[
q_0=q,\qquad q_1=1-q,\qquad 0<q\le1/2,
\]
so in \((u,v)\) coordinates
\[
u=0,\qquad v=1-2q\ge0.
\]
Now move **transversely** to the complementary line while keeping the data difference \(v\) fixed:
\[
q_0=q-\frac u2,\qquad q_1=1-q-\frac u2.
\tag{1.1}
\]
The output bias remains balanced-address average \((q_0+q_1)/2=(1-u)/2\). By the symmetries of (0.4)-(0.6), the slack is even in \(u\), so take \(u\ge0\).

Assume additionally
\[
u\le v
\tag{1.2}
\]
so that \(q+u/2\le1/2\). Then symmetry of \(\Gamma\) turns (0.6) into
\[
J_\Gamma(u,v)=\Gamma\!\left(\frac{1-u}{2}\right)
-\frac12\Gamma(q-u/2)-\frac12\Gamma(q+u/2).
\tag{1.3}
\]
At \(u=0\),
\[
J_\Gamma(0,v)=C-\Gamma(q).
\tag{1.4}
\]

## 2. Exact reserve loss

At the complementary point \(E(0,v)=0\). From (0.4) and (0.7), using \(v\le1\),
\[
\begin{aligned}
R_C(u,v)-R_C(0,v)
&=-Su^2-E(u,v)\\
&\ge-2u-(S+4)u^2.
\end{aligned}
\tag{2.1}
\]
For the live center
\[
S=1.260925607,
\]
so
\[
\boxed{R_{C^\dagger}(u,v)-R_{C^\dagger}(0,v)
\ge-2u-5.260925607u^2.}
\tag{2.2}
\]

## 3. Exact potential-loss bound

Let
\[
\rho=\frac{u}{2q}.
\]
When \(u\le2q\), the two data points in (1.3) are \(q(1\pm\rho)\). Applying (0.8),
\[
\Gamma^\dagger(q)-\frac{\Gamma^\dagger(q-u/2)+\Gamma^\dagger(q+u/2)}2
\le \frac{31}{2\ln2}u+\frac{a^\dagger}{4}u^2.
\tag{3.1}
\]
If also \(u\le2^{-13}\), then the center displacement in (1.3) is \(u/2\le2^{-14}\), so (0.9) gives
\[
\Gamma^\dagger((1-u)/2)-C^\dagger\le30u.
\tag{3.2}
\]
Therefore
\[
J_{\Gamma^\dagger}(u,v)-J_{\Gamma^\dagger}(0,v)
\le \left(30+\frac{31}{2\ln2}\right)u+rac{a^\dagger}{4}u^2.
\tag{3.3}
\]
Using the elementary source-valid inequality \(1/\ln2<3/2\),
\[
\boxed{J_{\Gamma^\dagger}(u,v)-J_{\Gamma^\dagger}(0,v)
<53.25u+0.067052u^2.}
\tag{3.4}
\]

Combining (2.2), (3.4), and \(D=R-J\),
\[
\boxed{
D_{\Gamma^\dagger}(u,v)
>F(q)-55.25u-5.327978u^2.
}
\tag{3.5}
\]
In all ranges below \(u<10^{-3}\), hence the transparent weakening
\[
\boxed{D_{\Gamma^\dagger}(u,v)>F(q)-56u}
\tag{3.6}
\]
is valid.

## 4. New theorem: a transverse unequal-data tube

### Theorem 4.1
For the live candidate \(\Gamma^\dagger\), let \(0<q<1/2\), \(v=1-2q\), and define the balanced-address MUX by (1.1).

**Small-data branch.** If
\[
0<q\le2^{-11},\qquad |u|\le\frac q{32},
\tag{4.1}
\]
then
\[
\boxed{D_{\Gamma^\dagger}(M;1/2,q-u/2,1-q-u/2)>\frac{23}{20}q>0.}
\tag{4.2}
\]
Indeed \(q/32\le2^{-16}<2^{-13}\), condition (1.2) is automatic, and from (0.1),(3.6),
\[
D>\frac{29}{10}q-56\frac q{32}=\frac{23}{20}q.
\]

**Compact branch.** If
\[
2^{-11}\le q<1/2,
\qquad |u|\le\min\{2^{-13},1-2q\},
\tag{4.3}
\]
then
\[
\boxed{D_{\Gamma^\dagger}(M;1/2,q-u/2,1-q-u/2)>\frac9{1024}>0.}
\tag{4.4}
\]
Indeed (0.2),(3.6) give
\[
D>\frac1{64}-56\,2^{-13}=\frac9{1024}.
\]
At \(q=1/2\) the transverse direction is simply the equal-data line and is already covered by the exact common-data addressing theorem, so excluding that endpoint in (4.3) loses no logical case.

This theorem is a genuine unequal-data statement: for \(u\ne0\), the two data biases no longer sum to one. It thickens the exact complementary-data line in the **orthogonal data-sum direction**, whereas account04/B12's newest theorem thickens that same line in the **address-bias direction**.

## 5. Exact old/new missing implication

**Old missing implication.** The live MUX obligation still required controlling the full three-parameter cube \((t,q_0,q_1)\). Existing exact pieces included the common-data family, the complementary-data balanced-address line, a thin equal-data collar in the balanced plane, and an address-bias tube over the complementary line.

**New implication.** The complementary line now has a second, transverse source-valid tube inside the balanced-address plane, with explicit reserves (4.2) and (4.4). In particular, no counterexample to \(\Gamma^\dagger\) can approach the complementary line through this transverse sector faster than the stated widths.

**Still missing.** The interior balanced-MUX region outside the equal-data and complementary-data tubes remains open, as does simultaneous two-direction thickening and arbitrary composition-prime gates. Therefore this is `ESSENTIAL_STEP_APPLIED`, not `FULL_PROOF_CANDIDATE`.

## 6. Stress checks

The proof uses only exact Boolean MUX identities and source-certified inequalities. Independent arithmetic checks of the displayed constants give
\[
55.25=2+30+93/4,
\qquad
5.327977\ldots=5.260925607+0.268204856/4,
\]
\[
\frac{29}{10}-\frac{56}{32}=\frac{23}{20},
\qquad
\frac1{64}-\frac{56}{2^{13}}=\frac9{1024}.
\]
A direct numerical stress scan of the source-independent entropy inequality (0.7) over the feasible MUX diamond found no violation; that scan is diagnostic only and is not used as a proof.

No scheduler, workflow, email, Drive, public-posting, permission, paid-compute, or other-account state was modified.