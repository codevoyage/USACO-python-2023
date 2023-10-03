/*
ID: shikha11
LANG: JAVA
TASK: cowtour
 */

import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class cowtour {

    static class Point {
        int x, y;

        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public static void main(String[] args) throws FileNotFoundException {
        Scanner fin = new Scanner(new File("cowtour.in"));
        PrintWriter fout = new PrintWriter(new File("cowtour.out"));

        int n = Integer.parseInt(fin.nextLine());
        Point[] points = new Point[n];
        for (int i = 0; i < n; i++) {
            String[] coordinates = fin.nextLine().split(" ");
            int x = Integer.parseInt(coordinates[0]);
            int y = Integer.parseInt(coordinates[1]);
            points[i] = new Point(x, y);
        }

        double[][] adjacency_matrix = new double[n][n];
        for (int i = 0; i < n; i++) {
            String line = fin.nextLine();
            for (int j = 0; j < n; j++) {
                if (i == j)
                    adjacency_matrix[i][j] = 0;
                else if (line.charAt(j) == '1')
                    adjacency_matrix[i][j] = computeDistance(points[i], points[j]);
                else
                    adjacency_matrix[i][j] = Double.POSITIVE_INFINITY;
            }
        }

        int[] component = new int[n];
        int compNumber = 1;

        for (int i = 0; i < n; i++) {
            if (component[i] == 0) {
                dfs(i, adjacency_matrix, component, compNumber);
                compNumber++;
            }
        }

        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++) {
                    if (component[i] == component[j] && component[i] == component[k]
                      && component[j] == component[k])
                    adjacency_matrix[i][j] = Math.min(adjacency_matrix[i][j], adjacency_matrix[i][k] + adjacency_matrix[k][j]);
                }
        }

        double[] maxDiameter = new double[compNumber];
        double[] farthestPoint = new double[n];

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (component[i] == component[j]) {
                    double dist = adjacency_matrix[i][j];
                    maxDiameter[component[i]] = Math.max(maxDiameter[component[i]], dist);
                    farthestPoint[i] = Math.max(farthestPoint[i], dist);
                    farthestPoint[j] = Math.max(farthestPoint[j], dist);
                }
            }
        }

        double minDiameter = Double.POSITIVE_INFINITY;

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (component[i] != component[j]) {
                    double diameter =
                      computeDistance(points[i], points[j]) + farthestPoint[i] + farthestPoint[j];
                    diameter = Math.max(diameter, Math.max(maxDiameter[component[i]], maxDiameter[component[j]]));
                    minDiameter = Math.min(minDiameter, diameter);
                }
            }
        }

        fout.printf("%.6f\n", minDiameter);
        fout.close();
    }

    static void dfs(int node, double[][] adjacency_matrix, int[] component, int compNumber) {
        if (component[node] != 0)
            return;
        component[node] = compNumber;
        for (int i = 0; i < adjacency_matrix[node].length; i++) {
            if (adjacency_matrix[node][i] != Double.POSITIVE_INFINITY && component[i] == 0)
                dfs(i, adjacency_matrix, component, compNumber);
        }
    }

    static double computeDistance(Point p1, Point p2) {
        return Math.sqrt(Math.pow(p1.x - p2.x, 2) + Math.pow(p1.y - p2.y, 2));
    }
}
