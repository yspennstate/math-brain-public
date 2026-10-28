SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B12, 2026-09-23T17:47:33Z.

attacking: local-Krylov-shadow export of arbitrary signed spectral additions into an actual ORIGINAL-coordinate cross block, then consume the projected-crossing receiver on the partner's live physical partition.

# account03/B12 r38 — local-shadow profile export for arbitrary signed additions

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Additional eigenvalue control  
Run: `20260923T174733Z-qform-eigenvalue-r38`  
Status: **PROVED SUPPORTING STABILITY THEOREM / PARTNER APPLIED AT AN EQUATION / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Continuity: proved on the cross-block exits stated below; not proved for the unrestricted conjecture.

## 1. Scope and corrections retained

The target remains: for every `n`, independent real ORIGINAL-coordinate inputs `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove that `X^T A X` has a universally bounded density, or give a valid counterexample.

No Gaussianity, moments, compact support, connected support, log-concavity, iid assumption, diagonal-basis assumption, or post-rotation independence is used. In particular, no matrix remainder below is called a small random quadratic error merely because its operator norm is small. Operator norm is used only to preserve deterministic singular-value gates of the coefficient matrix. The false law-uniform pointwise quadratic-phase estimate, arbitrary-joint coarea cap, worst-fiber supremum route, and conditional-cap-as-independence shortcuts are not used.


The completed designated partner used here is account04/B12 run

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B12/20260923T171921Z-account04-B12-local-krylov-shadow-r5/REPORT.md`.

Its local-Krylov-shadow theorem is the first premise below. The new marginal-free physical third-volume theorem used later is account03/B20 r34, and the exact crossing receiver is the independently checked interactive `NEW_PROJECTED_CROSSING.md` theorem.

## 2. Partner premise: local Krylov shadow

Let `A0,S` be real symmetric, let `U=Ran(S)`, and let `H` be a set of ORIGINAL coordinates. Put

`K_H=P_H(U+A0 U)`, `q_H=dim K_H`.

The completed account04/B12 theorem proves that, for `k+q_H<=|H|`, and for a further symmetric `R` with `||R||op<=epsilon`, if

`A=A0+S+R`,

then

`sqrt(lambda_k((A^2)[H,H]))
 >= (sqrt(lambda_(k+q_H)((A0^2)[H,H]))-epsilon)_+`.                 (2.1)

The signs and magnitudes of every eigenvalue of `S` are unrestricted. Thus an unbounded signed packet is charged only through the dimension of its one-step physical shadow, while `R` is charged only through the deterministic coefficient norm needed to preserve the matrix gate.

## 3. New theorem: local-shadow self/cross profile export

Write the FINAL matrix in the ORIGINAL-coordinate cut `H | H^c` as

`A = [ C   M ; M^T   D ]`,

where `C=A[H,H]` and `M=A[H,H^c]`.

### Theorem 3.1 — `QFORM-LOCAL-SHADOW-PROFILE-EXPORT-v1`

Under the hypotheses of (2.1), define

`g_k=(sqrt(lambda_(k+q_H)((A0^2)[H,H]))-epsilon)_+`.                (3.1)

For every `p,t>=1` satisfying

`p+t=k+1`,

one has

`boxed: s_p(C)^2 + s_t(M)^2 >= g_k^2.`                              (3.2)

Equivalently, for every `theta in (0,1)`,

`N_C(theta g_k)+N_M(sqrt(1-theta^2) g_k) >= k`,                    (3.3)

where `N_T(a)=#{j:s_j(T)>=a}` and singular values are padded by zero.

This is a deterministic stability theorem for adding arbitrary smaller and larger signed eigenmodes: the large packet `S` is allowed unlimited magnitude, the small/dense packet `R` is paid only through the matrix spectral gate, and any protected square-spectrum that disappears from the final physical self block must appear in the literal ORIGINAL-coordinate crossing block.

### Proof

For every symmetric matrix, direct block multiplication gives the exact identity

`(A^2)[H,H]=C^2+MM^T`.                                               (3.4)

By (2.1),

`lambda_k(C^2+MM^T)>=g_k^2`.                                       (3.5)

For positive semidefinite matrices `X,Y`, Weyl's upper eigenvalue inequality says

`lambda_(p+t-1)(X+Y)<=lambda_p(X)+lambda_t(Y)`.                     (3.6)

Apply (3.6) with `X=C^2`, `Y=MM^T`, and `p+t-1=k`. Since

`lambda_p(C^2)=s_p(C)^2`, `lambda_t(MM^T)=s_t(M)^2`,

(3.5) and (3.6) give (3.2).

For (3.3), let `r=N_C(theta g_k)`. If `r>=k`, there is nothing to prove. Otherwise use (3.2) with `p=r+1`, `t=k-r`. Then `s_(r+1)(C)<theta g_k`, so

`s_(k-r)(M)^2 > (1-theta^2)g_k^2`,

which proves (3.3). QED.

