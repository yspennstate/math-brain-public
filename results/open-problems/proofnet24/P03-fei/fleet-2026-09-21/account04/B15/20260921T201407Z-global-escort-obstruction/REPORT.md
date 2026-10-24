# B15 — global escort interpolation and the one-point-defect critical-scale obstruction

**Status:** **OPEN / PARTIAL. Full uniform-cube FEI remains OPEN / NOT PROVED.**  
**Execution:** **WITHOUT_VERIFIED_BRAIN.** No authenticated brain retrieval or receiver-context use entered this mathematics.  
**Role:** FEI spectral remainder proof / joint interface D (unequal Fourier magnitudes and arithmetic remainder).  
**Run:** `20260921T201407Z-b15-d683ad04`.  
**Claim level:** two analytic identities/theorems about the current packet bridge, plus a rigorous obstruction to a whole scalar global-tilt proof architecture. No publication-priority claim.

## 0. What changed

The named other-account input consumed in this run is account01/B15's report

`proofnet24/P03-fei/fleet-2026-09-21/account01/B15/20260921T193429Z-numaro-bellman-depth-credit/REPORT.md`

at blob `6163a527da34629dd19180510bc2fc9a6e6bed74`.

Its section 11 exhibits a genuine four-bit Boolean function for which the contribution of the valuation-depth-two packet to the product-law relative entropy is negative:

\[
K_{r=2}=\frac3{16}\log_2\frac{64}{225}<0.
\]

Therefore the globally nonnegative product-shadow KL credit cannot be sliced by valuation depth and spent packetwise. That report leaves the precise next arithmetic task: keep one globally normalized KL divergence, tilt the reference law using the arithmetic/valuation data, and ask whether the resulting partition term is \(O(I)\).

This run solves that sub-question for the natural and in fact complete **scalar geometric interpolation** between the arithmetic packet law and the product-shadow packet law.

There is an exact one-parameter bridge for every \(0\le\theta\le1\). However, the one-point-defect Boolean family proves:

> **Every fixed positive arithmetic mixing weight \(\theta>0\) produces a partition term whose ratio to total influence diverges.**

More sharply, if the weight is allowed to depend on dimension, keeping that partition term \(O(I)\) on the one-point defect requires the critical scale

\[
\theta_n=O(1/n).
\]

When \(n\theta_n\to c\), the partition/influence ratio has the exact asymptotic limit

\[
\frac{\log_2 Z_{\theta_n}}{I(f_n)}
\longrightarrow
\frac{4^c-1}{\ln 2}.
\]

Thus a scalar global tilt can avoid the partition obstruction only by asymptotically turning off its arithmetic weight. This does **not** refute a proof that keeps the global escort KL and partition coupled, and it does not refute more general non-scalar transports. It does rigorously rule out the proposed architecture "choose a fixed positive global arithmetic tilt, then pay its partition term separately by influence."

## 1. Inherited packet notation

Let \(f:\{0,1\}^n\to\{-1,+1\}\), and let the squared Fourier law be

\[
\mu(S)=\widehat f(S)^2.
\]

For each distinct nonzero Fourier magnitude \(a\), let

\[
A_a=\{S:|\widehat f(S)|=a\},
\qquad
p_a=\mu(A_a)=|A_a|a^2.
\]

Use the inherited arithmetic quantities

\[
r_a,\qquad b_a=a2^{r_a},\qquad
N_a=|A_a|4^{-r_a}=\frac{p_a}{b_a^2},
\]

\[
R=\sum_a p_a r_a,
\qquad
D=\sum_a p_a\log_2\frac1{b_a}.
\]

Then

\[
H(f)=2R+2D.
\]

Let

\[
j_i=\Pr_\mu[i\in S]=\operatorname{Inf}_i(f),
\]

and let \(\nu\) be the independent Bernoulli law with these same coordinate marginals. Define

\[
\beta_a=\nu(A_a),
\qquad
\beta_\perp=\nu(2^{[n]}\setminus \operatorname{supp}\mu).
\]

Thus \((\beta_a,\beta_\perp)\) is a probability vector. Every packet with \(p_a>0\) has \(\beta_a>0\).

Write

\[
N=\sum_aN_a,\qquad
q^N_a=\frac{N_a}{N},
\]

