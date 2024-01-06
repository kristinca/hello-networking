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
        


"""
