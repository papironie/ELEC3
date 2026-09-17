import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

tips = sns.load_dataset("tips")
print(tips.head())
sns.histplot(data= tips, x = "total_bill")
plt.show()