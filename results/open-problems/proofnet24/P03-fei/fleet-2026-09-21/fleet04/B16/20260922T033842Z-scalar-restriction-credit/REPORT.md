# fleet04/B16 — scalarization of the exact restriction credits

**Run:** `B16-20260922T033842Z-r12`  
**Classification:** `NEW_SOURCE_VALID_REDUCTION / LOCAL_SHORTCUT_REFUTED`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full unrestricted FEI:** **OPEN / NOT PROVED**

## 0. Control and scope


I nevertheless re-read the two exact interface-C dependencies named in the inherited prompt and preserve them unchanged:

* `proofnet24/P03-fei/fleet-2026-09-21/fleet02/B16/20260921T184541Z-actual-current-parent-mask-incidence/REPORT.md`, creation commit `7f9fdcbbba89432301a5e32985ae2bd3e7b1ac5e`: the authentic post-current central parent coefficient is `epsilon_{q,k} b_R^2/r_R`, after same-syndrome signed aggregation, with original-coordinate one-subcube geometry retained.
* `proofnet24/P03-fei/fleet-2026-09-21/fleet03/B18/20260921T185340Z-signed-flag-curvature/REPORT.md`, creation commit `4843e50690013fd18b85dd8763b53bdc75da79e8`: the physical signed derivative sink is `kappa=p+4o`, and the opposite-orientation bank cannot be discarded.

Those results remain valid at their proved scopes. The live owner target, however, is now the all-gate potential. The exact input used here is fleet04/B17's restriction cocycle

`proofnet24/P03-fei/fleet-2026-09-21/fleet04/B17/20260922T031352Z-biased-restriction-margin-cocycle/REPORT.md`

(blob `d32321447c5f30282f243d9a2907ec719d483c92`). I also use the fresh live successor normalization reported by fleet01/B16:

\[
C_*=6.5218512,\qquad
\Gamma_*=\Gamma_{\rm RO}+0.2682048\,p(1-p),
\]

without assuming that it is universally valid.

The goal of this run is to reduce the remaining exact local restriction credit from a full pair of Boolean spectra to four physical scalars, while retaining both of B17's mandatory information credits.

## 1. Exact local cocycle recalled

Fix a Boolean gate and pivot coordinate \(j\). Put

\[
t=p_j,\quad q=1-t,\quad
r_b=\Pr[G_b=1],\quad
r=qr_0+tr_1,
\]

and

\[
\delta=\Pr[G_0\ne G_1],\qquad V=4tq,\qquad m=V\delta.
\]

Let \(a_S,b_S\) be the biased Walsh coefficients of the two restrictions and

\[
P_0(S)=a_S^2,\qquad P_1(S)=b_S^2,\qquad
T_S=qP_0(S)+tP_1(S).
\]

B17 proves the exact identity

\[
D_\Gamma(G)
=qD_\Gamma(G_0)+tD_\Gamma(G_1)
+\mathcal R_{\Gamma,j}+\mathcal C_j,
\]

where

\[
\mathcal R_{\Gamma,j}
=q\Gamma(r_0)+t\Gamma(r_1)-\Gamma(r)
+\delta\{\Gamma(t)+h_2(V)\}
-h_2(t)-h_2(m)
\]

and

\[
\mathcal C_j=H(B\mid S)+I(S;J)\ge0.
\]

Here \(B\) is the restriction branch and \(J\) is the vertical Fourier-layer bit. Throwing away either information credit is already known to be invalid.

## 2. PROVED — two scalar lower bounds for the branch credit

The overlap of the two signed coefficient vectors is physical:

\[
\sum_S a_S b_S
=\mathbb E[f_0f_1]
=1-2\delta.
\]

Write

\[
F=\sum_S\sqrt{P_0(S)P_1(S)}
=\sum_S|a_Sb_S|
\ge |1-2\delta|.
\]

### Lemma 2.1 — posterior-quadratic bound

For every binary posterior \(u\),

\[
h_2(u)\ge4u(1-u).
\]

One self-contained proof writes \(x=1-2u\). Then

\[
\frac{(1+x)\ln(1+x)+(1-x)\ln(1-x)}2
=\sum_{k\ge1}\frac{x^{2k}}{(2k)(2k-1)}
\le x^2\sum_{k\ge1}\frac1{(2k)(2k-1)}
=x^2\ln2,
\]

which is exactly the stated inequality.

At spectral atom \(S\), the posterior branch probability is
\(tP_1(S)/T_S\). Hence

\[
H(B\mid S)
\ge4tq\sum_S\frac{P_0(S)P_1(S)}{T_S}.
\]

