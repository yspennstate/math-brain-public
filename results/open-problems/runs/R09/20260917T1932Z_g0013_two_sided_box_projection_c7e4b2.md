Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — METRIC MOVEMENT on active R09 successor G0013: `U_* = U_MP = 17/171 + (8/19) z_* = 0.1107882326... -> 580249/5337500 = 0.108711756440281...`; Tang remains RETIRED/FROZEN at `UNBOUNDED_ABOVE` with supported retirement count `6`, and G0002 remains handed off at `Delta_8=UNMEASURED`. Methods used: B3 PROVE SOMETHING STRONGER, B12 FIND WHAT IS CONSERVED, B18 SAY IT IN ANOTHER LANGUAGE.** GPT-6 / maximum was requested in prompt text, but this runtime exposes no authenticated model-family selector or reasoning-effort selector, so I do not claim otherwise.

# R09 CLOSABLE OUTSIDE — G0013: exact two-sided box projection and a stronger global copula bound

Date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity, ownership, and run-start reads

I did **not** reopen Pengfei Tang, Question 4.11. The periodic-tree target remains retired from R09 at the frozen metric `UNBOUNDED_ABOVE`, supported retirement count `6`. I also did not reopen G0002 / Cerf Conjecture 53.1, which remains handed off at `Delta_8=UNMEASURED`.

The controlling current claim is `operations/claims/G0013.md`: R09 exclusively owns the Catalano--Lavenant uniform-copula Wasserstein problem. With
\[
\lambda=\mathrm{Unif}[0,1],\qquad \nu=\lambda\otimes\lambda,
\]
write
\[
M=\sup_{\pi\in\Pi(\lambda,\lambda)} W_2^2(\pi,\nu).
\]
The source conjectures \(M=1/10\), with the diagonal and antidiagonal as maximizers. The frozen R09 metric is the smallest rigorous source-valid global upper bound `U_*` on \(M\).

The preceding complete report,
`runs/R09/20260917T1831Z_g0013_moment_projection_bound_a4e921.md`,
proved
\[
M\le U_{\rm MP}:=\frac{17}{171}+\frac8{19}z_*,
\]
where \(z_*>0\) is the unique positive root of
\[
175104z^3+4500z-125=0,
\]
and certified
\[
0.11078823246783626<U_{\rm MP}<0.1107882328888889.
\]

Before new mathematics I reread/recovered the current campaign/control state: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the current G0013 claim, the newest complete R09 report, the current neighboring R08 state (F0083) and the newest searchable R10 successor/rotation state, plus exact G0013 intake/attempt searches. The intake JSONL corpus is too large to render byte-for-byte in one connector response, so I used exact-ID/source searches rather than pretending otherwise. Root `RESULTS.md` remains stale on R09 relative to the newer exclusive G0013 claim; this worker does not edit shared roots.

## 2. Fresh source / later-paper / prior-art check — 17 September 2026

Primary source: Marta Catalano and Hugo Lavenant, *Measures of Dependence based on Wasserstein distances*, arXiv:2510.06034 (submitted 7 October 2025), Remark 3.

Current later paper: Stefan Schrott, *Couplings Farthest from the Independent Gaussian*, arXiv:2609.10467v1 (submitted 9 September 2026). Its abstract still says that Catalano and Lavenant **conjectured** that the monotone and antimonotone uniform couplings are farthest from independence, and proves the Gaussian analogue instead.

Fresh bounded searches on 17 September 2026 used the exact source title/authors, `Catalano Lavenant Wasserstein copula conjecture`, `Couplings Farthest from the Independent Gaussian`, `uniform copula farthest independence`, and combinations of `L2 projection`, `box constraints`, `moments`, `clipped affine`, and `bathtub principle`. I found no later source claiming a resolution of the uniform conjecture. Generic box/affine projection and bathtub-principle machinery is standard convex-analysis folklore; I found no inspected source advertising the exact conditional-CDF obstacle calculation or the global constant below. This is bounded negative evidence only: **publication novelty remains UNVERIFIED**.

## 3. Inherited full-class reduction

