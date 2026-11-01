// Agent079 independent exact audit of Agent019's five-site example.
// Run with a modern Node.js runtime: node 079_rank_two_exact.js
// Uses only BigInt rational arithmetic. No external dependencies.
// This checks one example and constants; it is not a universal proof.
"use strict";

const gcd = (a,b) => {
  a=a<0n?-a:a; b=b<0n?-b:b;
  while(b) [a,b]=[b,a%b];
  return a;
};
const rat=(a,b=1n)=>{
  a=BigInt(a); b=BigInt(b);
  if(!b) throw new Error("Zero denominator");
  if(b<0n){a=-a;b=-b;}
  const g=gcd(a,b);
  return [a/g,b/g];
};
const add=(a,b)=>rat(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
const neg=a=>[-a[0],a[1]],sub=(a,b)=>add(a,neg(b));
const mul=(a,b)=>rat(a[0]*b[0],a[1]*b[1]);
const div=(a,b)=>rat(a[0]*b[1],a[1]*b[0]);
const eq=(a,b)=>a[0]*b[1]===b[0]*a[1];
const fmt=a=>a[1]===1n?String(a[0]):String(a[0])+"/"+String(a[1]);
const Z=rat(0),O=rat(1),n=5;
const mat=f=>Array.from({length:n},(_,i)=>Array.from({length:n},(_,j)=>f(i,j)));
const sum=arr=>arr.reduce(add,Z);
const plus=(A,B)=>mat((i,j)=>add(A[i][j],B[i][j]));
const minus=(A,B)=>mat((i,j)=>sub(A[i][j],B[i][j]));
const scale=(A,s)=>mat((i,j)=>mul(A[i][j],s));
const mm=(A,B)=>mat((i,j)=>sum(Array.from({length:n},(_,k)=>mul(A[i][k],B[k][j]))));
const tr=A=>mat((i,j)=>A[j][i]);
const I=mat((i,j)=>i===j?O:Z),zero=mat(()=>Z);
const a=[1,2,3,4,5];
const Q=mat((i,j)=>sub(i===j?O:Z,rat(2*a[i]*a[j],55)));
const l=[rat(1,3),rat(2,3),rat(1,5),rat(2,5),rat(3,5)];
const B=mat((i,j)=>i===j?l[i]:
  ((i===0&&j===2)||(i===2&&j===0))?rat(1,100):
  ((i===1&&j===3)||(i===3&&j===1))?rat(1,80):Z);
const K=mm(mm(Q,B),tr(Q));
const proj=k=>mat((i,j)=>mul(Q[i][k],Q[j][k]));
const P=proj(0),V=proj(1),R=minus(minus(I,P),V);
const C=mm(mm(R,K),R);
const Cspec=[2,3,4].reduce((acc,k)=>plus(acc,scale(proj(k),l[k])),zero);

const det=(M)=>{
  if(!M.length)return O;
  let A=M.map(row=>row.slice()),d=O;
  for(let k=0;k<A.length;k++){
    let p=k;
    while(p<A.length&&A[p][k][0]===0n)p++;
    if(p===A.length)return Z;
    if(p!==k){[A[p],A[k]]=[A[k],A[p]];d=neg(d);}
    let pivot=A[k][k]; d=mul(d,pivot);
    for(let i=k+1;i<A.length;i++){
      let t=div(A[i][k],pivot);
      for(let j=k+1;j<A.length;j++)
        A[i][j]=sub(A[i][j],mul(t,A[k][j]));
      A[i][k]=Z;
    }
  }
  return d;
};
const masks=Array.from({length:1<<n},(_,mask)=>
  Array.from({length:n},(_,i)=>i).filter(i=>mask&(1<<i)));
const w=[1,1,2,3,4];
const f=masks.map(s=>Math.max(0,s.reduce((a,i)=>a+w[i],0)-4)**2);
const fc=f.map((_,m)=>f[31^m]);
const mobius=f=>{
  const c=f.slice();
  for(let i=0;i<n;i++)for(let m=0;m<(1<<n);m++)
    if(m&(1<<i))c[m]-=c[m^(1<<i)];
  return c;
};
const c=mobius(f),cc=mobius(fc);
const F=(A,c)=>sum(masks.map((s,m)=>c[m]===0?Z:
  mul(rat(c[m]),det(s.map(i=>s.map(j=>A[i][j]))))));
// Exact mixed finite difference: separate rank-one affinity makes
// this equal to the mixed derivative, even outside the contraction set.
const q=(A,c)=>sub(
  sub(add(F(plus(plus(A,P),V),c),F(A,c)),F(plus(A,P),c)),
  F(plus(A,V),c));

let superCount=0,superMin=Infinity;
for(let i=0;i<n;i++)for(let j=i+1;j<n;j++)for(let t=0;t<32;t++)
  if(!(t&((1<<i)|(1<<j)))){
    const d=f[t|(1<<i)|(1<<j)]+f[t]-f[t|(1<<i)]-f[t|(1<<j)];
    superMin=Math.min(superMin,d);superCount++;
  }
const qK=q(K,c),qC=q(C,c);
const vertices=[];let interp=Z;
for(let J=0;J<8;J++){
  let W=zero,weight=O;
  for(let j=0;j<3;j++){
    if(J&(1<<j))W=plus(W,proj(j+2));
    weight=mul(weight,J&(1<<j)?l[j+2]:sub(O,l[j+2]));
  }
  const qv=q(W,c),dual=q(minus(R,W),cc);
  interp=add(interp,mul(weight,qv));
  vertices.push({
    J,rank:J.toString(2).replaceAll("0","").length,
    weight:fmt(weight),q:fmt(qv),complement_q:fmt(dual),
    duality_exact:eq(qv,dual)
  });
}
const result={
  computation:"Independent JavaScript BigInt rational determinant finite differences; no sampling",
  supermodularity:{inequalities:superCount,min:superMin},
  negative_mobius:c.map((x,i)=>[i,x]).filter(x=>x[1]<0),
  orthogonal_exact:mm(Q,tr(Q)).every((row,i)=>row.every((x,j)=>eq(x,I[i][j]))),
  compression_matrix_matches_spectral:C.every((row,i)=>row.every((x,j)=>eq(x,Cspec[i][j]))),
  qK:fmt(qK),qRKR:fmt(qC),convex_interpolation:fmt(interp),
  claimed_value_matches:eq(qK,rat(14398,6875)),
  vertices
};

const assert=(ok,msg)=>{if(!ok)throw new Error(msg);};
assert(superCount===80&&superMin===0,"Supermodularity check failed");
assert(result.negative_mobius.length===4,"Expected negative higher Mobius coefficients");
assert(result.orthogonal_exact,"Householder orthogonality failed");
assert(result.compression_matrix_matches_spectral,"Compression matrix identity failed");
assert(eq(qK,qC),"Mixed derivative compression failed");
assert(eq(qK,interp),"Spectral interpolation failed");
assert(result.claimed_value_matches,"Claimed exact value differs");
const expectedQ=[
  "20/121","5836/3025","7409/3025","2074/605",
  "958/605","2038/605","2138/605","2138/605"
];
const expectedWeights=[
  "24/125","6/125","16/125","4/125",
  "36/125","9/125","24/125","6/125"
];
for(let j=0;j<vertices.length;j++){
  assert(vertices[j].duality_exact,"Complement identity failed at vertex "+j);
  assert(vertices[j].q===expectedQ[j],"Projection derivative differs at vertex "+j);
  assert(vertices[j].weight===expectedWeights[j],"Interpolation weight differs at vertex "+j);
}
console.log(JSON.stringify(result,null,2));
