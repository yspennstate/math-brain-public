import base64, zlib, json
from sympy import Rational, sqrt, simplify, Q, ask

DATA = """c-n2+TbAo83`Nln<s$|pL0ita{qM%LQ^DTS%I_RJHW*__)xUr3c=>o8_Ikg3z25)5K4Pz9oMH#0K^zj0S;gN~!fx@`(N7rxnUGb*-jD|A5Qm_5L+^&({eYl%NAHfYJMu&sSNB&dg?f-CXmrvb87cJ`ucKWLz#uFWkO^5;<UwvZAPv$X1A@$k%!bT{%!bU4%#O^C%#O^CgpP!cgpP!cgn@*Cgi#WnPra8(Y(bi!erie3J86*E{JCsFgJh&1ZB6tznEqUVQfj`A<65U3Vi1P}WJ1uFya8Jd2=d5!--0}bJcc}mJdQlFmbajH$NV^YkJ9qB;>u936<2A2IxBWoyw*~sK{C>hwo-`oI^Nf_q%=r}42VG-5|9a5Rb*{#L1sf{LuNx}LuNx}LuNx}M?yzJM;=G-j+Udeb8S<lp=+C}G(dwD$B$AIbZsq_j+@%`UL7u@d1SvS?Hc>vvF(xZJ#KYKKxUOayCMyOmL=g9hpZ|wAWuTe$2O4;VXX;SRb<92AKOIGmyGl)QEFZL(a6-_B)>l^LMRn16)ZJD@&&vpRrGw|dc@w41JWQJg1*ck4hhJFAhRR0BeNs3BeNs3BeNs3BeNr6pszq*QCe=#&VSRoKOvj?n>4OflF3*qK!a_a->_b(kvb`qBA<XnCS+BSB^mhyB!a$VNk%>si5SEo$ZW`L$n41M$n41MNa#rDNa#rDNEpZyXgN@8mdw}bz6>>QcQ=(%=ivxsBqs%l%?~!8x4W57QX&os$b_savPNe<Nr^N_haj^dvmvt~vmvt~vm>)3p(BqYkE8b}Ez22wQ$I+9WTYUm`Ex64Wts-tk{>gKP%2o8A;x4W<}wcZTo$0Nv|dYY3J;75R>3Pog;`-0kcIt)8cde;7iv<gNv$Ten$&7it4X~E^BT-+FOf@}tFq-*ds;OgIetm0)lkNMNvY*16ThU?nkaLQqCs+*>utzo2F5iou7PpMuZCOfmy~uKy}Mp>wm77;6R3q5yWYYEDP<Pg!HgO5oD1-nRZ1Cu)=$6I<KOiys_b>xKNmWaZC1n}4p~+9#w*fq>G_H$(jcrgAO;D@gsduoJb^rc-lMd0F8Wal$#M3kLuq{Ph6Zs+Kqh2W@i*jvAdgJ`mH|O#M?y!QK%PLJD0y07%Fg!^v_Sn$dTu5+t^1xJBo!^+FhvH$APx!0tRj!i@_kYS2^|R?2^|R?2^|TY30IXs=0N5^=0N5^=0N5sy|>TRF_HXCant%mwc>cAl>92c$x<oLw?dHy=@7Q#kbq3csv^tC^BqtG2^|R?31u01z7>ifvm>)3b0Bjdb0BjdVU&c|E>Z$ryGW%4>IW(94>vufBHz*;u{Y#^G)RXGh(nM^)=cC(*&~jGj)abcjy$qLwjiM+VW3u&%>8}ev~M~{L0X`}it_ipn+9oW#hI=)56lX+iah(7ZZZ$_3ZsHo$i2vI^(%w2s#w3zzFSPotk;zL-UD7CD$EM2fV?7KsNKpeeW6zv6>2c6!K?=Jn!{@jufzA;hFrq7JQs*9tBPEeL`s<hWe${Sza-}w9c2c}ILcrY^0%ce3kfk&!?<if4C1xr^I86oQfu9pr$@?2^X2Iy2jrQ<@o6;VhjWp+<!tot%4N44`N|~{kXdDaA4Sm4ljpjGjoequS0#}NSyiO>mM>2t9fICvHnu#Od%l;5bjW}hBp?&As>n!tzNv^HVIW~3Pn5pS^)yPM>#$O3-8<u^b3Yau`7$B0syJ%-0qKwdaY#Ur$B`$HC(wJKcbVCd|9~ZeJW=wDcAw?O=WMTkmJxACRFP@5eB2g6Uoz2_kJ}>1<H#e^YWXNFf;@pdGSQxopCT;dkbq3csv>jf`S>Z)AV}y)D0Arf_$h*ff!?F^E<f_zl-5+Fv)%)vf>($NtAN*DJU2R?!}7QWH*=8rcSz}3><u{}U1hyOKjvH7{aN1f95?LqsdRZoADM4RgWT<0A6WfVimWQ}hBOFT-fx76SJ{846hX_9`N;pIBC@IkY6WUNb9l?F^33Wj2jm%P%O6jX30YO*fHVmD+8ervL(rFuYYY04neX}6GZB^<5Q9V&Sz|r_>Lr4{0(}MglG*6_^Cq&YOyrU0KJr&dq(cHSs{~pOv>a$z#=hklspYT0BQnpH_iB-+FHig91K%<DwcGw3-Q$+|-D~WYm3Ix14q>ecSylG4@z1U?WHpQ2eO>QuPrctVAP$*T_F55n^0d6-MP`*it!Kt=@hUQ|p4W<qLA;8LV&oHpNQZcpJ&O3O1bu=ctIFO(MSRQk1a($L?poI<-g{jC{SW66rp5"""
TUPLES_K1 = [tuple(x) for x in json.loads(zlib.decompress(base64.b85decode(DATA)).decode())]
TUPLES_K2 = [(21, 69, 10, 54, 53, 12), (22, 69, 9, 44, 49, 30), (23, 68, 9, 40, 50, 30), (23, 66, 11, 38, 59, 30), (21, 67, 12, 50, 53, 20), (23, 66, 11, 35, 58, 30), (21, 68, 11, 49, 44, 30), (21, 69, 10, 53, 54, 12), (21, 68, 11, 49, 47, 30), (22, 69, 9, 47, 49, 30), (21, 69, 10, 51, 56, 12), (23, 68, 9, 41, 53, 30)]

