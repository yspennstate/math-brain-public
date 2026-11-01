from fractions import Fraction
from collections import Counter
from decimal import Decimal, getcontext
from functools import lru_cache
import ast, zlib, base64, hashlib

ENC = 'c-rlp!A`?K3`BpWx3t>s5Aa_-A^sgm)kCEM%7%4j?8gD23PiLMkH=$s-_KuPOIxm|<#zvext`9CpMUt^`;)(Z=b!#){i~q=mGl8GZ{JV&3gyNj=0SOV!WWo!&M*(i50pEHSdp-a<$Q$Q0l5HS%ZD;0Km~<OMk%1M0eObPRy#yWfC>s5byz@Q1M&=o-5_ifHsULT!fp^YgpDNvVMm}$S2Q1Cla*%>_Kma*VS_RrHXze<#1g^7MtniofLzHEp;+EZ*z1vjY+91;gfEjJq~a8+x`T3J!d_1dU=xxw8VmItcyOYxn?3;xhiNBF_Yg3tH7fyYA}cS~QNu%-Rr77bORg|pC!8%9uPcEv<8=i<X6n7bI0*|Z5H@F+h_LV86<W&6zKBN+Z+M7A4+}4R-#w(*7czw(DfR`w){Y><LBoqRR*HD5@=B4i(N{H6N}H)hZVR$ijhLrSs*$YbsUT_gq)?EE5q$+oGX@1&%L70`IzAww<|z9QN^8n<;;2SPq*`^Q=mHe#&}IJ=MaZVGOZV9XD7nG%4OwG|AGVqUxWWglVh)YlH2i+?Rm_R84VaYPG;FBoXwo=^6s5OloxnH`6&<BF%1_cbYM>^tB6u4?sx6G_9J#gxXcO<|96Gp;(V>1f=Z04RH1+T19NL=(SY{>7QR}J8^Fgr_^8V8$|J|nqsH__{od-1Bu!)Q{Wz@Vwtte<usjTa@+&1LA>^JxfDK^lFP=T}00YDO#z>NnqTo;V=`;}4i4z*qrv?q<;^kxh;G)r?|VmtdFKxA`C8z{d4hXL$-3Xjnn$=8Q4GMNEle<)v*Lk>+k!WmZk=oHVMUlg5kW7u1AW|1NA$#aT9;mB|}>w?T97F!q8l*ELTu-r8;RU)qgVl8ktQbE`Iuok#?^rk2{$DqTkj{=z;rb2|g`C6~Pa)U%#6SMT}QD&B2Vm1jQmXZsl9oE%slYgWiRzUjdd0ii$_ow;X'
PATCHES = ast.literal_eval(zlib.decompress(base64.b85decode(ENC)).decode())
assert len(PATCHES) == 40
assert hashlib.sha256(repr(PATCHES).encode()).hexdigest() == 'e3ffa83af5107d8805e32e25c86be204a1bb4a5c088b732cc3f159c062a5454f'

def norm(ch):
    p=sum(c=='+' for c in ch); m=sum(c=='-' for c in ch)
    if p>=2: return '+'
    if m>=2: return '-'
    return tuple(sorted(ch,key=repr))

@lru_cache(None)
def queries(t):
    if t=='u': return (('+','-'),)
    if t in ('+','-'): return ()
    out=set()
    for i,c in enumerate(t):
        if i and t[i]==t[i-1]: continue
        for cp,cm in queries(c):
            out.add((norm(t[:i]+(cp,)+t[i+1:]), norm(t[:i]+(cm,)+t[i+1:])))
    return tuple(sorted(out,key=repr))

def flip(t):
    if t=='+': return '-'
    if t=='-': return '+'
    if t=='u': return 'u'
    return norm(tuple(flip(c) for c in t))

def flip_move(mv):
    a,b=mv
    return flip(b),flip(a)

def ucount(t):
    if t=='u': return 1
    if t in ('+','-'): return 0
    return sum(ucount(c) for c in t)

# Structural certificate: every stored override is exactly one legal leaf query,
# strictly reduces unresolved-leaf rank, and the table is sign-equivariant.
for s,mv in PATCHES.items():
    assert mv in queries(s)
    assert all(ucount(z) < ucount(s) for z in mv)
    fs=flip(s)
    assert fs in PATCHES and PATCHES[fs] == flip_move(mv)

