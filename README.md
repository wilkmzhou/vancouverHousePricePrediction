# Predicting House Prices in Vancouver
### Order of tasks to complete for LASSO Regression project
1. Clean and wrangle dataset so it can be used in algorithms
   - Address NA values
   - Check for observation duplicates
   - Rename variables to easy-to-understand names
   - Split dataset 70/30 for training/testing
2. Preliminary Data Exploration
   - Assess if there is multicollinearity
   - Plot the variables to get a general understanding of what each variables 
   do to the house price
3. Put dataset through LASSO algorithm to find coefficients for predictive model
   - Find appropriate shrinking parameter, lambda, for algorithm
   - Turn dataset into a matrix
4. Check for overdispersion of the regression model from LASSO
5. Assess the predictibility of the regression model from LASSO
   - find ROC/AUC 
   - 