import re

log_path='setupapi.dev2.log'
usb_devices={
    'device_vendor_id':[],
    'device_product_id':[],
    'device_instance_id':[],
    'event_time':[]
}
reg_ex=r'^>>>  \[Device Install.*#(Disk&Ven_[A-Za-z0-9]+)&(Prod_([\w\s\S]+?))&(Rev_([\w\s\S]+?))#([\w\s\S]+?)#.*\]'

with open(log_path, "r") as log_file:

     for line in log_file:
        line_text=next(log_file)
        match=re.search(reg_ex,line)
        if(match != None):
            event_time=line_text.split("start ")[1].strip()
            usb_devices["device_vendor_id"].append(match.groups()[0])
            usb_devices["device_product_id"].append(match.groups()[1])
            usb_devices["device_instance_id"].append(match.groups()[2])
            usb_devices["event_time"].append(event_time)
