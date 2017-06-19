#include<bits/stdc++.h>
#include<algorithm>
#define ll long long

using namespace std;

int main()
{
    ll T,H,W;

    cin>>T;

    while(T--){
        cin>>H>>W;
        ll a[H][W];
        for(ll i =0;i<H;i++)
            for(ll j =0;j<W;j++)
                cin>>a[i][j];


        for(ll i = H-2;i>=0;i--)
            for(ll j =0;j<W;j++){

                if(j == 0){
                    a[i][j]+=max(a[i+1][j],a[i+1][j+1]);
                }
                else if(j == W-1){
                    a[i][j]+=max(a[i+1][j],a[i+1][j-1]);
                }
                else{
                    a[i][j]+=max(a[i+1][j],max(a[i+1][j+1],a[i+1][j-1]));
                }

            }

            cout<<*max_element(a[0],a[0]+W)<<endl;
    }

    return 0;
}
