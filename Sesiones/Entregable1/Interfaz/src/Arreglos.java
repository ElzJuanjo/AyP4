
import java.util.ArrayList;
import javax.swing.JOptionPane;

public class Arreglos {

    private ArrayList<ArrayList<Integer>> listaArreglos = new ArrayList<>();

    public Arreglos(int cantidadArreglos) {
        JOptionPane.showMessageDialog(null,
                "¡Deben tener más de 1000 elementos!",
                "CONDICIÓN", 1);
        for (int i = 0; i < cantidadArreglos; i++) {
            int n = Integer.parseInt(JOptionPane.showInputDialog(null,
                    "Tamaño de la lista con indice ["+i+"]:", "LLENADO DE DATOS",
                    3));
            if (n >= 1000) {
                ArrayList<Integer> nuevaLista = new ArrayList<>();

                while (nuevaLista.size() < n) {
                    int numeroAleatorio = (int) (Math.random() * 10000) + 1;
                    if (!nuevaLista.contains(numeroAleatorio)) {
                        nuevaLista.add(numeroAleatorio);
                    }
                }

                listaArreglos.add(nuevaLista);
            } else {
                JOptionPane.showMessageDialog(null,
                        "¡No cumple la condición!",
                        "AVISO", 2);
            }

        }
    }

    public ArrayList<ArrayList<Integer>> getListaArreglos() {
        return listaArreglos;
    }
}