For a positive smooth copula density, let
\[
T=\nabla\phi=(u,v)
\]
be the Brenier map from the independent uniform square to \(\pi\). For \(t,s\in[0,1]\), define the conditional sublevel lengths
\[
q_t(y)=\lambda\{x:u(x,y)\le t\},\qquad
r_s(x)=\lambda\{y:v(x,y)\le s\}.
\]
The output marginals are uniform, hence
\[
\int_0^1q_t(y)\,dy=t,\qquad
\int_0^1r_s(x)\,dx=s.
\tag{3.1}
\]
Set
\[
I_1=\int_0^1\operatorname{Var}(q_t)\,dt,\qquad
I_2=\int_0^1\operatorname{Var}(r_s)\,ds.
\]
The earlier R09 Brenier calculation proved the exact identity
\[
W_2^2(\pi,\nu)=I_1+I_2.
\tag{3.2}
\]

For each \(t\), decompose
\[
q_t(y)-t=A_t\Bigl(y-\frac12\Bigr)+g_t(y),
\]
where \(g_t\perp 1\) and \(g_t\perp y-\frac12\). Let
\[
h_t=\int_0^1g_t(y)^2\,dy,\qquad H_1=\int_0^1h_t\,dt,
\]
and define \(H_2\) symmetrically for \(r_s\). The shifted-Legendre/Jacobi spectral gap, together with positive semidefiniteness of the Brenier Hessian, gave
\[
2I_1+I_2+4H_1\le\frac16,\qquad
I_1+2I_2+4H_2\le\frac16.
\tag{3.3}
\]
Thus, with
\[
S=I_1+I_2,\qquad H=H_1+H_2,
\]
we have
\[
S\le\frac19-\frac43H.
\tag{3.4}
\]

The previous run relaxed the pointwise constraint \(0\le q_t\le1\) to a one-sided nonnegativity problem. The new work solves the **full two-sided box projection exactly**.

## 4. B3 + B18 — stronger statement in the right language: exact two-sided moment projection

The basic one-dimensional problem is the following.

### Lemma 4.1 (exact box-constrained moment projection)

Let \(q:[0,1]\to[0,1]\) be measurable with
\[
\int_0^1q=t.
\]
Define
\[
A=12\int_0^1\Bigl(y-\frac12\Bigr)(q(y)-t)\,dy
 =12\int_0^1\Bigl(y-\frac12\Bigr)q(y)\,dy
\]
and
\[
q(y)-t=A\Bigl(y-\frac12\Bigr)+g(y),
\qquad
g\perp\{1,y-\tfrac12\},
\qquad
h=\int_0^1g^2.
\]
Put
\[
m=\min(t,1-t),\qquad a=|A|.
\]
Then
\[
0\le a\le6m(1-m),
\tag{4.1}
\]
and the smallest possible \(h\) for fixed \((m,a)\) is
\[
h_{\min}(m,a)=
\begin{cases}
0,
&0\le a\le2m,\\[1ex]
\dfrac{(a-2m)^3}{12(6m-a)},
&2m<a\le6m-8m^2,\\[3ex]
m(1-m)-\dfrac{L}{6}-\dfrac{a^2}{12},
&6m-8m^2<a\le6m(1-m),
\end{cases}
\tag{4.2}
\]
where in the last line
\[
L=\sqrt{12m(1-m)-2a}\in[0,2m).
\tag{4.3}
\]
The minimizer is uniquely the clipped affine profile compatible with the two moments.

#### Proof

Complement \(q\mapsto1-q\) and reflection \(y\mapsto1-y\) preserve \(h\), so it suffices to take \(0\le m=t\le1/2\) and \(A=a\ge0\). The bathtub/rearrangement bound gives (4.1).

Let
\[
\ell(y)=m+a(y-\tfrac12).
\]
Since \(q-\ell=g\) is orthogonal to \(1\) and \(y-\tfrac12\),
\[
\int_0^1q^2=m^2+\frac{a^2}{12}+h.
\tag{4.4}
\]
Therefore minimizing \(h\) is exactly the strictly convex problem of minimizing \(\int q^2\) over the box \(0\le q\le1\) with the two prescribed moments. This is an \(L^2\) projection onto an affine slice of the box.

If \(a\le2m\), then \(\ell\in[0,1]\) pointwise because
\[
m-\frac a2\ge0,\qquad m+\frac a2\le2m\le1.
\]
Thus \(q=\ell\) is feasible and \(h_{\min}=0\).

