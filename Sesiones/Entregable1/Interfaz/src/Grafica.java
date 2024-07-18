
import java.awt.*;
import java.util.ArrayList;
import java.util.Arrays;
import javax.swing.*;
import org.knowm.xchart.XChartPanel;
import org.knowm.xchart.XYChart;
import org.knowm.xchart.XYChartBuilder;
import org.knowm.xchart.XYSeries;
import org.knowm.xchart.style.markers.SeriesMarkers;

public class Grafica implements Runnable {

    private String[] xLabels;
    private double[][] yData;

    public Grafica(String[] xLabels, double[][] yData) {
        this.xLabels = xLabels;
        this.yData = yData;
    }

    @Override
    public void run() {
        double[][] tiempos = new double[yData[0].length][xLabels.length];
        for (int i = 0; i < yData[0].length; i++) {
            for (int j = 0; j < xLabels.length; j++) {
                tiempos[i][j] = yData[j][i];
            }
        }

        double[] xData = new double[xLabels.length];
        for (int i = 0; i < xLabels.length; i++) {
            xData[i] = i;
        }

        XYChart chart = new XYChartBuilder()
                .width(800)
                .height(600)
                .title("GRÁFICA DE EFICIENCIA DE MÉTODOS DE ORDENAMIENTO")
                .xAxisTitle("Tamaño Lista")
                .yAxisTitle("Tiempo (segundos)")
                .build();

        chart.getStyler().setDefaultSeriesRenderStyle(XYSeries.XYSeriesRenderStyle.Line);

        ArrayList<String> metodos = new ArrayList<>(Arrays.asList("QuickSort", "HeapSort", "ShellSort", "RadixSort", "BucketSort"));
        for (int i = 0; i < tiempos.length; i++) {
            XYSeries series = chart.addSeries(metodos.get(i), xData, tiempos[i]);
            series.setMarker(SeriesMarkers.CIRCLE);
        }

        addCustomLabels(chart, xLabels);
    }

    private static void addCustomLabels(XYChart chart, String[] labels) {
        // Crear un panel para contener el gráfico y las etiquetas
        JFrame frame = new JFrame();
        frame.setLayout(new BorderLayout());
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // Añadir el panel del gráfico al centro del marco
        JPanel chartPanel = new XChartPanel<>(chart);
        frame.add(chartPanel, BorderLayout.CENTER);

        // Crear un panel de etiquetas en la parte inferior
        JPanel labelPanel = new JPanel();
        labelPanel.setLayout(new GridLayout(1, labels.length));
        for (String label : labels) {
            JLabel jLabel = new JLabel(label, SwingConstants.CENTER);
            labelPanel.add(jLabel);
        }

        // Añadir el panel de etiquetas al sur del marco
        frame.add(labelPanel, BorderLayout.SOUTH);

        // Configurar y mostrar el marco
        frame.pack();
        frame.setVisible(true);
    }
}
