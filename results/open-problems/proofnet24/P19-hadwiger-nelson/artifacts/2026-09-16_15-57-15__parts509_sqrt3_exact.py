#!/usr/bin/env python3
"""Exact self-check for P19 2026-09-16 Parts-509 sqrt(3)-orbit relation search.

Graph edge set: md-amer/hadwiger-nelson-e5 FINAL_reduced.json at commit
6d5ac08491f7cadbebd7d5b79e3f825d08eedf7b, Git blob
98c05513fa39510596e234740ae0a291df8ae2a2 (509 vertices, 2259 edges).
The edge payload below is that edge list encoded as zlib+base85.
The script uses an exact combinatorial 5-colouring backtracker; no floating point.
It checks the 18 public algebraic coordinate points v_309,...,v_326 have
exact squared distance 3 from v_0=(0,0), then for each terminal pair
(0,j) finds and verifies a proper 5-colouring with different terminal colours.
This DISPROVES forced equality for this explicit sqrt(3)-orbit candidate class;
it is not a 6-chromatic construction.
"""
import base64,zlib,time,sys,hashlib
import sympy as sp
N=509
PAYLOAD='c-l>yTe9pb4h1K)Kgzs`JO6pLG8ZSJf0Sh#V=M^)GWGlW#`*78@*?L?`6-*SD~EC_mvSq;cY5#g-sQc^dzbev?_J)zymxu;^4{gW+j}?n_Pdow$<^`uDL-XXcI8k`<x+0t`S1Jt`cLWa(UA2PCAac;=6JQ9^8K}{zx{pfr_Aq-?EdZ-IXbd5&}@InJ(0)r$MT1g?e|kQ<hTFpRa;YbrDwWl#!oqvo-ciNwb5;1$x9h(LyrGO-P@7lQ%>bYZqM(HJf69fX}_+V|4pBZ9LVACrQDv`2U$-<az1yp((S6259LHw8<74U{w|+cT70P)<V98+kd$d<Dda(Z=fC~;eG}OtJ<}Jmbh7ojt<RL)o<BciwGBxbYAgBul=r_=^(gyBmVS;Nd(=$H^C7D}NUpXY<=glDcWuK}KUe>``sY<MSI@aV7r9F2uJ-l+zH;Jk1zWTnRck=0O5|wdTJ^s#-3Of1a#QkJOZ!?-o?Gr(N)uP`gy-#_iUT7@)saE<L$I4Txpq_XTG^|*eV%O93BGu~*ka_UIx;9f11BeMiqMhp_bSr=O1sE`{C+c7qCISJQsm?$U9zXfZr1@cX#8=m<UxLAFz|T==Mk2$Mv#*yCCgt5xZF4YI5+>w$xD9K^F<R>HPgnKI%XO-^%&t1p7yOjRIvW2y<8kUF8eyD;0eli3yq5RA2sb1-0^{J+yzU}&&3ukN4QV{JD)#Vb^d5ZIWXRFjJ)5mD*$YF|H@-aUVmHe8neL?7B7_FwBKKKj)w1cF>+MVs3lMr=qD|%2%05Z-$6yh@2~nt$#UTKrK-=~0H&811q!V~Piv?TIgq%CIAZ7MSPu2I{zs(kD6!#ATa*ug@^9fu6xGIG1&orVu7=C}f-5T836IcMo9L?~aXkJ2KCcjZ!0||ZE%j9n@I&H7VhCzl85mX+wEuY2RzGFy3dmxKog=E+(aiZPgChOS_2ZL{x;oKmLL3+taPT?yo<eIuIa#}Z6$Ow3$y;32at$Ockq!(C5dVcITl)elYBm1#A2lH-vfc^ld4>ouyuzRe$_M*TF9sEh`}bFVfb@4+qhzTI=@|lWPb}*hszLR$PK5HPjU802&5BAMWVsG<AxmF9V>;+wA)56J)}Z=zq4i)`MXOHP`(OEN$+C3GQdoaucsJI9VF8Ee?zqsq9RqZ)wd!(xSku78N}{UaU;)a8plsMPV2cUp{-EcGsloiKi41ZgYiL4x9>q-u2+)IJVHKCq)$w0Xwi+NrJ$PAP$%SO{vDBab-It>l7?x6FOGoSYx7QkP2&(e^hmA`f<o0)YUC(e2x}{Xu*3tSlgn$Z!{djN5i`@Rk&yJHcfKE<KdE#gp&O5F@M6R{!O1*slr}TFP3*<%ObvF~V8?)Y+^~UWo&==aUhE|#yKPnn_gOXcWrAB7UBNJS(Eld;}KOGm0FQ{4BM;Av<<n?!{b$m`VL4{s$EKD2(!)x@U(dbDfOO>M;;6a&Cc!_WbhQ;Z@fVTI)CpVJmV<&izo*8APqa)#UB)pDpXc=*EFnUl=*3U~)-@rRd9?yTdz+`hI{*J`oF$@f#d$Ns(I$3_+k!aI#yCiy^4zGar&**s?$U${pQRNr?rR4HA)8WM=Vl3yD0QD`S?^womFu$NmZr^FsLrQLC&2`3hRyi^~9hskka`dqcCnG)$c&BY28ONG*@RHjzSIHCr><0^I`C|+K;}_&;<{CF#Ixq4ftA~#3^b+8#H`>0AM*zKCdj}|onLoO1Nv8il{9tBPIJ2As)!g}Wi~`dlbXdT(kJl<$wU*q<t7JY3%F{vl+RS`(evU1mA_=IMo6U+E{#lY(2`aLJo}-bYQYt7b%&fY==Y4o8D6N5&Yr6+2a%NzitvcWAD6u3>?fBd5`rGU-rNHN<hE@il1-X#rTXPtNL75$(r(su~!!;cEEUzkuy%AI#n^WygI#EehVH1a&iRu6aP2CTa^+AfbUYpVAv}b{lqu~vz0i@)9s3MDKggnUdp_$MRhUbVcbGgEuS<Zp#b|6JmN}>Aw+)O->7l}tD_Rmav=XT{iGv5WvYpr_vJlg&^WXuG7fGJPBDLrPM7(LTp(1PlLV9j8OieMr|@|=dlU(J09SMxfq%=DajWA*F&7hss{UF(P0mtAK497RC)94@ocb=FU_gU^zLWKcm4l)?ckW#>f8UV~gn<_Ig9jFnWzN>5s!1_z(ziOC`-OUEMD)(WoJLG{4p#HnOC|7uPySGw0q!UHVf0=~H@1>KT_HL!A29=kdwFL{;tEttY&LU+v!R!)*17)db<oo=Q7fSDsoj${vpJ$z-*5Ek*>h5->&C>BlR39SaoWw%=CNr2m?_646O35kI6>n{@T1LYQA3r)K0&?_Sd!1&9c2+H->#<!N;V5J*?ax`&8^*?Yu(xw?hKuQvH0k61?W#BwioriI99p}6&{RZF)C+V4E{{@)wII95L8yY_6x^dl@{n|@c(j1^(YX6u&m1IQ)y5|_!cSZ)VgNkbVV?tSyMGvT$u`>?r&!zs3zk-w`g6zfwZMWoxnuFqQuD*9>G+^hbn!GzR*4@od?aWwqPp+vu=7AK!QTJfpyoak#Q2i1dFOhlx)qemj8QOAB78X0}L{M>dXMwmAZb6Em&%L6j<wyojj;hD)giNp>rl_H0Z`YLI%TWcIof-4q#<oJI$Z@f{GZzNeBZ7UQ^LjVRze&1fehbjUHTDXNXaj=W{qOu---6NyAb0lj>0*m*$zGmyK3DOe0wTCMS)J%40D*0hUQIg9CGkn@0o8ah0ZjtOlfA;n$--Y;QSWdPOu+UUb}n=p9}AyE7{EIW4R8`Sz_uiYF7&ePnPv_Ejh|}%Oifkjyyh|&0jkG=lOr0x(w0>v>j_(b0X2~UWdKkfa<--dJ1Flt*tSX@b18s!W@Q6v&Qj>ri_bMspQJ0#wNC?@do@3(T5j_9H!1g<p$L?v?@wO>l>AH^fr?I`;`hxM1CA$q#o^n`X@LrRpkC!RryroqU+Cq+w>x}+C73(hu2Df*^Jc;XmLQ_up`!qbOcio72Lk0GcN!_d^;$1)y({mKm<_fk86W|f+%iu2#NEzuZi4XL4sLhr1>%ZQ>pfA(acIBCIov&(N*qDS8@*h^?@bZ~l-Cuy3E~7z$TXvRTJoB|m)`w-FE9Kuw7*Xql_Mpw3ftpel0h1FulM9@f88iv;Y4?pWC(x5aj)u12KATK6l^|cs`-i>NxQ=Kj>#tf)=N<@jaYRXbfHPi-^uru-$`!xcVBz6Ac4*Iy=v|=W4=R^);~uphz&lo*q=1({^3|(=zVz6eB`)XrhSi;PgVpH@u2#I?S!4<OnoJZT9ddfG^f6zUr1`76z-#GX1JE@q;J3TGV_^|e&2lw`)kyK>KU5PhjnZ+wo4){RL{^HJ>>XHdr7WtQur<J*)m$n753`DU(460a7z+ba_74CfP6<IUCR5lgh{A9VDFC{&!phnOPrH1Jv+Sbm@Iyqc9_pZ>3E!yfnSolmRB;id}d1L<B|;IVa^lqL(U(=iBvDgX#>>GEz4v%w`BZ=+O;RABe8qWtX=YnrT=25o|KKmzCF{Kuu1LI6CEXbG}$<%dhW@+Nc^*B+5**YPxeI8uS^r3(0WGR3u52?`ZFYskn-bePM`5#5_#BLE=howwqvD#^dzdoEn9o^J@?aB(fZG8XEGVE^&G4JexBa$Yu}3pq}bXccIh|%ZZ>U&#GR3E4w6qT<Cp$JvW)hP7bnP*;h*NqhSUxtlSzplN74imyN+iM$QNYOUpGXLCctJmbKU-6TC0V&a~SoZ{mE=q4{hIc@gniNF=J;)zc&rFL%(SyLn_g)DWXTek)6b+k(oTSe?t6|M3C)$pMjts$*!3^xkDxv(l2ZGwFkaq+BLJ#mBbelLL<Dn-ihxslL|TBG4`GB+q_AkUwCt#FAtLb1pN?~g#k3~&rCsNd*{bH=4+Q3q8$=XULHuE{dlGCD`(i=dFv}qj<b%1jt4IdB>kk=-+RIp(jO%EXFV%@j}g6_1X?ohGcta`cVEZu^TpShwEj2WI0k*cnek)3csjG#_{_}g(C4oAe(%#G^b2RQl~TR$r;qIfPWnE@`FniFe1)9vYov*oNBr!iTVV8ZoXSb>zln=8-=Co4kqMU@{yTqDF8aAn^kjb=Go-$i{U`E<+Re1f3elVF()WZd=N)I^$o(CAuYAjdd~c9`>;0TnLf;SiJp2*1_f5FPeq>D0H^l!}%lpV4j+Fa%f1mF>b|<fbogw}GrBvk2dB=MaDD<C|wa>TSIBrTL*Yln;aRJhQNrCv@Gj>?>>18@?mh(|Pufzee9=1P85P5SPeJrQQa=c^f*@*)ypNGDe<dFZ4eb4>$vonu|z9;_qj<ru##NRs4PUq?QJpG)+sde7_oW#5J;wBuar)#(S^mY@E)=hkazR!!3knxzL2<;^gGIDJE*}udu*mB*t2;Y6iYluBambiW3?OZZX(n8*EzxW4<&-=|Qc2eBXaU6QRC;skyYJtWXG8Xi!o$n};adN-;0+|W?8d}dXsR|u`q4({K-}}XfozE3eKPI_AKil~fAy3Xb-b2chTA)9iH{XIMbUZz8enl#QddLv)-mL$zo9Tcd9iJh3J#ViCB)+lM#@?*5nQyYbMqlU6SKvFZo>^QoAC)uod2inG7T?e~%MzRC$t{gntfZL-%Og|1rCx}C!IAUMZ=v`1toI=Pbl-f$MRl&*ukU#EkF1+mO4DC%@}81$hlR7{*Q+m?O^H3^l+NFw^(1WxT@OO+@s`jM{jy%R{pUUJ>C@Hm4(SJwc_C!HW4%054*NFNxok=JCCwn&)gjrEGMyL8-b1!=$Sd*pvW4+hmVY(Ysr5eL4B5{C**U>F^*f<kT0ZBs;SJfUA-lvc8{3cEBQu<TOLxl*`)6alc-Z>#GcGmOaqKm0$&@wLZ|uft@BLWEQBTVj1L<a&Zai(Q)7V7Pk_T_ByVwQt)?rXRvcB>;$v;BkO=}tdB|C0f=J(QeB)2F}j#+m|+jE__O7{G)o}xWH^Fw)atloRZPl+B_FJT|oM<=8`tdkade!An4yg6oGFRiaTPPd+UmApA--663b<UM*m7|Z>W-RCXGQ+ac&Jz4kcFT72rzT^Bnyt4bgnODo3W9Ipi_huc#b4TXQkoAY8{j6WmpKOx(cVoT6=BJVQY;(QBef@8^0csREo__<seCr9wI3=;apQl6OcN>|PwUH!nbKYO{yKkufLEe*jId*dX-9p}nd9$0TTJ**|7(LDBpUi73t~BSdKgl>4vKMO^AKFYFr7>S*dzbS)c3u69KaKen{e0ykE@ZrtY-?gZgdfWz_2-qZu5D%A-2CM8ll_<D+`r=ID|s$CxPQO$&kvl3aQ(!;WtaNhdiGz*_ekp5nSVmYDaqa~#`hcQFMjBlk6Y>|`@P>z-bQ-=$b0OkSH@@T#`uh1`2B$TPTIq`i`~w%E8{D1#Z*08%3A6_FV2uCcmLT;yUBHbEhN4``U&GJd-YD{|IKvt2=OzBAK%QsCH@9I|K&c2e=`2H7UDmQbHs6opF#Q?<6Ik|$MfB{(w>|7qom(J+I#cSq%q$7*wmK1TmR*gMK{07hPLRt%IK$^am9^pOF!+5E1mssM?dY18*DXWTwo{omvyRKk8HpqpXpAytUEjTOUq>)*vV6}w;XzX8eb**o5(v_ZX4gE=g%v5jE|lCA=f3F<v!=ta{c2BH^=>z>&7MN`SHpP<5_ncS&!_g+j$?j9(m7~r|QI8Hf#}J+15rpE&uDpPj}g6Ufqp*Y?8}*s1x7NGw}`mRy-T*E+c+X|A=38;t};3mpE>Dj;wm;c$~Sf;>}>sTE&~e&a;X)gS}!EZw8wRE8YyY1Xg?*Z0M_aGT4Pyab&P>Y!PqS8CUILdtk+d!REe-1B2~&^h>ToHkcLpH-jv{lx#|)-*TVqk6Vr}=SSoI(wp_dA^DF)c*8H{27X7sr`_@$TmSYy7h%qi@16f{h@Zp$%CQ$uroO?>OybG;#}l$WPv$)T=a65n4|Zun>xKW0UwJnOmOZh9e8=clUYYkUevj?<nEO)ijlaluAAU&OqkcI;>~r!jl<*z1nNhxD>?Pm%{*HU<8{^$S-g!2e5?6iB7k_{^$NbYJJYjq1u^;U3dVlA~J09<tenPy)Pvr{lJI}t$qJ9Uz_PE2g9&hM#isO|ZT<@>`9(zOlP+l2*_1GD<lpFM4#t+*yVo&J%zkYGX)BAXO81d)x`ib0Od&lD)k5`^8u8dE%Z$3TG_x|(gdB(q?cAW2i_|CJpmGR7WuBXS9{vv1iz2om)Z~vJ4Q{U@vXQv;W*WX}!=hgpyezKoE;e6!!iT|J1zs~Dl=cFIV8`_@p{PUzAL+t>$@4j~2r;q#We4ifSd1MD|{-Y)7Z;<{9-E;e;Jw^Qsq7Ue9+b{J(cjva~1Jb`B<I{cqbbI0vBpyKQ0vWIF$a~-C50HKb8Mp3?KSA^W-Pt>%SI9VapFQu3n{tQrFNnUFFW9bUzx(1MM6a@k>z&{K_&v^$@#dbV&l7)#^glS>@qEYYmEZrkLdL6m-+R7z2k943ecjid`}BL?{Tb(~4cbAne;BeQ7rOcRr@kfIf`1to>zVc^$p&G_HdMIY@p|R<JNEvJr}a$jC)v&m+0P4oUei9(`<v?<dDw#8wVPxQF0|cU`%0e=U-|vYSx?6CYJ+i0`X0mnCw)GA<-8x>kS))@sXs_IHbdWI>NnEo!&lz>GjFJ8Yk%o`Ed425q0fh}JbRdbnQzpy^&4rsxBXVG$NkE=fqlRGGf$~!zjhz}MzXgUuE+hZyURWEnu;~X_lkkWkBT|Qvyg4;?VZo~A=w`Pb>o5DkNDF!95-aYp_}2S{aWHT-+Iqoj;|6ueCdbs{v-FNKS}FL|B!5rhP10azlS`hJ%5I@54!jM`6<MI+Vi{i{0`!u?fDVJ&h7aH#BbWOb9;7%*rPo=wr5Ak`?Y5u$ky|AqesXtak$@k?A3qH*TNHWy?@4S$tLsu`e$#^I~?!$-+BKq&|?QV!hh%eE5UGH60Xp86xqt(XZ#SNZ^%C&`bwOEyjM^Bl<2*m#Do6q*AvGidM?h2fAucuujARTIEicH#Ubcl6uvrN^^9k~;v^1@7bhV4E>7YL>kj(Ccy{E!55$Y{`ZL7e_zwedU_3kWj|BSlcy=6#|KSSpPq`l{cN|Bg<xb)z<nIXlqu@vTp8rCx-^4X|b3S^x(Zl@3&miUG4Y42p3P3NCKU;k9XK1-Eaf7Y@zxhagEpZO|?~L}!wb-2<{=famb9>?o<bCIe{UPn1BkwmeKEt$UMc>f&uGfy8_y~R8e(iek3!>+F-t%w#aK3&IvEO>*o$J1T>>>7X9oQa+w4LjXSFR8LafaAyz4*3XTv$E!SZ{oB9r=%2YB$%F>+wkSu-<q8&p%$N{aAlm{>6>;^s$~k;Cb|KGADXm_m%&rj~jjMrw@2T?YY0$Tk?;X7C+o?oZkKa$lqwjD?j2N`}O}l-*Z;{K~jE4zmn&k=uPsUn;U&d{w4Fvd!E-m)<x9E`i1A5p8C%7Gg;3$GxeU8=bW8-&wCE@U;ORd)X#kPhCcUxX+QH<|Bdtf{XYM`BlX{z`mS-|f9`2X$^'
raw=zlib.decompress(base64.b85decode(PAYLOAD)).decode()
assert hashlib.sha256(raw.encode()).hexdigest()=='87d3a8dc040fc5be843f088f53de6c5f3b8b4f9aa301c2572a2823da6de7ecb1'
EDGES=[tuple(map(int,x.split(','))) for x in raw.split(';')]
assert len(EDGES)==2259 and len(set(EDGES))==2259
assert all(0<=u<v<N for u,v in EDGES)
ADJ=[set() for _ in range(N)]
for u,v in EDGES: ADJ[u].add(v); ADJ[v].add(u)