and define the two packet-label divergences

\[
K_N=D_{\rm KL,2}(p\|q^N),
\]

\[
K_\beta
=
D_{\rm KL,2}\bigl((p_a,0)\|(\beta_a,\beta_\perp)\bigr)
=
\sum_ap_a\log_2\frac{p_a}{\beta_a}.
\]

Finally let

\[
C_{\rm in}
=
\sum_ap_a
D_{\rm KL,2}\bigl(\operatorname{Unif}(A_a)\|
\nu(\cdot\mid A_a)\bigr).
\]

The two inherited exact representations are

\[
\boxed{2D=\log_2N-K_N}
\tag{1.1}
\]

and

\[
\boxed{
2D=\sum_i h_2(j_i)-2R-K_\beta-C_{\rm in}.
}
\tag{1.2}
\]

The second follows from the maximum-entropy product-law identity and the KL chain rule.

## 2. PROVED: the complete scalar global-escort interpolation

For \(0\le\theta\le1\), define

\[
\boxed{
Z_\theta
=
\sum_aN_a^\theta\beta_a^{\,1-\theta}
}
\tag{2.1}
\]

and the normalized packet law

\[
\boxed{
m_{\theta,a}
=
\frac{N_a^\theta\beta_a^{\,1-\theta}}{Z_\theta}.
}
\tag{2.2}
\]

### Theorem B15-ESCORT-01

For every Boolean \(f\) and every \(0\le\theta\le1\),

\[
\boxed{
2D
=
(1-\theta)
\left[
\sum_i h_2(j_i)-2R-C_{\rm in}
\right]
+
\log_2 Z_\theta
-
D_{\rm KL,2}(p\|m_\theta).
}
\tag{2.3}
\]

At \(\theta=1\), this is the arithmetic free-energy identity (1.1). At \(\theta=0\), it is the product-shadow packet identity. At \(\theta=1/2\), it is exactly the geometric packet/product bridge from account02/B15.

### Proof

Take the convex combination of (1.1) and (1.2):

\[
2D
=
\theta(\log_2N-K_N)
+
(1-\theta)
\left[
\sum_i h_2(j_i)-2R-K_\beta-C_{\rm in}
\right].
\tag{2.4}
\]

The weighted packet divergences collapse to one genuine KL divergence. Direct expansion gives

\[
\theta K_N+(1-\theta)K_\beta
=
D_{\rm KL,2}(p\|m_\theta)
+\theta\log_2N-\log_2Z_\theta.
\tag{2.5}
\]

Indeed,

\[
\begin{aligned}
D_{\rm KL,2}(p\|m_\theta)
&=
\sum_ap_a\log_2p_a
-\theta\sum_ap_a\log_2N_a\\
&\quad
-(1-\theta)\sum_ap_a\log_2\beta_a
+\log_2Z_\theta,
\end{aligned}
\]

whereas

\[
\theta K_N+(1-\theta)K_\beta
=
\sum_ap_a\log_2p_a
-\theta\sum_ap_a\log_2N_a
-(1-\theta)\sum_ap_a\log_2\beta_a
+\theta\log_2N.
\]

Substitute (2.5) into (2.4); the \(\theta\log_2N\) terms cancel and (2.3) follows. \(\square\)

### Why this is the relevant global tilt

The family \(m_\theta\) is not an arbitrary guess. It is the normalized geometric interpolation obtained by taking a scalar convex combination of the **two exact KL credits already present** in the arithmetic and product-shadow representations. Thus it is the natural full one-parameter class for the proposed "one globally normalized tilt, one genuine KL" maneuver.

The theorem also makes clear what cannot be done: replacing the last KL by zero gives an upper expression, but that upper expression still contains the partition term \(\log_2Z_\theta\). The next theorem shows that this partition cannot be separately influence-paid for any fixed positive arithmetic weight.

## 3. One-point defect data

For \(n\ge3\), let

\[
f_n(x)=1-2\mathbf 1_{\{x=0\}}.
\]

Its unnormalized Walsh spectrum is

\[
W(\varnothing)=2^n-2,\qquad
W(S)=-2\quad(S\ne\varnothing).
\]

The inherited packet arithmetic has two packets with

