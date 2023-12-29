# -*- coding: utf-8 -*-
"""Mini_Project_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1X1cL4DuOFmKuwCTlPdV7y5cbVuKNb3p8

#Initial SetUp
"""

# Commented out IPython magic to ensure Python compatibility.
# %load_ext rpy2.ipython

# Commented out IPython magic to ensure Python compatibility.
# %reload_ext rpy2.ipython

!pip install rpy2==3.5.1

# Commented out IPython magic to ensure Python compatibility.
# %%R
# customer_data=read.csv("/content/Mall_Customers.csv")

# Commented out IPython magic to ensure Python compatibility.
# %%R
# str(customer_data)

# Commented out IPython magic to ensure Python compatibility.
# %%R
# names(customer_data)

# Commented out IPython magic to ensure Python compatibility.
# %%R
# head(customer_data)

# Commented out IPython magic to ensure Python compatibility.
# %%R
# summary(customer_data $ Age)
# # $ is an extract operator.

# Commented out IPython magic to ensure Python compatibility.
# %%R
# sd(customer_data$Age)
#

# Commented out IPython magic to ensure Python compatibility.
# %%R
# summary(customer_data$Annual.Income..k..)

# Commented out IPython magic to ensure Python compatibility.
# %%R
# sd(customer_data$Annual.Income..k..)

# Commented out IPython magic to ensure Python compatibility.
# %%R
# summary(customer_data$Age)

# Commented out IPython magic to ensure Python compatibility.
# %%R
# sd(customer_data$Spending.Score..1.100.)

# Commented out IPython magic to ensure Python compatibility.
# %%R
# a=table(customer_data$Gender)
# barplot(a,main="Using BarPlot to display Gender Comparision",
#        ylab="Count",
#        xlab="Gender",
#        col=c('green', 'blue'),
#        legend=rownames(a))

# Commented out IPython magic to ensure Python compatibility.
# %%R
# install.packages("plotrix")

# Commented out IPython magic to ensure Python compatibility.
# %%R
# pct=round(a/sum(a)*100)
# lbs=paste(c("Female","Male")," ",pct,"%",sep=" ")
# library(plotrix)
# pie3D(a,labels=lbs,
#    main="Pie Chart Depicting Ratio of Female and Male",
#     col=c('green', 'blue'))
#

"""#VISUALIZATION"""

# Commented out IPython magic to ensure Python compatibility.
# %%R
# summary(customer_data$Age)

# Commented out IPython magic to ensure Python compatibility.
# %%R
# hist(customer_data$Age,
#     col="Blue",
#     main="Histogram to Show Count of Age Class",
#     xlab="Age Class",
#     ylab="Frequency",
#     labels=TRUE)

# Commented out IPython magic to ensure Python compatibility.
# %%R
# boxplot(customer_data$Age,
#        col="yellow",
#        main="Boxplot for Descriptive Analysis of Age")

"""#ANALYSIS

"""

# Commented out IPython magic to ensure Python compatibility.
# %%R
# summary(customer_data$Annual.Income..k..)

# Commented out IPython magic to ensure Python compatibility.
# %%R
# hist(customer_data$Annual.Income..k..,
#   col="cyan",
#   main="Histogram for Annual Income",
#   xlab="Annual Income Class",
#   ylab="Frequency",
#   labels=TRUE)

# Commented out IPython magic to ensure Python compatibility.
# %%R
# plot(density(customer_data$Annual.Income..k..),
#     col="yellow",
#     main="Density Plot for Annual Income",
#     xlab="Annual Income Class",
#     ylab="Density")
# polygon(density(customer_data$Annual.Income..k..),
#         col="#ccff66")

# Commented out IPython magic to ensure Python compatibility.
# %%R
# summary(customer_data$Spending.Score..1.100.)

# Commented out IPython magic to ensure Python compatibility.
# %%R
# boxplot(customer_data$Spending.Score..1.100.,
#    horizontal=TRUE,
#    col="YELLOW",
#    main="BoxPlot for Descriptive Analysis of Spending Score")

# Commented out IPython magic to ensure Python compatibility.
# %%R
# hist(customer_data$Spending.Score..1.100.,
#     main="HistoGram for Spending Score",
#     xlab="Spending Score Class",
#     ylab="Frequency",
#     col="cyan",
#     labels=TRUE)

"""
#K-Means Silhoutte
"""

# Commented out IPython magic to ensure Python compatibility.
# %%R
# install.packages("purrr")

"""**ELBOW** **METHOD**"""

# Commented out IPython magic to ensure Python compatibility.
# %%R
# library(purrr)
# set.seed(123)
# # function to calculate total intra-cluster sum of square
# iss <- function(k) {
#   kmeans(customer_data[,3:5],k,iter.max=100,nstart=100,algorithm="Lloyd" )$tot.withinss
# }
# k.values <- 1:10
# iss_values <- map_dbl(k.values, iss)
# plot(k.values, iss_values,
#     type="b", pch = 19, frame = FALSE,
#     xlab="Number of clusters K",
#     ylab="Total intra-clusters sum of squares")

"""**SILHOUETTE METHOD**"""

# Commented out IPython magic to ensure Python compatibility.
# %%R
# install.packages("gridExtra")

