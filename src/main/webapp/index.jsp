<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8" import="java.io.*, java.util.ArrayList, dbconn.beans.*"%>
<!DOCTYPE html>
<html>
<head>
<style>
@font-face {
    font-family: 'Pretendard-Regular';
    src: url('https://fastly.jsdelivr.net/gh/Project-Noonnu/noonfonts_2107@1.1/Pretendard-Regular.woff') format('woff');
    font-weight: 400;
    font-style: normal;
}
	*{
		margin:0 auto;
		color:white;
		font-family:Pretendard-Regular;
	}
	body{
		background-color:#1b1b1b;
		overflow-x:hidden;
	}
	#Banner{
		width:100%;
		display:flex;
		flex-wrap:nowrap;
		justify-content:space-between;
		height:500px;
	}
	#Banner button{
		margin:0px;
		width:50px;
		background-color:transparent;
		border:none;
		font-size:50px;
		font-weight:100;
	}
	#BannerImgs{
		width:100%;
		list-style:none;
		margin:0px;
		padding : 0px;
		display:flex;
		overflow:hidden;
	}
	#BannerImgs li{
		width:100%;
		height:100%;
		margin:0px;
		float:left;
		flex-shrink:0;
	}
	#BannerImgs li img{
		width:100%;
		height:500px;
	}
	.Genre{
		width:10000%;
		height:200px;
		list-style:none;
		margin : 100px;
	}
	.Genre li{
		margin : 10px;
		float : left;
		width: 200px;
		height:296px;
		margin:0px 20px;
	}
	.Genre li img{
		width:100%;
		height:100%;
		border-radius:15px;
	}
	header{
		margin: 20px;
		height:50px;
		display:flex;
		justify-content:space-between;
	}
	header *{
		margin: 0px;
	}
	header div{
	
	}
	header div *{
		width:40px;
		height:40px;
		margin-left: 20px;
	}
	header button{
		border:none;
		background-color:transparent;
		background-repeat:none;
		background-size:cover;
	}
	footer{
		width:80%;
		margin-top:200px;
		height:150px;
		padding:50px;
		padding-left:200px;
		border-top:1px rgba(0, 0, 0, 0.3) solid;
	}
	footer ul{
		margin-left:-50px;
		list-style:none;
		margin-bottom:10px;
		opacity : 0.5;
	}
	footer ul li{
		margin-left:20px;
		float:left;
	}
	footer ul li a{
		text-decoration-line:none;
	}
	footer hr{
		border-color:rgba(1, 1, 1, 0.5);
	}
	footer p{
		opacity : 0.2;
	}
	#bannerIndex{
		width:100px;
		height:20px;
		background-color:rgba(0,0,0,0.5);
		border-radius:15px;
		position:absolute;
		right:80px;
		margin-top:450px;
		text-align:center;
		color:white;
	}
	#top{
		position:fixed;
		right: 20px;
		bottom:100px;
		width:50px;
		height:50px;
		color:white;
		border:none;
		border-radius:25px;
		font-weight:bold;
		font-size:16pt;
		background-color:#4174D9;
	}
</style>
<meta charset="UTF-8">
<title>Index</title>
</head>
<body>
<jsp:useBean class="dbconn.beans.MovieDAO" id="movie" scope="session"/>
<%
	ArrayList<MovieDTO> movies = movie.selectMovieList();
	for(MovieDTO m : movie.selectMovie("select * from movieTbl where json_contains(genres, '[\"Action\"]')")){
		System.out.println(m.getTitle());
	}
%>
	<jsp:include page="header.jsp"/>
	<div id="Banner">
		<button><</button>
		<ul Id="BannerImgs">
			<li><img src="img/main.png"/></li>
			<li><img src="img/main.png"/></li>
		</ul>
		<div id="bannerIndex">
			4/4
		</div>
		<button>></button>
	</div>
	<ul class="Genre">
		<h1>액션</h1>
		<%
			for(MovieDTO m : movie.selectMovie("select * from movieTbl where json_contains(genres, '[\"Action\"]')")){
				out.write("<li><img src="+m.getPoster()+"/></li>");
			}
		%>
	</ul>
	<br>
	<ul class="Genre">
		<h1>애니메이션</h1>
		<%
			for(MovieDTO m : movie.selectMovie("select * from movieTbl where json_contains(genres, '[\"Animation\"]')")){
				out.write("<li><img src="+m.getPoster()+"/></li>");
			}
		%>
	</ul>
	<br>
	<ul class="Genre">
		<h1>판타지</h1><%
			for(MovieDTO m : movie.selectMovie("select * from movieTbl where json_contains(genres, '[\"Fantasy\"]')")){
				out.write("<li><img src="+m.getPoster()+"/></li>");
			}
		%>
	</ul>
	<br>
	<ul class="Genre">
		<h1>공상과학</h1>
		<%
			for(MovieDTO m : movie.selectMovie("select * from movieTbl where json_contains(genres, '[\"Sci-Fi\"]')")){
				out.write("<li><img src="+m.getPoster()+"/></li>");
			}
		%>
	</ul>
	<br>
	<ul class="Genre">
		<h1>범죄</h1>
		<%
			for(MovieDTO m : movie.selectMovie("select * from movieTbl where json_contains(genres, '[\"Crime\"]')")){
				out.write("<li><img src="+m.getPoster()+"/></li>");
			}
		%>
	</ul>
	<br>
	<ul class="Genre">
		<h1>스릴러</h1>
		<%
			for(MovieDTO m : movie.selectMovie("select * from movieTbl where json_contains(genres, '[\"Thriller\"]')")){
				out.write("<li><img src="+m.getPoster()+"/></li>");
			}
		%>
	</ul>
	<br>
	<ul class="Genre">
		<h1>코미디</h1>
		<%
			for(MovieDTO m : movie.selectMovie("select * from movieTbl where json_contains(genres, '[\"Comedy\"]')")){
				out.write("<li><img src="+m.getPoster()+"/></li>");
			}
		%>
	</ul>
	<br>
	<ul class="Genre">
		<h1>어드벤쳐</h1>
		<%
			for(MovieDTO m : movie.selectMovie("select * from movieTbl where json_contains(genres, '[\"Adventure\"]')")){
				out.write("<li><img src="+m.getPoster()+"/></li>");
			}
		%>
	</ul>
	<br>
	<ul class="Genre">
		<h1>로맨스</h1>
		<%
			for(MovieDTO m : movie.selectMovie("select * from movieTbl where json_contains(genres, '[\"Romance\"]')")){
				out.write("<li><img src="+m.getPoster()+"/></li>");
			}
		%>
	</ul>
	<br>
	<ul class="Genre">
		<h1>드라마</h1>
		<%
			for(MovieDTO m : movie.selectMovie("select * from movieTbl where json_contains(genres, '[\"Drama\"]')")){
				out.write("<li><img src="+m.getPoster()+"/></li>");
			}
		%>
	</ul>
	<button id="top">▴</button>
	<jsp:include page="footer.jsp"/>
</body>
</html>