### Important comparison with the previous r37 theorem

This theorem and r37's orthogonal spectral-completion theorem are complementary, not interchangeable. If an added packet is an orthogonal spectral completion satisfying `A0 S=0`, then r37 exploits the stronger positivity `A^2=A0^2+S^2` and pays no shadow-rank loss. The present theorem instead handles a generic signed packet that can interact with `A0`; it pays exactly the local one-step Krylov shadow `q_H` furnished by account04/B12.

## 4. High/low spectral split: arbitrary huge modes plus arbitrarily many small modes

Let an arbitrary symmetric addition have spectral expansion

`E=sum_j theta_j v_j v_j^T`.

For a threshold `h>=0`, split

`S_h=sum_(|theta_j|>h) theta_j v_j v_j^T`,

`W_h=sum_(|theta_j|<=h) theta_j v_j v_j^T`.

Then `||W_h||op<=h`. If `T` is any further symmetric coefficient tail with `||T||op<=delta`, put

`A=A0+S_h+(W_h+T)`,

`q_H(h)=dim P_H(Ran(S_h)+A0 Ran(S_h))`.

Applying Theorem 3.1 with `epsilon<=h+delta` gives, for `p+t=k+1`,

`boxed:
 s_p(A[H,H])^2+s_t(A[H,H^c])^2
 >= (sqrt(lambda_(k+q_H(h))((A0^2)[H,H]))-h-delta)_+^2.`            (4.1)

Thus:

- the eigenvalues `|theta_j|>h` may be arbitrarily large and have arbitrary signs;
- their magnitudes do not enter (4.1), only the local physical shadow dimension does;
- arbitrarily many remaining eigenvalues of either sign are admitted and cost only the spectral threshold `h`;
- no term `X^T S_h X` or `X^T W_h X` is treated as an independent convolution factor.

This is the direct additional-eigenvalue stability statement of this run.

## 5. Five-mode reserve: self core or continuously smoothing cross block

Take `k=5` in Theorem 3.1. If

`g:=sqrt(lambda_(5+q_H)((A0^2)[H,H]))-epsilon >0`,                  (5.1)

then choosing `p=t=3` gives

`boxed: s_3(C)^2+s_3(M)^2 >= g^2.`                                 (5.2)

Hence at least one of

` s_3(C)>=g/sqrt(2)`,                                               (5.3)

or

` s_3(M)>=g/sqrt(2)`                                                (5.4)

holds.

The cross alternative is already a complete analytic exit. The marginal-free physical third-volume theorem of account03/B20 r34 states that for every literal ORIGINAL-coordinate cross block `M`, with

`Z_3=e_3(MM^T)>0`,

one has a continuous `C_0` density and

`||p_Q||infinity <= K_3 Z_3^(-1/6)`,

`K_3=3*2^(4/3)*exp(1/3)=10.5501688311...`.                         (5.5)

Since `Z_3>=s_1(M)^2s_2(M)^2s_3(M)^2>=s_3(M)^6`, (5.4) yields

`boxed: ||p_Q||infinity <= sqrt(2) K_3/g
                         =14.9201918464.../g.`                      (5.6)

No row-volume marginal gate survives. The self alternative (5.3) is an actual physical principal block with three large singular values, but in unbounded `|H|` it is not by itself a full target closure; invoking the target recursively would be circular. Thus (5.2) is a clean reduction rather than an overclaim.

## 6. Required equation-level application of account04/B12

Use the partner's concrete carrier. Split `R^16=H direct_sum J`, with `|H|=|J|=8`, and

`A0 = [ 0    2 I_8 ;
       2 I_8  0   ]`.                                               (6.1)

Let `f1,f2` be two ORIGINAL coordinate vectors in the outside bank `J` and let

`S=tau_1 f1 f1^T + tau_2 f2 f2^T`,                                 (6.2)

where `tau_1,tau_2` are arbitrary real numbers with no magnitude bound. Let `T` be arbitrary symmetric with

`||T||op<=1/4`,                                                     (6.3)

and put `A=A0+S+T`.

Account04/B12 proves for this exact physical bank that

`q_H=dim P_H(Ran(S)+A0 Ran(S))=2`.                                 (6.4)

Also `(A0^2)[H,H]=4 I_8`. Substituting (6.4) into Theorem 3.1 with `k=5`, `epsilon=1/4` gives the actual inequality

`g=sqrt(lambda_7(4I_8))-1/4=2-1/4=7/4`,

and therefore

`boxed: s_3(A[H,H])^2+s_3(A[H,J])^2 >=49/16.`                      (6.5)

This is a direct use of the completed designated-partner theorem at an equation, not a generic citation.

If only the cross branch of (6.5) is used, (5.6) already gives the continuous bound

`||p_Q||infinity <= sqrt(2)K_3/(7/4)
                  =8.52582391221...`.                              (6.6)

In this particular family there is a sharper direct physical inequality. Since `S` is entirely inside the `J,J` self block,

