import json

# Source-bound diagnostic for account03/B06 report/checker blobs
# report: 102e3a54d5cac3a14afd00122e3d485d99a1b632
# checker: 4163d8856dd65ef7d8de8b01e2bf5a2bf03785e2
# Only the exact row needed for the diagnostic is repeated here.
T = 10
U = {6,7,8,9,10}
H = {0,1,2,3,4,5}
SSTAR = {11,12,13}
OLD_REMAINDER = {14,15,16,17}
U_PORT = 6
P = 11
OUT_T = {0,2,3,6,11,14,17}

assert len(OUT_T) == 7
assert U_PORT in OUT_T
# In the inherited globally-minimum packing U is chordless, so the universal
# degree count has at most one U-target plus four old-remainder targets.
universal_max_non_cross = 1 + len(OLD_REMAINDER)
universal_min_cross = 7 - universal_max_non_cross
assert universal_min_cross == 2

certificate_cross = sorted(OUT_T & (H | SSTAR))
certificate_clean_light = sorted(OUT_T & (SSTAR - {P}))
certificate_heavy = sorted(OUT_T & H)
assert len(certificate_cross) >= 2
# This exact peer certificate refutes the tempting stronger shortcut that the
# forced exits must include a light target different from p.
assert certificate_clean_light == []
assert certificate_heavy

payload = {
    "candidate": "BT4-R4-F3-SECOND-COLLAR-TWOEXIT-v1",
    "source_report_blob": "102e3a54d5cac3a14afd00122e3d485d99a1b632",
    "source_checker_blob": "4163d8856dd65ef7d8de8b01e2bf5a2bf03785e2",
    "universal_degree_budget": {
        "exact_outdegree": 7,
        "max_targets_on_chordless_U_plus_four_old_remainder_vertices": universal_max_non_cross,
        "min_targets_on_H_union_Sstar": universal_min_cross,
    },
    "peer_certificate": {
        "t": T,
        "outneighbors": sorted(OUT_T),
        "cross_targets_H_union_Sstar": certificate_cross,
        "clean_light_targets_Sstar_minus_p": certificate_clean_light,
        "heavy_targets": certificate_heavy,
        "stronger_always_clean_light_shortcut_refuted": True,
    },
    "result": "PASS",
}
print(json.dumps(payload, sort_keys=True, indent=2))
