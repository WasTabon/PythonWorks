--1
SELECT DISTINCT R.RecipeTitle 
FROM Recipes AS R
JOIN Recipe_Ingredients AS RI ON R.RecipeID = RI.RecipeID
JOIN Ingredients AS I ON RI.IngredientID = I.IngredientID
JOIN Ingredient_Classes AS IC ON I.IngredientClassID = IC.IngredientClassID
WHERE LOWER(IC.IngredientClassDescription) NOT LIKE '%seafood%';

--3
SELECT DISTINCT R.Preparation 
FROM Recipes AS R
JOIN Recipe_Classes AS RC ON R.RecipeClassID = RC.RecipeClassID
WHERE RC.RecipeClassID = 4;

--4
SELECT R.Preparation 
FROM Recipes AS R
WHERE LOWER(R.Preparation) LIKE '%pudding%';

--5
SELECT DISTINCT R.RecipeTitle 
FROM Recipes AS R
JOIN Recipe_Ingredients AS RI ON R.RecipeID = RI.RecipeID
JOIN Ingredients AS I ON RI.IngredientID = I.IngredientID
JOIN Measurements AS M ON RI.MeasureAmountID = M.MeasureAmountID
WHERE I.IngredientName = N'salt' AND RI.Amount <= 1;

--6
SELECT I.IngredientName,
       RI.Amount,
       M.MeasurementDescription
FROM Recipe_Ingredients AS RI
JOIN Ingredients AS I ON RI.IngredientID = I.IngredientID
JOIN Measurements AS M ON RI.MeasureAmountID = M.MeasureAmountID
WHERE RI.RecipeID = 7;
