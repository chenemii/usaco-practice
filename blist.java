// not my solution

import java.io.*;
import java.util.*;

public class Blist
{
	public static void main(String[] args) throws IOException
	{
		
		BufferedReader br = new BufferedReader(new FileReader("blist.in"));
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("blist.out")));

		StringTokenizer st = new StringTokenizer(br.readLine());

		int numcows = Integer.parseInt(st.nextToken());
		int[][] cows = new int [numcows][3];

		for(int i = 0; i<numcows; i++)
		{
			st = new StringTokenizer(br.readLine());
			cows[i][0] = Integer.parseInt(st.nextToken()); 
			cows[i][1] = Integer.parseInt(st.nextToken()); 
			cows[i][2] = Integer.parseInt(st.nextToken()); 
		}

		int maxbuckets = 0;
		int maxtime = 1000;

		for(int i = 0; i<=maxtime; i++)
		{
			int bucketsused = 0;
			for(int[] cow : cows)
			{
				if(cow[0] <= i && i <= cow[1])
				{
					bucketsused += cow[2];
				}
			}

			maxbuckets = Math.max(bucketsused, maxbuckets);
		}

		System.out.print(maxbuckets);
		pw.close();


	}
}