\[
N_0=1,\qquad N_1=2^n-1,\qquad r_0=r_1=0.
\tag{3.1}
\]

Each spectral coordinate marginal is

\[
j=2^{1-n},
\]

so the total influence is

\[
\boxed{
I_n=I(f_n)=n2^{1-n}.
}
\tag{3.2}
\]

Under the product law,

\[
\beta_0=(1-j)^n,
\qquad
\beta_1=1-(1-j)^n.
\tag{3.3}
\]

Since \(I_n=nj\to0\),

\[
\boxed{
\beta_1\sim I_n,\qquad \beta_0=1-I_n+o(I_n).
}
\tag{3.4}
\]

For this family, (2.1) becomes the exact closed form

\[
\boxed{
Z_{\theta,n}
=
\beta_0^{\,1-\theta}
+
(2^n-1)^\theta\beta_1^{\,1-\theta}.
}
\tag{3.5}
\]

## 4. PROVED: every fixed positive scalar arithmetic tilt has an unpaid partition blow-up

### Theorem B15-ESCORT-02

For every fixed \(\theta\in(0,1]\),

\[
\boxed{
\frac{\log_2Z_{\theta,n}}{I(f_n)}
\longrightarrow+\infty.
}
\tag{4.1}
\]

Consequently, even if one keeps the within-packet KL credit \(C_{\rm in}\) and the valuation reserve \(R\) exactly, but discards only the global escort divergence \(D_{\rm KL}(p\|m_\theta)\), there is no dimension-independent constant \(C_\theta\) paying the resulting upper expression by influence.

### Proof

Let

\[
t_{\theta,n}
=
(2^n-1)^\theta\beta_1^{\,1-\theta}.
\]

Using (3.4),

\[
\frac{t_{\theta,n}}{I_n}
=
\left(\frac{2^n-1}{I_n}\right)^\theta
\left(\frac{\beta_1}{I_n}\right)^{1-\theta}.
\tag{4.2}
\]

Now

\[
\frac{2^n-1}{I_n}
\sim
\frac{2^{2n-1}}{n},
\]

while \(\beta_1/I_n\to1\). Therefore for every fixed \(\theta>0\),

\[
\boxed{
\frac{t_{\theta,n}}{I_n}\to\infty.
}
\tag{4.3}
\]

On the other hand,

\[
\beta_0^{\,1-\theta}
=
1-(1-\theta)I_n+o(I_n).
\tag{4.4}
\]

Hence

\[
Z_{\theta,n}
=
1+t_{\theta,n}-(1-\theta)I_n+o(I_n).
\tag{4.5}
\]

If \(t_{\theta,n}\to0\), then (4.3) and (4.5) give
\(\log_2Z_{\theta,n}\sim t_{\theta,n}/\ln2\), so (4.1) follows.
If \(t_{\theta,n}\) does not tend to zero, then \(Z_{\theta,n}\) stays a positive distance above one or diverges along a tail, while \(I_n\to0\), and again (4.1) follows.

For the second statement, after dropping only the global escort KL from (2.3), the remaining expression is

\[
U_{\theta}(f)
=
(1-\theta)
\left[
\sum_i h_2(j_i)-2R-C_{\rm in}
\right]
+\log_2Z_\theta.
\tag{4.6}
\]

For the one-point defect \(R=0\). Also the KL chain rule gives

\[
\sum_i h_2(j_i)-C_{\rm in}
=
H(f)+K_\beta\ge0.
\]

Thus

\[
U_\theta(f_n)\ge\log_2Z_{\theta,n},
\]

and (4.1) implies \(U_\theta(f_n)/I(f_n)\to\infty\). \(\square\)

### Concrete regimes

The exact formula also shows the character of the blow-up:

- \(0<\theta<1/2\): \(\log Z_{\theta,n}\to0\) absolutely, but it decays exponentially more slowly than \(I_n\), so its **influence-normalized** cost still diverges.
- \(\theta=1/2\): \(Z_{\theta,n}\sim\sqrt{2n}\), recovering the preceding geometric-bridge obstruction \(\log_2Z\sim\frac12\log_2(2n)\).
- \(1/2<\theta<1\): the partition grows exponentially.
- \(\theta=1\): \(Z_{1,n}=N=2^n\), hence \(\log_2Z_{1,n}=n\).

