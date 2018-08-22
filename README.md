# two_connect
Establish connection only with connect

How does it work?
If both clients send SYN to each other simultaneously, one of them will accept SYN from the other side, and reply SYN/ACK.

Illustration:
1. A ----SYN---> B (B will drop SYN)
2. A <---SYN---- B (A will accept SYN)
3. A --SYN/ACK-> B (A reply SYN/ACK to B)
4. A <---ACK---- B (B reply ACK to A)
5. Connection established.
