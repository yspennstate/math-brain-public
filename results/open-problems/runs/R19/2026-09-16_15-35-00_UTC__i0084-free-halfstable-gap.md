Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — the scheduler exposes no model selector or reasoning selector, so GPT-6 / maximum was requested but was not verified and is not claimed.

Problem/source: Takahiro Hasebe and Yuki Ueda, *Large time unimodality for classical and free Brownian motions with initial distributions* (ALEA 2018; arXiv:1710.08240), Conjecture 5.5 / intake I0084.

Metric: **1/2 -> 2/2** of the two frozen positive alpha=1/2 classical/free universal source cases decided. Both are decided **negatively** by source-admissible finite-5/2-moment initial measures. Mathematical consequence: Conjecture 5.5 is false as stated. Portfolio/closure status remains **PARTIAL / AUDIT PENDING**: this is a half-stable refutation, not an all-alpha classification, and the new free claim has not yet received the two required independent other-track audits. Unchanged-run count resets to **0**.

# R19 / I0084 — free positive half-stable sparse-gap counterexample

Run ID: `2026-09-16_15-35-00_UTC__i0084-free-halfstable-gap`  
Repository: `yspennstate/math-open-problems`, branch `master`.

## 1. Repository continuity and recovered state

I continued from the newest completed R19 report rather than restarting:

- `runs/R19/2026-09-16_13-40-24_UTC__i0084-halfstable-lefttail.md`.

That report proved the **classical positive alpha=1/2** source claim false and moved the frozen metric from UNMEASURED to 1/2.  Its claim `R19-I0084-C001` uses an admissible initial law with finite 5/2 moment and shows `mu * L_t` is nonunimodal for every `t>0`.

I also recovered two later R19 artifacts which had been committed without an immutable run report:

- `artifacts/R19/2026-09-16_15-02-00_UTC__i0084_free_halfstable_checker.py`;
- `artifacts/R19/2026-09-16_15-05-29_UTC__i0084_free_halfstable_sparse_gap_checker.py` and its output.

The latter explicitly says it was intended for a free positive alpha=1/2 sparse-gap counterexample and cites Huang--Wang (2022), but no corresponding report exists under `runs/R19/`.  I therefore did **not** treat that orphan artifact as a completed theorem.  I reconstructed the argument from the primary analytic machinery, simplified the constants, adversarially checked the support-gap step, and wrote the full proof below.

Required fleet files read this invocation include `README.md`, `proofnet24/HOURLY20_PROTOCOL_2026-09-16.md`, `probability_campaign_2026_09/INDEX.md`, `probability_campaign_2026_09/RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/FLEET_2026-09-16.md`, and `operations/RFLEET_2026-09-16.md`.  Repository search recovered the exact I0084 intake row and current ownership.  The connector does not provide a practical semantic line-by-line read of every roughly 780-row intake mirror in one invocation; I do not claim such a read.  The target-specific intake row, ownership, prior R19 state, neighboring R18 material, and current R20 packages were recovered.

The old R19 free-group-factor assignment remains retired with its preserved handoff; no work on that personal/old target was resumed:

`proofnet24/R19-free-group-factors/runs/2026-09-16/2026-09-16_13-04-33_UTC__R19__free-shift-tor-obstruction__report.md`.

No root shared ledger was edited; P26 remains the shared-ledger writer.

## 2. Exact source scope and conventions

The version-of-record source was rechecked on 2026-09-16.  Conjecture 5.5 states:

> If `S_t` (respectively `T_t`) is the law at time `t>0` of a classical (respectively free) strictly stable process of index `alpha in (0,2)`, and the initial probability measure `mu` satisfies `int |x|^(2+alpha) dmu < infinity`, then `mu * S_t` (respectively `mu boxplus T_t`) is unimodal for all sufficiently large `t`.

Important scope points:

1. `*` is ordinary classical convolution and `boxplus` is additive free convolution.
2. Conjecture 5.5 itself imposes **no symmetry or skewness restriction** on the stable process.  Hence an extreme-skew positive alpha=1/2 stable process is source-admissible.
3. Section 5.2 of the source treats the classical positive alpha=1/2 Levy law
   \[
   L_t(dx)=\frac{t}{\sqrt{2\pi}}e^{-t^2/(2x)}x^{-3/2}{\bf 1}_{(0,\infty)}(x)\,dx.
   \]