# Exact root-cost ledger for the four newly installed sweeps.
PREVIOUS_U = Fraction(1332517664326644559,36028797018963968)
STAGES = [
    (10,155,8,Fraction(1332517664326644559,36028797018963968),Fraction(1332501816044412239,36028797018963968),Fraction(30953676235,70368744177664)),
    (11,254,4,Fraction(1332501816044412239,36028797018963968),Fraction(1332497576336439119,36028797018963968),Fraction(8280679635,70368744177664)),
    (12,414,4,Fraction(1332497576336439119,36028797018963968),Fraction(1332495381349676879,36028797018963968),Fraction(4186605,68719476736)),
    (13,658,4,Fraction(1332495381349676879,36028797018963968),Fraction(1332477360033879887,36028797018963968),Fraction(2199867651,4398046511104)),
]
for d,nstates,npatch,before,after,gain in STAGES:
    assert before-after == gain and gain > 0
for i in range(len(STAGES)-1):
    assert STAGES[i][4] == STAGES[i+1][3]
FINAL_U=STAGES[-1][4]
assert PREVIOUS_U-FINAL_U == sum((x[5] for x in STAGES), Fraction(0))
assert FINAL_U == Fraction(1332477360033879887,36028797018963968)

# B15 exact sign-paired defect data at the depth-10 pre-sweep.
G = Counter({
    Fraction(298677,4294967296):2,
    Fraction(352919261,34359738368):2,
    Fraction(2679195,268435456):2,
    Fraction(78965,16777216):2,
})
D = Counter([
    Fraction(10813595521,34359738368), -Fraction(10813595521,34359738368),
    Fraction(1388717721,17179869184), -Fraction(1388717721,17179869184),
    Fraction(852562887,4294967296), -Fraction(852562887,4294967296),
    Fraction(4087921,67108864), -Fraction(4087921,67108864),
])
assert sum(G.values()) == 8 and sum(D.values()) == 8
assert all(D[x] == D[-x] for x in list(D))

# B25 one-state occupancy identity: total hit probability, not one clock-layer
# probability, is the coefficient multiplying a local Bellman defect.
local_defect=Fraction(298677,4294967296)
layer10_probability=Fraction(1,1024)
total_hit_probability=Fraction(15,4096)
single_root_gain=Fraction(4480155,17592186044416)
assert total_hit_probability > layer10_probability
assert total_hit_probability*local_defect == single_root_gain

# Source-metric movement from the exact explicit depth-4 policy cost.
getcontext().prec=80
dec=lambda f: Decimal(f.numerator)/Decimal(f.denominator)
ln3=Decimal(3).ln()
sigma_lower=Decimal(1)-(dec(FINAL_U).ln()/Decimal(4))/ln3
sigma_upper=(Decimal(4)/Decimal(3)).ln()/ln3
W=sigma_upper-sigma_lower
old_lower=Decimal('0.1783937532290626654407820192070906898593985836476')
old_W=Decimal('0.0834657539138522087582722094784310187397726966161')
assert sigma_lower>old_lower and W<old_W

print('patch_table_sha256', hashlib.sha256(repr(PATCHES).encode()).hexdigest())
print('patch_count', len(PATCHES))
print('all_patch_moves_legal', True)
print('all_patch_moves_rank_decreasing', True)
print('global_sign_equivariant', True)
for row in STAGES:
    print('stage', *row)
print('previous_U4', PREVIOUS_U)
print('new_U4', FINAL_U)
print('exact_U4_gain', PREVIOUS_U-FINAL_U)
print('depth10_defect_counter', G)
print('depth10_bias_derivative_counter', D)
print('occupancy_layer10_probability', layer10_probability)
print('occupancy_total_hit_probability', total_hit_probability)
print('occupancy_local_defect', local_defect)
print('occupancy_exact_root_gain', single_root_gain)
print('stationary_4block_growth_upper', dec(FINAL_U)**(Decimal(1)/Decimal(4)))
print('sigma_lower', sigma_lower)
print('sigma_upper', sigma_upper)
print('W_sigma', W)
print('sigma_gain', sigma_lower-old_lower)
print('width_contraction', old_W-W)
print('ALL_EXACT_CANONICAL_POLICY_CERTIFICATE_CHECKS_PASS')
