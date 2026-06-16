<<<<<<< HEAD
<!-- ====================== BANNER ====================== -->
<div align="center">

# 🛡️ Cybersecurity &amp; Networking Portfolio

### Hands-on labs simulating production-like enterprise networks, offensive security, and security automation

<p>
  <img src="https://img.shields.io/badge/Focus-Network%20Engineering-2dd4bf?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Focus-Offensive%20Security-f87171?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Focus-Automation-fbbf24?style=for-the-badge" />
</p>

<p>
  <img src="https://img.shields.io/badge/Cisco-1BA0D7?style=flat-square&logo=cisco&logoColor=white" />
  <img src="https://img.shields.io/badge/Kali_Linux-557C94?style=flat-square&logo=kalilinux&logoColor=white" />
  <img src="https://img.shields.io/badge/Wireshark-1679A7?style=flat-square&logo=wireshark&logoColor=white" />
  <img src="https://img.shields.io/badge/Nmap-4682B4?style=flat-square&logo=nmap&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Active_Directory-0078D4?style=flat-square&logo=microsoft&logoColor=white" />
  <img src="https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black" />
</p>

<p>
  <a href="https://www.linkedin.com/in/luke-thompson-b4a0653a4/">
    <img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat-square&logo=linkedin&logoColor=white" />
  </a>
  <a href="mailto:light.security1@gmail.com">
    <img src="https://img.shields.io/badge/Email-Contact-EA4335?style=flat-square&logo=gmail&logoColor=white" />
  </a>
  <a href="https://github.com/TheCyberJed1">
    <img src="https://img.shields.io/badge/GitHub-Follow-181717?style=flat-square&logo=github&logoColor=white" />
  </a>
</p>

</div>

---

## 📖 Overview

This repository contains **hands-on networking and security labs** demonstrating real-world skills in:

- 🌐 **Network design** (CCNA-level)
- 🔀 **Routing &amp; switching**
- 🔍 **Security testing &amp; enumeration**
- 🏢 **Active Directory attack simulation**
- 🐍 **Python automation for security tasks**

> Each lab simulates a **production-like environment**, focusing on real troubleshooting, attack simulation, and enterprise networking design.
> This is the gap between *“I studied CCNA”* and *“I can design and explain enterprise networks.”*

> 🔗 **Live portfolio site:** open [`index.html`](index.html) locally, or enable **GitHub Pages** (Settings → Pages → deploy from `main`).

---

## 🧠 Core Skills Demonstrated

| 🌐 Networking | 🔐 Security | 🛠️ Tooling &amp; Automation |
|---------------|-------------|-----------------------------|
| VLAN segmentation &amp; switching | ACL-based network security | Python scripting |
| OSPF dynamic routing | Penetration testing fundamentals | Nmap automation |
| Inter-VLAN routing | Active Directory attack chains | Log parsing |
| NAT / PAT configuration | Enumeration &amp; scanning | Wireshark analysis |
| Network troubleshooting | Kerberoasting / lateral movement | Kali Linux tooling |

---

## 🚀 Featured Projects

### 🌐 CCNA Networking Labs

| # | Project | Concepts | Status |
|---|---------|----------|:------:|
| 01 | [**Enterprise Network Segmentation Using VLAN Architecture**](ccna-networking/lab-01-vlans/) | VLANs · trunking · switchport | 🚧 |
| 02 | [**Multi-Segment Enterprise Routing Architecture**](ccna-networking/lab-02-inter-vlan-routing/) | Router-on-a-stick · dot1Q · subinterfaces | 🚧 |
| 03 | [**Dynamic Routing Design Using OSPF for Enterprise Scalability**](ccna-networking/lab-03-ospf-routing/) | OSPF · adjacency · multi-area | 🚧 |
| 04 | [**Network Access Control Policy Implementation Using ACLs**](ccna-networking/lab-04-acls-security/) | Standard &amp; extended ACLs · policy mapping | 🚧 |
| 05 | [**Enterprise Internet Gateway with NAT/PAT Address Translation**](ccna-networking/lab-05-nat-pat/) | NAT · PAT overload · internet edge | 🚧 |
| 06 | [**Structured Network Troubleshooting Methodology**](ccna-networking/lab-06-troubleshooting/) | Layered diagnostics · fault injection | 🚧 |

