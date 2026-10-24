SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B05, 2026-09-23T20:54:21Z.
attacking: the punctured same-source shear interface; test whether the b->0 loss is caused by the shear itself or specifically by sharing the multiplier L with the transverse bank, and spend account02/B05's Borel null-hub receiver at the first exact inequality.

# account01/B05 auto16 — independent-multiplier convolution lift removes the punctured shear loss

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** quadratic coarea bound / equivalent interval bound preserving arbitrary product densities.  
**Status:** `NEW SUPPORTING THEOREM / PARTNER RESULT APPLIED / PRECISE MISSING FACTOR IDENTIFIED / FULL QFORM OPEN`.  
**Regularity:** essential boundedness is proved in the theorem below; continuity is not claimed. Full-target continuity remains OPEN.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. First essential implication

The immediately preceding B05 work showed that conditioning on one physical square coordinate pays a factor `(max_j v_j^2)^(-1/3)`, while compressing first to `(L,V,P)` can incur an unbounded mixed-Renyi factor. The newest account02/B05 two-bank theorem pays every fixed nonzero light coupling `b`, but its bound deteriorates like `|b|^(-1/3)` while the exact endpoint `b=0` is bounded. That leaves a punctured small-coupling interface.

This run isolates the missing structural factor. The shear `2bLP` itself is harmless, even when `P` and the square variable `V` are arbitrarily dependent. The punctured loss appears only when the multiplier `L` shares its original-coordinate source with `(P,V)` (or when an `L^2` pivot prevents the absorption below).

## 2. Main theorem

### Theorem — `QFORM-INDEPENDENT-MULTIPLIER-SHEAR-ABSORPTION-v1`

Let `H,L` be independent real random variables, mutually independent of a random pair `(P,V)`. Assume

`||f_H||_infinity <= m_H`, `||f_L||_infinity <= m_L`,

and assume only that `V` has a density with

`||p_V||_infinity <= K_V`.

No joint density of `(P,V)` is required. Let `t,lambda !=0` and let `b,c,beta,eta,gamma` be arbitrary real numbers. Define

`Q = 2 t H L + 2 b L P + 2 c L V + lambda V^2 + beta L + eta V + gamma`.       (2.1)

Then `Q` has an essentially bounded density and

`boxed{
 ||p_Q||_(infinity,ess)
 <= C_* (m_L m_H K_V/|t|)^(2/3) |lambda|^(-1/3),
}`                                                                    (2.2)

where `C_*=7.761982175235...` is the constant in account02/B05's proved theorem `QFORM-NULL-HUB-TRANSVERSE-SQUARE-v1`.

In particular, suppose `H,L,X_1,...,X_m` are independent with density caps at most one, and `V=sum v_j X_j` has `sum v_j^2=1`. The standard one-dimensional bounded-density projection inequality gives `K_V<=sqrt(2)`, so

`boxed{
 ||p_Q||_(infinity,ess)
 < 7.762*2^(1/3)|t|^(-2/3)|lambda|^(-1/3)
 < 9.780 |t|^(-2/3)|lambda|^(-1/3).
}`                                                                    (2.3)

The estimate is uniform in `b`, including `b=0` and `b->0`, and uniform in the law and size of `P`. Thus no support, moment, connected-support, Gaussian, log-concavity, or post-rotation independence assumption enters.

### Proof

Complete the square in the only genuine square variable. Put

`W = V + eta/(2 lambda)`.

Then

`lambda V^2 + eta V = lambda W^2 - eta^2/(4 lambda)`,

and

`2 c L V = 2 c L W - (c eta/lambda)L`.

Set

`beta_0 = beta - c eta/lambda`,

`S = tH + bP + cW + beta_0/2`.

Then the quadratic form becomes exactly

`Q = 2 L S + lambda W^2 + gamma - eta^2/(4 lambda)`.          (2.4)

The key point is that the pair `(S,W)` has a bounded two-dimensional density although `(P,W)` need not have one. Since `W` has density `p_W(w)=p_V(w-eta/(2lambda))`, disintegrate the law of `P` conditionally on `W=w` as `nu_w(dp)`. Because `H` is independent of `(P,W)`, for almost every `w` the conditional law of `S` given `W=w` is the convolution of `tH` with the pushforward of `nu_w` under `p -> bp+cw+beta_0/2`. Therefore it has a density bounded pointwise by

`||f_(tH)||_infinity <= m_H/|t|`.

Consequently `(S,W)` has a joint density satisfying

`boxed{
 p_(S,W)(s,w)
 = p_W(w) integral f_(tH)(s-bp-cw-beta_0/2) nu_w(dp)
 <= (m_H/|t|) p_W(w)
 <= m_H K_V/|t|.
}`                                                                    (2.5)

This argument remains valid if `P` and `V` are collinear or otherwise singular as a pair; no two-dimensional density of `(P,V)` is assumed.

Now use the independence of `L` from `(H,P,V)`: it implies

`L independent of (S,W)`.                                             (2.6)

Apply account02/B05's completed `QFORM-NULL-HUB-TRANSVERSE-SQUARE-v1` to (2.4), with its independent hub equal to the present `L`, its dependent pair equal to `(S,W)`, pair-density cap

`M <= m_H K_V/|t|`,

hub-density cap `m=m_L`, and transverse square coefficient `c_2=lambda`. The partner theorem yields

`||p_Q||_(infinity,ess)
 <= C_* (M m_L)^(2/3)|lambda|^(-1/3)
 <= C_* (m_L m_H K_V/|t|)^(2/3)|lambda|^(-1/3)`,

which is (2.2). QED.

## 3. A target-valid family: the entire puncture is paid

