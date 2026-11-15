from fractions import Fraction as F
m = [F(1), F(1), F(8,3), F(11), F(908,15), F(415), F(23840,7), F(325719,10),
     F(112135066,315), F(3065263961,700), F(69174280444,1155),
     F(5680684105259,6300), F(1112571762134554,75075)]
thr24 = F(533385290252268206796914811370716813306691285889, 36005162406403257088495500297206628000)
thr26 = F(494928082868210312280416728260442133271648915013635267802991, 1875040512409666424822745905712033018287315816250)
r = [float(m[k+1] / m[k]) for k in range(12)]   # r[k] = m_{2k+2}/m_{2k}
d = [r[k+1] - r[k] for k in range(11)]
def ext(top):  # predict m_{2top+2} from ratios through r[top-1], linear in differences
    dn = d[top-2] + (d[top-2] - d[top-3])
    rn = r[top-1] + dn
    return rn, float(m[top]) * rn
rn, p24 = ext(11)
print(f"order 24: predicted ratio {rn:.4f} m24 {p24:.6e} exact {float(m[12]):.6e} rel err {p24/float(m[12])-1:.2e}; pred over thr {p24/float(thr24)-1:.2e}; exact over thr {float(m[12]/thr24)-1:.2e}")
rn, p26 = ext(12)
print(f"order 26: predicted ratio {rn:.4f} m26 {p26:.6e} thr {float(thr26):.6e} pred over thr {p26/float(thr26)-1:.2e}")
rn0 = r[11] + d[10]
print(f"order 26 constant-difference: ratio {rn0:.4f} m26 {float(m[12])*rn0:.6e} over thr {float(m[12])*rn0/float(thr26)-1:.2e}")
print("needed ratio m26/m24 >=", f"{float(thr26/m[12]):.5f}", " needed difference >=", f"{float(thr26/m[12]) - r[11]:.5f}")