Cauchy gives

\[
F^2\le
\left(\sum_S\frac{P_0P_1}{T_S}\right)
\left(\sum_ST_S\right)
=
\sum_S\frac{P_0P_1}{T_S}.
\]

Therefore

\[
\boxed{
H(B\mid S)\ge
V(1-2\delta)^2.
}
\tag{2.1}
\]

### Lemma 2.2 — common-part/total-variation bound

Let

\[
v=\operatorname{TV}(P_0,P_1).
\]

Decompose each spectral law into its maximal common part:

\[
P_b=(1-v)R+vR_b.
\]

Equivalently, introduce a Bernoulli variable \(E\), independent of \(B\), with
\(\Pr[E=1]=v\); when \(E=0\), draw from the common law \(R\), and when \(E=1\), draw from the branch-specific residual. Data processing gives

\[
I(B;S)\le I(B;E,S)\le v\,h_2(t).
\]

Also,

\[
v
=\frac12\sum_S|\sqrt{P_0}-\sqrt{P_1}|(\sqrt{P_0}+\sqrt{P_1})
\le\sqrt{1-F^2}
\le2\sqrt{\delta(1-\delta)}.
\]

Since \(H(B\mid S)=h_2(t)-I(B;S)\),

\[
\boxed{
H(B\mid S)\ge
h_2(t)\bigl(1-2\sqrt{\delta(1-\delta)}\bigr).
}
\tag{2.2}
\]

This second bound is exact at \(\delta=0\) and \(\delta=1\), where the two squared spectral laws coincide. The first bound is often stronger in the interior. Thus define

\[
\boxed{
B_*(t,\delta)=
\max\left\{
V(1-2\delta)^2,\;
h_2(t)\bigl(1-2\sqrt{\delta(1-\delta)}\bigr)
\right\}.
}
\tag{2.3}
\]

Then \(H(B\mid S)\ge B_*(t,\delta)\).

## 3. PROVED — scalar lower bound for the vertical information credit

Put

\[
\mu_b=1-2r_b
\]

and define

\[
T_0=q\mu_0^2+t\mu_1^2,\qquad
u=V(r_1-r_0)^2.
\]

The atom \(S=\varnothing\) has total mass exactly \(T_0\), while the joint mass

\[
\Pr[S=\varnothing,J=1]
=tq(\mu_1-\mu_0)^2
=u.
\]

The total \(J=1\) mass is \(m=V\delta\). Coarsen \(S\) to the single bit

\[
Z=1_{\{S=\varnothing\}}.
\]

By data processing,

\[
I(S;J)\ge I(Z;J).
\]

The latter is completely scalar:

\[
\boxed{
I_0(t,r_0,r_1,\delta)
=
h_2(m)
-T_0h_2\!\left(\frac u{T_0}\right)
-(1-T_0)h_2\!\left(\frac{m-u}{1-T_0}\right),
}
\tag{3.1}
\]

with the usual continuous convention when \(T_0\in\{0,1\}\). Hence

\[
\boxed{
I(S;J)\ge I_0.
}
\tag{3.2}
\]

No arbitrary probability law has been inserted: \(T_0,u,m\) are exact masses of the authentic biased Walsh split.

## 4. Main theorem — four-scalar source-valid credit reduction

Combining (2.3) and (3.2),

\[
\boxed{
\mathcal C_j
\ge
B_*(t,\delta)+I_0(t,r_0,r_1,\delta).
}
\tag{4.1}
\]

Consequently define

\[
\begin{aligned}
\mathcal S_\Gamma(t,r_0,r_1,\delta)
={}&q\Gamma(r_0)+t\Gamma(r_1)-\Gamma(qr_0+tr_1)\\
&+\delta\{\Gamma(t)+h_2(V)\}
-h_2(t)-h_2(V\delta)\\
&+B_*(t,\delta)+I_0(t,r_0,r_1,\delta).
\end{aligned}
\tag{4.2}
\]

Then for every actual Boolean restriction pair,

\[
\boxed{
\mathcal R_{\Gamma,j}+\mathcal C_j
\ge
\mathcal S_\Gamma(t,r_0,r_1,\delta).
}
\tag{4.3}
\]

The only Boolean pair data left are the four scalars

\[
0<t<1,\quad 0\le r_0,r_1\le1,\quad
|r_1-r_0|\le\delta\le
\min\{r_0+r_1,\,2-r_0-r_1\}.
\tag{4.4}
\]

Thus a **sufficient** route to the live all-gate statement is now a four-real-variable scalar certification:

> prove \(\mathcal S_{\Gamma_*}\ge0\) throughout (4.4).

