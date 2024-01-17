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
    * it's still without a gateway, it has no ossibility of getting packets routed across the local network and onto the Internet
    * best that can be done is connect to a local network

"""