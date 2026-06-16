# Multi-Segment Enterprise Routing Architecture

## Objective
Enable routing between segmented VLANs using **router-on-a-stick** with dot1Q
subinterfaces, then prove both intended reachability and intended isolation.

## Topology
<!-- ![topology](../../diagrams/network-topologies/lab-02-inter-vlan.png) -->

## Tools Used
- Cisco Packet Tracer
- Cisco IOS CLI

## Implementation Steps
1. Build VLANs and trunk (from lab-01).
2. Create router subinterfaces (e.g. `Gig0/0.10`, `.20`, `.30`).
3. Apply `encapsulation dot1Q <vlan>` and an IP per subinterface.
4. Set each subinterface as the VLAN default gateway.
5. Run validation tests.

## Observations
<!-- What worked, what broke, what you had to debug. -->

## Security / Networking Concepts
- Inter-VLAN routing
- 802.1Q encapsulation on subinterfaces
- Default-gateway design

## Real-World Application
Router-on-a-stick is the classic low-cost inter-VLAN routing model for branch
sites before moving to L3 switches.

## Mitigation / Improvements
- Migrate to L3 switch SVIs for performance at scale
- Layer ACLs on top to enforce policy (lab-04)

## Evidence — Traffic Isolation Tests
| Source | Destination | Expected | Result |
|--------|-------------|----------|--------|
| HR PC  | IT PC       | ✅ allow |        |
| GUEST  | HR PC       | ❌ deny  |        |
| GUEST  | Internet    | ✅ allow |        |
