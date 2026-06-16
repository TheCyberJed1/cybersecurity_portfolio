# Enterprise Active Directory Attack Simulation — Kerberoasting + Lateral Movement

> ⚠️ **Lab use only.** All techniques performed in an isolated, self-owned lab
> environment for educational/defensive purposes.

## Objective
Simulate a realistic AD attack chain — from initial enumeration through
Kerberoasting to lateral movement — and map a defensive mitigation to each stage.

## Environment
- Windows Server Domain Controller (lab)
- Domain-joined workstation(s)
- Kali Linux attacker host

## Attack Chain
1. **Enumeration** — users, groups, SPNs, shares (`enum4linux`, `BloodHound`, `ldapsearch`).
2. **Kerberoasting** — request/extract service-ticket hashes (`GetUserSPNs`), crack offline (`hashcat`).
3. **Privilege escalation path** — abuse misconfigured ACLs / group memberships.
4. **Lateral movement** — reuse credentials / pass-the-hash to reach additional hosts.

## Tools Used
- Impacket (GetUserSPNs, secretsdump)
- BloodHound / SharpHound
- Hashcat
- CrackMapExec

## Mitigation / Defense Mapping
| Stage | Detection / Mitigation |
|-------|------------------------|
| Enumeration | Limit anonymous LDAP; monitor BloodHound-style queries |
| Kerberoasting | Strong (25+ char) service-account passwords; gMSA; alert on TGS requests |
| Priv-esc | Tier model; least-privilege ACL review |
| Lateral movement | LAPS; disable NTLM where possible; segment + monitor |

## Evidence
<!-- Screenshots of enumeration, cracked hash (redacted), BloodHound paths -->
