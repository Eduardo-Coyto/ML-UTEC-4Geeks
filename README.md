# Curso-ML-UTEC-4Geeks
1er Bootcamp en Machine Learning e Inteligencia Artificial Uruguay
## Git clone
- Básicamente realiza una copia idéntica de la última versión de un proyecto en un repositorio y la guarda en tu ordenador.


**git clone <https://link-con-nombre-del-repositorio>

## Git branch
- Usando ramas, varios desarrolladores pueden trabajar en paralelo en el mismo proyecto simultáneamente. Podemos usar el comando git branch para crearlas, listarlas y eliminarlas.


**git branch <nombre-de-la-rama>

  
Este comando creará una rama en local. Para enviar (push) la nueva rama al repositorio remoto, necesitarás usar el siguiente comando:  

  
git push <nombre-remoto> <nombre-rama>**  

  
_Visualización de ramas_

  
git branch
  
  
git branch --list

  
_Borrar una rama_

  
git branch -d <nombre-de-la-rama>  

## Git checkout

- Usaremos git checkout principalmente para cambiarte de una rama a otra. También lo podemos usar para chequear archivos y commits
    
git checkout <nombre-de-la-rama>

## Git status  
  
 - El comando de git status nos da toda la información necesaria sobre la rama actual
 
  git status
  
- Podemos encontrar información como:

1)  Si la rama actual está actualizada
2)  Si hay algo para confirmar, enviar o recibir (pull).
3)  Si hay archivos en preparación (staged), sin preparación(unstaged) o que no están recibiendo seguimiento (untracked)
4)  Si hay archivos creados, modificados o eliminados
  
  ![image](https://user-images.githubusercontent.com/79756539/166966442-a847f00a-258e-4d0c-8907-5a5c72ba589f.png)

  
## Git add
  
  -Cuando creamos, modificamos o eliminamos un archivo, estos cambios suceden en local y no se incluirán en el siguiente commit.
  Añadir un único archivo:
  
  git add <archivo>
  
  Añadir todo de una vez:
  
  git add -A
  
  
