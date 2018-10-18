| **Statistical Analyses**	|  **IV(s)**  |  **IV type(s)** |  **DV(s)**  |  **DV type(s)**  |  **Control Var** | **Control Var type**  | **Question to be answered** | **_H0_** | **alpha** | **link to paper**| 
|:----------:|:----------|:------------|:-------------|:-------------|:------------|:------------- |:------------------|:----:|:-------:|:-------|
Correlation	|1, prenatal exposure to maternal tobacco smoking over 12wk | dichotomous| 1, DNA methylation| continuous | 0 | N/A| 	Will there be potential associations between exposure to maternal smoking leading and DNA-Methylation? | Maternal smoking and DNA-Methylation are not correlated | 0.05 | [Maternal Smoking during Pregnancy and DNA-Methylation in Children at Age 5.5 Years: Epigenome-Wide-Analysis in the European Childhood Obesity Project (CHOP)- Study(https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0155554&type=printable) |
  |||||||||

![correlation plot from reference](correlation_screenshot.png)

  
  
| **Statistical Analyses**	|  **IV(s)**  |  **IV type(s)** |  **DV(s)**  |  **DV type(s)**  |  **Control Var** | **Control Var type**  | **Question to be answered** | **_H0_** | **alpha** | **link to paper**| 
|:----------:|:----------|:------------|:-------------|:-------------|:------------|:------------- |:------------------|:----:|:-------:|:-------|
MANCOVA	| 1,Age | ordinal | 1,FIQ | categorical | sex, diagnosis | continuous (could also be categorical) | 	we test if the effect of autism is dependent on sex within each of these cognitive domains: (i) mentalizing and emotion perception, (ii)executive function, (iii) perceptual attention to detail, and (iv) motor function | Ranks test groups <= Ranks control group | 0.05 | [Cognition in Males and Females with Autism: Similarities and Differences](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0047198) |
  |||||||||
  
![MANCOVA](MA.png)

| **Statistical Analyses**	|  **IV(s)**  |  **IV type(s)** |  **DV(s)**  |  **DV type(s)**  |  **Control Var** | **Control Var type**  | **Question to be answered** | **_H0_** | **alpha** | **link to paper**| 
|:----------:|:----------|:------------|:-------------|:-------------|:------------|:------------- |:------------------|:----:|:-------:|:-------|
Logistic Regression	| 1,BMI,liver right lobe | Categorical | 1,diagnosed or not | categorical | 0 | N/A | 	Given some medical parameters and results, test to see and diagnose whether or not a patient is obese. | p(0, 1) != a1*BMI + a2*TA systole + a3*TA diastole + a4*liver right lobe + a5*hilus down + a6*hilus big a7*lung arbrz | 0.05 | [The Classification of Obesity Disease in Logistic Regression and Neural Network Methods](https://link.springer.com/article/10.1007%2Fs10916-008-9165-5#Sec6) |
  |||||||||

![LR](lr.png)