Now suppose \(a>2m\). First consider
\[
a\le6m-8m^2.
\]
Set
\[
L=\frac{6m-a}{4m},\qquad
\alpha=1-L,\qquad
\beta=\frac{2m}{L^2},
\]
and
\[
p(y)=\beta(y-\alpha)_+.
\tag{4.5}
\]
Direct integration gives
\[
\int p=m,\qquad
12\int(y-\tfrac12)p=a.
\tag{4.6}
\]
Moreover
\[
p(1)=\frac{2m}{L}\le1
\]
is exactly equivalent to \(a\le6m-8m^2\), so \(p\) is box-feasible. The previous one-sided projection argument is therefore exact here, not merely a relaxation. It gives
\[
h_{\min}
=\|p-\ell\|_2^2
=\frac{(a-2m)^3}{12(6m-a)}.
\]

Finally suppose
\[
6m-8m^2<a\le6m(1-m).
\]
Define \(L\) by (4.3), and set
\[
\alpha=1-m-\frac L2,\qquad
\beta=1-m+\frac L2.
\]
The candidate is
\[
p(y)=
\begin{cases}
0,&y\le\alpha,\\
\dfrac{y-\alpha}{L},&\alpha<y<\beta,\\
1,&y\ge\beta.
\end{cases}
\tag{4.7}
\]
(At \(L=0\), interpret this as the indicator of the top interval of length \(m\).)
Direct integration gives
\[
\int p=m,
\qquad
12\int(y-\tfrac12)p=6m(1-m)-\frac{L^2}{2}=a,
\tag{4.8}
\]
and
\[
\int p^2=m-\frac L6.
\tag{4.9}
\]

To prove optimality without invoking an abstract KKT theorem, write
\[
s(y)=\frac{y-\alpha}{L},
\qquad
p=\operatorname{clip}_{[0,1]}(s).
\]
For any other box-feasible \(q\) with the same two moments,
\[
\int(q-p)s=0
\]
because \(s\) is affine. Pointwise Euclidean projection onto \([0,1]\) gives
\[
(q-p)(p-s)\ge0.
\]
Hence
\[
\int(q-p)p\ge0.
\]
Therefore
\[
\|q\|_2^2
=\|p\|_2^2+\|q-p\|_2^2+2\langle q-p,p\rangle
\ge\|p\|_2^2.
\]
Strict convexity gives uniqueness. Combining (4.4) with (4.9) yields the last line of (4.2). QED.

This is the stronger object the previous one-sided relaxation was approximating: the true extremizer is a clipped affine profile, with a genuine two-obstacle regime near maximal first moment.

## 5. B12 — conserved moments and an exact conditional-Gini identity

The useful conserved quantities are not only the mass \(t\) and first Jacobi coefficient \(A_t\). The whole nested family \(\{q_t\}\) has an exact probabilistic interpretation.

For fixed \(y\), let \(U,U^\star\) be conditionally i.i.d. with the law of \(u(X,y)\) given \(Y=y\). Then
\[
q_t(y)=\mathbb P(U\le t\mid Y=y),
\]
and
\[
\int_0^1q_t(y)^2\,dt
=1-\mathbb E[\max(U,U^\star)\mid Y=y].
\]
Averaging in \(y\), using the uniform output marginal \(\mathbb E U=1/2\), gives
\[
I_1
=\frac16-\frac12\,\mathbb E|U-U^\star|.
\tag{5.1}
\]
Similarly, if \(V,V^\star\) are conditionally i.i.d. given \(X\),
\[
I_2
=\frac16-\frac12\,\mathbb E|V-V^\star|.
\tag{5.2}
\]
Thus
\[
\boxed{
W_2^2(\pi,\nu)
=\frac13-\frac12(G_1+G_2),
}
\tag{5.3}
\]
where \(G_1,G_2\) are the two conditional Gini mean differences above.

Consequently the full Catalano--Lavenant conjecture is equivalent, on the Brenier representation, to
\[
\boxed{G_1+G_2\ge\frac7{15}.}
\tag{5.4}
\]
This identity does not by itself close the source problem, but it is a second exact language for the same obstruction. It also explains why the weighted Hessian/Jacobi functional appears: for monotone one-dimensional slices, conditional Gini differences are weighted derivative integrals.

## 6. B18 — clipped-affine penalty and a rational pointwise envelope

The exact obstacle lemma can be turned into a simple linear penalty with a deliberately chosen rational coefficient
\[
k=\frac{112}{13},
\qquad
\frac{k}{1+k}=\frac{112}{125}.
\tag{6.1}
\]
For fixed \((m,a)\), define
\[
\Psi(m,a)=\frac{a^2}{12}-k\,h_{\min}(m,a).
\tag{6.2}
\]

