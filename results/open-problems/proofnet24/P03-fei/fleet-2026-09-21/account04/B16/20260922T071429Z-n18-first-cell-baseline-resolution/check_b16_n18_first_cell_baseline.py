from fractions import Fraction as F
from decimal import Decimal, getcontext
import struct

# Account02/B16 certified two-secant data at u=1/5000.
# Every decimal interval below is copied verbatim from:
# proofnet24/P03-fei/fleet-2026-09-21/account02/B16/
# 20260922T063230Z-n18-exact-entropy-two-secant/check_exact_entropy_two_secant.out

def Q(s):
    return F(Decimal(s))

getcontext().prec = 120

B0_LO = Q("-0.00000146374656181129378785166846174297621881084133244996672358961997606147257726300623333433664")
B0_HI = Q("-0.00000146374656181129378785166846174023017714119930315849834774671939133167467700589197120313843")
A1_LO = Q("0.000289723835145426338606632815966685937369858305346898847039560420149018212457426197236608164")
A1_HI = Q("0.000289723835145426338606632815966685937369858305346898847039561861879534775476782046382059681")
A12_LO = Q("-0.000289607847377238818763664287039044749002907587456111881957141059056944575296078189189882460")
A12_HI = Q("-0.000289607847377238818763664287039044749002907587456111881957139617903609053871202824890717997")
MCRIT_LO = Q("12.6198355627019584068997717383090992721636270995425740720921806975693952899918042659844093")
MCRIT_HI = Q("12.6198355627019584068997717383327745416558587844737599771495574985079248063986445053323764")
D30_LO_PEER = Q("0.00000201588648381430150120419936749267478971069539115898574899121278614764226317723516843678153")
W = Q("0.259765502969375869532068437164660027266399033856017326079882035200262144")
A_STAR = Q("0.268204856")
C_CENTER_LO = Q("0.2681828436921863026325758917943138734666491688421")
C_CENTER_HI = Q("0.2681828436921863026325758917943138734666491726918")

# Exact source geometry.
u = F(1, 5000)
r1 = F(1, 2) - u
pout = Q("0.500400781197500003959999884800000512")
r2 = F(1, 1) - pout
first_node = F(1023, 2048)
assert first_node < r2 < F(1,2)
assert first_node < r1 < F(1,2)

# Exact binary64 values decoded from committed baseline NPZ blob
# sha 1e2a1a5c293fa7b6ec9885b7a410910d6589be80.
G0_hex = "0x1.9d1b71758e219p+3"
G1_hex = "0x1.9e76c3a5f50bcp+3"
G0f = float.fromhex(G0_hex)
G1f = float.fromhex(G1_hex)
assert struct.pack("<d", G0f).hex() == "19e25817b7d12940"
assert struct.pack("<d", G1f).hex() == "bc505f3a6ce72940"
G0 = F.from_float(G0f)
G1 = F.from_float(G1f)
assert G1 > G0

# Rigorous atanh-series bounds:
# log(x)=2*(z+z^3/3+...), z=(x-1)/(x+1).
def ln_bounds_ratio(num, den, terms=120):
    num, den = F(num), F(den)
    z = (num-den)/(num+den)
    assert 0 < z < 1
    s = F(0)
    for k in range(terms):
        s += z**(2*k+1) / (2*k+1)
    lo = 2*s
    rem = 2 * z**(2*terms+1) / ((2*terms+1) * (1-z*z))
    return lo, lo+rem

# ln 2 = log(2/1), and x_node-1 = log2(1024/1023).
ln2_lo, ln2_hi = ln_bounds_ratio(2,1,terms=180)
lnr_lo, lnr_hi = ln_bounds_ratio(1024,1023,terms=20)
dx_lo = lnr_lo / ln2_hi
dx_hi = lnr_hi / ln2_lo
dG = G1-G0
m_lo = dG / dx_hi
m_hi = dG / dx_lo
assert m_lo > 30
assert m_lo > MCRIT_HI

S_LO = A1_LO + A12_LO
S_HI = A1_HI + A12_HI
assert S_LO > 0
D30_lo = B0_LO + 30*S_LO
assert D30_lo >= D30_LO_PEER

Dbase_lo = B0_LO + m_lo*S_LO
Dbase_hi = B0_HI + m_hi*S_HI
assert Dbase_lo > 0

# Gate margin c_F = a_* - D_*/W.
c_lo = A_STAR - Dbase_hi/W
c_hi = A_STAR - Dbase_lo/W
assert c_hi < A_STAR
assert c_lo > C_CENTER_HI

def dec(fr, digits=30):
    getcontext().prec = digits+15
    return Decimal(fr.numerator)/Decimal(fr.denominator)

print("PASS")
print("first_node =", dec(first_node, 25))
print("r2 =", dec(r2, 40))
print("r1 =", dec(r1, 25))
print("G0_hex =", G0_hex)
print("G1_hex =", G1_hex)
print("m_base_lo =", dec(m_lo, 45))
print("m_base_hi =", dec(m_hi, 45))
print("mcrit_hi =", dec(MCRIT_HI, 45))
print("Dbase_lo =", dec(Dbase_lo, 45))
print("Dbase_hi =", dec(Dbase_hi, 45))
print("c_gate_lo =", dec(c_lo, 45))
print("c_gate_hi =", dec(c_hi, 45))
print("center_c_hi =", dec(C_CENTER_HI, 45))
print("stable_threshold =", dec(A_STAR, 20))
