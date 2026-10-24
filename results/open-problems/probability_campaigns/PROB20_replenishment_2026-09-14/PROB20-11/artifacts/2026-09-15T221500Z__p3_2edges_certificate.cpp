#include <bits/stdc++.h>
using namespace std;
static const int N=2048;
int fd(int a,int b){int w=__builtin_popcount((unsigned)(a^b));return min(w,12-w);}
int par(int x){return __builtin_popcount((unsigned)x)&1;}
array<bitset<N>,N> balls;
vector<array<uint16_t,299>> bpts(N);
bitset<N> EVM,ODM;
vector<int> shellv[7];

struct Key{
 int p0,p1,p2,d01,d02,d12;
 bool operator<(Key const&o) const{
   return tie(p0,p1,p2,d01,d02,d12)<tie(o.p0,o.p1,o.p2,o.d01,o.d02,o.d12);
 }
};
map<Key,pair<int,int>> TM;
void initTM(){
 TM[Key{0,0,0,2,2,2}]=make_pair(13,76);
 TM[Key{0,0,0,2,2,4}]=make_pair(5,48);
 TM[Key{0,0,0,2,4,2}]=make_pair(5,48);
 TM[Key{0,0,0,2,4,4}]=make_pair(3,34);
 TM[Key{0,0,0,2,4,6}]=make_pair(0,16);
 TM[Key{0,0,0,2,6,4}]=make_pair(0,16);
 TM[Key{0,0,0,2,6,6}]=make_pair(0,20);
 TM[Key{0,0,0,4,2,2}]=make_pair(5,48);
 TM[Key{0,0,0,4,2,4}]=make_pair(3,34);
 TM[Key{0,0,0,4,2,6}]=make_pair(0,16);
 TM[Key{0,0,0,4,4,2}]=make_pair(3,34);
 TM[Key{0,0,0,4,4,4}]=make_pair(1,20);
 TM[Key{0,0,0,4,4,6}]=make_pair(0,10);
 TM[Key{0,0,0,4,6,2}]=make_pair(0,16);
 TM[Key{0,0,0,4,6,4}]=make_pair(0,10);
 TM[Key{0,0,0,4,6,6}]=make_pair(0,8);
 TM[Key{0,0,0,6,2,4}]=make_pair(0,16);
 TM[Key{0,0,0,6,2,6}]=make_pair(0,20);
 TM[Key{0,0,0,6,4,2}]=make_pair(0,16);
 TM[Key{0,0,0,6,4,4}]=make_pair(0,10);
 TM[Key{0,0,0,6,4,6}]=make_pair(0,8);
 TM[Key{0,0,0,6,6,2}]=make_pair(0,20);
 TM[Key{0,0,0,6,6,4}]=make_pair(0,8);
 TM[Key{0,0,0,6,6,6}]=make_pair(0,4);
 TM[Key{0,0,1,2,1,1}]=make_pair(22,67);
 TM[Key{0,0,1,2,1,3}]=make_pair(22,31);
 TM[Key{0,0,1,2,3,1}]=make_pair(22,31);
 TM[Key{0,0,1,2,3,3}]=make_pair(14,23);
 TM[Key{0,0,1,2,3,5}]=make_pair(7,9);
 TM[Key{0,0,1,2,5,3}]=make_pair(7,9);
 TM[Key{0,0,1,2,5,5}]=make_pair(4,6);
 TM[Key{0,0,1,4,1,3}]=make_pair(6,31);
 TM[Key{0,0,1,4,1,5}]=make_pair(6,10);
 TM[Key{0,0,1,4,3,1}]=make_pair(6,31);
 TM[Key{0,0,1,4,3,3}]=make_pair(5,16);
 TM[Key{0,0,1,4,3,5}]=make_pair(3,7);
 TM[Key{0,0,1,4,5,1}]=make_pair(6,10);
 TM[Key{0,0,1,4,5,3}]=make_pair(3,7);
 TM[Key{0,0,1,4,5,5}]=make_pair(1,3);
 TM[Key{0,0,1,6,1,5}]=make_pair(0,10);
 TM[Key{0,0,1,6,3,3}]=make_pair(0,10);
 TM[Key{0,0,1,6,3,5}]=make_pair(0,4);
 TM[Key{0,0,1,6,5,1}]=make_pair(0,10);
 TM[Key{0,0,1,6,5,3}]=make_pair(0,4);
 TM[Key{0,0,1,6,5,5}]=make_pair(0,1);
 TM[Key{0,1,0,1,2,1}]=make_pair(22,67);
 TM[Key{0,1,0,1,2,3}]=make_pair(22,31);
 TM[Key{0,1,0,1,4,3}]=make_pair(6,31);
 TM[Key{0,1,0,1,4,5}]=make_pair(6,10);
 TM[Key{0,1,0,1,6,5}]=make_pair(0,10);
 TM[Key{0,1,0,3,2,1}]=make_pair(22,31);
 TM[Key{0,1,0,3,2,3}]=make_pair(14,23);
 TM[Key{0,1,0,3,2,5}]=make_pair(7,9);
 TM[Key{0,1,0,3,4,1}]=make_pair(6,31);
 TM[Key{0,1,0,3,4,3}]=make_pair(5,16);
 TM[Key{0,1,0,3,4,5}]=make_pair(3,7);
 TM[Key{0,1,0,3,6,3}]=make_pair(0,10);
 TM[Key{0,1,0,3,6,5}]=make_pair(0,4);
 TM[Key{0,1,0,5,2,3}]=make_pair(7,9);
 TM[Key{0,1,0,5,2,5}]=make_pair(4,6);
 TM[Key{0,1,0,5,4,1}]=make_pair(6,10);
 TM[Key{0,1,0,5,4,3}]=make_pair(3,7);
 TM[Key{0,1,0,5,4,5}]=make_pair(1,3);
 TM[Key{0,1,0,5,6,1}]=make_pair(0,10);
 TM[Key{0,1,0,5,6,3}]=make_pair(0,4);
 TM[Key{0,1,0,5,6,5}]=make_pair(0,1);
 TM[Key{0,1,1,1,1,2}]=make_pair(67,22);
 TM[Key{0,1,1,1,3,2}]=make_pair(31,22);
 TM[Key{0,1,1,1,3,4}]=make_pair(31,6);
 TM[Key{0,1,1,1,5,4}]=make_pair(10,6);
 TM[Key{0,1,1,1,5,6}]=make_pair(10,0);
 TM[Key{0,1,1,3,1,2}]=make_pair(31,22);
 TM[Key{0,1,1,3,1,4}]=make_pair(31,6);
 TM[Key{0,1,1,3,3,2}]=make_pair(23,14);
 TM[Key{0,1,1,3,3,4}]=make_pair(16,5);
 TM[Key{0,1,1,3,3,6}]=make_pair(10,0);
 TM[Key{0,1,1,3,5,2}]=make_pair(9,7);
 TM[Key{0,1,1,3,5,4}]=make_pair(7,3);
 TM[Key{0,1,1,3,5,6}]=make_pair(4,0);
 TM[Key{0,1,1,5,1,4}]=make_pair(10,6);
 TM[Key{0,1,1,5,1,6}]=make_pair(10,0);
 TM[Key{0,1,1,5,3,2}]=make_pair(9,7);
 TM[Key{0,1,1,5,3,4}]=make_pair(7,3);
 TM[Key{0,1,1,5,3,6}]=make_pair(4,0);
 TM[Key{0,1,1,5,5,2}]=make_pair(6,4);
 TM[Key{0,1,1,5,5,4}]=make_pair(3,1);
 TM[Key{0,1,1,5,5,6}]=make_pair(1,0);
 TM[Key{1,0,0,1,1,2}]=make_pair(22,67);
 TM[Key{1,0,0,1,3,2}]=make_pair(22,31);
 TM[Key{1,0,0,1,3,4}]=make_pair(6,31);
 TM[Key{1,0,0,1,5,4}]=make_pair(6,10);
 TM[Key{1,0,0,1,5,6}]=make_pair(0,10);
 TM[Key{1,0,0,3,1,2}]=make_pair(22,31);
 TM[Key{1,0,0,3,1,4}]=make_pair(6,31);
 TM[Key{1,0,0,3,3,2}]=make_pair(14,23);
 TM[Key{1,0,0,3,3,4}]=make_pair(5,16);
 TM[Key{1,0,0,3,3,6}]=make_pair(0,10);
 TM[Key{1,0,0,3,5,2}]=make_pair(7,9);
 TM[Key{1,0,0,3,5,4}]=make_pair(3,7);
 TM[Key{1,0,0,3,5,6}]=make_pair(0,4);
 TM[Key{1,0,0,5,1,4}]=make_pair(6,10);
 TM[Key{1,0,0,5,1,6}]=make_pair(0,10);
 TM[Key{1,0,0,5,3,2}]=make_pair(7,9);
 TM[Key{1,0,0,5,3,4}]=make_pair(3,7);
 TM[Key{1,0,0,5,3,6}]=make_pair(0,4);
 TM[Key{1,0,0,5,5,2}]=make_pair(4,6);
 TM[Key{1,0,0,5,5,4}]=make_pair(1,3);
 TM[Key{1,0,0,5,5,6}]=make_pair(0,1);
 TM[Key{1,0,1,1,2,1}]=make_pair(67,22);
 TM[Key{1,0,1,1,2,3}]=make_pair(31,22);
 TM[Key{1,0,1,1,4,3}]=make_pair(31,6);
 TM[Key{1,0,1,1,4,5}]=make_pair(10,6);
 TM[Key{1,0,1,1,6,5}]=make_pair(10,0);
 TM[Key{1,0,1,3,2,1}]=make_pair(31,22);
 TM[Key{1,0,1,3,2,3}]=make_pair(23,14);
 TM[Key{1,0,1,3,2,5}]=make_pair(9,7);
 TM[Key{1,0,1,3,4,1}]=make_pair(31,6);
 TM[Key{1,0,1,3,4,3}]=make_pair(16,5);
 TM[Key{1,0,1,3,4,5}]=make_pair(7,3);
 TM[Key{1,0,1,3,6,3}]=make_pair(10,0);
 TM[Key{1,0,1,3,6,5}]=make_pair(4,0);
 TM[Key{1,0,1,5,2,3}]=make_pair(9,7);
 TM[Key{1,0,1,5,2,5}]=make_pair(6,4);
 TM[Key{1,0,1,5,4,1}]=make_pair(10,6);
 TM[Key{1,0,1,5,4,3}]=make_pair(7,3);
 TM[Key{1,0,1,5,4,5}]=make_pair(3,1);
 TM[Key{1,0,1,5,6,1}]=make_pair(10,0);
 TM[Key{1,0,1,5,6,3}]=make_pair(4,0);
 TM[Key{1,0,1,5,6,5}]=make_pair(1,0);
 TM[Key{1,1,0,2,1,1}]=make_pair(67,22);
 TM[Key{1,1,0,2,1,3}]=make_pair(31,22);
 TM[Key{1,1,0,2,3,1}]=make_pair(31,22);
 TM[Key{1,1,0,2,3,3}]=make_pair(23,14);
 TM[Key{1,1,0,2,3,5}]=make_pair(9,7);
 TM[Key{1,1,0,2,5,3}]=make_pair(9,7);
 TM[Key{1,1,0,2,5,5}]=make_pair(6,4);
 TM[Key{1,1,0,4,1,3}]=make_pair(31,6);
 TM[Key{1,1,0,4,1,5}]=make_pair(10,6);
 TM[Key{1,1,0,4,3,1}]=make_pair(31,6);
 TM[Key{1,1,0,4,3,3}]=make_pair(16,5);
 TM[Key{1,1,0,4,3,5}]=make_pair(7,3);
 TM[Key{1,1,0,4,5,1}]=make_pair(10,6);
 TM[Key{1,1,0,4,5,3}]=make_pair(7,3);
 TM[Key{1,1,0,4,5,5}]=make_pair(3,1);
 TM[Key{1,1,0,6,1,5}]=make_pair(10,0);
 TM[Key{1,1,0,6,3,3}]=make_pair(10,0);
 TM[Key{1,1,0,6,3,5}]=make_pair(4,0);
 TM[Key{1,1,0,6,5,1}]=make_pair(10,0);
 TM[Key{1,1,0,6,5,3}]=make_pair(4,0);
 TM[Key{1,1,0,6,5,5}]=make_pair(1,0);
 TM[Key{1,1,1,2,2,2}]=make_pair(76,13);
 TM[Key{1,1,1,2,2,4}]=make_pair(48,5);
 TM[Key{1,1,1,2,4,2}]=make_pair(48,5);
 TM[Key{1,1,1,2,4,4}]=make_pair(34,3);
 TM[Key{1,1,1,2,4,6}]=make_pair(16,0);
 TM[Key{1,1,1,2,6,4}]=make_pair(16,0);
 TM[Key{1,1,1,2,6,6}]=make_pair(20,0);
 TM[Key{1,1,1,4,2,2}]=make_pair(48,5);
 TM[Key{1,1,1,4,2,4}]=make_pair(34,3);
 TM[Key{1,1,1,4,2,6}]=make_pair(16,0);
 TM[Key{1,1,1,4,4,2}]=make_pair(34,3);
 TM[Key{1,1,1,4,4,4}]=make_pair(20,1);
 TM[Key{1,1,1,4,4,6}]=make_pair(10,0);
 TM[Key{1,1,1,4,6,2}]=make_pair(16,0);
 TM[Key{1,1,1,4,6,4}]=make_pair(10,0);
 TM[Key{1,1,1,4,6,6}]=make_pair(8,0);
 TM[Key{1,1,1,6,2,4}]=make_pair(16,0);
 TM[Key{1,1,1,6,2,6}]=make_pair(20,0);
 TM[Key{1,1,1,6,4,2}]=make_pair(16,0);
 TM[Key{1,1,1,6,4,4}]=make_pair(10,0);
 TM[Key{1,1,1,6,4,6}]=make_pair(8,0);
 TM[Key{1,1,1,6,6,2}]=make_pair(20,0);
 TM[Key{1,1,1,6,6,4}]=make_pair(8,0);
 TM[Key{1,1,1,6,6,6}]=make_pair(4,0);
}

