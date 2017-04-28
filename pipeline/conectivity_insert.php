<?php

if( $_POST )
{
  $con = mysql_connect("localhost","root","root");

  if (!$con)
  {
    die('Could not connect: ' . mysql_error());
  }

  mysql_select_db("testdb", $con);

  $users_name = $_POST['Username'];
  $users_email = $_POST['Password'];

  $users_name = mysql_real_escape_string($users_name);
  $users_email = mysql_real_escape_string($users_email);


  $query = "INSERT INTO details VALUES ('$users_name', '$users_email');";


  mysql_query($query);

/*  echo "<h2>Account Created!</h2>";*/



echo '
        <script type="text/javascript">
            alert("Account Created!"); 
            window.location.href = "login.html";</script>'; 
  mysql_close($con);
}

?>
