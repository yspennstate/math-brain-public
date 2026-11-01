import math


def benchmark(m):
    gamma = 2.0
    logm = math.log(m)
    sigma = m ** (-1/3)
    q = logm / (4*m)
    mu_row = m*q
    mu_col = gamma*m*q
    # Deterministic occupancy cutoff L=4 log m.
    L = 4*logm
    # Worst of row/column means is mu_col = (1/2) log m.
    # Chernoff: P(Bin(n,q)>=L) <= (e*mu/L)^L.
    # Union over <=3m rows+columns for gamma=2.
    log_union_occ = math.log(3*m) + L*math.log(math.e*mu_col/L)
    k = math.sqrt(m)
    s1 = m*sigma*sigma / math.log(math.e/sigma)
    s2 = k*(math.log(m)+math.log(math.e/sigma))/m
    # Avoid catastrophic cancellation: (1-q)^m = exp(m log1p(-q)).
    log_clean_prob = m*math.log1p(-q)
    clean_aspect = gamma*math.exp(log_clean_prob)
    predecessor_mu = gamma*m*q  # latest theorem required this -> 0
    # Earlier global-defect theorem required N*m*q=o(k).
    global_defect_ratio = gamma*m*m*q/k
    # 2D high-frequency Fourier tail prefactor, c=0.01 as a sanity benchmark.
    log_2d_tail_c001 = 2*math.log(1/sigma) - 0.01*m*sigma*sigma
    return dict(
        m=m, q=q, mu_row=mu_row, mu_col=mu_col, L_over_k=L/k,
        log_union_occ=log_union_occ, S1=s1, S2=s2,
        clean_aspect=clean_aspect, predecessor_mu=predecessor_mu,
        global_defect_ratio=global_defect_ratio,
        log_2d_tail_c001=log_2d_tail_c001
    )


print("CRITICAL_MASK_PARTIAL_ROW_CHECKER")
print("gamma=2, k=sqrt(m), sigma=m^(-1/3), q=log(m)/(4m), L=4log(m)")
for m in (10**6, 10**9, 10**12, 10**18):
    r = benchmark(m)
    print(
        "m={m:.0e} q={q:.12g} mu_row={mu_row:.12g} mu_col={mu_col:.12g} "
        "L/k={L_over_k:.12g} log_occ_ub={log_union_occ:.12g} "
        "S1={S1:.12g} S2={S2:.12g} clean_aspect={clean_aspect:.12g} "
        "latest_mu={predecessor_mu:.12g} global_def_ratio={global_defect_ratio:.12g} "
        "log_2d_tail_c001={log_2d_tail_c001:.12g}".format(**r)
    )

# Exact/asymptotic identities used in the proof.
# e*mu_col/L = e/8, so the union-bound log is
# log(3m) + 4 log(m) log(e/8) = log 3 + [1+4 log(e/8)] log m,
# and 1+4 log(e/8)<0.
occ_power = 1 + 4*math.log(math.e/8)
assert occ_power < 0
print("occupancy_power =", repr(occ_power))

# S1 -> infinity and S2 -> 0 at the concrete scale.
assert benchmark(10**18)["S1"] > benchmark(10**12)["S1"] > benchmark(10**9)["S1"]
assert benchmark(10**18)["S2"] < benchmark(10**12)["S2"] < benchmark(10**9)["S2"]

# The latest predecessor condition mu=Nq->0 fails: here mu=(1/2)log m -> infinity.
assert benchmark(10**18)["predecessor_mu"] > benchmark(10**12)["predecessor_mu"]

# Clean rows have asymptotic aspect 2*m^(-1/4), hence o(1):
# row deletion cannot leave even m clean rows.
for m in (10**9, 10**12, 10**18):
    approx = 2*m**(-1/4)
    ratio = benchmark(m)["clean_aspect"]/approx
    assert 0.99 < ratio < 1.01
print("clean_aspect_ratio_to_2m^-1/4_at_1e18 =",
      benchmark(10**18)["clean_aspect"]/(2*(10**18)**(-1/4)))

# Fixed-depth convolutions remain atomic because the all-off/all-plus event
# has mass (q/2)^ell >0 for every finite m and fixed ell.
for ell in (1, 2, 3, 5):
    q = math.log(10**12)/(4*10**12)
    assert (q/2)**ell > 0
print("fixed_depth_atoms_positive = True")

print("ASYMPTOTIC_IDENTITIES:")
print("max row/column defects = O_P(log m) = o(sqrt(m))")
print("m sigma^2/log(e/sigma) -> infinity")
print("k[log m+log(e/sigma)]/m -> 0")
print("N q ~ (1/2)log m -> infinity: latest predecessor fails")
print("clean-row aspect ~ 2 m^(-1/4) -> 0: row thinning fails decisively")
print("sigma^-2 exp(-c m sigma^2) -> 0 for every fixed c>0")
print("ALL_CRITICAL_MASK_PARTIAL_ROW_CHECKS_PASS")