def verify(c): return c is not None and len(c)==N and all(0<=x<5 for x in c) and all(c[u]!=c[v] for u,v in EDGES)

def solve_neq(a,b,limit=60):
    col=[-1]*N; sat=[0]*N; un=set(range(N)); nodes=0; t0=time.time()
    def assign(v,c,tr):
        col[v]=c; un.remove(v); tr.append(('c',v))
        bit=1<<c
        for w in ADJ[v]:
            if col[w]==c:return False
            if col[w]<0 and not(sat[w]&bit):
                old=sat[w]; sat[w]|=bit; tr.append(('m',w,old))
                if sat[w]==31:return False
        if (v==a and col[b]==c) or (v==b and col[a]==c):return False
        return True
    def undo(tr):
        for q in reversed(tr):
            if q[0]=='m':sat[q[1]]=q[2]
            else: col[q[1]]=-1; un.add(q[1])
    def choose(): return max(un,key=lambda v:(sat[v].bit_count(),len(ADJ[v]),-v))
    sys.setrecursionlimit(5000)
    def dfs():
        nonlocal nodes
        nodes+=1
        if nodes%10000==0 and time.time()-t0>limit: raise TimeoutError
        if not un:return True
        v=choose(); forbidden=sat[v]
        for c in range(5):
            if forbidden>>c&1:continue
            if (v==a and col[b]==c) or (v==b and col[a]==c):continue
            tr=[]
            if assign(v,c,tr) and dfs():return True
            undo(tr)
        return False
    tr=[]; assert assign(0,0,tr)
    try: ok=dfs()
    except TimeoutError:return None,None,nodes,time.time()-t0
    return ok,(col[:] if ok else None),nodes,time.time()-t0

