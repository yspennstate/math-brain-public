"use strict";
// Agent092: deterministic BigInt rational verification. Run with Node.js.
const abs=x=>x<0n?-x:x;
function gcd(a,b){a=abs(a);b=abs(b);while(b){const c=a%b;a=b;b=c;}return a;}
function F(a,b=1n){a=BigInt(a);b=BigInt(b);if(!b)throw Error("zero denominator");if(b<0n){a=-a;b=-b;}const g=gcd(a,b);return [a/g,b/g];}
const add=(a,b)=>F(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
const neg=a=>[-a[0],a[1]], sub=(a,b)=>add(a,neg(b));
const mul=(a,b)=>F(a[0]*b[0],a[1]*b[1]), div=(a,b)=>F(a[0]*b[1],a[1]*b[0]);
const eq=(a,b)=>a[0]===b[0]&&a[1]===b[1], str=a=>a[1]===1n?String(a[0]):a[0]+"/"+a[1];
const zero=F(0),one=F(1),sum=xs=>xs.reduce(add,zero);
const dot=(a,b)=>sum(a.map((x,i)=>mul(x,b[i])));
const sc=(c,x)=>x.map(t=>mul(c,t));
const plus=(a,b)=>a.map((x,i)=>add(x,b[i]));
const outer=x=>x.map(a=>x.map(b=>mul(a,b)));
const madd=(A,B)=>A.map((r,i)=>r.map((x,j)=>add(x,B[i][j])));
const msc=(s,A)=>A.map(r=>r.map(x=>mul(s,x)));
const Z=n=>Array.from({length:n},()=>Array.from({length:n},()=>zero));
function det(M){const n=M.length;if(!n)return one;const A=M.map(r=>r.slice());let result=one;
 for(let j=0;j<n;j++){let p=j;while(p<n&&!A[p][j][0])p++;if(p===n)return zero;
 if(p!==j){[A[j],A[p]]=[A[p],A[j]];result=neg(result);}
 const pivot=A[j][j];result=mul(result,pivot);
 for(let i=j+1;i<n;i++){const t=div(A[i][j],pivot);for(let k=j+1;k<n;k++)A[i][k]=sub(A[i][k],mul(t,A[j][k]));A[i][j]=zero;}}
 return result;}
const n=6, N=1<<n, ids=m=>Array.from({length:n},(_,i)=>i).filter(i=>m&(1<<i));
const pc=m=>ids(m).length, weights=[1,1,2,2,3,3];
const f=Array.from({length:N},(_,m)=>{const t=Math.max(0,ids(m).reduce((s,i)=>s+weights[i],0)-4);return F(t*t);});
const c=f.map(x=>x);for(let i=0;i<n;i++)for(let m=0;m<N;m++)if(m&(1<<i))c[m]=sub(c[m],c[m^(1<<i)]);
const expect=K=>sum(c.map((z,m)=>{const I=ids(m);return mul(z,det(I.map(i=>I.map(j=>K[i][j]))));}));
const q=(K,u,v)=>sub(add(expect(madd(madd(K,outer(u)),outer(v))),expect(K)),add(expect(madd(K,outer(u))),expect(madd(K,outer(v)))));
function assert(t,m){if(!t)throw Error(m);}
const aa=Array.from({length:n},(_,i)=>i===0?F(3,5):i===1?F(4,5):zero);
const a0=Array.from({length:n},(_,i)=>i===0?F(-4,5):i===1?F(3,5):zero);
const h=[1,2,3,4], Q=Array.from({length:4},(_,i)=>Array.from({length:4},(_,j)=>sub(F(i===j?1:0),F(h[i]*h[j],15))));
const embed=j=>[zero,zero,...Q.map(r=>r[j])];
const b=embed(0), cc=embed(1),d=embed(2),e=embed(3);
const u=plus(sc(F(3,5),a0),sc(F(4,5),cc)),v=d;
const u2=plus(sc(F(3,5),u),sc(F(4,5),v)),v2=plus(sc(F(-4,5),u),sc(F(3,5),v));
const W=madd(outer(aa),outer(b));
const frame=[aa,b,u2,v2];
for(let i=0;i<4;i++)for(let j=0;j<4;j++)assert(eq(dot(frame[i],frame[j]),F(i===j?1:0)),"frame orthogonality");
for(const x of [u2,v2])assert(x.every(t=>!!t[0]),"update must involve every site");
let inequalities=0,minDelta=null;
for(let i=0;i<n;i++)for(let j=i+1;j<n;j++)for(let m=0;m<N;m++)if(!(m&((1<<i)|(1<<j)))){
const delta=sub(add(f[m|(1<<i)|(1<<j)],f[m]),add(f[m|(1<<i)],f[m|(1<<j)]));
assert(delta[0]>=0n,"supermodularity");inequalities++;if(minDelta===null||delta[0]*minDelta[1]<minDelta[0]*delta[1])minDelta=delta;}
const main=q(W,u2,v2),unrotated=q(W,u,v),cross=q(W,a0,d),within=q(W,cc,d);
const split=add(mul(F(9,25),cross),mul(F(16,25),within));
assert(eq(main,unrotated),"orthonormal-basis invariance");
assert(eq(main,split),"block-degree identity");
assert(c.some((z,m)=>pc(m)>=3&&z[0]<0n),"nontrivial negative high Mobius coefficient");
const lambda=F(2,5),mu=F(3,5),C=madd(msc(lambda,outer(aa)),msc(mu,outer(b)));
const qC=q(C,u2,v2);
const vertices=[Z(n),outer(aa),outer(b),W];
const interpolationWeights=[F(6,25),F(4,25),F(9,25),F(6,25)];
const qVertices=vertices.map(K=>q(K,u2,v2));
assert(qVertices.every(x=>x[0]>=0n),"vertex values");
assert(eq(qC,sum(qVertices.map((x,i)=>mul(x,interpolationWeights[i])))),"spectral interpolation");
const R=Z(n);for(let i=0;i<n;i++)for(let j=0;j<n;j++)R[i][j]=sub(F(i===j?1:0),add(mul(u2[i],u2[j]),mul(v2[i],v2[j])));
const K=madd(madd(C,msc(F(1,3),outer(u2))),msc(F(2,3),outer(v2)));
assert(eq(q(K,u2,v2),qC),"compression identity");
const report={
status:"PASS; every calculation is exact BigInt rational",
inequalities,minElementaryDifference:str(minDelta),
negativeMobius:c.map((z,m)=>({mask:m,size:pc(m),value:str(z)})).filter(o=>o.value.startsWith("-")),
vectors:{a:aa.map(str),b:b.map(str),a0:a0.map(str),c:cc.map(str),d:d.map(str),u:u2.map(str),v:v2.map(str)},
q_projection:str(main),q_cross:str(cross),q_within:str(within),
splittingWeights:["9/25","16/25"],q_compression:str(qC),
q_vertices:qVertices.map(str),interpolationWeights:interpolationWeights.map(str),
checks:["4-column frame orthonormal","both final update vectors supported on all six sites","240 elementary supermodularity inequalities","basis rotation invariance","exact block-degree splitting","rank-two spectral interpolation","compression identity"]
};
console.log(JSON.stringify(report,null,2));