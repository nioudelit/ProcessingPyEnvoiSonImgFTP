<!doctype html>
<html>
    <head>
        <meta charset="utf-8"/>
        <title>Galerie img générées</title>
        <style>
        body{
          font-family: Helvetica, sans-serif;
          text-align: center;
          margin: 0 auto;
        }
          .img{
            margin: 1em;
          }
        </style>
    </head>

    <body>
      <h1>Galerie des images générées avec Processing.</h1>
      <p>
        <h2>Sons</h2>
        <?php
        $fichiers = glob('son/*.wav');
        foreach($fichiers as $j){
          echo "<audio controls>";
          echo "<source src=\"" . $j . "\">" . "</audio>";
        }
        ?>
      </p>

      <p>
        <h2>Images</h2>
        <?php
        $fichiers = glob('img/*.png');
        foreach($fichiers as $i){
          echo "<img class=\"img\" src=\"" . $i . "\">";
        }
        ?>
      </p>
    </body>
</html>
