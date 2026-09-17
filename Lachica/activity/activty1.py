import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('combined_enrollment.csv')

dataset = data.iloc[:50, :7]
print(dataset)

rows = dataset.index

plt.plot(rows, dataset['Enrollment'], marker='o')
plt.title("Enrollment per row")
plt.xlabel("Row")
plt.ylabel("Enrollment")
plt.show()

plt.bar(rows, dataset['Enrollment'])
plt.title("Enrollment per row")
plt.xlabel("Row")
plt.ylabel("Enrollment")
plt.show()

plt.barh(dataset.index[:15].astype(str), dataset['Enrollment'].iloc[:15])
plt.title("Horizontal bar")
plt.show()

genderCount = dataset['Gender'].value_counts()
plt.pie(genderCount, labels=genderCount.index.astype(str))
plt.title("Gender Distribution")
plt.show()

gradeCount = dataset['Grade/Strand'].value_counts()
explode = [0.1] * len(gradeCount)
plt.pie(gradeCount, labels=gradeCount.index.astype(str), explode=explode)
plt.title("Grade/Strand distribution")
plt.show()

plt.scatter(rows, dataset['Enrollment'])
plt.title("Row vs Enrollment")
plt.xlabel("Row")
plt.ylabel("Enrollment")
plt.show()

plt.hist(dataset['Enrollment'], bins=10)
plt.title("Enrollment Distribution")
plt.xlabel("Enrollment")
plt.ylabel("Frequency")
plt.show()

plt.fill_between(range(len(dataset)), dataset['Enrollment'], alpha=0.6)
plt.plot(range(len(dataset)), dataset['Enrollment'])
plt.title("Enrollment area chart")
plt.xlabel("Row")
plt.ylabel("Enrollment")
plt.show()

# split the existing Gender column into 3 series for the stacked area
# (these are just temporary variables, not new columns in dataset)
male = (dataset['Gender'] == 'Male').astype(int)
female = (dataset['Gender'] == 'Female').astype(int)
total = (dataset['Gender'] == 'Total').astype(int)

plt.stackplot(range(len(dataset)), male, female, total,
              labels=['Male', 'Female', 'Total'])
plt.title("Stacked Area: Gender per row")
plt.xlabel("Row")
plt.ylabel("Value")
plt.legend(loc='upper left')
plt.show()