import java.io.*;
import java.util.*;

public class MixMilk {
	static final int N = 3;  // The number of buckets (which is 3)
	static final int TURN_NUM = 100;

	public static void main(String[] args) throws IOException {
		Kattio io = new Kattio("mixmilk");

		// capacity[i] is the maximum capacity of bucket i
		int[] capacity = new int[N];
		// milk[i] is the current amount of milk in bucket i
		int[] milk = new int[N];

		//inputs values into capacity and milk amount
		for (int i = 0; i < N; i++) {
			capacity[i] = io.nextInt();
			milk[i] = io.nextInt();
		}

		//100 pours
		for (int i = 0; i < TURN_NUM; i++) 
		{
			//source bucket
			// i % N ensures that it is rotating from bucket numbers 0, 1, and 2
			int from = i % N;

			//receiver bucket
			int to = (i + 1) % N;
			
			//amount = minimum of remaining milk in bucket 1 and available capacity of bucket 2
			int amt = Math.min(milk[from], capacity[to] - milk[to]);

			//subtract poured amount 
			milk[from] -= amt;

			// add poured amount 
			milk[to] += amt;
		}

		//print final amounts
		for (int m : milk) 
		{ 
			io.println(m); 
		}
		io.close();
	}


	static class Kattio extends PrintWriter 
	{
		private BufferedReader r;
		private StringTokenizer st;
		
		// standard input
		public Kattio()
		{ 
			this(System.in, System.out); 
		}
		public Kattio(InputStream i, OutputStream o) 
		{
			super(o);
			r = new BufferedReader(new InputStreamReader(i));
		}
		// USACO-style file input
		public Kattio(String problemName) throws IOException 
		{
			super(problemName + ".out");
			r = new BufferedReader(new FileReader(problemName + ".in"));
		}
		// returns null if no more input
		public String next() 
		{
			try 
			{
				while (st == null || !st.hasMoreTokens())
					st = new StringTokenizer(r.readLine());
				return st.nextToken();
			} catch (Exception e) 
				{ 

				}
			return null;
		}

		//reading ints doubles and longs
		public int nextInt() 
		{ 
			return Integer.parseInt(next()); 
		}
		public double nextDouble() 
		{
			return Double.parseDouble(next()); 
		}
		public long nextLong() 
		{
			return Long.parseLong(next());
		}
	}

}