4. The source definition of unimodality is: there exist a mode `a` and a nonnegative density `f`, nondecreasing on `(-infinity,a)` and nonincreasing on `(a,infinity)`, such that the measure is `mu({a}) delta_a + f(x)dx`.
5. At `alpha=1/2` the moment hypothesis is exactly finite `5/2` moment.

For the free positive half-stable process I use the standard Hasebe--Kuznetsov positive free stable law `nu_{alpha,rho}`.  Their positivity parameter satisfies `P(X_{alpha,rho}>0)=rho`, and
\[
\phi_{\alpha,\rho}(z)=-e^{i\pi\alpha\rho}z^{1-\alpha},\qquad 0<\alpha<1.
\]
Thus for `alpha=1/2, rho=1`,
\[
\boxed{\phi_{T_1}(z)=-i\sqrt z}
\tag{2.1}
\]
with the principal square root.  Set
\[
T_t=T_1^{\boxplus t};
\]
then
\[
\boxed{\phi_{T_t}(z)=-it\sqrt z.}
\tag{2.2}
\]
This is a positive free strictly 1/2-stable convolution semigroup.  Hasebe--Kuznetsov also prove the free stable laws are absolutely continuous with smooth densities, so `T_t` is atomless.

## 3. Dated current-status / prior-art check

Date: **2026-09-16**.

Primary sources checked directly:

- Hasebe--Ueda, ALEA 15 (2018), Conjecture 5.5 and Proposition 5.4;
- Hasebe--Kuznetsov, *On free stable distributions*, ECP 19 (2014), for the positive free stable parameterization and Voiculescu transform;
- Huang--Wang, *Regularity results for free Levy processes*, arXiv:2203.00421, especially Proposition 3.1, Proposition 3.2, Theorem 3.6 / Remark 3.7 and Theorem 3.9.

Bounded fresh searches included:

- exact phrase `"Conjecture 5.5" Hasebe Ueda unimodal`;
- `finite 2+alpha free stable unimodal convolution`;
- `Large time unimodality Conjecture 5.5`;
- `positive free stable unimodality initial distribution`;
- `1710.08240 stable unimodality`.

The searches recovered the original paper, the authors' later multiplicative-unimodality work, Hasebe--Kuznetsov and Huang--Wang, but no primary-source paper claiming a resolution of Conjecture 5.5 or the finite-(2+alpha)-moment free positive half-stable case.  This is a dated bounded search, not a claim of bibliographic omniscience.

Huang--Wang provide the global inversion/support machinery used below; they do not state the counterexample proved here.

## 4. Retained classical result

### R19-I0084-C001 — classical positive half-stable case

**STATUS: PROVED internally; one independent R18 finite/symbolic audit PASS; P26 audit pending.**

The previous immutable report constructed
\[
\mu_{\rm cl}=Z^{-1}\sum_{n\ge1}2^{-n^2}\,\delta_{-2^n}
\]
with every finite polynomial moment, and proved that `mu_cl * L_t` is nonunimodal for every `t>0`.  The exact derivative sign pattern is produced by one-sided support shielding of the positive Levy kernel.

R18 independently audited its finite/symbolic core and recorded PASS at

`artifacts/R18/2026-09-16_14-28-50_UTC__R18__r19-i0084-independent-audit-output.txt`

(blob `476ce76449eb1ffa32e7811eb47567b901e4832a`).

I do not rederive C001 here.

## 5. New free counterexample

### R19-I0084-C002 — free positive alpha=1/2 case

**STATUS: PROVED INTERNALLY / INDEPENDENT AUDITS PENDING.**

There exists a probability measure `mu_0` with finite moments of **every positive order** such that
\[
\boxed{\mu_0\boxplus T_t\text{ is not unimodal for every }t>0,}
\tag{5.1}
\]
where `T_t` is the standard positive free strictly stable semigroup of index `1/2` from (2.2).

This refutes the free positive alpha=1/2 specialization of Conjecture 5.5 even under a much stronger initial-tail assumption than finite 5/2 moment.

### 5.1 Sparse initial law and moments

