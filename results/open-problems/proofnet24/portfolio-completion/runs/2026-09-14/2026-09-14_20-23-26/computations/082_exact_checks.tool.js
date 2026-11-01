text(ALL_TOOLS.find(t=>t.name==="mcp__codex_apps__github_create_blob"));
const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){[a,b]=[b,a%b];}return a;};
const Q=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);if(d<0n){n=-n;d=-d;}let g=gcd(n,d);return[n/g,d/g];};
const qa=(a,b)=>Q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]),qn=a=>[-a[0],a[1]],qs=(a,b)=>qa(a,qn(b)),qm=(a,b)=>Q(a[0]*b[0],a[1]*b[1]),eq=(a,b)=>a[0]===b[0]&&a[1]===b[1],qlt=(a,b)=>a[0]*b[1]<b[0]*a[1];
const K=(a=Q(0),b=Q(0))=>[a,b],ka=(a,b)=>[qa(a[0],b[0]),qa(a[1],b[1])],kn=a=>[qn(a[0]),qn(a[1])],ks=(a,b)=>ka(a,kn(b)),km=(a,b)=>[qa(qm(a[0],b[0]),qm(Q(5),qm(a[1],b[1]))),qa(qm(a[0],b[1]),qm(a[1],b[0]))],keq=(a,b)=>eq(a[0],b[0])&&eq(a[1],b[1]);
const kz=()=>K(), ki=n=>K(Q(n)); const ksum=a=>a.reduce(ka,kz()),mulmat=(A,B)=>A.map(row=>B[0].map((_,j)=>ksum(row.map((v,k)=>km(v,B[k][j]))))),mv=(A,v)=>A.map(row=>ksum(row.map((a,j)=>km(a,v[j]))));
let checks=0;const check=(ok,label)=>{if(!ok)throw new Error(label);checks++;};
const pairs=[];for(let i=0;i<4;i++)for(let j=i;j<4;j++)pairs.push([i,j]);
function tensor(o){let P=Array.from({length:4},()=>Array.from({length:4},()=>[Q(0),Q(0),Q(0),Q(0)]));for(let a=0;a<10;a++){let[i,j]=pairs[a];for(let [k,v] of o[a]){P[i][j][k-1]=v;P[j][i][k-1]=v;}}return P;}
function valid(P){for(let i=0;i<4;i++)for(let j=0;j<4;j++){check(eq(P[i][j].reduce(qa,Q(0)),Q(1)),"row sum");check(eq(P[i][j][i],Q(0))&&eq(P[i][j][j],Q(0)),"exclusion");for(let k=0;k<4;k++)check(eq(P[i][j][k],P[j][i][k])&&P[i][j][k][0]>=0n,"symmetry positivity");}}
const det=o=>o.map(k=>[[k,Q(1)]]),half=(i,j)=>[[i,Q(1,2)],[j,Q(1,2)]];
const block=tensor([[[3,Q(1)]],half(3,4),[[2,Q(1)]],[[2,Q(1)]],[[4,Q(1)]],[[1,Q(1)]],[[1,Q(1)]],[[1,Q(1)]],half(1,2),[[2,Q(1)]]]);
const cyclic=tensor([[[2,Q(1)]],[[3,Q(1)]],half(2,4),[[2,Q(1)]],[[3,Q(1)]],[[4,Q(1)]],half(1,3),[[4,Q(1)]],[[1,Q(1)]],[[1,Q(1)]]]);
const cycle=tensor(det([2,3,2,2,1,1,1,1,1,1]));
const equip=tensor(pairs.map(([i,j])=>[0,1,2,3].filter(k=>k!==i&&k!==j).map(k=>[k+1,Q(1,i===j?3:2)])));
for(let P of [block,cyclic,cycle,equip])valid(P);
function V(P,x){return[0,1,2,3].map(k=>ksum([0,1,2,3].flatMap(i=>[0,1,2,3].map(j=>km(K(P[i][j][k]),km(x[i],x[j]))))));}
function J(P,x){return[0,1,2,3].map(k=>[0,1,2,3].map(j=>km(ki(2),ksum([0,1,2,3].map(i=>km(K(P[i][j][k]),x[i]))))));}
function tangent(A){return A.slice(0,3).map(r=>r.slice(0,3).map(v=>ks(v,r[3])));}
function char(A){let tr=ksum([A[0][0],A[1][1],A[2][2]]),c2=ksum([[0,1],[0,2],[1,2]].map(([i,j])=>ks(km(A[i][i],A[j][j]),km(A[i][j],A[j][i])))),d=ks(ka(km(A[0][0],ks(km(A[1][1],A[2][2]),km(A[1][2],A[2][1]))),km(A[0][2],ks(km(A[1][0],A[2][1]),km(A[1][1],A[2][0])))),km(A[0][1],ks(km(A[1][0],A[2][2]),km(A[1][2],A[2][0]))));return[ki(1),kn(tr),c2,kn(d)];}
const s=K(Q(-1,2),Q(1,2)),c=K(Q(3,2),Q(-1,2)),rho=K(Q(-2),Q(1)),p=[s,s,c,c].map(x=>km(K(Q(1,2)),x)),h=[c,kn(c),ki(1),ki(-1)];
check(V(block,p).every((x,i)=>keq(x,p[i])),"block fixed point");
check(mv(J(block,p),h).every((x,i)=>keq(x,km(rho,h[i]))),"block positive eigenline tangent");
for(let t of [Q(-1,10),Q(1,10)]){let x=p.map((v,i)=>ka(v,km(K(t),h[i]))),expected=p.map((v,i)=>ka(v,km(km(rho,K(t)),h[i])));check(V(block,x).every((v,i)=>keq(v,expected[i])),"exact nonlinear eigenline sample");}
const bchar=char(tangent(J(block,p)));const ev=[rho,ki(-1),K(Q(1),Q(-1))];const expected=[ki(1),kn(ksum(ev)),ksum([km(ev[0],ev[1]),km(ev[0],ev[2]),km(ev[1],ev[2])]),kn(km(km(ev[0],ev[1]),ev[2]))];check(bchar.every((v,i)=>keq(v,expected[i])),"block characteristic polynomial");
const u=Array(4).fill(K(Q(1,4)));check(V(cyclic,u).every(v=>keq(v,u[0])),"cyclic fixed point");check(char(tangent(J(cyclic,u))).every((v,i)=>keq(v,[ki(1),ki(2),K(Q(9,4)),K(Q(5,4))][i])),"cyclic characteristic polynomial");
const E=tangent(J(equip,u));check(E.every((r,i)=>r.every((v,j)=>keq(v,K(Q(i===j?-2:0,3))))),"equip tangent derivative");
const e1=[ki(1),kz(),kz(),kz()],e2=[kz(),ki(1),kz(),kz()];check(V(cycle,e1).every((v,i)=>keq(v,e2[i]))&&V(cycle,e2).every((v,i)=>keq(v,e1[i])),"vertex cycle");
const Ap=tangent(J(cycle,e1)),Aq=tangent(J(cycle,e2));check(mulmat(Ap,Aq).every(r=>r.every(v=>keq(v,kz())))&&mulmat(Aq,Ap).every(r=>r.every(v=>keq(v,kz()))),"both zero tangent return products");
const ep=Q(1,50),r=Q(21,1000);check(eq(qa(ep,qm(Q(2),qm(r,r))),Q(10441,500000)),"cap bound identity");check(qlt(Q(10441,500000),r),"strict cap bound");check(eq(qm(Q(24),qa(ep,r)),Q(123,125))&&qlt(Q(123,125),Q(1)),"contraction constant");check(eq(qm(Q(1,3),qm(Q(5,9),Q(5,9))),Q(25,243)),"coordinate floor constant");
store("082_exact_checks",{checks,all_exact_checks_passed:true,method:"JavaScript BigInt rational arithmetic and Q(sqrt(5)); mathematical continuum claims proved in report"});
text(load("082_exact_checks"));
text({halfRate:(Math.sqrt(5)-1)/2,rate051:(51*Math.sqrt(5)-53)/100,rateC:3*Math.sqrt(5)-6,localInstabilityWeight:2/Math.sqrt(5)});