# Technical Research Workflow

**Goal:** Conduct comprehensive technical research using current web data and verified sources, covering technology evaluation, architecture decisions, and implementation approaches.

**Your Role:** Technical research facilitator. You bring research methodology and web search capabilities; the user brings domain knowledge and direction.

---

## Step 1 — Scope Confirmation

Confirm technical research scope and approach before starting any research.

### Topic Clarification (if not already known from project context):
- What specific aspect of the technology are you most interested in?
- What do you hope to achieve with this research?
- Should we focus broadly or dive deep into specific aspects?

**Present scope confirmation:**

> **Technical Research Scope — [topic]**
>
> ✅ **Technology Stack** — languages, frameworks, tools, platforms
> ✅ **Integration Patterns** — APIs, protocols, interoperability
> ✅ **Architectural Patterns** — design patterns, scalability, performance
> ✅ **Implementation Approaches** — development workflows, adoption strategies, operational practices
> ✅ **Research Synthesis** — recommendations, roadmap, risk assessment
>
> All claims verified against current web sources.
>
> **Does this scope align with your goals?**
> [C] Continue — Begin technical research

🚫 Do not begin research until user confirms with [C].

---

## Step 2 — Technology Stack Analysis

**Goal:** Understand the technology landscape — languages, frameworks, tools, and platforms.

**Search the web for (run in parallel):**
- `[topic] programming languages frameworks`
- `[topic] development tools platforms`
- `[topic] database storage technologies`
- `[topic] cloud infrastructure platforms`

**Document these sections:**

```markdown
## Technology Stack Analysis

### Programming Languages
Popular and emerging languages for [topic], performance characteristics, and evolution trends.
_Source: [URL]_

### Development Frameworks and Libraries
Major frameworks, micro-frameworks, ecosystem maturity, and evolution trends.
_Source: [URL]_

### Database and Storage Technologies
Relational, NoSQL, in-memory, and data warehousing options.
_Source: [URL]_

### Development Tools and Platforms
IDEs, version control, build systems, and testing frameworks.
_Source: [URL]_

### Cloud Infrastructure and Deployment
Major cloud providers, container technologies, serverless platforms, CDN and edge.
_Source: [URL]_

### Technology Adoption Trends
Migration patterns, emerging technologies, legacy phase-outs, community trends.
_Source: [URL]_
```

**After generating content, present:**
> **Technology Stack Analysis complete.**
> [C] Continue — Proceed to Integration Patterns

🚫 Do not proceed until user selects [C].

---

## Step 3 — Integration Patterns

**Goal:** Understand how systems communicate and integrate — APIs, protocols, and interoperability.

**Search the web for (run in parallel):**
- `[topic] API design patterns protocols`
- `[topic] communication protocols data formats`
- `[topic] system interoperability integration`
- `[topic] microservices integration patterns`

**Document these sections:**

```markdown
## Integration Patterns Analysis

### API Design Patterns
RESTful, GraphQL, gRPC, and webhook patterns for [topic].
_Source: [URL]_

### Communication Protocols
HTTP/HTTPS, WebSocket, message queue protocols, and binary communication options.
_Source: [URL]_

### Data Formats and Standards
JSON, XML, Protobuf, MessagePack, and domain-specific exchange formats.
_Source: [URL]_

### System Interoperability Approaches
Point-to-point integration, API gateways, service mesh, enterprise service bus.
_Source: [URL]_

### Microservices Integration Patterns
Service discovery, circuit breaker, saga pattern, CQRS.
_Source: [URL]_

### Event-Driven Integration
Publish-subscribe, event sourcing, message brokers (Kafka, RabbitMQ), CQRS.
_Source: [URL]_

### Integration Security Patterns
OAuth 2.0, JWT, API key management, mutual TLS, data encryption.
_Source: [URL]_
```

**After generating content, present:**
> **Integration Patterns Analysis complete.**
> [C] Continue — Proceed to Architectural Patterns

🚫 Do not proceed until user selects [C].

---

## Step 4 — Architectural Patterns

**Goal:** Understand architectural patterns, design decisions, and system structure.

**Search the web for:**
- `[topic] system architecture patterns best practices`
- `[topic] software design principles patterns`
- `[topic] scalability architecture patterns`

**Document these sections:**

```markdown
## Architectural Patterns and Design

### System Architecture Patterns
Microservices, monolithic, serverless, event-driven, reactive, domain-driven design, cloud-native, and edge patterns with trade-offs.
_Source: [URL]_

### Design Principles and Best Practices
SOLID principles, clean architecture, hexagonal architecture, API design principles.
_Source: [URL]_

### Scalability and Performance Patterns
Horizontal vs vertical scaling, load balancing, caching strategies, distributed systems patterns.
_Source: [URL]_

### Integration and Communication Patterns
Architecture-level integration strategy and cross-service communication design.
_Source: [URL]_

### Security Architecture Patterns
Security-by-design principles, threat modeling, zero-trust, defense in depth.
_Source: [URL]_

### Data Architecture Patterns
Data modeling, event sourcing, CQRS, data lake vs warehouse, streaming.
_Source: [URL]_

### Deployment and Operations Architecture
Infrastructure as code, GitOps, observability patterns, SRE practices.
_Source: [URL]_
```

