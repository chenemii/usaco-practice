// not my solution

import java.io.*;
import java.util.StringTokenizer;

public class Main
{
	public static void main(String[] args) throws IOException 
	{
		BufferedReader br = new BufferedReader(new FileReader("lostcow.in"));
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("lostcow.out")));

		StringTokenizer st = new StringTokenizer(br.readLine());
		int john = Integer.parseInt(st.nextToken());
		int cow = Integer.parseInt(st.nextToken());

		int totaldistance = 0;
		int disttravel = 1;
		int direction = 1;
		
		while(true)
		{
			if((direction == 1 && john < cow && (cow <= (john+disttravel))) || (direction == -1 && john > cow && (cow >= (john-disttravel))))
			{
				totaldistance+=Math.abs(cow-john);
				System.out.println(totaldistance);
				break;
			}	

			else
			{
				totaldistance+=disttravel*2;
				disttravel*=2;
				direction*=-1;

			}
		}
	
		pw.close();
	}
}
