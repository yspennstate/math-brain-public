SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B03, 2026-09-23T19:16:57Z.
attacking: the diffuse near-coloop / exact angular packet by treating the whole projected selector bank jointly; derive a dependence-safe squared-time estimate and test whether its natural Jacobian scale can be forced by the target spectrum.

# account02/B03 — joint-projection Plancherel, sharper angular collision bound, and a target-valid scale obstruction

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Role:** Decoupled time integral / complementary constructions and source-valid counterexamples  
**Status:** `NEW SUPPORTING THEOREM + SHARPER CRITICAL COLLISION CERTIFICATE + TARGET-VALID SCALE OBSTRUCTION / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture remains open. This run keeps the whole independent-copy difference and does not separate any conjugate sum/difference variables. No moment, support, log-concavity, diagonal-basis, conditional-cap, or post-rotation independence assumption is used.

## 1. Fresh source boundary


Required pinned source: `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, directory `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`, especially `RESULTS.md`. I use its one-coordinate completion kernel at an actual inequality in Section 5.

Fresh projected-crossing source: `proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md` on current master. It supplies the source-valid projection bound `||p_{PX}||_infinity <= 2^{r/2}` for an orthonormal r-dimensional projection of an original cap-one product vector.

Designated partner: account03/B03 `20260923T181128Z-account03-B03-QFORM-r36/REPORT.md`. I apply its completed effective-dimension Riesz compiler to the new angular envelope in Section 4. The partner's critical rank-two result is not treated as a one-copy L-infinity theorem.

## 2. Joint-projection / joint-coefficient Plancherel theorem

The previous selector compiler required a bank of physical independent selector coordinates. For the angular packet the natural selector is instead a *joint orthogonal projection* of a product bank. The correct statement is still simple if the selector bank is kept intact.

### Theorem 2.1 — `QFORM-JOINT-PROJECTION-COEFFICIENT-PLANCHEREL-v1`

Let `Z in R^k` be independent of a background `W`, and assume Z has a joint density `f_Z` with

    ||f_Z||_infinity <= M_Z.

Let `C=C(W) in R^k` have a joint density `g_C` with

    ||g_C||_infinity <= M_C.

No independence is assumed among the coordinates of C, and C may be arbitrarily dependent on the rest of W. Let `B` be an invertible real `k x k` matrix, let `P:R^k->R` be arbitrary measurable, and let `R(W)` be arbitrary measurable. Define

    Q = R(W) + P(Z) + 2 Z^T B C(W).                                  (2.1)

Then for every `t != 0`,

    boxed:
    |phi_Q(t)|^2
      <= min{1, M_Z M_C pi^k |det B|^{-1} |t|^{-k}}.                (2.2)

Consequently, with

    A_k = M_Z M_C pi^k |det B|^{-1},                                (2.3)

for every `0<gamma<k`,

    boxed:
    int_R |t|^{gamma-1}|phi_Q(t)|^2 dt
      <= [2k/(gamma(k-gamma))] A_k^{gamma/k}.                        (2.4)

For `k>1`, Q has an L2 density and

    boxed:
    ||p_Q||_2^2 <= [k/(pi(k-1))] A_k^{1/k}.                          (2.5)

