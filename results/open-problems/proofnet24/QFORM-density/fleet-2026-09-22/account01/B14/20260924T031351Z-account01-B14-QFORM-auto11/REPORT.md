SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B14, 2026-09-24T03:13:51Z.
attacking: coherent two-sided pre-Plancherel localization — retain arbitrary slice-bank and slope-bank localization labels until the corresponding complex transforms are reassembled, so distant fragments and translations pay only aggregate whole-law certificates rather than fragmentwise endpoint norms.

# account01/B14 — coherent two-sided pre-Plancherel localization

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T031351Z-account01-B14-QFORM-auto11`  
Assignment: translations and localization  
Status: **NEW SUPPORTING LOCALIZATION THEOREM + STRICT TARGET APPLICATION + TWO-SIDED PROOF-ORDER BARRIER / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted theorem remains OPEN. Nothing below uses moment bounds, bounded supports, connectedness, finite fragment count, centering, post-rotation independence, arbitrary-joint coarea, or the known-false law-uniform pointwise quadratic Fourier decay.

## 1. Fresh source and mechanism change


- repository/commit: `yspennstate/math-open-problems@b376a5b911fdf54fef212829f376ab301e2561a3`;
- path: `proofnet24/QFORM-density/fleet-2026-09-22/account02/B14/20260924T025846Z-account02-B14-QFORM-auto11/REPORT.md`;
- theorem: `QFORM-PREPLANCHEREL-COHERENT-PARTITION-v1`.

The partner proves that arbitrary localization of the slope bank is zero-tax if the phase-weighted slope pieces are reassembled before the second Plancherel norm. In particular, one need not require a fragmentwise cap `L_j <= m_j L_0`; that condition was sufficient only for the proof order that applies the endpoint theorem separately to each piece.

This run proves the symmetric statement on the slice side and combines both sides. The key new rule is:

`localize both banks freely -> reassemble both complex transforms -> take the two L2/Plancherel norms -> pay the endpoint integral`.

No fragmentwise density or Fourier constants are needed.

## 2. The coherent two-sided theorem

Let `X` be a probability variable with density `f_X<=1`.

Let `mu` be a finite positive measure on `(L,Y)` of mass

`n=mu(R^2)`, `0<n<=1`,

independent of `X`, with disintegration

`mu(dl,dy)=nu_l(dy) dl`.

For `t!=0`, put

`F_t(l)=int exp(i t y) nu_l(dy)`

and suppose the **aggregate** frozen transform satisfies

`esssup_l |F_t(l)| <= A |t|^(-1/2)`.                              (2.1)

Let `tau` be a finite positive measure of mass

`m=tau(Omega)`, `0<m<=1`,

on a second independent bank `Z`. Let `S(Z),R(Z)` be arbitrary measurable real functions. Assume the **aggregate** positive slope pushforward has density

`S_#tau(ds)=h(s)ds`, `||h||_infinity<=M`.                          (2.2)

Let `eta` be the finite output measure of

`Q=H(X)+2XL+Y+2X S(Z)+R(Z)`,                                      (2.3)

where `H` is arbitrary measurable.

### Theorem `QFORM-TWO-SIDED-COHERENT-PREPLANCHEREL-LOCALIZATION-v1`

The measure `eta` has a continuous density vanishing at infinity and

`boxed:
 ||p_eta||_infinity
 <= 5 pi^(-1/5) A^(2/5) M^(2/5) (nm)^(3/5).`                     (2.4)

Moreover, (2.4) is unchanged under arbitrary finite or countable positive decompositions

`mu=sum_j mu_j`, `tau=sum_k tau_k`,

or soft/randomized decompositions by measurable nonnegative weights summing to one, provided the labels are carried algebraically and the corresponding phase-weighted transforms are reassembled **before** the two Plancherel norms. No individual fragment constants `A_j` or `M_k` are required.

### Proof

The slice bank first. Define the aggregate complex `L`-pushforward density `F_t` above and

`G_t(x)=int exp(2itxl) F_t(l) dl`.

Because

`|F_t(l)| <= nu_l(R)`,

we have

`||F_t||_1 <= int nu_l(R) dl = n`.                                (2.5)

Together with (2.1),

`||F_t||_2^2 <= A n |t|^(-1/2)`.                                 (2.6)

With the Fourier convention of the partner theorem and the change of variable `xi=2tx`, Plancherel gives

`||G_t||_2^2 = (pi/|t|)||F_t||_2^2
              <= pi A n |t|^(-3/2)`,                              (2.7)

hence

`||G_t||_2 <= sqrt(pi A n)|t|^(-3/4)`.                            (2.8)

Now the slope bank. Push the complex measure `exp(itR(z))tau(dz)` forward through `S`; denote its density by `g_t`. Total variation is dominated by the positive pushforward `h(s)ds`, so

`|g_t(s)|<=h(s)`, `||g_t||_1<=m`, `||g_t||_infinity<=M`,

