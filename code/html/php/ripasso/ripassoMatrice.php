<!DOCTYPE html>
<html>
<head>
    <title></title>
    <style>
        table, th, td {
            border: 3px solid purple;
            border-collapse: collapse;
            text-align: center;
        }
    </style>
</head>
<body>
    <?php
         echo "
            <form action=".$_SERVER['PHP_SELF']." method=\"post\">
            Inserisci numero: <input type=\"number\" name=\"num\"><br>
            <input type=\"submit\" name=\"sub\">
            </form>
        ";
        if(isset($_POST["num"])) {
            echo "<table>";
            for($i = 0; $i < $_POST["num"]; $i++) {
                echo "<tr>";
                for($j = 1; $j <= $_POST["num"]; $j++) {
                    echo "<td>" . ($j + $i) . "</td>"; 
                }
                echo "</tr>";
            }
            echo "</table>";
        }
    ?>
</body>
</html>