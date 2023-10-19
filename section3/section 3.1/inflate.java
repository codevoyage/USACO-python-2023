/*
ID: shikha11
LANG: JAVA
TASK: inflate
 */

import java.io.*;
import java.util.StringTokenizer;

public class inflate {
  public static void main(String[] args) throws IOException {
    BufferedReader fin = new BufferedReader(new FileReader("inflate.in"));
    PrintWriter fout = new PrintWriter(new FileWriter("inflate.out"));

    StringTokenizer st = new StringTokenizer(fin.readLine());
    int M = Integer.parseInt(st.nextToken());
    int N = Integer.parseInt(st.nextToken());

    int[] points = new int[N];
    int[] minutes = new int[N];

    for (int i = 0; i < N; i++) {
      st = new StringTokenizer(fin.readLine());
      points[i] = Integer.parseInt(st.nextToken());
      minutes[i] = Integer.parseInt(st.nextToken());
    }

    int[] maxPoints = new int[M + 1];

    for (int p = 0; p < N; p++) {
      int t = minutes[p];
      for (int time = t; time <= M; time++) {
        maxPoints[time] = Math.max(maxPoints[time], maxPoints[time - t] + points[p]);
      }
    }

    fout.println(maxPoints[M]);
    fout.close();
  }
}
