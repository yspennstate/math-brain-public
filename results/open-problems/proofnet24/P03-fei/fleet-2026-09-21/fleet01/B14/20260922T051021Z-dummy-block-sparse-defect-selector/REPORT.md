# B14 — a physical dummy-block selector pays the sparse balanced-pair Fourier-dust obstruction

**Classification:** `AUXILIARY_ONLY / SPARSE-DEFECT-OBSTRUCTION-PAID`.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; authenticated repository sources were read directly, but no installed/native brain retrieval or receiver-context mechanism entered the mathematics.

## 0. Stable candidate and exact remaining target

This run binds to the stable candidate `LIMIT-PRIME-GATE-LIFT-v1` from

`proofnet24/P03-fei/fleet-2026-09-21/fleet01/B18/20260922T0222Z-shared-graft-tail/REPORT.md`.

Write

\[
C_*=6.5218512,\qquad a_*=0.2682048,
\qquad
\Gamma_*(p)=\Gamma_{\rm RO}(p)+a_*p(1-p).
\]

For a Boolean gate `G` at product bias `p`, let

\[
D_*(G;p):=D_{\Gamma_*}(G;p).
\]

The target-level missing implication is still

\[
\boxed{D_*(P;p)\ge0}
\]

for every finite-arity composition-prime Boolean gate `P` and every interior product bias. The already-proved gate-composition cocycle then propagates the inequality to all gates, and the all-gate reformulation gives `H(f)<=C_* I(f)` on the uniform cube.

This report does **not** prove that universal statement.

## 1. Two exact peer results consumed and applied

### 1.1 Corrected random-depth criterion

I consumed the fresh fleet02/B18 handoff


whose scientific source is

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B18/20260922T051105Z-random-depth-barycenter/REPORT.md`, creation commit `3f228a8a91559bbc354d207baf74d6c88a68996f`.

It corrects an important point: allowing the random restriction depth `r=n-1` in an existential selector is tautological, because all children are constants/literals and the block residual is exactly the full parent target. Therefore a useful restriction theorem must exhibit a **genuinely nonterminal physical block** or an amortized multigeneration payment.

The selector below does exactly that on a named adversarial family: the block is the physical dummy-tag block and leaves the original `r` source coordinates alive.

### 1.2 Sparse balanced-pair Fourier-dust theorem

I also consume fleet02/B17

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B17/20260922T044637Z-radius2-dust-compensation/REPORT.md`.

Its Theorem 5.1 is source-exact. Let

\[
f:\{0,1\}^r\to\{\pm1\}
\]

be balanced, choose `a,b` with `f(a)=+1,f(b)=-1`, extend by `m` dummy coordinates,

\[
F_m(x,y)=f(x),
\]

and flip exactly

\[
u=(a,0^m),\qquad v=(b,e_1)
\]

to obtain `g_m`. Put `n=r+m` and

\[
q_m=2^{2-n}=2^{2-r-m}.
\]

The peer theorem proves

\[
H(g_m)-H(f)=4nq_m+O_{f,a,b}(q_m),
\]
\[
I(g_m)-I(f)=nq_m+O_{f,a,b}(q_m),
\]

hence, because both `f` and `g_m` are balanced,

\[
\boxed{
D_*(g_m)-D_*(f)
=(C_*-4)nq_m+O_{f,a,b}(q_m).
}
\tag{1.1}
\]

The new result below converts this global compensation into an **actual realizable block selector**.

## 2. Exact physical policy

Let

\[
Y=\{y_1,\ldots,y_m\}
\]

be the dummy-tag coordinates and choose the single physical block

\[
\boxed{T=Y.}
\tag{2.1}
\]

This is proper and nonempty whenever `m>=1` and `r>=1`; it leaves all original source coordinates alive. No affine coordinate change, component label, or auxiliary selector bit is introduced.

Let `f^a` denote the source `f` with only the value at `a` flipped, and similarly `f^b`. Conditioning on the physical tag block gives exactly

