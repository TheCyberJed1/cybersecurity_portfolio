# Network Access Control Policy Implementation Using ACLs

## Objective
Enforce a network security policy with **standard and extended ACLs** — block
departments from a sensitive subnet while permitting selective services
(HTTP, SSH).

## Topology
<!-- ![topology](../../diagrams/network-topologies/lab-04-acls.png) -->

## Tools Used
- Cisco Packet Tracer
- Cisco IOS CLI

## Implementation Steps
1. Identify sensitive subnet (e.g. Servers / Finance).
2. Write extended ACLs matching source, destination, protocol, and port.
3. Apply ACLs to the correct interface and direction.
4. Test allow/deny against the policy matrix.

## Security Policy Mapping
| Rule | Source | Destination | Service | Action |
|------|--------|-------------|---------|--------|
| 1    | GUEST  | Servers     | any     | DENY   |
| 2    | HR     | Servers     | HTTP    | PERMIT |
| 3    | IT     | Servers     | SSH     | PERMIT |
| 4    | any    | any         | any     | implicit DENY |

## Observations
<!-- What worked, what broke, what you had to debug. -->

## Security / Networking Concepts
- Standard vs. extended ACLs
- Rule ordering &amp; implicit deny
- Stateless filtering placement

## Real-World Application
ACLs are the enforcement layer that turns a segmented design into an actual
security policy.

## Mitigation / Improvements
- Move to stateful firewall for return-traffic handling
- Log denied flows for monitoring

## Evidence
<!-- show access-lists · connectivity tests per rule -->
