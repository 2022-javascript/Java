<?php
include_once("connect.php");

$name=$_POST["name"];
$password=$_POST["password"];
$date=$_POST["date"];

$sql="INSERT INTO sds (name,password,date)VALUES('$name','$password','$date')";

if($conn->query($sql))echo "<h3>로그인 성공</h3>";
else echo "<h3>로그인 실패</h3>";

?>