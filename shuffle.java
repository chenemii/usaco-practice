import java.util.*;
import java.io.*;

public class shuffle
{
    public static void main(String[] args) throws IOException
    {
        BufferedReader br = new BufferedReader(new FileReader("shuffle.in"));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("shuffle.out")));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int cows = Integer.parseInt(st.nextToken());
       
        st = new StringTokenizer(br.readLine());
        int[] moves = new int[cows];
        for(int i = 0; i<cows;i++)
        {
            moves[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        int[] end = new int[cows];
        for(int i = 0; i<cows;i++)
        {
            end[i] = Integer.parseInt(st.nextToken());
        }

  
        for(int i = 0; i<3; i++)
        {
            int[] og = new int[cows];

            for(int j = 0; j<cows; j++)
            {
                og[j] = end[moves[j] - 1];
            }

            end = og;
        }
       
        
        for(int i = 0; i<cows; i++)
        {
            System.out.println(end[i]);
        }

        pw.close();
        
    }
}