pair<int,int> triMax(int p0,int p1,int p2,int d01,int d02,int d12){
 int ps[3]={p0,p1,p2}; int D[3][3]={{0,d01,d02},{d01,0,d12},{d02,d12,0}};
 int q[3]={0,1,2};
 sort(q,q+3);
 do{
   Key k{ps[q[0]],ps[q[1]],ps[q[2]],D[q[0]][q[1]],D[q[0]][q[2]],D[q[1]][q[2]]};
   auto it=TM.find(k); if(it!=TM.end()) return it->second;
 }while(next_permutation(q,q+3));
 assert(false); return {-1,-1};
}
struct State{int id; array<int,7> ap; array<int,4> ds; int neven; array<int,2> U;};
vector<State> states(){
 return {
  State{1,array<int,7>{0,0,0,0,0,1,1},array<int,4>{2,4,2,2},6,array<int,2>{1030,1054}},
  State{2,array<int,7>{0,0,0,0,0,1,1},array<int,4>{2,4,4,2},6,array<int,2>{1028,1044}},
  State{3,array<int,7>{0,0,0,0,0,1,1},array<int,4>{4,4,2,2},6,array<int,2>{1028,1050}},
  State{4,array<int,7>{0,0,0,0,0,1,1},array<int,4>{4,4,4,2},6,array<int,2>{1026,1040}},
  State{5,array<int,7>{0,0,0,1,1,1,1},array<int,4>{2,4,2,2},6,array<int,2>{1050,1034}},
  State{6,array<int,7>{0,0,0,1,1,1,1},array<int,4>{2,4,2,4},6,array<int,2>{1040,1032}},
  State{7,array<int,7>{0,0,0,1,1,1,1},array<int,4>{2,4,4,4},6,array<int,2>{1030,1030}},
  State{8,array<int,7>{0,0,0,1,1,1,1},array<int,4>{4,4,2,2},6,array<int,2>{1048,1030}},
  State{9,array<int,7>{0,0,0,1,1,1,1},array<int,4>{4,4,2,4},6,array<int,2>{1038,1028}},
  State{10,array<int,7>{0,0,0,1,1,1,1},array<int,4>{4,4,4,4},6,array<int,2>{1028,1026}},
  State{11,array<int,7>{0,0,1,0,0,1,1},array<int,4>{2,3,2,2},6,array<int,2>{1027,1044}},
  State{12,array<int,7>{0,0,1,0,0,1,1},array<int,4>{2,3,4,2},6,array<int,2>{1025,1034}},
  State{13,array<int,7>{0,0,1,0,0,1,1},array<int,4>{4,3,2,2},6,array<int,2>{1024,1035}},
  State{14,array<int,7>{0,0,1,1,1,1,1},array<int,4>{2,3,2,2},6,array<int,2>{1047,1024}},
 };}

