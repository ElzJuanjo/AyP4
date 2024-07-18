
import java.awt.*;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.util.ArrayList;
import javax.swing.*;
import javax.swing.border.EmptyBorder;
import org.python.core.PyList;
import org.python.util.PythonInterpreter;

public class Ventana extends JFrame {

    private JTextField arreglosOrdenar = new JTextField();
    private JButton opcionOrdenar = new JButton("Crear Listas");
    private Arreglos listasOrdenar;
    private JButton mostrarGrafica = new JButton("Mostrar Gráfica");
    private JTextField indiceOrdenar = new JTextField();
    private JButton imprimirOriginal = new JButton("Imprimir Original");
    private JButton imprimirOrdenada = new JButton("Imprimir Ordenada");

    private JTextField arreglosHashing = new JTextField();
    private JButton opcionHashing = new JButton("Crear Arreglo");
    private ArrayList<Integer> listaHashing;
    private JButton imprimirDatos = new JButton("Imprimir Datos");
    private JButton imprimirSHA = new JButton("Imprimir SHA-1");
    private JButton BuscarSHA = new JButton("Buscar SHA-1");
    private JButton imprimirMC = new JButton("Imprimir Medio Cuadrado");
    private JButton BuscarMC = new JButton("Buscar Medio Cuadrado");
    private JButton imprimirTiempos = new JButton("Imprimir Tiempos");

    private String rutaFunciones = "C:\\Users\\Juan José JV\\Documents\\AyP4\\algoritmos_y_programacion_4\\Sesiones\\Entregable1\\Funciones";

    public Ventana() {
        this.setLayout(new GridLayout(1, 2));
        JPanel contenedorOrdenar = new JPanel(new GridLayout(10, 1));
        contenedorOrdenar.setBorder(new EmptyBorder(10, 10, 10, 10));
        JPanel contenedorHashing = new JPanel(new GridLayout(10, 1));
        contenedorHashing.setBorder(new EmptyBorder(10, 10, 10, 10));

        Font titulos = new Font("Cascadia Code", Font.BOLD, 24);
        Font textos = new Font("Cascadia Code", Font.PLAIN, 14);

        JLabel tituloOrdenar = new JLabel("ORDENAMIENTO");
        JLabel nTexto = new JLabel("Cantidad de listas: ");
        tituloOrdenar.setFont(titulos);
        nTexto.setFont(textos);
        opcionOrdenar.setFont(textos);
        contenedorOrdenar.add(tituloOrdenar);
        contenedorOrdenar.add(nTexto);
        contenedorOrdenar.add(arreglosOrdenar);
        contenedorOrdenar.add(opcionOrdenar);
        mostrarGrafica.setFont(textos);
        contenedorOrdenar.add(mostrarGrafica);
        contenedorOrdenar.add(new JPanel());
        JLabel textoIndice = new JLabel("Indice de la lista: ");
        textoIndice.setFont(textos);
        imprimirOrdenada.setFont(textos);
        imprimirOriginal.setFont(textos);
        contenedorOrdenar.add(textoIndice);
        contenedorOrdenar.add(indiceOrdenar);
        contenedorOrdenar.add(imprimirOriginal);
        contenedorOrdenar.add(imprimirOrdenada);

        JLabel tituloBuscar = new JLabel("HASHING");
        JLabel nTextoDos = new JLabel("Tamaño del arreglo: ");
        nTextoDos.setFont(textos);
        opcionHashing.setFont(textos);
        tituloBuscar.setFont(titulos);
        contenedorHashing.add(tituloBuscar);
        contenedorHashing.add(nTextoDos);
        contenedorHashing.add(arreglosHashing);
        contenedorHashing.add(opcionHashing);
        imprimirDatos.setFont(textos);
        imprimirSHA.setFont(textos);
        imprimirMC.setFont(textos);
        imprimirTiempos.setFont(textos);
        BuscarSHA.setFont(textos);
        BuscarMC.setFont(textos);
        contenedorHashing.add(imprimirDatos);
        contenedorHashing.add(imprimirSHA);
        contenedorHashing.add(BuscarSHA);
        contenedorHashing.add(imprimirMC);
        contenedorHashing.add(BuscarMC);
        contenedorHashing.add(imprimirTiempos);

        eventosOrdenar();
        eventosHashing();
        this.add(contenedorOrdenar);
        this.add(contenedorHashing);
    }

