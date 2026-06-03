# netcheck

This is a very simple netcheck portfolio project.

Overview:
The python script is able to ping a connection with a in or out of local network device. You can ping a list of devices, or through the command line can specify a device by its host-name or IP-Address. You are able to ping a port on a single device. The watch function allows the program to run in a continous state at the user defined intervals.

Note: It runs only on linux. 

Installation:
     1.Download Repository Files
     2.First install rich
        - In command line type
            ```bash
            pip install -r requirements.txt
            ```
    3.Run in local linux directory

Demo:
    Example 1:
    1.1 In command line type
        ```bash
        python3 ./netcheck.py -r 127.0.0.1
        ```
    1.2 Output
    ```json
    {
        "hostname": "127.0.0.1",
        "status": true,
        "time_stamp": "02/06/26 20:55:09"
    }
    ```
    Example 2:
    2.1 In command line type
        ```bash
        python3 ./netcheck.py -a all
        ```
    2.2 Output
    ```json
    {
        "hostname": "127.0.0.1",
        "status": true,
        "time_stamp": "02/06/26 21:02:51"
    }
    {
        "hostname": "172.24.80.1",
        "status": true,
        "time_stamp": "02/06/26 21:02:54"
    }
    {
        "hostname": "172.24.95.59",
        "status": true,
        "time_stamp": "02/06/26 21:02:57"
    }
    {
        "hostname": "199.0.18.18",
        "status": false,
        "time_stamp": "02/06/26 21:03:10"
    }
    ```

    Example 3:
    3.1 In command line type
    ```bash
    python3 ./netcheck.py -r 127.0.0.1 -p 22
    ```
    3.2 Output
    ```json
    {
        "hostname": "127.0.0.1",
        "status": true,
        "time_stamp": "02/06/26 21:05:11",
        "Port": "22",
        "port status": false
    }
    ```


Commandline arguments:
    -h, --help        show this help message in terminal and exits
    -r , --hostname   ip-address or hostname
    -a , --all        Pings all devices
    -p , --port       Pings a port on a single host
    -w , --watch      Pings the devices every set second
    
    note: There must more than 1 command line argument
        *   -r or -a are mandatory arguments
        *   -p only works with the -r arguments
        *   -p and -w are optional arguments
        *   -w works on both mandatory arguments
        *   -w in order to stop the program press the button combination Ctrl+C