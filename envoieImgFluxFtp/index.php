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
            max-width: 30%;
          }
        </style>
    </head>

    <body>
      <h1>Des moches.</h1>

      <p>
        <?php
        $fichiers = glob('img/*.jpg');
        foreach($fichiers as $i){
          echo "<img class=\"img\" src=\"" . $i . "\">";
        }
        ?>
      </p>
    </body>
</html>
