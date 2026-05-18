import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# 1. Importa i dati impostando la colonna 'date' come indice e forzando il tipo datetime
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# 2. Pulisci i dati escludendo i giorni che stanno nel top 2.5% o nel bottom 2.5%
df = df[
    (df['value'] >= df['value'].quantile(0.025)) &
    (df['value'] <= df['value'].quantile(0.975))
]

def draw_line_plot():
    # Crea una copia del dataframe per il grafico a linee
    df_line = df.copy()

    # Configura la figura in modo esplicito
    fig, ax = plt.subplots(figsize=(15, 5))
    
    # Disegna la linea
    ax.plot(df_line.index, df_line['value'], color='red', linewidth=1)
    
    # Imposta esplicitamente titolo e label degli assi richiesti
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Salva il grafico e restituisce la figura
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copia e prepara i dati estraendo l'anno e il mese dall'indice temporale
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.strftime('%B')

    # Ordine cronologico esatto dei mesi richiesto per il riordinamento delle colonne
    months_order = [
        'January', 'February', 'March', 'April', 'May', 'June', 
        'July', 'August', 'September', 'October', 'November', 'December'
    ]

    # Raggruppa per anno e mese calcolando la media, poi sposta i mesi nelle colonne (.unstack())
    df_grouped = df_bar.groupby(['year', 'month'])['value'].mean().unstack()
    df_grouped = df_grouped.reindex(columns=months_order)

    # Disegna il grafico a barre usando l'approccio ad assi
    fig, ax = plt.subplots(figsize=(7, 7))
    df_grouped.plot(kind='bar', ax=ax)
    
    # Configura i testi e le legende in modo preciso
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(title='Months', labels=months_order)

    # Salva il grafico e restituisce la figura
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepara i dati creando una copia e formattando anni e mesi
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Ordina i mesi in forma abbreviata (Jan, Feb, ecc.) come richiesto dai test
    months_short_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    df_box['month'] = pd.Categorical(df_box['month'], categories=months_short_order, ordered=True)

    # Configura la figura affiancando due grafici (1 riga, 2 colonne)
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    # Primo box plot: Distribuzione per Anno (Trend)
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    # Secondo box plot: Distribuzione per Mese (Stagionalità)
    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    # Salva il grafico e restituisce la figura
    fig.savefig('box_plot.png')
    return fig