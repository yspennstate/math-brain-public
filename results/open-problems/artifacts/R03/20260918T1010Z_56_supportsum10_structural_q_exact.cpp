/*
R03 run56 exact checker.
Scope: nonsymmetric iid Rademacher singularity, finite binary reduction m=10 over F_11.
Research idea before checker:
  * Run55 exact hyperplane-fiber enumeration became expensive at union support 8 (local dimension 6).
  * If a local Boolean slice H spans its six-dimensional factor, every proper affine hyperplane
    misses at least one point, so q_local <= |H|-1. With two free Boolean coordinates globally,
    Q <= max(4 q_local, |C_V|/2) <= |C_V|-4. This is weaker than exact q, but removes all
    projective-hyperplane enumeration and leaves a rigorous positive exact-nullity-two certificate.
  * Exhaust the next overlap-two support-sum-10 shell in disjoint order (5,5), (4,6), (3,7).
Also exactly checks a 3-coordinate counterexample to the universal folded-concentration inequality
as displayed in Eq. (22) of arXiv:1511.05283v7: rho(1,1,2)=1/4, whereas folding the tail with b=-1
at the second coordinate gives rho(1,-1)=1/2.
All arithmetic used for the finite certificate is exact integer / F_11 arithmetic.
*/
#include <bits/stdc++.h>
#include <boost/multiprecision/cpp_int.hpp>
using namespace std; using boost::multiprecision::cpp_int;
static const int M=10,P=11;
using V10=array<unsigned char,10>; using K20=array<unsigned char,20>; using K16=array<unsigned char,16>;
struct Line{V10 v; int mask;}; struct Cand{K20 key; int umask;};
struct Result{long long pairs,uniq,keep,types,pos,nosp; cpp_int E; map<string,long long> hist;};
int modinv(int a){for(int x=1;x<P;x++) if(a*x%P==1) return x; abort();}
vector<Line> gen_lines(int s){
 vector<Line> out; vector<int> c(s);
 function<void(int,int)> rec=[&](int pos,int st){
  if(pos==s){int mask=0;for(int i:c)mask|=1<<i;for(int bits=0;bits<(1<<(s-1));bits++){V10 v{};v.fill(0);v[c[0]]=1;for(int j=1;j<s;j++)v[c[j]]=(bits>>(j-1)&1)?P-1:1;out.push_back({v,mask});}return;}
  for(int i=st;i<=M-(s-pos);i++){c[pos]=i;rec(pos+1,i+1);} };
 rec(0,0); return out;
}
K20 rref2(const V10&a,const V10&b){
 int A[2][M];for(int j=0;j<M;j++){A[0][j]=a[j];A[1][j]=b[j];}int r=0;
 for(int col=0;col<M&&r<2;col++){int piv=-1;for(int rr=r;rr<2;rr++)if(A[rr][col]){piv=rr;break;}if(piv<0)continue;if(piv!=r)for(int j=0;j<M;j++)swap(A[piv][j],A[r][j]);int inv=modinv(A[r][col]);for(int j=0;j<M;j++)A[r][j]=A[r][j]*inv%P;for(int rr=0;rr<2;rr++)if(rr!=r&&A[rr][col]){int f=A[rr][col];for(int j=0;j<M;j++){A[rr][j]=(A[rr][j]-f*A[r][j])%P;if(A[rr][j]<0)A[rr][j]+=P;}}r++;}
 if(r!=2)abort();K20 k{};for(int j=0;j<M;j++){k[j]=A[0][j];k[M+j]=A[1][j];}return k;
}
int smask(const array<int,M>&u){int z=0;for(int i=0;i<M;i++)if(u[i])z|=1<<i;return z;}
bool signrel(const array<int,M>&u){int first=-1;for(int x:u)if(x){first=x;break;}if(first<0)return false;int inv=modinv(first);for(int x:u)if(x){int y=x*inv%P;if(y!=1&&y!=P-1)return false;}return true;}
// stage 0 = target (5,5): exclude historical families through run55.
// stage 1 = target (4,6): additionally exclude any (5,5),ov=2 plane already credited at stage 0.
// stage 2 = target (3,7): additionally exclude any (4,6),ov=2 plane already credited at stage 1.
bool clean(const K20&k,int stage){
 array<int,M>v{},w{};for(int i=0;i<M;i++){v[i]=k[i];w[i]=k[M+i];}
 vector<pair<int,int>> info;int mins=99;
 for(int t=0;t<=P;t++){array<int,M>u{};if(t<P){for(int i=0;i<M;i++)u[i]=(v[i]+t*w[i])%P;}else u=w;int ma=smask(u),s=__builtin_popcount((unsigned)ma);mins=min(mins,s);if(signrel(u))info.push_back({ma,s});}
 if(mins<=2)return false;
 for(int i=0;i<(int)info.size();i++)for(int j=i+1;j<(int)info.size();j++){
  int ov=__builtin_popcount((unsigned)(info[i].first&info[j].first));int a=min(info[i].second,info[j].second),b=max(info[i].second,info[j].second);
  if(ov<=1)return false;
  if(ov==2&&b<=4)return false;
  if(ov==2&&a==3&&b==5)return false;
  if(ov==2&&a==4&&b==5)return false;
  if(ov==2&&a==3&&b==6)return false;
  if(stage>=1&&ov==2&&a==5&&b==5)return false;
  if(stage>=2&&ov==2&&a==4&&b==6)return false;
 }
 return true;
}
K16 localkey(const K20&k,int umask){
 vector<int>idx;for(int i=0;i<M;i++)if(umask>>i&1)idx.push_back(i);if(idx.size()!=8)abort();int A[2][8];for(int j=0;j<8;j++){A[0][j]=k[idx[j]];A[1][j]=k[M+idx[j]];}int r=0;
 for(int col=0;col<8&&r<2;col++){int piv=-1;for(int rr=r;rr<2;rr++)if(A[rr][col]){piv=rr;break;}if(piv<0)continue;if(piv!=r)for(int j=0;j<8;j++)swap(A[piv][j],A[r][j]);int inv=modinv(A[r][col]);for(int j=0;j<8;j++)A[r][j]=A[r][j]*inv%P;for(int rr=0;rr<2;rr++)if(rr!=r&&A[rr][col]){int f=A[rr][col];for(int j=0;j<8;j++){A[rr][j]=(A[rr][j]-f*A[r][j])%P;if(A[rr][j]<0)A[rr][j]+=P;}}r++;}
 if(r!=2)abort();K16 z{};for(int j=0;j<8;j++){z[j]=A[0][j];z[8+j]=A[1][j];}return z;
}
int rank6(vector<array<int,6>> A){int r=0;for(int c=0;c<6;c++){int piv=-1;for(int i=r;i<(int)A.size();i++)if(A[i][c]){piv=i;break;}if(piv<0)continue;swap(A[piv],A[r]);int inv=modinv(A[r][c]);for(int j=0;j<6;j++)A[r][j]=A[r][j]*inv%P;for(int i=0;i<(int)A.size();i++)if(i!=r&&A[i][c]){int f=A[i][c];for(int j=0;j<6;j++){A[i][j]=(A[i][j]-f*A[r][j])%P;if(A[i][j]<0)A[i][j]+=P;}}r++;}return r;}
pair<int,bool> hspan(const K16&k){
 int row[2][8];for(int j=0;j<8;j++){row[0][j]=k[j];row[1][j]=k[8+j];}vector<int>piv;for(int rr=0;rr<2;rr++)for(int j=0;j<8;j++)if(row[rr][j]){piv.push_back(j);break;}vector<int>fr;for(int j=0;j<8;j++)if(find(piv.begin(),piv.end(),j)==piv.end())fr.push_back(j);if(fr.size()!=6)abort();vector<array<int,6>>pts;int h=0;
 for(int bits=0;bits<256;bits++){int s0=0,s1=0;for(int j=0;j<8;j++){int b=(bits>>j)&1;s0+=row[0][j]*b;s1+=row[1][j]*b;}if(s0%P==0&&s1%P==0){h++;array<int,6>x{};for(int q=0;q<6;q++)x[q]=(bits>>fr[q])&1;pts.push_back(x);}}
 return {h,rank6(pts)==6};
}
Result process(int s1,int s2,int stage){
 auto A=gen_lines(s1),B=gen_lines(s2);vector<Cand>cs;
 if(s1==s2){for(size_t i=0;i<A.size();i++)for(size_t j=i+1;j<A.size();j++)if(__builtin_popcount((unsigned)(A[i].mask&A[j].mask))==2)cs.push_back({rref2(A[i].v,A[j].v),A[i].mask|A[j].mask});}
 else {for(auto&a:A)for(auto&b:B)if(__builtin_popcount((unsigned)(a.mask&b.mask))==2)cs.push_back({rref2(a.v,b.v),a.mask|b.mask});}
 sort(cs.begin(),cs.end(),[](const Cand&x,const Cand&y){return x.key<y.key;});vector<Cand>uq;uq.reserve(cs.size());for(auto&x:cs)if(uq.empty()||uq.back().key!=x.key)uq.push_back(x);
 map<K16,long long>lc;long long keep=0;for(auto&x:uq)if(clean(x.key,stage)){if(__builtin_popcount((unsigned)x.umask)!=8)abort();keep++;lc[localkey(x.key,x.umask)]++;}
 Result R{(long long)cs.size(),(long long)uq.size(),keep,(long long)lc.size(),0,0,0,{}};
 for(auto&kv:lc){auto [hloc,span]=hspan(kv.first);long long mult=kv.second;if(!span){R.nosp+=mult;R.hist["nospan_h"+to_string(hloc)]+=mult;continue;}int h=4*hloc,Q=h-4;cpp_int basis=1;bool ok=true;for(int j=0;j<8;j++){int f=h-min(1<<j,Q);if(f<=0)ok=false;basis*=f;}if(!ok||h<=M){R.hist["zero_h"+to_string(hloc)]+=mult;continue;}R.E+=cpp_int(mult)*basis*(h-M+1)*(h-M);R.pos+=mult;R.hist["positive_h"+to_string(hloc)+"_H"+to_string(h)+"_Qbar"+to_string(Q)]+=mult;}
 return R;
}
long long rho_count(const vector<int>&a){long long z=0;for(int bits=0;bits<(1<<(int)a.size());bits++){long long s=0;for(int i=0;i<(int)a.size();i++)s+=((bits>>i)&1?1:-1)*a[i];if(s==0)z++;}return z;}
void show(const string&name,const Result&R){cout<<name<<" pairs="<<R.pairs<<" unique="<<R.uniq<<" keep="<<R.keep<<" types="<<R.types<<" pos="<<R.pos<<" nospan="<<R.nosp<<" E="<<R.E<<"\n";for(auto&z:R.hist)cout<<"  "<<z.first<<"="<<z.second<<"\n";}
int main(){
 Result a=process(5,5,0),b=process(4,6,1),c=process(3,7,2);
 if(a.pairs!=3225600||a.uniq!=3225600||a.keep!=3225600||a.types!=71680||a.pos!=2658600||a.nosp!=567000||a.E!=cpp_int("1071421143754060431360000"))return 21;
 if(b.pairs!=4838400||b.uniq!=3628800||b.keep!=3628800||b.types!=80640||b.pos!=2825550||b.nosp!=803250||b.E!=cpp_int("2074472379299873710080000"))return 22;
 if(c.pairs!=1935360||c.uniq!=1935360||c.keep!=967680||c.types!=21504||c.pos!=619920||c.nosp!=347760||c.E!=cpp_int("218427714332084404224000"))return 23;
 cpp_int E=a.E+b.E+c.E;if(E!=cpp_int("3364321237386018545664000"))return 24;
 cpp_int slackN=177023,slackD=16105,den=cpp_int(1)<<89;
 cpp_int corrN("1817511713884842410306025"),corrD("30421484882646254466629632");
 if(slackN*E*corrD!=corrN*slackD*den)return 25;
 cpp_int baseN("32588228263069034684065387846935"),baseD("62303201039659529147657486336");
 cpp_int newN("32584505999078998526809081107735"),newD("62303201039659529147657486336");
 if((baseN*newD-newN*baseD)*corrD!=corrN*baseD*newD)return 26;
 long long orig=rho_count({1,1,2}),fold=rho_count({1,-1});
 if(orig!=2||fold!=2)return 27;
 show("(5,5)",a);show("(4,6)",b);show("(3,7)",c);
 cout<<"TOTAL_E="<<E<<"\n";
 cout<<"COMBINED_CORRECTION="<<corrN<<"/"<<corrD<<"\n";
 cout<<"NEW_R11="<<newN<<"/"<<newD<<"\n";
 cout<<"BLINOVSKY_FOLD_COUNTEREXAMPLE: rho(1,1,2)=2/8=1/4; rho(1,-1)=2/4=1/2\n";
 cout<<"SELF-CHECK PASS\n";
}