Thus moving the scalar mixing parameter away from \(1/2\) does not remove the structural need for the global KL credit.

## 5. PROVED: the critical adaptive scale is \(1/n\)

The fixed-\(\theta\) theorem leaves a possible loophole: choose \(\theta\) adaptively with dimension. The one-point defect determines the exact scale at which that can avoid the partition blow-up.

### Theorem B15-ESCORT-03

Let \(\theta_n\in[0,1]\).

1. If
   \[
   n\theta_n\to c\in[0,\infty),
   \]
   then
   \[
   \boxed{
   \frac{\log_2Z_{\theta_n,n}}{I_n}
   \longrightarrow
   \frac{4^c-1}{\ln2}.
   }
   \tag{5.1}
   \]

2. If
   \[
   n\theta_n\to+\infty,
   \]
   then
   \[
   \boxed{
   \frac{\log_2Z_{\theta_n,n}}{I_n}
   \to+\infty.
   }
   \tag{5.2}
   \]

In particular, a necessary condition for \(\log_2Z_{\theta_n,n}=O(I_n)\) on this Boolean family is

\[
\boxed{\theta_n=O(1/n).}
\tag{5.3}
\]

### Proof of part 1

When \(n\theta_n\to c<\infty\), necessarily \(\theta_n\to0\). By (3.4),

\[
\frac{\beta_1}{I_n}\to1,
\]

and

\[
\frac1n\log\frac1{\beta_1}\to\ln2.
\]

Also

\[
\frac1n\log(2^n-1)\to\ln2.
\]

Therefore

\[
(2^n-1)^{\theta_n}\to 2^c,
\]

and

\[
\beta_1^{-\theta_n}\to2^c.
\]

Hence the second summand in (3.5) obeys

\[
(2^n-1)^{\theta_n}\beta_1^{1-\theta_n}
=
\beta_1
(2^n-1)^{\theta_n}\beta_1^{-\theta_n}
=
4^c I_n+o(I_n).
\tag{5.4}
\]

For the first summand,

\[
\beta_0^{1-\theta_n}
=
(1-\beta_1)^{1-\theta_n}
=
1-I_n+o(I_n).
\tag{5.5}
\]

Combining (5.4)-(5.5),

\[
Z_{\theta_n,n}
=
1+(4^c-1)I_n+o(I_n).
\]

Since \(\log_2(1+x)=x/\ln2+o(x)\), (5.1) follows.

### Proof of part 2

From (4.2),

\[
\log\frac{t_{\theta_n,n}}{I_n}
=
\theta_n\log\frac{2^n-1}{I_n}
+
(1-\theta_n)\log\frac{\beta_1}{I_n}.
\]

The second term tends to zero, while

\[
\log\frac{2^n-1}{I_n}
=
(2n+o(n))\ln2.
\]

Thus \(n\theta_n\to\infty\) implies \(t_{\theta_n,n}/I_n\to\infty\). The argument of Theorem 4.1 then gives (5.2). \(\square\)

### Quantitative interpretation

At the critical choice \(\theta_n=1/n\),

\[
\frac{\log_2Z_{\theta_n,n}}{I_n}
\longrightarrow
\frac3{\ln2}
=
4.3280851226\ldots
\]

The diagnostic checker gives:

| \(n\) | \(\theta=1/n\) | \(\log_2Z_\theta/I\) |
|---:|---:|---:|
| 8 | 0.125 | 2.5973984891 |
| 16 | 0.0625 | 3.2918192915 |
| 32 | 0.03125 | 3.6698616485 |
| 64 | 0.015625 | 3.9293000485 |
| 128 | 0.0078125 | 4.0946940309 |

The theorem, not this numerical table, supplies the all-\(n\) statement.

## 6. What this rules out — and what survives

The account01 depth-filtered-KL obstruction showed that one cannot localize the negative product-shadow credit by valuation packet and retain positivity.

Theorems 2.1, 4.1 and 5.1 now show that the most natural repair also has a hard limitation:

\[
\boxed{
\text{one scalar globally normalized arithmetic/product escort}
}
\]