    public void abrirPrograma() {
        this.pack();
        this.setTitle("Juanjo y Alejo [AyP 4]");
        this.setLocationRelativeTo(null);
        this.setResizable(false);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setVisible(true);
    }

    private void eventosOrdenar() {
        opcionOrdenar.addMouseListener(new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent e) {
                try {
                    int n = Integer.parseInt(arreglosOrdenar.getText());
                    if (n > 0 && n < 11) {
                        listasOrdenar = new Arreglos(n);
                        JOptionPane.showMessageDialog(null,
                                "¡Se han actualizado las listas!",
                                "INFO", 1);
                    } else {
                        JOptionPane.showMessageDialog(null,
                                "¡Debe ser entre [1,10] listas!",
                                "CONDICIÓN", 1);
                    }
                } catch (NumberFormatException exeption) {
                    JOptionPane.showMessageDialog(null,
                            "¡Debes ingresar un número entero!",
                            "AVISO", 2);
                }
            }
        }
        );
        mostrarGrafica.addMouseListener(new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent e) {
                try {
                    PythonInterpreter interpreter = new PythonInterpreter();
                    interpreter.set("rutaFunciones", rutaFunciones);
                    double[][] listaDeTiempos = new double[listasOrdenar.getListaArreglos().size()][5];
                    String[] listaTamano = new String[listasOrdenar.getListaArreglos().size()];
                    int j = 0;
                    for (ArrayList<Integer> subList : listasOrdenar.getListaArreglos()) {
                        listaTamano[j] = String.valueOf(subList.size());
                        interpreter.set("subList", subList);
                        interpreter.exec("""
                            import sys
                            sys.path.append(rutaFunciones)
                            from ordenamientos import calculateTimes
                            """);
                        PyList tiemposPython = (PyList) interpreter.eval("calculateTimes(subList)");
                        double[] tiemposJava = new double[tiemposPython.size()];
                        for (int i = 0; i < tiemposPython.size(); i++) {
                            tiemposJava[i] = (double) tiemposPython.get(i);
                        }
                        for (int i = 0; i < 5; i++) {
                            listaDeTiempos[j][i] = tiemposJava[i];
                        }
                        j++;
                    }
                    Grafica grafica = new Grafica(listaTamano, listaDeTiempos);
                    Thread hilo = new Thread(grafica);
                    hilo.run();
                } catch (Exception exeption) {
                    JOptionPane.showMessageDialog(null,
                            "¡Algo ha salido mal!",
                            "ERROR", 0);
                }
            }
        }
        );
        imprimirOriginal.addMouseListener(new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent e) {
                try {
                    int n = Integer.parseInt(indiceOrdenar.getText());
                    if (n >= 0 && n < listasOrdenar.getListaArreglos().size()) {
                        PythonInterpreter interpreter = new PythonInterpreter();
                        interpreter.set("listaOriginal", listasOrdenar.getListaArreglos().get(n));
                        interpreter.set("indice", n);
                        System.out.println();
                        interpreter.exec("""
                                print("\t* LISTA ORIGINAL [{}] ({}) *".format(indice,len(listaOriginal)))
                                print(listaOriginal)
                                """);
                    } else {
                        JOptionPane.showMessageDialog(null,
                                "¡El indice de las listas es entre [0," + (listasOrdenar.getListaArreglos().size() - 1) + "]!",
                                "CONDICIÓN", 1);
                    }
                } catch (Exception exception) {
                    JOptionPane.showMessageDialog(null,
                            "¡Algo ha salido mal!",
                            "ERROR", 0);
                }
            }
        }
        );
        imprimirOrdenada.addMouseListener(new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent e) {
                try {
                    int n = Integer.parseInt(indiceOrdenar.getText());
                    if (n >= 0 && n < listasOrdenar.getListaArreglos().size()) {
                        PythonInterpreter interpreter = new PythonInterpreter();
                        interpreter.set("listaOriginal", listasOrdenar.getListaArreglos().get(n));
                        interpreter.set("indice", n);
                        interpreter.set("rutaFunciones", rutaFunciones);
                        System.out.println();
                        interpreter.exec("""
                                import sys
                                sys.path.append(rutaFunciones)
                                from ordenamientos import bucketSort
                                copiaLista = list(listaOriginal)
                                bucketSort(copiaLista)
                                print("\t* LISTA ORDENADA [{}] ({}) *".format(indice,len(copiaLista)))
                                print(copiaLista)
                                """);
                    } else {
                        JOptionPane.showMessageDialog(null,
                                "¡El indice de las listas es entre [0," + (listasOrdenar.getListaArreglos().size() - 1) + "]!",
                                "CONDICIÓN", 1);
                    }
                } catch (Exception exception) {
                    JOptionPane.showMessageDialog(null,
                            "¡Algo ha salido mal!",
                            "ERROR", 0);
                }
            }
        }
        );
    }

    private void eventosHashing() {
        opcionHashing.addMouseListener(
                new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent e) {
                try {
                    int n = Integer.parseInt(arreglosHashing.getText());
                    if (n > 0 && n <= 500) {
                        listaHashing = new ArrayList<>();
                        while (listaHashing.size() < n) {
                            int numeroAleatorio = (int) (Math.random() * 1000) + 1;
                            if (!listaHashing.contains(numeroAleatorio)) {
                                listaHashing.add(numeroAleatorio);
                            }
                        }
                        JOptionPane.showMessageDialog(null,
                                "¡Se ha actualizado el arreglo!",
                                "INFO", 1);
                    } else {
                        JOptionPane.showMessageDialog(null,
                                "¡Debe tener entre [1,500] elementos!",
                                "CONDICIÓN", 1);
                    }
                } catch (NumberFormatException exeption) {
                    JOptionPane.showMessageDialog(null,
                            "¡Debes ingresar un número entero!",
                            "AVISO", 2);
                }
            }
        }
        );
        imprimirDatos.addMouseListener(
                new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent e) {
                try {
                    PythonInterpreter interpreter = new PythonInterpreter();
                    interpreter.set("listaOriginal", listaHashing);
                    System.out.println();
                    interpreter.exec("""
                        print("\t* DATOS DEL ARREGLO ({}) *".format(len(listaOriginal)))
                        print(listaOriginal)
                        """);
                } catch (Exception exception) {
                    JOptionPane.showMessageDialog(null,
                            "¡Algo ha salido mal!",
                            "ERROR", 0);
                }
            }
        }
        );
        imprimirSHA.addMouseListener(
                new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent e) {
                try {
                    PythonInterpreter interpreter = new PythonInterpreter();
                    interpreter.set("listaOriginal", listaHashing);
                    interpreter.set("rutaFunciones", rutaFunciones);
                    System.out.println();
                    interpreter.exec("""
                            import sys
                            sys.path.append(rutaFunciones)
                            from hashing import crearHashTableSHA1
                            print("\t* TABLA HASHING SHA-1 *")
                            resultado = crearHashTableSHA1(listaOriginal)
                            for i in range(len(listaOriginal)):
                                print("[{}] Posicion: {} | Clave: {}".format(i,resultado[0][i],resultado[1][i]))
                            """);
                } catch (Exception exception) {
                    JOptionPane.showMessageDialog(null,
                            "¡Algo ha salido mal!",
                            "ERROR", 0);
                }
            }
        }
        );
        imprimirMC.addMouseListener(
                new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent e) {
                try {
                    PythonInterpreter interpreter = new PythonInterpreter();
                    interpreter.set("listaOriginal", listaHashing);
                    interpreter.set("rutaFunciones", rutaFunciones);
                    System.out.println();
                    interpreter.exec("""
                        import sys
                        sys.path.append(rutaFunciones)
                        from hashing import crearHashTableMedioCuadrado
                        print("\t* TABLA HASHING MEDIO CUADRADO *")
                        resultado = crearHashTableMedioCuadrado(listaOriginal)
                        for i in range(len(listaOriginal)):
                            print("[{}] Posicion: {} | Clave: {}".format(i,resultado[0][i],resultado[1][i]))
                        """);
                } catch (Exception exception) {
                    JOptionPane.showMessageDialog(null,
                            "¡Algo ha salido mal!",
                            "ERROR", 0);
                }
            }
        }
        );
        imprimirTiempos.addMouseListener(
                new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent e) {
                try {
                    PythonInterpreter interpreter = new PythonInterpreter();
                    interpreter.set("listaOriginal", listaHashing);
                    interpreter.set("rutaFunciones", rutaFunciones);
                    System.out.println();
                    interpreter.exec("""
                    import sys
                    sys.path.append(rutaFunciones)
                    from hashing import calculateTimes
                    calculateTimes(listaOriginal)
                    """);
                } catch (Exception exception) {
                    JOptionPane.showMessageDialog(null,
                            "¡Algo ha salido mal!",
                            "ERROR", 0);
                }
            }
        }
        );
        BuscarSHA.addMouseListener(
                new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent e) {
                try {
                    String info = JOptionPane.showInputDialog(null,
                            "Ingrese la clave:", "BUSCAR SHA-1",
                            3);
                    PythonInterpreter interpreter = new PythonInterpreter();
                    interpreter.set("clave", info);
                    interpreter.set("rutaFunciones", rutaFunciones);
                    interpreter.set("listaOriginal", listaHashing);
                    System.out.println();
                    interpreter.exec("""
                        import sys
                        import time
                        sys.path.append(rutaFunciones)
                        from hashing import buscarEnHashTable,crearHashTableSHA1
                        tabla = crearHashTableSHA1(listaOriginal)
                        inicio = time.time()
                        resultado = buscarEnHashTable(tabla,clave)
                        fin = time.time()
                        print("\t* RESULTADO DE BUSQUEDA SHA-1 *")
                        print("Posicion en el arreglo: {}".format(resultado[0]))
                        print("Clave: {}".format(resultado[1]))
                        print("Valor: {}".format(resultado[2]))
                        print("Tiempo de busqueda: {}".format(fin-inicio))
                            """);
                } catch (Exception exception) {
                    JOptionPane.showMessageDialog(null,
                            "¡Algo ha salido mal!" + exception,
                            "ERROR", 0);
                }
            }
        }
        );
        BuscarMC.addMouseListener(
                new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent e) {
                try {
                    String info = JOptionPane.showInputDialog(null,
                            "Ingrese la clave:", "BUSCAR M-C",
                            3);
                    PythonInterpreter interpreter = new PythonInterpreter();
                    interpreter.set("clave", info);
                    interpreter.set("rutaFunciones", rutaFunciones);
                    interpreter.set("listaOriginal", listaHashing);
                    System.out.println();
                    interpreter.exec("""
                        import sys
                        import time
                        sys.path.append(rutaFunciones)
                        from hashing import buscarEnHashTable,crearHashTableMedioCuadrado
                        tabla = crearHashTableMedioCuadrado(listaOriginal)
                        inicio = time.time()
                        resultado = buscarEnHashTable(tabla,clave)
                        fin = time.time()
                        print("\t* RESULTADO DE BUSQUEDA MEDIO CUADRADO *")
                        print("Posicion en el arreglo: {}".format(resultado[0]))
                        print("Clave: {}".format(resultado[1]))
                        print("Valor: {}".format(resultado[2]))
                        print("Tiempo de busqueda: {}".format(fin-inicio))
                            """);
                } catch (Exception exception) {
                    JOptionPane.showMessageDialog(null,
                            "¡Algo ha salido mal!" + exception,
                            "ERROR", 0);
                }
            }
        }
        );
    }
}