r3,r11,r33=sp.sqrt(3),sp.sqrt(11),sp.sqrt(33)
orbit={
309:(0,r3),310:(sp.Rational(1,2),r11/2),311:((-1+r33)/4,(r3+r11)/4),312:(sp.Rational(3,2),r3/2),313:((1+r33)/4,(-r3+r11)/4),314:((1+r33)/4,(r3-r11)/4),315:(sp.Rational(3,2),-r3/2),316:((-1+r33)/4,(-r3-r11)/4),317:(sp.Rational(1,2),-r11/2),318:(0,-r3),319:(-sp.Rational(1,2),-r11/2),320:((1-r33)/4,(-r3-r11)/4),321:(-sp.Rational(3,2),-r3/2),322:((-1-r33)/4,(r3-r11)/4),323:((-1-r33)/4,(-r3+r11)/4),324:(-sp.Rational(3,2),r3/2),325:((1-r33)/4,(r3+r11)/4),326:(-sp.Rational(1,2),r11/2)}
assert all(sp.simplify(x*x+y*y-3)==0 for x,y in orbit.values())
print('graph',N,len(EDGES),'edge_serial_sha256',hashlib.sha256(raw.encode()).hexdigest())
print('sqrt3_orbit',len(orbit),'exact_geometry PASS')
satn=0
for j in sorted(orbit):
    ok,c,nodes,secs=solve_neq(0,j)
    assert ok is True and verify(c) and c[0]!=c[j]
    satn+=1
    print('pair',0,j,'SAT','terminal_colours',c[0],c[j],'nodes',nodes)
print('SUMMARY pairs',len(orbit),'SAT',satn,'UNSAT',0,'TIMEOUT',0)
print('ALL_EXACT_CHECKS_PASSED')
