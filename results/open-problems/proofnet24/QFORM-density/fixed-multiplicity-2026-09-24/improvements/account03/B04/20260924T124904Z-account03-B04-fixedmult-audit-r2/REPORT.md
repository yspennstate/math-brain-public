# account03/B04 r2 — nine-direction recheck and exact eight-direction terminal collar

Run: `20260924T124904Z-account03-B04-fixedmult-audit-r2`  
Owner objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Status: **NEW SUPPORTING THRESHOLD-8 REDUCTION; NINE-DIRECTION CANDIDATE STILL PENDING SECOND INDEPENDENT FULL REVIEW**.

## 1. Source boundary and nonduplication

The later owner objective supersedes the older slot prompt for this invocation. The pinned baseline is

- repository `yspennstate/math-open-problems`,
- source commit `7c0d6e60946b19423e6400a12d34b473cf0591e2`,
- manuscript blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`,
- path `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`.

This same worker already completed a full independent line-by-line audit of the 790-line baseline in the earlier same-hour run `20260924T121940Z-account03-B04-fixedmult-audit-r1`; that audit found the 17-eigenvalue theorem mathematically PASS, one nonfatal wording issue in the product-projection proof, and a repository-package reproducibility GAP because several README-advertised supplementary files were absent. I do not duplicate that audit here.

The earlier run also produced the candidate nine-eigenvalue theorem

`QFORM-FIXED-MULTIPLICITY-9-v1`:

> if the independent coordinate densities are bounded by `K`, `A=A^T`, and `s_9(A)>=s>0`, then every `X^TAX+b^TX+c` has an essentially bounded density with `||p||_infinity<=6010 K^2/s`.

Its new analytic inputs are a grouped product-Fourier compiler, a marginal-free `E_3` crossing-density receiver, and a marginal-free `E_2` half-potential receiver. I rechecked the delicate light-bank `L^2`/weighted-subset step in this run. The conditional-on-`X_I` mollified pushforward argument really does leave only an independent copy of `X_J`; pure `I` phases cancel, pure `J` phases have modulus one, and integrating the original independent `X_i` produces the stated scalar Fourier factors. The weighted-subset entropy identity

`H(w)+sum_i alpha_i log(alpha_i) <= ell log ell-log(ell!)`

follows by uniformly ordering the sampled `ell`-subset and applying entropy subadditivity. The constants in the `E_3` and `E_2` promotion trees then check.

A genuinely separate worker, account01/B16, subsequently reconstructed the whole nine-eigenvalue improvement and reported PASS at commit `54ec2a651d854563f8db0d92c4c3426f76551786`. Because this B04 run is the author-side follow-up, it is **not** a second independent review. The nine-direction theorem therefore remains `CANDIDATE_PENDING_SECOND_INDEPENDENT_FULL_REVIEW` under the owner protocol.

The account02/B08 audit at commit `98bf0cbd602c51f8b15a8b15b20ebf58ac27ba24` also supplies an exact family showing that the baseline completion bounds `rank R<=3r` and `rank R[L,L]<=r` are simultaneously sharp. Thus an eight-direction improvement cannot come merely from changing `3r` to `2r` or symmetrizing the interpolant.

The rest of this report isolates what the sharp completion forces at multiplicity eight.

## 2. Definitions and constants

Use the manuscript's parameters

`eta=1/100`, `kappa=1/80^2=1/6400`.

For `r>=1`, let

`V_r(A)=sum det(A[S,T])^2`,

where the sum is over ordered disjoint `r`-sets `S,T`. Define the global overlap-one third-minor energy

`Omega_1(A)=sum_{h,S,T} det(A[S union {h}, T union {h}])^2`,

where `|S|=|T|=2` and `S,T,{h}` are pairwise disjoint. Equivalently `Omega_1=sum_h M_{1,h}` in the notation of the previously proved overlap-one Schur packet.

Define also the three-bank two-sided collar energy

`Xi_2(A)=sum_{S,H,T} det(A[S,H])^2 det(A[H,T])^2`,

where `S,H,T` are pairwise disjoint two-sets and the triple is ordered.

Put

`epsilon_* = sqrt(18*kappa)=3 sqrt(2)/80`,

`c_* = 1-epsilon_*`,

and

`delta_* = (1-epsilon_*-eta)^2 - (sqrt(eta^2+eta)+epsilon_*)^2`.

Exact simplification gives

`delta_* = 97/100 - (297 sqrt(2)+3 sqrt(202))/4000`.

Numerically,

- `epsilon_*=0.05303300858899106433...`,
- `c_*=0.94696699141100893567...`,
- `delta_*=0.85433514019113377100...>0`.

## 3. The new structural theorem

### Theorem `QFORM-EIGHT-DIRECTION-TERMINAL-OVERLAP1-COLLAR-v1`

Let `A=A^T` have no `eta`-pivot in the manuscript's sense and assume

` s_8(A)>=1.`

Then one of the following alternatives holds.

1. **Third disjoint volume is already large:**

   `V_3(A)>=kappa^3`.

   Consequently a fair original-coordinate cut has `E_3>=4^(-3)kappa^3`, and the completed marginal-free third-volume product-Fourier receiver gives

   `||p_Q||_infinity <= 160 C_3 < 2400`,

   where `C_3=3 sqrt(2)e(9/2)^(1/6)=14.818337662843...`. This branch has a continuous `C_0` density.

2. **The exact eight-direction terminal collar is present:**

   `V_2(A)>=kappa^2`,

   `Omega_1(A) >= c_*^2 kappa^2`,

   and

   `Xi_2(A) >= (delta_*^2/2) kappa^2`.

Numerically the two new currencies obey

`Omega_1(A) >= 2.1893224678271921e-8`,

`Xi_2(A) >= 8.909772116276907e-9`.

Thus, after the nine-direction improvement, an eight-direction theorem is reduced to paying a quantitatively nonzero **overlap-one / two-sided physical collar**. The obstruction is not failure of volume: it is the need for a product-preserving analytic receiver for this overlap packet when the common physical diagonal can be zero or arbitrarily small.

### Proof

Assume `V_3<kappa^3`; we prove Alternative 2.

#### Step 1: the first two volume ratios cannot be small

First `V_1>=kappa`. Otherwise

`||off(A)|| <= ||off(A)||_F = sqrt(V_1)<sqrt(kappa)=1/80`,

while absence of a scalar pivot gives `||diag(A)||<eta=1/100`. Hence

`||A||<1/100+1/80<1`,

contrary to `s_8(A)>=1`.

Next, `V_2>=kappa V_1`. Suppose instead `V_2<kappa V_1`. Apply the manuscript's volume-sampled interpolation lemma at seed order `r=1`. There is a nonsingular disjoint one-by-one seed for which the completion

`A=D+R+E`

satisfies

`||E||<=||E||_F<2 sqrt(kappa)=1/40`,

`rank R<=3`, and `rank R[L,L]<=1`; moreover `D` is diagonal and vanishes on the seed coordinates.

Singular-value perturbation gives

`s_8(D+R)=s_8(A-E)>=39/40`.

Since `rank R<=3`, the manuscript's rank-shift inequality yields

`s_5(D)>=39/40`.

Hence at least five diagonal entries of `D`, all in `L`, have modulus at least `39/40`. Choose two of them, indexed by `H`. For `i in H`, since `E_ii=0` and `|A_ii|<eta`,

`|R_ii|>=39/40-1/100=0.965`.

For the one off-diagonal entry in each row,

`|R_ij|<=|A_ij|+|E_ij|<sqrt(eta^2+eta)+1/40=0.1254987562...`.

Thus `R[H,H]` is strictly row-diagonally dominant and therefore invertible, contradicting `rank R[L,L]<=1`. So

`V_2>=kappa V_1>=kappa^2`.

Since `V_3<kappa^3<=kappa V_2`, we have

`V_3/V_2<kappa`.                                                   (3.1)

#### Step 2: retain at least half of the order-two volume on good seeds

Sample each nonsingular disjoint two-by-two seed `B=A[S,T]` with probability

`det(B)^2/V_2`.

The manuscript's interpolation estimate at `r=2` gives

`E_B ||F_B||_F^2 <=9 V_3/V_2 <9 kappa`,

where `F_B=off(A[L,L]-P_B[L,L])` and

`P_B=A[:,T] B^(-1) A[S,:]`.

Let a seed be **good** when

`||F_B||_F^2<=18 kappa`.

Markov's inequality shows that good seeds carry at least one half of the determinant-squared sampling mass. Therefore

`sum_(B good) det(B)^2 >= V_2/2`.                                (3.2)

For a good seed, use the manuscript completion with `E[L,L]=F_B`. Put

`epsilon=||E||<=epsilon_*`.

Then `rank R<=6`, `R[L,L]=P_B[L,L]`, `rank R[L,L]<=2`, and

`s_8(D+R)=s_8(A-E)>=1-epsilon`.

The rank shift with `rank R<=6` yields

`s_2(D)>=1-epsilon`.

Hence there are two distinct indices `h_1,h_2 in L` such that

`|D_h|>=1-epsilon>=c_*`.                                        (3.3)

Let `H={h_1,h_2}`.

#### Step 3: every good seed emits two large overlap-one minors

For each selected `h in H`, the bordered-determinant identity is

`det A[S union {h}, T union {h}]
 = det(B) (A_hh-P_B,hh)
 = det(B) D_h`,                                                  (3.4)

because `E_hh=0` by construction.

Thus each good seed contributes two distinct overlap-one third minors with squared sum at least

`2 c_*^2 det(B)^2`.                                             (3.5)

There is no multiplicity loss when summing over seeds: an oriented overlap-one minor determines its common index `h`, then uniquely determines `S` and `T` by deleting `h` from its row and column sets. Summing (3.5) over good seeds and using (3.2),

`Omega_1(A)>=2 c_*^2 (V_2/2)=c_*^2 V_2>=c_*^2 kappa^2`.          (3.6)

This proves the first new currency.

#### Step 4: the same two anchors form a uniformly invertible interpolation collar

For the same good seed and `H`, diagonal entries of `P_B[H,H]` satisfy

`|P_hh|=|A_hh-D_h|>1-epsilon_*-eta`.                            (3.7)

For `h!=h'` in `H`,

