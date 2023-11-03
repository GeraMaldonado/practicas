Entrena <- function(datos, K, formula){
  library(caret)
  library(pROC)

  Y <- strsplit(formula, split = "~")[[1]]
  Y <- strsplit(formula, split = " ")[[1]]
  indiceColumna <- which(names(datos) == Y[1])
    
  indices <- createFolds( y = datos[,indiceColumna],
                          k=K,
                          returnTrain = TRUE,
                          list = TRUE)

  formula <- as.formula(formula)
  
  entrenamiento <- data.frame(AUC = numeric(0), Sens = numeric(0), Spe = numeric(0), Acc = numeric(0))
  prueba <- data.frame(AUC = numeric(0), Sens = numeric(0), Spe = numeric(0), Acc = numeric(0))
  
  for(i in 1:K){
    datosEntrenamiento <- datos[indices[[i]],]
    datosprueba <- datos[-indices[[i]],]
    modelo = glm(formula,
                 data = datos,
                 family = "binomial")
    
    predicciones = predict(modelo,  newdata = datosEntrenamiento,
                           type = "response")
    #Formamos la tabla
    tablita = data.frame(Deberia=datosEntrenamiento[,indiceColumna], 
                         Predicciones=predicciones)
    
    curva = roc(tablita$Deberia, 
                tablita$Predicciones, 
                levels=c(0,1),
                plot=TRUE,
                ci=TRUE, smooth=FALSE,
                direction='auto',
                col="blue", 
                main="Curva ROC (BCDR)")
    res1 <- coords(curva, "best", ret=c("accuracy", "specificity", "sensitivity"))
    #Area bajo la curva
    res2 <- curva$auc
    entrenamiento[i,] <- data.frame(AUC = res2, Sens = res1$sensitivity, Spe = res1$specificity, Acc = res1$accuracy)
    
    predicciones = predict(modelo,  newdata = datosprueba,
                           type = "response")
    
    tablita = data.frame(Deberia=datosprueba[,indiceColumna], 
                         Predicciones=predicciones)
    curva = roc(tablita$Deberia, 
                tablita$Predicciones, 
                levels=c(0,1),
                plot=TRUE,
                ci=TRUE, smooth=FALSE,
                direction='auto',
                col="blue", 
                main=paste("Curva ROC (BCDR) K = ",i))
    res1<- coords(curva, "best", ret=c("accuracy", "specificity", "sensitivity"))
    res2<- curva$auc
    prueba[i,] <- data.frame(AUC = res2, Sens = res1$sensitivity, Spe = res1$specificity, Acc = res1$accuracy)
  }
  
  promAUC <- (sum(entrenamiento[,1])/K)
  promSens <- (sum(entrenamiento[,2])/K)
  promSpe <- (sum(entrenamiento[,3])/K)
  promAcc <- (sum(entrenamiento[,4])/K)
  
  entrenamiento["promedio",] <- data.frame(AUC = promAUC, Sens = promSens, Spe = promSpe, Acc = promAcc)
  
  promAUC <- (sum(prueba[,1])/K)
  promSens <- (sum(prueba[,2])/K)
  promSpe <- (sum(prueba[,3])/K)
  promAcc <- (sum(prueba[,4])/K)
  
  prueba["promedio",] <- data.frame(AUC = promAUC, Sens = promSens, Spe = promSpe, Acc = promAcc)
  
  print(entrenamiento)
  print(prueba)
}


Entrena(datosCancer, 4, "classification ~ s_circularity + i_kurtosis + t_corr + t_inf1h ")


datosCancer <- read.csv("~/Descargas/bcdr_d01_features.csv")

datosCancer$classification[datosCancer$classification== "Benign"] <- 0
datosCancer$classification[datosCancer$classification== "Malign"] <- 1
datosCancer$classification <- as.numeric(datosCancer$classification)