# Commented out IPython magic to ensure Python compatibility.
# %%R
# library(cluster)
# library(gridExtra)
# library(grid)
# 
# k2<- kmeans(customer_data[,3:4],2,iter.max=100,nstart=50,algorithm="Lloyd")
# s2<- plot(silhouette(k2 $ cluster,dist(customer_data[,3:5],"euclidean")))

# Commented out IPython magic to ensure Python compatibility.
# %%R
# k3<-kmeans(customer_data[,3:5],3,iter.max=100,nstart=50,algorithm="Lloyd")
# s3<-plot(silhouette(k3$cluster,dist(customer_data[,3:5],"euclidean")))

# Commented out IPython magic to ensure Python compatibility.
# %%R
# k4<-kmeans(customer_data[,3:5],4,iter.max=100,nstart=50,algorithm="Lloyd")
# s4<-plot(silhouette(k4$cluster,dist(customer_data[,3:5],"euclidean")))

# Commented out IPython magic to ensure Python compatibility.
# %%R
# k5<-kmeans(customer_data[,3:5],5,iter.max=100,nstart=50,algorithm="Lloyd")
# s5<-plot(silhouette(k5$cluster,dist(customer_data[,3:5],"euclidean")))

# Commented out IPython magic to ensure Python compatibility.
# %%R
# k6<-kmeans(customer_data[,3:5],6,iter.max=100,nstart=50,algorithm="Lloyd")
# s6<-plot(silhouette(k6$cluster,dist(customer_data[,3:5],"euclidean")))

# Commented out IPython magic to ensure Python compatibility.
# %%R
# k7<-kmeans(customer_data[,3:5],7,iter.max=100,nstart=50,algorithm="Lloyd")
# s7<-plot(silhouette(k7$cluster,dist(customer_data[,3:5],"euclidean")))

# Commented out IPython magic to ensure Python compatibility.
# %%R
# k8<-kmeans(customer_data[,3:5],8,iter.max=100,nstart=50,algorithm="Lloyd")
# s8<-plot(silhouette(k8$cluster,dist(customer_data[,3:5],"euclidean")))

# Commented out IPython magic to ensure Python compatibility.
# %%R
# k9<-kmeans(customer_data[,3:5],9,iter.max=100,nstart=50,algorithm="Lloyd")
# s9<-plot(silhouette(k9$cluster,dist(customer_data[,3:5],"euclidean")))

# Commented out IPython magic to ensure Python compatibility.
# %%R
# k10<-kmeans(customer_data[,3:5],10,iter.max=100,nstart=50,algorithm="Lloyd")
# s10<-plot(silhouette(k10$cluster,dist(customer_data[,3:5],"euclidean")))

# Commented out IPython magic to ensure Python compatibility.
# %%R
# install.packages("NbClust")

# Commented out IPython magic to ensure Python compatibility.
# %%R
# install.packages("factoextra")

# Commented out IPython magic to ensure Python compatibility.
# %%R
# library(NbClust)
# library(factoextra)
# 
# fviz_nbclust(customer_data[,3:5], kmeans, method = "silhouette")

"""**Gap Statistic Method**"""

# Commented out IPython magic to ensure Python compatibility.
# %%R
# library(NbClust)
# library(factoextra)
# set.seed(125)
# stat_gap <- clusGap(customer_data[,3:5], FUN = kmeans, nstart = 25, K.max = 10, B = 50)
# fviz_gap_stat(stat_gap)

# Commented out IPython magic to ensure Python compatibility.
# %%R
# pcclust=prcomp(customer_data[,3:5],scale=FALSE) #principal component analysis
# summary(pcclust)
# 
# pcclust$rotation[,1:2]

# Commented out IPython magic to ensure Python compatibility.
# %%R
# k6<-kmeans(customer_data[,3:5],6,iter.max=100,nstart=50,algorithm="Lloyd")
# k6

# Commented out IPython magic to ensure Python compatibility.
# %%R
# set.seed(1)
# ggplot(customer_data, aes(x =Annual.Income..k.., y = Spending.Score..1.100.)) +
#   geom_point(stat = "identity", aes(color = as.factor(k6$cluster))) +
#   scale_color_discrete(name=" ",
#               breaks=c("1", "2", "3", "4", "5","6"),
#               labels=c("Cluster 1", "Cluster 2", "Cluster 3", "Cluster 4", "Cluster 5","Cluster 6")) +
#   ggtitle("Segments of Mall Customers", subtitle = "Using K-means Clustering")

# Commented out IPython magic to ensure Python compatibility.
# %%R
# ggplot(customer_data, aes(x =Spending.Score..1.100., y =Age)) +
#   geom_point(stat = "identity", aes(color = as.factor(k6$cluster))) +
#   scale_color_discrete(name=" ",
#                       breaks=c("1", "2", "3", "4", "5","6"),
#                       labels=c("Cluster 1", "Cluster 2", "Cluster 3", "Cluster 4", "Cluster 5","Cluster 6")) +
#   ggtitle("Segments of Mall Customers", subtitle = "Using K-means Clustering")

# Commented out IPython magic to ensure Python compatibility.
# %%R
# kCols=function(vec){cols=rainbow (length (unique (vec)))
# return (cols[as.numeric(as.factor(vec))])}
# 
# digCluster<-k6$cluster; dignm<-as.character(digCluster); # K-means clusters
# 
# plot(pcclust$x[,1:2], col =kCols(digCluster),pch =19,xlab ="K-means",ylab="classes")
# legend("bottomleft",unique(dignm),fill=unique(kCols(digCluster)))