\[
(g_m)_{Y=y}=\begin{cases}
f^a,&y=0^m,\\
f^b,&y=e_1,\\
f,&\text{otherwise}.\end{cases}
\tag{2.2}
\]

Therefore the full stable-candidate child defect is

\[
\boxed{
\mathbb E_YD_*((g_m)_{Y})
=(1-2^{1-m})D_*(f)
+2^{-m}\bigl(D_*(f^a)+D_*(f^b)\bigr).
}
\tag{2.3}
\]

Here `D_*` on the unbalanced one-point-flip children means the **full gate defect** with uniform input biases; no replacement by the balanced formula is made.

Define the fixed child debit

\[
K_{f,a,b}:=D_*(f^a)+D_*(f^b)-2D_*(f).
\tag{2.4}
\]

Then the block residual is exactly

\[
\boxed{
\mathcal R_m
:=D_*(g_m)-\mathbb E_YD_*((g_m)_Y)
=\bigl[D_*(g_m)-D_*(f)\bigr]-2^{-m}K_{f,a,b}.
}
\tag{2.5}

This is the quantity required by restriction induction; no child slack is discarded.

## 3. New theorem: the dummy block eventually pays every fixed sparse balanced-pair defect

### Theorem 3.1

For every fixed balanced Boolean source `f`, every opposite-sign pair `a,b`, and the family `g_m` above,

\[
\boxed{
\lim_{m\to\infty}
\frac{2^m}{m}\,\mathcal R_m
=2^{2-r}(C_*-4)>0.
}
\tag{3.1}

Consequently there is a finite `m_0(f,a,b)` such that for every `m>=m_0`,

\[
\boxed{
D_*(g_m)\ge\mathbb E_YD_*((g_m)_Y).
}
\tag{3.2}

Thus the explicit proper physical block `T=Y` is a paid selector on the entire sufficiently diluted tail of the sparse balanced-pair obstruction.

### Proof

By (1.1), there exist finite `A=A(f,a,b)` and `m_1` such that for `m>=m_1`,

\[
\left|
D_*(g_m)-D_*(f)-(C_*-4)(r+m)q_m
\right|
\le A q_m.
\tag{3.3}

Insert `q_m=2^{2-r}2^{-m}` into (2.5). Then

\[
\mathcal R_m
=2^{-m}\Bigl[
2^{2-r}(C_*-4)(r+m)
+O_{f,a,b}(2^{2-r})
-K_{f,a,b}
\Bigr].
\tag{3.4}

After multiplication by `2^m/m`, the fixed terms vanish and the coefficient of `m` remains, giving (3.1).

For an explicit sufficient threshold, any `A,m_1` satisfying (3.3) gives

\[
\mathcal R_m\ge
2^{-m}\left[
2^{2-r}\bigl((C_*-4)(r+m)-A\bigr)
-|K_{f,a,b}|
\right].
\tag{3.5}

Hence (3.2) holds whenever `m>=m_1` and

\[
\boxed{
 m>
 \frac{A}{C_*-4}
 +\frac{2^{r-2}|K_{f,a,b}|}{C_*-4}
 -r.
}
\tag{3.6}

Every quantity in (3.6) is attached to the fixed finite source/children; no dimension-dependent universal constant is being smuggled into the FEI statement. `square`

### Restriction-induction consequence

If the three fixed `r`-dimensional children `f,f^a,f^b` have already been paid by the induction, then (3.2) immediately pays `g_m` for every sufficiently large `m`. In particular, the large local debit that motivated the sparse-defect adversary cannot be recycled indefinitely through dummy dilution: the `m q_m` root compensation eventually dominates the fixed `2^{-m}` branch debit.

## 4. Exact all-m corollary for the canonical literal seed

The simplest member is completely explicit and requires no asymptotics.

Take `r=1`, let `f` be a literal, and choose its two opposite-sign inputs as `a,b`. Then both special children `f^a,f^b` are constants, while every other child is the literal. Therefore

\[
D_*(f)=D_*(f^a)=D_*(f^b)=0,
\]

and the dummy-block residual is exactly the parent defect.

Let `n=m+1` and `q=2^{2-n}`. Directly from the signed coefficient formula in the peer theorem, the spectrum has one heavy coefficient of squared mass `(1-q)^2` and

\[
N=2^{n-1}-1
\]

equal dust atoms of mass `q^2`. Consequently

\[
\boxed{I(g_m)-1=(n-2)q,}
\tag{4.1}

and, writing `d=Nq^2=2q-q^2`,

\[
\boxed{H(g_m)=h_2(d)+d\log_2N.}
\tag{4.2}

For `n=2`, `g_m` is itself a literal and both sides vanish. For `n=3,4`, the support bound gives

\[
H(g_m)\le n-1\le 6(n-2)q.
\]

For `n>=5`, `d<=2q`, `d>=q`, and

\[
h_2(d)
\le d\log_2(1/d)+\frac d{\ln2}
\le2q(n-2)+\frac{2q}{\ln2},
\]

while

\[
d\log_2N<2q(n-1).
\]

Therefore

\[
H(g_m)
<2q\left(2n-3+\frac1{\ln2}\right)
\le6(n-2)q
=6\,[I(g_m)-1].
\tag{4.3}

The last inequality holds for every integer `n>=5` because `n>=3+1/ln 2`. Since `C_*=6.5218512>6`,

\[
\boxed{
D_*(g_m)
=C_*[I(g_m)-1]-H(g_m)
\ge(C_*-6)[I(g_m)-1]
\ge0
}
\tag{4.4}

for **every** `m>=1`, with strict positivity once `n>=3`.

Thus in the canonical sparse-pair defect built over a literal, the actual block `T=Y` pays at every dilution depth, not merely asymptotically.

## 5. Why this is not a universal proof

This run deliberately attacks one of the owner's required source-valid obstruction families before adding more selector machinery.

- **Sparse balanced pair defects:** paid by Theorem 3.1; the literal-seed case is paid for every depth by Section 4.
- **Dummy variables without a defect:** the same block has zero residual, as it should; no artificial gain is created.
- **Addressing, majority, tribes:** these do not have the fixed finite special-tag branch structure (2.2), so Theorem 3.1 does not apply.
- **Tensor replication:** the theorem does not assert that an arbitrary tensor-critical core contains a paid dummy block; decomposable gate compositions remain governed by the exact gate cocycle.
- **Biased limits:** the theorem is for the uniform tag block and does not establish the full interior-bias prime-gate inequality.

So the new theorem removes a genuine sparse-defect obstruction to the restriction policy, but it does not supply the missing universal coverage theorem.

## 6. Old/new missing implication

**Old target-level missing implication:** prove `LIMIT-PRIME-GATE-LIFT-v1`, equivalently find a valid nonterminal block/amortized payment on every remaining prime gate or construct a prime/bias counterexample.

**Fresh peer correction applied:** the random-depth existential criterion cannot count `r=n-1`; that terminal choice is exactly the original target.

**New proved inference:** on the genuine balanced sparse-pair Fourier-dust family, the explicit **nonterminal physical dummy-tag block** has residual

\[
\mathcal R_m
=2^{-m}\bigl[2^{2-r}(C_*-4)m+O_{f,a,b}(1)\bigr],
\]

so it is strictly paid for all sufficiently large dilution, while the literal-seed subfamily is paid for every `m`.

**Remaining universal implication:** derive an analogous paid block or two-generation compensation from intrinsic structure of an arbitrary composition-prime Boolean gate. The next useful target is not another terminal-depth existential statement; it must control genuine interior scales and retain child slack/information credits.

**Classification:** `AUXILIARY_ONLY`. The result decisively eliminates one named obstruction family for the actual selector mechanism, but does not prove the universal prime-gate inequality.

## 7. Scope and privacy

Only FEI mathematics, logical account/slot labels, repository-relative source paths, public mathematical constants and sanitized proof metadata are present. No credentials, scheduler identifiers, machine paths, unrelated private data, email/Drive action, public posting, paid/remote compute, workflow dispatch or permission change is included.
