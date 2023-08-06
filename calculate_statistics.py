import numpy as np
from pathlib import Path

#read file as np array
file_path = Path(input("Provide file path: "))
numbers = np.loadtxt(file_path, dtype=np.uint8, delimiter=",")

#calculate mean, standard deviation, standard error 
mean = np.mean(numbers)
std_dev = np.std(numbers, ddof=1)
std_err = std_dev / np.sqrt(len(numbers))

#Find scores above one standard deviation from the average
above_avg = numbers[numbers > (mean + std_dev)]

#Find frequency of each number
frequencies = {score:np.count_nonzero(numbers==score) for score in set(numbers) }

#Find the most frequent number
max_frequency = max(frequencies.values())

#Generate ASCII table
x_axis_labels = np.unique(numbers)
ASCII_table = ""
for y in range(max_frequency, 0, -1):
    line = f"{y:2d} "
    
    for score in x_axis_labels:
        frequency = frequencies[score]
        if frequency >=y:
            line += "^" if score in above_avg else "*"
        else:
            line += " "
        line+=int(np.floor(1+np.log10(score))) * " "
    ASCII_table += line + "\n"
#Label x axis
x_labels = "  " + " ".join(x_axis_labels.astype(str))
ASCII_table += x_labels


#Print the results
print("Mean: ", mean)
print("Standard Deviation:", std_dev)
print("Standard Error:", std_err)
print("Scores above one standard deviation:", above_avg)

print(ASCII_table)