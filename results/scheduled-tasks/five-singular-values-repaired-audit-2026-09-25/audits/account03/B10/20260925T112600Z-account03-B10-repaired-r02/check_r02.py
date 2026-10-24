from fractions import Fraction as F
c3=F(15)**6-F(26244)*F(11,4)**6
c2=F(61,5)**8-F(8388608)*F(11,4)**4
conc=F(19)**4-F(2048)*F(68,25)**3*F(63,20)
half=F(76)-F(693,200)*F(548,25)
scalar=F(267)**2-F(12)*F(77)**2
definite=F(51)-F(16)*F(22,7)
indef=F(269)-(F(16)*(F(8)+F(4)*F(1733,2500)+F(6))+F(10,27))
assert c3==F(40788279,1024)>0
assert c2==F(4302512997281,390625)>0
assert conc==F(39009533,78125)>0
assert half==F(59,1250)>0
assert scalar==F(141)>0
assert definite==F(5,7)>0
assert indef==F(4469,16875)>0
s2u=F(14143,10000)
g1=F(44,96)-F(5,96)*s2u
g2=F(44,96)-F(15,96)*s2u
g3=F(44,96)-F(25,96)*s2u
assert g1-F(38,100)==F(299,64000)
assert g2-F(237,1000)==F(67,192000)
assert g3-F(9,100)==F(1,38400)
print("ALL REPAIRED R02 EXACT CERTIFICATES PASS")
print("C3 sixth-power margin =",c3)
print("C2 eighth-power margin =",c2)
print("concentration fourth-power margin =",conc)
print("half-potential <76 margin =",half)
print("diagonal density <267 squared margin =",scalar)
print("definite-pair <51 margin =",definite)
print("indefinite-density <269 margin =",indef)
print("gamma margins =",F(299,64000),F(67,192000),F(1,38400))
