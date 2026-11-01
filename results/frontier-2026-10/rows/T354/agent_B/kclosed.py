# Closed form of K_rr(n, beta1, beta2) (agent B, 20 Oct 2026); checked against kfactor.K_rr's lag sum.
# K = n/(n-1) (1-b1)/(1-g) - [n - b1(1-b1^n)/(1-b1) - b(1-b^n)/(1-b) + g(1-g^n)/(1-g) + g(1-b1^n)(1-b^n)/(1-g)] / (n(n-1)(1-b)),
# g = b1 b. Limits: n(1-b) -> 0 gives 1/2 at b1 = 0; n -> infinity gives the iid value (1-b1)/(1-g).
import sys
def K_closed(n, b1, b):
    g = b1 * b
    geo = lambda z: z * (1 - z ** n) / (1 - z) if z != 1 else n
    return n / (n - 1) * (1 - b1) / (1 - g) - (n - geo(b1) - geo(b) + geo(g) + g * (1 - b1 ** n) * (1 - b ** n) / (1 - g)) / (n * (n - 1) * (1 - b))
if __name__ == "__main__":
    from kfactor import K_rr
    worst = 0
    for n in (2, 5, 10, 37, 200):
        for b1 in (0.0, 0.5, 0.9):
            for b in (0.9, 0.99, 0.999):
                a, c = K_closed(n, b1, b), K_rr(n, b1, b); worst = max(worst, abs(a - c))
                print("n %4d b1 %.1f b2 %.3f n(1-b2) %7.3f  closed %.12f  lag-sum %.12f" % (n, b1, b, n * (1 - b), a, c))
    print("max |closed - lag sum| = %.2e" % worst)
