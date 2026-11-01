# fleet04/B15 — arity-five center tube, and a tensor no-go for the newest collision remainder

**Run:** `20260922T051120Z-b15-f617292c`  
**Classification:** `ESSENTIAL_STEP_APPLIED / CANDIDATE_REFUTED`; unrestricted FEI remains **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Change summary and later-owner scope


\[
C_*=6.5218512,\qquad
\Gamma_*(p)=\Gamma_{\rm RO}(p)+0.2682048\,p(1-p),
\]

and the missing implication is

\[
D_{\Gamma_*}(P;p)\ge0
\]

for every composition-prime Boolean gate of every arity and every interior product bias.  The main new owner-aligned result below proves that no arity-five counterexample can approach the uniform input-bias vector: there is an actual open five-dimensional tube about `(1/2,...,1/2)` on which **all** five-input gates satisfy the candidate.

Because the native B15 prompt explicitly requires consumption of fleet02/B15's newest negative-credit arithmetic result, I also bind to it exactly.  That consumption exposes a newer collision remainder proposed by fleet04/B17.  A materially different tensor-suspension construction below refutes that scalar collision remainder with **no finite universal constant**.  This is recorded to retire the bridge, not to open a replacement route.  It does not refute FEI and does not supersede the all-gate target.

## 1. Exact peer inputs

### 1.1 fleet02/B15: all current information credits retained

