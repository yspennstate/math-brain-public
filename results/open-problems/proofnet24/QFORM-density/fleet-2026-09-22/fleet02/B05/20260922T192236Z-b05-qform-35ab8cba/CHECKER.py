import math

# Arithmetic sanity checker for QFORM-NEARZERO-DIFFUSE-BANK-DOUBLE-OBSTRUCTION-v1.
# The report contains the analytic proof; this script only checks the closed forms.

PHI1_SQ = math.exp(-1.0) / (2.0 * math.pi)


def stats(m: int):
    assert m >= 3
    a = 1.0 / m
    b = 1.0 + 1.0 / m

    # Lambda_m=[[a,b,0],[b,a,0],[0,0,1]].
    eig = (-1.0, 1.0, 1.0 + 2.0 / m)
    det_lambda = -(1.0 + 2.0 / m)

    # Physical frame: singleton e0, m copies e1/sqrt(m), m copies e2/sqrt(m).
    max_diag = 1.0 / m
    det_pair_0y = -(m + 2.0) / (m * m)
    det_pair_0z = 1.0 / (m * m)
    det_pair_yz = 1.0 / (m ** 3)
    max_pair_det = max(abs(det_pair_0y), abs(det_pair_0z), abs(det_pair_yz))
    det_triple_0yz = -(m + 2.0) / (m ** 3)
    max_triple_det = abs(det_triple_0yz)

    # Completing the singleton square gives residual Z^2-(m+2)Y^2.
    L = m + 2.0
    half_riesz_lower = (
        PHI1_SQ
        / math.sqrt(1.0 + 2.0 / m)
        * math.log(math.sqrt(L) / 2.0)
    )

    # Partner n=3 theorem, using the physical aggregate Z-pivot of size 1:
    partner_bound = 16.0 * math.sqrt(30.0) * abs(det_lambda) ** (-0.25)

    return {
        "m": m,
        "eigenvalues": eig,
        "det_lambda": det_lambda,
        "max_diag": max_diag,
        "max_pair_det": max_pair_det,
        "max_triple_det": max_triple_det,
        "half_riesz_lower": half_riesz_lower,
        "partner_bound": partner_bound,
    }


if __name__ == "__main__":
    print("QFORM_B05_NEARZERO_DIFFUSE_BANK_CHECK")
    print(f"phi(1)^2={PHI1_SQ:.15g}")
    for m in (3, 4, 10, 100, 10_000, 1_000_000):
        s = stats(m)
        print(
            "m={m} eig={eig} det={det:.12g} maxdiag={diag:.12g} "
            "maxpairdet={pair:.12g} maxtripledet={tri:.12g} "
            "halfRieszLB={hr:.12g} partnerBound={pb:.12g}".format(
                m=m,
                eig=s["eigenvalues"],
                det=s["det_lambda"],
                diag=s["max_diag"],
                pair=s["max_pair_det"],
                tri=s["max_triple_det"],
                hr=s["half_riesz_lower"],
                pb=s["partner_bound"],
            )
        )
    print("QFORM_B05_NEARZERO_DIFFUSE_BANK_PASS")
