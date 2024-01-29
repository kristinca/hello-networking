"""
My notes and work from the book 'Introduction to Networking' by Charles Severance


1. Introduction
1.1 Communicating at a Distance
1.2 Computers Communicate Differently
1.4 Packets and Routers
    - packets = pieces of messsages
    - “Interface Message Processors” or “IMPs”
        * acted as the interface between general-purpose computers and the rest of the network
        * later these computers dedicated to communications were called “routers”
            ** their purpose was to route the packets they received towards their ultimate destination
    - When a long message was split into much smaller packets and each packet was sent individually
      the source and destination addresses had to be added to each packet,
      so that routers could choose the best path to forward each packet of the message
    - In addition to the source and destination addresses, it was also necessary
      to add data to each packet indicating the “offset” or position of the packet
      in the overall message so that the receiving computer could put the packets back together
      in the right order to reconstruct the original message
1.6 Putting It All Together
    - The core of the Internet is a set of cooperating routers that move packets
      from many sources to many destinations at the same time
    - Each computer or local area network is connected to a router
      that forwards the traffic from its location to the various destinations on the Internet
    - The term “Internet” comes from the idea of “internetworking”
      which captures the idea of connecting many networks together
    - Our computers connect to local networks and the Internet connects
      the local networks together so all of our computers can talk to each other
1.7 Glossary
    - address: A number that is assigned to a computer so that messages can be routed to the computer
    - hop: A single physical network connection
        * A packet on the Internet will typically make several “hops” 
          to get from its source computer to its destination
    - LAN: Local Area Network
        * A network covering an area that is limited by the ability for an organization
          to run wires or the power of a radio transmitter
    - leased line: An “always up” connection that an organization leased
                   from a telephone company or other utility to send data across longer distances
    - packet: A limited-size fragment of a large message
        * Large messages or files are split into many packets and sent across the Internet
        * The typical maximum packet size is between 1000 and 3000 characters
    - router: A specialized computer that is designed to receive incoming packets on many links
              and quickly forward the packets on the best outbound link to speed the packet to its destination
    - store-and-forward network: A network where data is sent from one computer to another
                                 with the message being stored for relatively long periods of time in an intermediate computer
                                 waiting for an outbound network connection to become available
    - WAN: Wide Area Network. A network that covers longer distances, up to sending data completely around the world
        * A WAN is generally constructed using communication links owned and managed by a number of different organizations

2. Network Architecture
    - The Four-Layer TCP/IP Model
        _______________________
        |                     |
        |     Application     |
        |_____________________|
        |                     |
        |      Transport      |
        |_____________________|
        |                     |
        |    Internetwork     |
        |_____________________|
        |                     |
        |        Link         |
        |_____________________|

        * Link
            ** deals with the wired or wireless connection from your computer to the local area network
        * Internetwork
            ** Internet Protocol (IP) used to implement the Internetwork layer
        * Transport
            ** Transport Control Protocol (TCP) is used to implement the Transport layer
        * Application
            ** what we as end users interact with
            ** example: web browser
2.1 The Link Layer
    - responsible for connecting your computer to its local network and moving the data across a single hop
    - most common Link layer technology today: wireless networking
    - link layer technologies are often shared amongst multiple computers at the same location
    - the Link layer needs to solve two basic problems when dealing with these shared local area networks
        * how to encode and send data across the link
            ** wireless: which radio frequencies are to be used to transmit data 
               and how the digital data is to be encoded in the radio signal
            ** wired connections: what voltage to use on the wire and how fast to send the bits across the wire
            ** fiber optics: frequencies of light to be used and how fast to send the data
    - how does a computer know if other computers want to send data at the same time?
        * “Carrier Sense Multiple Access with Collision Detection” (CSMA/CD)
          ** When your computer wants to send data, 
             it first listens to see if another computer is already sending data on the network
          ** If no other computer is sending data, your computer starts sending its data
          ** if two computers started sending at about the same time, the data collides,
             and your computer does not receive its own data
          ** the two computers that collided wait different lengths of time
             to retry their transmissions to reduce the chances of a second collision
          ** CSMA transmits data across a single link that ranges in distance from a few meters to as long as hundreds of kilometers
          ** to move data greater distances
              *** send packets through multiple routers connected by multiple link layers
              *** each time our packet passes through another link layer from one router to another we call it a “hop”

2.2 The Internetwork Layer (IP)
    - Once your packet destined for the Internet makes it across the first link, it will be in a router
    - the router makes its best guess as to how to get your packet closer to its destination
    - When the packet reaches the last link in its journey, the link layer knows exactly where to send your packet
    - sometimes things go wrong and packets are lost

2.3 The Transport Layer (TCP)
    - The Internetwork layer looks at a packet's destination address 
      and finds a path across multiple network hops to deliver the packet to the destination computer
    - The sending computer must store a copy of the parts of the original message
      that have been sent until the destination computer acknowledges successful receipt of the packets
    - The amount of data that the source computer sends before waiting for an acknowledgement is called the "window size"
    - when the network has high-speed connections and is lightly loaded the data will be sent quickly

2.4 The Application Layer
    - the World Wide Web application was developed by scientists at the CERN
    - Today the web is the most common network application in use around the world
    - server: runs on the destination computer and waits for incoming networking connections
    - client: runs on the source computer
    - browsing the web using software like Firefox, Chrome, or Internet Explorer,
      you are running a “web client” application which is making connections to web servers
      and displaying the pages and documents stored on those web servers
    - The Uniform Resource Locators (URLs) that your web browser shows in its address bar
      are the web servers that your client is contacting to retrieve documents for you to view
    - When we develop the server half and the client half of a networked application,
      we must also define an “application protocol” that describes how the two halves of the application
      will exchange messages over the network
    - The protocols used for each application are quite different
      and specialized to meet the needs of the particular application

2.5 Stacking the Layers
    - from bottom to top layers: 
        * Link
        * Internetwork
        * Transport
        * Application
    - All four layers run in your computer where you run the client application (like a browser),
      and all four layers also run in the destination computer where the application server is running.
    - You as the end user interact with the applications that make up the top layer of the stack,
      and the bottom layer represents the WiFi, cellular, or wired connection between your computer and the rest of the Internet
    - Routers operate at the Internetwork and Link layers
    - The Transport and Application layers only come into play after
      the Internetwork layer delivers your packets to the destination computer
    - If you wanted to write your own networked application, you would likely only talk to the Transport layer
      and be completely unconcerned about the Internetwork and Link layers
    - They are essential to the function of the Transport layer, but as you write your program,
      you do not need to be aware of any of the lower-layer details.

2.6 Glossary
  - client: In a networked application, the client application is the one that requests services or initiates connections
  - fiber optic: A data transmission technology that encodes data using light and
                sends the light down a very long strand of thin glass or plastic. Fiber optic connections are fast
                and can cover very long distances
  - offset: The relative position of a packet within an overall message or stream of data
  - server: In a networked application, the server application is the one that responds 
            to requests for services or waits for incoming connections
  - window size: The amount of data that the sending computer is allowed to send before waiting for an acknowledgement

  
3. Link Layer
  - Often the Link layer transmits data using a wire, a fiber optic cable, or a radio signal
  - transmitting data:
    * about 1 km: Wired Ethernet, WiFi, and the cellular phone network
    * up to thousands of kilometers: fiber optics
    * long distances: satelites
  - Regardless of the distance we can send the data, it is still traveling over a single link

3.1 Sharing the Air
  - WiFi: laptop or phone is sending and receiving data with a small, low-powered radio
  - PC sends packets to the router, which forwards the packets using a link to the rest of the net
  - the first router that handles packets: base station or gateway
  - all the computers within range can hear all packets
  - WiFis have unique serial number at the time they are manufactured
  - 48-bit serial number for WiFi radio (Media Access Control - MAC) example: 0f:2a:b3:1f:b3:1a
  - when connecting to new WiFi, the computer needs to figure out
    which of the MAC addresses on the WiFi can be used to send packets to the router
      * sends a broadcast message with its own serial number as the “from” address
        and the broadcast address as the “to” address to ask if there are any gateways present on the WiFi network

          From: 0f:2a:b3:1f:b3:1a
          To: ff:ff:ff:ff:ff:ff
          Data: Who is the MAC-Gateway
          for this network?

      * If there is a gateway on the network, the gateway sends a message 
        containing its serial number back to the computer

          From: 98:2f:4e:78:c1:b4
          To: 0f:2a:b3:1f:b3:1a
          Data: I am the gateway
          Welcome to my network

      * no replies: the computer waits a few seconds and then assumes there is no gateway for this network
      * no gateway: the computer might show a different WiFi icon or not show the WiFi icon at all
  - use the broadcast address as little as possible because
      !!! every computer connected to the WiFi receives and  !!! processes !!! any messages
          sent to the broadcast address to make sure the messages were not intended for them

3.2 Courtesy and Coordination
  - “token” : indicates when each station is given the opportunity to transmit data
      * Stations cannot start a transmission unless they have token
      * Instead of listening for “silence” and jumping in, they must wait for their turn to come around
  - When a station receives the token and has a packet to send, it sends the packet
  - Once the packet has been sent, the station gives up the token and waits until the token comes back to it
  - If none of the stations have any data to send, 
    the token is moved from one computer to the next computer as quickly as possible
  - The “try then retry” CSMA/CD approach works very well when:
      * there is NO DATA
      * LOW or MODERATE LEVELS OF DATA levels of data are being sent
  - on a token-style network
    * no data being sent and you want to send a packet => wait for a while
      before you receive the token and can start transmitting
    * you finish your packet => wait until the token comes back before you can send the next packet
  - token approach => when using a link medium such as as a satellite link or a undersea fiber optic link
    where it might take too long or be too costly to detect a collision
  - CSMA/CD (listen-try) => when the medium is inexpensive, shorter distance,
    and there are a lot of stations sharing the medium that only send data in short bursts

3.5 Glossary
  - base station: Another word for the first router that handles your
    packets as they are forwarded to the Internet
  - broadcast: Sending a packet in a way that all the stations connected to a local area network will receive the packet
  - gateway: A router that connects a local area network to a wider area network such as the Internet
    Computers that want to send data outside the local network must send their packets to the gateway for forwarding
  - MAC Address: An address that is assigned to a piece of network hardware when the device is manufactured
  - token: A technique to allow many computers to share the same physical media without collisions.
    Each computer must wait until it has received the token before it can send data


4. Internetworking Layer (IP)
  - The job of the router is to make sure packets move through the router
    and end up on the correct outbound link layer
  - A typical packet passes through from five to 20 routers as it moves from its source to its destination
  - Internet Protocol Address (IP Address): ultimate destination address of the packets

4.1 Internet Protocol (IP) Addresses
  - We cannot use link layer addresses to route packets across multiple networks
      * There is !!! NO RELATIONSHIP !!! between a link layer address
        and the location where that computer is connected to the network
  - addresses assigned to every computer based on where the computer is connected to the network
  - IPv4
    * 4 numbers separated by dots
    * example: 212.78.1.25
    * each number => [0, 255]
  - IPv6
    * example: 2001:0db8:85a3:0042:1000:8a2e:0370:7334
  - most important thing about IP addresses
      !!! THEY CAN BE BROKEN INTO 2 PARTS !!!
    * first part is called the Network Number
      ** IPv4 example:
          Network Number: 212.78
          Host Identifier: 1.25
      ** 65,536 computers could be connected to the network using the network number of "212.78"
      ** all packets with an IP address of 212.78.*.* can be routed to the same location,
         because all PCs appear to the net on a single connection
      ** when a packet arrives in a router and the router needs to decide which outbound link to send the packet to,
        the router only needs to look at the first part of the address to determine the best outbound link

4.2 How Routers Determine the Routes
  - When a new core router is connected to the Internet, it does not know all the routes
  - It may know a few preconfigured routes, but to build a picture of how to route packets
    it must discover routes as it encounters packets    
  - When a router encounters a packet that it does not already know how to route,
    it queries the routers that are its neighbors
  - Sometimes the neighboring routers need to ask their neighbors and so on
    until the route is actually found and sent back to the requesting router
  - routing table for a particular router: mapping of network numbers to outbound links
  - the router does a lookup on the first packet
    * then it could route the next billion packets to that network number
      just by using the information it already has in its routing tables

4.3 When Things Get Worse and Better
  - Sometimes the network has problems and a router must find a way to route data around the problems
    * common problem: one of the outbound links fails
      ** The router discards all of the entries in its routing table that were being routed on that link
      ** Next, as more packets arrive for those network numbers, the router goes through the route discovery process again,
       this time asking all the neighboring routers except the ones that can no longer be contacted due to the broken link
      ** routing tables are rebuilt that reflect the new network configuration => packets are routed more slowly for a while

      !!! THERE SHOULD BE AT LEAST 2 INDEPENDENT PATHS FROM A SOURCE NETWORK TO A DESTINATION NETWORK IN THE NETWORK CORE !!!
    * Routers are also good at detecting and dynamically routing packets around links that are slow or temporarily overloaded
    * side effects of the way routers discover the structure of the network
      ** the route your packets take from the source to the destination can change over time
      ** We don't ask the IP layer to worry about the order of the packets, so second packet may arrive before the first

4.4 Determining Your Route
  - the routers that participate in forwarding your packets across the Internet
    do not know the entire route your packet will take
    * They only know which link to send your packets to so they will get closer to their final destination
  - most computers have a network diagnostic tool called “traceroute” (or “tracert”, depending on the OS)
    that allows you to trace the route between your computer and a destination computer
    * The traceroute command does not actually trace your packet at all
    * It takes advantage of a feature in the IP network protocol that was designed
      to avoid packets becoming “trapped” in the network and never reaching their destination
  - how a packet might get trapped in the network forever and how the IP protocol solves that problem ???
    * example: three routers with routing table entries that formed an endless loop
    * Each of the routers thinks it knows the best outbound link for IP addresses that start with 212.78
    * If a packet with a prefix of 212.78 found its way into one of these routers,
      it would be routed around a circle of three links forever
    * soon the links would be full of traffic going round and round, the routers would fill up with packets waiting to be sent
      and all three routers would crash
    * solution: each packet has a number called Time To Live (TTL)
      ** Each time an IP packet is forwarded down a link, the router subtracts 1 from the TTL value
      ** when the TTL reaches zero, the router assumes that something is wrong and throws the packet away
      ** This approach ensures that routing loops do not bring whole areas of the network down
      ** when the router throws a packet away, it usually sends back a courtesy notification + IP address of that router

4.5 Getting an IP Address

  - Dynamic Host Configuration Protocol (DHCP)

  ___________
  |         |
  |    PC   |    ======= IP? =======>     Server
  |_________|

  ___________
  |         |
  |    PC   |    <======= .42 =======     Server
  |_________|

  ___________
  |         |
  |    PC   |    <==================>     Server
  |_________|


    * first thing a computer does at the link level is sending a message to a special broadcast address, searches for a base station
    * when the computer is successfully connected at the link layer through that base station,
      it sends another broadcast message, searches for a gateway connected to the network 
      ** if there is a gateway, it asks for its IP address and asks which IP should it use
    * if the computer is not there for a while, that IP address is given to another one
  - In some operating systems, when a computer connects to a network, issues a DHCP request, and receives no answer,
    it decides to assign itself an IP address anyway. Often these self-assigned addresses start with "169. . . .".
    * it's still without a gateway, it has no possibility of getting packets routed across the local network and onto the Internet
    * best that can be done is connect to a local network

4.6 A Different Kind of Address Reuse
  - Addresses that start with “192.168.” are called non-routable addresses
    * They can be used within a single local network, but not used on the global network
  - Network Address Translation (NAT)

    => conserve the real routable addresses and use the same non-routable addresses
      over and over for workstations that move from one network to another

    * The gateway has a single routable IP address that it is sharing
      across multiple workstations that are connected to the gateway
    * The computer uses its non-routable address like 192.168.0.5 to send its packets
      but as the packets move across the gateway, the gateway replaces the address with its actual routable address
    * When packets come back to your workstation, the router puts your workstation's non-routable
      address back into the returning packets

4.7 Global IP Address Allocation
  - to connect the network for a new organization to the Internet:
    * contact an Internet Service Provider and make a connection
    * ISP would give you a range of IP addresses (i.e., one or more network numbers)
      that you could allocate to the computers attached to your network
    * they receive the network numbers from a higher-level Internet Service Provider
    * At the top level of IP address allocations are five Regional Internet Registries (RIRs), for a major geographic area
      ** North America (ARIN)
      ** South and Central America (LACNIC)
      ** Europe (RIPE NCC)
      ** Asia-Pacific (APNIC)
      ** Africa (AFRNIC)
    
      IPv4: 32-bit ==================>  IPv6: 128-bit

  - The IP layer is not 100% reliable
    * Packets can be lost due to momentary outages or because the network is momentarily confused
      about the path that a packet needs to take across the network
    * Packets that your system sends later can find a quicker route through the network
      and arrive before packets that your system sent earlier
    * instead of asking too much of the IP layer, we leave the problem of packet loss
      and packets that arrive out of order to our next layer up, the Transport layer

4.9 Glossary
  - core router: A router that is forwarding traffic within the core of the Internet
  - DHCP: Dynamic Host Configuration Protocol
    * DHCP is how a portable computer gets an IP address when it is moved to a new location
  - edge router: A router which provides a connection between a local network and the Internet. Equivalent to gateway
  - Host Identifier: The portion of an IP address that is used to identify a computer within a local area network
  - IP Address: A globally assigned address that is assigned to a computer
    so that it can communicate with other computers that have IP addresses and are connected to the Internet
    * To simplify routing in the core of the Internet IP addresses are broken into Network Numbers and Host Identifiers
    * An example IP address 212.78.1.25 (IPv4)
  - NAT: Network Address Translation. This technique allows a single global IP address
    to be shared by many computers on a single local area network
  - Network Number: The portion of an IP address that is used to dentify which local network the computer is connected to
  - packet vortex: An error situation where a packet gets into an infinite loop because of errors in routing tables
  - RIR: Regional Internet Registry
    * The five RIRs roughly correspond to the continents of the world
      and allocate IP address for the major geographical areas of the world
  - routing tables: Information maintained by each router that keeps track
    of which outbound link should be used for each network number
  - Time To Live (TTL): A number that is stored in every packet that is reduced by one
    as the packet passes through each router
    * When the TTL reaches zero, the packet is discarded
  - traceroute: A command that is available on many Linux/UNIX systems
    that attempts to map the path taken by a packet as it moves from its source to its destination
      * May be called tracert on Windows systems
  - two-connected network: A situation where there is at least two possible paths between any pair of nodes in a network
    * A two-connected network can lose any single link without losing overall connectivity

5. The Domain Name System
  - The Domain Name System lets you access websites by their domain name, so 
    you don't have to keep a list of numeric Internet Protocol (IP) addresses like 212.78.1.25
    * IP address are determined by where your computer connects to the Internet
  - When a computer makes a connection to a system using a domain name address
    * the computer looks up the IP address that corresponds to the domain name
      ** it's easier to move a server from one location to another
      ** the server is given a new IP address and the entry for the domain address is updated
    * then it makes the connection using the IP address

5.1 Allocating Domain Names
  - Domain names are allocated based on organizations that own the domain name
  - International Corporation for Assigned Network Names and Numbers(ICANN)
    * At the top of the domain name hierarchy
    * Chooses the top-level domains (TLDs) like .com, .edu, and .org and assigns those to other organizations to manage
    * Assigns two-letter country code top-level domain names like .us, .za, .nl, and .jp 
      to countries (Country-Code Top-Level Domain Names (ccTLDs))
      ** Countries often add second-level TLDs, like .co.uk
    * Once a domain name is assigned to an organization,
      the controlling organization is allowed to assign subdomains within the domain
      ** The individual owners of those domains are allowed to manage their domain and
        create subdomains under it for their own use or use by others

5.2 Reading Domain Names
  - example IP address: 212.78.1.25
    * the left prefix is the Network Number
    * right part of the address is most specific

      212.78.1.25
      Broad ----> Narrow

    * For domain names, we read from right to left

      drchuck.personal.si.umich.edu
      Narrow         <---     Broad
    
      ** The most general part of this domain name is .edu -> higher education institutions
      ** The subdomain umich.edu is a particular higher education institution

5.4 Glossary
  - DNS: Domain Name System
         * A system of protocols and servers that allow networked applications to look up domain names
         and retrieve the corresponding IP address for the domain name
  - domain name: A name that is assigned within a top-level domain
                 * example: khanacademy.org is a domain that is assigned within the .org top-level domain
  - ICANN: International Corporation for Assigned Network Names and Numbers
           * Assigns and manages the top-level domains for the Internet
  - registrar: A company that can register, sell, and host domain names
  - subdomain: A name that is created below a domain name
               * example: umich.edu is a domain name and both 
                 www.umich.edu and mail.umich.edu” are subdomains within umich.edu
  - TLD: Top Level Domain
         * The rightmost portion of the domain name
         * example TLDs: .com, .org, .club, .help
  
6. Transport Layer
  
        Link -----> Internetworking -----> Transport

  - A key element of the Internetworking layer: it does not attempt to guarantee delivery of any particular packet,
   * sometimes packets can be lost or misrouted
  - The Transport layer is where we handle reliability and message reconstruction on the destination computer
  - Just like the IP layer, the Transport layer adds a small amount of data to each packet
    to help solve the problems of packet reassembly and retransmission

6.1 Packet Headers
  - packet going across one of many links between its source and destination computers has
    * link header
    * IP header
    * Transport Control Protocol (TCP) header,
    along with the actual data in the packet

  
     Link Header        IP Header         TCP Header       Data Packet
    _______________________________________________________________________
    |             |                   |                 |                 |
    |  From | To  |  From | To | TTL  |  Port | Offset  |   ...           |
    |_____________|___________________|_________________|_________________|


    - Link Header
      * removed when the packet is received on one link
      * a new link header is added when the packet is sent out on the next link on its journey
    - IP Headers
      * holds the source and destination Internet Protocol (IP) addresses and the Time to Live (TTL) for the packet
      * set on the source computer and is unchanged (other than the TTL)
        as the packet moves through the various routers on its journey
    - TCP Headers
      * indicate where the data in each packet belongs
      * it keeps track of the position of each packet relative to the beginning of the message or file
        and places the offset in each packet that is created and sent
    - IP and TCP headers
      * stay with a packet as it is going across each link in its journey (may go across several link layers)

6.2 Packet Reassembly and Retransmission
  - As the destination computer receives the packets, it looks at the offset position from the beginning of the message
    so it can put the packet into the proper place in the reassembled message
  - the Transport layer handles packets that arrive out of order 
    * it puts the packet data at the correct position relative to the beginning of the message
  - Window size 
    * amount of data that the sending computer will send before pausing to wait for an acknowledgment
      from the Transport layer on the destination computer
    * it is adjusted
      ** ensures that data is sent rapidly when the connection between two computers is fast
         and much more slowly when the connection has slow links or a heavy load
  - If a packet is lost
    * the destination computer will never send an acknowledgment for that data
    * the sending computer quickly reaches the point where it has sent
      enough unacknowledged data to fill up the window and stops sending new packets
    * At this point, both computers are waiting 
      ** the sending computer is waiting for an acknowledgement for a lost packet that will never come, 💔
      ** the receiving computer is waiting for a lost packet that will never come, 💔
    * At some point, the receiving computer sends a packet to the sending computer
      indicating where in the stream the receiving computer has last received data
      * When the sending computer receives this message, it resends data
        from the last position that the receiving computer had successfully received ^^
 
6.3 The Transport Layer In Operation
  - The sending computer must hold on to all of the data it is sending
    until the data has been acknowledged
  - Once the receiving computer acknowledges the data, the sending computer can discard the sent data
  - example: a message is broken into many packets
    * the first ten packets of the message have been sent and acknowledged by the destination computer ('a')
    * the sending computer has sent six more packets ('S') and then stopped because it reached its window size
    * => three packets that have been sent but not yet received (''S'')
    * there are many hops in the network =>
      it is very common for more than one packet to be enroute in the network at the same time
    * The Transport layer on the receiving computer has received and acknowledged ten packets
      + delivered them to the receiving application ('a')
    * Receiving a packet out of order is not a cause for concern 
      if the missing packet arrives in a reasonably short amount of time
    * As long as all the packets are received, the receiving Transport layer will reconstruct the message,
      fitting the packets together like puzzle pieces
      + deliver them to the receiving application

6.4 Application Clients and Servers
  
  _____________
  |           |                                             You provide reliable connections between
  | Transport |    ======= What's my purpose ??? =======>   between networked applications 
  |   layer   |                                             so those applications can send and receive streams of data
  |___________|                                                             ||
                                                                            ||
                                                                            \/
                                                            you compensate for the fact that
                                                            the Link and Internetworking layers might lose data


6.5 Server Applications and Ports
  - Example server applications on a remote computer: web, video, mail
  - Example: a web client (a browser) needs to connect to the web server running on the remote computer
    * a client application needs to know which remote computer to connect to 
      + needs to choose a particular application to interact with on that remote computer
  - ports
    * all have same IP Address
    * each server application has a different port number
    * well-known default ports for various server applications
      ** Telnet (23) - Login
      ** SSH (22) - Secure Login
      ** HTTP (80) - World Wide Web
      ** HTTPS (443) - Secure Web
      ** SMTP (25) - Incoming Mail
      ** IMAP (143/220/993) - Mail Retrieval
      ** POP (109/110) - Mail Retrieval
      ** DNS (53) - Domain Name Resolution
      ** FTP (21) - File Transfer

6.7 Glossary
  - acknowledgement: When the receiving computer sends a notification back to the source computer
                     indicating that data has been received
  - buffering: Temporarily holding on to data that has been sent or received
               until the computer is sure the data is no longer needed
  - listen: When a server application is started and ready to accept incoming connections from client applications
  - port: A way to allow many different server applications to be waiting for incoming connections on a single computer
          * Each application listens on a different port
          * Client applications make connections to well-known port numbers to make sure
            they are talking to the correct server application

7. Application Layer
  - The architecture for a networked application is called client/server

7.2 Application Layer Protocols
  - Protocol: A set of rules that govern how we communicate
  - HTTP (HyperText Transport Protocol) - web clients and web servers - https://tools.ietf.org/html/rfc7230

7.3 Exploring the HTTP Protocol
  - The telnet application was first developed in 1968
      * was developed according to one of the earliest standards for the Internet https://tools.ietf.org/html/rfc15
      * was designed and built even before the first TCP/IP network was in production

      domain name (or IP address) + a port to connect to on that host

      * example: telnet www.dr-chuck.com 80
      * response: series of headers (metadata) describing the document ===> a blank line ===> the actual document

7.4 The IMAP Protocol for Retrieving Mail
  - used so that a mail application running on your computer can retrieve mail from a central server
  - the Internet Message Access Protocol (IMAP) is described in a series of Request For Comment (RFC) documents
    starting with this RFC https://tools.ietf.org/html/rfc3501
  - example: client (C), server (S)
          C: A142 SELECT INBOX
          S: * 172 EXISTS
          S: * 1 RECENT
          S: * OK [UNSEEN 12] Message 12 is first unseen
          S: * OK [UIDVALIDITY 3857529045] UIDs valid
          S: * OK [UIDNEXT 4392] Predicted next UID
          S: * FLAGS (\Answered \Flagged \Deleted \Seen \Draft)
          S: * OK [PERMANENTFLAGS (\Deleted \Seen \*)] Limited
          S: A142 OK [READ-WRITE] SELECT completed

7.5 Flow Control
  - example: the web browser has made a transport connection to the web server
             and has started downloading an image file
            * The web server has opened the image file and is sending the data
              from the file to its Transport layer as quickly as possible
            * !!! window size !!!
            * When the window fills up, the web server is paused until the Transport layer
             on the destination computer has started to receive and acknowledge packets
            * As the Transport layer on the destination computer starts to receive packets,
              reconstruct the stream of data, and acknowledge packets,
              it delivers the reconstructed stream of packets to the web browser application display on the user's screen
      
    __________________________________________________________________________________
    |                 |             | Internetwork    |            |                 |
    |  Web Server App |  Transport  | And Link Layers | Transport  | Web Browser App |
    |_________________|_____________|_________________|____________|_________________|      
         /\       
         ||       
    _____||______                                                       ________
    |           |       ...aSSSSSS ====== S S S =======> ..aRR R        | AAAA |
    | ...FFFFF  |                  <======= ACK ========                | AA.. |
    |___________|                                                       |______|

      * The Transport layer has sent six packets (S) and has stopped sending
        because it has reached its window size and paused the web server
      * Three of those six packets have made it to the Transport layer on the destination computer (R)
        and three of the packets are still making their way across the Internet (S)
      * the destination Transport layer pieces the stream back together,
        it both sends an acknowledgement (ACK) and delivers the data to the receiving application (the web browser)
      * The web browser reconstructs the image (A) and displays it to the user as the data is received
      * the transport layers !!! DO NOT KEEP THE PACKETS FOR THE ENTIRE FILE !!!
        ** They only retain packets that are in transit and unacknowledged

7.6 Writing Networked Applications

7.8 Glossary
  - HTML: HyperText Markup Language
          * A textual format that marks up text using tags
  - HTTP: HyperText Transport Protocol
          * An Application layer protocol that allows web browsers to retrieve web documents from web servers
  - IMAP: Internet Message Access Protocol.
          * A protocol that allows mail clients to log into and retrieve mail from IMAP-enabled mail servers
  - flow control: When a sending computer slows down to make sure that it does not overwhelm
                  either the network or the destination computer.
                  * Flow control also causes the sending computer o increase the speed at which data is sent
                    when it is sure that the network and destination computer can handle the faster data rates
  - socket: A software library available in many programming languages that makes creating a network connection
            and exchanging data nearly as easy as opening and reading a file on your computer
  - status code: One aspect of the HTTP protocol that indicates the overall success or failure of a request for a document
  - telnet: A simple client application that makes TCP connections to various address/port combinations
            and allows typed data to be sent across the connection
            * In the early days of the Internet, telnet was used to remotely log in to a computer across the network
  - web browser: A client application that you run on your computer to retrieve and display web pages
  - web server: An application that deliver (serves up) Web pages

8. Secure Transport Layer
  - the Link, Internetwork, and Transport layers are focused on the efficient movement of data
    and solving the problems of a large-scale shared distributed network
    without worrying about the privacy of that data
  - There are TWO general approaches to securing network activity
    * The first makes sure that all of the network hardware (routers and links)
      is in physically secure locations so it is not possible for someone to sneak in
      and monitor traffic while it is crossing the Internet
      ** not practical approach for hundreds of thousands of network routers owned and operated by many different organizations
      ** once WiFi is added to the mix and your packets went over radio waves,
         a network attacker could just sit in a coffee shop and intercept packets as they passed through the air
    * Second approach is to encrypt data in your computer before it is sent across its first physical link,
      and then decrypt the data in the destination computer after it arrives
      ** The encryption also guarantees that there is no way to alter your data while it is crossing the Internet

8.1 Encrypting and Decrypting Data
  - ciphertext: scrambled message
  - ALL encryption systems depend on some kind of a SECRET KEY
    that BOTH parties are aware of so they can decrypt received data

8.2 Two Kinds of Secrets
- traditional way to encrypt transmissions is using a shared secret (a password, a sentence, a number)
  that only the sending and receiving parties know
- the attackers are monitoring and capturing all network traffic
  ===> they could also capture the unencrypted message that contained the shared secret
  ===> the attacker could intercept a message, delay it, then decrypt it, change and re-encrypt it,
       and send the modified message back on its way
- the concept of asymmetric key encryption (public/private keys) was developed in 1970
  * The computer that will be receiving the encrypted data chooses both the encryption key and decryption key
  * Then the encryption key is sent to the computer that will be sending the data
  * The sending computer encrypts the data and sends it across the network
  * The receiving computer uses the decryption key to decrypt the data
  * We call the encryption key the public key because it can be widely shared
  * We call the decryption key the private key because it never leaves the computer where it was created
  * if an attacker has the public key (which was sent unencrypted) and the encrypted text,
    it is quite difficult to decrypt the encrypted data

8.3 Secure Sockets Layer (SSL)
  - an optional partial layer between the Transport layer and the Application layer - to add security
    ===> The Secure Sockets Layer (SSL) or Transport Layer Security (TLS)
         * There are subtle differences between SSL and TLS but they both encrypt data at the Transport layer
  - When an application requested that the Transport layer make a connection to a remote host,
    it could request that the connection either be encrypted or unencrypted
  - If an encrypted connection was requested, the Transport layer encrypted the data before breaking the stream into packets
    * the Transport layer, Internetwork layer, and physical (link) layers could still
      perform exactly the same way whether the packets were encrypted or not
    * The applications making the connections were also spared the details of how encryption and decryption worked

8.4 Encrypting Web Browser Traffic
  - use https for all web traffic

8.5 Certificates and Certificate Authorities
  - is the public key that you have received when you connected to a server 
    really from the organization it claims to be from ???
  - example
    * Perhaps you think you are connecting to www.amazon.com but a rogue computer intercepts your traffic,
      claiming to be www.amazon.com and giving you a public key to use for encryption
    * If your web browser trusts the key, it will use the rogue computer's public key to
      encrypt your banking information and send it to the rogue computer
    * The rogue computer gave you the public key, it also has the corresponding private key and
      is able to decrypt and abscond with your banking information
    * who the key is actually coming from is achieved by sending you a public key that is digitally
      signed by a Certificate Authority (CA)
      ** When your computer or browser is initially installed, it knows about a number of wellknown certificate authorities
      ** If your browser is given a public key that is signed by one of the well-known certificate authorities,
         it trusts the key and uses it to encrypt and send your data

8.7 Glossary
 - asymmetric key: An approach to encryption where one (public) key is used to encrypt data
                   prior to transmission and a different (private) key is used to decrypt data once it is received
 - certificate authority: An organization that digitally signs public keys after verifying
                           that the name listed in the public key is actually the person
                           or organization in possession of the public key
 - ciphertext: A scrambled version of a message that cannot be read without knowing the decryption key and technique 
 - decrypt: The act of transforming a ciphertext message to a plain text message using a secret or key
 - encrypt: The act of transforming a plain text message to a ciphertext message using a secret or key
 - plain text: A readable message that is about to be encrypted before being sent
 - private key: The portion of a key pair that is used to decrypt transmissions
 - public key: The portion of a key pair that is used to encrypt transmissions
 - shared secret: An approach to encryption that uses the same key for encryption and decryption
 - SSL: Secure Sockets Layer
        * An approach that allows an application to request that a Transport layer connection
          is to be encrypted as it crosses the network
        * Similar to Transport Layer Security (TLS)
  - TLS: Transport Layer Security
         * An approach that allows an application to request that a Transport layer connection
          is to be encrypted as it crosses the network. Similar to Secure Sockets Layer (SSL)

9. The OSI Model
  - The TCP/IP model is an implementation model
      * it provides the guidance for those who would build TCP/IP-compatible network hardware or software
  - The Open System Interconnection (OSI) model is more of an abstract model
      * it can be used to understand a wide range of network architectures
      * it has seven layers
        _______________________
        |                     |
        |     Application     |
        |_____________________|
        |                     |
        |     Presentation    |
        |_____________________|
        |                     |
        |       Session       |
        |_____________________|
        |                     |
        |      Transport      |
        |_____________________|
        |                     |
        |       Network       |
        |_____________________|
        |                     |
        |      Data Link      |
        |_____________________|
        |                     |
        |       Physical      |
        |_____________________|

9.1 Physical (Layer 1)
  - deals with the physical attributes of the actual wired, wireless, fiber optic,
    or other connection that is used to transport data across a single link
  - defines the shapes of the connectors and type of media which can be used
  - bit encoding (modulation)
    * encodes the bits that make up the data being sent across the medium
    * determines how fast data can be sent across the link

9.2 Data Link (Layer 2)
  - how the systems using a physical link cooperate with one another
  - when data is broken into packets, the Data Link layer defines special sequences
    to indicate the beginning and end of each packet
  - The stations communicating using the physical connection are assigned addresses
    to allow for effective use of the media
  - on a wireless network multiple stations are sharing the same media
    * the Data Link layer defines how those stations will share the connections
      with the other systems connected to the network
  - Most Data Link layers also have some form of checksum
    to detect and/or correct for errors in the transmitted data
  - design problems solved in the Physical and Data Link layers
    of the OSI model are addressed by the Link layer of the TCP/IP model

9.3 Network (Layer 3)
  - Like the Internetwork Layer (IP) in the TCP/IP model, the OSI Network layer
    deals with the global assignment of “routable” addresses to the various systems connected to the network
  - governs how routers forward packets across multiple hops to get from their source to their destination
  - Like the IP layer, The OSI Network layer does not attempt to be error free
    * it assumes that lost data will be detected and retransmitted at the next layer up

9.4 Transport (Layer 4)
  - manages packet loss and retransmission as well as flow control and window size
  - The rest of the functionality of the TCP/IP Transport layer
    is handled in the Session layer in the OSI model

9.5 Session (Layer 5)
  - handles establishing connections between applications
  - deals with ports so that a connecting client application
    can find the correct server application on a particular system
  - Some aspects of secure transmission are also handled in the OSI Session layer

9.6 Presentation (Layer 6)
  - focuses on how data is represented and encoded for transmission across the network
  - handles data encryption and decryption
  - example: the Presentation layer would describe how to encode the pixels of an image
             so that the receiving application can properly decode the data

9.7 Application (Layer 7)
  - The OSI Application Layer is very similar to the Application layer
    in the TCP/IP model, in that it contains the applications themselves
  - some applications are client applications that initiate connections, 
    other applications are the server applications that respond to those connection requests
  - The various pairs of applications have protocol standards that define interoperability
    between multiple clients and multiple servers from different vendors

9.8 Comparing the OSI and TCP/IP Models

9.9 Link Layer (TCP/IP)
  - combines the Physical and Data Link layers from the OSI model
  - The Physical and Data Link layers are usually implemented in hardware
  - Products like Ethernet, WiFi, satellite or fiber optic often are implemented in a network driver card
    that plugs into the back of a computer or router
    * The network driver card generally implements both the physical and the data link
      aspects of the connection in the hardware on the card
    * data link layers are tuned to the limitations and requirements of their corresponding physical layers
    * in real systems, it is somewhat rare for a particular data link layer to be
      arbitrarily paired with any number of physical layers
  - it can be hard to separate the physical and data link aspects for a particular link technology
    * the TCP model combines them into a single layer for simplicity

9.10 Internetwork Layer (TCP/IP)
  - the OSI Network and TCP/IP Internetwork layers perform the same functions
    of creating a globally routable address space and building routers
    to insure that packets properly find their way from the source to the destination across multiple hops

9.11 Transport Layer (TCP/IP)
  - The features of the Transport layer in TCP/IP are spread across the Transport and Session layers of the OSI model
  - The OSI Transport layer deals with flow control and packet retransmission
  - The OSI Presentation layer deals with multiple applications running on multiple ports
    as well as session establishment and teardown
  - The Secure Sockets Layer (SSL) in the TCP/IP model corresponds to
    parts of the Session and Presentation layers in the OSI model

9.12 Application Layer (TCP/IP)
  - The TCP/IP Application Layer combines the non-security aspects
    of the OSI Presentation layer and the OSI Application layer
  - many TCP/IP applications deal with issues like encoding and decoding various types of data
  - the TCP/IP model does not see data formatting as a separate layer
  - Various data encoding and decoding technologies are used in TCP/IP applications,
    but TCP/IP tends to treat these capabilities as library code
    that applications make use of as needed for the application

9.14 Glossary
  - abstract model: A model and set of terminology that is used to generally understand a problem area
                    and guide the development of standards and implementations to solve problems
  - implementation model: A model and set of terminology that is used to guide the development of standards
                          and an implementation to solve a particular problem
  - ISO: International Organization for Standardization
        * A worldwide body that develops standards in computing, networking, and many other areas
  - OSI: Open System Interconnection.
         * A seven-layer model used to help organize the design of various approaches to network architecture.

"""