The newest completed fleet02/B15 source is

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B15/20260922T040227Z-balanced-stop-kl-fusion/REPORT.md`.

For every balanced noncharacter Boolean `f`, with spectral sample `S`, `K=|S|`, `I=E K`, occurrence law

\[
q_i=\frac{\Pr(i\in S)}{I},
\]

it proves the exact source identity

\[
\boxed{
H(f)= I H_2(q)+T_{\rm stop}
      -\mathbb E\log_2(K!)
      -\mathcal K_\rho
      -\mathcal J_{\rm mix}.
}
\tag{1.1}
\]

Here `K_rho>=0` is the genuine prefix/deletion KL refund and

\[
\mathcal J_{\rm mix}
=
D_{\rm KL,2}(\alpha\|q)
+(I-1)D_{\rm KL,2}(\rho\|q)\ge0
\tag{1.2}
\]

is the genuine root/deletion mixing KL refund.  The same source proves `T_stop=O(I-1)` for balanced Boolean sources and pays the one-time valuation reserve at the same support-deficit scale.  Nothing below assumes packet integrality, repeats valuation at every deletion, or drops either KL credit.

### 1.2 fleet04/B17: ordered-occurrence fusion and collision target

The completed source

`proofnet24/P03-fei/fleet-2026-09-21/fleet04/B17/20260922T041638Z-ordered-occurrence-collision/REPORT.md`

fuses the credits in (1.1) into the actual ordered-occurrence divergence

\[
\mathcal D_{\rm ord}
=\sum_k W_kD_2(P_k\|q^{\otimes k})
=H_2(K)-T_{\rm stop}+\mathcal K_\rho+\mathcal J_{\rm mix}.
\tag{1.3}
\]

Data processing through the event that `k` independent `q`-draws are all distinct gives

\[
D_2(P_k\|q^{\otimes k})\ge-\log_2(k!e_k(q)),
\tag{1.4}
\]

and hence

\[
H(f)\le H_2(K)+\mathcal C_{\rm coll}(f),
\qquad
\boxed{
\mathcal C_{\rm coll}(f)
=I H_2(q)+\mathbb E\log_2 e_K(q).
}
\tag{1.5}
\]

Because `H(K)=O(I-1)` is already paid, B17 proposed the sufficient scalar implication

\[
\mathcal C_{\rm coll}(f)\le C_{\rm coll}[I(f)-1]
\tag{1.6}
\]

for all balanced Boolean `f`.  B17's addressing test showed any such coefficient must be at least four, but did not settle finiteness.

## 2. Main owner-aligned theorem: every five-input gate is safe in a uniform-bias tube

The source

`proofnet24/P03-fei/fleet-2026-09-21/fleet01/B17/20260922T043923Z-arity5-uniform-c001/REPORT.md`

proves for **every** five-input Boolean gate `G`

\[
D_{\Gamma_{.01}}(G;\tfrac12,\ldots,\tfrac12)\ge0,
\qquad
\Gamma_{.01}(p)=\Gamma_{\rm RO}(p)+0.01\,p(1-p).
\tag{2.1}
\]

The stable candidate differs by

\[
\delta=0.2682048-0.01=0.2582048.
\]

For every gate/bias vector, the scalar-lift cocycle gives

\[
D_{\Gamma_*}(G;p)
=
D_{\Gamma_{.01}}(G;p)+\delta M_G(p),
\tag{2.2}
\]

where

\[
M_G(p)=\frac14 I(G;p)-p_{\rm out}(1-p_{\rm out})\ge0.
\tag{2.3}
\]

At the uniform five-cube point let `m` be the number of `-1` truth-table values and `B` the undirected cube boundary of that set. Then

\[
I(G)=\frac B{16},\qquad
p_{\rm out}=\frac m{32},
\]

so

\[
\boxed{
M_G(\tfrac12^5)
=
\frac{16B-m(32-m)}{1024}.
}
\tag{2.4}
\]

The numerator is an integer.  Hence either `M_G=0` or

\[
M_G(\tfrac12^5)\ge\frac1{1024}.
\tag{2.5}
\]

Combining (2.1)-(2.5),

\[
\boxed{
M_G(\tfrac12^5)>0
\Longrightarrow
D_{\Gamma_*}(G;\tfrac12^5)
\ge
\frac{0.2582048}{1024}
=
0.000252153125.
}
\tag{2.6}
\]

If `M_G=0`, equality holds in uniform-cube Poincare.  In Fourier form,

\[
I-\operatorname{Var}(G)
=
\sum_{S\ne\emptyset}(|S|-1)\widehat G(S)^2=0,
\]

so all nonconstant Fourier mass lies on level one.  A Boolean function of Fourier degree at most one is a constant or a signed dictator: from `G^2=1`, coefficients of `x_i x_j` force at most one nonzero linear coefficient, and coefficients of `x_i` then force the constant coefficient to vanish unless the function is constant.  Constants are direct base cases, while a signed dictator satisfies the gate identity with equality for **every** bias vector.

The certified read-once potential `Gamma_RO` is continuous: its candidate is piecewise linear in `x=log_2(1/p)` on `p<=1/2`, mirrored about `1/2`, with a continuous tail; the quadratic lift is continuous.  Biased Fourier coefficients, biased influences and output measure are continuous in the interior product biases, and `-x log x` is continuous at zero.  Therefore `D_{\Gamma_*}(G;p)` is continuous at `p=(1/2)^5` for each fixed gate.

There are only finitely many five-input truth tables.  For every nonconstant nondictator gate, (2.6) gives the same positive center buffer.  Taking the minimum of the finitely many individual continuity radii proves:

### Theorem B15-ARITY5-CENTER-TUBE-01

There exists an absolute number `epsilon_5>0` such that for every Boolean gate on at most five inputs and every bias vector satisfying

\[
\max_i|p_i-\tfrac12|<\epsilon_5,
\]

one has

\[
\boxed{
D_{\Gamma_*}(G;p)\ge0.
}
\tag{2.7}
\]

Equivalently, no sequence of arity-five counterexamples to `LIMIT-PRIME-GATE-LIFT-v1` can converge to the uniform bias vector.

This is an existence theorem, not an explicit numerical tube radius.  Its new ingredient beyond the exact central-slice certificate is the discrete Poincare buffer (2.4)-(2.6), which makes the larger stable lift strictly safe for every non-affine gate and lets compactness convert one certified point into an honest open all-gate region.

## 3. Materially different Interface-D test: the collision remainder is unbounded

Although (1.6) keeps all B15 credits through the data-processing step, it is false with every finite constant.  The obstruction is a genuine balanced Boolean family.

For `n>=2`, let

\[
g_n(x)=1-2\mathbf1_{\{x=0\}}
\]

be the `n`-variable one-point defect and put

\[
a=2^{1-n}.
\]

Its normalized Walsh coefficients are

\[
\widehat g_n(\emptyset)=1-a,\qquad
\widehat g_n(S)=-a\quad(S\ne\emptyset).
\tag{3.1}
\]

Thus each coordinate occurrence probability is exactly `a` and

\[
I(g_n)=na.
\tag{3.2}
\]

Let `h_{n,k}=g_n^{\otimes k}` on `N=nk` disjoint variables and add one fresh unbiased character `y`:

\[
f_{n,k}(y,x)=y\,h_{n,k}(x).
\tag{3.3}
\]

Then `f_{n,k}` is balanced Boolean.  Its spectral sample always contains `y`.  If `L` is the Fourier level of one seed, its exact law is

\[
\Pr(L=0)=(1-a)^2,\qquad
\Pr(L=t)=\binom nt a^2\quad(1\le t\le n),
\tag{3.4}
\]

with `E L=na`.  For `T=L_1+\cdots+L_k`,

\[
K=1+T,\qquad
I(f_{n,k})-1=Na.
\tag{3.5}
\]

The occurrence law has

\[
q_y=\frac1{1+Na},\qquad
q_x=\frac a{1+Na}
\tag{3.6}
\]

for each of the `N` ordinary coordinates.

For `K=1+T`, the elementary symmetric polynomial is exactly

\[
e_{1+T}(q)
=
(1+Na)^{-(1+T)}
\left[
\binom NT a^T+\binom N{T+1}a^{T+1}
\right].
\tag{3.7}
\]

Also

\[
I H_2(q)
=
(1+Na)\log_2(1+Na)-Na\log_2 a.
\tag{3.8}
\]

Using `E T=Na`, all normalizer and `a` terms cancel between (3.7) and (3.8).  Therefore the B17 collision remainder has the exact closed form

\[
\boxed{
\mathcal C_{\rm coll}(f_{n,k})
=
\mathbb E\!\left[
\log_2\binom NT
+
\log_2\!\left(1+a\frac{N-T}{T+1}\right)
\right].
}
\tag{3.9}
\]

This identity is the key calculation; no information credit has been discarded in obtaining it.

For fixed `n`, the strong law gives `T/N -> a`.  The standard type bound

\[
Nh_2(t/N)-\log_2(N+1)
\le
\log_2\binom Nt
\le
Nh_2(t/N)
\tag{3.10}
\]

holds uniformly in `t`, while the second logarithm in (3.9) is between zero and `log_2(1+aN)`.  Since `h_2` is bounded and continuous,

\[
\boxed{
\lim_{k\to\infty}
\frac{\mathcal C_{\rm coll}(f_{n,k})}{I(f_{n,k})-1}
=
\frac{h_2(a)}a.
}
\tag{3.11}
\]

Finally, with `a=2^{1-n}`,

\[
\frac{h_2(a)}a
=
\log_2\frac1a
+\frac{1-a}{a}\log_2\frac1{1-a}
\sim n-1+\frac1{\ln2}
\longrightarrow\infty.
\tag{3.12}
\]

Hence:

### Theorem B15-COLLISION-NOGO-02

There is **no finite universal constant** `C_coll` for (1.6), even restricted to balanced Boolean functions:

\[
\boxed{
\sup_{f\ {m balanced}}
\frac{\mathcal C_{\rm coll}(f)}{I(f)-1}
=\infty.
}
\tag{3.13}
\]

The natural coefficient-four candidate is therefore false.  This is stronger than a failure on arbitrary subset laws: every witness above is an actual Boolean function.

It is not a counterexample to FEI.  Indeed

\[
\frac{H(f_{n,k})}{I(f_{n,k})-1}
=
\frac{H(g_n)}{I(g_n)},
\tag{3.14}
\]

which stays bounded and tends to `4` as `n` grows.  The divergence occurs only after replacing the full ordered-occurrence KL by the distinctness-event data-processing lower bound.  That coarse-graining loses an amount linear enough to swamp the support-deficit currency.

## 4. Explicit finite certificate for the coefficient-four failure

A standard-library checker reconstructs the one-point seed Walsh transform exactly and uses rational arithmetic throughout the `n=4, k=32` level convolution.  Logarithms are enclosed by an atanh series after exact power-of-two range reduction.

It certifies the actual balanced Boolean function on

\[
1+4\cdot32=129
\]

variables with

\[
\boxed{
\frac{\mathcal C_{\rm coll}}{I-1}
>
4.102446124368132
>4.
}
\tag{4.1}
\]

Checker SHA-256:

`4a03b2980dd99d03b3277f3c2fe4df41d748cd8067d64d16137825a863c817ba`

Captured-output SHA-256:

`f7d1ec91e5da7a08f9a6fa7b9ab49e69f52cd15622f5de0c08d9e726936dc347`

The checker is a falsification/self-consistency artifact; the unbounded theorem (3.13) is analytic.

## 5. Consequences for the common proof chain

The collision data-processing replacement (1.4)-(1.6) is retired.  The failure pinpoints the lost structure: conditioning `q^{\otimes K}` only on the one-bit event “all coordinates are distinct” retains too little of the ordered source law.  The full ordered-occurrence KL in (1.3) may still contain the needed source information; this report does **not** refute bounds that keep more of `P_K`, couple valuation inside those fibres, or use the full all-gate potential directly.

Under the later owner convergence order, the active universal target remains `LIMIT-PRIME-GATE-LIFT-v1`.  The new owner-aligned reduction is now:

* arity five is certified at the exact center by fleet01/B17;
* this run proves there is a genuine open all-gate tube around that center;
* any arity-five falsifier must therefore live a positive distance off-center;
* the collision remainder cannot be used as a scalar shortcut for controlling that frontier.

The next useful B15 work should stay on the fixed gate candidate and make `epsilon_5` effective, or attack a genuinely off-center prime gate/bias vector.  Repeating collision/valuation scalar remainders would violate both the new no-go theorem and the owner's convergence order.

## 6. Literature/status guard

No novelty or publication-priority claim is made for either theorem in this run.  A fresh primary-source search still finds unrestricted FEI stated as a conjecture: Potapov (18 September 2026) proves it for plateaued and partially bent classes, while González--MacManus--Pereyra (29 May 2026) give a restriction framework whose key universal inequality would imply the full conjecture.  Full FEI remains open.
