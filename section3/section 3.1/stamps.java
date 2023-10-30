/*
ID: shikha11
LANG: JAVA
TASK: stamps
 */

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class stamps {
  public static void main(String[] args) throws IOException {
    BufferedReader fin = new BufferedReader(new FileReader("stamps.in"));
    FileWriter fout = new FileWriter("stamps.out");

    String[] kn = fin.readLine().split(" ");
    int K = Integer.parseInt(kn[0]);
    int N = Integer.parseInt(kn[1]);

    int maxStamp = 0;
    int[] stamps = new int[N];
    String line;
    while ((line = fin.readLine()) != null && Character.isDigit(line.charAt(0)) && maxStamp < N) {
      String[] tokens = line.split(" ");
      for (String token : tokens) {
        int intValue = Integer.parseInt(token);
        stamps[maxStamp] = intValue;
        maxStamp++;
      }
    }

    int maxStampValue = 0;
    for (int i = 0; i < maxStamp; i++) {
      maxStampValue = Math.max(maxStampValue, stamps[i]);
    }
    int maxPossibleValue = maxStampValue * K;

    // initialize dp array to infinity
    int[] dp = new int[maxPossibleValue + 1];
    for (int i = 1; i <= maxPossibleValue; i++) {
      dp[i] = 200000000;
    }

    for (int i = 0; i < maxStamp; i++) {
      for (int j = stamps[i]; j <= maxPossibleValue; j++) {
        dp[j] = Math.min(dp[j], dp[j - stamps[i]] + 1);
      }
    }

    int result = 0;
    while (result <= maxPossibleValue && dp[result] <= K) {
      result++;
    }

    fout.write(String.valueOf(result - 1) + "\n");
    fout.close();
  }
}
