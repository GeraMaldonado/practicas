datosFaltantes <- function(datos){
  for(i in 1:ncol(datos)){
    na <- sum(is.na(datos[,i]))
    indice <- c()
    if(na>0){
      for(j in 1:nrow(datos)){
        if(any(is.na(datos[j,i]))){indice <- c(indice,j)}
      }
      print(paste("Columna:",i,",",na,"dato(s) faltante(s), idices ", paste(indice, collapse = ", "), sep = " "))
    }else{
      print(paste("Columna:",i,"ok",sep=" "))
    }
  }
}


imputacion <- function(datos){
  for(i in 1:ncol(datos)){
    na <- sum(is.na(datos[,i]))
    if(na>0){
      promedio <- mean(datos[,i],na.rm=T)
      for(j in 1:nrow(datos)){
        if(any(is.na(datos[j,i]))){datos[j,i] <- round(promedio,0)}
      }
    print(paste("Datos faltanres de la columna",i," remplazado con:", promedio))
    }
  }
  return(datos)
}
