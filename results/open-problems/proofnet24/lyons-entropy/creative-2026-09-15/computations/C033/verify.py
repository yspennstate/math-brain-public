"""Reproduce C033's exact certificates and finite verification record."""

import json
from pathlib import Path
from exact_transport import (
    C, F, assert_diamonds, closed_floor_transport, edge_deletion_transport, laws,
    maxflow_transport, positive_transport, rational_frame,
    serial_weights, verify_hall_sos,
)


ROOT = Path(__file__).resolve().parent


def law_json(law):
    return [{"set":list(s), "probability":str(p)} for s,p in sorted(law.items())]


def main():
    tests = []
    for n,real in [(3,False),(4,False),(5,False),(6,False),
                   (8,False),(12,False),(5,True),(6,True)]:
        frame = rational_frame(n,real=real)
        bottom,left,top,middle = laws(frame)
        answer,augmentations = maxflow_transport(left,top)
        assert_diamonds(frame,answer)
        closed,closed_floor,uniform_gap,closed_augmentations = closed_floor_transport(frame)
        assert_diamonds(frame,closed)
        tests.append({"n":n, "real":real, "case":"rational_unitary",
                      "augmentations":augmentations,
                      "positive_weights":sum(x > 0 for x in answer.values()),
                      "all_w_coordinates_nonzero":all(x > 0 for x in bottom.values()),
                      "all_U_minors_nonzero":all(x > 0 for x in left.values()),
                      "all_V_minors_nonzero":all(x > 0 for x in top.values()),
                      "closed_positive_floor":str(closed_floor),
                      "proved_uniform_Hall_gap":str(uniform_gap),
                      "closed_floor_all_weights_positive":True,
                      "all_diamond_marginals_verified":True})

    for n in (3,5,7):
        frame = [[C(int(i == j)) for j in range(3)] for i in range(n)]
        bottom,left,top,middle = laws(frame)
        answer,augmentations = maxflow_transport(left,top)
        assert_diamonds(frame,answer)
        assert sum(x > 0 for x in answer.values()) == 1
        tests.append({"n":n, "case":"coordinate_degeneracy",
                      "augmentations":augmentations,
                      "all_diamond_marginals_verified":True})

    canonical_tests = []
    positive_tests = []
    sos_checks = 0
    certificate = None
    for n in (3,4,5):
        frame = rational_frame(n)
        bottom,left,top,middle = laws(frame)
        canonical = edge_deletion_transport(left,top)
        assert_diamonds(frame,canonical)
        canonical_tests.append({"n":n,
                                "positive_weights":sum(x > 0 for x in canonical.values()),
                                "sum_min_formula_verified":True})
        positive,epsilon,slack,augmentations = positive_transport(left,top)
        assert_diamonds(frame,positive)
        positive_tests.append({"n":n, "epsilon":str(epsilon),
                               "minimum_nontrivial_Hall_slack":str(slack),
                               "all_incidence_weights_positive":True})
        sos_checks += verify_hall_sos(frame)
        if n == 4:
            certificate = {
                "description":"Exact fully complex four-site rank-one diamond certificate",
                "frame_columns":["w","u","v"],
                "frame_entries_real_imag":[[z.json() for z in row] for row in frame],
                "bottom":law_json(bottom), "hidden_pair_law":law_json(left),
                "top":law_json(top), "aggregate_middle":law_json(middle),
                "canonical_weights":serial_weights(canonical),
                "positive_weights":serial_weights(positive),
                "positive_floor":str(epsilon),
                "minimum_nontrivial_Hall_slack":str(slack),
                "closed_positive_floor":str(closed_floor_transport(frame)[1]),
            }
    result = {"status":"PASS", "arithmetic":"exact Gaussian rational / Fraction",
              "maxflow_cases":tests, "sum_min_cases":canonical_tests,
              "positive_floor_cases":positive_tests,
              "Hall_families_checked":sos_checks,
              "Hall_SOS_identities_checked":2*sos_checks,
              "uniform_Hall_gap_inequalities_checked":sos_checks-6,
              "scope":"Finite checks verify the implementations; all-parameter theorems are proved in agents/C033.md."}
    (ROOT/"certificate.json").write_text(json.dumps(certificate,indent=2)+"\n")
    (ROOT/"verified_output.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))


if __name__ == "__main__":
    main()
