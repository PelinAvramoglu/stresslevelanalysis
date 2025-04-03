# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 21:51:43 2025

@author: Huaweı
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

# 1. Veri Setini Yükle
df = pd.read_excel('stresslevel.xlsx')

# 2. Sayısal verilere dönüşüm (hata durumunda NaN olmaması için)
df[['SleepDuration', 'StudyDuration', 'StressLevelIncrease', 'DaysUntilExam']] = df[
    ['SleepDuration', 'StudyDuration', 'StressLevelIncrease', 'DaysUntilExam']
].apply(pd.to_numeric, errors='coerce')

# 3. Histogramlar - Değişken Dağılımı
plt.figure(figsize=(12, 6))
for i, column in enumerate(['SleepDuration', 'StudyDuration', 'StressLevelIncrease', 'DaysUntilExam']):
    plt.subplot(2, 2, i+1)
    sns.histplot(df[column], bins=15, kde=True, color='steelblue')
    plt.title(f'{column} Distribution')
plt.tight_layout()
plt.show()

# 4. Boxplot Analizi - Aykırı değerleri belirleme
plt.figure(figsize=(12, 6))
for i, column in enumerate(['SleepDuration', 'StudyDuration', 'StressLevelIncrease', 'DaysUntilExam']):
    plt.subplot(2, 2, i+1)
    sns.boxplot(y=df[column], color='lightcoral')
    plt.title(f'{column} Boxplot')
plt.tight_layout()
plt.show()

# 5. Scatterplot + Trendline (Regresyon Çizgisi)
plt.figure(figsize=(12, 6))
sns.pairplot(df[['SleepDuration', 'StudyDuration', 'StressLevelIncrease', 'DaysUntilExam']], kind='reg', diag_kind='kde')
plt.show()

# 6. Korelasyon Matrisi (Heatmap)
plt.figure(figsize=(8, 6))
correlation_matrix = df[['SleepDuration', 'StudyDuration', 'StressLevelIncrease', 'DaysUntilExam']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix')
plt.show()

# 7. Regresyon Analizi - Stres Seviyesi Artışını Tahmin Etme
X = df[['SleepDuration', 'StudyDuration', 'DaysUntilExam']]
X = sm.add_constant(X)  # Sabit terimi ekle
y = df['StressLevelIncrease']

model = sm.OLS(y, X).fit()  # Modeli eğit
print(model.summary())  # Regresyon analizini yazdır

# 8. Scatter Plot (Sleep Duration vs. Stress Level Increase)
plt.figure(figsize=(6, 4))
sns.regplot(x=df['SleepDuration'], y=df['StressLevelIncrease'], scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
plt.title('Sleep Duration vs. Stress Level Increase')
plt.xlabel('Sleep Duration (hours)')
plt.ylabel('Stress Level Increase')
plt.show()

# 9. Scatter Plot (Study Duration vs. Stress Level Increase)
plt.figure(figsize=(6, 4))
sns.regplot(x=df['StudyDuration'], y=df['StressLevelIncrease'], scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
plt.title('Study Duration vs. Stress Level Increase')
plt.xlabel('Study Duration (hours)')
plt.ylabel('Stress Level Increase')
plt.show()
