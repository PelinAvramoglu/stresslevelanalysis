# The Stress Equation: How Study Time, Sleep, and Exam Pressure Interact
## Presentation:
You can access my presentation through the website below: https://pelin-avramoglu-dsa210-term-project.netlify.app/
## Objective: 
The objective of this project is to uncover meaningful patterns among students by clustering them based on variables such as study time, sleep duration, days until exams, and weather conditions. Using the elbow method and PCA-reduced K-means clustering, we identified three distinct student groups, while the model performance summary table highlights the accuracy of various algorithms in predicting individual stress levels.



## Project Idea

Stress, especially in academic settings, is a common reaction to the pressures of exams. I am interested in exploring how study time, sleep duration, and the proximity of exams influence my stress levels. This project will track these factors over 30 days to better understand how they interact and impact my stress, particularly as the exam approaches. By recording my study hours, sleep duration, and perceived stress levels, I aim to uncover patterns and gain insights into how these variables contribute to my overall stress, and how I can better manage them to improve my academic performance and well-being.
## Methodology
### Dataset Description

This dataset will be collected over a 30 day period to analyze the impact of study time, sleep duration, and stress levels leading up to an exam. Each entry represents a daily record of the following variables:

- **Date**: The specific date of data collection.
- **DayOfWeek**: The day of the week, helping to identify any patterns related to specific weekdays or weekends.
- **Route**: Describes the activity for the day. This will indicate whether it’s a study day or a regular non-study day. On study days, it will also show whether it’s regular study or exam preparation.
- **StudyDuration**: The number of hours spent studying on a given day. Study time increases as the exam approaches, with more intensive study on the last few days leading to the exam.
- **StressLevelBefore**: A perceived stress level on a scale of 1 to 10 before studying. A score of 1 means no stress, and 10 means maximum stress.
- **StressLevelAfter**: The perceived stress level on a scale of 1 to 10 after studying. This is recorded to see the change in stress levels due to the study session.
- **StressLevelIncrease**: The increase in stress level, calculated by subtracting `StressLevelBefore` from `StressLevelAfter`. This variable helps to understand how studying impacts stress levels.
- **SleepDuration**: The number of hours of sleep I had the night before the study day. This will help evaluate if sleep influences stress levels.
- **DaysUntilExam**: The number of days remaining until the next exam. This will dynamically change and influence study time and stress.
- **IsExamDay**: A binary indicator (Yes/No) showing if the day is an exam day. This is crucial for understanding how stress and study time are impacted on exam days.
- **CaffeineIntake: Estimated caffeine intake (cups/day) based on the type of day (higher for exam prep and exam days, lower for rest days).




### Data Analysis

1. **Correlation Analysis**: I will use Pearson’s correlation coefficient to evaluate the relationship between study duration, sleep duration, and stress levels.
2. **Trend Analysis**: Using time series analysis, I will look for patterns in stress levels in relation to study duration and sleep over time, especially in the days leading to the exam.
3. **Regression Model**: I will apply a multiple regression model where stress levels (before and after studying) are the dependent variables, and study duration, sleep duration, and days until the exam are the independent variables.
4. **Statistical Tests**: I will perform t-tests and ANOVA to analyze if the differences in stress levels are statistically significant based on study time and sleep duration.

### Expected Outcomes

1. **Study Duration and Stress**: I expect to see an increase in stress levels as study time increases, particularly in the last few days before the exam.
2. **Sleep Duration and Stress**: Better sleep should correlate with lower stress levels, especially on intense study days.
3. **Days Until Exam**: Stress levels are expected to be higher as the exam approaches. Even if study time increases, stress will likely rise unless sleep quality is maintained.

## Hypothesis
- **Null Hypothesis (H₀):** There is no significant relationship between study duration, sleep duration, and stress levels. Stress levels remain consistent regardless of changes in study time and sleep patterns.
- **Alternative Hypothesis (H₁):**  Study duration, sleep duration, and proximity to exams significantly impact stress levels. Increased study time and reduced sleep are associated with higher stress levels, especially as the exam approaches.
### Hypothesis Testing Results

