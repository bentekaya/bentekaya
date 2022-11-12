#une partie de projet "prédiction d 'une maladie cardiovasculaire"
#Analyse statistique
data <- read.csv(url("https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data"), header = FALSE)
#output y=Target (variable qualitatives)
colnames(data)<-c("age","sex","cp","trest","chol","fbs","reseg","thalec","exang","oldpeak","slop","ca","thal","target")
#pretraitement de la colonne target 
data$target[data$target==2]<-1
data$target[data$target==3]<-1
data$target[data$target==4]<-1
#valaeur manquante
data<-data[-88,]
valeurmanquanteca<-which(data$ca %in% "?")
valeurmanquantethal<-which(data$thal %in% "?")
valeur<-c(valeurmanquanteca,valeurmanquantethal)
data<-data[-valeur,]
#verification de type de variable
str(data)
#modification de type de variable
#variable qualitative =factor
data$sex<-as.factor(data$sex)
data$cp<-as.factor(data$cp)
data$fbs<-as.factor(data$fbs)
data$reseg<-as.factor(data$reseg)
data$exang<-as.factor(data$exang)
data$slop<-as.factor(data$slop)
data$ca<-as.factor(data$ca)
#variable quantitative
data$age<-as.integer(data$age)
data$trest<-as.integer(data$trest)
data$chol<-as.integer(data$chol)
data$thalec<-as.integer(data$thalec)
str(data)



  # Recodage des variables
levels(data$sex) <- c("Femme", "Homme")
levels(data$cp) <- c("Angine stable", "Angine instable", "Autres douleurs", "Asymptomatique")
levels(data$fbs) <- c("Non", "Oui")
levels(data$reseg) <- c("Normal", "Anomalies", "Hypertrophie")
levels(data$exang) <- c("Non", "Oui")
levels(data$slop) <- c("En hausse", "Stable", "En baisse")
levels(data$ca) <- c("Absence d'anomalie", "Faible", "Moyen", "Eleve")
levels(data$thal) <- c("Non", "Thalassemie sous controle", "Thalassemie instable")
levels(data$target) <- c("Non", "Oui")
#------------
#variable qualitative :calcul les effectifs
table(data$sex)#effectif
round(prop.table(table(data$sex)),4)*100#frequence en pourcentages
table(data$fbs)
round(prop.table(table(data$fbs)), 4)*100

# Variable restecg
table(data$restecg)
round(prop.table(table(data$restecg)), 4)*100

# Variable exang
table(data$exang)
round(prop.table(table(data$exang)), 4)*100

# Variable slope
table(data$slope)
round(prop.table(table(data$slope)), 4)*100

# Variable ca
table(data$ca)
round(prop.table(table(data$ca)), 4)*100

# Variable thal
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
#diagramme circulaire
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
     #garph mids pour connaitre ou on mets les données
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
