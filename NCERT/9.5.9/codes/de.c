#include <stdio.h>
#include <math.h>
#include <stdlib.h>

// Function to calculate dy/dx
float dy_dx(float x, float y) {
    if (x == 0) {
        return 0.0;
    } else {
        float numerator = -y;
        float denominator = x * log(y / x) - 2 * x;
        
        // Avoid division by zero or any near-zero values in the denominator
        if (fabs(denominator) < 1e-6) {
            return 0.0;
        }
        
        return numerator / denominator;
    }
}

// Function to calculate points using Euler's method and write to file
void points(float x_0, float y_0, float x_end, float h, int steps) {
    FILE *file = fopen("points.dat", "w");  // Open the file to write points
    if (file == NULL) {
        printf("Error opening file.\n");
        exit(1);
    }

    float x_n = x_0;
    float y_n = y_0;
    float x_n1, y_n1;

    for (int i = 0; i < steps; i++) {
        x_n1 = x_n + h;
        y_n1 = y_n + h * dy_dx(x_n, y_n);

        fprintf(file, "%.3f %.3f\n", x_n1, y_n1);  // Write x and y values to file
        x_n = x_n1;
        y_n = y_n1;
    }

    fclose(file);  // Close the file
}

int main() {
    float x_0 = 1.0;
    float y_0 = 1.0;
    float x_end = 5.0;
    float step_size = 0.001;

    // Calculate the number of steps
    int steps = (int)((x_end - x_0) / step_size) + 1;

    // Calculate points and write to file
    points(x_0, y_0, x_end, step_size, steps);

    printf("Points written to points.dat\n");
    return 0;
}
