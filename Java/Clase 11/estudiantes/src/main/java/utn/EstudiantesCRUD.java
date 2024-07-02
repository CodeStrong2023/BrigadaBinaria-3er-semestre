package utn;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class EstudiantesCRUD {
    public static void listEstudiantes(Connection connection) throws SQLException {
        String query = "SELECT * FROM estudiantes2024";
        Statement statement = connection.createStatement();
        ResultSet resultSet = statement.executeQuery(query);

        while (resultSet.next()) {
            int id = resultSet.getInt("idestudiantes2024");
            String nombre = resultSet.getString("nombre");
            String apellido = resultSet.getString("apellido");
            String telefono = resultSet.getString("telefono");
            String email = resultSet.getString("email");
            System.out.println(id + ": " + nombre + " " + apellido + " - " + telefono + " - " + email);
        }
    }

    public static void insertEstudiante(Connection connection, String nombre, String apellido, String telefono, String email) throws SQLException {
        String query = "INSERT INTO estudiantes2024 (nombre, apellido, telefono, email) VALUES (?, ?, ?, ?)";
        PreparedStatement preparedStatement = connection.prepareStatement(query);
        preparedStatement.setString(1, nombre);
        preparedStatement.setString(2, apellido);
        preparedStatement.setString(3, telefono);
        preparedStatement.setString(4, email);
        preparedStatement.executeUpdate();
        System.out.println("Estudiante insertado.");
    }

    public static void updateEstudiante(Connection connection, int id, String nombre, String apellido) throws SQLException {
        String query = "UPDATE estudiantes2024 SET nombre = ?, apellido = ? WHERE idestudiantes2024 = ?";
        PreparedStatement preparedStatement = connection.prepareStatement(query);
        preparedStatement.setString(1, nombre);
        preparedStatement.setString(2, apellido);
        preparedStatement.setInt(3, id);
        preparedStatement.executeUpdate();
        System.out.println("Estudiante actualizado.");
    }

    public static void deleteEstudiante(Connection connection, int id) throws SQLException {
        String query = "DELETE FROM estudiantes2024 WHERE idestudiantes2024 = ?";
        PreparedStatement preparedStatement = connection.prepareStatement(query);
        preparedStatement.setInt(1, id);
        preparedStatement.executeUpdate();
        System.out.println("Estudiante eliminado.");
    }

    public static void alterTableAutoIncrement(Connection connection, int startValue) throws SQLException {
        String query = "ALTER TABLE estudiantes2024 AUTO_INCREMENT = ?";
        PreparedStatement preparedStatement = connection.prepareStatement(query);
        preparedStatement.setInt(1, startValue);
        preparedStatement.executeUpdate();
        System.out.println("AUTO_INCREMENT modificado.");
    }
}