`A[H,J]=2I_8+T[H,J]`,

and `||T[H,J]||op<=1/4`. Thus every one of its eight singular values satisfies

`s_8(A[H,J])>=7/4`.                                                 (6.7)

Now apply the independently checked exact-rank crossing theorem from `NEW_PROJECTED_CROSSING.md` to the ACTUAL partition `H|J`. Both banks consist of exactly eight ORIGINAL coordinates, so their joint product densities are at most one and remain so after the orthogonal SVD coordinates on each eight-dimensional bank. All self-block quadratic terms, including the arbitrary unbounded packet (6.2), are absorbed into the theorem's arbitrary functions `F` and `G`. Therefore

`||p_Q||infinity
 <= 8/(8-2) * (prod_(j=1)^8 s_j(A[H,J]))^(-1/8)
 <= 4/3 * (7/4)^(-1)
 = boxed: 16/21
 =0.7619047619....`                                                 (6.8)

The Fourier envelope in that theorem is integrable, so this branch has a continuous `C_0` density.

Moreover, arbitrary additional ORIGINAL coordinates may be appended with completely arbitrary self spectrum and arbitrary couplings to `H` and `J`: condition on those outside original coordinates. Their couplings become affine terms inside `F` and `G`, while the literal `H,J` cross block (6.7) remains unchanged. Hence (6.8) tolerates arbitrary additional outside eigenvalues and either sign without any convolution argument. Arbitrary further additions confined to the `H,H` or `J,J` self blocks are likewise free because the exact crossing theorem allows arbitrary internal functions.

The only additions that can degrade (6.8) are those whose actual coefficient footprint changes the protected `H,J` crossing block; those are quantified by its final singular values rather than by any supposed independence of their quadratic contribution.

## 7. Finite deterministic checks

A deterministic checker for Theorem 3.1 generated 10,000 random symmetric instances with:

- `n=13`, `|H|=9`, `k=5`;
- generic symmetric baselines `A0`;
- one or two arbitrary signed update modes with magnitudes sampled in `[-100,100]`;
- local shadow dimension computed from `P_H(U+A0U)`;
- an independent dense symmetric matrix scaled to operator norm `epsilon` sampled in `[0,0.35]`.

All 10,000 instances satisfied

`s_3(C)^2+s_3(M)^2 >=
 (sqrt(lambda_(5+q_H)((A0^2)[H,H]))-epsilon)_+^2`.

There were **zero violations**. The smallest observed numerical margin was `0.5610936251842147`; the median margin was `2.1119555917309`. These are consistency checks only; the proof is the analytic argument in Section 3.

## 8. Remaining implication

The full QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**.

The new theorem pays arbitrary signed additions once a physical carrier has enough square-spectrum reserve after the local-shadow budget. What is still missing from the bare hypothesis `s_3(A)>=1` is a universal product-preserving mechanism forcing one of:

1. a bounded physical carrier with enough reserve after `q_H` is paid;
2. a literal cross block with quantitative third volume (now fully paid by the marginal-free E3 theorem);
3. one of the already developed grouped-bank, hub, ridge, overlap-square, or three-cut common-plane receivers.

The newest account02/B20 three-cut compressor shows another surviving geometry: three physical banks whose cross tails are simultaneously near rank two and live near a common `2+2+2` coefficient-plane triangle. The theorem here does not delete those nonzero tails; a next step should combine the local-shadow profile with that common-plane retained-tail geometry.

Continuity is proved in (5.6) and (6.8), but not for the self-core survivor or the unrestricted theorem.

## 9. Sources and provenance

- Fresh brain control at start: `7a0d97f43e2bd0ed8e16b1b09df220eea4805924`; prepublication refresh: `fd833b8e184d76d66929db61837a07f3ca3c7574`.
- Fresh math-open-problems head observed during source refresh: `cbbf02361424fcf02504cf6f7f786aef1760bc8a`.
- Designated partner: `proofnet24/QFORM-density/fleet-2026-09-22/account04/B12/20260923T171921Z-account04-B12-local-krylov-shadow-r5/REPORT.md`.
- Marginal-free E3 receiver: `math-open-problems@a23ddf469392d77526db53d0811248a52a84d088`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B20/20260923T164400Z-account03-B20-QFORM-r34/REPORT.md`.
- Projected crossing: `math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401`, `proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.
- Latest three-cut synthesis consumed: `math-open-problems@cbbf02361424fcf02504cf6f7f786aef1760bc8a`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B20/20260923T172757Z-account02-B20-QFORM-auto11/REPORT.md`.

Repository transport is not native learned-memory ingestion; this run remains `WITHOUT_VERIFIED_BRAIN`. The changed-file allowlist contains only this worker's mathematical report/check files and its own brain handoff/status/memory artifacts. No credentials, account tokens, private personal material, or unrelated data are included. No repository-local privacy scanner is exposed through the current connector, so the privacy check is limited to manual inspection of this explicit allowlist.
