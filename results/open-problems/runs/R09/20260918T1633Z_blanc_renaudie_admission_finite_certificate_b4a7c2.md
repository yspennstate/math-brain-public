Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 at maximum. SUCCESSOR ADMISSION MOVED `E_ready: 0 -> 1`; the new frozen research metric is `M_A=0 -> 0` (no dimension yet certified). Methods used: #4, #15, #24.**

# R09 — Blanc-Renaudie mean-field `d=7,8,9,10`: admission plus a finite Simon–Lieb initialization certificate

Run date: 2026-09-18 UTC  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Lane: **CLOSABLE OUTSIDE**

## 1. Runtime/control truth

The prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. The runtime exposes no authenticated reasoning-effort receipt, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, maximum reasoning, or an hour-long execution guarantee.

The task-management surface available to this run still exposes task title/prompt, recurrence or timing, enabled state, and task identity, but no bindable model-family field, no bindable reasoning-effort field, and no authenticated completed-run model/effort telemetry. Making `GPT-6 / maximum` enforceable would require an owner-authorized product/workspace/API/admin surface that actually exposes persistent model and effort fields plus per-run attestation. The historical `You cannot modify this task` authorization boundary (including the old P26 case) still has the same lawful remedies: use the owning/otherwise-authorized context, an authorized ownership/admin transfer, or platform support. I made no scheduler or permission change.

## 2. Continuity and repository read