### Lemma 6.1 (piecewise rational envelope)

For \(0\le m\le1/2\),
\[
\Psi(m,a)\le b(m)
\qquad(0\le a\le6m(1-m)),
\tag{6.3}
\]
where
\[
b(m)=
\begin{cases}
\dfrac7{13}m^2,&0\le m\le\dfrac25,\\[1.5ex]
\dfrac{2273}{20000},&\dfrac25\le m\le\dfrac12.
\end{cases}
\tag{6.4}
\]

#### Proof for \(m\le2/5\)

In the lower-clipping regime write
\[
a=2mu,\qquad 1\le u<3.
\]
Then
\[
\Psi(m,a)
=m^2 G(u),
\qquad
G(u)=\frac13\left[
u^2-\frac{112}{13}\frac{(u-1)^3}{3-u}
\right].
\]
The exact factorization
\[
G(u)-\frac7{13}
=
\frac{(5u-7)^2(5u-1)}{39(u-3)}
\le0
\tag{6.5}
\]
holds for \(1\le u<3\). The no-clipping regime is even smaller.

It remains to exclude a rebound after the upper obstacle becomes active. In the two-sided regime, with \(L\) from (4.3),
\[
\frac{\partial\Psi}{\partial a}
=
\frac{(1+k)a-k/L}{6}
=
\frac{1+k}{6L}
\left(aL-\frac{112}{125}\right).
\tag{6.6}
\]
For fixed \(m\le1/2\), in the two-sided region \(0\le L\le2m\), and
\[
aL=\frac{12m(1-m)L-L^3}{2}
\]
is increasing in \(L\). At the transition \(L=2m\),
\[
aL=4m^2(3-4m).
\]
The latter is increasing on \([0,1/2]\) and at \(m=2/5\) equals exactly
\[
4\Bigl(\frac25\Bigr)^2
\Bigl(3-\frac85\Bigr)
=\frac{112}{125}.
\]
Hence for \(m\le2/5\), \(\partial_a\Psi\le0\) throughout the two-sided regime. The value can only decrease past the transition, proving the first line of (6.4).

#### Proof for \(2/5\le m\le1/2\)

The lower-clipping value increases up to its transition, so it suffices to control the two-sided regime. Put
\[
x=m(1-m),\qquad
a=6x-\frac{L^2}{2}.
\]
Using the last line of (4.2),
\[
\Psi
=
\frac{1+k}{12}a^2-kx+\frac{kL}{6}.
\tag{6.7}
\]
For fixed \(L\),
\[
\frac{\partial\Psi}{\partial x}
=(1+k)a-k.
\]
Throughout the two-sided regime with \(m\ge2/5\),
\[
a\ge6m-8m^2\ge1>\frac{k}{1+k}=\frac{112}{125},
\]
so (6.7) increases with \(x\). Since \(x\le1/4\), every such value is bounded by the corresponding \(m=1/2\) value with the same \(L\in[0,1]\).

At \(m=1/2\),
\[
F(L):=\Psi\Bigl(\frac12,\frac{3-L^2}{2}\Bigr)
=
\frac{125}{624}L^4
-\frac{125}{104}L^2
+\frac{56}{39}L
-\frac{73}{208}.
\tag{6.8}
\]
Moreover
\[
F''(L)=\frac{125}{52}(L^2-1)\le0
\quad(0\le L\le1),
\]
so \(F\) is concave. Exact rational arithmetic gives
\[
F'\!\left(\frac{1809}{2500}\right)
=\frac{1168129}{19500000000}>0,
\]
while
\[
F'\!\left(\frac{7237}{10000}\right)
=-\frac{68138947}{1248000000000}<0.
\]
Thus its unique maximizer lies between these two rationals. Concavity gives the tangent upper bound
\[
\max_{[0,1]}F
\le
F\!\left(\frac{1809}{2500}\right)
+
F'\!\left(\frac{1809}{2500}\right)
\left(
\frac{7237}{10000}-\frac{1809}{2500}
\right)
=
\frac{2216159556349}{19500000000000}.
\]
Finally
\[
\frac{2273}{20000}
-
\frac{2216159556349}{19500000000000}
=
\frac{15443651}{19500000000000}>0.
\]
This proves the second line of (6.4). QED.

