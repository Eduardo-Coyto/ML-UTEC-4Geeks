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
  
  _Añadir un único archivo:_
  
  git add <archivo>
  
  _Añadir todo de una vez:_
  
  git add -A
  
  Si revisas la captura de pantalla que he más arriba, verás que hay nombres de archivos en rojo - esto significa que los archivos están sin preparación. Estos archivos no serán incluidos en tus commits hasta que no los añadas. Por lo tanto, para añadirlos deberas usar git add
  
 ![image](https://user-images.githubusercontent.com/79756539/166967198-b3701b0c-876a-49b5-9ab4-b8a1bcab7b57.png)
  
  
  ## Git commit
  
  -Git commit es como establecer un punto de control en el proceso de desarrollo al cual puedes volver más tarde si es necesario.
  
  git commit -m "mensaje de confirmación"
  
  _Importante:_ Git commit guarda tus cambios únicamente en local.
  
 
  ## Git push
  
-Después de haber confirmado tus cambios, el siguiente paso que quieres dar es enviar tus cambios al servidor remoto. Git push envía tus commits al repositorio remoto.
  
  
  git push <nombre-remoto> <nombre-de-tu-rama>
  
 -si la rama ha sido creada recientemente, puede que tengas que cargar y subir tu rama con el siguiente comando:
  
git push --set-upstream <nombre-remoto> <nombre-de-tu-rama>
  
  o
  
  **git push -u origin <nombre-de-tu-rama>**
  
  
  ## Git pull
  
  -Se utiliza para recibir actualizaciones del repositorio remoto. Este comando es una combinación del git fetch y del git merge lo cual significa que cundo usemos el git pull recogeremos actualizaciones del repositorio remoto (git fetch) e inmediatamente aplicamos estos últimos cambios en local (git merge).
  
**git pull <nombre-remoto>**
  
  
  ##Git revert
 
  - Cuando necesitamos deshacer los cambios que hemos hecho. Hay varias maneras para deshacer nuestros cambios en local y/o en remoto (dependiendo de lo que necesitemos), pero necesitaremos utilizar cuidadosamente estos comandos para evitar borrados no deseados.
  
  Una manera segura para deshacer nuestras commits es utilizar git revert. Para ver nuestro historial de commits, primero necesitamos utilizar el  git log -- oneline:
  

  
  