Take independent cap-one physical coordinates `H,L` and an independent product bank `X`. Let `P,V` be two orthonormal linear forms of that bank and set

`Q_b = 2HL + 2bLP + V^2`.                                            (3.1)

In the orthonormal linear-coordinate basis `(H,L,P,V)`, its homogeneous matrix is

`B_b = [[0,1,0,0],
        [1,0,b,0],
        [0,b,0,0],
        [0,0,0,1]].`                                                  (3.2)

Its spectrum is

`boxed{ spec(B_b) = {+sqrt(1+b^2), -sqrt(1+b^2), 0, 1}. }`            (3.3)

Hence every real `b`, including arbitrarily small nonzero `b`, satisfies the exact three-large-eigenvalue target. Theorem 2 with `t=lambda=1`, `m_H=m_L=1`, `K_V<=sqrt(2)` gives

`boxed{ ||p_(Q_b)||_(infinity,ess) < 9.780 }`                          (3.4)

uniformly for all `b in R` and all admissible rough product laws.

This is stronger on this family than applying the newest account02/B05 two-bank curved-tube theorem directly, whose displayed nonzero-coupling branch carries a `|b|^(-1/3)` loss. There is no contradiction: that theorem permits `L` itself to share both product banks with `(P,V)`, while (2.6) is the exact extra structure used here.

## 4. What factor was actually missing

Equation (2.5) identifies the useful coarea currency. The point is not a cap on `(P,V)`. It is the **convolution lift in the coefficient paired with the multiplier**:

`H independent of (P,V)`

turns the possibly singular pair `(P,V)` into a bounded pair `(tH+bP+cV,V)` with cap `<=m_H K_V/|t|`; then

`L independent of (H,P,V)`

lets the partner null-hub coarea theorem spend this cap without any conditional-fiber supremum.

Thus the exact first unpaid implication is now

`QFORM-SHARED-MULTIPLIER-CONVOLUTION-LIFT-v1`:

> replace (2.5)-(2.6) by a product-preserving interval/coarea estimate when `L,P,V` are simultaneous linear forms of the same two original-coordinate product banks. It must remain uniform as `b->0`, must aggregate the bank structure before any conditional density supremum, and must tolerate arbitrary fragmented/unbounded cap-one laws. A separate nonzero `L^2` pivot also remains outside Theorem 2 because absorbing it into `S` would make `S` depend on the multiplier `L` and destroy (2.6).

This formulation explains why the latest two-bank curved tube is close but still loses `|b|`: in that source-shared setting the exact independence that made (2.5) a free convolution is absent. Small `bP` cannot be treated as a small random perturbation without moments.

## 5. Relation to current corrections

The proof uses no pointwise oscillatory decay, no arbitrary-joint quadratic coarea lemma, no independence after rotation, no conditional-density supremum, and no interval-to-Borel promotion. The only smoothing bound is the genuine convolution with the independent scalar `H`, followed by account02/B05's already-proved Borel null-hub receiver. The theorem therefore survives the current correction set.

The theorem does not prove the full QFORM conjecture because a general spectral reduction does not produce an original-coordinate scalar `L` independent of the bank carrying `(P,V)`, and a general pivot may leave an `L^2` term. The full target remains OPEN. The additional continuous-density conclusion is also NOT PROVED in this branch.

## 6. Sources actually used

- Fresh control: `yspennstate/math-research-brain` main, OWNER CONTROL revision `2026-09-22.15`, programme `QFORM-DENSITY-3EIG-20260922`; current continuation `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`.
- Designated partner theorem: account02/B05, `QFORM-NULL-HUB-TRANSVERSE-SQUARE-v1`, report `proofnet24/QFORM-density/fleet-2026-09-22/account02/B05/20260923T200516Z-account02-B05-QFORM-auto11c/REPORT.md`; theorem constant `C_*=7.761982175235...`.
- Newest designated-partner comparison: account02/B05, commit `5b7cf251ab2c7533eed306b2c9eb8859f52ff6f0`, report `proofnet24/QFORM-density/fleet-2026-09-22/account02/B05/20260923T203105Z-account02-B05-QFORM-auto11d/REPORT.md`, `QFORM-TWOBANK-HUB-DENSITY-v1`.
- Fresh two-bank curved-tube source: `proofnet24/QFORM-density/interactive/20260923T202245Z-two-bank-curved-tube/REPORT.md`.
- Immediate B05 predecessor: commit `8a0e1e276065a2e77a9276f5d1e78666c3e86aeb`, physical-square extraction / mixed-Renyi obstruction.

## 7. Scope and next action

**Proved this run:** a uniform full-line essential-density bound for the exact-null independent-multiplier family (2.1), with arbitrary same-source shear `P` and without requiring `(P,V)` to have a joint density; target-valid family (3.1) is uniformly paid through `b=0`.

**Not proved:** the source-shared multiplier case; nonzero multiplier-square pivot; unrestricted full QFORM; full-target continuity.

**Next mathematical step:** attack `QFORM-SHARED-MULTIPLIER-CONVOLUTION-LIFT-v1` by keeping a two-bank decomposition until after the `H`-convolution and proving a shell estimate directly for `2L(tH+bP+cV)+lambda V^2`, rather than conditioning on `L` or taking a pair-density supremum. The desired replacement should interpolate the exact `b=0` Borel square receiver with the nonzero-b curved tube without a reciprocal power of `b`.

Manual changed-file review found only mathematical text and repository paths in this report; no credentials, private personal data, financial material, or unrelated content are present. No external secret-scanner executable was invoked. No schedule, notification, permission, visibility, public release, cross-account authentication, or paid-model/API state was changed.