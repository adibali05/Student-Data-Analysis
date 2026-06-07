import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# CSV file ko load karein
df = pd.read_csv("student_performance_dataset.csv")

# Dekhein ki data sahi se load hua ya nahi (pehli 5 rows dikhayega)
print("--- Dataset ki shuruati rows ---")
print(df.head())
# --- Is code ko line 11 ke neeche lagayein ---

# 1. Ek figure window create karein jisme dono graphs aayenge
plt.figure(figsize=(12, 5))

# 2. Pehla Graph: Bar Graph (Gender vs Average Final Grade)
plt.subplot(1, 2, 1) # 1 row, 2 columns, pehla plot
sns.barplot(data=df, x="Gender", y="Final_Grade", palette="Set2")
plt.title("Gender vs Average Final Grade")

# 3. Doosra Graph: Scatter Plot ya Trend Line (Attendance vs Final Grade)
plt.subplot(1, 2, 2) # 1 row, 2 columns, doosra plot
sns.regplot(data=df, x="Attendance_Rate", y="Final_Grade", scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
plt.title("Attendance Rate vs Final Grade")

# 4. Layout set karein aur graphs ko screen par show karein
plt.tight_layout()
plt.show()  # Yeh line likhna sabse zaroori hai graph window kholne ke liye!