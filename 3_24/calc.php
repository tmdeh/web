<!doctype html>
<html lang="ko">
	<head>
		<meta charset="utf-8" />
	</head>
	<body>
		<form method="GET">
			<input type="number" name="a" value="<?php=$_REQUEST['a'];?>">
			<select name="op">
				<option value="add">+</option>
				<option value="sub" selected>-</option>
				<option value="mul">x</option>
				<option value="div">/</option>
			</select>
			<input type="number" name="b" value="<?php=$_REQUEST['b'];?>">
			<input type="submit" value="계산하기">
			<input type="reset" value="초기화">
		</form>
		<div>
			결과: 
<!-- /*
print_r: 배열 등 객체의 정보를 출력해줌

// GET 요청으로 들어온 변수
print_r($_GET);

// POST 요청으로 들어온 변수
print_r($_POST);

// GET, POST 요청 및 COOKIE 가 합쳐있음
print_r($_REQUEST);
*/ -->

<?php
// 변수가 정의되어 있는지 확인
if (isset($_REQUEST['a'])) {
	// 문자열을 숫자형으로 변환
	$a = (int)$_REQUEST['a'];
    $b = (int)$_REQUEST['b'];
	$op = (int)$_REQUEST['op'];

    if($op == 'add') {
        $result = $a + $b;
        echo $result;
    }
    else if($op == 'sub') {
        $result = $a - $b;
    }
    else if($op == 'mul') {
        $result = $a * $b;
    }
    else if($op == 'div') {
        $result = $a / $b;
    }
    echo $result;
	//TODO: 나머지 코드 작성
}
else {
    echo "계산하기 버튼을 눌러주세요";
}
?>

		</div>
	</body>
</html>