does preserve a genuine KL divergence, but if its arithmetic weight is bounded away from zero (or merely satisfies \(n\theta_n\to\infty\)), its partition is not influence-paid even on the canonical one-point defect.

Thus the route

1. globally tilt toward arithmetic data;
2. discard the resulting global KL because it is nonnegative;
3. pay the partition term separately by influence

is rigorously dead for every fixed positive scalar tilt.

This is stronger than the previously known \(\theta=1/2\) failure: it covers the whole scalar Rényi/geometric interpolation and identifies the exact adaptive threshold.

What remains alive is also precise.

- The **global escort KL must stay coupled to its partition**, just as the account01 packet-depth counterexample already warned.
- An adaptive \(\theta_n=O(1/n)\) can tame the partition on the one-point defect, but then the scalar interpolation places only a vanishing dimension-dependent weight on the arithmetic free-energy identity. This does not by itself produce a universal proof.
- A packet-dependent/non-scalar transport is not ruled out, but it needs a new normalization/monotonicity theorem; it cannot appeal merely to packetwise KL nonnegativity.
- The account02 self-XOR/Hellinger route is genuinely different: its current unpaid term is the mass-weighted \(|d|\ge2\) dual-shift remainder, not this scalar packet partition. That is a plausible pivot if no coupled packet-KL transport can be found.

## 7. Current literature check

A fresh primary-source check on 21 September 2026 still finds no unrestricted uniform-cube FEI proof in the inspected current literature.

- Vladimir N. Potapov, arXiv:2609.21563, posted 18 September 2026, proves FEI for plateaued functions with sharp class constant \(4\) and for partially bent functions with sharp constant \(2\). It does not cover arbitrary unequal-magnitude spectra.
- María José González, Paul MacManus, María Cristina Pereyra, arXiv:2606.00246, 29 May 2026, develop the restriction/stopping-tree route and explicitly describe a still-missing general restriction inequality whose validity would imply full FEI.
- Peijie Li and Guangyue Han, arXiv:2512.03117, 2 December 2025, prove a strengthened information-theoretic inequality that still contains the coordinate influence-profile entropy term in addition to total influence.

No publication-priority claim is made for the escort interpolation or critical-scale obstruction. The interpolation is an elementary information identity; the project-specific value is that it closes the currently proposed scalar global-tilt repair and quantifies exactly how it fails.

## 8. Reproducibility

`check_global_escort_obstruction.py` is standard-library only and evaluates the exact closed-form one-point-defect inputs with 180-digit decimal arithmetic. It reports fixed \(\theta\in\{1/4,1/2,3/4,1\}\) and the critical choice \(\theta=1/n\) for \(n=8,16,32,64,128\).

The script is a diagnostic, not the proof of Theorems 4.1 and 5.1.

Script SHA-256:

`9b34f4d08d6b3bb0ec1cd58504be97c28bf4495c38b65bcc3fb1af6840cd4c11`

Recorded output SHA-256:

`88f7de816222d3fa2aa89c8cbffe60167ef660c2d138b1ad3d86e34015053add`

## 9. Before / after and next obligation

**Before:** the joint D interface had a valid valuation-tail payment and a valid global product-shadow KL, but depth-filtering that KL was false. The proposed next repair was a single globally normalized arithmetic tilt with a partition term hoped to be \(O(I)\).

**After:** the complete scalar global-escort family is explicit in (2.3). Every fixed positive arithmetic weight has a partition/influence blow-up on one-point defects. The exact adaptive threshold is \(\theta_n\asymp1/n\).

**FULL PROBLEM:** `OPEN -> OPEN`.

**MECHANISM CHANGE:** `depth-filtered KL -> single global scalar escort -> rigorous all-positive-fixed-weight obstruction`.

**Next exact B15 obligation:** either

1. prove a **coupled** inequality in which \(\log Z_\theta-D_{\rm KL}(p\|m_\theta)\) is paid as one object (never separating the KL), with a function-adaptive \(\theta\) and the one-point defect / punctured-majority / Numaro families as mandatory stress tests; or
2. leave scalar packet escorts and build a genuinely non-scalar transport/dual representation, or consume the self-XOR/Hellinger multi-shift route.

A repeat of partition-only payment, valuation-depth slicing, or fixed-\(\theta\) geometric interpolation would now be a known dead route.
