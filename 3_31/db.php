<?php
// 서버 연결 / 서버주소, 아이디, 비밀번호, DB이름
$mysqli = new mysqli('localhost', 's2000', '20002000', 's2000');
if (mysqli_connect_error()) {
    exit('Connect Error');
}

// 쿼리 실행
$cursor = $mysqli->query("SELECT * FROM `users` WHERE 1=1");

// SELECT 구문일 경우 가져온 행 갯수
echo $cursor->num_rows;
echo "<br>";

// 결과 1개 가져오기
//$row = $cursor->fetch_assoc();

// 결과 전부 가져오기
while ($row = $cursor->fetch_assoc()) {
    //print_r($row);
    echo $row['user_id'] . ": " . $row['user_pw'];
    echo "<br>";
}
?>