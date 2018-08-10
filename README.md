# MightyLions_HCL_hackathon
<h3>Team : Mighty Lions</h3>
<h3>College:</h3>
Kamaraj College of Engineering and Technology.

<h3>Team:</h3>
1. V.Devaguru (TL)
2. A.R.Munavar Hussain
3. L.Shanmugapriya

<h3>Pre-Project work:</h3>
Gender Recognition with voice dataset using Machine Learning/Artificial Intelligence algorithms.

Our objective, at this stage of the contest is not to build a complete solution for a real time problem, but to understand, experiment and learn machine learining and its related algorithms. In this project we have identified a voice as male or female based on various acoustic properties of the voice and speech. The dataset, 'voicedataset.csv' taken from kaggle, has the following fields "meanfreq","sd","median","Q25","Q75","IQR","skew","kurt","sp.ent","sfm","mode","centroid","meanfun","minfun","maxfun","meandom","mindom","maxdom","dfrange","modindx","label". Here all fields represent an acoustic property except for the label field. Label denotes the original gender for the particular sample voice.

A set of data (80%) is taken as train data and rest (20%) as test. Different ML/AI algorithms has been worked out and their results ('ml_grv_results.png') are included in this repository. Our Inference from the above is that the DecisionTreee classifier has higher accuracy for this dataset model and we have also included the algorithm ('ml_grv_algo.png') for it. We have worked on five algorithms namely DecisionTree, K-mean, SVM, Naives bayes and logistic regression from which decision_tree ('mh_grv_dtree.py') and k-mean ('mh_grv_kmean.py') are added. 
