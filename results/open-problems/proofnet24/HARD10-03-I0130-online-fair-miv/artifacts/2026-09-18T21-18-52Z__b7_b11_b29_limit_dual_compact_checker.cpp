#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <set>
#include <tuple>
#include <climits>
#include <vector>
using namespace std;
struct Action{int A,B,dh,c,m;};
static Action mk960(int A,int B){assert(0<=A&&A<=960&&0<=B&&B<=960);assert((9*A+11*B)%40==0);assert((11*A+9*B)%40==0);return{A,B,(9*A+11*B)/40,(11*A+9*B)/40,max(A,B)};}
static vector<Action> fam652(){vector<Action>v;for(int i=0;i<=24;++i)for(int j=0;j<=24;++j)v.push_back(mk960(40*i,40*j));const int ex[][2]={{6,236},{13,233},{67,237},{26,236},{94,234},{84,234},{3,223},{3,233},{74,234},{114,234},{4,234},{176,236},{115,235}};for(auto&p:ex)v.push_back(mk960(4*p[0],4*p[1]));const int cut[][2]={{179,959},{613,953},{649,949},{539,959},{775,955},{885,945},{561,941},{419,959},{586,946},{215,955},{579,959},{70,910},{527,947},{497,957}};for(auto&p:cut)v.push_back(mk960(p[0],p[1]));assert(v.size()==652);return v;}
static pair<long long,long long> branches(const vector<long long>&p,const Action&x,int D,long long P,long long Q){long long H=9LL*x.A*Q-10LL*P*x.m;int DH=D+x.dh;if(DH<(int)p.size())H+=p[DH];int DL=abs(D-x.c);long long L=(D>=x.c?-11LL*x.A*Q:9LL*x.B*Q-40LL*D*Q)-10LL*P*x.m+p[DL];return{H,L};}
struct Run{int first,stable,last;long long first_root,fixed_root,threshold,checked;vector<long long>fixed;};
static Run solve(const vector<Action>&acts,long long P,long long Q,int MAXD=2800,int MAXH=700){vector<long long>prev(MAXD+1),cur(MAXD+1);long long thr=12480LL*Q+28800LL*P;int first=-1,stable=-1;long long fr=-1,checked=0;for(int h=1;h<=MAXH;++h){bool ch=false;for(int D=0;D<=MAXD;++D){long long best=0;for(auto&x:acts){auto[H,L]=branches(prev,x,D,P,Q);best=max(best,min(H,L));}cur[D]=best;ch|=cur[D]!=prev[D];++checked;}prev.swap(cur);if(first<0&&prev[480]>=thr){first=h;fr=prev[480];}if(!ch){stable=h;break;}}int last=-1;for(int D=0;D<=MAXD;++D)if(prev[D])last=D;return{first,stable,last,fr,prev[480],thr,checked,prev};}
struct Face{long long C,S;};static __int128 fv(Face f,long long P,long long Q){return(__int128)f.C*Q+(__int128)f.S*P;}static Face minR(Face a,Face b,long long P,long long Q){auto A=fv(a,P,Q),B=fv(b,P,Q);if(A<B)return a;if(B<A)return b;return a.S<b.S?a:b;}static Face maxR(Face a,Face b,long long P,long long Q){auto A=fv(a,P,Q),B=fv(b,P,Q);if(A>B)return a;if(B>A)return b;return a.S>b.S?a:b;}
static pair<Face,int> fixed_face(const vector<Action>&acts,long long P,long long Q,int MAXD=2800,int MAXH=700){vector<Face>prev(MAXD+1,{0,0}),cur(MAXD+1);for(int h=1;h<=MAXH;++h){bool ch=false;for(int D=0;D<=MAXD;++D){Face best{0,0};for(auto&x:acts){int DH=D+x.dh;Face ph=DH<=MAXD?prev[DH]:Face{0,0};Face H{ph.C+9LL*x.A,ph.S-10LL*x.m};int DL=abs(D-x.c);Face pl=prev[DL];long long base=D>=x.c?-11LL*x.A:9LL*x.B-40LL*D;Face L{pl.C+base,pl.S-10LL*x.m};best=maxR(best,minR(H,L,P,Q),P,Q);}cur[D]=best;ch|=cur[D].C!=prev[D].C||cur[D].S!=prev[D].S;}prev.swap(cur);if(!ch)return{prev[480],h};}return{prev[480],-1};}
int main(){
 const long long P0=64,Q0=28335; auto old=fam652(); auto oldr=solve(old,P0,Q0); assert(oldr.first==248&&oldr.stable==293&&oldr.last==2506&&oldr.fixed_root==oldr.threshold);
 assert(oldr.last==2506); const int residual_cutoff=oldr.last+480; assert(residual_cutoff==2986);
 Action z=mk960(900,940); assert(z.c==459&&z.dh==461);
 auto newer=old; newer.push_back(z); assert(newer.size()==653);
 auto atold=solve(newer,P0,Q0); long long limit_gain=atold.fixed_root-oldr.fixed_root; assert(limit_gain>0);
 const int H0=248,MAXD=2800;vector<vector<long long>>val(H0+1,vector<long long>(MAXD+1));for(int h=1;h<=H0;++h)for(int D=0;D<=MAXD;++D){long long best=0;for(auto&x:old){auto[H,L]=branches(val[h-1],x,D,P0,Q0);best=max(best,min(H,L));}val[h][D]=best;}
 int D=480;long long cap=(1LL<<62);bool saw=false;for(int h=H0;h>=1&&val[h][D]>0;--h){long long best=val[h][D];int sel=-1;long long bsl=-1,sh=0,sl=0;for(int i=0;i<(int)old.size();++i){auto[H,L]=branches(val[h-1],old[i],D,P0,Q0);if(min(H,L)!=best)continue;bool unique=((H==best)!=(L==best));long long s=llabs(H-L);if(unique&&s>bsl){bsl=s;sel=i;sh=H-best;sl=L-best;}}assert(sel>=0);cap=min(cap,bsl);if(h==245&&D==51){auto[ZH,ZL]=branches(val[h-1],z,D,P0,Q0);long long res=min(ZH,ZL)-best;assert(res==326750);assert(cap==125450);assert(res>cap);saw=true;}auto&x=old[sel];D=(sh==0?D+x.dh:abs(D-x.c));}assert(saw);
 vector<vector<long long>>aug(H0+1,vector<long long>(MAXD+1));for(int h=1;h<=H0;++h)for(int DD=0;DD<=MAXD;++DD){long long best=0;for(auto&x:newer){auto[H,L]=branches(aug[h-1],x,DD,P0,Q0);best=max(best,min(H,L));}aug[h][DD]=best;}long long hgain=aug[H0][480]-val[H0][480];assert(hgain>=125450);assert(limit_gain>=hgain);
 long long augroot=aug[H0][480], second=LLONG_MIN; int win=-1; long long wH=0,wL=0;
 for(int i=0;i<(int)newer.size();++i){auto [H,L]=branches(aug[H0-1],newer[i],480,P0,Q0); long long v=min(H,L); if(v>second){second=v;} if(v==augroot){win=i;wH=H;wL=L;}}
 assert(win>=0);
 const long long P1=267,Q1=117230; auto crit=solve(newer,P1,Q1); assert(crit.first==247&&crit.stable==294&&crit.last==2504); assert(crit.first_root==crit.threshold&&crit.fixed_root==crit.threshold);
 auto[face,facest]=fixed_face(newer,P1,Q1); assert(face.C==13014&&face.S==-205660&&facest==294); long long num=face.C-12480,den=28800-face.S,g=gcd(num,den);num/=g;den/=g;assert(num==P1&&den==Q1);
 long long un=9LL*Q1-10LL*P1,ud=10LL*Q1;g=gcd(un,ud);un/=g;ud/=g;assert(un==10524&&ud==11723);long long wn=30LL*un-19LL*ud,wd=30LL*ud;g=gcd(wn,wd);wn/=g;wd/=g;assert(wn==92983&&wd==351690);long long impn=10175LL*ud-un*11334LL,impd=11334LL*ud;g=gcd(llabs(impn),impd);impn/=g;impd/=g;assert(impn==2509&&impd==132868482LL);
 cout<<"I0130_B7_B11_B29_LIMIT_DUAL_COMPACT_PASS\n";
 cout<<"old_family=652 old_eps=64/28335 old_first="<<oldr.first<<" old_stable="<<oldr.stable<<" old_last="<<oldr.last<<"\n";
 cout<<"B29_old_residual_support_cutoff_index="<<residual_cutoff<<" cutoff_gap="<<residual_cutoff<<"/240\n";
 cout<<"candidate_action=900/960,940/960 quotient_u=459/240 quotient_v=461/240\n";
 cout<<"B11_support_state=(h245,D51) local_residual_scaled=326750 path_capacity_scaled=125450 finite_root_gain_scaled="<<hgain<<" fixed_limit_root_gain_scaled="<<limit_gain<<" root_winner_index="<<win<<" root_winner_action="<<newer[win].A<<"/960,"<<newer[win].B<<"/960 root_winner_branch_gap="<<llabs(wH-wL)<<"\n";
 cout<<"new_family=653 new_eps=267/117230 first="<<crit.first<<" stable="<<crit.stable<<" last="<<crit.last<<" fixed_face=(13014-205660*eps)/9600\n";
 cout<<"new_upper=10524/11723 new_width=92983/351690 upper_improvement=2509/132868482 source_valid_total_goods_max="<<crit.first+3<<"\n";
 cout<<"checked_states_old="<<oldr.checked<<" new_at_old="<<atold.checked<<" new_critical="<<crit.checked<<"\n";
}
