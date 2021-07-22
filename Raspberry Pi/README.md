<hmtl>
<head>
</head>
<body>
    <h1>Raspberry Pi programs</h1>
    <p>Here can be found the codes that will program the Raspberry Pi.</p><hr><br>
    <h2>Prerequisites:</h2>
    <p>Make sure to have the Raspberry Pi OS <a href="https://www.raspberrypi.org/software/" target="_blank">Raspbian </a> installed on your Pi.</p><br>
    <h2>direct-car.py</h2>
    <p>This program communicates with the Apache server hosted on the Pi. The function <a href="https://www.php.net/manual/en/function.shell-exec.php" target="_blank">shell_exec</a> grabs a string command that will be directly executed on the Terminal of the Raspberry Pi to control the RC car. The command that it executes is a python program, <u>direct-car.py <u> which controls the GPIO pins of the Pi.</p><br>
    <h2>Command-listener.py</h2>
    <p>This program is very similar to <u>direct-car.py</u>, except that it allows us to control the RC car directly from the Terminal of the Pi instead of having to use the Apache server. To make this possible, SSH into your Raspberry Pi using the following command in the terminal of your computer:</p><br>
    ```ssh username@raspberry-pi-ip-address ```
    <br><p>and then enter you password. Detailed steps can be found at https://www.raspberrypi.org/documentation/remote-access/ssh/</p>
</body>
</html>