`P_hh'=A_hh'-E_hh'`,

so the no-pivot entry bound and `|E_hh'|<=epsilon_*` give

`|P_hh'|<sqrt(eta^2+eta)+epsilon_*`.                            (3.8)

Therefore

`|det P_B[H,H]|
 >=(1-epsilon_*-eta)^2-(sqrt(eta^2+eta)+epsilon_*)^2
 =delta_*>0`.                                                    (3.9)

But the interpolation factorization is exact:

`P_B[H,H]=A[H,T] B^(-1) A[S,H]`.

Taking determinants in (3.9) gives

`|det A[S,H] det A[H,T]|
 =|det B| |det P_B[H,H]|
 >=delta_* |det B|`.                                             (3.10)

Squaring, summing one selected `H` for each good seed, and again using uniqueness of the ordered triple `(S,H,T)` and (3.2),

`Xi_2(A)
 >=delta_*^2 sum_(B good) det(B)^2
 >=(delta_*^2/2)V_2
 >=(delta_*^2/2)kappa^2`.                                        (3.11)

This proves Alternative 2 and the theorem. QED.

## 4. Consequence for multiplicity eight

The pivot cases of the nine-direction proof already work under `s_8>=1`:

- a scalar pivot leaves at least seven Schur directions; if the Schur complement has a pivot, the baseline pivot half-potential theorem needs only two directions, while if it has no pivot the new `E_2` half-potential route needs only `s_5>=1`;
- a definite pair pivot is paid directly;
- an indefinite pair pivot leaves at least six directions, far more than the one nonzero Schur direction needed by the logarithmic-potential argument.

