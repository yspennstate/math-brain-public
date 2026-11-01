# C0056 direct referee packet — 2026-10-10

## Scope and source

Primary Bourgade 2018, Section 2.1: $H_{RS}=\Delta+\lambda V$ on $\mathbb Z^d$, iid centered variance-one sites. The source separately discusses (A) infinite-volume a.c. spectrum in $d=3$ at weak disorder and (B) GOE microscopic statistics of periodic finite-volume restrictions. Intake `problems.jsonl:56` combines them. A September 23, 2026 OpenAI preprint claims (A), for iid uniform sites, on a fixed open interval in every $d\ge3$. I checked its stated theorem and spectral conclusion but not its full proof. It makes no GOE claim. Present a.c. status: **CLAIMED IN UNREVIEWED PREPRINT**; GOE/current combined status: **UNKNOWN**. No parent-problem solved assertion.

## Direct check of w483 core packet

Artifact: `~/brain_workers/w483/ATTEMPT.md`, SHA256 `4F99EBDF4C964AACC446B9399DB3EAB0B6EDCECF85AD00534470CCD9C9867338`. This is a direct audit of that attempt, not of another review.

| Item | Verdict | Reproduction / limit |
|---|---|---|
| L1 Poisson pair and Fourier identities | KEEP | $P_\eta*P_\eta=P_{2\eta}$; Plancherel yields $1/(2\pi)$. The diagonal at a simple finite-volume atom is $a_j^2/(2\pi\eta)$. No independent-environment factorization is used. |
| L2 annealed $L^2$ criterion | KEEP as conditional lemma | Monotone convergence of $e^{-2\eta|t|}|\widehat\nu(t)|^2$ gives Fourier $L^2$ almost surely under a finite expected bound. A finite measure with $L^2$ Fourier transform has an $L^2$ density. Site translation and a countable intersection yield operator-level a.c. on covered windows; nonzero mass is separate. |
| L3 pair-concentration reduction | KEEP as conditional lemma | $-\partial_rP_{2\eta}(r)=4\eta r/[\pi(r^2+4\eta^2)^2]$. Integrating $Ar+B/N$ gives $A/2+B/(2\pi\eta N)$. The asserted uniform $Ar+B/N$ bound for the actual model is explicitly UNPROVED. |
| L4 limit order | KEEP | At fixed $\eta>0$, strong convergence of cut-bond finite-volume operators gives weak local measures. Common compact spectral support gives an integrable square envelope for Poisson densities. Let volume grow before $\eta\downarrow0$; reversing limits leaves atoms. |
| L5 flat Cantor example | KEEP as abstract counterexample | Equal first $m$ digits occur with probability $2^{-m}$ and put samples within $3^{-m}\le\eta$. Thus $P_{2\eta}(s-t)\ge2/(5\pi\eta)$; $\eta<3^{1-m}$ yields $2^{-m}>\eta^\alpha/2$, proving the stated $\eta^{\alpha-1}/(5\pi)$ lower bound. It is outside the lattice iid class. |
| L6 Minami plus conditional marks | KEEP only as a reduction; **FIX any reading as a proved Anderson estimate** | Combes–Germinet–Klein, arXiv:0804.3202v3, Eq. (1.4), gives $\mathbb E n_Q(n_Q-1)\le(R|Q|N)^2$ for independent bounded-density diagonal disorder, $R=1/(2g)$. At most $2W/r$ bins of width $r\le W$, each enlarged to length $3r$, give $(K/N^2)(2W/r)(3RrN)^2=18KR^2Wr$. The diagonal adds $D/N$. The conditional mark bound $\mathbb E[a_ja_k\mid E_1,\ldots,E_N]\le K/N^2$ is a separate unproved hypothesis; Minami counts eigenvalues and says nothing about these marks. |
| L7 free calibration | KEEP special case | $f_1(s)=1/[\pi\sqrt{4-s^2}]$ belongs to $L^{3/2}$; Young twice gives $\|f_1^{*3}\|_\infty\le\|f_1\|_{3/2}^3=B(1/2,1/4)^2/(2\pi^3)$. This is only $g=0$. |
| L8 random atom versus averaged density | KEEP abstract counterexample | For $\nu_X=\delta_X$, $X\sim U[0,1]$, $\mathbb E\nu_X$ has density 1 but each sample is pure point, and $\mathbb E\|P_\eta*\nu_X\|_2^2=1/(2\pi\eta)$. |

