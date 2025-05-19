# The Stress Equation: How Study Time, Sleep, and Exam Pressure Interact
## Objective (Regression): 
Predict post-study stress levels (StressLevelAfter) from study duration, sleep hours, caffeine intake, and days until the exam.



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

#### Feature Engineering

- **StressLevelDifference:** Calculated the difference between stress levels before and after study sessions.
- **Study Time:** Categorized study times based on the proximity to the exam (e.g., Regular Study, Pre-Exam Study).
- **Sleep Quality Indicator:** A binary variable indicating whether sleep duration was at least 7 hours (considered good sleep).

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
## ML (Comparative Analysis Using Regression Techniques such as Linear Regression, kNN, SVM, Random Forest, and Neural Networks)

![image](https://github.com/user-attachments/assets/b55321fc-b239-4042-b94a-90185663c9d6)


The scatter plot presents the performance of the Linear Regression model in predicting post-study stress levels. On the x-axis, actual stress levels range from approximately 6 to 11, while the predicted values on the y-axis span a similar range, indicating that the model is capable of capturing the general scale of the target variable. The red dashed line represents the ideal prediction line where predicted values exactly match actual ones. Most data points lie close to this line, such as one point where the actual stress level is around 7 and the predicted value is approximately 7.8, and another where the actual value is 11, with a predicted value near 10.1. These small deviations indicate the model slightly underestimates stress at higher levels. Nonetheless, the overall distribution of the points around the reference line suggests that the model provides a reasonably accurate fit with no significant outliers or evidence of severe prediction error.

### k-Nearest Neighbors (k-NN) – Actual vs Predicted
![image](https://github.com/user-attachments/assets/c29dbd5d-a4b5-4b91-bf24-7b1d716c5814)


The k-NN model demonstrates a moderately consistent pattern between actual and predicted stress levels. Most points lie near the ideal red dashed line, indicating relatively accurate predictions. However, there are visible deviations, especially at higher actual stress values such as 11, where predicted values drop to approximately 9.5, suggesting an underestimation. Similarly, when the actual value is 7, the model predicts stress slightly above 8, indicating slight overfitting in some low-range cases. Overall, k-NN captures the general trend but exhibits sensitivity to local variations due to its non-parametric nature.


### Support Vector Regression – Actual vs Predicted
![image](https://github.com/user-attachments/assets/bd49b378-90b2-48d5-a7dd-82eeeb5d34e9)

The Support Vector Regression (SVR) model provides a relatively close approximation to actual stress levels, especially at higher values such as 11, where predictions range from 9.8 to 10.2. At lower actual values (e.g., 6 or 7), the model occasionally overpredicts, as seen with predicted values near 8. Despite these minor deviations, the overall distribution of predictions along the ideal reference line suggests that SVR performs well in modeling the stress variable, particularly in the upper-mid range, leveraging its ability to balance complexity and margin optimization.

### Random Forest – Actual vs Predicted
![image](https://github.com/user-attachments/assets/e05447d5-2413-4bf1-8488-77e192b9912d)

The Random Forest model shows strong predictive performance with minimal variance from the actual stress levels. Most data points align closely with the red dashed line, particularly at the extremes, such as actual stress levels of 6 and 11, where the predictions are nearly exact. The model’s ensemble nature helps reduce overfitting and enhances accuracy. For instance, at actual values of 7 and 9, the predicted levels are around 7.2 and 9.1, respectively, indicating a very low prediction error. This suggests that Random Forest is highly effective for this regression task.

### Neural Network – Actual vs Predicted
![image](https://github.com/user-attachments/assets/4baddb9d-87db-43b1-a03d-0b4f587774ef)

The Neural Network model exhibits strong alignment with actual stress levels across the entire range. Data points are consistently positioned close to the diagonal reference line, showing accurate predictions at both low and high ends. For example, when the actual stress is 11, the model predicts approximately 10.9, and for 6, the prediction is around 6.1. This reflects the model's capacity to generalize well from limited data. The small variance in predicted values highlights the neural network’s ability to capture complex, nonlinear relationships within the dataset.

### Model Error Comparison (MAE & RMSE – Lower is Better)
![image](https://github.com/user-attachments/assets/4052e883-f829-4dbf-9c3b-8d05dd755559)
![image](https://github.com/user-attachments/assets/4bbd5c69-2d8f-4f05-add8-10b44b8d6320)

The error metrics, Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE), are crucial indicators of model performance, where lower values signify better accuracy. Among the models, the Neural Network outperforms all others with the lowest MAE of 0.533 and RMSE of 0.622, indicating highly precise predictions. In contrast, k-Nearest Neighbors (MAE: 1.057, RMSE: 1.149) and Support Vector Regression (MAE: 0.977, RMSE: 1.081) show the highest error rates, suggesting poorer generalization. Linear Regression and Random Forest perform comparably, with Random Forest slightly edging out Linear Regression by achieving lower MAE (0.919) and RMSE (0.934) values than Linear Regression (MAE: 0.872, RMSE: 0.918).
### R² Score Comparison (Higher is Better)

The R² score, also known as the coefficient of determination, measures the proportion of variance in the dependent variable that is predictable from the independent variables. A higher R² indicates better model fit. The Neural Network achieves the highest R² score at 0.906, showcasing its superior capacity to explain the variability in stress levels. Linear Regression and Random Forest follow with R² scores of 0.796 and 0.788, respectively, indicating solid performance. Meanwhile, Support Vector Regression (0.717) and k-Nearest Neighbors (0.680) exhibit the weakest fits among the models, highlighting their relative limitations in capturing the underlying patterns in the data.



## Conclusion

By meticulously tracking my study time, sleep duration, and stress levels over a 30 day period, this project aims to uncover the intricate relationship between these factors and how they contribute to academic stress. As exams approach, the pressure to perform intensifies, and understanding how study time and sleep influence stress can lead to actionable insights. Through this analysis, I hope to identify patterns that can optimize my study habits and sleep routines, ultimately reducing stress and fostering a healthier, more effective approach to studying. The findings will not only enhance my personal academic performance but also provide valuable strategies for managing stress during high-pressure academic periods.

