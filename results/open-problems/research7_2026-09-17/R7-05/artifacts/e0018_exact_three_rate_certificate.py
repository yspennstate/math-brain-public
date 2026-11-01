"""Exact certificate for R7-05 / E0018 (Malrieu Open question 3).

This script uses only rational arithmetic in SymPy.  It verifies three
pointwise corrector inequalities for the symmetric two-state switched
planar system.  Sturm root counts are exact.

For B_i traceless, u=(cos(theta),sin(theta)), set
  a_i(theta)=<B_i u,u>,
  b_i(theta)=<B_i u_perp,u>,
and for a pi-periodic corrector phi(theta,i),
  (L_r phi)_i=b_i phi_i' + r(phi_{1-i}-phi_i).

The target level is h=1/3.  At r=1/20 and r=10 we certify
  a_i + L_r phi > h  for i=0,1 and all theta.
At r=1 we certify
  a_i + L_r phi < h  for i=0,1 and all theta.

After the scalar shift A_i=B_i-h I, these become strict positive,
negative, positive Lyapunov-sign certificates at the three rates.
"""
import sympy as sp

T = sp.symbols("T", real=True)
QQ = sp.Rational

B0 = sp.Matrix([[QQ(1,4), -QQ(1,2)], [QQ(1,2), -QQ(1,4)]])
B1 = sp.Matrix([[QQ(2,3), QQ(1,3)], [QQ(7,12), -QQ(2,3)]])
H = QQ(1,3)


def R(s):
    return sp.Rational(s)


# Each coefficient list is [cos(2 theta), sin(2 theta), cos(4 theta), ...].
CASES = {
    "left_lower": {
        "r": QQ(1,20), "K": 12, "sense": "lower", "c1": R("5720777/1000000"),
        "mode0": [
            R("40563/200000"), R("-495201/1000000"), R("-11407/250000"), R("8361/100000"),
            R("55753/1000000"), R("-10097/1000000"), R("-38463/1000000"), R("-631/100000"),
            R("20129/1000000"), R("1611/125000"), R("-8031/1000000"), R("-12769/1000000"),
            R("321/250000"), R("2301/250000"), R("747/500000"), R("-649/125000"),
            R("-1849/1000000"), R("2217/1000000"), R("1203/1000000"), R("-309/500000"),
            R("-491/1000000"), R("57/1000000"), R("19/200000"), R("3/500000")],
        "mode1": [
            R("2781651/500000"), R("544929/200000"), R("-3211997/1000000"), R("-4066079/1000000"),
            R("19493/20000"), R("4297491/1000000"), R("799477/1000000"), R("-889233/250000"),
            R("-1796987/1000000"), R("456517/200000"), R("991253/500000"), R("-15257/15625"),
            R("-198503/125000"), R("13549/1000000"), R("480201/500000"), R("91253/200000"),
            R("-401313/1000000"), R("-50731/100000"), R("68543/1000000"), R("336657/1000000"),
            R("8253/200000"), R("-6969/50000"), R("-28521/1000000"), R("25473/1000000")],
    },
    "middle_upper": {
        "r": QQ(1,1), "K": 4, "sense": "upper", "c1": R("219591/1000000"),
        "mode0": [R("687/1600"), R("-107949/250000"), R("-10653/500000"), R("65031/500000"),
                  R("-3769/500000"), R("-1201/50000"), R("1739/1000000"), R("443/500000")],
        "mode1": [R("310769/500000"), R("-65681/1000000"), R("-84551/500000"), R("-31/10000"),
                  R("26009/500000"), R("17521/1000000"), R("-843/125000"), R("-12221/1000000")],
    },
    "right_lower": {
        "r": QQ(10,1), "K": 4, "sense": "lower", "c1": R("-1709/100000"),
        "mode0": [R("44347/10000"), R("61767/100000"), R("-216959/100000"), R("8439/50000"),
                  R("28039/25000"), R("-4373/20000"), R("-33909/100000"), R("-97/4000")],
        "mode1": [R("444383/100000"), R("5143/5000"), R("-21869/10000"), R("-13293/50000"),
                  R("27769/25000"), R("1797/12500"), R("-2689/10000"), R("-6919/50000")],
    },
}