Define
\[
A_n=2^{2^n},\qquad
w_n=2^{-n}A_n^{-n}\quad(n\ge1),
\tag{5.2}
\]
put
\[
W=\sum_{n\ge1}w_n,\qquad w_0=1-W,
\]
and set
\[
\boxed{
\mu_0=w_0\delta_0+\sum_{n\ge1}w_n\delta_{-A_n}.
}
\tag{5.3}
\]

First, `w_1=1/8`.  For `n>=2`, since `A_n>=16`,
\[
w_n=2^{-n}A_n^{-n}\le 2^{-5n}=32^{-n}.
\]
Hence
\[
W<\frac18+\sum_{n\ge2}32^{-n}
=\frac18+\frac1{992}<\frac14,
\tag{5.4}
\]
so
\[
w_0>\frac34.
\tag{5.5}
\]

For the critical source moment,
\[
\int |x|^{5/2}\,d\mu_0(x)
=
\sum_{n\ge1}2^{-n}A_n^{5/2-n}.
\tag{5.6}
\]
The `n=1,2` terms are finite, while for `n>=3`,
\[
5/2-n\le-1/2,
\]
so the tail is bounded by
\[
\sum_{n\ge3}2^{-n}A_n^{-1/2}
=
\sum_{n\ge3}2^{-n-2^{n-1}}<\infty.
\tag{5.7}
\]
The same argument with `5/2` replaced by any fixed `p>0` shows that `mu_0` has every finite polynomial moment.

### 5.2 Huang--Wang subordination setup

Write
\[
G(z)=G_{\mu_0}(z),\qquad F(z)=1/G(z).
\]
For the free convolution `T_t boxplus mu_0`, Huang--Wang use
\[
\boxed{
H_t(z)=z+\phi_{T_t}(F(z))
=z-it\sqrt{F(z)}.
}
\tag{5.8}
\]
Their global inversion theorem associates:

- an open set `V_t subset R`;
- a continuous boundary-height function `f_t` with `V_t={x:f_t(x)>0}`;
- a strictly increasing homeomorphism `h_t:R->R`.

Their Theorem 3.9 gives a continuous version `p_t` of the absolutely continuous density satisfying
\[
p_t(h_t(x))>0\quad(x\in V_t),
\qquad
p_t(h_t(x))=0\quad(x\in\mathbb R\setminus V_t).
\tag{5.9}
\]
Proposition 3.2 characterizes `x in R\V_t` by the existence of a nonnegative angular derivative `H_t'(x)`.

### 5.3 A real zero-density interval for every t

Fix arbitrary `t>0`.  Choose `n>=2` so large that
\[
\sqrt{A_n}>9t.
\tag{5.10}
\]
This is possible because `A_n` is doubly exponential.  Put
\[
A=A_n,\qquad c_n=-A/2.
\]
Since
\[
A_{n-1}=\sqrt A\le A/4,
\]
we have
\[
-A_n<c_n<-A_{n-1}.
\tag{5.11}
\]

At `c_n`,
\[
G(c_n)
=-\frac{2w_0}{A}
+\sum_{k<n}\frac{w_k}{A_k-A/2}
+\sum_{k\ge n}\frac{w_k}{A_k-A/2}.
\tag{5.12}
\]
The middle sum is nonpositive.  For `k>=n`, `A_k-A/2>=A/2`, hence by (5.4)--(5.5),
\[
G(c_n)
< -\frac{3}{2A}+\frac{2W}{A}
< -\frac1A.
\tag{5.13}
\]
Set
\[
a_n:=-G(c_n)>1/A.
\tag{5.14}
\]

Also define
\[
I_2(c_n):=\int\frac{d\mu_0(s)}{(c_n-s)^2}=-G'(c_n).
\]
The atom at `0` contributes at most `4/A^2`.  For `k<n`,
\[
|c_n+A_k|=A/2-A_k\ge A/4,
\]
so all such atoms contribute less than
\[
\frac{16W}{A^2}<\frac4{A^2}.
\]
For `k>=n`, `|c_n+A_k|>=A/2`, so their total contribution is less than
\[
\frac{4W}{A^2}<\frac1{A^2}.
\]
Consequently
\[
\boxed{I_2(c_n)<\frac9{A^2}.}
\tag{5.15}
\]

