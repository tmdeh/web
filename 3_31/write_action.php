<?php

$content = $_POST['content'];

// 파일을 열어서
//fopen(파일 경로, 모드)
// 모드: Read / Write / Append
$file = fopen('./content.txt', 'w');

// 파일 안에 내용 기록
//fwrite(fopen으로 열어둔 파일 핸들러, 파일에 입력할 내용);
fwrite($file, $content);

// 파일 핸들러를 닫기
fclose($file);

// 파일에 내용을 썼으니 원래 페이지로 돌아가기
header('Location: ./write.php');
?>