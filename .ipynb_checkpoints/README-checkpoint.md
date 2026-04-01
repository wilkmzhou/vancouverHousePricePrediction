# Predicting House Prices in Vancouver
### Order of tasks to complete for LASSO Regression project
1. Clean and wrangle dataset so it can be used in algorithms
   - Address NA values ✅
   - Check for observation duplicates ✅
   - Rename variables to easy-to-understand names ✅
   - Split dataset 80/20 for training/testing ✅
2. Preliminary Data Exploration
   - Assess if there is multicollinearity ✅
   - Plot the variables to get a general understanding of what each variables do to the house price ✅
   - Remove redundant variables or variables unimportant in regression ✅
   do to the house price
3. Put dataset through LASSO algorithm to find coefficients for predictive model
   - Find appropriate shrinking parameter, lambda, for algorithm ✅
   - Scale dataset for LASSO regression ✅
   - Convert categorical variables to dummy variables so LASSO algorithm reads them as numerical varibles ✅
4. Repeat process for OLS regression
   - Scale dataset so predictions match those of LASSO regression model ✅
   - Fit the ordinary least squares regression model ✅
6. Assess the metrics of LASSO and OLS regression models
   - compute RMSE ✅
   - compute R-squared and adjusted R-squared ✅