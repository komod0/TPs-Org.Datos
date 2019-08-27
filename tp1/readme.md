## Notebook en Kaggle


## Informe
https://docs.google.com/document/d/1U-cCdz9mLbTJTAkp7kmF-VZ5WCEUuPRNRY0dMeQAoD8/edit

## Pendientes
https://docs.google.com/spreadsheets/d/1CjCCyjQu7wG6GAMnjj8r6Q6EANdKf7q6V7l_auf2dw8/edit#gid=0

## Documentación de Pandas
https://pandas.pydata.org/pandas-docs/stable/

# Consideraciones sobre los gráficos
- Antes de hacerlo, hacer una pregunta interesante que lo justifique
- Deben empezar en cero
- El formato (figsize) debe coincidir con el tamaño de los ejes
- Ponerles título, y nombres a los ejes
- Debe estar asociado a una conclusión interesante sobre los datos
- Poner "Log-Log plot." para aclarar que es logarítmico.
plt.xlabel("", fontsize = 14)
plt.ylabel("", fontsize = 14)
plt.title("", fontsize = 14)

### scatter: puntos individuales
- X numérica
- Y numéricas
- COLORES para comparaciones
- Se puede agregar línea de tendencias (sin o con faceteo)

### bar: valor numérico para cada caso
- X categórica
- Y numérica, empezando en cero
- COLORES para comparaciones

### hist: cuántas veces una variable numérica toma distintos valores
- X numérica (está ordenada)
- Y numérica discreta
- SIN COLOR

### density: versión continua del histograma, para mostrar la distribución de X
- Y ahora es continua
Para hacerlo (con seaborn)
sb.kdeplot(LO_QUE_SE_QUIERE_RAFICAR, shade = True, legend = False)


### box: para visualizar distribución de la variable
- Se pueden graficar varios boxplots para compararlos de acuerdo a una var. categórtica

### line: el clásico gráfico de ingresos en el tiempo de los dibujitos
- X tiempo (casi siempre)
- Y numérica (casi siempre, pero puede ser cualquier cosa)
- Y se puede usar para un ranking (perdiendo la distancia entre los casos)
- Cuidado: muy sensible a valores inusuales

### area: el área de cada curva en función del valor de cada valor.
- X tiempo (casi siempre)
- Y numérica (casi siempre, pero puede ser cualquier cosa)
- NO es pintar por debajo de cada línea: fijarse que las áreas
    (colores) nunca se superponen: el área es proporcional al 
	  valor de la variable, y debajo de la línea superarior se 
	 tiene el área total.


# Comandos para pandas (agreguen los que quieran)

- trasponer
.T 																    

- primeros n
df.head(n)															 

- n al azar
df.sample(n)														 

- descripción dimensional
df.shape

- metadata
df.info()															   

- cantidad de no-NaN (igual que info)
df.count()	

- cantidad total, incluye NaN
len(df)	

- resumen de los numéricos
df.describe() 	

- resumen de los no numéricos
df.describe(include = [numpy.object, pandas.Categorical])		    

- tipos de datos de las columnas
df.dtypes															   

- cuántos hay de cada tipo
df.get_dtype_counts()	

- ARRAY DE valores únicos por columna
df['COLUMNA'].unique()		

- hacer un sub data frame
df[['COLUMNA1', 'COLUMNA2']]

- cantidad de nulos por columna
df.isnull().sum()		

- top k mayores
df.nlargest(n, 'NOMBRE')

- top k menores
df.nsmallest(n, 'NOMBRE')

- columnas con cierto tipo de datos
df.select_dtypes(include = ['int65'])

- que contenga cierta palabra
df.filter(like = 'PALABRA')

- filtrar por expresión regular
df.filter(regex = '\')										

- ordenar por COLUMNA. Se puede poner más de una
df.sort_values('COLUMNA')			

- mostrar de abajo hacia arriba
df.iloc[::-1]		

- rankear cada atributo
df.rank()															    	


# Algunos comandos útiles de git (agreguen los que quieran)

####  Para enviar algo 
git pull repoDatos master
git add " "
git commit -m "Agrego nuestro archivo de prueba"
git push repoDatos master


#### CONFIGURACIÓN INICIAL
git config --global user.name "NOMBRE"
git config --global user.email "MAIL"
git config --list
git init

#### AGREGAR REPOSITORIO EXTERNO
git remote add <nombre> <url_repositorio>

#### BORRAR REPOSITORIO EXTERNO
git remote rm <nombre>

#### VER CUÁL ERA EL REPOSITORIO EXTERNO (en la parte de arriba)
git show

#### TRAERTE INFORMACIÓN DEL MASTER DEL REPO
git pull <nombre> master

#### HACER UN COMMIT Y SUBIRLO (SIEMPRE PULL ANTES)
git pull <nombre> master
git add <algo>
git commit -m "mensaje"
git push <nombre> master

#### CONOCER LA URL DEL REPO EXTERNO
git remote get-url <nombre>

#### OBTENER ID DEL COMMIT
git rev-parse HEAD 

#### DESHACER UN COMMIT
git reset HEAD~

#### SI NO TE DEJA HACER PULL/PUSH 
git stash
(y ahora volve a hacer el commit)

#### SI HICISTE LIO CON EL STASH/COMMIT
git init
git stash
git pull...

#### SI HICISTE MÁS LIO CON EL STASH/COMMIT
git rm -r --cached <carpeta>
git commit -m "mensaje"

#### SI NO TE RECONOCE EL COMMIT
git init y arranca de nuevo

#### SI TE SIGUE SIN RECONOCER
Fijate si no es un archivo considerado en el .gitignore
Ver "deshacer un commit"

#### VER INFORMACIÓN DEL ÚLTIMO PULL
git info

#### CAMBIAR USUARIO (Windows)
Control Panel >> User Account >> Credential Manager >> Windows Credential
Hacer un push para que te pida las credenciales

#### [ fatal: refusing to merge unrelated histories ]
git pull REPOSITORIO master --allow-unrelated-histories
git merge master YuGiOh/master
... add and commit here...
git push YuGiOh master

