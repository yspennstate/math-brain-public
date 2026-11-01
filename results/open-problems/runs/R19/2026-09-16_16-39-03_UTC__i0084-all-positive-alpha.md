Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested, but the exposed runtime/scheduler has no model selector or reasoning-effort selector, so I do not claim otherwise. **NO MOVEMENT in the frozen metric: 2/2 -> 2/2. Section-B moves tried: 6, 7, 18.**

Problem/source: Takahiro Hasebe and Yuki Ueda, *Large time unimodality for classical and free Brownian motions with initial distributions* (ALEA 15, 2018), Conjecture 5.5 / intake I0084.

Status: **SOURCE REFUTED MATHEMATICALLY; fleet closure still PENDING P26.** The fixed half-stable metric is already saturated at 2/2 by the retained classical and free positive-alpha=1/2 counterexamples. This run does not manufacture metric movement. It instead proves two stronger all-positive-index statements, identifies why the large-time scaling limit does not restore unimodality, corrects a source-extraction/convolution mismatch, records the newly arrived R18 full audit of the free half-stable proof, and independently audits R20's new p=181 certificate.

# 1. Repository continuity and scope

I continued from the newest R19 report, not from chat memory:

`runs/R19/2026-09-16_15-35-00_UTC__i0084-free-halfstable-gap.md`.

Before doing mathematics I read or queried the required current repository state:

