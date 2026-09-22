import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

tips = sns.load_dataset("tips")
# print(tips.head())
# print()

# pd.set_option("display.max_rows", None)
# pd.set_option("display.max_columns", None)
# tips = sns.load_dataset("tips")
# print(tips)

# sns.histplot(data = tips , x = "total_bill",bins= 20)
# plt.title("Distribution of Total Bills - 8 Bins")
# plt.xlabel("Total Bill")
# plt.ylabel("Frequency")

# sns.kdeplot(data=tips, x = 'total_bill', hue='time', fill=True, common_norm= False)
# plt.title("Distribution of Total Bills: Lunch vs Dinner")
# plt.xlabel("Total Bill")

# sns.histplot(data=tips, x= "total_bill", hue="sex", kde= True)

# sns.histplot(data=tips, x= "total_bill", hue="time", multiple="stack")
# plt.title("Total Bill Distribution by Meal Time")

# sns.boxplot(data=tips, x="day", y="total_bill",)
# plt.title("Total Bill Distribution by Day")
# plt.xlabel("Day")
# plt.ylabel("Total Bill")

# sns.violinplot(data=tips, x="day", y="total_bill", inner="quartile")
# sns.stripplot(data=tips, x="day", y="total_bill", alpha = 0.5 )

# sns.countplot(data=tips, x="day", hue="smoker")
# plt.title("Smoker and Non-Smoker")
# plt.xlabel("Day")
# plt.ylabel("Total Bill")

# sns.barplot(data=tips, x="day", y="total_bill", hue="time")
# plt.title("Average Total Bill by Day and Meal Time")
# plt.xlabel("Day")
# plt.ylabel("Average Total Bill")

# sns.regplot(data=tips, x="total_bill", y="tip")

# sns.pairplot(tips, vars=["total_bill","tip","size"], hue="time")

numeric_data= tips.select_dtypes(include="number")
correlation = numeric_data.corr()
print(correlation)

sns.heatmap(correlation, annot=True)


plt.show()
