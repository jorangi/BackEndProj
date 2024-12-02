package dbconn.beans;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class DBConnDAO {
	private static Connection conn = null;
	private static String jdbcDriver = "jdbc:mysql://localhost:3306/BPDB?serverTimezone=UTC&useSSL=false&useUnicode=true&characterEncoding=utf-8";
	private static String dbUser = "root";
	private static String dbPass = "12345678";
	private static PreparedStatement stmt = null; 
	
	public static String checkConn() {
		if(conn == null)
			return "Null";
		else
			return "Exist";
	}
	private static void dbConnect() {
		System.out.println("DBConnect");
		try {
			Class.forName("com.mysql.cj.jdbc.Driver");
			conn = DriverManager.getConnection(jdbcDriver, dbUser, dbPass);
		}catch(ClassNotFoundException e) {
			System.out.println("Class Error");
			e.printStackTrace();
		} catch (SQLException e) {
			System.out.println("SQLError");
			e.printStackTrace();
		}
	}
	public static Connection getConn() {
		if(conn == null) dbConnect();
		return conn;
	}
	public static PreparedStatement getStmt(String sql) {
		if(conn == null) dbConnect();
		try {
			stmt = DBConnDAO.conn.prepareStatement(sql);
			return stmt;
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			return null;
		}
	}
	public static void dbClose() {
		try {
			conn.close();
			stmt.close();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}		
	}
}
