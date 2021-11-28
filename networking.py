# Adding static route to access other nodes connected to a gateway you are already connected token

#************* view route table ********

    # windows
        `route print`

    # Linux
        # All these methods won't survive reboot
                route # option 1
                ip route show   #option 2
                netstat -nr  # option 3

        # Permanently adding static route
                Edit the file /etc/network/interfaces
                Append the following command:

                        up route add -net <destinaton_network> netmask <destination_mask> gw <gateway_address> ,<interface_name>

#******* Add static route to table *********

    # windows
        route add <destination network> mask <mask address> <gateway>

    # Linux
        ip route add <destination network/mask> via <gateway>  #CDIR is accepted

#******* Remove static route

    # windows
        route delete <destination network>

    # Linux
        ip route del <destination_addr> via <gateway>