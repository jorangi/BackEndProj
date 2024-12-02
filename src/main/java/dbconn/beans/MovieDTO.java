package dbconn.beans;

import java.util.ArrayList;

public class MovieDTO {
	private int rank;
	private String title;
	private String id;
	private ArrayList<ReviewDTO> reviews;
	private ArrayList<String> genres;
	private float score;
	private int numVotes;
	private int relaseYear;
	private String poster;
	private String trailer;
	public String getTitle() {
		return title;
	}
	public void setTitle(String title) {
		this.title = title;
	}
	public String getId() {
		return id;
	}
	public void setId(String id) {
		this.id = id;
	}
	public ArrayList<ReviewDTO> getReviews() {
		return reviews;
	}
	public void setReviews(ArrayList<ReviewDTO> reviews) {
		this.reviews = reviews;
	}
	public ArrayList<String> getGenres() {
		return genres;
	}
	public void setGenres(ArrayList<String> genres) {
		this.genres = genres;
	}
	public float getScore() {
		return score;
	}
	public void setScore(float score) {
		this.score = score;
	}
	public int getNumVotes() {
		return numVotes;
	}
	public void setNumVotes(int numVotes) {
		this.numVotes = numVotes;
	}
	public int getRelaseYear() {
		return relaseYear;
	}
	public void setRelaseYear(int relaseYear) {
		this.relaseYear = relaseYear;
	}
	public int getRank() {
		return rank;
	}
	public void setRank(int rank) {
		this.rank = rank;
	}
	public String getPoster() {
		return poster;
	}
	public void setPoster(String poster) {
		this.poster = poster;
	}
	public String getTrailer() {
		return trailer;
	}
	public void setTrailer(String trailer) {
		this.trailer = trailer;
	}
}
