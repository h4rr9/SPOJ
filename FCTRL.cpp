#include<bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    ll T,N,count_5,count_2,temp1,temp2;

    cin>>T;

    while(T--){
        cin>>N;
        count_5=count_2=0,temp1=temp2=N;
        while(temp1 && temp2){
            temp1/=5;
            temp2/=2;
            count_5+=temp1;
            count_2+=temp2;
        }


        cout<<min(count_5,count_2)<<endl;

    }


    return 0;
}
