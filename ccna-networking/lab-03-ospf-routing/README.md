# Dynamic Routing Design Using OSPF for Enterprise Scalability

## Objective
Replace static routing with **OSPF** across a three-router topology serving
multiple LANs, and verify neighbor adjacencies and route propagation.

## Topology
<!-- ![topology](../../diagrams/network-topologies/lab-03-ospf.png) -->

- 3 routers (R1, R2, R3)
- Multiple LAN segments behind each router
- OSPF single-area (Area 0) — extendable to multi-area

## Tools Used
- Cisco Packet Tracer
- Cisco IOS CLI

## Implementation Steps
1. Address all interfaces and links.
2. Enable OSPF and advertise networks (`network ... area 0`).
3. Set router-IDs and tune interface costs.
4. Verify adjacencies and routing tables.

## Observations
<!-- What worked, what broke, what you had to debug. -->

## Security / Networking Concepts
- Link-state routing &amp; SPF
- OSPF adjacency states (Down → Full)
- Areas, costs, and route summarization

## Real-World Application
OSPF is a default IGP in enterprise networks; demonstrating adjacency
troubleshooting is a high-signal junior-network skill.

## Mitigation / Improvements
- Enable OSPF authentication (MD5 / SHA)
- Use passive-interface on user-facing segments
- Summarize at area boundaries

## Evidence
<!-- show ip ospf neighbor · show ip route ospf · ping across segments -->
