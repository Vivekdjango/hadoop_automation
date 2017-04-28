<?php
session_set_cookie_params(0);
session_start();
if(session_destroy())
{
header("Location: login.html");
}
session_destroy();
?>
