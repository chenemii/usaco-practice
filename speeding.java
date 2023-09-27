import java.io.*;
import java.util.*;

// solution from someone else

public class speeding
{
	public static void main(String[] args) throws IOException
	{
		BufferedReader br = new BufferedReader(new FileReader("speeding.in"));
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("speeding.out")));

		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());

		int[] speedLimits = new int[100];
		int currentMile = 0;

		// inputting speed limit for each mile into array
		for(int i = 0; i<n; i++)
		{
			st = new StringTokenizer(br.readLine());
			int length = Integer.parseInt(st.nextToken());
			int limit = Integer.parseInt(st.nextToken());

			for(int j = 0; j<length; j++)
			{
				speedLimits[currentMile] = limit;
				currentMile++;
			}
		}

		int[] travelSpeed = new int[100];
		currentMile = 0;

		// inputting speed traveled for each mile into array
		for(int i = 0; i<m; i++)
		{
			st = new StringTokenizer(br.readLine());
			int length = Integer.parseInt(st.nextToken());
			int speed = Integer.parseInt(st.nextToken());

			for(int j = 0; j<length; j++)
			{
				travelSpeed[currentMile] = speed;
				currentMile++;
			}
		}

		// comparing speed traveled and speed limit mile per mile
		int maxOver = 0;
		for(int i = 0; i<100; i++)
		{
			int amtExceeded = travelSpeed[i]-speedLimits[i];

			if(amtExceeded>maxOver)
			{
				maxOver = amtExceeded;
			}
		}

		pw.println(maxOver);

		pw.close();

	}

}
