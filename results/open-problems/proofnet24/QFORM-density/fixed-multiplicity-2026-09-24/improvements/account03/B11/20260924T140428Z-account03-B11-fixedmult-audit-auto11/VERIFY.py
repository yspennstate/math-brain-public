#!/usr/bin/env python3
"""Finite constant checks for the s8 split-row logarithmic endpoint.
Not a proof certificate; the analytic proof is in S8_SPLITROW_LOG_ENDPOINT.md.
"""
import json
import math


def main():
    delta = 97/100 - (297*math.sqrt(2) + 3*math.sqrt(202))/4000
    kappa = 1/6400
    xi = (delta**2/2) * kappa**2
    packet = xi / 3**6
    inv8 = packet**(-1/8)
    cstar = math.e * inv8
    ustar = math.pi * cstar
    threshold = math.exp(-2)/cstar
    front = math.e*cstar

    assert delta > 0.8543
    assert 8.909e-9 < xi < 8.911e-9
    assert 1.222e-11 < packet < 1.223e-11
    assert inv8 < 23.127
    assert cstar < 62.865
    assert ustar < 197.494
    assert threshold > 0.002152
    assert front < 170.883

    rank2 = {str(r): math.gamma(r+1)**(1/r) for r in (2,3,4,8,16,32)}
    result = {
        "status": "PASS",
        "delta_star": delta,
        "kappa": kappa,
        "xi2_terminal_lower": xi,
        "three_color_packet_product_lower": packet,
        "packet_product_inverse_eighth": inv8,
        "C_star": cstar,
        "U_star": ustar,
        "small_interval_threshold": threshold,
        "small_ball_front_eC": front,
        "rank2_Lr_examples": rank2,
        "limitations": [
            "Finite arithmetic checks only; not a proof certificate.",
            "The split-row determinant theorem and terminal-collar theorem are proved in their source-pinned artifacts."
        ]
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