## 7. Global theorem: \(U_*\) moves to \(580249/5337500\)

For each conditional CDF, its actual \(h\) is at least \(h_{\min}\). Since \(k>0\), Lemma 6.1 gives
\[
\frac{A_t^2}{12}-k h_t\le b(m_t),
\qquad
m_t=\min(t,1-t).
\]
Therefore
\[
\operatorname{Var}(q_t)
=
\frac{A_t^2}{12}+h_t
\le
b(m_t)+\frac{125}{13}h_t.
\tag{7.1}
\]
The same holds for \(r_s\).

Integrating the envelope exactly,
\[
B:=\int_0^1b(\min(t,1-t))\,dt
\]
equals
\[
\begin{aligned}
B
&=
2\left[
\int_0^{2/5}\frac7{13}t^2\,dt
+
\int_{2/5}^{1/2}\frac{2273}{20000}\,dt
\right]\\
&=
\boxed{\frac{178247}{3900000}}.
\end{aligned}
\tag{7.2}
\]
Hence
\[
I_i\le B+\frac{125}{13}H_i
\qquad(i=1,2),
\]
and so
\[
S\le2B+\frac{125}{13}H.
\tag{7.3}
\]
Together with the inherited spectral inequality (3.4),
\[
S\le
\min\left\{
2B+\frac{125}{13}H,\;
\frac19-\frac43H
\right\}.
\]
The increasing and decreasing affine bounds meet at
\[
H_0
=
\frac{\frac19-2B}{\frac{125}{13}+\frac43}
=
\boxed{\frac{115259}{64050000}}.
\]
Therefore
\[
\boxed{
S
\le
2B+\frac{125}{13}H_0
=
\frac{580249}{5337500}
=
0.108711756440281\ldots
}
\tag{7.4}
\]

By (3.2), for every positive smooth copula,
\[
W_2^2(\pi,\nu)\le\frac{580249}{5337500}.
\]
For a general copula, apply the Neumann heat semigroup independently in the two coordinates. It preserves the uniform marginals, produces positive smooth copula densities for positive time, and converges to the original copula in \(W_2\) on the compact square. Continuity of \(W_2(\,\cdot\,,\nu)\) passes (7.4) to the limit. Thus:

### Theorem 7.1

For every \(\pi\in\Pi(\lambda,\lambda)\),
\[
\boxed{
W_2^2(\pi,\lambda^{\otimes2})
\le
\frac{580249}{5337500}
=
0.108711756440281\ldots
}
\tag{7.5}
\]
Consequently
\[
\boxed{
\frac1{10}\le M\le\frac{580249}{5337500}.
}
\tag{7.6}
\]

The new global gap above the conjectured value is
\[
\frac{580249}{5337500}-\frac1{10}
=
\boxed{\frac{46499}{5337500}}
=
0.008711756440281\ldots
\tag{7.7}
\]
The preceding exact checker certified
\[
U_{\rm MP}>0.11078823246783626,
\]
so the strict metric improvement is at least
\[
0.11078823246783626-0.10871175644028103
>
0.0020764760.
\]

In the conditional-Gini language (5.3), the same theorem is
\[
G_1+G_2
\ge
\frac23-2\frac{580249}{5337500}
=
\boxed{\frac{3596753}{8006250}}
=
0.449243153786104\ldots
\tag{7.8}
\]
versus the conjectured sharp lower bound \(7/15\).

## 8. What the three methods actually did

**B3 — prove something stronger.** Instead of improving the previous one-sided relaxation by another constant, I solved the full two-sided \([0,1]\) moment-projection problem exactly. The stronger statement identifies the unique clipped-affine optimizer and all three regimes.

**B12 — find what is conserved.** The zeroth and first centered moments are exactly conserved by the projection, turning the higher-mode quantity \(h\) into a literal Hilbert-space distance. At the family level, nesting of the conditional CDFs also yields the exact conditional-Gini identities (5.1)--(5.3). That reformulation was not needed for the numerical constant, but it exposes a new source-equivalent target.

**B18 — say it in another language.** Rewriting the conditional-CDF obstruction as a box-constrained \(L^2\) projection converts the vague “higher Jacobi modes must be present” idea into a clipped-affine obstacle problem with an explicit dual/projection certificate. This language produced the rational penalty \(k=112/13\) and the new global bound.

## 9. Exact self-check

The exact/symbolic self-check is

