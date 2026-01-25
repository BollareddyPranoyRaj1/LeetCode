class Solution {
    public int reverse(int x) {
        int rev=0,n,N=x;
        if(N<0){
            x*=-1;
        }
        while(x>0){
            n=x%10;
            if(rev>(Integer.MAX_VALUE-n)/10){
                return 0;
            }
            rev=rev*10+n;
            x/=10;
        }
        if(N<0){
            rev*=-1;
        }
        return rev;
    }
}