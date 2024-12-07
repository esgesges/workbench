<html>
<body>
<?php
echo "<form name=\"formNome\" action=\"" . $_SERVER['PHP_SELF'] . "\" method=\"post\">";
?>
    <label> Operando 1: </label>
    <input type="text" name="op1" /> <br/>
    <label> Operando 2: </label>
    <input type="text" name="op2" /> <br/>
    <input type="submit" name="sbm" value="Invia" />
</form>

<?php
if (isset($_POST["sbm"])) {
    echo "Operazione <br/>";
    if (is_string($_POST["op1"])) {
        $op1 = (int) $_POST["op1"];
    }
    if (is_string($_POST["op2"])) {
        $op2 = (int) $_POST["op2"];
    }
    echo $op1 . " + " . $op2 . " = " . ($op1 + $op2) . "<br/>";
    echo $op1 . " - " . $op2 . " = " . ($op1 - $op2) . "<br/>";
    echo $op1 . " x " . $op2 . " = " . ($op1 * $op2) . "<br/>";
    echo $op1 . " : " . $op2 . " = " . ($op1 / $op2) . "<br/>";
}
?>
</body>
</html>
