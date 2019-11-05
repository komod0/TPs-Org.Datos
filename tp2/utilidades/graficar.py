import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter # Para formatear los ejes

def ver_dispersion(y_test, prediction):
    plt.figure(figsize=(10,10))
    plt.scatter(y_test, prediction, alpha = 0.2) 
    plt.title('Dispersión: Valores Reales Vs Predicciones', fontsize = 25)
    plt.ylabel('Predicciones', fontsize = 20)
    plt.xlabel('Valores reales', fontsize = 20)
    plt.xticks(rotation = 30, fontsize = 17, ha = 'right')
    plt.yticks(fontsize = 17)
    plt.gca().xaxis.set_major_formatter(FormatStrFormatter('%.0f'))
    plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.0f'))
    # Recta x = y
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=4)
    plt.show()
    return None