**After generating content, present:**
> **Architectural Patterns Analysis complete.**
> [C] Continue — Proceed to Implementation Research

🚫 Do not proceed until user selects [C].

---

## Step 5 — Implementation Research

**Goal:** Understand practical implementation approaches — adoption strategies, workflows, and operational practices.

**Search the web for:**
- `[topic] technology adoption strategies migration`
- `[topic] software development workflows tooling`
- `[topic] DevOps operations best practices`

**Document these sections:**

```markdown
## Implementation Approaches and Technology Adoption

### Technology Adoption Strategies
Migration patterns, gradual vs big-bang approaches, legacy modernization, vendor evaluation.
_Source: [URL]_

### Development Workflows and Tooling
CI/CD pipelines, code quality and review processes, collaboration tools.
_Source: [URL]_

### Testing and Quality Assurance
Testing strategies, frameworks, coverage approaches, QA practices.
_Source: [URL]_

### Deployment and Operations Practices
Monitoring, observability, incident response, infrastructure as code, security operations.
_Source: [URL]_

### Team Organization and Skills
Team structure, required skills, training paths, hiring considerations.
_Source: [URL]_

### Cost Optimization and Resource Management
Cost modeling, resource rightsizing, build vs buy decisions.
_Source: [URL]_

### Risk Assessment and Mitigation
Implementation risks, technical debt, vendor lock-in, migration risks.
_Source: [URL]_

## Technical Research Recommendations

### Implementation Roadmap
Phased approach and recommended sequencing.

### Technology Stack Recommendations
Preferred options based on research findings.

### Skill Development Requirements
Key skills and training to prioritize.

### Success Metrics and KPIs
How to measure success during and after implementation.
```

**After generating content, present:**
> **Implementation Research complete.**
> [C] Continue — Proceed to Research Synthesis

🚫 Do not proceed until user selects [C].

---

## Step 6 — Research Synthesis

Synthesize all findings into a comprehensive, authoritative final document with executive summary, narrative introduction, and strategic recommendations.

**Web search for additional synthesis context:**
- `[topic] future outlook trends`
- `[topic] significance importance`

**Final document structure to produce:**

```markdown
# [Compelling Title]: Comprehensive [topic] Technical Research

## Executive Summary

[2–3 paragraph summary of the most critical findings and strategic implications]

**Key Findings:**
- [Most significant technology landscape insights]
- [Critical architectural considerations]
- [Important implementation patterns]
- [Strategic implications]

**Strategic Recommendations:**
- [Top 3–5 actionable recommendations]

## Table of Contents

1. Research Introduction and Methodology
2. Technology Stack Analysis
3. Integration Patterns
4. Architectural Patterns and Design
5. Implementation Approaches
6. Strategic Synthesis and Recommendations
7. Future Outlook
8. Research Methodology and Sources

---

## 1. Research Introduction and Methodology

### Research Significance
[Why this technical research matters now, with current context]
_Source: [URL]_

### Research Methodology
- **Research Scope:** [Coverage areas]
- **Data Sources:** [Sources and verification approach]
- **Analysis Framework:** [Methodology used]
- **Time Period:** [Recency focus]

### Research Goals and Objectives
**Original Goals:** [goals]
**Achieved Objectives:** [what was answered]

---

## 2–5. [Synthesized content from Steps 2–5]

[Integrate and expand all prior research sections, adding cross-sectional insights and connections discovered during synthesis]

---

## 6. Strategic Synthesis and Recommendations

### Technology Landscape Summary
[2–3 sentences capturing the current technology state]

### Key Opportunities
Top 2–3 technology or implementation opportunities.

### Key Risks and Challenges
Top 2–3 risks or challenges to address.

### Recommended Technology Path
Concrete recommendations for technology choices and architecture.

### Implementation Roadmap
Phased approach with priorities and sequencing.

### Confidence Notes
Areas where data was limited, conflicting, or potentially outdated.

---

## 7. Future Outlook

### Near-term (1–2 years)
[Projections and implications]
_Source: [URL]_

### Medium-term (3–5 years)
[Expected developments]
_Source: [URL]_

### Long-term (5+ years)
[Strategic outlook]
_Source: [URL]_

---

## 8. Research Methodology and Sources

### Source Documentation
All primary and secondary sources used, with search queries.

### Research Quality Assurance
Source verification, confidence levels, and known limitations.

---

**Research Completion Date:** [date]
**Source Verification:** All facts cited with sources
**Confidence Level:** High — based on multiple authoritative sources
```

**After producing the complete document, present:**
> **Technical research synthesis complete!**
>
> The full research document has been saved.
> [C] Complete — Finalize and save the document

🚫 Do not finalize until user selects [C].