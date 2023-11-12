import java.io.*;
import java.util.*;

public class Traffic 
{
	public static void main(String[] args) throws IOException 
    {
		BufferedReader br = new BufferedReader(new FileReader("traffic.in"));
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("traffic.out")));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int miles = Integer.parseInt(st.nextToken());
		String[] type = new String[miles];
		int[][] flow = new int[2][miles];

		for(int i = 0; i < miles; i++)
		{
			st = new StringTokenizer(br.readLine());
			type[i] = st.nextToken();
			flow[0][i] = Integer.parseInt(st.nextToken());
			flow[1][i] = Integer.parseInt(st.nextToken());
		}

		int min = Integer.MIN_VALUE+100;
		int max = Integer.MAX_VALUE-100;

		//before
		for(int i = miles-1; i>=0; i--)
		{
			if(type[i].equals("none"))
			{
				min = Math.max(min, flow[0][i]);
				max = Math.min(max, flow[1][i]);
			}

			else if(type[i].equals("on"))
			{
				min-=flow[1][i];
				max-=flow[0][i];
			}

			else if(type[i].equals("off"))
			{
				min+=flow[0][i];
				max+=flow[1][i];
			}
		}

		System.out.println(min + " " + max);

		min = Integer.MIN_VALUE+100;
		max = Integer.MAX_VALUE-100;

		//after
		for(int i = 0; i<miles; i++)
		{
			if(type[i].equals("none"))
			{
				min = Math.max(min, flow[0][i]);
				max = Math.min(max, flow[1][i]);
			}

			else if(type[i].equals("on"))
			{
				min+=flow[0][i];
				max+=flow[1][i];

			}

			else if(type[i].equals("off"))
			{
				min-=flow[1][i];
				max-=flow[0][i];
			}
		}

		System.out.println(min + " " + max);

		pw.close();

	}
}
