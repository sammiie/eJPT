### **Adding static route to access other nodes connected to a gateway you are already connected to**
### **View Route table**

- **Windows**
`route print`

- **Linux**
`route` #option 1
`ip route show` #Option 2
`netstat -nr` #Option 3

_Permanently adding static route_
    Edit the file /etc/network/interfaces
    Append the following command:

        `up route add -net <destinaton_network> netmask <destination_mask> gw <gateway_address> <interface_name>`

### **Add static route to table**

- **Windows**
     `route add <destination network> mask <mask address> <gateway>`

- **Linux**
     `ip route add <destination network/mask> via <gateway>`  #CDIR is accepted

### **Remove static route**

- **Windows**
        `route delete <destination network>`

- **Linux**
        `ip route del <destination_addr> via <gateway>`

