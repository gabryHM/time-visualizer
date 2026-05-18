import time_series_visualizer
import unittest

# Genera localmente i tre grafici per controllare visivamente il risultato
print("Generazione dei grafici temporali in corso...")
time_series_visualizer.draw_line_plot()
time_series_visualizer.draw_bar_plot()
time_series_visualizer.draw_box_plot()
print("Grafici salvati con successo come 'line_plot.png', 'bar_plot.png' e 'box_plot.png'!")

print("\n" + "="*50 + "\nAvvio dei test automatici di freeCodeCamp:\n" + "="*50)

# Importa ed esegue i test unitari contenuti nel test_module
from test_module import TimeSeriesVisualizerTestCase
unittest.main()