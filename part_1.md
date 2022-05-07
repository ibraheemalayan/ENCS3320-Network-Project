# Part 1

# Ping a virtual machine bridged to the local network

![image](https://i.ibb.co/sV7f5qV/image.png)

pinging a linux virtual machine bridged to the local network ( IP `10.0.0.25` ) with 4 ICMP ECHO_REQUEST packets    
> the average RTT is 0.759 ms 

# Ping www.youtube.com

![image](https://i.ibb.co/W5GP4NL/image.png)

pinging one of youtube's servers ( IP `10.0.0.25` ) with ICMP ECHO_REQUEST packets
> the average RTT is 615.805 ms 

# Trace-route www.youtube.com

![image](https://i.ibb.co/zPRPPt0/image.png)

tracing all the routers from a virtual machine to a youtube server, the route consists of 12 hops where the first one is the local network router `10.0.0.138` and the last one is the intended youtube server `142.250.186.46`

# Nslookup www.youtube.com

![image](https://i.ibb.co/XsFQsb5/image.png)

nslookup queried available `A` and `AAA` records for **www.youtube.com** from google's DNS server ( `8.8.8.8` ), Google responded with *20* records **( 16 `A`, 4 `AAA` )** for the same host in order to provide redundancy and fallbacks and some sort of DNS level load balancing.
 



