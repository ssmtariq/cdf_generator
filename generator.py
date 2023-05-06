import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

## Author: ssmtariq
## Copyright: Copyright 2023

# Load data from .txt files
data1 = np.loadtxt('data1.txt')
data2 = np.loadtxt('data2.txt')

# Fit kernel density estimates
kde1 = sns.kdeplot(data1, cumulative=True, linewidth=9, label='Data 1', color='red')
kde2 = sns.kdeplot(data2, cumulative=True, linewidth=9, label='Data 2', color='green')

######### Option-1: Add vertical & horizontal line without data label ############
# Compute 99th percentile
percentile_99_data1 = np.percentile(data1, 99)
percentile_99_data2 = np.percentile(data2, 99)

# Add vertical lines for 99th percentile
plt.axvline(percentile_99_data1, color='red', linestyle='--', linewidth=6)
plt.axvline(percentile_99_data2, color='green', linestyle='--', linewidth=6)

# Add horizontal lines for 99th percentile
plt.axhline(0.99, color='red', linestyle='--', linewidth=6)
plt.axhline(0.99, color='green', linestyle='--', linewidth=6)
############################ Option-1 End ####################################

######### Option-2: Add 95th percentile data label on horizontal line ############
# # Compute and plot 95th percentile for data 1
# pct95_1 = np.percentile(data1, 95)
# plt.axhline(y=0.95, linestyle='--', color='red', linewidth=2)
# plt.axvline(x=pct95_1, linestyle='--', color='red', linewidth=2)
# plt.text(pct95_1 + 2, 0.95, f'{pct95_1:.2f} ms', fontsize=14, color='red')
#
# # Compute and plot 95th percentile for data 2
# pct95_2 = np.percentile(data2, 95)
# plt.axhline(y=0.95, linestyle='--', color='green', linewidth=2)
# plt.axvline(x=pct95_2, linestyle='--', color='green', linewidth=2)
# plt.text(pct95_2 + 2, 0.95, f'{pct95_2:.2f} ms', fontsize=14, color='green')
############################ Option-2 End ####################################

######### Option-3: Add 95th percentile data label on vertical line ############
# # Calculate 95th percentile values for both data sets
# pct_95_data1 = np.percentile(data1, 95)
# pct_95_data2 = np.percentile(data2, 95)
#
# # Add vertical line for 95th percentile of Data 1
# plt.axvline(pct_95_data1, color='red', linestyle='--', linewidth=2)
# plt.text(pct_95_data1, 0.5, f"{pct_95_data1:.2f}", fontsize=14, color='red')
#
# # Add vertical line for 95th percentile of Data 2
# plt.axvline(pct_95_data2, color='green', linestyle='--', linewidth=2)
# plt.text(pct_95_data2, 0.5, f"{pct_95_data2:.2f}", fontsize=14, color='green')
#
# # Add horizontal line for 95th percentile
# plt.axhline(0.95, color='black', linestyle='--', linewidth=2)
############################ Option-3 End ####################################


# Add labels and title
plt.xlabel('Latency(ms)', fontsize=48, labelpad=20)
plt.ylabel('CDF', fontsize=48, labelpad=10)
plt.title('Thingsboard', fontsize=52, pad=20)

# Add some space before xlabel
plt.subplots_adjust(bottom=0.16)

# Set custom legend colors
legend_handles = [Line2D([0], [0], color='red', linewidth=9),
                  Line2D([0], [0], color='green', linewidth=9)]
plt.legend(legend_handles, ['Original Code', 'Optimized Code'], fontsize=36, loc='lower right')

# Increase x and y tick label font size
plt.tick_params(axis='x', labelsize=36)
plt.tick_params(axis='y', labelsize=36)

# Display the plot
plt.show()
