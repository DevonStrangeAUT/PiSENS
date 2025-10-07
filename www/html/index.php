    <?php
        
$script = __DIR__ . DIRECTORY_SEPARATOR . "PiSENS/argumentParser.py";
exec("python $script temperature 2>&1", $out, $status);
        
        
        if(array_key_exists('save_button', $_POST)) {
            button1();
        }
        function button1() {
        
            $script = __DIR__ . DIRECTORY_SEPARATOR . "PiSENS/argumentParser.py";
            exec("python $script temperature 2>&1", $out, $status);
            
            $servername = "localhost";
            $username = "fynn";
            $password = "miloandsprinkles";
            $dbname = "pisens";
            // Create connection
            $conn = new mysqli($servername, $username, $password, $dbname);
            // Check connection
            if ($conn->connect_error) {
              die("Connection failed: " . $conn->connect_error);
            }

            $sql = "INSERT INTO temperature (value) VALUES (" . $out[0] . ")";
            echo $sql;
            $result = $conn->query($sql);

            $conn->close();
            
            
            
        }
    ?>



<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>HTML 5 Boilerplate</title>
    <link rel="stylesheet" href="styles.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">


</head>
<body>

<div>
    <div class="row">
        <div class="col-sm-2">
            <ul class="nav flex-column">

                <li class="nav-item">
                    <a class="nav-link" aria-current="page" href="/">Home Page</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" aria-current="page" href="/temperature.php">Temperature History</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" aria-current="page" href="/humidity.php">Humidity History</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" aria-current="page" href="#">Forecast History</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" aria-current="page" href="#">Pressure History</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" aria-current="page" href="#">Temperature History</a>
                </li>
            </ul>
        </div>
        <div class="col-sm-10">
            <h1 class="text-center">
                PiSENS: Pi Interactive Sensing Environment Notification System
            </h1>
            <div class="container text-center">
                <div class="row">
                    <div class="col">
                        <div class="readingCards card">
                            <div class="card-body">
                                <h5 class="card-title">Temperature</h5>
                                
<?php 

echo $out[0];

?>

                            </div>
                        </div>
                    </div>
                    <div class="col">
                        <div class="readingCards card">
                            <div class="card-body">
                                <h5 class="card-title">Humidity</h5>
                                <div class="card" style="width: 18rem;">
                                    <ul class="list-group list-group-flush">
                                        <li class="list-group-item text-left">Local: 
                                        
                                        <?php 

$script1 = __DIR__ . DIRECTORY_SEPARATOR . "PiSENS/argumentParser.py";
exec("python $script humidity", $out1, $status1);
echo $out1[0];

?>
                                        
                                        </li>
                                        <li class="list-group-item">Regional (Remote API Call): 
                                        
                                        
                                        
                                        <?php
                                        
                                        $response = file_get_contents('https://api.open-meteo.com/v1/forecast?latitude=-36.848461&longitude=174.763336&current=temperature_2m,relative_humidity_2m,apparent_temperature,is_day,wind_speed_10m,wind_direction_10m,wind_gusts_10m,precipitation,rain,showers,snowfall,weather_code,cloud_cover,pressure_msl,surface_pressure&timezone=auto');
                       
                                        $response = json_decode($response);
                                        echo $response->current->relative_humidity_2m;
                                        ?>
                                        
                                        </li>
                                        <li class="list-group-item">International</li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="row mt-4">
                    <div class="col">
                        <div class="readingCards card">
                            <div class="card-body">
                                Forecast
                            </div>
                        </div>
                    </div>
                    <div class="col">
                        <div class="readingCards card">
                            <div class="card-body">
                                Pressure
                                
                                <?php 

$script2 = __DIR__ . DIRECTORY_SEPARATOR . "PiSENS/argumentParser.py";
exec("python $script pressure", $out2, $status2);
echo $out2[0];

?>
                                
                                
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="mt-4">
                    <form method="POST">
                        <input type="hidden" value="<?php echo $out[0]; ?>" name="temperature"> </input>
                       <button class="btn btn-primary btn-lg" type="submit" name="save_button" value="1">Save</button>
                   </form>
                </div>

            </div>
        </div>
    </div>
</div>




<script src="index.js"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js" integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI" crossorigin="anonymous"></script>

</body>
</html>
