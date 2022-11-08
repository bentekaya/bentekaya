
table(data$thal)
round(prop.table(table(data$thal)), 4)*100

# Variable target
table(data$target)
round(prop.table(table(data$target)), 4)*100

# --------------------

# Indicateurs cles (variables quantitatives)
str(data)
summary(data$age)
summary(data$age)
summary(data$trestbps)
summary(data$chol)
summary(data$thalech)
summary(data$oldpeak)
var(data$age)
sd(data$age)

var(data$trestbps)
sd(data$trestbps)
var(data$chol)
sd(data$chol)
var(data$thalech)
sd(data$thalech)
var(data$oldpeak)
sd(data$oldpeak)
#--------------
#variable sex
graph1<-plot(data$sex,xlab="sex",
     ylab="effectif",
     main="répartition",
     las=1,
     sub="machine learning",
     space=2,
     col=c("blue","red"),
     cex.main=1.8,
     cex.axis=1,
     ylim=c(0,250))
text(x = graph1, y = table(data$sex)+15, labels = as.character(table(data$sex)), cex = 1.1)
#diagramme curculaire
pie(table(data$exang),main="rep",clockwise=TRUE)
#boite à moustache pour variable quantitative
#varaiable age
boxplot(data$age,ylab="age",main="boite à moustache",
col="blue" ,
las=1,cex.lab=1.2,
notch=TRUE ,

)
#COCHE DANS LE MEDIANE
#histogramme
graph3 <- hist(data$trest,
xlab = "Tension arterielle au repos",
ylab = "Effectifs",
main = "Repartition des patients selon la tension arterielle au repos",
las = 1,
sub = "Donnees : Heart Disease Data Set (UCI Machine Learning)",
col = "blue",


cex.main = 1.4,
cex.lab = 1.2)
     #garph mids pour connaitre ou on mettre les données
text(x = graph3$mids, graph3$counts, labels = graph3$counts, adj = c(0.5, -0.5))
#croisé
graph4<-barplot(table(data$target,data$sex),beside=TRUE,
        col = c("#003049", "#d62828"),
        xlab = "Sexe",
        ylab = "Patients",
        las = 1,
        main = "Repartition des patents selon la presence d'une maladie cardiovasculaire \n et le sexe")
legend("top", legend = levels(data$target), fill = c("#003049", "#d62828"), title = "Maladie cardiovasculaire", horiz = TRUE)
text(x = graph4, y = table(data$target, data$sex)+7, labels = as.character(table(data$target, data$sex)), cex = 1.1, font = 3)
# Boites a moustaches croisees

## Variable target/age
boxplot(data$age ~ data$target,
        main = "Boite a moustaches de la population selon l'age et la presence \n de maladie cardiovasculaire",
        xlab = "Presence d'une maladie cardiovasculaire",
        ylab = "Age",
        col = "yellow",
        las = 1,
       
        cex.main = 1.2,
        cex.lab = 1.2
)

#---------------
## Test du Khi-2 (variables qualitatives)
## H0 : Les deux variables sont independantes (si p-value > 0,05)
## H1 : Les deux variables sont dependantes (si p-value < 0,05)
chisq.test(data$sex, data$target)
#calcul moyenne
tapply(data$age, data$target, mean)
library(dplyr)
shapiro.test(filter(data, exang == "Oui")$age) # H1
shapiro.test(filter(data, target == "Oui")$trestbps) # H1
shapiro.test(filter(data, target == "Oui")$chol) # H0
shapiro.test(filter(data, target == "Oui")$thalach) # H0
shapiro.test(filter(data, target == "Oui")$oldpeak) # H1
## Test de Mann-Whitney
### H0 : Il n'y a pas de difference significative entre la moyenne des deux variables (si p-value > 0,05)
### H1 : Il y a une difference significative entre la moyenne des deux variables (si p-value < 0,05)
wilcox.test(data$age~data$target)
wilcox.test(data$trestbps~data$target)
wilcox.test(data$oldpeak~data$target)

## Test de Student
### H0 : Il n'y a pas de difference significative entre la moyenne des deux variables (si p-value > 0,05)
### H1 : Il y a une difference significative entre la moyenne des deux variables (si p-value < 0,05)
t.test(data$chol~data$target)
t.test(data$thalach~data$target)
