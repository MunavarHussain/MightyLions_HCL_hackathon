# MightyLions_HCL_hackathon
<h3>Team : Mighty Lions</h3>
<h3>College:</h3>
Kamaraj College of Engineering and Technology.

<h3>Team:</h3>
1. V.Devaguru (TL)
2. A.R.Munavar Hussain
3. L.Shanmugapriya

<h3>Pre-Project work:</h3>
<h4>Title - </h4>Gender Recognition with voice dataset using Machine Learning/Artificial Intelligence algorithms.

<h4>Objective - </h4>
Our objective, at this stage of the contest, is not to build a complete solution for a real-time problem, but to understand, experiment and learn machine learning and its related algorithms. In this project, we have identified a voice as male or female based on various acoustic properties of the voice and speech. 

<h4>Dataset - </h4>
The dataset 'voicedataset.csv' included, has the following fields mean frequency("meanfreq") ,standard deviation("sd") , median frequency("median") , first quantile("Q25") ,third quantile("Q75") ,interquantile range("IQR") ,skewness("skew") ,kurtosis("kurt") ,spectral entropy("sp.ent") ,spectral flatness("sfm") ,mode frequency("mode") ,frequency centroid ("centroid") ,average of fundamental frequency("meanfun") ,minimum fundamental frequency("minfun") ,maximum fundamental frequency("maxfun") ,average of dominant frequency("meandom") ,minimum of dominant frequency("mindom") ,maximum of dominant frequency("maxdom") ,range of dominant frequency("dfrange") , modulation index("modindx") , "label". Here all fields represent an acoustic property except for the label field. Label denotes the original gender for the particular sample voice. From the csv file of 3168 voice samples with 1584 male and 1584 female data, a set of data (80%) is taken as train data and rest (20%) as the test. 

<h4>Results & Inference - </h4>
Different ML/AI algorithms have been worked out and their results ('ml_grv_results.png') are included in this repository. Additionally, the execution time for each algorithm is calculated and reported. Our Inference from the above is that the decision tree classifier has higher accuracy for this dataset model and we have also included the algorithm ('ml_grv_algo.png') for it. We have worked on five algorithms namely DecisionTree, K-mean, SVM, Naives bayes and logistic regression from which decision_tree ('mh_grv_dtree.py') and k-mean ('mh_grv_kmean.py') are added. 
