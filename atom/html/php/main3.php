<html>
<body>
<?php
if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST["sbm"])) {
    if (is_string($_POST["op1"])) {
        $op1 = (int) $_POST["op1"];
    }
}
?>

<form name="formNome" action="<?php echo $_SERVER['PHP_SELF']; ?>" method="post">
    <label> Inserisci numero da indovinare: </label>
    <input type="text" name="op1" /> <br/>
    <input type="submit" name="sbm" value="Invia" />
</form>

<?php
if (isset($op1)) {
    echo '<form name="formTentativi" action="' . $_SERVER['PHP_SELF'] . '" method="post">';
    echo '<label> Inserisci tentativo 1: </label>';
    echo '<input type="text" name="t1" /> <br/>';
    echo '<label> Inserisci tentativo 2: </label>';
    echo '<input type="text" name="t2" /> <br/>';
    echo '<label> Inserisci tentativo 3: </label>';
    echo '<input type="text" name="t3" /> <br/>';
    echo '<input type="hidden" name="op1" value="' . $op1 . '" />';
    echo '<input type="submit" name="fin" value="Invia" />';
    echo '</form>';
}

if (isset($_POST["fin"])) {
    $op1 = (int) $_POST["op1"];
    $t1 = (int) $_POST["t1"];
    $t2 = (int) $_POST["t2"];
    $t3 = (int) $_POST["t3"];
    $risultato = $op1;

    echo "Risultati: <br/>";
    if ($t1 == $risultato || $t2 == $risultato || $t3 == $risultato) {
        echo "Hai vinto!";
    } else {
        echo "Hai perso!";
    }
    echo "<br/>Il numero da indovinare era: " . $op1;
    echo "<br/>I tuoi tentativi sono: " . $t1 . ", " . $t2 . ", " . $t3;
    echo "<br/>";
}
?>
</body>
</html>