### 🔴 Security Labs

| Project | What It Shows |
|---------|---------------|
| [**Enterprise Active Directory Attack Simulation**](security-labs/active-directory/) *(Kerberoasting + Lateral Movement)* | Enumeration → privilege-escalation path → mitigation steps |
| [**Automated Network Reconnaissance Workflow**](security-labs/enumeration/) *(Nmap + Python)* | Scan automation · output parsing · reporting structure |
| [**Web Application Vulnerability Testing Workflows**](security-labs/web-app-testing/) | Enumeration · vulnerability classes · repeatable methodology |
| [**Kali Pen-Testing Toolkit &amp; Workflows**](security-labs/kali-pentesting/) | Linux security tooling · offensive workflow |

> 🚧 = lab folder scaffolded with documentation template, ready for evidence &amp; configs.

---

## 📁 Repository Structure

```
cybersecurity-portfolio/
│
├── README.md
├── index.html                  # portfolio website
│
├── ccna-networking/
│   ├── lab-01-vlans/
│   ├── lab-02-inter-vlan-routing/
│   ├── lab-03-ospf-routing/
│   ├── lab-04-acls-security/
│   ├── lab-05-nat-pat/
│   └── lab-06-troubleshooting/
│
├── security-labs/
│   ├── active-directory/
│   ├── kali-pentesting/
│   ├── web-app-testing/
│   └── enumeration/
│
├── diagrams/
│   ├── network-topologies/
│   └── attack-chains/
│
├── scripts/
│   ├── nmap-automation.py
│   ├── log-parser.py
│   └── recon-tools/
│
└── writeups/
    ├── lab-template.md
    ├── case-study-template.md
    └── lessons-learned.md
```

---

## 📝 Documentation Standard

Every lab follows the same structure — a signal that I can **document technical systems** the way an enterprise expects:

`Objective` → `Topology` → `Tools Used` → `Implementation Steps` → `Observations` → `Concepts` → `Real-World Application` → `Mitigation / Improvements` → `Evidence`

See [`writeups/lab-template.md`](writeups/lab-template.md) for the full template.

---

## 🎯 Key Takeaway

When you browse this repo, you can infer that I:

- ✅ Understand **enterprise architecture**
- ✅ Can **document technical systems**
- ✅ Think in **attack + defense models**
- ✅ Operate beyond *“lab learner”* level

---

## 📬 Contact

<div align="center">

**Luke Thompson**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-luke--thompson-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/luke-thompson-b4a0653a4/)
[![Email](https://img.shields.io/badge/Email-light.security1@gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:light.security1@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-TheCyberJed1-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/TheCyberJed1)

</div>
=======
# Cybersecurity & Networking Portfolio

## Overview
This repository contains hands-on networking and security labs demonstrating real-world skills in:
- Network design (CCNA-level)
- Routing & switching
- Security testing & enumeration
- Active Directory attack simulation
- Python automation for security tasks

---

## Core Skills Demonstrated
- VLAN segmentation & switching design
- OSPF dynamic routing
- ACL-based network security
- NAT/PAT configuration
- Network troubleshooting
- Penetration testing fundamentals
- Linux security tooling (Kali)
- Basic security automation (Python)

---

## Featured Projects

### CCNA Networking Labs
- VLAN segmentation & trunking design
- Multi-router OSPF enterprise simulation
- Secure ACL firewall simulation
- NAT/PAT internet gateway setup

### Security Labs
- Active Directory attack chain simulation
- Network enumeration & scanning pipelines
- Web vulnerability testing workflows

---

## Key Takeaway
Each lab simulates production-like environments, focusing on real troubleshooting, attack simulation, and enterprise networking design.

---

## Contact
https://www.linkedin.com/in/luke-thompson-b4a0653a4/
light.security1@gmail.com
>>>>>>> 98052b48df4c85023e45b3446cd5fe6bf90b3346
