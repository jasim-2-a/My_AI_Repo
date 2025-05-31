import statistics
import scipy.stats
import numpy as np

def display_menu():
    print("\nStatistical Operations Menu:")
    print("1. Mean")
    print("2. Median")
    print("3. Mode")
    print("4. Variance")
    print("5. Standard Deviation")
    print("6. Skewness")
    print("7. Kurtosis")
    print("8. Z-score")
    print("9. Percentile")
    print("10. Quartiles")
    print("11. Correlation Coefficient (for 2 variables)")
    print("12. Exit")


data_str1 = input("Enter data for variable 1 (space-separated numbers): ")
data_list1 = [float(x) for x in data_str1.str]


data_list2 = []
second_data = input("Do you want to enter a second variable for correlation? (y/n): ").lower()
if second_data == 'y':
    data_str2 = input("Enter data for variable 2 (space-separated numbers): ")
    data_list2 = [float(x) for x in data_str2.strip().split()]
 

while True:
    display_menu()
    choice = input("Choose an operation (1-12): ")

    try:
        if choice == '1':
            print(f"Mean: {round(statistics.mean(data_list1), 2)}")

        elif choice == '2':
            print(f"Median: {round(statistics.median(data_list1), 2)}")

        elif choice == '3':
            try:
                mode = statistics.mode(data_list1)
            except statistics.StatisticsError:
                mode = statistics.multimode(data_list1)
            print(f"Mode: {mode}")

        elif choice == '4':
            print(f"Variance: {round(statistics.variance(data_list1), 2)}")

        elif choice == '5':
            print(f"Standard Deviation: {round(statistics.stdev(data_list1), 2)}")

        elif choice == '6':
            print(f"Skewness: {round(scipy.stats.skew(data_list1), 2)}")

        elif choice == '7':
            print(f"Kurtosis: {round(scipy.stats.kurtosis(data_list1), 2)}")

        elif choice == '8':
            z_scores = scipy.stats.zscore(data_list1)
            print(f"Z-scores: {[round(z, 2) for z in z_scores]}")

        elif choice == '9':
            p = float(input("Enter the percentile you want (e.g., 25, 50, 90): "))
            percentile_val = np.percentile(data_list1, p)
            print(f"{p}th Percentile: {round(percentile_val, 2)}")

        elif choice == '10':
            q = np.percentile(data_list1, [25, 50, 75])
            print(f"Quartiles: 25th = {round(q[0], 2)}, 50th = {round(q[1], 2)}, 75th = {round(q[2], 2)}")

        elif choice == '11':
            if len(data_list2) != len(data_list1):
                print("Error: Both variables must have the same number of data points.")
            elif len(data_list2) == 0:
                print("Second variable is not provided.")
            else:
                corr_matrix = np.corrcoef(data_list1, data_list2)
                print("Correlation Coefficient Matrix:")
                print(corr_matrix.round(2))
                print(f"Correlation Coefficient between the variables: {round(corr_matrix[0,1], 2)}")

        elif choice == '12':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 12.")

    except Exception as e:
        print(f"An error occurred: {e}")