long long incH(int old){return old>=3?1LL*(old-1)*(old-2)/2:0;}
struct Search{
 State s; int ps[12],D[12][12],c[12],occ[N]; long long def[2]={0,0},exc[2]={0,0};
 int slack[2]; long long nodes[12]={},leaves=0,covers=0;
 Search(State S):s(S){
   fill(c,c+12,-1); memset(occ,0,sizeof(occ)); memset(D,0,sizeof(D));
   for(int i=0;i<7;i++)ps[i]=s.ap[i];
   int ie=s.neven-count(s.ap.begin(),s.ap.end(),0);
   int pos=7; for(int i=0;i<ie;i++)ps[pos++]=0; while(pos<12)ps[pos++]=1;
   vector<pair<int,int>> es={{0,1},{1,2},{3,4},{5,6}};
   map<pair<int,int>,int> em; for(int k=0;k<4;k++){auto [i,j]=es[k];em[{i,j}]=em[{j,i}]=k;}
   for(int i=0;i<12;i++)for(int j=i+1;j<12;j++){
     int dd=(i<7&&j<7&&em.count({i,j}))?s.ds[em[{i,j}]]:(ps[i]==ps[j]?6:5);
     D[i][j]=D[j][i]=dd;
   }
   slack[0]=s.U[0]-1024; slack[1]=s.U[1]-1024;
 }
 pair<int,int> tri(int a,int b,int cc){auto q=balls[a]&balls[b]&balls[cc];return {(int)(q&EVM).count(),(int)(q&ODM).count()};}
 pair<int,int> expected(int i,int j,int k){return triMax(ps[i],ps[j],ps[k],D[i][j],D[i][k],D[j][k]);}
 void apply(int x,int sg){for(int y:bpts[x])occ[y]+=sg;}
 bool addOK(int v,int x,vector<int>const&as,long long&de,long long&doo,long long&he,long long&ho){
   de=doo=0;
   for(int a=0;a<(int)as.size();a++)for(int b=a+1;b<(int)as.size();b++){
     int i=as[a],j=as[b]; auto actual=tri(c[i],c[j],x), mx=expected(i,j,v);
     assert(actual.first<=mx.first&&actual.second<=mx.second);
     de+=mx.first-actual.first; doo+=mx.second-actual.second;
   }
   if(def[0]+de>slack[0]||def[1]+doo>slack[1])return false;
   he=ho=0;
   for(int y:bpts[x]){
     long long q=incH(occ[y]); if(par(y)==0)he+=q; else ho+=q;
   }
   return def[0]+de+exc[0]+he<=slack[0] && def[1]+doo+exc[1]+ho<=slack[1];
 }
 void rec(int v,vector<int>&as){
   if(v==12){
     leaves++; bitset<N> u; for(int i=0;i<12;i++)u|=balls[c[i]];
     if((int)u.count()==N)covers++;
     return;
   }
   int anchor=-1,best=INT_MAX;
   for(int u:as){int z=shellv[D[v][u]].size(); if(z<best){best=z;anchor=u;}}
   for(int rel:shellv[D[v][anchor]]){
     int x=c[anchor]^rel; if(par(x)!=ps[v])continue;
     bool ok=true; for(int u:as)if(fd(x,c[u])!=D[v][u]){ok=false;break;} if(!ok)continue;
     if(v==4&&x<c[3])continue; if(v==6&&x<c[5])continue;
     if(v>=7){for(int w=v-1;w>=7;--w)if(ps[w]==ps[v]){if(x<c[w])ok=false;break;} if(!ok)continue;}
     long long de,doo,he,ho; if(!addOK(v,x,as,de,doo,he,ho))continue;
     nodes[v]++; c[v]=x; def[0]+=de;def[1]+=doo;exc[0]+=he;exc[1]+=ho;apply(x,1);as.push_back(v);
     rec(v+1,as); as.pop_back();apply(x,-1);exc[0]-=he;exc[1]-=ho;def[0]-=de;def[1]-=doo;c[v]=-1;
   }
 }
 void initFixed(vector<int> const&vals){
   fill(c,c+12,-1);memset(occ,0,sizeof(occ));def[0]=def[1]=exc[0]=exc[1]=0;
   vector<int> as;
   for(int i=0;i<(int)vals.size();i++){c[i]=vals[i];as.push_back(i);apply(c[i],1);}
   for(int i=0;i<(int)vals.size();i++)for(int j=i+1;j<(int)vals.size();j++)for(int k=j+1;k<(int)vals.size();k++){
     auto a=tri(c[i],c[j],c[k]),m=expected(i,j,k);def[0]+=m.first-a.first;def[1]+=m.second-a.second;
   }
   for(int x=0;x<N;x++)if(occ[x]>=4){
     long long q=1LL*(occ[x]-1)*(occ[x]-2)*(occ[x]-3)/6; if(par(x)==0)exc[0]+=q;else exc[1]+=q;
   }
   if(def[0]+exc[0]<=slack[0]&&def[1]+exc[1]<=slack[1])rec(vals.size(),as);
   for(int i:as)apply(c[i],-1);
 }
 void run(){
   int d01=D[0][1],c1=(d01==2?3:15);
   vector<int> c2s;
   if(ps[2]==0)c2s.push_back(d01==2?63:119);
   else if(d01==2)c2s.push_back(31); else c2s={55,496};
   for(int c2:c2s){
     assert(fd(0,c1)==D[0][1]&&fd(0,c2)==D[0][2]&&fd(c1,c2)==D[1][2]);
     if(s.id>=1&&s.id<=4){
       int c3=(d01==2?461:441);
       assert(fd(c3,0)==6&&fd(c3,c1)==6&&fd(c3,c2)==6);
       initFixed({0,c1,c2,c3});
     }else if(s.id==7){
       for(int c3:{460,220,453,205}){
         assert(fd(c3,0)==5&&fd(c3,c1)==5&&fd(c3,c2)==5);
         initFixed({0,c1,c2,c3});
       }
     }else initFixed({0,c1,c2});
   }
 }
};
void initGeom(){
 vector<int>B0;
 for(int x=0;x<N;x++){int d=fd(0,x);shellv[d].push_back(x);if(d<=3)B0.push_back(x);if(par(x)==0)EVM.set(x);}
 ODM=~EVM; assert(B0.size()==299);
 for(int c=0;c<N;c++){int q=0;for(int b:B0){int x=c^b;balls[c].set(x);bpts[c][q++]=x;}assert(q==299);}
}
int main(int argc,char**argv){
 initTM();initGeom();int want=argc>1?atoi(argv[1]):0;int checked=0;
 for(auto s:states()){
   if(want&&s.id!=want)continue; Search q(s); q.run(); checked++;
   cout<<"class "<<s.id<<" slack "<<q.slack[0]<<","<<q.slack[1]<<" leaves "<<q.leaves<<" covers "<<q.covers<<" nodes";
   for(int v=3;v<12;v++)if(q.nodes[v])cout<<" "<<v<<":"<<q.nodes[v];cout<<"\n";
   assert(q.leaves==0&&q.covers==0);
 }
 cout<<"CERTIFICATE PASSED for "<<checked<<" class(es)\n";
}