In this study, various hypothesis tests were conducted to examine the relationships between stress levels and different factors such as exam days, sleep duration, and study duration. The Mann-Whitney U Test revealed a significant difference in stress levels between exam and non-exam days (U = 20.000, p = 0.014453), indicating that stress increases significantly on exam days. The Kruskal-Wallis Test (H = 15.453, p = 0.001407) showed a significant variation in stress levels across different study routes. Both Spearman and Pearson correlation analyses demonstrated strong and significant negative correlations between sleep duration and stress increase (Spearman ρ = -0.915, Pearson r = -0.901, p < 0.0001), and between study duration and stress increase (Spearman ρ = -0.884, Pearson r = -0.90, p < 0.0001), suggesting that higher sleep and study durations are associated with lower stress levels. These findings highlight the critical role of time management and adequate rest in managing stress, particularly around exam periods.

## Methods

### Data Collection
I will collect my data as follows: I will retrieve my stress levels from the Samsung Health Monitor app through my smartwatch. My study times will be pulled from the timer I have installed on my computer. Sleep duration will be obtained from the Samsung Health app. As for the days until my exams, I will manually enter them based on my exam schedule. And Caffeine Intake is taken from Starbucks or Coffy app via APIs to estimate the number of cups consumed per day.

Throughout the 30-day tracking period, data was collected using the following methods:

- **Study Time:** Recorded manually based on the amount of time spent studying each day.
- **Stress Levels:** Self-reported using Samsung Health Monitor app before and after each study session.
- **Sleep Duration:** The number of hours slept each night was tracked using the Samsung Health app, ensuring accurate and consistent data collection.
- **Days Until Exam:** The number of days remaining until the next exam was calculated and recorded each day.
- **Caffeine Intake: Taken from Starbucks or Coffy app via APIs to estimate the number of cups consumed per day.





### Data Processing


#### Data Transformation  

To better capture the effect of exam proximity, we categorized `DaysUntilExam` into a new feature called **`ExamPhase`**, which groups days into distinct intervals based on how close the exam is:

| DaysUntilExam | ExamPhase |
|---------------|-----------|
| ≥ 7 days      | Far       |
| 3–6 days      | Near      |
| ≤ 2 days      | Imminent  |


#### Data Cleaning

- Converted date and time data into appropriate formats for analysis.
- Removed any missing or inconsistent data.


### Visualization Techniques

#### Univariate Analysis

- Histogram for **Study Duration** distribution.
- Histogram for **Sleep Duration** distribution.
- Histogram for **Stress Levels** before and after study sessions.

#### Bivariate Analysis

- **Scatter plot** to analyze the relationship between **Study Duration** and **StressLevelDifference**.
- **Scatter plot** to analyze the relationship between **Sleep Duration** and **StressLevelBefore**.

#### Multivariate Analysis

- Line plot to observe trends in **Stress Level** before and after study over time, particularly as exams approach.
- Bar plots to explore the relationship between **Days Until Exam** and **Stress Levels**.
- Correlation heatmap to analyze the relationships between study time, sleep duration, and stress levels.

### Machine Learning Models

#### Regression Models:

- **Linear Regression:** To assess the linear relationship between study time, sleep duration, and stress levels.
- **Decision Tree:** To identify key factors influencing stress levels before and after study sessions.

#### Statistical Tests

- **T-tests** and **ANOVA:** To evaluate the statistical significance of differences in stress levels based on study time and sleep duration.
  