- `probability_campaign_2026_09/INDEX.md`;
- `probability_campaign_2026_09/RANKING.md`;
- root `POSTED.md`;
- root `RESULTS.md`;
- root `QUEUE.md`;
- `operations/FLEET_2026-09-16.md`;
- `operations/RFLEET_2026-09-16.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- the I0084 intake row in `probability_1000_intake_I_20260914/problems.jsonl`;
- the newest R18 package, which now contains an independent end-to-end audit of R19-I0084-C002;
- the newest ready R20/I0100 package, `runs/R20/2026-09-16T14-49-00Z_i0100_p181_5d7a3c.md`.

The intake JSONL/repository are too large for the connector to display byte-for-byte in one response. I used repository-wide searches and fetched the exact I0084 row and the relevant neighboring/current files. I do not pretend that every one of roughly 780 intake rows was rendered in full in this invocation.

No root/shared-ledger file is edited here; P26 remains the shared-ledger writer. No Gmail, Drive, scheduler, permission, or public-posting action is taken.

# 2. Source normalization correction: version of record overrides the lossy intake extraction

This run rechecked the ALEA version of record, page 373, DOI `10.30757/ALEA.v15-15`, and the arXiv record `1710.08240`.

The exact source convention is:

\[
S_t=\text{law of a classical strictly stable process},\qquad
T_t=\text{law of a free strictly stable process},
\]

and Conjecture 5.5 asks, under

\[
\int_{\mathbb R}|x|^{2+\alpha}\,d\mu(x)<\infty,
\]

for eventual unimodality of

\[
\boxed{\mu*S_t\quad\text{(classical branch)}}
\]

and respectively

\[
\boxed{\mu\boxplus T_t\quad\text{(free branch)}}.
\]

The root intake row I0084 is an OCR/extraction simplification that collapses the displayed `S_t (resp. T_t)` / `* (resp. boxplus)` notation into prose resembling one symbol `S_t` and one `*`. That extracted row is not authoritative against the version of record.

Therefore I do **not** silently replace the source convention. I keep:

- classical stable law -> classical convolution `*`;
- free stable law -> free convolution `boxplus`.

Because the owner specifically asked about the alternative literal extraction, Section 5 below separately proves that **even if** one classically convolves with a positive free-stable density, the same sparse-tail mechanism gives nonunimodality. That is a robustness check, not the source's free branch and not counted as extra metric credit.

There is no skewness restriction in Conjecture 5.5 beyond being a strictly stable process. The positive extreme-skew family exists for \(0<\alpha<1\), corresponding to positivity parameter \(\rho=1\).

# 3. Recovered frozen metric and audits

Frozen metric:

> number of the two positive alpha=1/2 source branches (classical and free) decided in the full source quantifier class under the finite 5/2-moment assumption.

Retained state before this run:

\[
\boxed{2/2.}
\]

- `R19-I0084-C001`: classical positive alpha=1/2 counterexample, with all finite polynomial moments; independent R18 audit PASS.
- `R19-I0084-C002`: free positive alpha=1/2 counterexample under the actual source free convolution `boxplus`; the previous report had its OTHER-track audit pending.

New repository state read this run:

`runs/R18/2026-09-16_16-27-31_UTC__R18__i0080-stuck1-r19audit-b5c2.md`

contains

`R18-AUDIT-R19-I0084-C002-ENDTOEND-001 = PASS_FULL_MATHEMATICAL_PROOF`.

Thus both half-stable mathematical branches now have an independent OTHER-track audit. The required P26 audit is still not located, so fleet closure remains pending.

Metric after this run:

\[
\boxed{2/2.}
\]

Unchanged-run count after saturation: **1**.

A single admissible counterexample is enough to refute the universal source assertion for that branch. The statement `2/2` does **not** mean that every admissible initial measure has been classified.

# 4. Move 6 — deform to an explicitly solvable input: a universal one-sided-kernel counterexample

## R19-I0084-C004 — universal one-sided convolution obstruction

**STATUS: PROVED.**

For \(t>0\), let \(k_t\) be a probability density satisfying:

1. \(k_t(x)=0\) for \(x\le0\);
2. \(k_t\in C^1((0,\infty))\);
3. there exists \(v_t>0\) such that
   \[
   k_t'(v_t)<0;
   \]
4. with that \(v_t\),
   \[
   M_t:=\sup_{u\ge v_t}|k_t'(u)|<\infty.
   \]

Define one probability measure, independent of \(t\) and of the kernel family,

\[
\boxed{
\mu_\star
=
w_0\delta_0+\sum_{n\ge1}e^{-n^4}\delta_{-n^2},
\qquad
w_0=1-\sum_{n\ge1}e^{-n^4}.
}
\tag{C004.1}
\]

Since
\[
\sum_{n\ge1}e^{-n^4}
<
\sum_{n\ge1}e^{-n}
=
\frac1{e-1}<1,
\]
we have \(w_0>0\).

Then for **every** \(t>0\),

\[
\boxed{\mu_\star*k_t\text{ is not unimodal}.}
\tag{C004.2}
\]

Moreover \(\mu_\star\) has every exponential moment of order \(|x|\):

\[
\boxed{
\int e^{c|x|}\,d\mu_\star(x)
=
w_0+\sum_{n\ge1}e^{-n^4+cn^2}<\infty
\quad(c>0).
}
\tag{C004.3}
\]

Hence it has every finite polynomial moment.

### Proof

Fix \(t>0\). Set

\[
q_t:=-k_t'(v_t)>0.
\]

For the weights \(w_n=e^{-n^4}\), define the relative farther-left tail

\[
R_n
:=
\frac{\sum_{j>n}w_j}{w_n}.
\]

Writing \(j=n+r\),

\[
(n+r)^4-n^4
=
4n^3r+6n^2r^2+4nr^3+r^4
\ge4n^3r,
\]
so

\[
R_n
\le
\sum_{r\ge1}e^{-4n^3r}
=
\frac{e^{-4n^3}}{1-e^{-4n^3}}
\longrightarrow0.
\tag{C004.4}
\]

Choose \(n\) so large that

\[
2n-1>v_t,
\qquad
M_tR_n<q_t/2.
\tag{C004.5}
\]

Let

\[
x_n=-n^2+v_t.
\]

The convolution has density

\[
f_t(x)
=
w_0k_t(x)+\sum_{j\ge1}w_jk_t(x+j^2).
\]

At \(x=x_n\), every atom to the **right** of \(-n^2\) contributes zero. Indeed, for \(j<n\),

\[
x_n+j^2
=
v_t-(n^2-j^2)
\le
v_t-(2n-1)<0,
\]
and also \(x_n<0\), so the atom at \(0\) contributes zero.

The \(j=n\) atom contributes

\[
w_n k_t'(v_t)=-q_tw_n.
\]

For \(j>n\),

\[
x_n+j^2=v_t+(j^2-n^2)\ge v_t,
\]
hence the absolute derivative contribution is at most \(M_tw_j\). Therefore the derivative series converges absolutely at \(x_n\), and

\[
\begin{aligned}
f_t'(x_n)
&\le
-q_tw_n+M_t\sum_{j>n}w_j\\
&=
w_n(-q_t+M_tR_n)\\
&<
-\frac{q_t}{2}w_n<0.
\end{aligned}
\tag{C004.6}
\]

But \(x_n\to-\infty\). If \(f_t\) were unimodal with a finite mode \(m\), then its continuous density would be nondecreasing on \(( -\infty,m)\). For all sufficiently large \(n\), \(x_n<m\), contradicting \(f_t'(x_n)<0\).

Thus \(\mu_\star*k_t\) is not unimodal for any \(t>0\).

Finally, for any \(c>0\), the exponent \(-n^4+cn^2\to-\infty\) quadratically in \(n^2\), proving C004.3. QED.

## What changed relative to the source's Proposition 5.4

The source's specific sparse construction at alpha=1/2 is tied to its condition (5.36), and the authors prove that within that particular construction the \(5/2\)-moment must diverge.

C004 uses a different mechanism:

- gaps grow only linearly in the index, since the atom locations are \(-n^2\);
- the weights decay superexponentially relative to the neighboring tail;
- one-sided support shields every heavier atom lying to the right;
- no source-specific derivative lower bound involving the gap size is needed.

This is why all exponential moments can coexist with nonunimodality for every time.

# 5. Classical stable consequences, including the literal OCR/extraction convention

## R19-I0084-C005 — every positive classical stable index \(0<\alpha<1\) is refuted by one initial law

**STATUS: PROVED.**

Let \(S_t^{(\alpha,+)}\) be any standard positive strictly classical alpha-stable semigroup with

\[
0<\alpha<1.
\]

Its density is supported on \([0,\infty)\), smooth on \((0,\infty)\), and bell-shaped; in particular its derivative is negative somewhere. Standard stable density asymptotics give bounded derivative on every tail \([v,\infty)\).

Therefore C004 applies, with the **same** measure \(\mu_\star\), for every \(\alpha\in(0,1)\) and every \(t>0\):

\[
\boxed{
\mu_\star*S_t^{(\alpha,+)}
\text{ is not unimodal for every }t>0,\quad 0<\alpha<1.
}
\tag{C005.1}
\]

And \(\mu_\star\) satisfies much more than the conjectured moment assumption:

\[
\boxed{
\int |x|^{2+\alpha}\,d\mu_\star(x)<\infty
\quad\text{for every }0<\alpha<1.
}
\tag{C005.2}
\]

Thus the classical positive-stable subfamily of Conjecture 5.5 fails throughout the entire admissible positive range \(0<\alpha<1\), not just at \(\alpha=1/2\).

### Literal extracted/OCR convention

Suppose, contrary to the ALEA version of record, one literally interprets the lossy intake text as asking for **ordinary classical convolution** of \(\mu\) with the density of a positive **free** stable law.

Hasebe--Kuznetsov show for the free stable parameterization that

\[
P(X_{\alpha,\rho}>0)=\rho
\]
and that free stable laws have smooth densities. Hence \(\rho=1\), \(0<\alpha<1\), gives a one-sided smooth density. Their convergent large-\(x\) density series gives tail derivative decay, and any nonconstant integrable positive density must decrease somewhere.

Therefore C004 also applies to that non-source literal interpretation:

\[
\boxed{
\mu_\star * \nu_{\alpha,1,t}
\text{ is nonunimodal for every }t>0,\quad 0<\alpha<1,
}
\tag{C005.3}
\]

where `*` here is deliberately classical convolution and \(\nu_{\alpha,1,t}\) is the positive free-stable density.

C005.3 is included only to neutralize the notation-extraction ambiguity. The actual free branch of Conjecture 5.5 uses \(\boxplus\), handled in Section 7.

# 6. Move 7 — take the large-time limit: convergence to the stable profile does not preserve unimodality

## R19-I0084-C006 — \(W^{1,1}\) scaling-limit obstruction

**STATUS: PROVED.**

Fix \(0<\alpha<1\) and let \(k\) be the time-one positive classical alpha-stable density. With the standard stable scaling

\[
k_t(x)=s_t^{-1}k(x/s_t),
\qquad
s_t=t^{1/\alpha},
\]
let

\[
f_t=\mu_\star*k_t
\]
and rescale back to unit stable scale:

\[
g_t(y):=s_t f_t(s_ty).
\]

Then

\[
g_t(y)
=
\int_{\mathbb R}
k\!\left(y-\frac{x}{s_t}\right)\,d\mu_\star(x).
\tag{C006.1}
\]

Because translations are continuous in \(L^1\),

\[
\|g_t-k\|_1
\le
\int
\left\|
\tau_{x/s_t}k-k
\right\|_1
\,d\mu_\star(x)
\longrightarrow0
\tag{C006.2}
\]

by dominated convergence, the integrand being bounded by \(2\|k\|_1=2\).

The positive stable density is smooth and unimodal, so \(k'\in L^1\). Differentiating C006.1 in the weak/absolutely continuous sense gives

\[
g_t'(y)
=
\int
k'\!\left(y-\frac{x}{s_t}\right)d\mu_\star(x),
\]
and the same translation argument yields

\[
\boxed{
\|g_t-k\|_{W^{1,1}(\mathbb R)}\longrightarrow0.
}
\tag{C006.3}
\]

Nevertheless C005 proves that **every** \(g_t\) is nonunimodal.

### Interpretation

The large-time scaling limit is the correct stable density, even in the stronger \(W^{1,1}\) topology, but unimodality is not stable under this convergence at a one-sided kernel.

The reason is geometric: the limiting positive stable density is identically zero on the entire negative half-line. Its derivative has no strictly positive left-tail margin there. An arbitrarily small amount of mass placed sufficiently far left can create a local derivative sign violation without being visible in the scaling limit.

Thus a proof strategy based only on convergence of the rescaled evolution to the stable law — even with first-derivative \(L^1\) control — cannot establish eventual unimodality. It would need a **uniform signed-tail margin** or another mechanism that rules out remote modes.

This is the precise failure found by Move 7.

# 7. Move 18 — translate the free branch into boundary/angular-derivative language and extend from alpha=1/2 to all positive alpha

## R19-I0084-C007 — the positive free-stable branch fails for every \(0<\alpha<1\)

**STATUS: PROVED INTERNALLY; new all-alpha extension awaits an independent audit.**

This generalizes the retained and independently audited alpha=1/2 free proof C002.

Use the same sparse measure from C002:

\[
A_n=2^{2^n},
\qquad
w_n=2^{-n}A_n^{-n},
\qquad
w_0=1-\sum_{n\ge1}w_n,
\]
\[
\boxed{
\mu_0=w_0\delta_0+\sum_{n\ge1}w_n\delta_{-A_n}.
}
\tag{C007.1}
\]

For every \(p>0\),

\[
\sum_{n\ge1}w_nA_n^p
=
\sum_{n\ge1}2^{-n}A_n^{p-n}<\infty,
\]
so

\[
\boxed{
\int |x|^p\,d\mu_0(x)<\infty
\quad\text{for all }p>0.
}
\tag{C007.2}
\]

Fix

\[
0<\alpha<1,\qquad t>0.
\]

Let \(T_t^{(\alpha,+)}\) be the positive free strictly alpha-stable semigroup, positivity parameter \(\rho=1\). Hasebe--Kuznetsov's principal-branch normalization gives

\[
\boxed{
\phi_{T_t}(z)
=
-t e^{i\pi\alpha}z^{1-\alpha}.
}
\tag{C007.3}
\]

Consider Huang--Wang's global inversion map for the free convolution

\[
\mu_0\boxplus T_t:
\qquad
H_t(z)
=
z+\phi_{T_t}(F_{\mu_0}(z)).
\tag{C007.4}
\]

### Step 1. A real boundary point with positive angular derivative

Put

\[
A=A_n,\qquad c_n=-A/2.
\]

For all large \(n\), \(A_{n-1}=\sqrt A\le A/4\), and \(w_0>3/4\).

Write

\[
G=G_{\mu_0},
\qquad
I_2(c)=\int\frac{d\mu_0(s)}{(c-s)^2}.
\]

At \(c=c_n\), the mass at \(0\) gives

\[
\frac{w_0}{c}< -\frac{3}{2A}.
\]

All atoms with index \(j<n\) also give negative contributions and may be discarded in an upper bound for \(G(c)\).

The own atom contributes at most

\[
\frac{w_n}{A/2}
=
\frac{2w_n}{A}
\le
\frac1{4A},
\]
since \(w_n\le w_1=1/8\).

For \(j>n\),

\[
A_j-A/2\ge A_j/2\ge A_{n+1}/2=A^2/2,
\]
so the whole farther-left positive tail contributes at most

\[
\frac{2}{A^2}\sum_{j>n}w_j
<
\frac{1}{4A}
\]
for large \(A\).

Therefore

\[
\boxed{
G(c_n)<-\frac1A.
}
\tag{C007.5}
\]

Set

\[
a_n:=-G(c_n)>\frac1A.
\tag{C007.6}
\]

For \(I_2(c_n)\), split the mass into \(j<n\), \(j=n\), \(j>n\).

For the base mass and all \(j<n\),

\[
|c_n+A_j|
=
A/2-A_j
\ge A/4,
\]
hence their total contribution is at most \(16/A^2\).

The own atom contributes at most \(4/A^2\).

The farther-left tail contributes at most \(4/A^4\).

Thus, for large \(n\),

\[
\boxed{
I_2(c_n)<\frac{21}{A^2}.
}
\tag{C007.7}
\]

Since

\[
F_{\mu_0}(c_n)=\frac1{G(c_n)}=-\frac1{a_n},
\]
the principal branch gives

\[
F_{\mu_0}(c_n)^{1-\alpha}
=
a_n^{\alpha-1}e^{i\pi(1-\alpha)}.
\]

Consequently

\[
\phi_{T_t}(F_{\mu_0}(c_n))
=
-t e^{i\pi\alpha}
a_n^{\alpha-1}e^{i\pi(1-\alpha)}
=
t a_n^{\alpha-1}\in\mathbb R.
\tag{C007.8}
\]

Also,

\[
F_{\mu_0}'(c_n)
=
\frac{I_2(c_n)}{a_n^2}.
\]

Differentiating C007.4 yields the real angular derivative

\[
\boxed{
H_t'(c_n)
=
1-
t(1-\alpha)
I_2(c_n)a_n^{\alpha-2}.
}
\tag{C007.9}
\]

Because \(\alpha-2<0\) and \(a_n>1/A\),

\[
a_n^{\alpha-2}
<
A^{2-\alpha}.
\]

Together with C007.7,

\[
H_t'(c_n)
>
1-21t(1-\alpha)A^{-\alpha}.
\tag{C007.10}
\]

Since \(A_n\to\infty\), choose \(n=n(t,\alpha)\) so large that

\[
21t(1-\alpha)A_n^{-\alpha}<1/2.
\]

Then

\[
\boxed{H_t'(c_n)>1/2.}
\tag{C007.11}
\]

The point \(c_n\) lies in the atom-free gap

\[
(-A_n,-A_{n-1}).
\]

On a sufficiently small open interval \(J_n\ni c_n\), the Cauchy transform remains negative and the same boundary expression varies continuously, so \(H_t'(x)>0\) for \(x\in J_n\).

Huang--Wang Proposition 3.2 identifies real points with nonnegative angular derivative as points in the zero-height boundary \(\mathbb R\setminus V_t\). Hence

\[
\boxed{J_n\subset\mathbb R\setminus V_t.}
\tag{C007.12}
\]

### Step 2. The output density is zero on an open interval

Huang--Wang Theorem 3.9 gives a continuous density version satisfying

\[
p_{\mu_0\boxplus T_t}(h_t(x))=0
\qquad
(x\in\mathbb R\setminus V_t).
\]

Since \(h_t\) is strictly increasing,

\[
\boxed{
p_{\mu_0\boxplus T_t}=0
\quad\text{on the nonempty open interval }h_t(J_n).
}
\tag{C007.13}
\]

### Step 3. There is strictly positive density on both sides

The flanking initial atoms are

\[
-A_n<c_n<-A_{n-1}.
\]

At an atom \(\beta\) of the initial measure, the only possible zero-boundary classification with \(F_{\mu_0}^*(\beta)=0\) is Huang--Wang type A. Remark 3.7 characterizes type A by

\[
\mu_0(\{\beta\})+T_t(\{s_{T_t}\})\ge1.
\]

The positive free stable law is absolutely continuous, hence atomless, and every atom of \(\mu_0\) has weight strictly less than one. Therefore the type-A inequality fails at both \(-A_n\) and \(-A_{n-1}\).

Thus both flanking atoms lie in \(V_t\). Theorem 3.9 gives strictly positive density at their \(h_t\)-images.

Since \(h_t\) is strictly increasing,

\[
h_t(-A_n)<h_t(J_n)<h_t(-A_{n-1}),
\]
so the output density has positive points on both sides of a nonempty open zero interval.

A unimodal probability density cannot have such a configuration. Therefore

\[
\boxed{
\mu_0\boxplus T_t^{(\alpha,+)}
\text{ is not unimodal for every }t>0,\quad 0<\alpha<1.
}
\tag{C007.14}
\]

Together with C007.2, this disproves the free branch of the conjecture throughout the entire positive/free-stable parameter range \(0<\alpha<1,\rho=1\).

### Scope

C007 is much stronger than the frozen half-stable metric, but it remains **PARTIAL as an all-parameter classification** of Conjecture 5.5:

- it covers the extreme positive skew \(\rho=1\);
- positive one-sided stable laws exist only for \(0<\alpha<1\);
- it does not classify symmetric/intermediate skewness or \(\alpha>1\).

It is nevertheless more than enough to refute the universal conjecture as stated.

# 8. What the three new-method moves taught us

## Move 6 — DEFORM TO A POINT YOU CAN SOLVE

Successful.

Instead of continuing the source's special Levy-kernel inequalities, I moved to a universal one-sided \(C^1\) kernel and an explicitly solvable superexponential sparse law. The mechanism is not special to stable densities: one-sided support shields all heavier right atoms, while the relative farther-left tail can be made arbitrarily small.

## Move 7 — TAKE THE LIMIT

Successful, but as an obstruction rather than a proof.

After stable rescaling, the entire nonunimodal evolution converges in \(W^{1,1}\) to the unimodal stable density. Hence a clean large-time scaling limit does **not** imply eventual unimodality. The missing ingredient is a uniform signed-tail margin, which a one-sided limiting density cannot have on its zero half-line.

## Move 18 — SAY IT IN ANOTHER LANGUAGE

Successful.

For free convolution, the gap mechanism becomes an angular-derivative/support-topology problem:

\[
H_t'(c)>0
\Longrightarrow
c\in\mathbb R\setminus V_t
\Longrightarrow
p(h_t(c))=0.
\]

This representation makes the alpha-dependence elementary. The alpha=1/2 square-root calculation from C002 becomes

\[
H_t'(c)
=
1-t(1-\alpha)I_2(c)(-G(c))^{\alpha-2},
\]

and the doubly-exponential gap makes the correction \(O(tA_n^{-\alpha})\). That extends the same mechanism to every \(0<\alpha<1\).

# 9. Prior-art/current-status check, 2026-09-16

Primary sources checked:

- Hasebe--Ueda, ALEA 15 (2018), version of record, DOI `10.30757/ALEA.v15-15`, especially Proposition 5.4 and Conjecture 5.5 on page 373;
- arXiv `1710.08240`;
- Hasebe--Kuznetsov, *On free stable distributions*, ECP 19 (2014), article 56, DOI `10.1214/ECP.v19-3443`;
- Huang--Wang, *Regularity results for free Lévy processes*, arXiv `2203.00421`, later Advances in Mathematics 402 (2022), 108323;
- Thomas Simon, *Positive stable densities and the bell-shape*, arXiv `1302.0956`.

Later-author/related check:

- Hasebe--Ueda--Wang, *Log-unimodality for free positive multiplicative Brownian motion*, arXiv `2009.13848` / Colloquium Mathematicum 169 (2022), is a distinct multiplicative problem and does not resolve Conjecture 5.5.

Bounded dated searches included:

- exact title + `Conjecture 5.5`;
- `1710.08240` + stable unimodality;
- `"positive free stable" unimodal convolution initial distribution`;
- `"free stable process" unimodal initial distribution`;
- `"strictly stable" "finite moment" unimodal free convolution`.

No accessible later primary-source resolution of Conjecture 5.5 surfaced. This is a bounded search, not a claim of worldwide bibliographic nonexistence.

The one-sided classical C004 mechanism appears to be different from the source's Proposition 5.4 mechanism. I found no prior source in this bounded search stating this universal sparse-tail obstruction with all exponential moments. Novelty therefore remains **UNVERIFIED**, not claimed.

# 10. Independent R20 audit now that a package is ready

Newest R20 package read:

`runs/R20/2026-09-16T14-49-00Z_i0100_p181_5d7a3c.md`.

Audit ID:

\[
\boxed{\texttt{R19-AUDIT-R20-I0100-P181-01}}
\]

Verdict:

\[
\boxed{\texttt{PASS\_EXACT\_FINITE\_CASE}.}
\]

I wrote an independent exact checker rather than calling R20's checker. It reconstructs:

1. the localized Paley nonedge representatives from modular arithmetic;
2. the degree-12 minimal polynomial of \(2\cos(2\pi/90)\);
3. the exact primal weights from normalization plus the 23 nonedge Fourier equations;
4. the exact dual multipliers from complementary-slackness equalities on the reported support;
5. exact algebraic positivity/nonnegativity via rational root-isolating intervals.

It independently recovered

\[
N=
[3,4,5,6,7,11,18,19,21,24,25,28,30,31,33,34,36,38,39,40,41,43,45],
\]

24 strictly positive primal weights, 46 exact zero dual slacks out of 90, and

\[
\boxed{
\vartheta(\overline{G_{181,1}})
=
9.324087759831998081273716499206167128041\ldots
}
\]

with matching exact primal/dual objectives.

This audits only the finite \(p=181\) certificate. It does **not** audit or prove R20's asymptotic Conjecture 26.

Artifacts:

- `artifacts/R19/2026-09-16_16-39-03_UTC__R20_i0100_p181_independent_audit.py`
- `artifacts/R19/2026-09-16_16-39-03_UTC__R20_i0100_p181_independent_audit.out`

Executed output SHA-256:

`48ae28a7709b84c8c412dbecf39b9002710ed06313a25b35b8d0ccf41ef86d4e`.

# 11. Model/scheduler interface and the inaccessible P26 task

The repository implementation records and the current exposed automation schema still agree:

- there is **no model selector field**;
- there is **no reasoning/thinking-effort selector field**;
- prompt, title, schedule/timing, enablement are exposed, but not runtime model configuration.

Therefore `GPT-6 / maximum` remains a prompt request only. This run actually reports GPT-5.6 Sol; reasoning effort is UNVERIFIED.

To guarantee GPT-6 at maximum, the platform would have to expose authorized model/reasoning fields on the scheduler/task, or an account/workspace administrator/platform support path with permission to set them. A prompt string cannot turn an unavailable configuration field into a runtime guarantee.

The current repository operations record that the P26 scheduler ID

`6aa7b43682948191b697d72fec69d539`

returned exactly:

`You cannot modify this task.`

The allowed workaround is **not** to create a duplicate task and not to bypass permissions. The task owner / correct workspace administrator / platform support must repair or expose access. Until then, P26's required audit remains pending. No schedule modification was attempted in this run.

# 12. Cumulative ledger

## PROVED / supported

- `R19-I0084-C001`: classical positive alpha=1/2 source counterexample with finite 5/2 moment; R18 audit PASS.
- `R19-I0084-C002`: free positive alpha=1/2 source counterexample under `boxplus`; R18 end-to-end audit now PASS.
- Source Conjecture 5.5 is mathematically refuted by either source-admissible alpha=1/2 counterexample; fleet closure still awaits P26.
- `R19-I0084-C004` NEW: one universal all-exponential-moment sparse law defeats every one-sided \(C^1\) kernel satisfying the mild negative-derivative/tail-derivative conditions, at every time.
- `R19-I0084-C005` NEW: the classical positive stable branch fails for every \(0<\alpha<1\), every \(t>0\), using one fixed \(\mu_\star\).
- `R19-I0084-C006` NEW: after stable rescaling, these nonunimodal densities converge in \(W^{1,1}\) to the unimodal stable density.
- `R19-I0084-C007` NEW: the free positive stable branch fails for every \(0<\alpha<1\), every \(t>0\), using one fixed all-polynomial-moment \(\mu_0\).
- `R19-AUDIT-R20-I0100-P181-01`: PASS_EXACT_FINITE_CASE.

## CORRECTED

- The actual version-of-record Conjecture 5.5 uses `mu*S_t` in the classical branch and `mu boxplus T_t` in the free branch.
- The root intake extraction loses this `S_t/T_t` and `*/boxplus` distinction. The source PDF controls.
- For robustness, C005.3 separately handles the literal classical-convolution/free-stable-density interpretation.

## OPEN / pending

- P26 independent source/closure audit for I0084.
- Independent audit of the new all-alpha extensions C004--C007.
- Full classification across all \(\alpha\in(0,2)\) and all stable skewness parameters. The positive \(0<\alpha<1,\rho=1\) theorem is still PARTIAL relative to that larger parameter-classification question.
- Paper folder is not created before the required P26 audit.

# 13. Failed routes / exact obstructions retained

1. The source's original alpha=1/2 sparse construction cannot reach the 5/2 moment; the authors prove that limitation for their condition (5.36).
2. Large-time stable scaling is not enough: C006 gives \(W^{1,1}\) convergence to a unimodal density while every finite-time density is nonunimodal.
3. The intake/OCR notation cannot be trusted for the classical/free operation; version-of-record source normalization is mandatory.
4. A half-stable or positive-skew theorem, even one valid for every \(0<\alpha<1\), does not classify all stable indices/skewnesses.

# 14. Next obligation

The mathematical source statement is already refuted and the fixed metric is saturated. The highest-value next action is therefore closure hardening rather than another half-stable lemma:

1. obtain the required P26 end-to-end source/scope/proof audit;
2. ask a distinct track to audit the new all-positive-alpha C004/C007 extensions if those stronger results are to enter a paper;
3. after the P26 source-level PASS, create the required self-contained paper folder comparing exactly:
   - source Conjecture 5.5;
   - classical counterexample;
   - free counterexample;
   - strengthened positive-index range;
   - the OCR/source-normalization correction.

If P26 remains inaccessible, preserve this report and continue without bypassing the permission boundary.

# 15. Structured ledger delta

```yaml
ledger_delta:
  track: R19
  source: "T. Hasebe and Y. Ueda, ALEA 15 (2018), Conjecture 5.5 / arXiv:1710.08240 / intake I0084"
  target: "eventual unimodality under finite (2+alpha)-moment; frozen positive alpha=1/2 classical/free source branches"
  metric: "number of the two frozen positive alpha=1/2 source branches decided in the source quantifier class"
  before: "2/2"
  after: "2/2"
  movement: "no movement"
  unchanged_count: 1
  status: "SOURCE_REFUTED_MATHEMATICALLY__FLEET_CLOSURE_PENDING_P26"
  tried_moves: [6, 7, 18]
  source_scope_correction:
    version_of_record: "mu*S_t for classical stable; mu boxplus T_t for free stable"
    intake_issue: "lossy extraction collapses S_t/T_t and */boxplus distinction"
  new_exact_results:
    - "C004: universal one-sided-kernel sparse-tail obstruction, all exponential moments"
    - "C005: classical positive stable branch refuted for every 0<alpha<1 and every t>0"
    - "C006: W^{1,1} stable-scaling convergence does not preserve unimodality"
    - "C007: free positive stable branch refuted for every 0<alpha<1 and every t>0"
  audit_ids:
    classical_half: "R18-I0084-C001=PASS"
    free_half: "R18-AUDIT-R19-I0084-C002-ENDTOEND-001=PASS_FULL_MATHEMATICAL_PROOF"
    p26: "PENDING_NOT_LOCATED"
    r20_outgoing: "R19-AUDIT-R20-I0100-P181-01=PASS_EXACT_FINITE_CASE"
  exact_evidence:
    - "artifacts/R19/2026-09-16_16-39-03_UTC__R20_i0100_p181_independent_audit.py"
    - "artifacts/R19/2026-09-16_16-39-03_UTC__R20_i0100_p181_independent_audit.out"
  remaining_obligation: "P26 end-to-end I0084 source/scope/proof audit; then paper packaging"
```
