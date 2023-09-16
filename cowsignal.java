//http://www.usaco.org/index.php?page=viewproblem2&cpid=665

import java.io.*;
import java.util.*;

//solution from someone else

public class CowSignal 
{
	public static void main(String[] args) throws IOException 
	{
		BufferedReader in = new BufferedReader(new FileReader("cowsignal.in")); 
		PrintWriter out = new PrintWriter(new BufferedWriter(new 
			FileWriter("cowsignal.out"))); 

		StringTokenizer st = new StringTokenizer(in.readLine());

		int M = Integer.parseInt(st.nextToken());
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());

		for(int i = 0; i < M; i++) // for each line
		{
			String line = in.readLine();
			String output = "";

			//multiply each character
			for(int j = 0; j < N; j++) // for each character
			{
				for(int k = 0; k < K; k++) // multiply individual chars by expansion size
				{
					output+=line.charAt(j); // add to output
				}
			}
			
			//multiply each line
			for(int j = 0; j < K; j++) // for expansion size in each line
			{
				out.println(output); // multiply output by expansion to get expanded lines
			}

		}
			out.close();

	}

}

