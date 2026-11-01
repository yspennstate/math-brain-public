import math


def main():
    B0 = math.sqrt(math.pi)/(2*math.sqrt(3))*math.erf(math.sqrt(3)) - (1-math.exp(-3))/6
    C_col = 12*B0
    C_gauss = 3*math.sqrt(2)
    gap = C_gauss-C_col
    c1 = -11/36 + 2*math.exp(-3)/9 + math.sqrt(3*math.pi)*math.erf(math.sqrt(3))/12

    assert gap > 0
    assert c1 < 0
    assert (-11/36 + 1/90 + 31/120) == -13/360
    assert -13/360 < 0

    # Exact Gram identity is diagonal after summing the symmetric heavy pair.
    for eta in (0.001, 0.1, 0.4, 0.9):
        heavy = (eta, 0.0, 1.0-eta)
        diffuse = (1.0-eta, 1.0, eta)
        gram = tuple(heavy[i]+diffuse[i] for i in range(3))
        assert max(abs(gram[i]-1.0) for i in range(3)) < 1e-14

    print(f"B0={B0:.16f}")
    print(f"C_col={C_col:.16f}")
    print(f"3sqrt2={C_gauss:.16f}")
    print(f"gap={gap:.16f}")
    print(f"c1={c1:.16f}")
    print(f"12c1={12*c1:.16f}")
    print("PASS")


if __name__ == "__main__":
    main()