If this scalar inequality holds, B17's exact restriction-tree cocycle immediately gives \(D_{\Gamma_*}(G;p)\ge0\) for every Boolean gate and every product bias, hence the all-gate FEI implication for the current candidate. If the scalar inequality fails somewhere, that does **not** refute \(\Gamma_*\): (4.1) is a lower bound and may be non-sharp. It does, however, identify precisely where additional signed/Boolean information must be retained.

This is the run's main useful reduction.

## 5. Exact limitation — support-deficit currency alone is not a pointwise local proof

A tempting simplification is to replace the shaped read-once potential by a pure quadratic potential

\[
\Gamma_C(p)=C\,V_p=4C\,p(1-p)
\]

and try to prove every local gluing node from only its Poincare currency. That pointwise local shortcut fails already for a three-input Boolean gate, even at \(C=8\).

Let the remaining inputs be \(x,y\), the pivot be \(z\), and set

\[
\Pr[x=1]=\frac78,\qquad
\Pr[y=1]=\frac18,\qquad
\Pr[z=1]=\frac38.
\]

Take

\[
G_0(x,y)=\neg x\lor y,\qquad
G_1(x,y)=1_{\{x=y\}}.
\]

In truth-table integer notation on \((x,y)\), these are `13` and `9`; the three-bit gate is `157`. Exactly,

\[
r_0=\frac{15}{64},\qquad
r_1=\frac7{32},\qquad
\delta=\frac1{64}.
\]

The branch squared spectra are

\[
P_0=\frac1{1024}(289,343,343,49),
\]

\[
P_1=\frac1{256}(81,63,63,49),
\]

and the parent squared spectrum is

\[
\frac1{65536}
(19321,19663,19663,5929,15,105,105,735).
\]

The exact local Poincare denominator in the \(C\,V\) normalization is

\[
V\{\delta-(r_1-r_0)^2\}
=\frac{945}{65536}.
\]

Writing \(L\) for the exact parent entropy increase
\(H(G)-\frac58H(G_0)-\frac38H(G_1)\), the local node requires

\[
C\ge
\frac{L-\delta h_2(15/16)}{945/65536}
=
8.31683046964934\ldots.
\tag{5.1}
\]

In particular \(C=8\) fails locally. The sign \(>8\) is certified without floating-point logarithms. After multiplying the desired inequality by \(65536\), it becomes

\[
430712+\sum_n c_n\log_2 n>0,
\]

and exponentiating reduces it to one exact comparison of two positive integers; the checker performs that comparison directly. The positive side has bit length `919024`, the negative side `918725`.

This is **not** a global counterexample to the gate inequality for \(\Gamma_8\): child continuation defects can compensate a negative local node. It only kills the stronger shortcut that every physical restriction node can be paid pointwise by a universal pure support-deficit/Poincare term. The exact B17 continuation credits must remain live.

## 6. Verification

`check_b16_scalar_credit_quadratic_obstruction.py` is standard-library only. It:

* reconstructs exact squared biased-Walsh masses as `Fraction`s;
* checks the scalar-credit bound on 7,680 small Boolean restriction-pair/bias cases;
* reconstructs the exact three-input counterexample spectra and all physical scalars;
* certifies the strict \(C>8\) local obstruction by an exact integer comparison, not a floating sign.

Clean execution:

```
PASS
scalar_credit_cases 7680
worst_scalar_credit_gap -2.2204460492503131e-16
counterexample_r0_r1_delta 15/64 7/32 1/64
counterexample_currency 945/65536
required_pure_quadratic_C 8.316830469649341
exact_integer_sign_bits 919024 918725
```

The tiny negative displayed finite-test gap is ordinary double rounding in a case of analytic equality; the theorem is analytic and the decisive counterexample sign is exact-integer certified.

Checker SHA-256:

`495c8fea3a0da572393a983a59fae0ecf68239d94cced4a61617bd93e25cb797`.

## 7. Next exact target

The current proof gap is now narrower in a way that is directly compatible with the live owner programme:

1. interval-certify the scalar sufficient inequality (4.2) for the actual immutable \(\Gamma_*\) on the Frechet domain (4.4), starting with the compact interior left after the fresh boundary-repulsion theorems; or
2. if (4.2) fails, inspect the failing scalar cell and retain one additional source-exact statistic rather than discarding the KL/vertical credits.

The old interface-C orientation, terminal, negative-credit, dual-code and parent-mask results are preserved; they are not silently reused in this newer gate proof.

No benchmark gold, mocks, paid/remote compute, workflow dispatch, email/Drive action, notification enabling, or unrelated private data was used.
