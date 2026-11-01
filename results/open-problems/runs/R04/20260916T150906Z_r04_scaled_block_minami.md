Model: GPT-5.6 Sol. Reasoning level: UNVERIFIED — the scheduler exposes no model or reasoning selector, so GPT-6 maximum was not set or verified.
Problem: Fyodorov–Mirlin (1991), *Scaling properties of localization in random band matrices: A sigma-model approach*, Phys. Rev. Lett. 67, 2405–2409, DOI 10.1103/PhysRevLett.67.2405. Fixed metric **MOVED**: on the unchanged domain `2W+1<=N`, the previous common-scale block-GOE record is sharpened by a variable-scale block-GOE decomposition; with the same proof-level PSSS constant `C_*`, the uniform factor drops from `sqrt(6)` to `1+sqrt(6)/2`. Status: **PARTIAL**; subsequential existence is retained, but the fixed-c limiting point process is not identified.

# R04 immutable run report — variable-scale block Minami and exact critical transfer reduction

Run ID: `20260916T150906Z_r04_scaled_block_minami`
Repository: `yspennstate/math-open-problems`, branch `master`
Overall source-problem status: **OPEN / PARTIAL milestone**.
Unchanged count after this run: **0**, because the fixed metric record moved.

## 1. Repository recovery and protocol state

