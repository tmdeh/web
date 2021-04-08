<?php
// 세션 시작
session_start();
// 서버 연결 / 서버주소, 아이디, 비밀번호, DB이름
$mysqli = new mysqli('localhost', '아이디', '비밀번호', 'DB주소');
if (mysqli_connect_error()) {
    exit('Connect Error');
}

// 쿼리 실행
$cursor = $mysqli->query("SELECT * FROM `users` WHERE user_id = '" . $id . "' AND user_pw = '" . $pw . "';");
// SELECT * FROM `users` WHERE user_id = 'admin' AND user_pw = '1234';"

if ($cursor->num_rows > 0) {
    // DB에서 한개 이상 결과가 나온다면 로그인 성공
    
    // 결과 행을 가져옴
    $row = $cursor->fetch_assoc();
    
    // 세션 이름에 pk값 저장
    $_SESSION['name'] = $row['pk'];
    
    // 원래 페이지로 이동
    header("Location: ./index.php");
}else{
	// 비밀번호가 맞지 않다면 오류 표시 후 뒤로가기
?>
	<script>
		alert("비밀번호가 올바르지 않습니다.");
		// 뒤로가기
		history.back();
	</script>
<?php
}
?>