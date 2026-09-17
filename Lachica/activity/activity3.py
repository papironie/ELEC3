import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

tips = sns.load_dataset("tips")
print(tips.head())

sns.scatterplot(data=tips, x="total_bill", y="tip")

plt.ylabel("Tip")
plt.xlabel("Total Bill")
plt.title("Tips per Total Bill")
plt.show()