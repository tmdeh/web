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
if (isset($_REQUEST['op'])) {
	$op = $_REQUEST['op'];
}else{
	$op = 'add';
}
?>
<!doctype html>
<html lang="ko">
	<head>
		<meta charset="utf-8" />
	</head>
	<body>
		<form method="GET">
			<input type="number" name="a" value="<?=$_REQUEST['a']?>">
			<select name="op">
<?php
$arr = array(
	array('add', '+'), 
	array('sub', '-'), 
	array('mul', 'x'), 
	array('div', '/')
	);
//for ($i = 0; $i < $arr.count(); $i++)
foreach ($arr as &$it) {
?>
	<option value="<?=$it[0]?>" <?php if ($op == $it[0]) echo "selected"; ?>><?=$it[1]?></option>
<?php
}
?>
			</select>
			<input type="number" name="b" value="<?=$_REQUEST['b']?>">
			<input type="submit" value="怨꾩궛�섍린">
			<input type="reset" value="珥덇린��">
		</form>
		<div>
			寃곌낵: 
<?php

/*
print_r: 諛곗뿴 �� 媛앹껜�� �뺣낫瑜� 異쒕젰�댁쨲

// GET �붿껌�쇰줈 �ㅼ뼱�� 蹂���
print_r($_GET);

// POST �붿껌�쇰줈 �ㅼ뼱�� 蹂���
print_r($_POST);

// GET, POST �붿껌 諛� COOKIE 媛� �⑹퀜�덉쓬
print_r($_REQUEST);
*/

// 蹂��섍� �뺤쓽�섏뼱 �덈뒗吏� �뺤씤
if (isset($_REQUEST['a'])) {
	// 臾몄옄�댁쓣 �レ옄�뺤쑝濡� 蹂���
	$a = (int)$_REQUEST['a'];
	$b = (int)$_REQUEST['b'];
	$op = $_REQUEST['op'];
	
	if ($op == 'add') {
		$result = $a + $b;
	}else if ($op == 'sub') {
		$result = $a - $b;
	}else if ($op == 'mul') {
		$result = $a * $b;
	}else if ($op == 'div') {
		$result = $a / $b;
	}
	
	echo $result;
}else{
	echo "怨꾩궛�섍린 踰꾪듉�� �뚮윭二쇱꽭��.";
}
?>
<!--

/*
print_r: 諛곗뿴 �� 媛앹껜�� �뺣낫瑜� 異쒕젰�댁쨲

// GET �붿껌�쇰줈 �ㅼ뼱�� 蹂���
print_r($_GET);

// POST �붿껌�쇰줈 �ㅼ뼱�� 蹂���
print_r($_POST);

// GET, POST �붿껌 諛� COOKIE 媛� �⑹퀜�덉쓬
print_r($_REQUEST);
*/

// 蹂��섍� �뺤쓽�섏뼱 �덈뒗吏� �뺤씤
if (isset($_REQUEST['a'])) {
	// 臾몄옄�댁쓣 �レ옄�뺤쑝濡� 蹂���
	$a = (int)$_REQUEST['a'];
	
	//TODO: �섎㉧吏� 肄붾뱶 �묒꽦
}

		</div>
	</body>
</html>