Thus, for an independent copy Q',

    boxed:
    P(|Q-Q'|<=eps)
      <= [2k/(pi(k-1))] A_k^{1/k} eps.                               (2.6)

For `k>2`, direct Fourier inversion gives a continuous `C_0` density with

    boxed:
    ||p_Q||_infinity
      <= [k/(pi(k-2))] A_k^{1/k}
      = [k/(k-2)](M_Z M_C/|det B|)^{1/k}.                            (2.7)

The critical `k=2` case gives L2, linear *collision* small ball and every weighted squared-time integral below exponent 2, but (2.2) alone does not give one-copy L-infinity.

### Proof

For fixed t define the twisted joint Fourier transform

    F_t(xi)=int_R^k f_Z(z) exp(i t P(z)+i xi.z) dz.                  (2.8)

Conditioning only on the whole background,

    phi_Q(t)=E_W[exp(i t R(W)) F_t(2t B C(W))].                     (2.9)

Cauchy--Schwarz over the **whole** W gives

    |phi_Q(t)|^2
      <= E_W |F_t(2tBC(W))|^2
      <= M_C int_R^k |F_t(2tBc)|^2 dc.                              (2.10)

The deterministic change `xi=2tBc` and Plancherel give

    (2.10)
      <= M_C |det(2tB)|^{-1} int |F_t(xi)|^2 dxi
      =  M_C |det(2tB)|^{-1}(2pi)^k int f_Z(z)^2 dz
      <= M_Z M_C pi^k |det B|^{-1}|t|^{-k}.                         (2.11)

The phase P is completely arbitrary because it is unimodular inside the L2 norm. Splitting the integrals at `T=A_k^{1/k}` proves (2.4)-(2.7). For (2.6), the density of `Q-Q'` is `p_Q * p_{-Q}` and has supremum at most `||p_Q||_2^2`; an interval of radius eps has length `2eps`.

The independent-copy identity is retained only in its whole-variable form

    |phi_Q(t)|^2 = E exp(i t (Q-Q')).                               (2.12)

No coordinate sum/difference pair is declared independent. QED.

## 3. Exact angular packet: the coefficient Jacobian cancels the physical pivot scale

Take the exact angular packet used by the designated partner,

    Q = a^{-1}(H_0 + beta Z_1 + m Z_2)^2 + 2 sigma U Z_1,           (3.1)

where

    H_0 = a X_i + h_L.X_L + h_K.X_K,                                (3.2)
    U   = u.X_L,                                                     (3.3)
    Z_1 = v.X_R,   Z_2=q.X_R,                                       (3.4)

`u,v,q` are unit vectors, `q perpendicular v`, the banks are disjoint original-coordinate product banks, `a !=0`, and `m sigma !=0`. There is no assumption on beta or on the dependence of H_0 and U.

Set `Z=(Z_1,Z_2)`. The current projected-crossing source gives the source-valid joint projection cap

    ||p_Z||_infinity <= 2.                                           (3.5)

Expand (3.1) as

    Q = a^{-1}H_0^2
        + a^{-1}(beta Z_1+mZ_2)^2
        + 2 Z_1(beta H_0/a + sigma U)
        + 2 Z_2(m H_0/a).                                            (3.6)

Thus Theorem 2.1 applies with `B=I_2` and coefficient vector

    C=(beta H_0/a + sigma U, m H_0/a).                               (3.7)

The joint density of `(H_0,U)` satisfies

    p_{H_0,U}(h,u_0) <= |a|^{-1} p_U(u_0)                            (3.8)

in the Radon--Nikodym sense: condition on every variable except the genuine independent physical coordinate `X_i`, and use its density cap one. Since U is a one-dimensional orthogonal projection of a cap-one product bank,

    ||p_U||_infinity <= sqrt(2),                                     (3.9)

hence

    ||p_{H_0,U}||_infinity <= sqrt(2)/|a|.                           (3.10)

The linear map `(h,u)->C` has determinant

    det [[beta/a, sigma],[m/a,0]] = -sigma m/a.                      (3.11)

Therefore

    boxed:
    ||p_C||_infinity <= sqrt(2)/(|sigma| m).                         (3.12)

The pivot coefficient a and the shear beta cancel exactly. Inserting (3.5) and (3.12) into Theorem 2.1 yields

### Corollary 3.1 — `QFORM-ANGULAR-JOINT-BANK-COLLISION-v1`

    boxed:
    |phi_Q(t)|^2
      <= min{1,
          2^{3/2} pi^2 (|sigma|m)^{-1}|t|^{-2}}.                    (3.13)

Equivalently,

    |phi_Q(t)|
      <= min{1,
          2^{3/4} pi (|sigma|m)^{-1/2}|t|^{-1}}.                    (3.14)

This improves the coefficient `2pi(|sigma|m)^{-1/2}` in the partner's generic exact-rank-two crossing certificate by using the additional genuine-pivot density inside the *coefficient-vector* law rather than treating both sides only through the universal two-dimensional projection cap.

## 4. Apply the designated partner result at an actual inequality

Apply account03/B03 r36 Lemma 2.1, its completed effective-dimension Riesz compiler, to (3.14) with `d=2` and

    K=2^{3/4} pi (|sigma|m)^{-1/2}.                                  (4.1)

Then

    boxed:
    int_R |t|^{-1/2}|phi_Q(t)|^2 dt
      <= (16/3) 2^{3/8} sqrt(pi) (|sigma|m)^{-1/4}                   (4.2)

with numerical outer constant

    12.2591374008.                                                    (4.3)

Using the exact whole-copy Riesz identity from the same partner report,

    int_R |t|^{-1/2}|phi_Q(t)|^2 dt
      = sqrt(2pi) E|Q-Q'|^{-1/2},                                   (4.4)

we obtain

    boxed:
    E|Q-Q'|^{-1/2
      <= (16/3)2^{-1/8}(|sigma|m)^{-1/4}
      =4.89068823042... (|sigma|m)^{-1/4}.                           (4.5)

Also, direct integration of (3.13) gives

    boxed:
    ||p_Q||_2^2 <= 2^{7/4}(|sigma|m)^{-1/2},                         (4.6)

and therefore the actual linear collision estimate

    boxed:
    P(|Q-Q'|<=eps)
      <= 2^{11/4}(|sigma|m)^{-1/2} eps
      =6.72717132203... (|sigma|m)^{-1/2} eps.                       (4.7)

Every quantity in (4.2)-(4.7) is obtained without splitting a conjugate sum/difference pair. This is a direct application of the designated partner's completed result to the new envelope.

The same partner report's critical translation-uniform half-Riesz receiver also improves numerically here: from (3.14),

    sup_s E|Q-s|^{-1/2}
      <= 12.0067774299... (|sigma|m)^{-1/4}.                         (4.8)

This is useful if the packet appears beside a genuinely disjoint extra physical square. The exact packet itself does not automatically contain such an unused square, so (4.8) is not promoted to a one-copy L-infinity claim.

## 5. Target-valid obstruction: `|sigma|m` is not a spectral exit scale

The natural coefficient-Jacobian scale in (3.13) cannot be forced from the owner target. This is already visible in four original coordinates.

For `0<eta<=1`, take independent arbitrary cap-one real variables `X,W,U,V` and

    Q_eta=(X+eta W)^2+2UV.                                           (5.1)

Its quadratic matrix, in the order `(X,W,U,V)`, is

    A_eta = [[1,eta,0,0],
             [eta,eta^2,0,0],
             [0,0,0,1],
             [0,0,1,0]].                                             (5.2)

The spectrum is exactly

    {1+eta^2, 1, -1, 0}.                                             (5.3)

Thus `s_3(A_eta)=1` for every eta: this is an exact unrestricted owner-target family. It is the angular packet with

    a=1, sigma=1, m=eta, beta=0.                                    (5.4)

Hence the new critical certificate (4.7) deteriorates like `eta^{-1/2}` and (4.5) like `eta^{-1/4}` although the target spectral scale is fixed. Therefore the implication

    s_3(A)>=1  ==>  |sigma|m >= c                                   (5.5)

is false even in an exact rank-three packet. The joint-bank compiler is a real analytic gain but its Jacobian scale is not by itself the missing universal structural certificate.

This is *not* a counterexample to QFORM. In fact the same family is uniformly paid by the pinned completion mechanism, as follows.

### 5.1 Exact product residual estimate

For independent U,V with densities at most one and

    R=2UV,                                                           (5.6)

conditioning on U gives, for every shift s and every `0<rho<=1`,

    P(|R-s|<=rho | U=u) <= min{1,rho/|u|}.                           (5.7)

Among all probability densities bounded by one, the expectation of the symmetric decreasing function `min(1,rho/|u|)` is maximized by density one on `[-1/2,1/2]`. Hence

    sup_s P(|R-s|<=rho)
      <= 2 rho log(e/rho),        0<rho<=1.                          (5.8)

The layer-cake identity then gives

    sup_s E|R-s|^{-1/2}
      = sup_s int_0^infinity P(|R-s|<t^{-2}) dt
      <= 1 + int_1^infinity 2t^{-2}(1+2log t) dt
      = 7.                                                           (5.9)

For general sigma, scaling gives

    sup_s E|2sigma UV-s|^{-1/2} <= 7 |sigma|^{-1/2}.                 (5.10)

### 5.2 Actual application of the required pinned e5 result

Pinned `RESULTS.md` Lemma 3 (one-coordinate completion) gives, if

    T=d[Z+h]^2+R,

with Z a genuine independent cap-one physical coordinate,

    p_T(s) <= |d|^{-1/2} E|s-R|^{-1/2}.                              (5.11)

Apply (5.11) to (5.1) using the original physical coordinate X: `d=1`, `h=eta W`, and `R=2UV`. Equations (5.9)-(5.11) give the actual one-copy inequality

    boxed:
    ||p_{Q_eta}||_infinity <= 7                                     (5.12)

for every `0<eta<=1` and **every** independent cap-one input law. Thus the family that makes the new collision/Jacobian certificate diverge is nevertheless uniformly controlled by another completed, source-valid mechanism.

This is the useful obstruction: a global proof must switch receivers as `m` collapses; it cannot demand one lower bound on the coefficient-Jacobian scale `|sigma|m` throughout the angular packet.

## 6. What is now paid and what remains

Paid in this run:

1. A whole-bank Plancherel theorem for a joint projected selector vector and a fully dependent joint coefficient vector, with arbitrary internal phases on both sides.
2. In the exact angular packet, the genuine pivot gives the sharper coefficient density cap `sqrt(2)/(|sigma|m)` and hence the critical envelope (3.13).
3. The designated partner's Riesz compiler converts that envelope to the explicit dependence-safe bounds (4.2)-(4.7), including linear collision small-ball scale.
4. The owner-target family (5.1) proves that `|sigma|m` is not target-controlled, while the pinned one-coordinate completion theorem pays the same family uniformly by (5.12).

The first unpaid implication is therefore narrower and genuinely one-copy/structural:

`QFORM-ANGULAR-MECHANISM-SWITCH-v1`:

> In every remaining exact or approximate angular survivor at target scale, extract product-preservingly either (i) a square-plus-bilinear receiver with `|a sigma|` bounded below at usable scale, (ii) a grouped square/crossing receiver exploiting the transverse q-direction when the aggregate coefficient `m^2/|a|` is large, or (iii) an already-paid exact-coloop/ridge/three-volume exit. The transition cannot be based solely on `|sigma|m`, since (5.1)-(5.5) refute that structural shortcut.

The current Claude `(SP)` conditional-adaptation proposal remains open and is not used. The later affine-shear logarithmic tube correction is preserved. The full QFORM conjecture and unrestricted continuity remain **OPEN**.