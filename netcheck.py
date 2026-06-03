import subprocess,argparse,json,datetime,socket,time,sys
from rich import print_json
from datetime import datetime

def print_func(p1, ip_addr, port = '', port_status = 1,flask_stat = ''):
    stime = datetime.now().strftime('%d/%m/%y %H:%M:%S')
    if p1.returncode == 0:
        entry = {'hostname':ip_addr,'status':True,'time_stamp':stime}
    else:
        entry = {'hostname':ip_addr,'status':False,'time_stamp':stime}

    if port:
        entry['Port'] = port
        if port_status == 0:
            entry['port status'] = True
        else:
            entry['port status'] = False
    if flask_stat:
        return entry
        
    print_json(json.dumps(entry,indent = 4))
    with open('logs.txt','a') as file:
            json.dump(entry,file,indent = 4)
    
        

def process_run(content):
    p1 = subprocess.run(['ping','-c','4', content],capture_output = True)
    return p1

def device_file():
    with open("devices.txt", "r") as file:
        content = file.readlines()
    return content

def single_host(hostname, flask_status = ''):
    save = process_run(hostname)
    if flask_status:
        save = print_func(save,hostname,None,None,flask_status)
        return save
    else:
         print_func(save,hostname)

def all():
    content = device_file()
    for content in content:
        ip_name = content.strip()
        save = process_run(ip_name)
        print_func(save,ip_name)

def port():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    socket_code = s.connect_ex((args.hostname,int(args.port)))
    save = process_run(args.hostname)
    print_func(save,args.hostname,args.port,socket_code)

def watch_timer(mode =''):
    try:
        while(True):
            if mode == 'a':
                all()
            elif mode == 's':
                single_host()
            elif mode == 'p':
                port()
            time.sleep(int(args.watch))
    except KeyboardInterrupt:
        print("Stopping Program")


    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Pings the connection of a device' )
    parser.add_argument('-r','--hostname',metavar= '', help='ip-address or hostname')
    parser.add_argument('-a','--all', metavar= '', help='Pings all devices')
    parser.add_argument('-p','--port',metavar= '', help ='Pings a port')
    parser.add_argument('-w','--watch',metavar= '', help= 'Pings the devices every set second')
    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()

    if args.all:
        if args.watch:
            watch_timer('a')
        else:
            all()
            
    elif args.hostname:
        if args.port:
            if args.watch:
                watch_timer('p')
            else:
                port()
        elif args.watch:
            watch_timer('s')
        else:
            single_host(args.hostname)
    
    




    