and therefore

`||g_t||_2^2<=mM`.                                                 (2.9)

Put

`K_t(x)=int exp(2itxs)g_t(s)ds`.

The second Plancherel identity gives

`||K_t||_2 <= sqrt(pi m M)|t|^(-1/2)`.                            (2.10)

The exact hub factorization is

`hat eta(t)=int f_X(x) exp(itH(x)) G_t(x)K_t(x) dx`.

Since `f_X<=1`, Cauchy--Schwarz, (2.8), and (2.10) imply

`|hat eta(t)|
 <= pi sqrt(A M n m)|t|^(-5/4).`                                  (2.11)

The total mass of `eta` is `nm`, so also

`|hat eta(t)|<=nm`.                                                (2.12)

For `B,C>0`, splitting at `t_0=(C/B)^(4/5)` gives the exact integral

`int_R min(B,C|t|^(-5/4))dt = 10 C^(4/5)B^(1/5).`                (2.13)

Apply (2.13) with

`B=nm`, `C=pi sqrt(A M n m)`.

Fourier inversion yields

`||p_eta||_infinity
 <= (1/(2pi))*10*pi^(4/5)(AMnm)^(2/5)(nm)^(1/5)
 =5 pi^(-1/5)A^(2/5)M^(2/5)(nm)^(3/5)`,

which is (2.4). Integrability of the Fourier transform gives a continuous `C_0` density.

For the partition assertion, write the phase-weighted slice transform as

`F_t=sum_j F_{j,t}`

and the phase-weighted slope pushforward density as

`g_t=sum_k g_{k,t}`.

Countable sums converge in total variation because the pieces are positive submeasures of finite total mass. If one first reassembles these sums, equations (2.5)-(2.12) see only the aggregate positive measures `mu` and `tau`. Thus the proof is literally independent of the number, masses, locations or geometry of the labels. QED.

## 3. Arbitrary translations with no moment or support tax

The preceding theorem gives a useful translation corollary that is stronger than cellwise mass-homogeneity.

Let `(L_0,Y_0)` be independent of an arbitrary random element `T`; let `L_0` have density at most one and suppose

`Phi(t)=E exp(itY_0)`, `|Phi(t)|<=A_0|t|^(-1/2)`.

For arbitrary measurable translations/phases `a(T),b(T)`, put

`L=L_0+a(T)`, `Y=Y_0+b(T)`.

Then the aggregate frozen transform is

`F_t(l)=Phi(t) E[f_(L_0)(l-a(T)) exp(itb(T))]`,

so

`esssup_l |F_t(l)|<=A_0|t|^(-1/2)`                                (3.1)

with no bound on `a(T),b(T)` and no moment or support assumption on `T`.

Similarly, let `S_0` have density cap `M_0`, let `U` be arbitrary and independent, and put

`S=S_0+c(U)`

for arbitrary measurable `c`. Then the aggregate slope density is a convolution of `p_(S_0)` with a probability measure, so

`||p_S||_infinity<=M_0`.                                           (3.2)

An arbitrary additional phase `R(S_0,U)` is harmless because the phase-weighted pushforward is dominated in total variation by the positive pushforward.

Therefore arbitrary countable partitions of `T` and `U`, arbitrary distant fragments, arbitrary translations and unbounded supports may be carried as labels and erased by coherent reassembly with **exactly the same constant** as the unsplit law. This is not a bounded-diameter or fixed-fragment-count reduction.

## 4. Actual strict-target inequality from the completed account02/B14 theorem

Take independent

`X,L,Z,Y ~ Uniform[0,1]`

and

`Q=2X(L+Z)+Y^2`.                                                    (4.1)

In original independent coordinates `(X,L,Z,Y)`, the homogeneous matrix is

`A_* = [[0,1,1,0],
        [1,0,0,0],
        [1,0,0,0],
        [0,0,0,1]]`,                                               (4.2)

with spectrum

`{sqrt(2),-sqrt(2),1,0}`.                                          (4.3)

Thus (4.1) is genuinely in the owner's exact three-large-eigenvalue target.

Use `(L,Y^2)` as the slice bank and `Z` as the slope bank. Set

`I(t)=int_0^1 exp(it y^2)dy`.

I claim

`|I(t)|<=2|t|^(-1/2)` for all `t!=0`.                              (4.4)

For `0<|t|<=1`, this follows from `|I(t)|<=1`. For `T=|t|>1`, let `r=T^(-1/2)`. The interval `[0,r]` contributes at most `r`. On `[r,1]`, integration by parts using

`d exp(iTy^2)=2iTy exp(iTy^2)dy`

gives

`|int_r^1 exp(iTy^2)dy|
 <= 1/(2T)+1/(2Tr)+(1/(2T))int_r^1 y^(-2)dy
 =1/sqrt(T)`.                                                       (4.5)

Hence (4.4).

The frozen slice transform is

`F_t(l)=1_[0,1](l) I(t)`,

