# Structured Network Troubleshooting Methodology Using Layered Diagnostics

## Objective
Apply a repeatable, layered (OSI-driven) troubleshooting methodology to a network
with **intentionally injected faults**, and document the diagnosis path.

## Topology
<!-- ![topology](../../diagrams/network-topologies/lab-06-troubleshooting.png) -->

## Injected Faults
- Wrong subnet mask on a host/interface
- Missing / incorrect route
- Administratively down interface
- VLAN / trunk misconfiguration

## Tools Used
- `ping`, `traceroute`
- `show ip interface brief`, `show ip route`, `show vlan brief`, `show running-config`
- Wireshark (packet-flow confirmation)

## Methodology
1. **Define** the problem (symptom vs. expected).
2. **Gather** facts (show/ping/trace).
3. **Isolate** by layer (L1 → L2 → L3 → up).
4. **Hypothesize** the cause.
5. **Fix &amp; verify**; document.

## Diagnosis Log
| Symptom | Tool used | Root cause | Fix |
|---------|-----------|------------|-----|
|         |           |            |     |

## Real-World Application
Structured diagnostics is exactly what NOC / help-desk escalation expects —
methodical, layer-by-layer, evidence-backed.

## Mitigation / Improvements
- Config backups &amp; change control to prevent regressions
- Monitoring/alerting to catch interface/route changes early

## Evidence
<!-- before/after show outputs, ping/trace captures -->
