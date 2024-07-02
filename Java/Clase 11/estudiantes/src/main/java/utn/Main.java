package utn;

import java.sql.Connection;
import java.sql.SQLException;

public class Main {
    public static void main(String[] args) {
        Connection conexion = Conexion.getConnection();
        if (conexion != null) {
            System.out.println("Conexión exitosa: " + conexion);

            try {
                // Listar estudiantes
                EstudiantesCRUD.listEstudiantes(conexion);

                // Insertar estudiante
                EstudiantesCRUD.insertEstudiante(conexion, "Juan", "Pérez", "2604806669", "juan@gmail.com");

                // Modificar estudiante
                EstudiantesCRUD.updateEstudiante(conexion, 1, "Juana", "Mercado");

                // Eliminar estudiante
                EstudiantesCRUD.deleteEstudiante(conexion, 3);

                // Modificar AUTO_INCREMENT
                EstudiantesCRUD.alterTableAutoIncrement(conexion, 1);
            } catch (SQLException e) {
                e.printStackTrace();
            }

        } else {
            System.out.println("Error al establecer la conexión");
        }
    }
}
