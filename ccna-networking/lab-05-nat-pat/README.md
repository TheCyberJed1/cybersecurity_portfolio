# Enterprise Internet Gateway with NAT/PAT Address Translation

## Objective
Simulate an internet edge: translate an inside private network to a single public
address using **PAT (NAT overload)** against a simulated ISP.

## Topology
<!-- ![topology](../../diagrams/network-topologies/lab-05-nat.png) -->

- Inside: private network (e.g. 192.168.0.0/16)
- Outside: simulated ISP / public segment
- Edge router performing PAT overload

## Tools Used
- Cisco Packet Tracer
- Cisco IOS CLI

## Implementation Steps
1. Define `ip nat inside` / `ip nat outside` interfaces.
2. Create an ACL matching inside traffic to be translated.
3. Configure `ip nat inside source list <acl> interface <outside> overload`.
4. Generate traffic and inspect the translation table.

## Observations
<!-- What worked, what broke, what you had to debug. -->

## Security / Networking Concepts
- NAT vs. PAT (overload)
- Inside-local / inside-global mappings
- Port-based multiplexing

## Real-World Application
Every small/medium business edge uses PAT so an entire LAN shares one public IP —
demonstrates real internet-edge behavior.

## Mitigation / Improvements
- Add static NAT / port-forwarding for hosted services
- Pair with edge ACL / firewall for inbound protection

## Evidence
<!-- show ip nat translations · show ip nat statistics -->