`artifacts/R09/20260917T1932Z_g0013_two_sided_box_projection_exact.py`

and its executed output is

`artifacts/R09/20260917T1932Z_g0013_two_sided_box_projection_exact.out`.

The script verifies the two clipped-affine moment formulas symbolically, the lower-ramp factorization, the rational transition \(m=2/5\), the tail concavity certificate and rational derivative signs, the tangent margin, the integrated constant \(B\), the intersection \(H_0\), the final rational \(U_*\), and strict improvement over the previous certified lower bracket. The archived output ends

`SELF_CHECK_ONLY / PASS`.

This is a self-check of finite/symbolic algebra. It is **not** an independent audit.

## 10. Status, blocker, and next new routes

The source remains **PARTIAL / OPEN_CURRENT**, not proved. The metric moved, so the supported G0013 stagnation count resets to `0`.

The remaining gap is no longer the one-dimensional box projection: that problem is now solved exactly. What is still discarded is **cross-level structure** of the nested family \(t\mapsto q_t\) and the coupling between the two Brenier coordinates. The current proof applies the obstacle independently at each level and then keeps only the total higher-mode mass \(H_1+H_2\).

Next methods should be genuinely different from this run:

- **B8 (DISCRETIZE):** discretize the nested family itself, not the copula, into an order polytope of CDF levels and identify the exact finite inequality corresponding to \(G_1+G_2\ge7/15\);
- **B14 (FIND THE GROUP ACTING):** quotient the conditional-Gini formulation by square symmetries and characterize equality/near-equality orbits of the diagonal and antidiagonal Brenier maps;
- **B20 (FIND WHY THE ALGORITHM FAILS):** run the natural levelwise clipped-affine optimizer simultaneously across \(t\), determine the precise incompatibility with CDF nesting / cyclic monotonicity, and convert that incompatibility into a positive global deficit.

## 11. Model-control / permission status

The limitation remains unchanged in the interface exposed to this run. The task-management schema exposes title, prompt, schedule / relative start, timing mode, enabled state, and related delivery controls, but **no model-family selector, no reasoning-effort selector, and no authenticated applied-run model telemetry**. Thus the prompt can request GPT-6 / maximum, but this worker cannot honestly assert it was applied.

To enforce GPT-6 / maximum would require a product/API or owning scheduler surface that exposes (i) a model-family field, (ii) a reasoning-effort field, and (iii) authenticated completed-run telemetry confirming both. The historical `You cannot modify this task` P26 error is an authorization-context boundary. The valid workaround is to use the task's authorized owning context, transfer ownership/admin rights through the supported product flow, or obtain platform support. Duplicating or bypassing a denied task is not a valid repair, and this run performed no scheduler changes.

## 12. Structured `ledger_delta`

```yaml
ledger_delta:
  track: R09
  current_claim: G0013
  source_status: OPEN_CURRENT
  status: PARTIAL
  metric_name: U_*
  before:
    exact: "17/171 + (8/19) z_*, z_*>0 solves 175104 z^3 + 4500 z - 125 = 0"
    certified_bracket: "(0.11078823246783626, 0.1107882328888889)"
  after:
    exact: "580249/5337500"
    decimal: 0.10871175644028103
  movement: true
  supported_unchanged_count: 0
  source_lower_bound:
    exact: "1/10"
  remaining_gap:
    exact: "46499/5337500"
  new_theorem:
    scope: "all copulas in Pi(Unif[0,1], Unif[0,1])"
    statement: "W2^2(pi, lambda^2) <= 580249/5337500"
  exact_projection:
    scope: "all measurable q:[0,1]->[0,1] with fixed mass and first centered moment"
    optimizer: "unique clipped affine profile"
  methods:
    - 3
    - 12
    - 18
  checker:
    source: "artifacts/R09/20260917T1932Z_g0013_two_sided_box_projection_exact.py"
    output: "artifacts/R09/20260917T1932Z_g0013_two_sided_box_projection_exact.out"
    result: "SELF_CHECK_ONLY / PASS"
  tang_q4_11:
    state: "RETIRED/FROZEN"
    metric: "UNBOUNDED_ABOVE"
    supported_retirement_count: 6
  g0002:
    state: "HANDOFF"
    metric: "Delta_8=UNMEASURED"
  audits:
    p26: "not requested in this run"
    second_other_track: "not requested in this run"
  next_methods:
    - 8
    - 14
    - 20
```