so the completed account02/B14 theorem applies with the **actual aggregate** constant

`A=2`.

The slope is `S(Z)=Z`, whose density cap is

`M=1`.

Applying the completed partner theorem therefore yields the concrete target-level inequality

`boxed:
 ||p_Q||_infinity
 <= 5 pi^(-1/5) 2^(2/5)
 = 5.24749493498713... .`                                          (4.6)

The density is continuous and vanishes at infinity. This improves the earlier `A=4` symmetric-interval stress certificate for this particular legal target law; it is not a claim about the sharp universal QFORM constant.

By conditioning on arbitrary additional outside original coordinates, any ambient extension whose retained principal block is (4.2) and whose additional terms become affine in these four retained variables inherits the same bound whenever the overlap factorization is preserved. More generally, the translation corollary in Section 3 allows arbitrary translated auxiliary banks before the two aggregate certificates are paid.

## 5. New two-sided proof-order obstruction

The preceding law also shows why the earlier cellwise double-fragment compiler, although correct, is the wrong final interface.

Let

`ell_j = j^(-3/2)/zeta(3/2)`, `j>=1`,

and partition `[0,1]` into adjacent intervals `J_j` of lengths `ell_j`. Partition **both** `L` and `Z` using these intervals.

For the slice piece `L in J_j`, its mass is

`n_j=ell_j`,

while

`F_(j,t)(l)=1_(J_j)(l) I(t)`.

Any constant `A_j` satisfying

`esssup_l |F_(j,t)(l)|<=A_j |t|^(-1/2)` for all `t!=0`

must obey, at `t=1`,

`A_j>=|I(1)|>=Re I(1)>=cos(1)>0`.                                 (5.1)

Thus the slice endpoint constant does **not** carry a positive power of the fragment mass.

For the slope piece `Z in J_k`, its mass is

`m_k=ell_k`,

but its unnormalised slope density is exactly `1_(J_k)`, so the minimal cap is

`M_k=1`.                                                           (5.2)

If one applies the previous two-sided subprobability endpoint theorem separately to every `(j,k)` cell and then sums, the coefficient contains

`sum_(j,k) A_j^(2/5)M_k^(2/5)(n_jm_k)^(3/5)`

which, by (5.1)-(5.2), is bounded below by

`cos(1)^(2/5)
 [zeta(3/2)^(-3/5) sum_j j^(-9/10)]^2
 = +infinity`.                                                      (5.3)

So the fragment-first positive endpoint compiler becomes literally vacuous on this simple compact connected-support target law.

Nothing happened to the actual distribution. Reassemble the same slice pieces to recover `F_t=1_[0,1]I(t)` before the first Plancherel step, and reassemble the same slope pieces to recover `h=1_[0,1]` before the second. The coherent theorem immediately restores the finite bound (4.6).

For `N` equal pieces on each side the contrast is quantitative: the fragment-first cell compiler grows like `N^(4/5)`, while coherent reassembly remains exactly `5 pi^(-1/5)2^(2/5)`.

This is `QFORM-TWO-SIDED-FRAGMENT-FIRST-ENDPOINT-DIVERGENCE-v1`. It is a **proof-order obstruction, not a counterexample to QFORM**.

## 6. What is now resolved and what remains

For the overlap/two-Plancherel chamber, pure support localization is no longer an obstruction on either active bank. Arbitrary labels, remote fragments and translations may be introduced for bookkeeping and then erased coherently before the relevant L2 norm. The whole-law constant is preserved exactly and no fragmentwise mass-homogeneity hypothesis is necessary.

The remaining debt is structural, not measure-theoretic: from the bare condition `s_3(A)>=1`, force a product-preserving overlap representation with a whole aggregate half-order slice certificate and a whole aggregate slope-density certificate, or enter one of the other completed ridge/physical-E3/pair/receiver/Schur/grouped-bank chambers. The newest account03/B19 frontier shows that a strong physical rank-two crossing can still leave a heavy-six/adaptively aligned same-bank survivor; coherent localization prevents proof-order losses there but does not by itself manufacture the missing aggregate slope.

Full unrestricted QFORM therefore remains OPEN / NOT PROVED / NOT DISPROVED.

## 7. Integrity

- Partner actually applied at equation (4.6): account02/B14 `QFORM-PREPLANCHEREL-COHERENT-PARTITION-v1`, source `b376a5b911fdf54fef212829f376ab301e2561a3`.
- New result: coherent **two-sided** pre-Plancherel localization and its translation corollary.
- New barrier: simultaneous slice/slope fragment-first endpoint summation can diverge although the unchanged law has the finite target bound (4.6).
- Uniform pointwise quadratic Fourier decay was not used.
- No rotation of random variables was used.
- No bounded support, moment, finite-fragment-count, or centeredness assumption is used in the theorem.
- Repository retrieval/write is not native learned-memory ingestion; execution remains `WITHOUT_VERIFIED_BRAIN`.
