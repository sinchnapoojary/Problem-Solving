//Find if the number is prime or not

public class prime{
    public static void main(String arg[]){
        int n =7;
        int flag=0;
        for (int i=2;i*i<=n;i++)
        {
            if (n%i==0)
            {
                flag=1;
                System.out.println("Not Prime");
                break;
            }
        }
        if (flag==0)
        System.out.println("Prime");
    }
}


