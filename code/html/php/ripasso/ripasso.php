<!DOCTYPE html>
<html>
    <body>
        <?php
        $mesi=array("gennaio"=>"1", "febbraio"=>"2", "marzo"=>"3", "aprile"=>"4", "maggio"=>"5", "giugno"=>"6", "luglio"=>"7", "agosto"=>"8", "settembre"=>"9", "ottobre"=>"10", "novembre"=>"11", "dicembre"=>"12");
        foreach($mesi as $x=>$x_value)
        {
            if($_POST["num"] == $x_value){
                echo "Il mese è ". $x . "<br>";
            }

        }
        ?>
    </body>
</html>