## Results and Graph Interpretations
### Individual Boxplots and Histograms
![image](https://github.com/user-attachments/assets/7256fe42-5a08-4f85-8775-3f7cd6a6670d)
![image](https://github.com/user-attachments/assets/177b50d8-4a99-489a-97ce-be748342bedf)
1. Sleep Duration
Most sleep durations range from 5 to 8 hours, with the median around 6.5 hours. A few nights fall below 5 hours or above 8.5 hours, but no extreme outliers.

2. Study Duration
Study times mostly range from 3 to 6 hours, with the median slightly above 5 hours. Some days are shorter, but there are no extremely long study sessions.

3. Stress Level Increase
Stress increases are mostly between 0–2 points, with a few reaching 3–5 points. Large stress jumps are rare but occur closer to exams.

4. Days Until Exam
The data shows exams are typically 4 to 6 days away, with the median around 5 days. Only one observation was within 1–2 days before the exam.
### Pairwise Scatterplots and Trendline Relationships

![image](https://github.com/user-attachments/assets/049ab568-ea62-4350-abfb-a743d8e1c262)

The marginal distributions along the diagonal reveal that most days cluster around 5–8 hours of sleep, 2–6 hours of study, a modest stress increase (around 1–4 points), and exams occurring roughly 2–8 days out. Sleep duration appears approximately normally distributed, study time is slightly right-skewed (with a few very intensive study days), stress increase is left-skewed (large stress jumps are rare), and days until exam are roughly symmetric within the observed range.

Looking at the off-diagonal scatterplots with fitted trend lines, several clear patterns emerge. First, there is a strong positive association between sleep and study duration—days with more sleep also tend to be days of longer study, perhaps reflecting more balanced or productive routines. Second, sleep and stress increase are strongly negatively correlated: as sleep hours go up, the rise in stress levels drops, suggesting adequate rest buffers against exam-related anxiety. Third, sleep also shows a moderate positive link with days until exam: you tend to sleep more when the exam is still several days away and perhaps you’re less pressured. Study duration itself is negatively related to stress increase (longer study sessions coincide with smaller stress jumps) and positively related to days until exam (you study more when you still have time). Finally, stress increase and days until exam share a strong negative relationship: the closer you get to the exam date, the sharper the spike in stress. Altogether, these relationships paint a consistent picture of how rest, work, and looming deadlines interact to shape your stress levels.

### Heatmap
![image](https://github.com/user-attachments/assets/fa4760a6-5d58-4fb4-b889-0e8d7ca65a5f)
This correlation matrix highlights the relationships between four variables: SleepDuration, StudyDuration, StressLevelIncrease, and DaysUntilExam. There is a strong positive correlation (0.9) between SleepDuration and StudyDuration, suggesting that students who sleep more also tend to study more. Both of these variables show a strong negative correlation with StressLevelIncrease (-0.9 for SleepDuration and -0.99 for StudyDuration), meaning that increased sleep and study time are associated with lower stress levels — likely indicating healthier study habits. DaysUntilExam is positively correlated with both SleepDuration (0.72) and StudyDuration (0.77), implying that when exams are far away, students sleep and study more. As exams approach, however, StressLevelIncrease shows a negative correlation with DaysUntilExam (-0.79), suggesting that stress rises as the number of days until the exam decreases. This pattern reflects a common academic scenario where looming deadlines increase anxiety and reduce healthy habits like sleep.
# ML (Comparative Analysis Using Regression Techniques such as kNN, SVM, Random Forest, and Neural Networks)
##  Purpose of the Models and Visualizations
n this project, various machine learning models and visualizations were used to explore and understand the relationships between daily habits and stress levels during an academic exam period. Each model and graph served a specific purpose in the analysis:

Random Forest: This model was used to identify the most influential features affecting stress. The resulting feature importance graph highlighted that "Route" (how the day was spent) and "Caffeine Intake" had the greatest impact, while variables such as "IsExamDay" and "DayOfWeek" were less significant.

Neural Network: The training and validation loss graph from the neural network model was used to monitor the model’s learning progress over time. The consistent decrease in both losses indicated that the model learned effectively and generalized well without overfitting.

Support Vector Regression (SVR): This model was applied to predict stress levels based on features like sleep duration, study time, caffeine intake, and exam proximity. The comparison between actual and predicted values helped evaluate how accurately the model captured stress trends.

Elbow Method: This technique was used to determine the optimal number of clusters for unsupervised learning. The elbow in the graph at k=3 suggested that grouping the data into three clusters would be most effective and meaningful.

K-Means Clustering Result: After determining the number of clusters, K-Means was applied to group similar behavior patterns. The clusters, visualized using PCA, revealed different student profiles—such as those experiencing high stress near exams, or those with balanced routines and lower stress.

![image](https://github.com/user-attachments/assets/ed70d4cc-81b6-412c-97bb-efbde8948b83)

According to the results, the Neural Network model outperformed the others with the lowest error rates (MAE: 0.533, RMSE: 0.622) and the highest accuracy (R²: 0.906), indicating a strong ability to predict stress levels on the test data. Among the remaining models, Random Forest also showed solid performance with an R² of 0.788, though with slightly higher errors. Support Vector Regression and k-Nearest Neighbors performed less accurately in comparison. Overall, the results suggest that the Neural Network model is the most effective for this particular regression task.
#### Random forest
![image](https://github.com/user-attachments/assets/9bab5132-b821-4628-9d7d-7ceb5f73f174)
According to the results from the Random Forest model, the two most influential factors affecting my stress levels are “Route” (where I spend my day) and “CaffeineIntake.” This suggests that both my environment and how much caffeine I consume play a key role in how stressed I feel. On the other hand, features like “IsExamDay,” “ExamPhase,” and “DayOfWeek” seem to have very little impact. “SleepDuration” and “DaysUntilExam” showed a moderate influence, indicating that rest and the anticipation of upcoming exams still matter, but perhaps not as much as daily habits and surroundings. Overall, the findings highlight how my everyday routines and lifestyle choices contribute significantly to my stress levels.
#### Neural Network
![image](https://github.com/user-attachments/assets/6fc80733-fff7-45a4-a291-7c63d0dc10a2)
The graph shows a steady decline in both training and validation loss over 100 epochs, which indicates that the neural network is learning effectively from the data. The fact that the validation loss decreases almost in parallel with the training loss suggests that the model is generalizing well and not overfitting. The gap between the two curves remains small, further confirming that the performance on unseen data closely follows the training performance. Overall, the model appears to be improving its predictions consistently across epochs, which is a strong indication of a successful training process.

#### Support Vector 
![image](https://github.com/user-attachments/assets/d25949c8-6aa6-403a-ad13-ce6633bf594f)

This plot shows how well the SVR model captures the relationship between various factors and stress levels. The model predicts stress based on features such as sleep duration, study time, days until an exam, and caffeine intake. The predicted values suggest that the model understands general patterns—like higher stress levels possibly being linked to less sleep, more caffeine, or approaching exam days. However, the slight differences between actual and predicted values indicate that the model may not fully capture sudden changes in stress caused by more complex or personal factors. Still, it reflects a meaningful connection between the input data and stress level trends.


#### Elbow Method
![image](https://github.com/user-attachments/assets/7ca5ac43-96f6-48ea-b736-fee8c6b5cd0d)
The Elbow Method was used to determine the optimal number of clusters based on the features: study time, sleep duration, days until exam, and weather conditions. The Within-Cluster Sum of Squares (WCSS) decreased rapidly until 
k=3, after which the rate of improvement slowed noticeably—forming an "elbow" in the graph. This indicates that using three clusters is optimal, as it balances compact grouping with model simplicity. In this context, the three clusters likely represent students experiencing different patterns of academic workload and external stress factors, such as approaching exams and varying sleep or weather conditions.
#### K-Means Clustering Result:
![image](https://github.com/user-attachments/assets/8db96cda-58e4-4a47-b6d2-f0a21143a386)

K-Means clustering was applied using the variables: study time, sleep duration, days until exam, and weather, with the results visualized in two dimensions using PCA for clarity. The plot clearly shows three distinct clusters, suggesting that the data naturally groups into three behavioral or situational profiles. For instance, one cluster might consist of students with high study time and low stress due to more days until their exams, while another may include those with poor sleep and high stress nearing exam days. This clustering provides meaningful insights into how daily routines and environmental factors correlate with stress levels, which can help in developing personalized support strategies.
## Conclusion

By meticulously tracking my study time, sleep duration, and stress levels over a 30 day period, this project aims to uncover the intricate relationship between these factors and how they contribute to academic stress. As exams approach, the pressure to perform intensifies, and understanding how study time and sleep influence stress can lead to actionable insights. Through this analysis, I hope to identify patterns that can optimize my study habits and sleep routines, ultimately reducing stress and fostering a healthier, more effective approach to studying. The findings will not only enhance my personal academic performance but also provide valuable strategies for managing stress during high-pressure academic periods.