Because `G(c_n)<0`,
\[
F(c_n)=-1/a_n.
\]
The principal square root has upper-half-plane boundary value
\[
\sqrt{F(c_n)}=\frac{i}{\sqrt{a_n}}.
\]
Moreover
\[
F'(c_n)=\frac{I_2(c_n)}{a_n^2}.
\]
Differentiating (5.8) angularly therefore gives the real number
\[
\boxed{
H_t'(c_n)
=1-\frac{t I_2(c_n)}{2a_n^{3/2}}.
}
\tag{5.16}
\]
Using (5.14)--(5.15),
\[
H_t'(c_n)
>
1-\frac{9t}{2\sqrt A}
>
\frac12.
\tag{5.17}
\]
Thus Proposition 3.2 puts `c_n` in `R\V_t`.

A single point would not be enough: Huang--Wang exhibit isolated zero-density points in other free convolutions.  Here the inequalities are strict.  On the atom-free gap `(-A_n,-A_{n-1})`, the functions `G`, `I_2`, and the real boundary expression (5.16) vary continuously wherever `G<0`.  Therefore there exists an open interval
\[
J_n\ni c_n,\qquad
J_n\Subset(-A_n,-A_{n-1}),
\tag{5.18}
\]
on which
\[
G(x)<0,\qquad H_t'(x)>0.
\]
Applying Proposition 3.2 pointwise,
\[
\boxed{J_n\subset\mathbb R\setminus V_t.}
\tag{5.19}
\]
Thus by (5.9), `p_t` vanishes on the nonempty open interval `h_t(J_n)`.

### 5.4 Positive density on both sides of the gap

It remains to rule out the possibility that this is merely outside a one-sided support.

The initial atoms `-A_n` and `-A_{n-1}` both belong to `V_t`.
Indeed, at an atom `alpha=-A_j`,
\[
F_{\mu_0}^*(\alpha)=0,
\qquad |G_{\mu_0}(\alpha+i\varepsilon)|\to\infty.
\]
So in Huang--Wang Theorem 3.6 the only possible boundary type is type A.  Their Remark 3.7 characterizes type A by
\[
\mu_0(\{\alpha\})+T_t(\{s_{T_t}\})\ge1.
\tag{5.20}
\]
The positive free stable law `T_t` is atomless, while every `w_j<1`; hence (5.20) fails.  Therefore `alpha` is not in `R\V_t`, so
\[
-A_n,-A_{n-1}\in V_t.
\tag{5.21}
\]
By Theorem 3.9,
\[
p_t(h_t(-A_n))>0,
\qquad
p_t(h_t(-A_{n-1}))>0.
\tag{5.22}
\]
Since `h_t` is strictly increasing and
\[
-A_n<J_n<-A_{n-1},
\]
the open interval `h_t(J_n)` of zero density lies strictly between two points of positive density.

### 5.5 Nonunimodality

A unimodal measure in the source sense cannot have a nonempty open interval on which its density is zero lying strictly between two points where its density is positive.  If the mode is to the left, to the right, or inside that interval, one of the required monotonicity conditions is immediately violated.  An atom at the mode cannot repair the violation.

Equations (5.19) and (5.22) therefore imply
\[
\mu_0\boxplus T_t\text{ is not unimodal}.
\]
Since `t>0` was arbitrary, (5.1) follows.

This completes the internal proof of C002.

## 6. Exact finite/symbolic certificate

The run-specific deterministic checker is

`artifacts/R19/2026-09-16_15-35-00_UTC__i0084_free_halfstable_gap_checker.py`

created at commit

`88042774bec5c8b980d39cc291f4011e6261d8d2`

and read back at that exact commit.

Executed output:

`artifacts/R19/2026-09-16_15-35-00_UTC__i0084_free_halfstable_gap_checker_output.txt`

created at commit

`83dbb9c23ce7199d5df511a121e21c118e1cc29b`

and read back at that exact commit.

The checker verifies exactly:

1. `W < 1/8 + 1/992 < 1/4`, hence `w_0>3/4`;
2. the critical `5/2-n <= -1/2` exponent;
3. the derivative constants `I_2<9/A^2` and `sqrt(A)>9t => H_t'>1/2`;
4. `A_{n-1}=sqrt(A_n)<=A_n/4` on a finite exact sanity core;
5. `phi_{1/2,1}(z)` has coefficient `-i` in the Hasebe--Kuznetsov normalization;
6. the independent R20 p=41 theta certificate described below.

