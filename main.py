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


"""