def cs_table(K):
    """cos(2k theta), sin(2k theta) as rational functions of T=tan(theta)."""
    c2 = (1-T**2)/(1+T**2)
    s2 = 2*T/(1+T**2)
    C = [sp.Integer(1)]
    S = [sp.Integer(0)]
    for _ in range(K):
        Cp, Sp = C[-1], S[-1]
        C.append(sp.factor(Cp*c2-Sp*s2))
        S.append(sp.factor(Sp*c2+Cp*s2))
    return C, S


def radial_angular(B):
    u = sp.Matrix([1,T])
    up = sp.Matrix([-T,1])
    den = 1+T**2
    a = sp.factor((u.T*B*u)[0]/den)
    b = sp.factor((up.T*B*u)[0]/den)
    return a, b


def build_phi(coeffs, const, C, S):
    K = len(coeffs)//2
    phi = const
    dphi = sp.Integer(0)
    for k in range(1,K+1):
        ck, sk = coeffs[2*(k-1)], coeffs[2*(k-1)+1]
        phi += ck*C[k] + sk*S[k]
        dphi += (-2*k*ck)*S[k] + (2*k*sk)*C[k]
    return sp.factor(phi), sp.factor(dphi)


def sturm_variations_at_infinity(poly, positive=True):
    seq = sp.sturm(poly.as_expr(), T)
    signs = []
    for q in seq:
        p = sp.Poly(q,T,domain=sp.QQ)
        s = sp.sign(p.LC())
        if (not positive) and (p.degree() % 2):
            s = -s
        signs.append(int(s))
    return sum(1 for a,b in zip(signs,signs[1:]) if a*b < 0), signs


def verify_case(name, data):
    r, K = data["r"], data["K"]
    C,S = cs_table(K)
    phi0,dphi0 = build_phi(data["mode0"], sp.Integer(0), C,S)
    phi1,dphi1 = build_phi(data["mode1"], data["c1"], C,S)
    phis=[phi0,phi1]; dphis=[dphi0,dphi1]
    print(f"CASE {name}: r={r}, K={K}, sense={data['sense']}")
    for i,B in enumerate((B0,B1)):
        a,b = radial_angular(B)
        f = sp.factor(a+b*dphis[i]+r*(phis[1-i]-phis[i]))
        residual = f-H if data["sense"]=="lower" else H-f
        P = sp.Poly(sp.expand(sp.cancel(residual*(1+T**2)**(K+1))), T, domain=sp.QQ)
        assert P.degree() == 2*K+2
        nreal = P.count_roots(-sp.oo,sp.oo)
        vm,sm = sturm_variations_at_infinity(P, positive=False)
        vp,spn = sturm_variations_at_infinity(P, positive=True)
        assert nreal == 0
        assert vm == vp
        assert P.eval(0) > 0
        assert P.LC() > 0
        print(f"  mode={i}: degree={P.degree()}, real_roots={nreal}, "
              f"V(-inf)={vm}, V(+inf)={vp}, P(0)={P.eval(0)}, LC={P.LC()}")
    print("  VERIFIED: strict pointwise inequality for both modes on RP^1")


if __name__ == "__main__":
    print("B0 =", B0)
    print("B1 =", B1)
    print("h =", H)
    for name,data in CASES.items():
        verify_case(name,data)
    A0 = B0-H*sp.eye(2)
    A1 = B1-H*sp.eye(2)
    print("A0 =", A0)
    print("A1 =", A1)
    print("CONCLUSION: for the shifted pair A_i=B_i-(1/3)I, the top radial exponent is")
    print("  positive at r=1/20, negative at r=1, positive at r=10.")
    print("All three assertions are exact rational/Sturm certificates.")