def margin_k1(tup):
    CSL, CSH, sV, ZL, ZH, ZV = tup
    EL = -Rational(4,33) + Rational(13,33)*sqrt(26)
    EH = -Rational(13,33)*sqrt(26) + Rational(32,11)*sqrt(3)
    E  = -Rational(2,33) + Rational(16,11)*sqrt(3)
    Et = Rational(4,1815) + Rational(496,605)*sqrt(3)
    return simplify((CSL + Rational(ZL,11))*EL
                    + (CSH + Rational(ZH,11))*EH
                    + (sV + Rational(ZV,11))*E
                    - 200*Et)

def margin_k2(tup):
    CSL, CSH, sV, ZL, ZH, ZV = tup
    EL = -Rational(8,33)*sqrt(2) + Rational(5,11)*sqrt(30)
    EH = -Rational(5,11)*sqrt(30) + Rational(52,33)*sqrt(13)
    E  = -Rational(4,33)*sqrt(2) + Rational(26,33)*sqrt(13)
    Et = Rational(16,1815)*sqrt(2) + Rational(754,1815)*sqrt(13)
    return simplify((CSL + Rational(ZL,11))*EL
                    + (CSH + Rational(ZH,11))*EH
                    + (sV + Rational(ZV,11))*E
                    - 200*Et)

vals1=[margin_k1(t) for t in TUPLES_K1]
vals2=[margin_k2(t) for t in TUPLES_K2]
assert len(vals1)==723 and len(vals2)==12
assert all(ask(Q.positive(v)) is True for v in vals1)
assert all(ask(Q.positive(v)) is True for v in vals2)
m1=min(vals1,key=lambda x:float(x.evalf(50)))
m2=min(vals2,key=lambda x:float(x.evalf(50)))
e1=-Rational(598,33)*sqrt(26)-Rational(486,121)+Rational(6736,121)*sqrt(3)
e2=-Rational(2525,121)*sqrt(30)-Rational(3500,363)*sqrt(2)+Rational(14690,363)*sqrt(13)
assert simplify(m1-e1)==0 and simplify(m2-e2)==0
L3=Rational(173205,100000); U26=Rational(509902,100000)
assert L3**2<3 and U26**2>26
lb1=Rational(6736,121)*L3-Rational(598,33)*U26-Rational(486,121)
assert lb1==Rational(47821,9075000) and lb1>0
L13=Rational(360555,100000); U30=Rational(547723,100000); U2=Rational(141422,100000)
assert L13**2<13 and U30**2>30 and U2**2>2
lb2=-Rational(2525,121)*U30-Rational(3500,363)*U2+Rational(14690,363)*L13
assert lb2==Rational(26102969,1452000) and lb2>0
print("K1",len(vals1),"min",m1,"lb",lb1)
print("K2",len(vals2),"min",m2,"lb",lb2)
print("EXACT DOMINO RADICAL CHECKS PASSED")