The **single hardest open piece in w483** is the fixed-positive-disorder marked two-eigenvalue concentration estimate, uniform in volume and smoothing scale. The primary Minami theorem does not supply the missing conditional eigenvector moments. Even if obtained, the GOE part needs its own proof.

## Direct check of w484 independent packet

Artifact: `~/brain_workers/w484/ATTEMPT.md`, SHA256 `5F5ECD3C46306622DEC368C6FBC597ADA6486B6B37F213A96B4CB23C65F42294`.

| Item | Verdict | Reproduction / limit |
|---|---|---|
| L01 annealed first moment | KEEP | For the zero-hopping iid diagonal model, $\mathbb E\,\Im G_{00}(0+i\eta)/\pi=\arctan(1/\eta)/\pi\to1/2$ while every local measure is atomic. Ward's identity holds exactly; it does not change this. The example is outside the target's hopping assumption. |
| L02 local $L^p$ criterion | KEEP as conditional lemma | Fatou makes a bounded $L^p(I)$ subsequence pathwise; reflexivity for $p>1$ and test-function convergence of the Poisson approximate identity identify the weak limit with $\mu_\omega|_I$. This requires the unproved uniform $p$ moment at fixed disorder. |
| L03 cavity calculation | KEEP as exact identity and conditional bound | Condition on all sites except 0. With $b=\eta+\Im\Sigma>0$, $G_{00}=1/(\lambda V_0-a-ib)$. Substitution $s=\lambda v$ and $\int_\mathbb R b^2/(s^2+b^2)^2ds=\pi/(2b)$ give $\mathbb E[u_\eta^2\mid\text{cavity}]\le M/(2\pi\lambda b)$. For uniform $V_0\in[-1,1]$, the interval $[a-b,a+b]$ yields the stated lower bound $1/(4\lambda\pi^2b)$ when $|a|+b\le\lambda$. There is no proved uniform inverse-$b$ bound on actual resonant cavities. |

The **single hardest open piece in w484** is uniform control of the inverse cavity width $b^{-1}$ as $\eta\downarrow0$ at fixed positive disorder, on the resonant set. Correlated six-neighbor cavity terms cannot be replaced by independent copies.

## My disjoint additions and requested review

`ATTEMPT.md` gives a finite-time obstruction using free periodic tori and an all-time Fourier criterion. Its Fourier criterion overlaps w483's L1-L2, so the distinctive contribution is the explicit finite-time torus bound. A second disjoint statement: the free infinite lattice has a.c. spectrum, yet its deterministic finite-volume unfolded point process cannot have the nondegenerate GOE law as a distributional limit. Thus a.c. alone supplies no GOE inference. These are elementary special cases, not progress on the positive-disorder theorem; w488 should referee the new finite-time and GOE-obstruction lemmas before any theorem card is integrated.

## Reproduction references

- `~/brain_workers/w485/ATTEMPT.md` — independent derivation saved before peer read.
- Bourgade source: https://cims.nyu.edu/~bourgade/papers/ICMProceedings.pdf , Section 2.1.
- Combes–Germinet–Klein source: https://arxiv.org/pdf/0804.3202 , Eq. (1.4), definition of $Q_\Lambda$.
- Claimed 2026 a.c. preprint theorem: https://raw.githubusercontent.com/openai/math/main/preprints/Absolutely-Continuous-Spectrum-for-Weak-Disorder-Anderson-Models-in-Dimensions-at-Least-Three-September-23-2026/build/01-introduction.tex .

NEXT: Route this packet to w483, w484, w488 and integration contact; prepare a draft brain bundle recording the two-branch source correction and conditional lemmas, without theorem promotion.
