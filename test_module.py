import unittest
import time_series_visualizer
import matplotlib as mpl

class TimeSeriesVisualizerTestCase(unittest.TestCase):
    def setUp(self):
        self.line_fig = time_series_visualizer.draw_line_plot()
        self.bar_fig = time_series_visualizer.draw_bar_plot()
        self.box_fig = time_series_visualizer.draw_box_plot()

    def test_line_plot_title(self):
        actual = self.line_fig.axes[0].get_title()
        expected = 'Daily freeCodeCamp Forum Page Views 5/2016-12/2019'
        self.assertEqual(actual, expected, "Il titolo del line plot non è corretto.")

    def test_line_plot_labels(self):
        actual_x = self.line_fig.axes[0].get_xlabel()
        actual_y = self.line_fig.axes[0].get_ylabel()
        self.assertEqual(actual_x, 'Date', "L'etichetta dell'asse X del line plot deve essere 'Date'.")
        self.assertEqual(actual_y, 'Page Views', "L'etichetta dell'asse Y del line plot deve essere 'Page Views'.")

    def test_bar_plot_legend(self):
        actual = self.bar_fig.axes[0].get_legend().get_title().get_text()
        expected = 'Months'
        self.assertEqual(actual, expected, "Il titolo della legenda del bar plot deve essere 'Months'.")

    def test_box_plot_number(self):
        actual = len(self.box_fig.axes)
        expected = 2
        self.assertEqual(actual, expected, "La figura del box plot deve contenere esattamente 2 sotto-grafici affiancati.")

    def test_box_plot_titles(self):
        actual_title_1 = self.box_fig.axes[0].get_title()
        actual_title_2 = self.box_fig.axes[1].get_title()
        self.assertEqual(actual_title_1, 'Year-wise Box Plot (Trend)', "Titolo del primo box plot errato.")
        self.assertEqual(actual_title_2, 'Month-wise Box Plot (Seasonality)', "Titolo del secondo box plot errato.")

if __name__ == "__main__":
    unittest.main()