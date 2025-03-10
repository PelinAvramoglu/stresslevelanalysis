# The Stress Equation: How Study Time, Sleep, and Exam Pressure Interact

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


## Methods

### Data Collection

Throughout the 30-day tracking period, data was collected using the following methods:

- **Study Time:** Recorded manually based on the amount of time spent studying each day.
- **Stress Levels:** Self-reported using Samsung Health Monitor app before and after each study session.
- **Sleep Duration:** The number of hours slept each night was tracked using the Samsung Health app, ensuring accurate and consistent data collection.
- **Days Until Exam:** The number of days remaining until the next exam was calculated and recorded each day.



### Data Processing

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


## Conclusion

By meticulously tracking my study time, sleep duration, and stress levels over a 30 day period, this project aims to uncover the intricate relationship between these factors and how they contribute to academic stress. As exams approach, the pressure to perform intensifies, and understanding how study time and sleep influence stress can lead to actionable insights. Through this analysis, I hope to identify patterns that can optimize my study habits and sleep routines, ultimately reducing stress and fostering a healthier, more effective approach to studying. The findings will not only enhance my personal academic performance but also provide valuable strategies for managing stress during high-pressure academic periods.

