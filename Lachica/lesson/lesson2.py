import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

tips = sns.load_dataset("tips")
# print(tips.head())
# sns.histplot(data= tips, x = "total_bill")
# plt.show()

# sns.histplot(data = tips , x = "total_bill", kde= True)
# plt.ylabel("Tip")
# plt.show()

# sns.kdeplot(data=tips, x='total_bill')

# sns.histplot(data=tips, x='total_bill', hue='sex', kde=True)

sns.boxplot(data=tips, x= 'day', y= 'total_bill')

# sns.violinplot(data=tips, x='day', y='total_bill')

# sns.countplot(data=tips, x="day")

# sns.barplot(data=tips, x="day", y="total_bill")

# sns.scatterplot(data=tips, x="total_bill", y="tips")

plt.show()