Local checker SHA-256:

`3fb065e00ce28011c0b7715c17197a875f80271420f90c83c0886467c32a7428`.

Output SHA-256:

`d2b7ca4b12bdbf8f7f6acb5e3990ae3227e06abcfba2c2665f87c563df52b1e1`.

The infinite support/subordination argument is proved on the page; the finite checker is not presented as a substitute for Huang--Wang's theorems.

## 7. Adversarial checks and failed routes

### X0084-01 — one boundary point is not enough

A first version of the free route tried to prove only `c_n in R\V_t`.  That does **not** by itself yield a support gap: Huang--Wang give examples where a boundary point is an isolated zero of the density inside its support.  The current proof repairs this by retaining strict inequalities and obtaining an **open interval** `J_n subset R\V_t` by continuity.

### X0084-02 — approximate relation to classical one-sided shielding is invalid

The classical Levy density has literal one-sided support, so remote atoms can be shielded pointwise.  Free convolution has no comparable termwise convolution formula.  The free proof instead uses the exact subordination map and global-inversion support set `V_t`; no classical shielding identity is imported.

### X0084-03 — an output support gap must have mass on both sides

A zero-density interval could lie outside a connected one-sided support.  The proof therefore explicitly shows the two flanking initial atoms are in `V_t`, and Theorem 3.9 gives positive output density at their `h_t`-images.

### Recovered orphan route

The unreported 15:05 R19 artifact used a more complicated collection of auxiliary scales `B_n` and constants.  Nothing in that artifact is silently promoted.  The present proof replaces it by the simpler exact estimates
\[
-G(c_n)>1/A_n,
\qquad
I_2(c_n)<9/A_n^2,
\]
which are sufficient.

## 8. Source-level consequence and exact parameter scope

The frozen positive half-stable metric is now complete:

- **classical positive alpha=1/2**: universal eventual-unimodality claim is false; retained C001 gives an admissible finite-5/2-moment initial measure for which nonunimodality persists for every `t>0`;
- **free positive alpha=1/2**: universal eventual-unimodality claim is false; new C002 gives an initial measure with every polynomial moment for which nonunimodality persists for every `t>0` for the standard positive free strictly 1/2-stable semigroup `phi_t(z)=-it sqrt(z)`.

Thus the fixed metric moves
\[
\boxed{1/2\longrightarrow2/2.}
\]

Logically, either counterexample already makes Conjecture 5.5 false **as stated**, because the conjecture quantifies over all `alpha in (0,2)` and all admissible initial measures.  Nevertheless, this work is only a half-stable result and does **not** classify what happens for other alpha/skewness values.  Under the repository closure rules the package remains PARTIAL/AUDIT_PENDING until the required independent audits are complete.

The theorem is stable under positive deterministic rescaling of the chosen free stable process: if the normalization is `phi_t(z)=-i gamma t sqrt(z)` with fixed `gamma>0`, the proof changes only (5.10) to `sqrt(A_n)>9 gamma t`.  No translation drift is added; the process used is strictly stable.

## 9. Independent R20 audit

The current R20 track is Afonso Bandeira, Randomstrasse 101 (2025), Conjecture 26 / I0100.  Two R20 packages are present; the newer one advances the finite exact metric to `p=181` but is a much larger degree-12 number-field certificate.

This run completes a claim-scoped independent exact audit of the earlier `p=41` package:

**Audit ID:** `R19-AUDIT-R20-I0100-P41-01`  
**STATUS: PASS.**

I independently rebuilt the `p=41` symmetry-reduced primal/dual certificate in exact radicals.  The checker verifies:

- localized complement reduced classes `[1,2,3,6,8]`;
- exact primal normalization and nonnegativity;
- all five complement Fourier equalities;
- exact dual nonnegative slacks;
- matching objective
  \[
  \vartheta(\overline{G_{41,1}})=2\sqrt5.
  \]

The exact slack set is
\[
\{0,1,\sqrt5/4,\sqrt5/4-1/2\}.
\]

This audit is finite and claim-scoped; it does **not** audit R20's newer `p=181` number-field certificate or Conjecture 26's asymptotic claim.

## 10. Audit status for R19

Available independent audit evidence:

