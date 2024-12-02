package dbconn.beans;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.Arrays;
import org.json.JSONArray;

public class MovieDAO {
	public void insertMovie(MovieDTO movie) {
		try {
			PreparedStatement stmt = DBConnDAO.getStmt("insert into movieTbl values(?, ?, ?, ?, ?, ?, ?);");
			stmt.setInt(1, movie.getRank());
			stmt.setString(2, movie.getId());
			stmt.setString(3, movie.getTitle());
			String genres = "";
			for(int i = 0; i < movie.getGenres().size(); i++) {
				genres += movie.getGenres().get(i);
				if(i < movie.getGenres().size() - 1)
					genres += ", ";
			}
			stmt.setString(4, genres);
			stmt.setDouble(5, movie.getScore());
			stmt.setInt(6, movie.getNumVotes());
			stmt.setInt(7, movie.getRelaseYear());
			stmt.executeUpdate();
		}catch(SQLException e) {
			e.printStackTrace();
		}finally {
			DBConnDAO.dbClose();
		}
	}
	public void updateMovie(MovieDTO movie) {
		try {
			PreparedStatement stmt = DBConnDAO.getStmt("insert into movieTbl values(?, ?, ?, ?, ?, ?, ?);");
			stmt.setInt(1, movie.getRank());
			stmt.setString(2, movie.getId());
			stmt.setString(3, movie.getTitle());
			String genres = "";
			for(int i = 0; i < movie.getGenres().size(); i++) {
				genres += movie.getGenres().get(i);
				if(i < movie.getGenres().size() - 1)
					genres += ", ";
			}
			stmt.setString(4, genres);
			stmt.setDouble(5, movie.getScore());
			stmt.setInt(6, movie.getNumVotes());
			stmt.setInt(7, movie.getRelaseYear());
			stmt.executeUpdate();
		}catch(SQLException e) {
			e.printStackTrace();
		}finally {
			DBConnDAO.dbClose();
		}
	}
	public ArrayList<MovieDTO> selectMovieList(){
		ResultSet rs = null;
		ResultSet movieTitle_rs = null;
		ResultSet review_rs = null;
		ArrayList<MovieDTO> aList = new ArrayList<MovieDTO>();
		try {
			PreparedStatement stmt = DBConnDAO.getConn().prepareStatement("select * from movieTbl");
			rs = stmt.executeQuery();
			while(rs.next()) {
				MovieDTO movie = new MovieDTO();
				movie.setRank(rs.getInt("rank"));
				movie.setId(rs.getString("id"));
				PreparedStatement title_stmt = DBConnDAO.getConn().prepareStatement("select * from movieTitleTbl where id = ?");
				title_stmt.setString(1, movie.getId());
				movieTitle_rs = title_stmt.executeQuery();
				movieTitle_rs.next();
				movie.setTitle(movieTitle_rs.getString("title"));
				JSONArray genresJson = new JSONArray(rs.getString("genres"));
				ArrayList<String> genres = new ArrayList<String>();
				for(int i = 0; i < genresJson.length(); i++) genres.add(genresJson.getString(i));
				movie.setGenres(genres);
				movie.setScore(rs.getFloat("score"));
				movie.setNumVotes(rs.getInt("numVotes"));
				movie.setRelaseYear(rs.getInt("releaseYear"));
				movie.setPoster(rs.getString("poster"));
				movie.setTrailer(rs.getString("trailer"));
				ArrayList<ReviewDTO> reviews = new ArrayList<ReviewDTO>();
				PreparedStatement review_stmt = DBConnDAO.getConn().prepareStatement("select * from reviewTbl where movieId = ?");
				review_stmt.setString(1, movie.getId());
				review_rs = review_stmt.executeQuery();
				while(review_rs.next()) {
					ReviewDTO review = new ReviewDTO();
					review.setName(review_rs.getString("name"));
					review.setTitle(review_rs.getString("title"));
					review.setText(review_rs.getString("text"));
					review.setScore(review_rs.getInt("score"));
					review.setDate(review_rs.getString("date"));
					review.setImg(review_rs.getString("link"));
					review.setId(review_rs.getString("id"));
					review.setMovieId(movie.getId());
					reviews.add(review);
				}
				movie.setReviews(reviews);
				aList.add(movie);
			}
		}catch(Exception e) {
			e.printStackTrace();
		}
		return aList;
	}
	public ArrayList<MovieDTO> selectMovie(String sql){
		ResultSet rs = null;
		ResultSet movieTitle_rs = null;
		ResultSet review_rs = null;
		ArrayList<MovieDTO> aList = new ArrayList<MovieDTO>();
		try {
			PreparedStatement stmt = DBConnDAO.getConn().prepareStatement(sql);
			rs = stmt.executeQuery();
			while(rs.next()) {
				MovieDTO movie = new MovieDTO();
				movie.setRank(rs.getInt("rank"));
				movie.setId(rs.getString("id"));
				PreparedStatement title_stmt = DBConnDAO.getConn().prepareStatement("select * from movieTitleTbl where id = ?");
				title_stmt.setString(1, movie.getId());
				movieTitle_rs = title_stmt.executeQuery();
				movieTitle_rs.next();
				movie.setTitle(rs.getString("title"));
				ArrayList<String> genres = new ArrayList<String>(Arrays.asList(rs.getString("genres").split(", ")));
				movie.setGenres(genres);
				movie.setScore(rs.getFloat("score"));
				movie.setNumVotes(rs.getInt("numVotes"));
				movie.setRelaseYear(rs.getInt("releaseYear"));
				movie.setPoster(rs.getString("poster"));
				movie.setTrailer(rs.getString("trailer"));
				ArrayList<ReviewDTO> reviews = new ArrayList<ReviewDTO>();
				PreparedStatement review_stmt = DBConnDAO.getConn().prepareStatement("select * from reviewTbl where id = ?");
				review_stmt.setString(1, movie.getId());
				review_rs = review_stmt.executeQuery();
				while(review_rs.next()) {
					ReviewDTO review = new ReviewDTO();
					review.setName(review_rs.getString("name"));
					review.setTitle(review_rs.getString("title"));
					review.setText(review_rs.getString("text"));
					review.setScore(review_rs.getInt("score"));
					review.setDate(review_rs.getString("date"));
					review.setImg(review_rs.getString("link"));
					review.setId(review_rs.getString("id"));
					reviews.add(review);
				}
				movie.setReviews(reviews);
				aList.add(movie);
			}
		}catch(Exception e) {
			e.printStackTrace();
		}
		return aList;
	}
}
