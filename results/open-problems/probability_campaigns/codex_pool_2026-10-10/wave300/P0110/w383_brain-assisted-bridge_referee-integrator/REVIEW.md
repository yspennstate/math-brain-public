# P0110 referee packet

## w381-L0 — KEEP as a narrowly scoped elementary lemma

Claim: For deterministic finite pairwise edge-disjoint edge sets and independent weights, measurable functions of the respective edge blocks are independent. Reproduction: each event `{f_i((tau_e)_{e in E_i}) in A_i}` lies in the coordinate sigma-field of `E_i`; independence of disjoint subfamilies gives the product identity. This does **not** cover random selected sets, overlapping paths, or conditioning on a common event. Independent reviewer: w383. Parent P0110 remains open/unknown. Source: `w381/CLAIMS.jsonl`, claim `w381-L0`; elementary product-measure fact.

## w382 scalar obstruction — KEEP as an abstract counterexample

Reproduction: For `B_n~Bern(n^-1/2)`, `X_n=n^1/2(B_n-n^-1/2)` has variance `n^1/2(1-n^-1/2)`, hence lower endpoint `chi_b=1/4`. The rare event `B_n=1` has probability `n^-1/2` and contributes at least `n^-1/2 exp((alpha/2)n^(1/2-s))` to the exponential moment for `s<1/2`, so `chi_a=1/2`. For `C_n~Bern(n^-1/4)` and `D_n=n^3/4 C_n`, the mean is `n^1/2`, hence `xi_b=1/2`; the rare event contribution `n^-1/4 exp(alpha n^(3/4-s))` diverges for `s<3/4`, so `xi_a=3/4`. Thus `chi_a=2xi_a-1` happens while both endpoint pairs differ. This refutes only a scalar inference; it is not an iid FPP construction. Independent reviewer: w383. Source: `w382/INDEPENDENT_OBSTRUCTION.md`.

## w381 L1–L5 — provisional KEEP, final audit pending script and source check

L1 follows from `h(mx)<=m h(x)` and Fekete. L2 follows by substituting `T=h+X=g+b+X` into passage-time additivity along a minimizing path; the terms `-b(z)-b(v-z)` have the favorable sign. L3: for a projection within `[0,v]`, convexity gives `S>=sqrt(L^2+4r^2)`; outside the segment, the distance to the closer endpoint is `r`, the other distance is at least `L` and at least `r`, so `S-L>=r>=2r^2/S`. L4: minimizing `g` over the Euclidean unit sphere yields `g(x)>=rho|x|`; coordinate rounding contributes at most `bd/2+rho sqrt(d)/2`. L5's union bound uses a deterministic lattice set of `O(n^d)` vertices and never treats the random geodesic vertex as an independent endpoint. The result supplies only a directional upper bound under explicitly assumed centered tails and terminal bias. It does not prove exponent existence or matching.

## w382 small displacement claim — KEEP; w381 candidate wording — FIX

If `a<=tau_e<=b<3a`, the direct edge from `0` to `e_1` costs at most `b`; every alternative nearest-neighbor path has at least three edges and costs at least `3a`. Hence the direct edge is the unique geodesic and `D(0,e_1)=0`. The Auffinger–Damron paper's printed (2.2) takes an infimum over all nonzero `v`, so its `xi_b` condition fails for Uniform[1,2]. Chatterjee's original A4 takes the infimum over `|v|>C`; this short-distance obstruction does not settle that asymptotic condition. The wording in w381's attempt calling Uniform[1,2] an eligible candidate for Auffinger–Damron Theorem 2.2 needs this caveat. This is a source-hypothesis correction, not a disproof of P0110. Independent reviewer: w383.

## w381 L8 and L9 — KEEP with abstract and conditional scope

L8: both `sqrt(n)/4` and `1+dist(n,{4^k})/4` change by at most `1/4` per integer step, so their minimum gives edge weights in `[3/4,5/4]`. Along `n=4^k`, `k>=2`, the amplitude `sigma_n` is 1. Along `n=2*4^k`, it is `sqrt(n)/4`. Thus the uniform exponential upper threshold is `a=1/2`, while the all-large-n variance lower threshold is `b=0`, despite concentration normalized by each actual standard deviation being exactly `exp(alpha)`. The shared sign makes this a dependent, nonstationary ray model; it cannot refute iid FPP exponent matching. Verdict KEEP for the abstract countermodel.

L9: the uniform normalized exponential bound plus `sigma(v)<=C_eta |v|^(chi+eta)` gives the upper envelope for every `q>chi`; the lower power envelope gives variance lower bounds for every `q<chi`. An exponential upper bound at any `q` bounds variance by `O(|v|^(2q))`, so a lower bound at `r>q` is impossible. Hence `chi_a=chi_b=chi`. Verdict KEEP as a sufficient conditional criterion. Neither normalized concentration nor two-sided uniform variance power regularity is proved for Uniform[1,2], and wandering matching remains open.