Therefore **the only remaining multiplicity-eight branch is the no-pivot collar in Alternative 2**. In particular, an eight-direction proof no longer needs a better global rank bound or a generic `E_2` density theorem. It needs a theorem of the following precise kind:

`QFORM-EIGHT-OVERLAP1-TWOSIDED-COLLAR-RECEIVER-v1`:

> under the no-pivot hypotheses, convert the quantitative `Omega_1/Xi_2` packet above into a universal density bound while retaining arbitrary same-bank curvature and allowing every common diagonal `A_hh` to vanish.

Existing per-anchor overlap-one Schur receivers contain a factor involving the scalar pivot `A_hh` and therefore do not by themselves spend (3.6) in the exact-zero/near-zero chamber. The two-sided collar (3.10) records the extra structure available specifically at multiplicity eight and should be retained rather than collapsed to a single tiny pivot.

## 5. Scope and review state

- The baseline 17-eigenvalue manuscript remains mathematically PASS in this worker's completed earlier audit; no new defect was found here.
- The nine-eigenvalue improvement has now received one genuinely separate complete PASS review, account01/B16 at `54ec2a651d854563f8db0d92c4c3426f76551786`. A second independent full review is still required before owner-level promotion.
- The theorem in Section 3 is new supporting mathematics. It does **not** prove the eight-eigenvalue theorem by itself.
- The unrestricted three-eigenvalue conjecture remains open.
- Global continuity remains open. The `V_3` branch in Alternative 1 has a continuous `C_0` density; the unresolved collar branch has no claimed density conclusion yet.
- No Gaussian, log-concavity, moment, bounded-support, connected-support, diagonal-basis, post-rotation independence, arbitrary-joint coarea, or pointwise rough quadratic-phase decay assumption is used.