- `R18-I0084-C001`: PASS for the retained classical finite/symbolic core, artifact blob `476ce76449eb1ffa32e7811eb47567b901e4832a`;
- `R19-I0084-C002` free proof: **independent other-track audit pending**;
- P26 source/closure audit: **pending / not located**.

Therefore I do **not** call the repository package closed and do not create a paper folder yet.

## 11. Ledger / status table

| Claim | Status | Scope |
|---|---|---|
| R19-I0084-C001 | PROVED internally; R18 finite-core audit PASS | classical positive alpha=1/2, finite 5/2 moment, nonunimodal every t |
| R19-I0084-C002 | PROVED internally; external audit pending | free positive alpha=1/2, every polynomial moment, nonunimodal every t |
| R19-I0084-C003 | REFUTED mathematically / closure audits pending | Hasebe--Ueda Conj. 5.5 false as stated |
| X0084-01 | DISPROVED ROUTE | one boundary point does not imply a support gap |
| X0084-02 | DISPROVED ROUTE | classical one-sided shielding cannot be copied to free convolution |
| X0084-03 | REPAIRED | explicit V-points verify positive density on both sides |
| all-alpha behavior after correcting Conj. 5.5 | OPEN / not this frozen metric | no classification claimed |

## 12. ledger_delta for P26

```yaml
ledger_delta:
  track: R19
  source: "T. Hasebe and Y. Ueda, ALEA 2018, Conjecture 5.5 / I0084"
  target: "eventual unimodality for positive alpha=1/2 classical/free stable evolution under finite 5/2 moment"
  metric: "number of the two frozen classical/free positive alpha=1/2 universal source cases decided"
  before: "1/2"
  after: "2/2"
  status: "REFUTED mathematically as stated; repository closure PARTIAL/AUDIT_PENDING; half-stable only, no all-alpha classification"
  unchanged_count: 0
  exact_evidence:
    - "runs/R19/2026-09-16_13-40-24_UTC__i0084-halfstable-lefttail.md"
    - "artifacts/R18/2026-09-16_14-28-50_UTC__R18__r19-i0084-independent-audit-output.txt"
    - "artifacts/R19/2026-09-16_15-35-00_UTC__i0084_free_halfstable_gap_checker.py @ 88042774bec5c8b980d39cc291f4011e6261d8d2"
    - "artifacts/R19/2026-09-16_15-35-00_UTC__i0084_free_halfstable_gap_checker_output.txt @ 83dbb9c23ce7199d5df511a121e21c118e1cc29b"
  audits:
    classical_second_track: "R18 PASS finite/symbolic core"
    free_second_track: "PENDING"
    P26: "PENDING / not located"
  outgoing_audit:
    id: "R19-AUDIT-R20-I0100-P41-01"
    status: "PASS"
    scope: "R20/I0100 p=41 exact primal/dual theta certificate only"
```

## 13. Next obligation

The metric is 2/2, so the next obligation is **audit/closure hardening**, not another alpha=1/2 lemma:

1. obtain an independent other-track audit of the full free proof C002, especially the use of Huang--Wang Proposition 3.2 and Theorem 3.9 at the two flanking atoms and the open interval `J_n`;
2. obtain the P26 source/scope audit;
3. if both pass, build the required paper folder with a self-contained proof, exact checker/output and a README contrasting the exact alpha=1/2 refutation with the full source conjecture;
4. only after closure rotate the closable R19 slot according to the fleet protocol.  No schedule change is made by this worker.

**No email, Drive, public posting, purchases, permissions or schedule changes were performed.**

## Primary references

- T. Hasebe and Y. Ueda, *Large time unimodality for classical and free Brownian motions with initial distributions*, ALEA 15 (2018), 353--374, Conjecture 5.5.
- T. Hasebe and A. Kuznetsov, *On free stable distributions*, Electron. Commun. Probab. 19 (2014), no. 56.
- H.-W. Huang and J.-C. Wang, *Regularity results for free Levy processes*, arXiv:2203.00421 (2022), especially Proposition 3.1, Proposition 3.2, Theorem 3.6 / Remark 3.7, Theorem 3.9.
- H. Bercovici and D. Voiculescu, *Free convolution of measures with unbounded support*, Indiana Univ. Math. J. 42 (1993), 733--773.
