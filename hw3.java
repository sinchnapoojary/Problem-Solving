/* 
HW3: Print the given pattern
You are given a number N and you have to print the given pattern:
For N=3
3 3 3 2 2 2 1 1 1
3 3 2 2 1 1
3 2 1
*/

public class hw3{
    public static void  main(String[] args) {
        int i, j, k;
        int n=3;
        for (i=n;i>0;i--)
        {
            for(j=n;j>0;j--)
            {
                for(k=0;k<i;k++)
                {
                    System.out.print(j+" ");
                }
            }
            System.out.println();
        }

        
    }
}