Before doing new mathematics I reread the campaign/root controls on `master`:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/FLEET_2026-09-16.md` and `operations/RFLEET_2026-09-16.md`;
- newest own report `runs/R04/20260916T140957Z_r04_block_minami.md`;
- neighboring random-matrix report `runs/R03/20260916T1408Z_12_support6_exactn9.md`;
- newest R05 report `runs/R05/20260916T141505Z_i0030_edge_mnhd_n8.md`;
- newest R06 report `runs/R06/20260916T144133Z_i0056_edge_vertex_closure.md`.

I re-attempted the intake family `probability_1000_intake_*/problems.jsonl`, including the Claude, D, E, F, G, H and I ledgers. The connector truncates these large JSONL files, so this is **PARTIAL due connector truncation**, not a claim of a fresh semantic row-by-row reread of all roughly 780 entries. No queue switch is due: R04 still owns the external Fyodorov–Mirlin target and it is neither posted nor settled.

Root shared ledgers were not edited; P26 remains their writer. No Gmail, Drive, email, public publication, purchase, permission change, workflow execution, or scheduler change was performed.

## 2. Source locator and current-status check — 2026-09-16

Original source:

Y. V. Fyodorov and A. D. Mirlin, *Scaling properties of localization in random band matrices: A sigma-model approach*, Phys. Rev. Lett. **67** (1991), 2405–2409, DOI `10.1103/PhysRevLett.67.2405`.

The precise accessible locator remains the APS abstract on article p. 2405. It says that the reduction to a one-dimensional nonlinear supersymmetric sigma model becomes exact as the effective bandwidth `b -> infinity` and that `b^2/N` is the relevant scaling parameter. Thus `b ~ sqrt(N)` is exactly the critical scaling singled out by the source program. The modern exact unfolded point-process formulation used by R04 is a rigorous sharpening, not a verbatim numbered conjecture in the accessible 1991 text.

Dated current-scope checks on 2026-09-16 included the three required arXiv records and searches for fixed-c Hermitian critical statistics:

- Yau–Yin, arXiv:`2501.01718`: microscopic semicircle law, delocalization, QUE and GUE local statistics for their Hermitian Gaussian model for `W>N^(1/2+epsilon)`;
- Erdős–Riabov, arXiv:`2506.06441`: Wigner–Dyson statistics, full delocalization and QUE for broad real/complex classes when `W >> sqrt(N)`;
- Drogin, arXiv:`2508.05802`: sharp `W^2`-scale localization for `W^2 << N`;
- Shcherbina–Shcherbina, arXiv:`2604.15355`, is a **non-Hermitian** characteristic-polynomial threshold result and does not settle this target.

No Hermitian theorem identifying the exact real-box `W=c sqrt(N)` bulk point process was found in this bounded search. This is a search outcome, not proof that no unpublished result exists.

The published block-Gaussian input remains Ron Peled, Jeffrey Schenker, Mira Shamis, Sasha Sodin, *On the Wegner Orbital Model*, IMRN 2019, 1030–1058, DOI `10.1093/imrn/rnx145`, arXiv:`1608.02922`. Their Theorem 3, Eq. (1.22), gives all factorial moments for deformed block-Gaussian matrices. Immediately after Theorem 3 they record the expected 1D band crossover at `W ~ sqrt(L)`. Their proof of Theorem 3 sets `C_1=10 C`, with `C` the larger of the constants in Theorem 2 and Proposition 2.1; I use this fixed proof-level universal constant below and denote it `C_*`. No numerical value is invented.

## 3. Frozen model and metric

Let `H=H_N` be the real symmetric Gaussian circular band matrix

\[
\mathbb E H_{xy}=0,\qquad
\mathbb E H_{xy}^2=v\,\mathbf 1_{\{d_N(x,y)\le W\}},\qquad
v=(2W+1)^{-1},\qquad W=\lfloor c\sqrt N\rfloor,
\]

with independent upper-triangular coordinates. Freeze `c>0` and `E=0`. Since `rho_sc(0)=1/pi`, the unfolded interval `[-1,1]` is

\[
I_N=[-\pi/N,\pi/N],
\qquad X_N=\mathcal N(H_N,I_N).
\]

The previous run certified, on `2W+1<=N`, the common-scale block bound

\[
B_{\rm common}=Y_{\rm common}+Y_{\rm common}^2,
\quad
Y_{\rm common}=2\pi C_*\sqrt{\frac{2(2W+1)}q},
\quad
q=\Big\lfloor\frac{N}{\lceil N/(W+1)\rceil}\Big\rfloor,
\]

and hence the uniform envelope `Y_common <= 2 pi sqrt(6) C_*`. The scalar diagonal-conditioning bound `B_diag=2 pi(2W+1)+sqrt(2 pi(2W+1))` is also retained.

## 4. R04-FM-C3 — scaled-block PSSS factorial-moment theorem

**Status: PROVED by adapting the published PSSS proof with no new probabilistic input.**

### Statement

Let

\[
H=H_0+\bigoplus_{j=1}^K a_jV_j,
\]

where `H_0` is deterministic real symmetric, `a_j>0`, and the `V_j` are independent standard GOE blocks of sizes `m_j` in the PSSS normalization. Put

\[
S_a:=\sum_{j=1}^K\frac{m_j}{a_j}.
\]

Then for every interval `I` and every integer `m>=1`,

\[
\boxed{
\mathbb E\,(\mathcal N(H,I))_m
\le
(C_* |I| S_a)^m.
}
\tag{4.1}
\]

The same statement holds in the unitary case.

### Full proof

PSSS Proposition 2.4 and formula (2.10) are deterministic block-resolvent/counting identities. Replacing the `j`th random block `V_j` by `a_jV_j` changes the local term only from

\[
\mathcal N(V_j+A,J)
\quad\hbox{to}\quad
\mathcal N(a_jV_j+A,J).
\]

For `m=1`, rescaling gives

\[
\mathcal N(a_jV_j+A,J)
=
\mathcal N(V_j+a_j^{-1}A,a_j^{-1}J),
\]

so the single-block estimate used in the proof of PSSS Theorem 2 becomes

\[
\mathbb E\mathcal N(a_jV_j+A,J)
\le C\,m_j\frac{|J|}{a_j}.
\]

Summing the block representation proves the `m=1` case of (4.1) with `C_*>=C`.

Now assume (4.1) through factorial order `m-1`. Follow PSSS equations (2.13)–(2.19). Their local matrix in block `j` becomes

\[
B_{j,J}=a_jV_j+A_j-M(J)
=a_j\left[V_j+a_j^{-1}(A_j-M(J))\right].
\]

Hence

\[
B_{j,J}^{-1}
=a_j^{-1}\left[V_j+a_j^{-1}(A_j-M(J))\right]^{-1}.
\]

Every use of Proposition 2.1 in their equations (2.15) and (2.18) therefore has exactly the interval scale `|J|/a_j`; the local factor `C_* m_j |J|` becomes

\[
C_*\frac{m_j}{a_j}|J|.
\]

The rank-one perturbation in their equation (2.16),

\[
H_{v,\tau}=H+\tau P_j^*vv^*P_j,
\]

changes only the deterministic deformation `H_0` after conditioning on `v`; all block scales `a_i` and all independent GOE blocks remain unchanged. Therefore the induction hypothesis applies to `H_{v,\tau}` with the same global quantity `S_a`. The analogue of their (2.13) is

\[
2\xi\,C_*\frac{m_j}{a_j}(C_*S_a|I|)^{m-1}.
\]

Finally formula (2.10) sums this over `j`, producing

\[
C_*|I|\sum_j\frac{m_j}{a_j}(C_*S_a|I|)^{m-1}
=(C_*S_a|I|)^m.
\]

This closes the induction. No step changes the PSSS proof constant `C_*`; only the exact scaling factors `a_j^{-1}` are inserted. QED.

The theorem also applies conditionally when `H_0` is an independent random matrix, by conditioning on `H_0` first.

## 5. R04-FM-C4 — variable-scale exact Gaussian split and improved metric

**Status: PROVED.**

Assume the retained domain

\[
2W+1\le N.
\tag{5.1}
\]

If `N=2W+1`, the circular band graph is complete; take one block of size `N`. Otherwise set

\[
s=W+1,\qquad k=\lfloor N/s\rfloor\ge2,\qquad r=N-ks,
\]

and partition the ordered indices into `k` consecutive blocks of size `s` plus, if `r>0`, one final block of size `r`. Denote the block sizes by `m_j`. Every pair inside one such block has circular distance at most `W`.

For each block define its **own maximal GOE scale**

\[
\boxed{
a_j^2=\frac{m_j}{2(2W+1)}=\frac{v m_j}{2}.
}
\tag{5.2}
\]

A standard GOE(`m_j`) block has diagonal variance `2/m_j` and off-diagonal variance `1/m_j`. Therefore `a_jV_j` has

\[
\operatorname{Var}(a_jV_{aa})=v,
\qquad
\operatorname{Var}(a_jV_{ab})=v/2\quad(a<b).
\]

Subtract these variances coordinate-by-coordinate from the exact target covariance. The residual variances are zero on block diagonals, `v/2` on within-block off-diagonals, the full target variance `v` on inter-block band coordinates, and zero outside the band. They are all nonnegative. Gaussian variance splitting therefore yields an independent real-symmetric Gaussian residual `R` with

\[
\boxed{
H_N\stackrel d=R+\bigoplus_j a_jV_j.
}
\tag{5.3}
\]

This adds no matrix coordinate and preserves the exact circular band profile and variance normalization.

Condition on `R` and apply C3. Since

\[
\sum_j\frac{m_j}{a_j}
=\sqrt{2(2W+1)}\sum_j\sqrt{m_j},
\]

put

\[
\Lambda_{N,W}
:=
\frac{\sqrt{2(2W+1)}}{N}\sum_j\sqrt{m_j},
\qquad
Y_{\rm var}:=2\pi C_*\Lambda_{N,W}.
\tag{5.4}
\]

Then

\[
\boxed{
\mathbb E X_N^2
\le
B_{\rm var}(N,c):=Y_{\rm var}+Y_{\rm var}^2.
}
\tag{5.5}
\]

The **smallest bound now certified in the R04 record** is

\[
\boxed{
B_{\rm cert}^{\rm new}(N,c)
=
\min\{B_{\rm diag}(N,c),B_{\rm var}(N,c)\}.
}
\tag{5.6}
\]

### 5.1 Pointwise domination of the previous block record

Let `J=ceil(N/(W+1))`, the number of blocks in both the old balanced construction and the new greedy construction, and let `q=floor(N/J)`. Cauchy–Schwarz gives

\[
\left(\sum_j\sqrt{m_j}\right)^2\le JN.
\]

Since `qJ<=N`,

\[
\Lambda_{N,W}^2
\le
\frac{2(2W+1)J}{N}
\le
\frac{2(2W+1)}q.
\tag{5.7}
\]

Thus, with the **same** proof-level constant `C_*`,

\[
Y_{\rm var}\le Y_{\rm common},
\qquad
B_{\rm var}\le B_{\rm common}.
\]

### 5.2 Improved uniform envelope

The complete case `N=2W+1` gives `Lambda=sqrt(2)`. Otherwise write

\[
N=s(k+x),\qquad s=W+1,\qquad k\ge2,\qquad 0\le x<1,
\]

and put `y=sqrt(x)`. Then

\[
\Lambda_{N,W}
=\sqrt{4-2/s}\,\frac{k+y}{k+y^2}.
\]

For `0<=y<=1`, the last ratio decreases in `k`, so its maximum occurs at `k=2`. Hence

\[
\Lambda_{N,W}
\le
2\frac{2+y}{2+y^2}.
\]

The derivative numerator is `2-4y-y^2`, whose unique root in `[0,1]` is `y=sqrt(6)-2`. Therefore

\[
\boxed{
\Lambda_{N,W}\le1+\frac{\sqrt6}{2}=\frac{2+\sqrt6}{2}.
}
\tag{5.8}
\]

Consequently, on exactly the same domain (5.1),

\[
\boxed{
\mathbb E X_N^2
\le
\pi(2+\sqrt6)C_*
+
\pi^2(2+\sqrt6)^2C_*^2.
}
\tag{5.9}
\]

For comparison, the previous common-scale proof with the same `C_*` gave

\[
2\pi\sqrt6\,C_*+24\pi^2C_*^2.
\]

The coefficient of the linear term drops from `2 pi sqrt(6)=15.3905...` to `pi(2+sqrt(6))=13.9785...`, and the quadratic coefficient from `24 pi^2=236.8705...` to `pi^2(2+sqrt(6))^2=195.3980...`.

For the true critical sequence with fixed `c`, `Lambda_{N,W}->2`; therefore the asymptotic envelope remains

\[
\limsup_N\mathbb E X_N^2
\le4\pi C_*+16\pi^2C_*^2.
\]

So this run improves the exact finite-`N` record and its uniform envelope, not the fixed-`c` leading asymptotic constant.

## 6. Exact block transfer reduction and an obstruction to a naive SDE limit

The metric proof prefers blocks of size `W+1`. Those blocks are **bad for a standard transfer matrix**: the coupling to the next block is strictly triangular and hence deterministically singular. This was checked first as the counterexample to the naive transfer choice.

For transfer, instead take block size exactly `W` and restrict initially to a divisible subsequence `N=KW`, `K>=3`. Write the block vectors as `u_j in R^W`. The matrix is exactly cyclic block tridiagonal:

\[
B_{j-1}^{T}u_{j-1}+D_ju_j+B_ju_{j+1}=zu_j.
\tag{6.1}
\]

Here each `D_j` is a full real-symmetric Gaussian `W x W` block with the target entry variance `v`, and each `B_j` is lower triangular with

\[
(B_j)_{pq}\ne0\iff q\le p,
\]

all nonzero entries independent `N(0,v)`. There are no couplings beyond neighboring blocks; the circular seam has the same triangular law. The families `(D_j,B_j)` are iid over `j`.

Because every diagonal entry of `B_j` is a nondegenerate Gaussian, `B_j` is invertible almost surely. Define the state

\[
s_j=\binom{u_j}{B_{j-1}^{T}u_{j-1}}.
\]

Then (6.1) gives the exact iid transfer recursion

\[
\boxed{
s_{j+1}=M_j(z)s_j,
\qquad
M_j(z)=
\begin{pmatrix}
B_j^{-1}(zI-D_j)&-B_j^{-1}\\
B_j^T&0
\end{pmatrix}.
}
\tag{6.2}
\]

The periodic eigenvalue condition is exactly that the monodromy `M_K(z)...M_1(z)` have a nonzero fixed vector. At criticality,

\[
\boxed{
\frac KW=\frac N{W^2}\longrightarrow c^{-2}.
}
\tag{6.3}
\]

Thus the original model has an exact stochastic transfer-product formulation in which **both** the transfer dimension `2W` and the number of iid steps `K` diverge with fixed aspect ratio `K/W -> c^{-2}`. This is a precise finite-dimensional bridge to the Fyodorov–Mirlin scaling variable.

However the raw transfer matrices are not near identity. Since `B_j^{-1}` is triangular with diagonal entries `1/(B_j)_{pp}`,

\[
\|B_j^{-1}\|\ge\max_p |(B_j)_{pp}|^{-1}.
\]

Writing `(B_j)_{pp}=sqrt(v) Z_p`, `Z_p~N(0,1)` iid, gives the exact bound

\[
\mathbb P\{\|B_j^{-1}\|\le L\}
\le
\left[1-\mathbb P\left\{|Z|<\frac1{L\sqrt v}\right\}\right]^W.
\tag{6.4}
\]

For `L=A W^(3/2)` the right side tends to

\[
\exp\left(-\frac{2}{A\sqrt\pi}\right).
\]

So `W^(3/2)` inverse spikes occur at nonvanishing probability. A naive raw-coordinate Brownian/SDE transfer limit is therefore not justified. Any successful transfer limit needs a projective/QR or other renormalized formulation that controls these triangular hard-edge events. Standard iid square-Gaussian singular-value estimates do not apply unchanged because the band coupling block is triangular.

The exact checker verifies the support identities `q<=p` for `W`-blocks, `q<p` for the singular `W+1` transfer blocking, and absence of beyond-neighbor couplings on the `c=1`, `N=n^2,W=n` subsequence.

## 7. Exact checker and adversarial finite tests

Executed:

- `artifacts/R04/20260916T150906Z_r04_scaled_block_minami_exact.py`
- `artifacts/R04/20260916T150906Z_r04_scaled_block_minami_exact.out`

The checker uses exact `Fraction` arithmetic for the Gaussian covariance split and the Cauchy-comparison preconditions. It exhausts **62,750 admissible `(N,W)` pairs with `N<=500`**, verifies the exact per-block variances, checks the transfer support geometry for `W=1,...,79`, and symbolically verifies the uniform maximizer identity

\[
2\frac{2+(\sqrt6-2)}{2+(\sqrt6-2)^2}=1+\frac{\sqrt6}{2}.
\]

Output ends `SELF-CHECK PASS`.

Local SHA-256 values before upload:
- checker: `768c214c3cd9f7801a122eac399a989d36a8919e9040611037994cfb6e1af275`;
- output: `a6fe75f4b24d2bc992097253e9aafc7e1554d01e22404d83e45f380f04cabea3`.

The runtime emitted an unrelated spreadsheet-runtime warmup warning on process startup; the checker itself completed with exit code zero and `SELF-CHECK PASS`.

## 8. Independent R05 audit

Newest ready R05 package:

`runs/R05/20260916T141505Z_i0030_edge_mnhd_n8.md`.

The previous R04 theorem audit of `R05-I0030-C1` remains

`R04-AUDIT-R05-I0030-C1-20260916T130900Z: PASS_MATH / NOVELTY_UNVERIFIED`.

This run independently audited the **new n=8 representative certificate**, without pretending to reproduce R05's exhaustive 44,808-labeled-regular-graph census.

Audit ID:

`R04-AUDIT-R05-I0030-N8-20260916T150906Z: PASS_SCOPED_REPRESENTATIVES`.

The checker independently verifies that R05's five graph6 representatives

`GqGOOK`, `GsXP_[`, `G?~vf_`, `G]~v~w`, `G~~~~{`

are respectively isomorphic to `C8`, `Q3`, `K_{4,4}`, the 8-vertex cocktail-party graph, and `K8`; explicit automorphism families are checked to act transitively on oriented edges; and the exact integer identity

\[
(A^{m+1})_{xx}=d(A^m)_{xy},\qquad x\sim y,
\]

is independently checked through `m=17` for every oriented edge of all five representatives.

**Scope limitation:** this audit does not independently verify that these are the only five arc-transitive isomorphism classes on eight vertices or reproduce R05's full labeled enumeration. It is therefore `PASS_SCOPED`, not a second full completeness audit of the n=8 metric extension.

## 9. Status and next attack

Retained:
- uniform local factorial moments and subsequential point-process existence at `E=0`;
- simplicity of subsequential limits;
- exact critical band normalization.

Still OPEN:
- full-sequence convergence;
- deterministic-energy limiting intensity;
- identification of the fixed-`c` crossover law;
- profile universality;
- the `c downarrow 0` Poisson and `c up-arrow infinity` GOE/Sine_1 limits inside one identified family.

The next highest-value attack is no longer count tightness. It is to renormalize the exact iid transfer product (6.2) so that the triangular `B_j^{-1}` hard-edge spikes are separated from the projective dynamics. A QR/Iwasawa cocycle is the natural next test: factor each `M_j(z)` into radial singular-value growth and an angular/projective component, then ask whether the angular process has increments of order `1/W` over `K~W/c^2` steps. Any claimed diffusion limit must explicitly survive the lower-triangular band dependence and the exact variance `v=(2W+1)^(-1)`.

No fixed-`c` point-process identification claim is made.

## 10. ledger_delta for P26

```yaml
ledger_delta:
  worker: R04
  source: "Fyodorov–Mirlin, Phys. Rev. Lett. 67 (1991), 2405–2409, DOI 10.1103/PhysRevLett.67.2405"
  target: "E=0 bulk unfolded point process for the real Gaussian circular band model, W=floor(c sqrt(N)); current milestone is the unfolded [-1,1] count second moment"
  metric: "smallest certified R04 upper bound on E[X_N^2], retaining N-domain"
  domain: "2*floor(c*sqrt(N))+1 <= N"
  before: "min(B_diag,B_common), B_common=Y_common+Y_common^2, Y_common=2*pi*C_*sqrt(2(2W+1)/q); uniform Y_common<=2*pi*sqrt(6)*C_*"
  after: "min(B_diag,B_var), B_var=Y_var+Y_var^2, Y_var=2*pi*C_*Lambda_NW, Lambda_NW=sqrt(2(2W+1))*sum_j sqrt(m_j)/N for greedy sizes m_j; uniform Lambda_NW<=(2+sqrt(6))/2"
  uniform_after: "E[X_N^2] <= pi(2+sqrt(6))*C_* + pi^2(2+sqrt(6))^2*C_*^2"
  status: PARTIAL
  unchanged_count: 0
  exact_evidence:
    - "PSSS Theorem 3, Eq. (1.22), and proof Eqs. (2.10)-(2.19); scaled-block extension proved in this report"
    - "artifacts/R04/20260916T150906Z_r04_scaled_block_minami_exact.py"
    - "artifacts/R04/20260916T150906Z_r04_scaled_block_minami_exact.out"
    - "checker commit a3ebe6973eb71b1d26a2862714057e4883e75562"
    - "output commit 6190b6d206156017f02c9b133a9eb678a61a26da"
  audit_ids:
    - "SELF-CHECK:R04-20260916T150906Z-PASS"
    - "R03-AUDIT-R04-FM-C1-01:PASS (prior scalar claim only)"
    - "P26:PENDING for C3/C4"
  outgoing_audit:
    - "R04-AUDIT-R05-I0030-N8-20260916T150906Z:PASS_SCOPED_REPRESENTATIVES"
```
