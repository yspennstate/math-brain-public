# account03/B03 FEI handoff — repetition-code exceptional-set surgery

Recipient: `account01/B02`  
Programme: `FEI-ALL-TEAM-20260922T095941Z`  
Run: `20260922T111324Z-code-repetition-surgery`  
Status: `ESSENTIAL_STEP_APPLIED / FULL_FEI_OPEN`  
Brain: `WITHOUT_VERIFIED_BRAIN`.

## Source-bound mathematical result

Authoritative report:

- repository: `yspennstate/math-open-problems`
- creation commit: `bbab379c6344a9cefb57b0ce34843b7648e77d73`
- path: `proofnet24/P03-fei/fleet-2026-09-22/account03/B03/20260922T111324Z-code-repetition-surgery/REPORT.md`
- readback Git blob: `4d28b7c63e772fcadba61feedf4e96e92f12eae7`

Claim card:

- creation commit: `a6075ebf552d2508cbc0b254fb1365c3efeae0f0`
- path: `proofnet24/P03-fei/fleet-2026-09-22/account03/B03/20260922T111324Z-code-repetition-surgery/CLAIMS.json`
- readback Git blob: `f0d621525324c387557e8f50dded5c0618b29271`

### Theorem family

For the binary repetition code `C_n={0^n,1^n}` and

`F_n=chi_1(1-2 1_{C_n})`, `n>=3`, set `q_n=2^{2-n}`.

The exact normalized Walsh spectrum is

- `hat F_n({1}) = 1-q_n`,
- `hat F_n(S) = -q_n` for every other odd `S`,
- `hat F_n(S) = 0` for even `S`.

More generally, for any binary linear code `C` of codimension `r`, `V=C^perp`, and `a notin V`,

`hat F_{C,a}(s)=1_{s=a}-2^{1-r}1_{s in a+V}`,

and the exact signed xor convolution is `hat F * hat F = delta_0`. This is an actual Boolean identity, not an unweighted-L2 replacement.

For the repetition family the exact occurrence vector and influence excess are

`r=(1-q_n,q_n,...,q_n)`,

`J_n=I(F_n)-1=(n-2)q_n`.

The exact entropy is

`H_n=-(1-q_n)^2 log2((1-q_n)^2)+q_n(2-q_n)(2n-4)`.

Analytically, `H_n<5 J_n` for every `n>=3` and `H_n/J_n -> 4`.

### Decisive live-candidate result

For current candidate `SHAPED_EPS02268865`, whose balanced center is source-pinned as

`C_*=6.558445288811087`,

we therefore have for every `n>=3`

`D_*(F_n)=C_* J_n-H_n > (C_*-5)J_n > 0`,

and `D_*(F_n)/J_n -> C_*-4 = 2.558445288811087...`.

So this entire growing-distance `[n,1,n]` code-supported exceptional-set family cannot refute the live candidate. Preserve this positive child/descendant slack; do not set it to zero in a composition.

### Exact K_occ comparison

Applied other-account source:

`yspennstate/math-open-problems@603b35e74227d1c2d8ee34c0c527c439c686e30b:proofnet24/P03-fei/fleet-2026-09-21/account04/B17/20260922T092422Z-biased-booleanity-gap/REPORT.md`

(`B-BIASED-BOOLEANITY-GAP-v1`). For the same occurrence vector its exact positive I-projection root is

`1-c=(1-c(1-q_n))(1-c q_n)^{n-1}`, with `c>=1/2`.

Thus

`H_max=[h2(c(1-q_n))+(n-1)h2(cq_n)-h2(c)]/c`,

`K_occ=H_max-H_n`, and analytically

`K_occ/J_n = n-5+log2(e)+o(1)`.

Consequently no universal bound `K_occ <= A(I-1)` can hold on all balanced Boolean functions. This does not refute FEI; it shows the exact occupancy KL credit has an essential rare-event logarithm. In the exact decomposition `D=B_inf+K_occ`, this family has `B_inf/J_n=-n+O(1)` while `D/J_n` stays positive, so the large negative first-moment residual is genuinely canceled by exact KL.

## Collaboration provenance

Assigned partner `account04/B03` had no compatible completed current-program FEI handoff at the fresh startup or pre-publication scans. No older FOREST result was substituted and no peer PASS was fabricated. The assignment's named compatible `account04/B17` source above was therefore used asynchronously.

## Suggested recipient action

For `account01/B02`: use the general code transform `hat F=delta_a-2^{1-r}1_{a+C^perp}` as a design space. The next nontrivial test is a growing-size code/design support whose dual has several weight shells; optimize the dual-coordinate occurrence geometry against the exact balanced inequality `H <= C_*(I-1)` while retaining the exact signed convolution and canonical `K_occ`. The repetition family proves that exponentially rare code surgery can generate `K_occ/(I-1)~n` without threatening the current candidate.

Checker source SHA-256: `5585c35bcacec46d283d6f8046f21210aa12528d2c2976f25bb50dae3439eb29`; output SHA-256: `0089d37efa9308868975ce5e086c9613ddcf032e56ee1e7c67f837c30f0fb427`; executed result `PASS`.
