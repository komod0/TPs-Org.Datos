# Trabajo Práctico I

## Informe
https://docs.google.com/document/d/1U-cCdz9mLbTJTAkp7kmF-VZ5WCEUuPRNRY0dMeQAoD8/edit

## Pendientes
https://docs.google.com/spreadsheets/d/1CjCCyjQu7wG6GAMnjj8r6Q6EANdKf7q6V7l_auf2dw8/edit#gid=0

## Documentación de Pandas
https://pandas.pydata.org/pandas-docs/stable/

# Consideraciones sobre los gráficos

###scatter: puntos individuales
[*] X numérica
[*] Y numéricas
[*] COLORES para comparaciones
[*] Se puede agregar línea de tendencias (sin o con faceteo)

###bar: valor numérico para cada caso
[*] X categórica
[*] Y numérica, empezando en cero
[*] COLORES para comparaciones

###hist: cuántas veces una variable numérica toma distintos valores
[*] X numérica (está ordenada)
[*] Y numérica discreta
[*] SIN COLOR

###density: variante continua del histograma, para mostrar la distribución de X

###box: para visualizar distribución de la variable
[*] Se pueden graficar varios boxplots para compararlos de acuerdo a una var. categórtica

###ine: el clásico gráfico de ingresos en el tiempo de los dibujitos
[*] X tiempo (casi siempre)
[*] Y numérica (casi siempre, pero puede ser cualquier cosa)
[*] Y se puede usar para un ranking (perdiendo la distancia entre los casos)
[*] Cuidado: muy sensible a valores inusuales

###area: el área de cada curva en función del valor de cada valor.
[*] X tiempo (casi siempre)
[*] Y numérica (casi siempre, pero puede ser cualquier cosa)
[*] NO es pintar por debajo de cada línea: fijarse que las áreas
    (colores) nunca se superponen: el área es proporcional al 
	  valor de la variable, y debajo de la línea superarior se 
	 tiene el área total.


# Comandos para pandas (agreguen los que quieran)
.T 																    #trasponer

df.head(n)															 #primeros n
df.sample(n)														 #n al azar
df.shape															   #descripción dimensional
df.info()															   #metadata
df.count()															 #cantidad de no-NaN (igual que info)
len(df)																   #cantidad total, incluye NaN
df.describe() 													#resumen de los numéricos
df.describe(include = [numpy.object, pandas.Categorical])		    #resumen de los no numéricos
df.dtypes															   #tipos de datos de las columnas
df.get_dtype_counts()											#cuántos hay de cada tipo
df['COLUMNA'].unique()										#ARRAY DE valores únicos por columna
df[['COLUMNA1', 'COLUMNA2']]							#hacer un sub data frame
df.isnull().sum()													#cantidad de nulos por columna
df.nlargest(n, 'NOMBRE')									#top k mayores
df.nsmallest(n, 'NOMBRE')									#top k menores
df.select_dtypes(include = ['int65'])			#columnas con cierto tipo de datos
df.filter(like = 'PALABRA')								#que contenga cierta palabra
df.filter(regex = '\')										#filtrar por expresión regular
df.sort_values('COLUMNA')									#ordenar por COLUMNA. Se puede poner más de una
df.iloc[::-1]													  	#mostrar de abajo hacia arriba
df.rank()															    #rankear cada atributo
																	        #tiene opciones para rankear por
																        	#distintas cosas y eso


# Algunos comandos útiles de git (agreguen los que quieran)

=== Para enviar algo ===
git pull repoDatos master
git add " "
git commit -m "Agrego nuestro archivo de prueba"
git push repoDatos master


CONFIGURACIÓN INICIAL
git config --global user.name "NOMBRE"
git config --global user.email "MAIL"
git config --list
git init

AGREGAR REPOSITORIO EXTERNO
git remote add <nombre> <url_repositorio>

BORRAR REPOSITORIO EXTERNO
git remote rm <nombre>

VER CUÁL ERA EL REPOSITORIO EXTERNO (en la parte de arriba)
git show

TRAERTE INFORMACIÓN DEL MASTER DEL REPO
git pull <nombre> master

HACER UN COMMIT Y SUBIRLO (SIEMPRE PULL ANTES)
git pull <nombre> master
git add <algo>
git commit -m "mensaje"
git push <nombre> master

CONOCER LA URL DEL REPO EXTERNO
git remote get-url <nombre>

OBTENER ID DEL COMMIT
git rev-parse HEAD 

DESHACER UN COMMIT
git reset HEAD~

SI NO TE DEJA HACER PULL/PUSH 
git stash
(y ahora volve a hacer el commit)

SI HICISTE LIO CON EL STASH/COMMIT
git init
git stash
git pull...

SI HICISTE MÁS LIO CON EL STASH/COMMIT
git rm -r --cached <carpeta>
git commit -m "mensaje"

SI NO TE RECONOCE EL COMMIT
git init y arranca de nuevo

SI TE SIGUE SIN RECONOCER
Fijate si no es un archivo considerado en el .gitignore
Ver "deshacer un commit"

VER INFORMACIÓN DEL ÚLTIMO PULL
git info

CAMBIAR USUARIO (Windows)
Control Panel >> User Account >> Credential Manager >> Windows Credential
Hacer un push para que te pida las credenciales

[ fatal: refusing to merge unrelated histories ]
git pull REPOSITORIO master --allow-unrelated-histories
git merge master YuGiOh/master
... add and commit here...
git push YuGiOh master

