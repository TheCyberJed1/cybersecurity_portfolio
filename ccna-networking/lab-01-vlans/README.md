# Enterprise Network Segmentation Using VLAN Architecture

## Objective
Simulate a small enterprise LAN segmented into three isolated departments —
**HR**, **IT**, and **Guest** — using VLANs, then enable controlled inter-VLAN
routing via router-on-a-stick.

## Topology
<!-- ![topology](../../diagrams/network-topologies/lab-01-vlans.png) -->

| VLAN | Name  | Subnet          | Purpose            |
|------|-------|-----------------|--------------------|
| 10   | HR    | 192.168.10.0/24 | HR department      |
| 20   | IT    | 192.168.20.0/24 | IT department      |
| 30   | GUEST | 192.168.30.0/24 | Guest / untrusted  |

## Tools Used
- Cisco Packet Tracer
- Cisco IOS CLI

## Implementation Steps
1. Create VLANs 10/20/30 on the switch.
2. Assign access ports to the correct VLAN (`switchport mode access`).
3. Configure the switch-to-router link as an 802.1Q trunk.
4. Configure router subinterfaces (router-on-a-stick) for inter-VLAN routing.
5. Set DHCP/static addressing per VLAN.

## Observations
<!-- What worked, what broke, what you had to debug. -->

## Security / Networking Concepts
- VLAN segmentation &amp; broadcast-domain isolation
- Switchport access vs. trunk modes
- 802.1Q trunking

## Real-World Application
Departmental segmentation limits broadcast scope and contains lateral movement —
a baseline control in every enterprise campus network.

## Mitigation / Improvements
- Restrict trunk allowed-VLAN lists
- Disable DTP / unused ports; place them in a blackhole VLAN
- Add ACLs to restrict inter-VLAN traffic (see lab-04)

## Evidence
<!-- Screenshots, running-config exports, ping tests -->