Before changing target state I recovered the current controlling owner directive, `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, `operations/claims/TANG-2020-Q4.11.md`, the newest R09 report, the current coordinator status, recent master commits, and the old C0064 intake/attempt evidence relevant to the new percolation candidate.

The old Tang claim file still literally says `PENDING_ADMISSION`, but that historical reservation is superseded by the later immutable R09 handoffs: Tang's periodic-tree assertion is already retired/refuted in this lane and is not reopened. G0013 and `CHEN-WANG-2025-GAUSSIAN-SUBUNIFORM` likewise remain retired/frozen. The previous R09 report left this worker at a CLOSABLE successor-admission gate with `E_ready=0`.

The repository changed materially after that report: a new 17 September 2026 probability source appeared in the fresh literature, while two precise questions from another 17 September source (Khan–Pedersen–Stinchcombe) were already taken by R01/R06. I therefore did not override those owners and screened the new percolation source instead.

## 3. New source passes the CLOSABLE admission gate

### 3.1 Source

Arthur Blanc-Renaudie, *Markovian renormalisation for percolation in high-dimension: Semi-decidability of mean field behavior*, arXiv:2609.20764v1, submitted 17 September 2026.

Theorem 1.1 states that for every `d>6` and spread parameter `L>=1` there is a **computable** function `f` such that the following are equivalent:

- there exist `C>0` and `p0<p_c` with `chi(p0)>=f(C)` and
  \[
  \tau_{p_0}(x)\le C\langle x\rangle^{2-d}\qquad\forall x\in\mathbb Z^d,
  \tag{C}
  \]
- there exists `A>0` such that
  \[
  \tau_{p_c}(x)\sim A\langle x\rangle^{2-d}\qquad(|x|\to\infty).
  \tag{A}
  \]

Corollary 1.2 says `(A)` is semi-decidable. For nearest-neighbour percolation (`L=1`), the paper records that `d>=11` is known and explicitly leaves `7<=d<=10` open. Section 1.3 goes further: it says these dimensions can in principle be proved in finite time, but the author does not determine whether this can be done within a reasonable human lifetime. The stated computational obstacles are the difficulty of estimating `tau_{p0}` once `chi(p0)` is of order `100`–`1000`, and the lack of good short-time non-asymptotic local-CLT estimates for the cluster Markov chain. The paper also remarks that a small enough triangle condition may bypass the extremely costly local modifications.

The author's current research page independently describes this program as “Semi-decidability of meanfield behavior in dimensions 7<=d<=10.”

### 3.2 Current literature

A dated exact-ID/title/nearest-neighbour-dimension search on 18 September 2026 found Blanc-Renaudie v1 and the established Fitzner–van der Hofstad 2017 theorem for nearest-neighbour `d>=11`; it found no source-matching proof for any of `d=7,8,9,10`. Because Blanc-Renaudie v1 is less than one day old, this is explicitly **bounded negative evidence**, not a novelty certificate.

I also checked the author's recent percolation papers. The 2026 Blanc-Renaudie–Hutchcroft `k`-point paper works subject to the usual perturbative/lace-expansion hypotheses and does not remove the nearest-neighbour `d=7,...,10` gap. The 2025 Blanc-Renaudie–Nachmias torus paper likewise assumes sufficiently high nearest-neighbour dimension or spread-out `d>6` and does not settle these four nearest-neighbour cases.

### 3.3 Repository ownership and historical attempt

Fresh repository searches for `2609.20764` and its exact title found no prior canonical claim or active owner. The create-only claim path was absent before creation.

The older intake contains the closely related but not identical C0064: Heydenreich–van der Hofstad Open Problem 10.1, the Fourier infrared bound for nearest-neighbour percolation in every `d>6`. Its single recorded attempt `C0064-A001` is unreviewed and stopped because the lace-expansion/NoBLE small parameter does not close in `d=7,...,10`; there is no current canonical claim at `operations/claims/C0064.md`. I do **not** identify Blanc-Renaudie's pointwise asymptotic `(A)` with that Fourier statement without a written implication, so C0064 is not silently declared solved or absorbed.

### 3.4 Exclusive claim and frozen metric

I created the exclusive claim

`operations/claims/BLANC-RENAUDIE-2026-MEANFIELD-7-10.md`

at commit

`39560ed860c25965e1d95bb3756b2c618ae5a9a5`.

The exact full-source R09 target is the finite unresolved suite `(A_d)` for **all four** `d in {7,8,9,10}`. One solved dimension is PARTIAL; full source closure needs all four.

The frozen metric is

\[
M_A:=\#\left\{d\in\{7,8,9,10\}:\text{R09 has a complete rigorous certificate of Theorem 1.1(a) in dimension }d\right\}.
\]

Baseline and end-of-run value:

\[
\boxed{M_A:0\longrightarrow0.}
\]

Thus the **lifecycle gate moved** (`E_ready:0->1`), but there is no fake mathematical movement: no dimension is certified yet.

## 4. Method #4 — prove something weaker completely: an explicit finite Simon–Lieb certifier for condition (C)

The source says condition `(C)` can be checked in finite time by combining finite-box computation and sharpness. I made that statement concrete enough to be used as an exact certificate. The core finite-size criterion itself is classical Simon–Lieb/Hammersley machinery; I do **not** claim that mechanism as novel.

Work with nearest-neighbour Bernoulli bond percolation on `Z^d`. For a finite set `S` containing `0`, write

\[
\tau_{S,p}(x,y)=\mathbb P_p(x\leftrightarrow y\text{ by an open path contained in }S)
\]

and

\[
\varphi_p(S)
:=p\sum_{\substack{u\in S,\ v\notin S\\u\sim v}}
\tau_{S,p}(0,u).
\]

Panis–Schapira (2026) explicitly recalls the classical fact that `varphi_p(S)<1` is a finite-size criterion for exponential decay, obtained by iterating the Simon–Lieb inequality. I now package that criterion with a rigorous finite-box **upper** approximation, which is the part needed for Blanc-Renaudie's initialization.

Let

\[
\Lambda_m=[-m,m]^d\cap\mathbb Z^d,
\qquad a:=\varphi_p(\Lambda_m),
\qquad q:=m+1,
\]

and suppose `a<1`. Put

\[
T(r):=\sup_{\|x\|_\infty\ge r}\tau_p(0,x).
\]

### Lemma 4.1 — exact block tail

For every integer `r>=0`,

\[
\boxed{T(r)\le a^{\lfloor r/q\rfloor}.}
\tag{4.1}
\]

### Proof

For `x` outside `Lambda_m`, the Simon–Lieb first-exit inequality gives

\[
\tau_p(0,x)
\le p\sum_{\substack{u\in\Lambda_m,\ v\notin\Lambda_m\\u\sim v}}
\tau_{\Lambda_m,p}(0,u)\,\tau_p(v,x).
\]

Every exit vertex `v` has `||v||_infty=m+1=q`. Hence if `||x||_infty>=r>=q`,

\[
\|x-v\|_\infty\ge r-q,
\]

so

\[
T(r)\le aT(r-q).
\]

Iterating and using `T(s)<=1` for `0<=s<q` proves (4.1). In particular `a<1` itself certifies exponential decay and hence `p<p_c`. ∎

The next point is important: a restricted finite-box connection probability is a **lower** bound on the infinite-volume connection probability, so simply enumerating a box does not verify `(C)`. One needs a rigorous outside-box correction.

### Lemma 4.2 — finite-box upper completion

Fix integers `0<=R<N`. For every `x in Lambda_R`,

\[
\boxed{
\tau_p(0,x)
\le
\tau_{\Lambda_N,p}(0,x)
+
\varphi_p(\Lambda_N)
\,a^{\left\lfloor\frac{N+1-R}{m+1}\right\rfloor}.
}
\tag{4.2}
\]

### Proof

Apply Simon–Lieb with `S=Lambda_N` and `Lambda=Z^d`:

\[
\tau_p(0,x)
\le \tau_{\Lambda_N,p}(0,x)
+p\sum_{\substack{u\in\Lambda_N,\ v\notin\Lambda_N\\u\sim v}}
\tau_{\Lambda_N,p}(0,u)\tau_p(v,x).
\]

For every exiting `v`, `||v||_infty=N+1`; for `x in Lambda_R`,

\[
\|v-x\|_\infty\ge N+1-R.
\]

Translation invariance and Lemma 4.1 therefore bound every last factor by

\[
a^{\left\lfloor\frac{N+1-R}{m+1}\right\rfloor},
\]

and the remaining boundary sum is exactly `varphi_p(Lambda_N)`. ∎

### Proposition 4.3 — a completely finite certificate for Blanc-Renaudie (C), once `f_d(C)` is instantiated

Fix `d>6`, rational (or rigorously interval-certified) `p,C>0`, and integers `m<R<N`. Suppose a finite calculation certifies:

1. `a=varphi_p(Lambda_m)<1`;
2. the finite-box susceptibility lower bound
   \[
   \chi_N(p):=\sum_{x\in\Lambda_N}\tau_{\Lambda_N,p}(0,x)\ge f_d(C);
   \tag{4.3}
   \]
3. for every `x in Lambda_R`,
   \[
   \tau_{\Lambda_N,p}(0,x)
   +\varphi_p(\Lambda_N)a^{\lfloor(N+1-R)/(m+1)\rfloor}
   \le C\langle x\rangle_2^{2-d};
   \tag{4.4}
   \]
4. for every integer `r>=R+1`,
   \[
   a^{\lfloor r/(m+1)\rfloor}
   \le C d^{-(d-2)/2}r^{2-d}.
   \tag{4.5}
   \]

Then `p<p_c`, `chi(p)>=f_d(C)`, and

\[
\tau_p(0,x)\le C\langle x\rangle_2^{2-d}\qquad\forall x\in\mathbb Z^d.
\]

Consequently Blanc-Renaudie Theorem 1.1(a) holds and `(A_d)` follows.

### Proof

Condition 1 and Lemma 4.1 give exponential decay, so `p<p_c`. Restricted connections are contained in unrestricted ones, hence

\[
\chi(p)\ge\chi_N(p)\ge f_d(C).
\]

For `x in Lambda_R`, (4.4) and Lemma 4.2 prove the desired pointwise bound. For `||x||_infty=r>=R+1`, Lemma 4.1 and (4.5) give

\[
\tau_p(0,x)
\le C d^{-(d-2)/2}r^{2-d}.
\]

Since `||x||_2<=sqrt(d)||x||_infty` and `2-d<0`,

\[
d^{-(d-2)/2}r^{2-d}\le ||x||_2^{2-d},
\]

which proves `(C)` outside the finite core as well. ∎

### What is and is not gained

For rational `p`, every restricted connectivity probability in (4.3)–(4.4), and every `varphi_p(Lambda_k)`, is in principle an exact rational finite-graph reliability computation. Thus **after an explicit value of the source's computable `f_d(C)` is extracted**, all remaining obligations in Proposition 4.3 are finite exact inequalities. This does not make them computationally cheap.

The immediate bottleneck is therefore sharper than “check infinitely many x”: it is now

1. extract a practical explicit dependency `f_d(C)` from Blanc-Renaudie's quantitative proof, preferably using Remark 3.6 to bypass the costly local modifications when the triangle condition is numerically small; and
2. compute enough finite-box restricted two-point data at a `p0` with `chi(p0)` large enough.

I do not count Proposition 4.3 toward `M_A`; it is a certifier, not a certificate for a specific dimension.

## 5. Method #15 — break symmetry on purpose: anisotropic exponential tilting does **not** rescue a bad symmetric block

I tested whether the infinite tail in Proposition 4.3 could be improved by giving different exponential penalties to different coordinate directions.

For the cube `Lambda_m`, let the finite first-exit kernel be

\[
q_m(v)
:=p\sum_{\substack{u\in\Lambda_m\\u\sim v}}
\tau_{\Lambda_m,p}(0,u),
\qquad v\notin\Lambda_m,\ v\sim\Lambda_m.
\]

Thus

\[
\sum_vq_m(v)=\varphi_p(\Lambda_m)=a.
\]

For `lambda=(lambda_1,...,lambda_d)` with `lambda_i>=0`, the natural anisotropic weighted mass is

\[
A_m(\lambda)
:=\sum_vq_m(v)\exp\!\left(\sum_{i=1}^d\lambda_i|v_i|\right).
\tag{5.1}
\]

Two exact facts kill the naive anisotropic shortcut.

First,

\[
A_m(\lambda)\ge A_m(0)=a,
\]

so **no positive exponential tilt can rescue a block for which `a>=1`**.

Second, because both the lattice and the cube are invariant under coordinate permutations, `q_m(Pv)=q_m(v)` for every permutation `P`. The function `A_m` is convex and permutation-invariant. If

\[
\bar\lambda=\frac1d\sum_i\lambda_i,
\]

then Jensen's inequality over all coordinate permutations gives

\[
\boxed{
A_m(\bar\lambda\mathbf 1)
=A_m\!\left(\frac1{d!}\sum_P P\lambda\right)
\le\frac1{d!}\sum_PA_m(P\lambda)
=A_m(\lambda).
}
\tag{5.2}
\]

Thus at fixed average exponential rate, the **isotropic** tilt is already optimal for a symmetric cube. Breaking the coordinate weights alone cannot improve the scalar Simon–Lieb certificate.

This is a useful failed route. To gain from broken symmetry one must change more than the weight: e.g. rectangular/adaptive regions, a multi-state first-exit kernel that remembers face/direction, or the genuinely longer-memory cluster chain suggested by Blanc-Renaudie. I did not promote any of those harder variants to a theorem in this run.

## 6. Method #24 — find the extremal object: the infinite polynomial-tail check collapses to one finite block endpoint

Condition (4.5) still looks like infinitely many inequalities. It is actually a finite exact check.

Let

\[
D=d-2,\qquad q=m+1,\qquad 0<a<1,
\]

and define

\[
b_k:=a^k\bigl((k+1)q-1\bigr)^D,
\qquad k\ge0.
\tag{6.1}
\]

For every integer `r` with `floor(r/q)=k`, the quantity relevant to (4.5),

\[
a^{\lfloor r/q\rfloor}r^D,
\]

is increasing in `r` inside that block. Hence its block maximum occurs at the single endpoint

\[
r_k=(k+1)q-1
\]

and equals `b_k`.

Moreover

\[
\frac{b_{k+1}}{b_k}
=a\left(\frac{(k+2)q-1}{(k+1)q-1}\right)^D,
\tag{6.2}
\]

and the right side is strictly decreasing in `k`, with limit `a<1`. Therefore `(b_k)` is unimodal: it can increase only up to one crossing and then decreases forever.

Consequently, over any tail `r>=R`, the worst ratio in (4.5) is attained at a **finite, explicitly locatable block endpoint**. Starting at the block containing `R`, advance `k` only until the exact rational inequality

\[
\boxed{
a\bigl((k+2)q-1\bigr)^D
\le \bigl((k+1)q-1\bigr)^D}
\tag{6.3}
\]

first holds. The maximum of all subsequent blocks is then the current endpoint; no further search is needed.

Thus condition (4.5) is not an analytic-tail bottleneck at all. For rational finite-volume data it reduces to a finite exact comparison of rational numbers; no logarithms or floating-point asymptotics are required.

This identifies the extremal object for the Simon–Lieb envelope: **a single block-endpoint radius near the unique transition where exponential decay overtakes the polynomial factor `r^{d-2}`**.

## 7. Prior-art honesty

The core implication

\[
\varphi_p(S)<1\quad\Longrightarrow\quad\text{exponential decay}
\]

is classical. Panis–Schapira's May 2026 paper explicitly calls it a finite-size criterion obtained by iterating Simon–Lieb and notes that the argument traces back to Hammersley. I therefore do **not** claim novelty for Lemma 4.1.

The finite-box upper completion (Lemma 4.2), the packaged certifier (Proposition 4.3), the anisotropic Jensen obstruction (5.2), and the exact block-endpoint reduction (6.1)–(6.3) are derivations made in this run. I have not found a source claiming these exact packaged statements, but priority is **UNVERIFIED** and no novelty claim is made before a dedicated search and independent audit.

## 8. Why the source metric did not move

The full source metric remains

\[
\boxed{M_A=0.}
\]

No dimension can honestly be counted from the present theorem package because the source's computable function `f_d(C)` is not written explicitly in the paper, and I have not yet extracted its complete dependency chain or produced the requisite exact finite-volume connectivity data. Blanc-Renaudie explicitly says this numerical initialization is the unresolved practical barrier. Calling a dimension solved now would confuse a **finite algorithm** with a **successful certificate**.

This is the first research run on the new active target, so no stuck/retirement count is inferred from the prior successor-gate runs.

## 9. Next new-method directions

The next run must not repeat #4/#15/#24. The three reserved fresh moves are:

- **#8 — discretize:** turn the proof-dependency chain defining `f_d(C)` into an explicit constant DAG, starting from the branch that uses Remark 3.6 to skip local modifications under a numerically small triangle condition;
- **#16 — compute every small case:** derive exact symbolic `varphi_p(Lambda_m)` and finite-box susceptibility bounds for the smallest tractable blocks, first analytically where possible, to see which dimension/scale becomes the best candidate rather than assuming `d=10`;
- **#20 — find why the algorithm fails:** quantify separately the constant-extraction, reliability-enumeration, and short-time LTCL costs, and identify the first one that makes a human-scale exact certificate impossible.

The preferred first dimension is **not frozen yet**. The source says `d=7` is the hardest because `psi_7(chi)=sqrt(chi)` and requires larger susceptibility, so `d=10` is a natural initial computational candidate, but that is a heuristic ordering only until the explicit constant DAG is extracted.

## 10. Structured ledger delta

```yaml
ledger_delta:
  worker: R09
  lane: CLOSABLE_OUTSIDE
  previous_lifecycle: successor_admission_gate
  previous_gate_metric:
    name: E_ready
    before: 0
    after: 1
    reason: "fresh source-exact READY/CLOSABLE successor admitted and exclusively claimed"
  active_source: BLANC-RENAUDIE-2026-MEANFIELD-7-10
  source_url: https://arxiv.org/abs/2609.20764
  claim_path: operations/claims/BLANC-RENAUDIE-2026-MEANFIELD-7-10.md
  claim_commit: 39560ed860c25965e1d95bb3756b2c618ae5a9a5
  frozen_metric:
    name: M_A
    definition: "number of d in {7,8,9,10} with a complete rigorous Blanc-Renaudie Theorem 1.1(a) certificate"
    before: 0
    after: 0
  status: OPEN
  source_scope: "all four unresolved nearest-neighbour dimensions 7,8,9,10; one dimension is PARTIAL"
  methods_used: [4, 15, 24]
  next_methods: [8, 16, 20]
  finite_claim_checker: "not applicable this run: no enumerative finite certificate was claimed; theorem-sized analytic arguments are written on page"
  prior_art_status: "bounded current search completed; novelty/priority UNVERIFIED"
  independent_full_claim_audits: "0/2"
  shared_root_edits: false
  peer_file_edits: false
  scheduler_changes: false
  email_or_drive: false
  public_posting: false
```

No shared root, peer-track file, scheduler, email, Drive, public-posting, purchase, workflow, or permission state was modified.
