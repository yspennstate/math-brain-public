# B02/A008: near-flat fiber means, fixed whole-spectrum code
Date: 2026-10-12 UTC. Status: AUTHOR-PROVED restricted-family theorem, independent review NOT_RUN, full FEI OPEN.
Native worker ownership: account02/B02; A008 is the mathematical packet. No new worker, schedule, deployment or public action.
This is a probability-reference / prefix-code theorem, NOT an actual posterior-forest generator. Nothing here is claimed native-ingested into Math Brain.

## Exact theorem

Fix t>=6 and integer m with 0<=m<=2^t-2t. Let A_t in F_2^{t x (2^t-1)} consist of all nonzero columns of F_2^t, and let g:F_2^m x F_2^t -> {+1,-1} be Boolean. For independent uniform z,x set f(z,x)=g(z,A_t x). Write h(z)=E_u[g(z,u)] and define
 q = E_z [1-h(z)^2] = sum_{b,v!=0} ghat(b,v)^2,
 eta^2 = Var_z h(z) = sum_{b!=0} ghat(b,0)^2.
Assume (i) g(z,.) is nonconstant for at least half of the z values, and (ii) eta^2<=q/4.

Then one fixed bias-independent, Fourier-law-independent, canonical prefix-free binary code for EVERY possible complete Fourier support of f has expected length L(f)<(8/3) I(f), and hence
 H(f) <= L(f) < (8/3) I(f).
It depends only on (t,m,A_t), not g, h, q, eta or an unknown Fourier distribution. Fourier entropy uses log_2 and 0 log(1/0)=0. This relaxes the previous flat-fiber-mean condition eta=0: nonzero variance of fiber means is permitted. It is a restricted-family result and does not establish full FEI.

## Complete mathematical proof

1. Because A_t has rank t, Ax is uniform and the Fourier transform transfers injectively via
 S(b,v)=supp(b) union {m+j:(A_t^T v)_j=1},
 fhat(S(b,v))=ghat(b,v); all other physical coefficients are zero. For v!=0 the simplex code A_t^T v has exactly d=2^{t-1} ones, so |S(b,v)|=d+|b|.
2. The nonempty physical Fourier-support classes are (LOW) v=0,b!=0 and (HIGH) v!=0. The empty class is b=v=0. Denote p_empty=ghat(0,0)^2=1-eta^2-q. The HIGH influence is I_high=sum_{b,v!=0}(d+|b|)ghat(b,v)^2. Exact total influence is I=I_high+sum_{b!=0}|b|ghat(b,0)^2 >= I_high and I>=d q.
3. Prescribe candidate binary codeword lengths:
    ell(empty)=1;
    ell(S(b,0))=m+2 when b!=0;
    ell(S(b,v))=ceil(7(d+|b|)/6) when v!=0.
   Each candidate label is a full physical support (not one gate or an individual coordinate). The lengths depend only on t,m,A_t.
4. The LOW Kraft sum is (2^m-1)2^{-(m+2)}<1/4 (also valid for m=0). The HIGH Kraft sum is
    K_high=(2^t-1) sum_{j=0}^m binom(m,j) 2^{-ceil(7(d+j)/6)}.
   Put a=9/20. Since 2^{-7/6}<a (equivalently 9^6*128>20^6), monotonicity gives
    K_high < 2^t a^d(1+a)^m
           <= (800/841)^t (7569/8000)^d
           < (19/20)^32 < 1/4
   for every t>=6 and m<=2d-2t. The final comparison is the exact integer inequality 4*19^32<20^32. The EMPTY Kraft term is 1/2. Thus total Kraft sum K<1.
5. Kraft-McMillan provides an injective prefix-free code with exactly these lengths. An explicit deterministic canonical construction sorts all (b,v) first by assigned length and then lexicographically, allocates the successive canonical binary prefix words of that length, and maps the decoded label (b,v) back to S(b,v). This is a complete decoder whose codebook is fixed by (A_t,t,m). No spectral data is transmitted as free side information.
6. Since ceil(a_real)<=a_real+1, its exact expected code length satisfies
    L <= (1-eta^2-q)*1 + (m+2)eta^2 + (7/6) I_high + q
      = 1+(m+1)eta^2+(7/6)I_high
      <= 1+(m+1)q/4+(7/6)I.
