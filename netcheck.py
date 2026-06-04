import subprocess,argparse,json,socket,time,sys
from rich import print_json
from datetime import datetime

def compile_entry(p1, ip_addr, port = '', port_status = 1,flask_stat = False):
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

    return entry

def print_func(entry):
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

def single_host(hostname, flask_status = False):
    save = process_run(hostname)
    if flask_status:
        entry = compile_entry(save,hostname,None,None,flask_status)
        return entry
    else:
        entry = compile_entry(save,hostname,None,None,flask_status)
        print_func(entry)

def ping_all(flask_status = False):
    content = device_file()
    list_of_entries = []
    for content in content:
        ip_name = content.strip()
        save = process_run(ip_name)
        entry = compile_entry(save,ip_name,None,None,flask_status)
        if flask_status:
            list_of_entries.append(entry)
        else:
            print_func(entry)
    if flask_status:
        return list_of_entries

def port(hostname = '',port = '',flask_status=False):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    socket_code = s.connect_ex((hostname,int(port)))
    save = process_run(hostname)
    entry = compile_entry(save,hostname,port,socket_code)
    if flask_status:
        return entry
    else:
        print_func(entry)

def watch_timer(mode ='',time_amt = 0, flask_status = False,hostname='',port=''):
    try:
        while(True):
            if mode == 'a':
                if flask_status:
                    return ping_all(True)
                else: 
                    ping_all()
            elif mode == 's':
                if flask_status:
                    return single_host(hostname,True)
                else:
                    single_host(hostname)
            elif mode == 'p':
                if flask_status:
                    return port(hostname,port,True)
                else:
                    port()
            time.sleep(int(time_amt))
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
            watch_timer('a',args.watch)
        else:
            ping_all()
            
    elif args.hostname:
        if args.port:
            if args.watch:
                watch_timer('p',args.watch,None,args.hostname,args.port)
            else:
                port(args.hostname,args.port)
        elif args.watch:
            watch_timer('s',args.watch,None,args.hostname)
        else:
            single_host(args.hostname)
    
    




    