7. For each nonconstant t-bit Boolean fiber g(z,.), its variance is at least 4*2^{-t}(1-2^{-t}), since the mean is 1-2k/2^t for some 1<=k<=2^t-1. At least half of fibers are nonconstant, so
    q >= 2*2^{-t}(1-2^{-t}),
    I >= d q >= 1-2^{-t}.
   Combine step 6, m<=2d-2t and I>=d q:
    L/I <= 7/6+(m+1)/(4d)+1/(1-2^{-t})
         <= 8/3 - (2t-1)/(4d) + 1/(2^t-1)
         < 8/3.
   The last strict inequality follows from (2t-1)(2^t-1)>2^{t+1}, true for all t>=6. Shannon's source coding bound yields H(f)<=L(f). Q(S)=2^{-ell(S)}/K is also a normalized whole-set law with cross entropy L+log2 K < L.

## Strict scope and concrete genuinely nonflat example

For each t>=6,m>=1, choose k(z)=1+(popcount(z) mod 2) and E_z={3z+5j mod 2^t:0<=j<k(z)}. Define g(z,u)=-1 on E_z, +1 otherwise. Every fiber is nonconstant, the cardinalities of E_z vary (h is genuinely nonconstant), and the exact ratios eta^2/q are 1/374 at t=6 and 1/758 at t=7, satisfying eta^2<=q/4. This includes arbitrary growing address dependence while maintaining a fixed decoder. The assumptions restrict g; the construction does not prove a forest-run realization or universal FEI.

## Executed bounded validation (not an independent proof)

Environment: Python 3 standard library, exact integer Walsh-Hadamard / fractions, numerical binary logarithms. Command: python /tmp/b02_nearflat_fiber.py. No paid compute, RNG, test-bank data or protected evaluation material.
- 4 maximum-m exact Kraft sums (t,m)=(6,52),(7,114),(8,240),(9,494): 0.808105989991,0.755626192977,0.750054501419,0.750000005311, each <1.
- 7 complete integer Walsh/Parseval/spectral weight checks for (t,m)=(6,1),(6,2),(6,3),(6,4),(7,1),(7,2),(7,3): 7/7 PASS for the hypotheses, exact influence identity and prefix length inequality. Each entropy H computed numerically and was below exact L. All finite checks corroborate rather than prove the universal statement.
- For (t,m)=(6,1): q=187/2048, eta^2=1/4096, I=95/32, L=18127/4096, H approximately 1.008555580677 bits.
- Exact integer certificates: 4*19^32<20^32, 7569/8000<19/20, and 9^6*128>20^6 passed.

## Source pins, hypotheses, reuse, and remaining obligations

Observed repository heads at research time: math-research-brain/main ccf6b704a8a3ca31aef199f5c13db57d0d965eac; math-open-problems/master 4ba9d45a2d0a43ac6bb8e923bf107054319439b6.
Read exact source blobs: Brain scheduled_tasks/CURRENT_OBJECTIVE.md 3bc19ac1c6850a797409c6d4ddd47d65a2ea0d7e, scheduled_tasks/README.md 2293391fec923119d8c2d829e374aaa784586960, current ORDER.md 81b6d6f988aee4489512c6e62543253900620453, CASE_TARGETS.json 97e41262ebb4f09eec53630a918acae09efc9a48, owner relay original REQ-20261012T031958Z-FULL-FEI-OWNER--owner-relay-fei-control--send-r1.json 3290aff155f63dbc1a5c58ae58c3dc3d6254b508, and current A008 previous original account02/B02 high-syndrome-code REPORT.md bb01bbf564fd4ddadc0a5951ee9c4ceb8cb62347. Canonical open-problems reports/fei-2026-10-11/assignments/B02.json 29600a047ed321e39f4063c57f321dceeb387f13, CURRENT_STATUS.md c416d4b4a83fc67965cb95d06a0cc80c5c29a520 and EXECUTION_PROTOCOL.json 457358ff62cbf1141a72096bcabdf95bf18c1be2. No claims are based on held/protected test items.

Prior restricted-family constant-fiber-mean theorem (eta=0) had a sharper constant 34/21 for t>=6 but did not permit nonconstant h(z). This new result extends its hypothesis class at the cost of a larger coefficient and retains the growing-overlap simplex lift with m as large as 2^t-2t. Status: AUTHOR-PROVED, review NOT_RUN, acceptance UNVERIFIED, actual posterior-forest realization NOT_RUN, native Math Brain ingestion/retrieval NOT_RUN, receiver use/outcome UNVERIFIED. This report's repository persistence is only a source artifact, never ingestion.

Next exact step for packet A008, with A086/A094 as independent reviewers: test whether the high-syndrome canonical class can be represented by distinct admissible partition-forest runs with a uniform multiplicative comparison of their complete-set probabilities. Account explicitly for root, subset and attachment costs and genuine run normalization. If that fails, record a concrete representation-level obstruction without claiming to disprove full FEI.
